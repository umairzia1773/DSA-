import random as r

class PrinterQueue:
    def __init__(self):
        self.queue = []
        self.printer_is_free = True
        self.printer_doing_task = None
        self.tick = 0

    def add_task(self, pages):
        self.queue.append(pages)
        print(f"At tick {self.tick}, task {len(self.queue)} of {pages} pages received for printing.")

    def Print_the_Papers(self):
        if not self.printer_is_free:
            return

        if self.queue:
            self.printer_doing_task = self.queue.pop(0)
            self.printer_is_free = False
            print(f"At tick {self.tick}, task {len(self.queue) + 1} starts printing.")

    def tick_tick(self):
        self.tick += 1
        RN = r.randint(10, 100)
        if RN % 5 == 0 or RN % 13 == 0 or RN % 67 == 0:
            pages = RN % 61
            self.add_task(pages)
        if not self.printer_is_free:
            self.printer_doing_task -= 1
            if self.printer_doing_task <= 0:
                print(f"At tick {self.tick}, task {len(self.queue) + 1} completed.")
                self.printer_is_free = True
        self.Print_the_Papers()

def main():
    printer = PrinterQueue()
    for i in range(150):
        printer.tick_tick()
main()
