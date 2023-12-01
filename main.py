from testing_llms_demo.llm import generate_job_description

result = generate_job_description(role="Lead Analyst",
                                  responsibilities=["stakeholder management", "building high-performing teams",
                                                    "communications", "BigQuery", "Tableau"])
print(result)
