import final
from final import get_user_tz, get_user_task, create_to_do_list, create_db
from _pytest.monkeypatch import MonkeyPatch
from pytest import raises
import sqlite3 as mdb
import sqlite3

class TestInputs():
    def setup(self):
        self.monkeypatch = MonkeyPatch()

    def test_get_user_tz_invalid(self):
        with raises(SystemExit):
            # Exceeds max attempts and system exits due to misuse usage
            self.monkeypatch.setattr("builtins.input", lambda _: "Invalid Input")
            # Enters loop
            get_user_tz()


# Connects to the real Database but need to learn how to use LIMIT clause
def test_create_to_do_list():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    task_data = create_to_do_list("Hey", "6:00 AM")
    last_element = task_data.pop()
    assert last_element == ("Hey", "6:00 AM")
    cursor.execute("DELETE FROM tasks WHERE task = :completed_task", {"completed_task": "Hey"})
    connection.commit()

def test_database():
    db = create_db("Cooking", "21:20 PM")
    last_element = db.pop()
    assert last_element == ("Cooking", "21:20 PM")

def test_database_complete_task():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    db = create_db("Cooking", "21:20 PM")
    last_element = db.pop()
    cursor.execute("DELETE FROM tasks WHERE task = :completed_task", {"completed_task": "Cooking"})
    assert last_element != "cooking"
    connection.commit()







