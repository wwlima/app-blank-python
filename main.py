from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def principal():
    return {"status": "on line"}

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)