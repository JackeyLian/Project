import sqlite3
import pytz
import time
from sys import exit
from re import search 
from tabulate import tabulate
from datetime import datetime
from sys import exit
 
 
# Classes can be used so the program doesn't get messy with many of the same related functions
 
class DataBase():
    def __init__(self, task, user_dt):
        self.task = task
        self.user_dt = user_dt
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
        cursor.execute("DELETE FROM tasks WHERE task = :completed_task", {"completed_task": self.completed_task})
        connection.commit()
 
def main():
    while True:
        to_do_list = create_to_do_list()
        print(tabulate(to_do_list, headers=["Tasks", "Time Added"], tablefmt="github"))
        user_input = input("(C) Complete Task\n(C) Input: ")
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
                    time.sleep(2)
        else: 
            print("Please input a valid task")
            time.sleep(2)
 

def create_to_do_list():
    user_dt = get_user_tz()
    task = get_user_task()
    to_do_list = create_db(task, user_dt)
    return to_do_list
 
 
def get_user_tz():
    max_attempts = 3
    while True:
        user_input = input("What is your timezone?\nH for help\nInput: ").strip()
        if user_input in pytz.common_timezones:
            utc_dt = datetime.now()
            user_dt = pytz.timezone(user_input)
            fmt = '%Y-%m-%d %H:%M:%S %Z'
            user_dt = utc_dt.astimezone(user_dt).strftime(fmt)
            return user_dt
        elif user_input == "H":
            print("e.g. America/New_York, America/Los_Angeles, America/Detroit, etc.")
            time.sleep(2)
        elif max_attempts == 3:
            exit("Invalid Usage")
        else:
            max_attempts -= 1 

 
 
def get_user_task():
    max_attempts = 3
    while True:
        task = input("Task: ")
        if task:
            return task
        elif max_attempts == 3:
            exit("Invalid Usage")
        else:
            max_attempts += 1
            print("Please input a task")
            time.sleep(2)
 
 
def create_db(task, user_dt):
    db = DataBase(task, user_dt)
    data = db.get_data()
    return data
 
 
 
if __name__ == "__main__":
    main()