#author: Antonio Berardi

import socket
import sys
from subprocess import check_output, STDOUT, CalledProcessError


""" try:
    r = check_output(["nc","-u","-l","-p","15006"],stderr=STDOUT)
    print("------- Resultado:"+format(r))
except CalledProcessError as identifier_check_output:
    print(identifier_check_output) """

print("Socket_UDP!")