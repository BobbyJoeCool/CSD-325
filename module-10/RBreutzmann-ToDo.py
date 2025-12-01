# Breutzmann, Robert
# CSD 325 - Advanced Python
# Assignment 10.2
# Due Date 12/7/2025
import tkinter as tk
import tkinter.messagebox as msg

### Change the Title of the window to your last name-ToDo. Ex. Sampson-ToDo  
### Change the color of the menu items, two (2) complementary colors work best.
#### Currently, the user clicks the left mouse button to delete a task.. change that to the right mouse button.
### Provide instructions in the label on how to delete a task.
### We want the user to exit correctly, so add a menu item of File -> Exit. When clicked, Exit will end the program.
### Run the program, add a few tasks and take a screenshot. Paste that screenshot into your Word document.
### As the program is running, delete a task, then take a screenshot. Paste that screenshot into your Word document.

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        ### These next 3 chunks add the menu bar with a File-Exit option.
        menu_frame = tk.Frame(self, bg="lightgrey")
        menu_frame.pack(fill="x")

        file_button = tk.Menubutton(menu_frame, text="File", relief="raised")
        file_button.pack(side="left")

        file_dropdown = tk.Menu(file_button, tearoff=False)
        file_dropdown.add_command(label="Exit", command=self.destroy)

        file_button.config(menu=file_dropdown)



        #Changed the title of the App Window
        self.title("RBreutzmann To-Do App")
        self.geometry("400x600")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here ---  **Right Click Item to Delete**", bg="lightgrey", fg="black", pady=10)

        # Changed the Bind on this to button 2 to make it a right click.
        todo1.bind("<Button-2>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # CHanged the scheme of the colors for the buttons - Purple and Blue with White Text
        self.colour_schemes = [{"bg": "purple4", "fg": "white"}, {"bg": "mediumblue", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            # Changed the bind on this to Button 2 to make it a right click.
            new_task.bind("<Button-2>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()