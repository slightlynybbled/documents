import logging
from documents import Document, StringField, IntField

logger = logging.getLogger('documents.testing')
logging.basicConfig(level=logging.DEBUG)


class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(required=True)
    age = IntField()

# multi-line save example
user = User(email='you@me.com')
user.name = 'j'
user.save()

# single-line save example
User(email='you@you.com', name='k', age=22).save()
User(email='you1@you.com', name='k', age=23).save()
User(email='you2@you.com', name='k', age=24).save()
User(email='you30@you.com', name='k', age=25).save()
User(email='you31@you.com', name='k', age=25).save()
User(email='you32@you.com', name='k', age=25).save()
User(email='you4@you.com', name='k', age=26).save()
User(email='you5@you.com', name='k', age=27).save()

for user in User().objects(name='k', age=25):
    logger.info(user)
