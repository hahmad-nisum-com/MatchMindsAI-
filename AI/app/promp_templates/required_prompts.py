
skill_extraction_prompt = """
    Please summarize the following document. Return the extracted data as key-value pairs in a JSON object only. Do not add any explanations, comments, or additional information.
    - name: Full name of the person (string)
    - email: Email address (string)
    - skills: A list of skills (list of strings)
    - tech_stack: A list of programming languages, tools, or frameworks (list of strings)
    - certifications: List of certifications (if available, or null if none) (list of strings)
    - experience: A list of objects containing:
        - company: Name of the company (string)
        - tenure: Employment tenure, always return the dates in the following format:
            - If the date is "Month YYYY", return it as "MM/YYYY" (e.g., "June 2022" → "06/2022")
            - If the date range includes months, return it as "MM/YYYY - MM/YYYY" (e.g., "May 2021 – April 2022" → "05/2021 - 04/2022")
            - If the date is "Present", return it as "MM/YYYY - Present" (e.g., "Sep 2022 – Present" → "09/2022 - Present")
    - education: A list of degrees or educational qualifications (list of strings)
    - total_experience: 1 (float)
    Here is the text to extract from:

    {text}

    """
skill_grading_prompt="""
    Input:
    CV Content: {text}
    Skills List: {skills}
    Experience List: {experience}

    Objective:
    Analyze the CV content to determine the tenure (number of years/months) the employee has worked with each skill listed in the Skills List.
    For each entry in the Skills List, the model should:
    Search the CV Content for mentions of the skill (e.g., specific technologies, tools, or languages).
    Extract the related work experience (years/months) associated with each mention of the skill.
    Based on the information, calculate and store the total experience in Experience List for each skill.
   
    Steps:
    Parse the CV Content and identify all instances where a skill from the Skills List is mentioned.
    For each skill found, extract the date range or work duration (tenure) provided in the CV.
    Accumulate the experience for each skill based on the identified tenure. If the CV does not specify the exact months or years of experience, assume a default value (e.g., 1 year).
    Store the calculated experience in the Experience List, associating it with the correct skill.
    
    Note: return an array of object containing skills and their level like key value pairs. donot explain anything just return json.
    """
job_requirement_prompt = """
    Input:
    Job content: {text}
    Task: 
    You are an AI model tasked with assessing the required information about job posting .
    - Analyze the job content and identify the required skills and experiences.
    - Analyze the job content and identify the required experience.
    Only return skills and required experience nothing more and donot explain any thing

"""
job_matching_prompt = """
    Input:
    required Skills and experience: {required_content}
    Skills List with experience: {skills}
    Total Experience: {total_experience}
    
    Task: 
    You are an AI model tasked with assessing the match between the job requirements and Skills provided.
    - Analyze the required job skills and employee skills list provided.
    - return the match score by matching the job requirements and skills of employee
    Response:
    - Match Score: match score%
"""