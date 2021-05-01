## RUN THIS FILE FIRST AND DO NOT EDIT CODE ##
import pip

try:
    def InstallModule(module):
        if hasattr(pip, 'main'):
            pip.main(['install', module])
        else:
            pip._internal.main(['install', module])

    InstallModule('pygame')
    InstallModule('mutagen')

    print('Successfully setup mp3player_python; you may now run main.py')
except Exception as e:
    print(e)