from pydantic import baseModel

class StorySchema(BaseModel):
    name: str
    title: str
    email: str
    story: str

class StoryDB(StorySchema):
    id: int

class StoryPublic(BaseModel):
    id: int
    title: str
    email: str