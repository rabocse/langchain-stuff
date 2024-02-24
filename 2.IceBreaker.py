#from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os
from third_party.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    #load_dotenv()

    # env_variable_value = os.getenv('OPENAI_API_KEY')

    # information = """
    #     The person needs a device that can offer network perimeter security. 
    #     It needs to run in routed mode and provide stateful packet filtering.
    #     Layer 7 inspections are a must.
    #     It should support some kind of centralized management since the person needs to manage multiple branches.
    # """


    # ## Prompt to be used in the Prompt Template
    # summary_template = """
    # Given the Linkedin information {information} about a requirement from a network engineer, I want you to create:

    # 1. A short summary of a Cisco solution that could help for such requirement.
    # 2. Additional features (two or three is fine) from the chosen Cisco solution.
    # """

    # summary_prompt_template = PromptTemplate(input_variables=["information"], template= summary_template)



    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # res = chain.invoke(input={"information": information})

    # print(res)

    linkedin_data= scrape_linkedin_profile(linkedin_profile_url='https://gist.githubusercontent.com/rabocse/6cf6dc6808f5abf983acdb4e5f6dba03/raw/40041968fc633f3a38a5ea95155ffa5f01a63eb6/scrapedLinkedinProfile.json')

    print(linkedin_data.json())