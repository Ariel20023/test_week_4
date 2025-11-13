import uvicorn
import pydantic
if __name__ == "__main__":
    uvicorn.run("APP.app:app", reload=True)



