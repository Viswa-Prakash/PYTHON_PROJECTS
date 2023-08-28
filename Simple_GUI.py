import tkinter as tk

class InputGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Input GUI")
        
        self.create_ui()

    def create_ui(self):
        label = tk.Label(self.root, text="Enter your name:", font=("Arial", 14))
        label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        button = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.display_input)
        button.pack()

    def display_input(self):
        input_text = self.entry.get()
        self.result_label.config(text=f"Hello, {input_text}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = InputGUI(root)
    root.mainloop()
