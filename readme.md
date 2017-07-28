# Purpose

To create a database-like access to data without all the fuss of a
database.  Similar idea to TinyDB, but with a direct implementation
that emulates that of MongoEngine.

# Maturity

As this is based on MongoEngine, the interface is not likely to
change.  Any elements that are in-place will likely remain in place
and working.

I am committed to a high degree of testing (see `/tests`), meaning
greater than 90% coverage.  At the time of this writing, there is 100%
test coverage.

# Use

As this is an attempt to emulate MongoEngine, the 
[Mongine Documentation](http://docs.mongoengine.org/index.html)
is the guide.  All elements of MongoEngine are not implemented, 
but all elements that are implemented should work the same as
those options in MongoEngine.

## Basic Example

```python 
from documents import Document, StringField, IntField

# create a 'User' class
class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(required=True)
    age = IntField()
    
# enter a few documents
User(email='name0@email.com', name='name0', age=10).save()
User(email='name1@email.com', name='name1', age=20).save()
User(email='name2@email.com', name='name2', age=30).save()
User(email='name3@email.com', name='name2', age=30).save()
User(email='name4@email.com', name='name2', age=30).save()
User(email='name5@email.com', name='name2', age=40).save()
User(email='name6@email.com', name='name2', age=50).save()
User(email='name7@email.com', name='name2', age=60).save()
User(email='name8@email.com', name='name2', age=70).save()

# you can also create a document in this way
user = User(email='name8@email.com', name='name2', age=70)
user.save()

# make some queries
results = User().objects(age=30)
num_of_records = results.count()

first_result = User().objects(age=30).first()
first_result_email = first_result['email']
```

# How it Works

For every document that is created, a corresponding `.json` file 
is created which contains that document's data.  For instance,
the `User` class in the above example creates a `user.json` file.
