@echo off
rem Builds the Visual C x64 import libraries.
rem Requires gendef (see MakeDefs.bat) and vcvars64.bat on
rem the executable search path.

CALL vcvars64.bat
CALL MakeDefs.bat
CALL MakeLibs.bat
