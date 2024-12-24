import os
from fastapi import FastAPI, UploadFile, File
from app.scrap.skill_scrapper import process_file

def save_file(file_content: bytes, filename: str):
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(file_content)
    return filepath
app = FastAPI()
UPLOAD_DIR = "./uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)  

@app.post("/scrape")
async def scrape(file: UploadFile = File(...)):
    file_content = await file.read()
    filename = file.filename
    file_path = save_file(file_content, filename)
    result = await process_file(file_path)
    return result
