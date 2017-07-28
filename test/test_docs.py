import os
import pytest
from documents import Document, StringField, IntField, Records


class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(required=True)
    age = IntField()


@pytest.fixture
def user():
    User(email='name0@email.com', name='name0', age=10).save()
    User(email='name1@email.com', name='name1', age=20).save()
    User(email='name2@email.com', name='name2', age=30).save()
    User(email='name3@email.com', name='name2', age=30).save()
    User(email='name4@email.com', name='name2', age=30).save()
    User(email='name5@email.com', name='name2', age=40).save()
    User(email='name6@email.com', name='name2', age=50).save()
    User(email='name7@email.com', name='name2', age=60).save()
    User(email='name8@email.com', name='name2', age=70).save()

    yield None

    os.remove('user.json')


def test_document_creation(user):
    os.path.exists('user.json')


def test_doesnt_exist():
    assert User().objects(age=10) == []


def test_constraints(user):
    # test unique constraint
    assert User(email='name0@email.com', name='name0', age=10).save() is False

    # test required constraint
    assert User(name='name1').save() is False

    # test wrong type input for the integer
    assert User(email='name3@email.com', name='name3', age='10').save() is False


def test_query_multiple(user):
    results = User().objects(age=30)
    assert len(results) == 3
    assert results.count() == 3
    assert isinstance(results, list)
    assert isinstance(results, Records)


def test_query_first(user):
    first_result = User().objects(age=30).first()

    assert first_result['email'] == 'name2@email.com'
    assert first_result['name'] == 'name2'
    assert first_result['age'] == 30


def test_query_first_not_exist(user):
    first_result = User().objects(age=31).first()

    assert first_result is None
