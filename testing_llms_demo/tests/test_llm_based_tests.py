from pprint import pprint

from langchain.chat_models import ChatOpenAI
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain_core.prompts import PromptTemplate

from testing_llms_demo.llm import generate_job_description, prompt


def evaluate_llm_response(input_prompt, generated_response):
    evaluator_prompt = PromptTemplate.from_template(
        """You are an evaluator, focused on checking that Generated Response contains only key information that is present in Input Prompt 

          Here's an Input Prompt: {input_prompt} 
          Here's the Generated Response: {generated_response}

          Instruction: Return a valid JSON object with 4 keys: result (SATISFACTORY or NOT_SATISFACTORY), reason (explaining rationale for result), input_prompt, generated_response
          result must be SATISFACTORY only if Generated Response match all the responsibilities listed in Input Prompt 
          """
    )

    evaluator_runnable = evaluator_prompt | ChatOpenAI(model="gpt-4", temperature=0) | SimpleJsonOutputParser()
    evaluation_result = evaluator_runnable.invoke(
        {"input_prompt": input_prompt, "generated_response": generated_response})
    pprint(evaluation_result)

    return evaluation_result


def test_generate_job_description_includes_all_key_responsibilities():
    role = "Pet caretaker"
    responsibilities = ["feeding cats", "belly rubs for puppies"]
    input_prompt = prompt.format_prompt(role=role, responsibilities=responsibilities)

    job_description = generate_job_description(role=role, responsibilities=responsibilities)
    evaluation_result = evaluate_llm_response(input_prompt=input_prompt, generated_response=job_description)

    assert evaluation_result["result"] == "SATISFACTORY"


# intentionally simulate failure by adding 'feeding ducks' in the actual job description
def test_generate_job_description_when_generated_response_contains_info_not_present_in_prompt():
    # arrange
    role = "Pet caretaker"
    responsibilities = ["feeding cats", "belly rubs for puppies"]
    input_prompt = prompt.format_prompt(role=role, responsibilities=responsibilities)

    # act
    job_description = generate_job_description(role=role,
                                               responsibilities=responsibilities + ["feeding ducks and chicken"])

    # assert
    evaluation_result = evaluate_llm_response(input_prompt=input_prompt, generated_response=job_description)
    assert evaluation_result["result"] == "SATISFACTORY"
