#!/bin/sh
mkdir /usr/share/debgui
cp * /usr/share/debgui
ln -s /usr/share/debgui/debgui.py /usr/bin/debgui
echo "Recuerda que para usar este programa necesitas al menos los paquetes 'dh-make' y 'devhelpers'"
echo "Remenber that this program need 'dh-make' and 'devhelpers' packages"
