from functools import partial  # To prevent unwanted windows.
from tkinter import *


# noinspection PyArgumentList
class Converter:
    def __init__(self, parent):
        # Formatting variables
        self.parent = parent
        background_color = "light blue"

        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 194 degrees F',
                              '40 degrees C is 4.4 degrees F',
                              '12 degrees C is 53.6 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F']

        # Initialise list to hold calculation history
        self.all_calculations = []

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Reading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # History / history button frame (row 5)
        self.hist_history_frame = Frame(self.converter_frame)
        self.hist_history_frame.grid(row=5, pady=10)

        self.history_button = Button(self.converter_frame, font="Arial 14",
                                     text="History", padx=10, pady=10, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        # Add Answer to list for history

    def history(self, calc_history):
        History(self, calc_history)



class History:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"  # pale green"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # set up child window (ie history box)
        self.history_box = Toplevel()

        # if user press cross at top, closes history and releases button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background,
                                   pady=10)
        self.history_frame.grid()

        # set up history heading
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font=("Arial", "16", "bold"),
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                       "calculations. Please use the "
                                       "export button to create a text "
                                       "file of all your calculations for "
                                       "this session",
                                  font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background, fg="maroon", wrap=250)
        self.history_text.grid(row=1)

        # History Output goes here... (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                                - item -1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="arial 12 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
