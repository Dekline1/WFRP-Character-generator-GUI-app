import tkinter as tk
from tkinter import font
import variables
import definitions


def execute(event=None):
    def command_list(userCommand):

        if userCommand in definitions.commandDictionary:
            return definitions.commandDictionary[userCommand][0]()
        else:
            return variables.defaultUnknownCommandLine1 + userCommand + variables.defaultUnknownCommandLine2

    try:
        command = commandBox.get("1.0", "end-1c").strip()
        commandBox.delete("1.0", tk.END)
        result = str(command_list(command))

        if result == "clear":
            resultsBox.delete("1.0", tk.END)
        elif result == "exit":
            window.destroy()
        else:
            current_content = resultsBox.get("1.0", tk.END).splitlines()
            if len(current_content) >= float(variables.resultBoxLength * variables.windowSizeConverter):
                resultsBox.delete("1.0", "2.0")
            else:
                resultsBox.insert(tk.END, result)
                resultsBox.insert(tk.END, '\n')
                resultsBox.see(tk.END)

                backLogBox.insert(tk.END, definitions.back_log())
                backLogBox.insert(tk.END, '\n')
                backLogBox.see(tk.END)

    except Exception as e:
        result = str(e)
        resultsBox.insert(tk.END, result)
        resultsBox.insert(tk.END, '\n')
        resultsBox.see(tk.END)


def window_geometry():
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * variables.windowSizeConverter)
    windowHeight = int(screenHeight * variables.windowSizeConverter)

    center_x = int(screenWidth / 2 - windowWidth / 2)
    center_y = int(screenHeight / 2 - windowHeight / 2)

    return window.geometry(f'{windowWidth}x{windowHeight}+{center_x}+{center_y}')


window = tk.Tk()
window.title(variables.windowTitle)
window_geometry()
window.configure(bg=variables.windowBackGroundColor)
default_font = font.Font(family=variables.familyFont, size=variables.fontSize)
window.option_add("*Font", default_font)

labelCommand = tk.Label(window,
                        text=variables.labelCommandLineText,
                        bg=variables.boxBackGroundColor,
                        fg=variables.boxTextColor)

labelCommand.place(x=int(variables.labelCommandBoxPlaceX * variables.windowSizeConverter),
                   width=int(variables.labelCommandBoxWidth * variables.windowSizeConverter),
                   y=int(variables.labelCommandBoxPlaceY * variables.windowSizeConverter),
                   height=int(variables.labelCommandBoxHeight * variables.windowSizeConverter))

if variables.backLogActive:
    labelBackLog = tk.Label(window,
                            text=variables.labelBackLogText,
                            bg=variables.boxBackGroundColor,
                            fg=variables.boxTextColor)

    labelBackLog.place(x=int(variables.labelBackLogBoxPlaceX * variables.windowSizeConverter),
                       width=int(variables.labelBackLogBoxWidth * variables.windowSizeConverter),
                       y=int((variables.labelCommandBoxPlaceY + variables.commandBoxHeight + variables.globalOffset
                              + variables.commandBoxHeight + variables.globalOffset) * variables.windowSizeConverter),
                       height=int(variables.labelCommandBoxHeight * variables.windowSizeConverter))

labelResults = tk.Label(window,
                        text=variables.labelResultsText,
                        bg=variables.boxBackGroundColor,
                        fg=variables.boxTextColor)

labelResults.place(x=int((variables.commandBoxPlaceX + variables.commandBoxWidth + variables.globalOffset)
                         * variables.windowSizeConverter),
                   width=int(variables.labelCommandBoxWidth * variables.windowSizeConverter),
                   y=int(variables.labelCommandBoxPlaceY * variables.windowSizeConverter),
                   height=int(variables.labelCommandBoxHeight * variables.windowSizeConverter))

commandBox = tk.Text(window,
                     bg=variables.boxBackGroundColor,
                     fg=variables.boxTextColor)

commandBox.place(x=int(variables.commandBoxPlaceX * variables.windowSizeConverter),
                 width=int(variables.commandBoxWidth * variables.windowSizeConverter),
                 y=int((variables.labelCommandBoxPlaceY + variables.labelCommandBoxHeight +
                        variables.globalOffset) * variables.windowSizeConverter),
                 height=int(variables.commandBoxHeight * variables.windowSizeConverter))

commandBox.bind('<Return>', execute)

if variables.backLogActive:
    backLogBox = tk.Text(window,
                         bg=variables.boxBackGroundColor,
                         fg=variables.boxTextColor,
                         font=font.Font(size=variables.backLogFontSize))

    backLogBox.place(x=int(variables.backLogBoxPlaceX * variables.windowSizeConverter),
                     width=int(variables.backLogBoxWidth * variables.windowSizeConverter),
                     y=int((variables.labelCommandBoxPlaceY + variables.labelCommandBoxHeight + variables.globalOffset
                            + variables.commandBoxHeight + variables.globalOffset + variables.labelBackLogBoxHeight
                            + variables.globalOffset) * variables.windowSizeConverter),
                     height=int(variables.backLogBoxHeight * variables.windowSizeConverter))

resultsBox = tk.Text(window,
                     bg=variables.boxBackGroundColor,
                     fg=variables.boxTextColor)

resultsBox.place(x=int((variables.commandBoxPlaceX + variables.commandBoxWidth +
                        variables.globalOffset) * variables.windowSizeConverter),
                 width=int(variables.resultsBoxWidth * variables.windowSizeConverter),
                 y=int((variables.labelResultsBoxPlaceY + variables.labelResultsBoxHeight +
                        variables.globalOffset) * variables.windowSizeConverter),
                 height=int(variables.resultsBoxHeight * variables.windowSizeConverter))

window.mainloop()
