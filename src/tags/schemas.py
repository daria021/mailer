from pydantic import BaseModel, ConfigDict


class TagUpdate(BaseModel):
    text: str
    model_config = ConfigDict(from_attributes=True)


class TagCreate(TagUpdate):
    text: str


class TagResponse(TagCreate):
    id: int
    text: str


class TagFilter(BaseModel):
    text: str
