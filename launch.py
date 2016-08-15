import configparser,  subprocess

# parse and get serial number and serverIP from launcher.ini
config = configparser.ConfigParser()
config.read('launcher.ini')
read1 = config.get('Options', 'Serial')
read2 = config.get('Options', 'ServerIP')
# parse and get serial number and serverIP from launcher.original.ini
config = configparser.ConfigParser()
config.read('launcher.original.ini')
read3 = config.get('Options', 'Serial')
read4 = config.get('Options', 'ServerIP')
# compare values
if read1 != read3:
   read2 != read4;
   pass
# copy launcher.original.in in launcher.ini
read_orig_ini=open("launcher.original.ini", 'r')
try:
      reading_file=read_orig_ini.read()
      write_orig_ini=open("launcher.ini", 'w')
      try:
           write_orig_ini.write(reading_file)
      finally:
           write_orig_ini.close()
finally:
      read_orig_ini.close()
# check AutoLogin, Logins, Serial value
config = configparser.ConfigParser()
config.read('launcher.ini')
Auto_login = config.get('Options', 'AutoLogin')
Logins = config.get('Options', 'Logins')
Serial = config.get('Options', 'Serial')
if not Auto_login:
# start gui
      subprocess.call("/home/dima/PycharmProjects/Python/gui.py", shell=True)
# start gui2
else:
    if not Logins:
      subprocess.call("/home/dima/PycharmProjects/Python/gui2.py", shell=True)
    if not Serial:
      subprocess.call("/home/dima/PycharmProjects/Python/gui2.py", shell=True)

