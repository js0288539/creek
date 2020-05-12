@echo off
rem Make .lib import libraries.
rem Requires Visual C++ Studio or Toolkit.
rem vcvars64.bat must be run first to use LINK.EXE.

LINK.EXE /LIB /NOLOGO /DEF:SDL.def /MACHINE:x64 /OUT:SDL.lib
LINK.EXE /LIB /NOLOGO /DEF:SDL_ttf.def /MACHINE:x64 /OUT:SDL_ttf.lib
LINK.EXE /LIB /NOLOGO /DEF:SDL_image.def /MACHINE:x64 /OUT:SDL_image.lib
LINK.EXE /LIB /NOLOGO /DEF:SDL_mixer.def /MACHINE:x64 /OUT:SDL_mixer.lib
LINK.EXE /LIB /NOLOGO /DEF:freetype.def /MACHINE:x64 /OUT:freetype.lib
LINK.EXE /LIB /NOLOGO /DEF:tiff.def /MACHINE:x64 /OUT:tiff.lib
LINK.EXE /LIB /NOLOGO /DEF:png.def /MACHINE:x64 /OUT:png.lib
LINK.EXE /LIB /NOLOGO /DEF:jpeg.def /MACHINE:x64 /OUT:jpeg.lib
LINK.EXE /LIB /NOLOGO /DEF:webp.def /MACHINE:x64 /OUT:webp.lib
LINK.EXE /LIB /NOLOGO /DEF:mpg123.def /MACHINE:x64 /OUT:mpg123.lib
LINK.EXE /LIB /NOLOGO /DEF:z.def /MACHINE:x64 /OUT:z.lib
LINK.EXE /LIB /NOLOGO /DEF:vorbisfile.def /MACHINE:x64 /OUT:vorbisfile.lib
LINK.EXE /LIB /NOLOGO /DEF:vorbis.def /MACHINE:x64 /OUT:vorbis.lib
LINK.EXE /LIB /NOLOGO /DEF:ogg.def /MACHINE:x64 /OUT:ogg.lib
LINK.EXE /LIB /NOLOGO /DEF:portmidi.def /MACHINE:x64 /OUT:portmidi.lib
rem LINK.EXE /LIB /NOLOGO /DEF:gcc.def /MACHINE:x64 /OUT:gcc.lib
rem LINK.EXE /LIB /NOLOGO /DEF:stdcxx.def /MACHINE:x64 /OUT:stdcxx.lib
