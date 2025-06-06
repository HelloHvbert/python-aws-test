import threading
import time

people = [
    {"first_name": "John", "last_name": "Black", "age": 30},
    {"first_name": "Michael", "last_name": "Johnsson", "age": 13},
    {"first_name": "Mery", "last_name": "Hunter", "age": 60},
    {"first_name": "Chris", "last_name": "Williams", "age": 45},
]


class Person:
    people_count = 0
    lock = threading.Lock()

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        # == to =, == is used for comparing
        self.age = age
        self.id = self.increase_count()

    # This method should not be modified.
    def introduce(self):
        time.sleep(1)
        print(f"Hello, my first name is {self.first_name} and I am {self.age} years old.")

    @classmethod
    def increase_count(cls):
        with cls.lock:
            cls.people_count += 1
            return cls.people_count


def main():
    threads = []
    for p in people:
        # wrong order, should be first_name, last_name, age
        x = Person(p["first_name"], p["last_name"], p["age"])
        threads.append(threading.Thread(target=x.introduce))

    for thread in threads:
        thread.start()
    # Waiting for all threads
    for t in threads:
        t.join()

    print(f"Number of people created: {Person.people_count}")
    return


# main -> __main__
if __name__ == "__main__":
    main()
