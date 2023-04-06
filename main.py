import sys
import json
from random import randint
from PySide6.QtWidgets import ( QApplication,
      QLabel,
      QMainWindow,
      QPushButton,
      QVBoxLayout,
      QHBoxLayout,
      QWidget,
      QLineEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_days = DaysWindow()
        self.window_week = WeekWindow()
        self.setWindowTitle("Perfect Planner")
        self.label_main = QLabel("Perfect Planner")
        self.button_week = QPushButton("WEEK")
        self.button_days = QPushButton("DAYS")
        self.button_info = QPushButton("INFO")
        self.button_days.clicked.connect(self.toggle_window_days)
        self.button_week.clicked.connect(self.toggle_window_week)


        layout = QVBoxLayout()

        layout.addWidget(self.label_main)
        layout.addWidget(self.button_week)
        layout.addWidget(self.button_days)
        layout.addWidget(self.button_info)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def toggle_window_days(self, checked):
        if self.window_days.isVisible():
            self.window_days.hide()
        else:
            self.window_days.show()

    def toggle_window_week(self, checked):
        if self.window_week.isVisible():
            self.window_week.hide()
        else:
            self.window_week.show()


class WeekWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week Planner")

        self.label_168method = QLabel("168-Method")

        self.label_task = QLabel("Task")
        self.label_hours = QLabel("Hours/week")

        self.input_task = QLineEdit()
        self.input_hours = QLineEdit()
        self.button_add = QPushButton("Add")
        self.button_add.clicked.connect(self.add_task)
        self.button_change = QPushButton("Change")
        self.button_delete = QPushButton("Delete")

        self.label_plans = QLabel()



        layout_label = QHBoxLayout()
        layout_bar = QHBoxLayout()
        layout_actions = QHBoxLayout()
        layout_window = QVBoxLayout()
        layout_tasks = QHBoxLayout()

        layout_label.addWidget(self.label_168method)

        layout_bar.addWidget(self.label_task)
        layout_bar.addWidget(self.label_hours)

        layout_actions.addWidget(self.input_task)
        layout_actions.addWidget(self.input_hours)
        layout_actions.addWidget(self.button_add)
        layout_actions.addWidget(self.button_change)
        layout_actions.addWidget(self.button_delete)

        layout_tasks.addWidget(self.label_plans)

        layout_window.addLayout(layout_label)
        layout_window.addLayout(layout_bar)
        layout_window.addLayout(layout_actions)
        layout_window.addLayout(layout_tasks)

        self.setLayout(layout_window)

    def add_task(self):
        task = self.input_task.text()
        time = self.input_hours.text()
        # self.label_plans.setText(self.input_task.text())
        new_data = {
            task: time,

        }
        # with open("data.json", "w") as data_file:
        #     json.dump(new_data, data_file, indent=4)

        if len(task) == 0 or len(time) == 0:
            print("Opps...error")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                self.input_task.clear()
                self.input_hours.clear()



class DaysWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("WEEK")
        self.button_monday = QPushButton("MONDAY")


        layout.addWidget(self.button_monday)
        self.setLayout(layout)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()