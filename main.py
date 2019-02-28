import sys
import queue
import shutil

import psutil

from PySide2 import QtCore, QtGui, QtWidgets

import htct
import mainwindow
import compilewindow
import settingsdialog
import presetdialog
import vars
import compileinter
import configinter
import defaultconfig
import utils
import vdfutils
import icon


if __name__ == '__main__':
    sys.exit(htct.main())
    
    