"""Low-level API wrapper for HabitRPG."""
from datetime import datetime
import json
from time import strptime, strftime
import requests


class HabitAPI(object):
    """Wrapper class for the HabitRPG API."""
    DIRECTION_UP = "up"
    DIRECTION_DOWN = "down"

    TYPE_HABIT = "habit"
    TYPE_DAILY = "daily"
    TYPE_TODO = "todo"
    TYPE_REWARD = "reward"

    def __init__(self, user_id, api_key, base_url="https://habitrpg.com/"):
        self.user_id = user_id
        self.api_key = api_key
        self.base_url = base_url

    def auth_headers(self):
        """Return dictionary of auth header keys."""
        return {
            "x-api-user": self.user_id,
            "x-api-key": self.api_key,
        }

    def request(self, method, path, *args, **kwargs):
        """Convenience method for API calls."""
        path = "%s/%s" % ("api/v2", path) \
            if not path.startswith("/") else path[1:]

        if "headers" not in kwargs:
            kwargs["headers"] = self.auth_headers()

        if "data" in kwargs:
            kwargs["data"] = json.dumps(kwargs["data"])
            kwargs["headers"]["Content-Type"] = "application/json"

        return getattr(requests, method)(self.base_url + path, *args, **kwargs)

    def user(self):
        """Return the full user object."""
        return self.request("get", "user").json()

    def reset_user(self):
        """Return the full user object."""
        return self.request("post", "user/reset").json()

    def tasks(self):
        """Return all the available tasks."""
        return self.request("get", "user/tasks").json()

    def task(self, task_id):
        """Return the specified task."""
        return self.request("get", "user/task/%s" % task_id).json()

    def create_todo(self, data):
        """Convenience function to create a todo."""
        return self.create_task(self.TYPE_TODO, **data)

    def create_task(self, task_type, **kwargs):
        """
        Create a task, defined by the HabitRPG TaskSchema.

        Defaults to creating a Todo, but can be changed by passing task_type.
        """
        kwargs.update({'type': task_type})
        return self.request("post", "user/tasks/", data=kwargs).json()

    def update_task(self, task_id, data):
        """Updates the specified task with provided data."""
        return self.request("put", "user/tasks/%s" % task_id, data=data).json()

    def delete_task(self, task_id):
        """Deletes the specified task."""
        return self.request("delete", "user/tasks/%s" % task_id).json()

    def perform_task(self, task_id, direction):
        """
        Performs the task, which means to score a daily or habit up or down,
        or mark a todo as completed.
        """
        url = "user/tasks/%s/%s" % (task_id, direction)

        return self.request("post", url).json()

    def sort_tags(self, start=0, stop=0):
        return self.request("post", "user/tags/sort?from=%d&to=%d".format(start, stop)).json()

    def add_tag(self, data):
        headers = self.auth_headers()
        headers['Content-Type'] = "application/json"

        response = self.request("post", "user/tags/", data=data, headers=headers).json()
        return response

    def edit_tag(self, id, data):
        headers = self.auth_headers()
        headers['Content-Type'] = "application/json"

        response = self.request("put", "user/tags/%s" % id, data=data, headers=headers).json()
        return response

    def delete_tag(self, id):
        headers = self.auth_headers()
        response = self.request("delete", "user/tags/%s" % id, headers=headers).json()
        return response


def convert_HRPG_datestring_to_datetime( s ):
    return datetime(*strptime(s[:19], "%Y-%m-%dT%H:%M:%S")[:6])

def convert_datetime_to_HRPG_datestring(t):
    return t.strftime("%Y-%m-%dT%H:%M:%S.000Z")
