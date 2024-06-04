import tkinter as tk
from tkinter import font

import characterGENERATOR.characterGENERATORparameters
import mainAPPvariables
import mainAPPdefinitions


def execute(event=None):
    # resultsBox.insert(tk.END, "hh")
    # resultsBox.insert(tk.END, '\n')
    # resultsBox.see(tk.END)

    def command_list(userCommand):

        if userCommand in mainAPPdefinitions.commandDictionary:
            return mainAPPdefinitions.commandDictionary[userCommand][0](userCommand)
        elif (userCommand[0] in mainAPPdefinitions.commandListAdvanced) and (len(userCommand) == 4):
            return mainAPPdefinitions.advanced(userCommand)
        else:
            return (mainAPPvariables.defaultUnknownCommandLine1 + userCommand
                    + mainAPPvariables.defaultUnknownCommandLine2)

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
            if len(current_content) >= float(mainAPPvariables.resultBoxLength
                                             * mainAPPvariables.windowSizeConverter):
                resultsBox.delete("1.0", "2.0")
            else:
                resultsBox.insert(tk.END, result)
                resultsBox.insert(tk.END, '\n')
                resultsBox.see(tk.END)

                backLogBox.insert(tk.END, mainAPPdefinitions.back_log())
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

    windowWidth = int(screenWidth * mainAPPvariables.windowSizeConverter)
    windowHeight = int(screenHeight * mainAPPvariables.windowSizeConverter)

    center_x = int(screenWidth / 2 - windowWidth / 2)
    center_y = int(screenHeight / 2 - windowHeight / 2)

    return window.geometry(f'{windowWidth}x{windowHeight}+{center_x}+{center_y}')


window = tk.Tk()
window.title(mainAPPvariables.windowTitle)
window_geometry()
window.configure(bg=mainAPPvariables.windowBackGroundColor)
default_font = font.Font(family=mainAPPvariables.familyFont, size=mainAPPvariables.fontSize)
window.option_add("*Font", default_font)

labelCommand = tk.Label(window,
                        text=mainAPPvariables.labelCommandLineText,
                        bg=mainAPPvariables.boxBackGroundColor,
                        fg=mainAPPvariables.boxTextColor)

labelCommand.place(x=int(mainAPPvariables.labelCommandBoxPlaceX * mainAPPvariables.windowSizeConverter),
                   width=int(mainAPPvariables.labelCommandBoxWidth * mainAPPvariables.windowSizeConverter),
                   y=int(mainAPPvariables.labelCommandBoxPlaceY * mainAPPvariables.windowSizeConverter),
                   height=int(mainAPPvariables.labelCommandBoxHeight * mainAPPvariables.windowSizeConverter))

if mainAPPvariables.backLogActive:
    labelBackLog = tk.Label(window,
                            text=mainAPPvariables.labelBackLogText,
                            bg=mainAPPvariables.boxBackGroundColor,
                            fg=mainAPPvariables.boxTextColor)

    labelBackLog.place(x=int(mainAPPvariables.labelBackLogBoxPlaceX * mainAPPvariables.windowSizeConverter),
                       width=int(mainAPPvariables.labelBackLogBoxWidth * mainAPPvariables.windowSizeConverter),
                       y=int((mainAPPvariables.labelCommandBoxPlaceY + mainAPPvariables.commandBoxHeight
                              + mainAPPvariables.globalOffset + mainAPPvariables.commandBoxHeight
                              + mainAPPvariables.globalOffset) * mainAPPvariables.windowSizeConverter),
                       height=int(mainAPPvariables.labelCommandBoxHeight * mainAPPvariables.windowSizeConverter))

labelResults = tk.Label(window,
                        text=mainAPPvariables.labelResultsText,
                        bg=mainAPPvariables.boxBackGroundColor,
                        fg=mainAPPvariables.boxTextColor)

labelResults.place(x=int((mainAPPvariables.commandBoxPlaceX + mainAPPvariables.commandBoxWidth
                          + mainAPPvariables.globalOffset) * mainAPPvariables.windowSizeConverter),
                   width=int(mainAPPvariables.labelCommandBoxWidth * mainAPPvariables.windowSizeConverter),
                   y=int(mainAPPvariables.labelCommandBoxPlaceY * mainAPPvariables.windowSizeConverter),
                   height=int(mainAPPvariables.labelCommandBoxHeight * mainAPPvariables.windowSizeConverter))

commandBox = tk.Text(window,
                     bg=mainAPPvariables.boxBackGroundColor,
                     fg=mainAPPvariables.boxTextColor)

commandBox.place(x=int(mainAPPvariables.commandBoxPlaceX * mainAPPvariables.windowSizeConverter),
                 width=int(mainAPPvariables.commandBoxWidth * mainAPPvariables.windowSizeConverter),
                 y=int((mainAPPvariables.labelCommandBoxPlaceY + mainAPPvariables.labelCommandBoxHeight +
                        mainAPPvariables.globalOffset) * mainAPPvariables.windowSizeConverter),
                 height=int(mainAPPvariables.commandBoxHeight * mainAPPvariables.windowSizeConverter))

commandBox.bind('<Return>', execute)

if mainAPPvariables.backLogActive:
    backLogBox = tk.Text(window,
                         bg=mainAPPvariables.boxBackGroundColor,
                         fg=mainAPPvariables.boxTextColor,
                         font=font.Font(size=mainAPPvariables.backLogFontSize))

    backLogBox.place(x=int(mainAPPvariables.backLogBoxPlaceX * mainAPPvariables.windowSizeConverter),
                     width=int(mainAPPvariables.backLogBoxWidth * mainAPPvariables.windowSizeConverter),
                     y=int((mainAPPvariables.labelCommandBoxPlaceY + mainAPPvariables.labelCommandBoxHeight
                            + mainAPPvariables.globalOffset + mainAPPvariables.commandBoxHeight
                            + mainAPPvariables.globalOffset + mainAPPvariables.labelBackLogBoxHeight
                            + mainAPPvariables.globalOffset) * mainAPPvariables.windowSizeConverter),
                     height=int(mainAPPvariables.backLogBoxHeight * mainAPPvariables.windowSizeConverter))

resultsBox = tk.Text(window,
                     bg=mainAPPvariables.boxBackGroundColor,
                     fg=mainAPPvariables.boxTextColor)

resultsBox.place(x=int((mainAPPvariables.commandBoxPlaceX + mainAPPvariables.commandBoxWidth +
                        mainAPPvariables.globalOffset) * mainAPPvariables.windowSizeConverter),
                 width=int(mainAPPvariables.resultsBoxWidth * mainAPPvariables.windowSizeConverter),
                 y=int((mainAPPvariables.labelResultsBoxPlaceY + mainAPPvariables.labelResultsBoxHeight +
                        mainAPPvariables.globalOffset) * mainAPPvariables.windowSizeConverter),
                 height=int(mainAPPvariables.resultsBoxHeight * mainAPPvariables.windowSizeConverter))

resultsBox.insert(tk.END, characterGENERATOR.characterGENERATORparameters.welcomeText, mainAPPdefinitions.help_me())


window.mainloop()

resultsBox.insert(tk.END, "hh")
resultsBox.insert(tk.END, '\n')
resultsBox.see(tk.END)
