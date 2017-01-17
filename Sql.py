#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sqlite3

class Sql:
    def __init__(self):
        self._fichier = "./BDD/taches.sq3"
        _set_connexion_sqlite3()

    def _set_connexion_sqlite3():
        self._connexion = sqlite3.connect(self._fichier)

    def SQL_Disconnect():
        self._connexion.close

    def _get_fichier(self):
        return self._fichier

    def _set_fichier(self, file):
        self._fichier = file

    def _set_curseur(self):
        self._cursor = self._connexion.cursor()

    def close_cursor():
        self._cursor.close()

    def delete_table(t):
        self._cursor.execute("DROP TABLE " + t + ";")
        
#fichierBDD = "./BDD/taches.sq3"
#connexion = sqlite3.connect(fichierBDD)
#cursor = connexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXIST taches (id INTEGER, nom TEXT, debut DATE, priorite INT)")

cursor.execute("INSERT INTO taches(id, nom, debut, priorite) VALUES(1,'Premiere tache',20170112,1)")
cursor.execute("INSERT INTO taches(id, nom, debut, priorite) VALUES(2,'Deuxieme tache',20170112,1)")

cursor.execute("SELECT * FROM taches")
for task in cur:
    print(task)
connexion.commit()
#cursor.close()
#connexion.close()
