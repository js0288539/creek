@echo off
rem Make .def files needed for .lib file creation.
rem Requires gendef.exe on the search path
rem (found under mingw-w64-tools in the MinGW-w64
rem git repository at SourceForge:
rem http://sourceforge.net/p/mingw-w64/mingw-w64/ci/master/tree/).

gendef - SDL.dll >SDL.def
gendef - SDL_ttf.dll >SDL_ttf.def
gendef - SDL_image.dll >SDL_image.def
gendef - SDL_mixer.dll >SDL_mixer.def
gendef - libfreetype-6.dll >freetype.def
gendef - libtiff-5.dll >tiff.def
gendef - libpng16-16.dll >png.def
gendef - libjpeg-8.dll >jpeg.def
gendef - libwebp-5.dll >webp.def
gendef - libmpg123-0.dll >mpg123.def
gendef - zlib1.dll >z.def
gendef - libvorbisfile-3.dll >vorbisfile.def
gendef - libvorbis-0.dll >vorbis.def
gendef - libogg-0.dll >ogg.def
gendef - portmidi.dll >portmidi.def
rem gendef - libgcc_s_sjlj-1.dll >gcc.def
rem gendef - libstdc++-6.dll >stdcxx.def
