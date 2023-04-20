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

# Fonction pour permettre l'utilisation de fonctions SQL ainsi que l'utilisation de
# try / except pour trouver les potentielles erreurs plus facilement
def SQLRequest(Request):
    connection=sqlite3.connect(db, timeout=10)
    cursor=connection.cursor()
    try :
        cursor.execute(Request)
    except Exception as e:
        messagebox.showerror("SQL Request",e)
        print(e)
        print(e.args[0])

    connection.commit()
    result=cursor.fetchall()
    connection.close()
    return (result)
    
# Fonction pour permettre l'utilisation des requetes SQL qui utilisent le SQL VIEW ainsi que l'utilisation de
# try / except pour trouver les potentielles erreurs plus facilement
def SQLRequestView(Request):
    connection=sqlite3.connect(db, timeout=10)
    cursor=connection.cursor()

    CreateView='CREATE VIEW IF NOT EXISTS view AS SELECT ROW_NUMBER(),* FROM Citations INNER JOIN Auteurs on Citations.AuteurID=Auteurs.AuteurID'       
    try :
        cursor.execute(CreateView)
    except Exception as e:
        messagebox.showerror("SQL Request View CREATE view",e)

    try :
        cursor.execute(Request)
    except Exception as e:
        messagebox.showerror("SQL Request View",e)
        print(e)
    connection.commit()
    result=cursor.fetchall()
    connection.close()
    return result