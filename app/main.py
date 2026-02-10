from fastapi import FastAPI, UploadFile, File, Depends
import shutil
import uuid

from app.parser import parse_pdf
from app.categorizer import categorize
from app.insights import summary

app = FastAPI(title="Financial Insights API")

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    file_path = f"uploads/{uuid.uuid4()}.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = parse_pdf(file_path)

    df["Category"] = df["Description"].apply(categorize)

    result = summary(df)

    return result
