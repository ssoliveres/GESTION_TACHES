#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sqlite3

class Sql:
   def __init__(self):
      self._fichier = "./BDD/taches.sq3"

   def _set_connexion_sqlite3(self):
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

   def show_table(t):
      self._cursor.execute("SELECT * FROM " + t)
      for taskList in self._cursor:
         print tasklist

connexion = Sql()
connexion._set_connexion_sqlite3()
 
connexion.commit()
