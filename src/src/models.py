from pydantic import BaseModel

class ReadmeResponse(BaseModel):
    generated_readme: str
