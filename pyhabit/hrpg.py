from pyhabit import HabitAPI
from uuid import uuid1 as uuid

class User(object):

    def __init__(self, user_id, token):
        self._api = HabitAPI( user_id, token )

    def reset(self):
        self._api.reset_user( )

    def getTags(self):
        response = self._api.sort_tags()
        tags = {}
        for item in response:
            tag = Tag.fromDict(item)
            tags[tag.id] = tag
        return tags

    def createTag(self, name):
        return Tag(name)

    def addTag(self, tag):
        self._api.add_tag( tag.toDict() )

    def updateTag(self, tag):
        self._api.edit_tag( tag.id, tag.toDict())

    def deleteTag(self, tag):
        self._api.delete_tag( tag.id )

class Tag(object):

    def __init__(self, name = ''):
        self.name = name
        self.id = str(uuid())

    @staticmethod
    def fromDict(item):
        tag = Tag()
        tag.id = item['id']
        try:
            tag.name = item['name']
        except KeyError:
            tag.name = ''
        return tag

    def toDict(self):
        return {'id':self.id, 'name':self.name }