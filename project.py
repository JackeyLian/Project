import sqlite3
import time
import pytz
from pytz import common_timezones
from sys import exit
from tabulate import tabulate
from datetime import datetime


# Classes can be used so the program doesn't get messy with many of the same related functions
class DataBase():
    def __init__(self, task, user_dt):
        self.task = task
        self.user_dt = user_dt

    def insert_data(self):
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()
        # Data types could be used to specify | e.g. text, integer, char
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task text, time)")
        cursor.execute("INSERT INTO tasks VALUES (:task, :time)", {"task": self.task, "time": self.user_dt})
        connection.commit()

    def get_data(self):
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        data = cursor.fetchall()
        return data


class CompleteTask():
    def __init__(self, completed_task):
        self.completed_task = completed_task

    @staticmethod
    def get_task():
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()
        cursor.execute("SELECT task FROM tasks")
        task_data = cursor.fetchall()
        return task_data

    def complete_task(self):
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()
        # Remove data specifying where the task completed was in the Clause
        # cursor.execute(f"DELETE FROM tasks where task = {completed_task}")
        cursor.execute("DELETE FROM tasks WHERE task = :completed_task", {"completed_task": self.completed_task})
        connection.commit()

def main():
    while True:
        task = get_user_task()
        timezone = get_user_tz()
        to_do_list = create_to_do_list(task, timezone)
        print(tabulate(to_do_list, headers=["Tasks", "Time Added"], tablefmt="github"))
        user_input = input("(C) Complete Task\n(F) Exit Program\nTask Input: ").upper()
        if user_input == "C":
            task_data = CompleteTask.get_task()
            loop = True
            while loop:
                user_input = input("Completed Task: ")
                completed_task = CompleteTask(user_input)
                for task in task_data:
                    if user_input in task:
                        completed_task.complete_task()
                        loop = False
                        break
                    else:
                        print("Please input a valid task")
        elif user_input == "F":
            exit("To-Do List exited")
        else:
            print("Input another task.")
            time.sleep(2)

def get_user_task():
    max_attempts = 3
    while True:
        task = input("Task: ")
        if task:
            return task
        elif max_attempts == 0:
            exit("Improper usage of program")
        else:
            print("Please input a task")
            max_attempts -= 1

def get_user_tz():
    max_attempts = 3
    while True:
        user_input = input("What is your timezone?\nH for help\nInput: ").strip()
        if user_input in common_timezones:
            utc_dt = datetime.now()
            user_dt = pytz.timezone(user_input)
            fmt = '%Y-%m-%d %H:%M:%S %Z'
            user_dt = utc_dt.astimezone(user_dt).strftime(fmt)
            return user_dt
        elif user_input == "H":
            print("e.g. America/New_York, America/Los_Angeles, America/Detroit, etc.")
            time.sleep(2)
        elif max_attempts == 0:
            exit("Improper usage of program")
        else:
            print("Ask for help?")
            max_attempts -= 1

def create_to_do_list(task, timezone):
    task_data = create_db(task, timezone)
    # Returns data from Database to be printed in tabulate
    return task_data

def create_db(task, timezone):
    # Creates the Database for the To-do-list
    db = DataBase(task, timezone)
    db.insert_data()
    # Gets data from Sqlite3 for tabulate print out on CLI
    data = db.get_data()
    return data

if __name__ == "__main__":
    main()