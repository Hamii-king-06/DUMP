import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from ULTIMATE64 import menu

    main_menu()

elif bit == '32bit':

    from ULTIMATE import menu

    main_menu()

