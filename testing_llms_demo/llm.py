from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

prompt = PromptTemplate.from_template(
    """You are an assistant that helps with generating job descriptions. 
      You will only generate job descriptions based on inputs provided, and not add any unnecessary or untruthful information

      Here's a list of responsibilities for the role of {role}: 
      {responsibilities}

      Instruction: Generate a job description for the given role; clearly list expectations for each responsibility area."""
)


def generate_job_description(role, responsibilities):
    runnable = prompt | OpenAI() | StrOutputParser()
    result = runnable.invoke({"role": role, "responsibilities": responsibilities})

    return result
