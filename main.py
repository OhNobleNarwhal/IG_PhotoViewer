# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Tim Dempster                                                                                                        #
# OhNobleNarwhal December 2018                                                                                        #
#                                                                                                                     #
# Code to take an Instagram picture and open just the picture file itself.                                            #
# Design is to view the source, navigate within that source to the image hyperlink and save it.                       #
# Then, the program opens that source in a new tab.                                                                   #
#                                                                                                                     #
#                                                                                                                     #
# The URL for the picture is found in the source after the line: <meta property="og:image" content="DESIREDURL"       #
#                                                                                                                     #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import urllib2
import re
import webbrowser
# First iteration is using a specific URL, but this will be developed into user input or even right-click GUI

"""sourceString = urllib2.urlopen('https://www.instagram.com/p/Bq5a3BYhJaj/').read()
X = re.search('<meta property="og:image" content="(.+?)" />', sourceString)
if X:
    result = X.group(1)    #desired URL
print result

webbrowser.open_new_tab(result)
"""

testURL = raw_input("Enter Instagram picture URL: ")
sourceString = urllib2.urlopen(testURL).read()
X = re.search('<meta property="og:image" content="(.+?)" />', sourceString)
if X:
    result = X.group(1) #desired URL

webbrowser.open_new_tab(result)


#This works but hitting enter on the user input opens the url the user entered...
