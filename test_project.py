import project
from project import get_user_tz, get_user_task, create_to_do_list, create_db
from _pytest.monkeypatch import MonkeyPatch
from pytest import raises
import sqlite3

class TestInputs():
    def setup_method(self):
        self.monkeypatch = MonkeyPatch()

    def test_get_user_tz_invalid(self):
        with raises(SystemExit):
            # Sets up the input for lanmbda to be "Invalid Input" by assigning through Monkeypatch
            # Exceeds max attempts and system exits due to misuse usage
            self.monkeypatch.setattr("builtins.input", lambda _: "Invalid Input")
            # Enters loop
            get_user_tz()

    def test_get_user_task(self):
        with raises(SystemExit):
            self.monkeypatch.setattr("builtins.input", lambda _: "")
            get_user_task()


# Connects to the Database used by the User
def test_create_to_do_list():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    task_data = create_to_do_list("Hey", "6:00 AM")
    # Pops the last element in the sqlite3 database list which is suppose to be ("Hey", "6:00 AM")
    last_element = task_data.pop()
    # Asserts that the last element assigned is the inputted value and that there is connection,
    # between Sqlite3 and the program.
    assert last_element == ("Hey", "6:00 AM")
    # Delete the inputted value which was "Hey" and commits the changes, removing "Hey".
    cursor.execute("DELETE FROM tasks WHERE task = :completed_task", {"completed_task": "Hey"})
    connection.commit()

def test_database():
    # Test that the database connects and inserts the value "This is not a task"
    db = create_db("This is not a task", "21:20 PM")
    last_element = db.pop()
    assert last_element == ("This is not a task", "21:20 PM")

def test_database_complete_task():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    db = create_db("This is not a task", "21:20 PM")
    last_element = db.pop()
    cursor.execute("DELETE FROM tasks WHERE task = :completed_task", {"completed_task": "This is not a task"})
    # Asserts that the database completes the task "This is not a task" and eliminates it from the to-do list
    assert last_element != "This is not a task"
    connection.commit()
    # Ending the pytest, the connection between the tasks.db and the pytest closes. Ending the test session.
    connection.close()







