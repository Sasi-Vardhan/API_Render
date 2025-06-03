from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import fitz 

app = FastAPI()

UPLOAD_DIR = Path("uploaded_pdfs")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.api_route("/", methods=["GET", "POST"])
async def read_root(file: UploadFile = File(None)):
    if file:
        contents = await file.read()

        # Open PDF from bytes
        pdf = fitz.open(stream=contents, filetype="pdf")

        # Extract text from the first page
        first_page = pdf[2]
        text = first_page.get_text()

        return {"first_page_text": text.strip()}
    return {"message": "Hello, FastAPI!"}