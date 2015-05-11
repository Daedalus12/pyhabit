from itertools import compress
from datetime import datetime
from api import convert_HRPG_datestring_to_datetime
from pyhabit import HabitAPI
from uuid import uuid1 as uuid


class Attribute(object):
    Strength, Constitution, Perception, Intelligence = range(4)

    @classmethod
    def fromString(cls, s):
        if   s.lower()[:3] == "str" : return Attribute.Strength
        elif s.lower()[:3] == "con" : return Attribute.Constitution
        elif s.lower()[:3] == "per" : return Attribute.Perception
        elif s.lower()[:3] == "int" : return Attribute.Intelligence

class User(object):
    def __init__(self, user_id, token):
        self._api = HabitAPI(user_id, token)

        resp = self._api.user()
        self.tags = Tag.fromDictList(resp['tags'])
        self.todos = ToDo.fromDictList(resp['todos'])


    def reset(self):
        self._api.reset_user()

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
        self._api.add_tag(tag.toDict())

    def updateTag(self, tag):
        self._api.edit_tag(tag.id, tag.toDict())

    def deleteTag(self, tag):
        self._api.delete_tag(tag.id)


class Tag(object):
    def __init__(self, name=''):
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
        return {'id': self.id, 'name': self.name}

    @classmethod
    def fromDictList(cls, dict_list):
        tags = {}
        for d in dict_list:
            tag = cls.fromDict(d)
            tags[tag.id] = tag
        return tags


class _Task(object):
    def __init__(self):
        self.text = ""
        self.notes = ""
        self.id = uuid()
        self.attribute = Attribute.Strength
        self.priority = 1
        self.value = 0
        self.tags = []
        self.challenge = []
        self.dateCreated = datetime.now()

    @classmethod
    def fromDict(cls, d):
        task = _Task()
        task.text = d['text']
        task.notes = d['notes']
        task.id = d['id']
        task.attribute = Attribute.fromString(d['attribute'])
        task.priority = d['priority']
        task.value = d['value']
        task.tags = list(compress(d['tags'].keys(), d['tags'].items()))
        # task.challenge = []
        task.dateCreated = convert_HRPG_datestring_to_datetime(d['dateCreated'])
        return task

class ToDo(_Task):

    class Item(object):
        def __init__(self):
            self.id = uuid()
            self.text = ""
            self.completed = False

        @classmethod
        def fromDict(cls, d):
            i = ToDo.Item()
            i.id = d['id']
            i.text = d['text']
            i.completed = d['completed']
            return i

    def __init__(self):
        super(ToDo, self).__init__()
        self.completed = False
        self.checklist = []

    @classmethod
    def fromDict(cls, d):
        tk = super(ToDo, cls).fromDict(d)
        td = ToDo()

        for key, val in  tk.__dict__.iteritems():
            td.__dict__[key] = tk.__dict__[key]

        for item in d['checklist']:
            td.checklist.append(ToDo.Item.fromDict(item))
        return td


    @classmethod
    def fromDictList(cls, dict_list):
        todos = {}
        for d in dict_list:
            todo = cls.fromDict(d)
            todos[todo.id] = todo
        return todos
