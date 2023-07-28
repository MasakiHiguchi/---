import tkinter as tk

class ManageOrderProductPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Manage Order Product Page")
        self.geometry("800x400")

        self.create_widgets()

    def return_to_main_page(self):
        self.destroy()

    def create_widgets(self):
        # ... ここにGUIのウィジェットを配置するコードを追加 ...

        btn_return = tk.Button(self, text="戻る", command=self.return_to_main_page)
        btn_return.pack(side=tk.RIGHT, padx=10, pady=10)

if __name__ == "__main__":
    app = ManageOrderProductPage()
    app.mainloop()
