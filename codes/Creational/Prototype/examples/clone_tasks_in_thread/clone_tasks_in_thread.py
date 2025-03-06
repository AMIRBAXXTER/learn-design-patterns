import threading
import time
import copy
from abc import ABC, abstractmethod
import queue
import random


# Prototype Interface
class TaskPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def run(self):
        pass


# Concrete Prototype: Image Processing
class ImageProcessingTask(TaskPrototype):
    def __init__(self, image_path):
        self.image_path = image_path
        self.metadata = self.load_metadata(image_path)  # Simulate loading metadata

    def load_metadata(self, image_path):
        # Simulate fetching metadata from database or file
        time.sleep(0.2)
        return {"resolution": "3000x2000", "format": "JPEG"}

    def clone(self):
        return copy.deepcopy(self)

    def run(self):
        print(
            f"Thread: {threading.current_thread().name} | Processing image: {self.image_path} with metadata: {self.metadata}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate image processing


# Concrete Prototype: Email Sending
class EmailTask(TaskPrototype):
    def __init__(self, recipient, subject, message):
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.template = self.load_template()

    def load_template(self):
        # Simulate loading email template from file
        time.sleep(0.1)
        return "<div>...Email Template...</div>"

    def clone(self):
        return copy.deepcopy(self)

    def run(self):
        print(
            f"Thread: {threading.current_thread().name} | Sending email to: {self.recipient} with subject: {self.subject}")
        time.sleep(random.uniform(0.1, 0.3))  # Simulate sending email


# Thread Pool class
class ThreadPool:
    def __init__(self, num_threads):
        self.task_queue = queue.Queue()
        self.threads = []
        self.num_threads = num_threads

        for i in range(num_threads):
            thread = threading.Thread(target=self._worker, name=f"Thread-{i + 1}")
            self.threads.append(thread)
            thread.daemon = True  # Exit program when all tasks are done
            thread.start()

    def add_task(self, task):
        self.task_queue.put(task)

    def _worker(self):
        while True:
            task = self.task_queue.get()
            try:
                task.run()
            except Exception as e:
                print(f"Error running task: {e}")
            finally:
                self.task_queue.task_done()

    def wait_completion(self):
        self.task_queue.join()  # Wait for all tasks to complete


if __name__ == "__main__":
    # Create a Thread Pool with 4 threads
    pool = ThreadPool(num_threads=4)

    # Create prototype image processing task
    image_task_prototype = ImageProcessingTask(image_path="image1.jpg")

    # Create prototype email task
    email_task_prototype = EmailTask(recipient="user@example.com", subject="Hello", message="Welcome!")

    # Add tasks to the Thread Pool
    for i in range(5):
        # Clone image processing task and add it to the queue
        task = image_task_prototype.clone()
        task.image_path = f"image{i + 1}.jpg"  # Modify specific property
        pool.add_task(task)

        # Clone email task and add it to the queue
        task = email_task_prototype.clone()
        task.recipient = f"user{i + 1}@example.com"  # Modify specific property
        pool.add_task(task)

    # Wait for all tasks to complete
    pool.wait_completion()

    print("All tasks completed.")
