import tkinter as tk
from tkinter import font

import characterGENERATOR.characterGENERATORparameters
import mainAPP.mainAPPvariables
import mainAPP.mainAPPdefinitions


def execute(event=None):
    # resultsBox.insert(tk.END, "hh")
    # resultsBox.insert(tk.END, '\n')
    # resultsBox.see(tk.END)

    def command_list(userCommand):

        if userCommand in mainAPP.mainAPPdefinitions.commandDictionary:
            return mainAPP.mainAPPdefinitions.commandDictionary[userCommand][0](userCommand)
        elif userCommand[0] in mainAPP.mainAPPdefinitions.commandListAdvanced:
            return mainAPP.mainAPPdefinitions.advanced(userCommand)
        else:
            return (mainAPP.mainAPPvariables.defaultUnknownCommandLine1 + userCommand
                    + mainAPP.mainAPPvariables.defaultUnknownCommandLine2)

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
            if len(current_content) >= float(mainAPP.mainAPPvariables.resultBoxLength
                                             * mainAPP.mainAPPvariables.windowSizeConverter):
                resultsBox.delete("1.0", "2.0")
            else:
                resultsBox.insert(tk.END, result)
                resultsBox.insert(tk.END, '\n')
                resultsBox.see(tk.END)

                backLogBox.insert(tk.END, mainAPP.mainAPPdefinitions.back_log())
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

    windowWidth = int(screenWidth * mainAPP.mainAPPvariables.windowSizeConverter)
    windowHeight = int(screenHeight * mainAPP.mainAPPvariables.windowSizeConverter)

    center_x = int(screenWidth / 2 - windowWidth / 2)
    center_y = int(screenHeight / 2 - windowHeight / 2)

    return window.geometry(f'{windowWidth}x{windowHeight}+{center_x}+{center_y}')


window = tk.Tk()
window.title(mainAPP.mainAPPvariables.windowTitle)
window_geometry()
window.configure(bg=mainAPP.mainAPPvariables.windowBackGroundColor)
default_font = font.Font(family=mainAPP.mainAPPvariables.familyFont, size=mainAPP.mainAPPvariables.fontSize)
window.option_add("*Font", default_font)

labelCommand = tk.Label(window,
                        text=mainAPP.mainAPPvariables.labelCommandLineText,
                        bg=mainAPP.mainAPPvariables.boxBackGroundColor,
                        fg=mainAPP.mainAPPvariables.boxTextColor)

labelCommand.place(x=int(mainAPP.mainAPPvariables.labelCommandBoxPlaceX * mainAPP.mainAPPvariables.windowSizeConverter),
                   width=int(mainAPP.mainAPPvariables.labelCommandBoxWidth * mainAPP.mainAPPvariables.windowSizeConverter),
                   y=int(mainAPP.mainAPPvariables.labelCommandBoxPlaceY * mainAPP.mainAPPvariables.windowSizeConverter),
                   height=int(mainAPP.mainAPPvariables.labelCommandBoxHeight * mainAPP.mainAPPvariables.windowSizeConverter))

if mainAPP.mainAPPvariables.backLogActive:
    labelBackLog = tk.Label(window,
                            text=mainAPP.mainAPPvariables.labelBackLogText,
                            bg=mainAPP.mainAPPvariables.boxBackGroundColor,
                            fg=mainAPP.mainAPPvariables.boxTextColor)

    labelBackLog.place(x=int(mainAPP.mainAPPvariables.labelBackLogBoxPlaceX * mainAPP.mainAPPvariables.windowSizeConverter),
                       width=int(mainAPP.mainAPPvariables.labelBackLogBoxWidth * mainAPP.mainAPPvariables.windowSizeConverter),
                       y=int((mainAPP.mainAPPvariables.labelCommandBoxPlaceY + mainAPP.mainAPPvariables.commandBoxHeight
                              + mainAPP.mainAPPvariables.globalOffset + mainAPP.mainAPPvariables.commandBoxHeight
                              + mainAPP.mainAPPvariables.globalOffset) * mainAPP.mainAPPvariables.windowSizeConverter),
                       height=int(mainAPP.mainAPPvariables.labelCommandBoxHeight * mainAPP.mainAPPvariables.windowSizeConverter))

labelResults = tk.Label(window,
                        text=mainAPP.mainAPPvariables.labelResultsText,
                        bg=mainAPP.mainAPPvariables.boxBackGroundColor,
                        fg=mainAPP.mainAPPvariables.boxTextColor)

