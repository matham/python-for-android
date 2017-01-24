from pythonforandroid.toolchain import BootstrapNDKRecipe
from os.path import exists
from pythonforandroid.patching import is_msys

class LibSDL2TTF(BootstrapNDKRecipe):
    version = '2.0.14'
    url = ('https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-{version}'
           + ('.zip' if is_msys() else 'tar.gz'))
    dir_name = 'SDL2_ttf'

recipe = LibSDL2TTF()
