#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Python module debgui.py
# Autogenerated from debgui.glade
# Generated on Fri Sep 30 22:01:04 2005

# Warning: Do not modify any context comment such as #--
# They are required to keep user's code

import os

import gtk

from SimpleGladeApp import SimpleGladeApp
from SimpleGladeApp import bindtextdomain

# Cabeceras incluidas por mi
from cmd import Cmd
import sys
import re
import string

app_name = "debgui"
app_version = "0.0.2"

glade_dir = ""
locale_dir = ""

bindtextdomain(app_name, locale_dir)

class MainWindow(SimpleGladeApp):

    def __init__(self, path="debgui.glade",
                 root="main_window",
                 domain=app_name, **kwargs):
        path = os.path.join(glade_dir, path)
        SimpleGladeApp.__init__(self, path, root, domain, **kwargs)

    #-- MainWindow.new {
    def new(self):
        print "A new %s has been created" % self.__class__.__name__
    #-- MainWindow.new }

    #-- MainWindow custom methods {
    #   Write your own methods here
    #-- MainWindow custom methods }

    #-- MainWindow.terminar {
    def terminar(self, widget, *args):
        self.quit()             # Terminamos el programa
    #-- MainWindow.terminar }

    #-- MainWindow.boton_crearpaquete_clicked {
    def boton_crearpaquete_clicked(self, widget, *args):
        # print "boton_crearpaquete_clicked called with self.%s" % widget.get_name()
        #Recogemos la informacion del formulario
        DirectorioTrabajo = self.filechooserbutton1.get_filename()
        ArchivoFuentes = self.filechooserbutton2.get_filename()
        Email = self.entry2.get_text()
        
        '''
        Separamos el path en trozos para comprobar el formato en funcion de la
        extension del archivo y para tomar el nombre del paquete el nombre del
        paquete, que usaremos como parametro para dh-make y para rellenar el 
        campo correspondiente en el formulario
        '''
        partes1 = re.split('/', ArchivoFuentes)
        NombreFuente = partes1[len(partes1) - 1]
        partes2 = re.compile(r'(\W+)').split(ArchivoFuentes)
        Extension1 = partes2[len(partes2) - 1]
        Extension2 = partes2[len(partes2) - 3]
        
        # print "La extension es: " + Extension1
        partes3 = re.compile('-' or '_').split(NombreFuente)
        NombrePaquete = partes3[0]
        # Pasamos el nombre del paquete al formulario
        self.entry6.set_text(partes3[0])
        
        # Comprobamos el formato del archivo y preparamos el comando a ejecutar
        print "Aqui se deberia coger el archivo " + ArchivoFuentes + " y descomprimirlo en " + DirectorioTrabajo + "\n"
        if (Extension2 == "tar"):
            if (Extension1 == "gz"):
                print "Desempaquetando tar.gz...\n"
                Comando = "cd " + DirectorioTrabajo + "; tar zxvf " + ArchivoFuentes
                os.system(Comando)
                restamos = 7
            elif (Extension1 == "bz2"):
                print "Desempaquetando tar.bz2...\n"
                Comando = "cd " + DirectorioTrabajo + "; tar jxvf " + ArchivoFuentes
                os.system(Comando)
                restamos = 8
            else:
                print "El archivo tiene un formato no soportado aun.\n"
                restamos = 1
        elif (Extension1 == "gz"):
            print "Descomprimiendo archivo gz...\n"
            Comando = "cd " + DirectorioTrabajo + "; gunzip " + ArchivoFuentes
            os.system(Comando)
            restamos = 4
        elif (Extension1 == "tgz"):
            print "Desempaquetando archivo tgz...\n"
            Comando = "cd " + DirectorioTrabajo + "; tar zxvf " + ArchivoFuentes
            os.system(Comando)
            restamos = 5
        else:
            print "El archivo tiene un formato no soportado actualmente.\n"
            restamos = 1
        
        # Ahora que ya tenemos las fuentes descomprimidas toca debianizarlas
        # Vamos al lio
        ultimo = len(NombreFuente) - restamos
        fuente = NombreFuente[0:ultimo]
        DirectorioCompleto = DirectorioTrabajo + "/" + fuente
        Debianiza = "cd " + DirectorioCompleto + "; dh_make " + TipoPaquete + " -e " + Email + " -p " + NombrePaquete
        print "Debianizando las fuentes descomprimidas...\n"
        print Debianiza
        ejecucion = os.popen(Debianiza, 'w')
        #print ejecucion
        #if (lineas[8] == "Hit <enter> to confirm:"):
        #lineas = string.split(ejecucion, '\n')
        #for i in range(len(lineas2)):
        #    if (lineas2[i] == "Hit <enter> to confirm:"):
        #        ejecucion.write('\n')
        ejecucion.write('\n')
    #-- MainWindow.boton_crearpaquete_clicked }

    #-- MainWindow.on_radiobutton1_activate {
    def on_radiobutton1_activate(self, widget, *args):
        # print "on_radiobutton1_activate called with self.%s" % widget.get_name()
        global TipoPaquete
        TipoPaquete = "-s"
    #-- MainWindow.on_radiobutton1_activate }

    #-- MainWindow.on_radiobutton2_activate {
    def on_radiobutton2_activate(self, widget, *args):
        # print "on_radiobutton2_activate called with self.%s" % widget.get_name()
        global TipoPaquete
        TipoPaquete = "-m"
    #-- MainWindow.on_radiobutton2_activate }

    #-- MainWindow.on_radiobutton3_activate {
    def on_radiobutton3_activate(self, widget, *args):
        # print "on_radiobutton3_activate called with self.%s" % widget.get_name()
        global TipoPaquete
        TipoPaquete = "-l"
    #-- MainWindow.on_radiobutton3_activate }

    #-- MainWindow.on_radiobutton4_activate {
    def on_radiobutton4_activate(self, widget, *args):
        # print "on_radiobutton4_activate called with self.%s" % widget.get_name()
        global TipoPaquete
        TipoPaquete = "-k"
    #-- MainWindow.on_radiobutton4_activate }


#-- main {

def main():
    main_window = MainWindow()

    main_window.run()
if __name__ == "__main__":
    main()

#-- main }
