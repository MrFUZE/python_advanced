import logging
import random
import threading
import queue
import time
import pydantic

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


class Job(pydantic.BaseModel):
    priority: int
    value: int

    def get_job(self) -> tuple:
        return self.priority, self.value


class Producer(threading.Thread):

    def __init__(self, q: queue.PriorityQueue):
        super(Producer, self).__init__()
        self.q = q

    @classmethod
    def create_job(cls) -> list[Job]:
        job_list: list[Job] = []
        for p in range(10):
            job_list.append(Job(
                priority=p,
                value=random.randint(0, 2),
            ))
        return job_list

    def run(self) -> None:
        logger.info("Producer: Running")
        job_list = self.create_job()
        for job in job_list:
            self.q.put(job.get_job())
        while not self.q.empty():
            pass
        logger.info("Producer: Done")


class Consumer(threading.Thread):

    def __init__(self, q: queue.PriorityQueue):
        super(Consumer, self).__init__()
        self.q = q

    def run(self) -> None:
        logger.info("Consumer: Running")
        while job := self.q.get():
            logger.info(f"running: {job} sleep({job[1]})")
            time.sleep(job[1])
            self.q.task_done()
            if self.q.empty():
                logger.info("Consumer: Done")
                break


def main():
    q = queue.PriorityQueue(10)
    producer = Producer(q)
    consumer = Consumer(q)
    producer.start()
    consumer.start()
    q.join()
    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
