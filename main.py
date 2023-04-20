# William Bourque 1942926

import pathlib
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import sqlite3
import random
from deep_translator import GoogleTranslator
from tkinter import messagebox
from tkinter.messagebox import showinfo
import os
import sys
from functools import partial
from tkinter import messagebox as msg


# Mise en relation du chemin d'accès pour le dossier de travail 
path = "C:/Users/willb/Documents/GitHub/TP1_Native_WilliamBourque_1942926"
db = "C:/Users/willb/Documents/GitHub/TP1_Native_WilliamBourque_1942926/quotes.db"
Index = 0