from fastapi import FastAPI

app = FastAPI()


@app.post('/classify')
async def classifyImage():
    return {"message": "cat and dog classifier"}