labelResults.place(x=int((mainAPP.mainAPPvariables.commandBoxPlaceX + mainAPP.mainAPPvariables.commandBoxWidth
                          + mainAPP.mainAPPvariables.globalOffset) * mainAPP.mainAPPvariables.windowSizeConverter),
                   width=int(mainAPP.mainAPPvariables.labelCommandBoxWidth * mainAPP.mainAPPvariables.windowSizeConverter),
                   y=int(mainAPP.mainAPPvariables.labelCommandBoxPlaceY * mainAPP.mainAPPvariables.windowSizeConverter),
                   height=int(mainAPP.mainAPPvariables.labelCommandBoxHeight * mainAPP.mainAPPvariables.windowSizeConverter))

commandBox = tk.Text(window,
                     bg=mainAPP.mainAPPvariables.boxBackGroundColor,
                     fg=mainAPP.mainAPPvariables.boxTextColor)

commandBox.place(x=int(mainAPP.mainAPPvariables.commandBoxPlaceX * mainAPP.mainAPPvariables.windowSizeConverter),
                 width=int(mainAPP.mainAPPvariables.commandBoxWidth * mainAPP.mainAPPvariables.windowSizeConverter),
                 y=int((mainAPP.mainAPPvariables.labelCommandBoxPlaceY + mainAPP.mainAPPvariables.labelCommandBoxHeight +
                        mainAPP.mainAPPvariables.globalOffset) * mainAPP.mainAPPvariables.windowSizeConverter),
                 height=int(mainAPP.mainAPPvariables.commandBoxHeight * mainAPP.mainAPPvariables.windowSizeConverter))

commandBox.bind('<Return>', execute)

if mainAPP.mainAPPvariables.backLogActive:
    backLogBox = tk.Text(window,
                         bg=mainAPP.mainAPPvariables.boxBackGroundColor,
                         fg=mainAPP.mainAPPvariables.boxTextColor,
                         font=font.Font(size=mainAPP.mainAPPvariables.backLogFontSize))

    backLogBox.place(x=int(mainAPP.mainAPPvariables.backLogBoxPlaceX * mainAPP.mainAPPvariables.windowSizeConverter),
                     width=int(mainAPP.mainAPPvariables.backLogBoxWidth * mainAPP.mainAPPvariables.windowSizeConverter),
                     y=int((mainAPP.mainAPPvariables.labelCommandBoxPlaceY + mainAPP.mainAPPvariables.labelCommandBoxHeight
                            + mainAPP.mainAPPvariables.globalOffset + mainAPP.mainAPPvariables.commandBoxHeight
                            + mainAPP.mainAPPvariables.globalOffset + mainAPP.mainAPPvariables.labelBackLogBoxHeight
                            + mainAPP.mainAPPvariables.globalOffset) * mainAPP.mainAPPvariables.windowSizeConverter),
                     height=int(mainAPP.mainAPPvariables.backLogBoxHeight * mainAPP.mainAPPvariables.windowSizeConverter))

resultsBox = tk.Text(window,
                     bg=mainAPP.mainAPPvariables.boxBackGroundColor,
                     fg=mainAPP.mainAPPvariables.boxTextColor)

resultsBox.place(x=int((mainAPP.mainAPPvariables.commandBoxPlaceX + mainAPP.mainAPPvariables.commandBoxWidth +
                        mainAPP.mainAPPvariables.globalOffset) * mainAPP.mainAPPvariables.windowSizeConverter),
                 width=int(mainAPP.mainAPPvariables.resultsBoxWidth * mainAPP.mainAPPvariables.windowSizeConverter),
                 y=int((mainAPP.mainAPPvariables.labelResultsBoxPlaceY + mainAPP.mainAPPvariables.labelResultsBoxHeight +
                        mainAPP.mainAPPvariables.globalOffset) * mainAPP.mainAPPvariables.windowSizeConverter),
                 height=int(mainAPP.mainAPPvariables.resultsBoxHeight * mainAPP.mainAPPvariables.windowSizeConverter))

resultsBox.insert(tk.END, characterGENERATOR.characterGENERATORparameters.welcomeText, mainAPP.mainAPPdefinitions.help_me())


window.mainloop()

resultsBox.insert(tk.END, "hh")
resultsBox.insert(tk.END, '\n')
resultsBox.see(tk.END)
