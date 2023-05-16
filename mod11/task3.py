import logging
import random
import threading
import time

TOTAL_TICKETS = 10
THRESHOLD = 3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore, dir_semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.dir_sem = dir_semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')
                if TOTAL_TICKETS == THRESHOLD:
                    self.dir_sem.release()
                    logger.info('Director started printing tickets')
                    self.dir_sem.acquire()
        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

class Director(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore, dir_semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.dir_sem = dir_semaphore
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        while True:
            self.dir_sem.acquire()
            if TOTAL_TICKETS >= THRESHOLD:
                self.dir_sem.release()
                continue
            logger.info('Director is printing tickets')
            time.sleep(random.randint(1, 3))
            new_tickets = random.randint(1, 10)
            TOTAL_TICKETS += new_tickets
            logger.info(f'Director printed {new_tickets} tickets; total tickets {TOTAL_TICKETS}')
            self.dir_sem.release()
            with self.sem:
                self.sem.release()
                self.sem.release()
                self.sem.release()
            if TOTAL_TICKETS >= 10:
                break

def main():
    semaphore = threading.Semaphore(3)
    dir_semaphore = threading.Semaphore(0)
    sellers = []

    for _ in range(3):
        seller = Seller(semaphore, dir_semaphore)
        seller.start()
        sellers.append(seller)

    director = Director(semaphore, dir_semaphore)
    director.start()

    for seller in sellers:
        seller.join()

    director.join()

if __name__ == '__main__':
    main()
