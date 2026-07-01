from dataclasses import asdict

from sqlalchemy import select

from Viajei_api.models import User

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
