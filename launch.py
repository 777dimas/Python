import configparser, subprocess

# parse and get serial number and serverIP from launcher.ini
config = configparser.ConfigParser()
config.read('launcher.ini')
serialValue = config.get('Options', 'Serial')
serverIPValue = config.get('Options', 'ServerIP')

# parse and get serial number and serverIP from launcher.original.ini
config.read('launcher.original.ini')
serialValueOriginal = config.get('Options', 'Serial')
serverIPValueOriginal = config.get('Options', 'ServerIP')

# compare values
if  serialValue != serialValueOriginal:
    serverIPValue != serverIPValueOriginal;
    pass

# copy launcher.original.in in launcher.ini
read_orig_ini = open("launcher.original.ini", 'r')
try:
    reading_file = read_orig_ini.read()
    write_orig_ini = open("launcher.ini", 'w')
    try:
        write_orig_ini.write(reading_file)
    finally:
        write_orig_ini.close()
finally:
    read_orig_ini.close()

# check AutoLogin, Logins, Serial value
config.read('launcher.ini')
Auto_login = config.get('Options', 'AutoLogin')
Logins = config.get('Options', 'Logins')
Serial = config.get('Options', 'Serial')
if not Auto_login:
    if Logins and Serial:
        # start gui2
        subprocess.call("/home/dima/PycharmProjects/Python/custom_login_gui.py", shell=True)
        subprocess.call("/home/dima/PycharmProjects/Python/start.py", shell=True)
    else:
        # start gui
        subprocess.call("/home/dima/PycharmProjects/Python/error_gui.py", shell=True)
else:
    subprocess.call("/home/dima/PycharmProjects/Python/start.py", shell=True)

