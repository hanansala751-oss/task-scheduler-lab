import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def INSERT(self, task_name, priority):
        heapq.heappush(self.heap, (-priority, self.counter, task_name))
        self.counter += 1

    def EXTRACT_MAX(self):
        if not self.heap:
            return None
        neg_priority, _, task_name = heapq.heappop(self.heap)
        return task_name, -neg_priority

    def display(self):
        if not self.heap:
            print("Scheduler is empty")
            return
        for neg_p, _, name in sorted(self.heap):
            print(f"{name}: {-neg_p}")

if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.INSERT("Backup Database", 2)
    scheduler.INSERT("Render Video", 1)
    scheduler.INSERT("Handle User Request", 10)
    scheduler.INSERT("System Update", 5)

    scheduler.display()

    print("--- Executing ---")
    print(scheduler.EXTRACT_MAX())
    print(scheduler.EXTRACT_MAX())

    scheduler.display()