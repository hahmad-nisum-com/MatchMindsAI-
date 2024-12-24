
from datetime import datetime
import os
from langchain.prompts import PromptTemplate
from app.utils import extract_text_from_pdf,calculate_experience,extraxt_text_from_file
from dotenv import load_dotenv
from langchain_google_vertexai import VertexAI
from app.promp_templates.required_prompts import skill_extraction_prompt,skill_grading_prompt,job_requirement_prompt,job_matching_prompt
from app.model.user_profile import  UserProfile
from langchain.output_parsers import PydanticOutputParser
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
llm = VertexAI(model_name="gemini-pro")


# Get current date (without time)

async def process_file(file_path):
    # Extract text from the uploaded PDF file
    print("-----------------------file recieved------------------------")
    text = extract_text_from_pdf(file_path)
    job_text=extraxt_text_from_file('app/data/jobs.txt')
    print(job_text)
    print("----------------------extracting data-----------------------")
    current_date = datetime.today()
    prompt_template = PromptTemplate(input_variables=["text","current_date"], template=skill_extraction_prompt)
    parser=PydanticOutputParser(pydantic_object=UserProfile)
    chain = prompt_template | llm | parser
    print("----------------------Getting Information-----------------------")
    cleaned_response = chain.invoke({"text": text,"current_date":current_date})
    print("----------------------Calculating Experience-----------------------")
    calculated_Experience= calculate_experience(cleaned_response.experience)
    cleaned_response.total_experience=calculated_Experience
    print('grading skills')
    grading_skills_prompt=PromptTemplate(input_variables=['text','skills',], template=skill_grading_prompt)
    grading_chain=grading_skills_prompt|llm
    result=grading_chain.invoke({"text":text,'skills':cleaned_response.skills,'experience':cleaned_response.experience})
    print(result)
    job_requirement_promt_template=PromptTemplate(input_variables=['text'], template=job_requirement_prompt)
    grading_chain=job_requirement_promt_template|llm
    job_requirements=grading_chain.invoke({"text":job_text})
    print(job_requirements)
    job_requirement_promt_template=PromptTemplate(input_variables=['text'], template=job_requirement_prompt)
    requirement_chain=job_requirement_promt_template|llm
    job_requirements=requirement_chain.invoke({"text":job_text})
    job_matching_prompt_=PromptTemplate(input_variables=['required_content','skills','total_experience'], template=job_matching_prompt)
    matching_chain=job_matching_prompt_|llm
    matching_resiult=matching_chain.invoke({"required_content":job_requirements,'skills':result,'total_experience':cleaned_response.total_experience})
    print(matching_resiult)
    print("------------------------result-----------------------------------")

    return cleaned_response
