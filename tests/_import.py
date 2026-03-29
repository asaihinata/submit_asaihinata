from os.path import abspath, dirname, join
from sys import path

path.append(abspath(join(dirname(__file__),'..')))
from src import *

clear()
