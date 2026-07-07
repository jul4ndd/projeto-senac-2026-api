from viajei_api.schemas.user import User


class StorySchema(baseModel):
    name: str
    title: str
    email = User.email
    body: str
