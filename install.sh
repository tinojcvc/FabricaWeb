echo "instalando git para la descarga remota"
apt-get install git

echo "instalando libreiras de desarrollo para python"
apt-get build-dep python-imaging

echo "desea descargar el proyecto la ultima version del proyecto [y/n]"
read option

if  [ $option == "y" ]; then
	echo "descarga del proyecto"
	mkdir FabricaWeb
	cd FabricaWeb
	git clone https://github.com/tinojcvc/FabricaWeb
fi

echo "instalando mongodb"
apt-get install mongodb

echo "instalando python pip"
apt-get install python-pip

echo "instalando curl para peticiones get y post"
apt-get install curl

echo 'install python'
apt-get install build-dep python-imaging

pip install urllib3
pip install pillow

