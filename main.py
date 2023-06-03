from typing import Annotated
from fastapi import FastAPI, UploadFile
import aiofiles

app = FastAPI()

base_files_dir = '/Users/lawrence/Desktop/works/dog_cats_app_backend/images'


@app.post('/classify')
async def classifyImage(image:  UploadFile):
    async with aiofiles.open(f"{base_files_dir}/{image.filename}", 'wb') as out_file:
        content = await image.read()
        await out_file.write(content)

    return {"message": "cat and dog classifier", "file": image}
