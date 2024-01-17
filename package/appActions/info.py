import pygetwindow as gw
from AppKit import NSWorkspace
from ..settings import main_platform

def getAppId():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier'] 

def getAppName():
    if (main_platform == 'macos'):
        return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    else:
        return gw.getActiveWindow().title