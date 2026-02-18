from fastapi import FastAPI, UploadFile
import shutil

from parser import parse_pdf
from analyzer import summarize

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile):

    path = file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = parse_pdf(path)

    result = summarize(df)

    return result
