# import the Tkinkter module
import tkinter as tkinter
import circle

# create a new window


def MakeView():
    window = tkinter.Tk()
    window.title("Visual Experiment")
    window.geometry("1024x768")
    window.mainloop()
    canvas = tkinter.Canvas(window, width=1024, height=768,
                            borderwidth=1, highlightthickness=1, bg="black")
    canvas.grid()
    canvas.create_circle(100, 120, 50, fill="white",
                         outline="ddd", width=4)
    return window


# draw the window and start the application


def main():
    """main function for all program logic"""
    view = MakeView()
    # access to view


main()
