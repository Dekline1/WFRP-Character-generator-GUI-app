import math

# by_script settable parameters & options (no parameters validation)

backLogActive = True  # default value = True - backlog label and window visible
fontSize = 14  # default value = 14 for bold, and 13 for normal. Non scalable
backLogFontSize = 10  # default value = 10  Non scalable
familyFont = "Source Code Pro"

windowTitle = "GUI frame Tkinter"
labelCommandLineText = "Access terminal"
labelResultsText = "Output data"
labelBackLogText = "Back log"

windowBackGroundColor = "#1e1f22"
boxBackGroundColor = "#2b2d30"
boxTextColor = "#bcbec4"

defaultUnknownCommandLine1 = "Unknown command: "
defaultUnknownCommandLine2 = ", type: [h]elp"

windowSizeConverter = 0.90  # default value = 0.9, min rational value is 0.4

# all bellowed values is compared with windowSizeConverter in script

resultBoxLength = math.inf  # default value = infinity, 35 is default for fit to window geometry (experimental value,
# not real amount of lines)
globalOffset = 50  # default value = 50

labelCommandBoxWidth = 350  # default value = 350
labelCommandBoxHeight = 80  # default value = 80
labelCommandBoxPlaceX = 50  # default value = 50
labelCommandBoxPlaceY = 50  # default value = 50

labelResultsBoxWidth = 350  # default value = 350
labelResultsBoxHeight = 80  # default value = 80
# labelResultsBoxPlaceX # auto adjusted in script
labelResultsBoxPlaceY = 50  # default value = 50

labelBackLogBoxWidth = 350  # default value = 350
labelBackLogBoxHeight = 80  # default value = 80
labelBackLogBoxPlaceX = 50  # default value = 50
# labelBackLogBoxPlaceY # auto adjusted in script

commandBoxWidth = 700  # default value = 700
commandBoxHeight = 80  # default value = 400
commandBoxPlaceX = 50  # default value = 50
# commandBoxPlaceY # auto adjusted in script

resultsBoxWidth = 1050  # default value = 700
resultsBoxHeight = 860  # default value = 400
# resultsBoxPlaceX  # auto adjusted in script
# resultsBoxPlaceY  # auto adjusted in script

backLogBoxWidth = 700  # default value = 700
backLogBoxHeight = 600  # default value = 400
backLogBoxPlaceX = 50  # default value = 50
# commandBoxPlaceY # auto adjusted in script
