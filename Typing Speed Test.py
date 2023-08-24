import tkinter as tk
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text_to_type = "The quick brown fox jumps over the lazy dog."
        self.current_input = tk.StringVar()
        self.timer_running = False
        self.start_time = 0

        self.setup_ui()

    def setup_ui(self):
        self.label_text = tk.Label(self.root, text=self.text_to_type, wraplength=300)
        self.label_text.pack(pady=10)

        self.entry_input = tk.Entry(self.root, textvariable=self.current_input)
        self.entry_input.pack(pady=5)

        self.label_timer = tk.Label(self.root, text="Time: 0s")
        self.label_timer.pack()

        self.label_accuracy = tk.Label(self.root, text="Accuracy: -")
        self.label_accuracy.pack()

        self.button_start = tk.Button(self.root, text="Start", command=self.start_test)
        self.button_start.pack(pady=10)

    def start_test(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.root.after(1000, self.update_timer)
            self.entry_input.bind("<KeyRelease>", self.check_input)

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.label_timer.config(text=f"Time: {elapsed_time}s")
            self.root.after(1000, self.update_timer)

    def check_input(self, event):
        typed_text = self.current_input.get()
        if typed_text == self.text_to_type:
            self.timer_running = False
            self.entry_input.unbind("<KeyRelease>")
            self.calculate_accuracy()

    def calculate_accuracy(self):
        typed_text = self.current_input.get()
        correct_chars = sum(1 for c1, c2 in zip(typed_text, self.text_to_type) if c1 == c2)
        accuracy = (correct_chars / len(self.text_to_type)) * 100
        self.label_accuracy.config(text=f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
