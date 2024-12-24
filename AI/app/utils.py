import io
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader
import re
from langchain_community.document_loaders import TextLoader

def extraxt_text_from_file(file_path):
    loader=TextLoader(file_path)
    documents=loader.load()
    result=""
    for doc in documents:
        cleaned_content = " ".join(doc.page_content.split())
        # Add cleaned content to the result
        cleaned_text = re.sub(r'[\uF000-\uFFFF]', '', cleaned_content)
        result += cleaned_text+ "\n"
    return result
def extract_text_from_pdf(file_path):
    # Convert bytes to file-like object
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    # Check the first document's text
    result=""
    for doc in documents:
        cleaned_content = " ".join(doc.page_content.split())
        # Add cleaned content to the result
        cleaned_text = re.sub(r'[\uF000-\uFFFF]', '', cleaned_content)
        result += cleaned_text+ "\n"
    return result


def calculate_experience(experience_data):
    total_years = 0
    today = datetime.today()
    
    for job in experience_data:
        company = job.company
        start_date = datetime.strptime(job.tenure.split(' - ')[0], '%m/%Y')
        
        # Determine end date: if it's "Present", use today's date
        if 'Present' in job.tenure or "Current" in job.tenure:
            end_date = today
        else:
            end_date = datetime.strptime(job.tenure.split(' - ')[1], '%m/%Y')
        
        delta_years = end_date.year - start_date.year
        delta_months = end_date.month - start_date.month
        
        if delta_months < 0:
            delta_years -= 1
            delta_months += 12
        
        # Convert to decimal (years + months/12)
        total_years += delta_years + (delta_months / 12)

    return round(total_years, 2)
