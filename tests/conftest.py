import pytest

from ecommerce.user.models import User


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute assert before and after a test in run"""

    from conf_test_db import override_get_db
    database = next(override_get_db())
    new_user = User(name='Nikola', email='nmatijas@outlook.com', password='test1234')
    database.add(new_user)
    database.commit()

    yield

    #teardown
    database.query(User).filter(User.email == 'nmatijas@outlook.com').delete()
    database.commit()

