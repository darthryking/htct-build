htct-build
==========

Copyright © 2019 by DKY (Ryan Lam)

The files in this repository comprise the core materials that are necessary to
build the __Hazard Team Compile Tool__. They have been provided here, free of
charge, for anyone's use in building their own `htct.exe` executable.


Current version: ___0.6.0 BETA___


### Requirements
* Python 3.7
* PyInstaller 3.4
* PySide2 5.11.2 or equivalent
* psutil 5.4.8

A `requirements.txt` file has been provided in this repository for (optional)
convenient dependency installation with `pip`.

### Optional Requirements
* UPX 3.91 or equivalent (for PYD and executable compression)

### To Build
1. Ensure that the above requirements are installed.
2. Run `build_htct.bat`.
3. A new folder `dist` will appear with `htct.exe` inside.
4. Done!

### Known Potential Errors
If you get DLL load errors when running your custom-built `htct.exe`, that is
due to UPX corrupting the following DLLs when PyInstaller packages the
executable:
* vcruntime140.dll
* msvcp140.dll
* qwindows.dll
* qwindowsvistastyle.dll

To fix these errors, you have a couple of options. You can either:

1. Disable UPX. To do this, add the `--noupx` option to the `pyinstaller`
    invocation in `build_htct.bat`.

... or:

2. Install a development version of PyInstaller that can accept the
    `--upx-exclude` option. Specifically, you will need a version of
    PyInstaller that includes [pull request #3821](https://github.com/pyinstaller/pyinstaller/pull/3821).
    You will then need to add the following options to the `pyinstaller`
    invocation in `build_htct.bat`:

    * `--upx-exclude vcruntime140.dll`
    * `--upx-exclude msvcp140.dll`
    * `--upx-exclude qwindows.dll`
    * `--upx-exclude qwindowsvistastyle.dll`
