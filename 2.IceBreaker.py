#from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os
from third_party.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
##    load_dotenv()

    env_variable_value = os.getenv('OPENAI_API_KEY')



    ## Prompt to be used in the Prompt Template
    summary_template = """
    Given the Linkedin information {information} about a person, I want you to create:

    1. A title in capital. 
    2. A short summary.
    3. Two interesting facts about the person. 
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template= summary_template)

    print(" ==================================\n")

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data= scrape_linkedin_profile(linkedin_profile_url='https://gist.githubusercontent.com/rabocse/6cf6dc6808f5abf983acdb4e5f6dba03/raw/3b8132051891134ce4e4cfc97912d1ee107f9463/scrapedLinkedinProfile.json')  

    res = chain.invoke(input={"information":linkedin_data})

    print(res["text"])