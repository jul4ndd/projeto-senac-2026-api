from dataclasses import asdict

from sqlalchemy import select

from Viajei_api.models import User, Story

def test_creat_user(session, mock_db_time):
    with mock_db_time(model=user) as time:
        new_user = User("julie@test.test", "senha123")

        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.email == "julie@test.test"))


    assert user.email == "julie@test.test"

    assert asdict(user) == {
        'id': 1, 
        'password': 'senha123',
        'email': 'julie@test.test', 
        'created_at': time
    }

def test_create_story(session, mock_db_time, user):
    with mock_db_time as time:
        new_story = Story(author="jj", title="Titulo", story="Era uma vez...")

        new_story.email = user.email

        session.add(new_user)
        session.commit()

    user = session.scalar(select(Story).where(Story.author == "jj"))

    assert asdict(story) == {
        "id": 1,
        "author": "jj",
        "title": "Titulo", 
        "email": "example@example.com",
        "story": "era uma vez...",
        "created_at": time

}