htct-build
==========

Copyright © 2015 by DKY (Ryan Lam)

The files in this repository comprise the core materials that are necessary to 
build the __Hazard Team Compile Tool__. They have been provided here, free of 
charge, for anyone's use in building their own `htct.exe` executable.


Current version: ___0.4.1 BETA___


###Requirements
* Python 2.7
* PyInstaller 2.1
* PySide 1.2.2 or equivalent
* psutil 2.2.1

A `requirements.txt` file has been provided in this repository for (optional) 
convenient dependency installation with `pip`.

###Optional Requirements
* UPX 3.91 or equivalent (for PYD and executable compression)

###To Build
1. Ensure that the above requirements are installed.
2. Run `build_htct.bat`.
3. A new folder `dist` will appear with `htct.exe` inside.
4. Done!
