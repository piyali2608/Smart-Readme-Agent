from fastapi import FastAPI, UploadFile, File
import zipfile
import shutil
import os

from app.tools import extract_project_text
from app.agents import generate_readme
from app.models import ReadmeResponse

app = FastAPI(title="Smart README AI Agent")

@app.post("/upload-project", response_model=ReadmeResponse)
async def upload_project(file: UploadFile = File(...)):

    upload_path = f"temp_{file.filename}"

    # Save uploaded zip
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract
    extract_folder = upload_path.replace(".zip", "")
    os.makedirs(extract_folder, exist_ok=True)

    with zipfile.ZipFile(upload_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    # Extract project content
    project_text = extract_project_text(extract_folder)

    # Generate README
    result = generate_readme(project_text)

    return {"generated_readme": result}
