echo "======================="
echo "instalando git para la descarga remota"
apt-get install git
echo "======================="

echo "======================="
echo "instalando libreiras de desarrollo para python"
apt-get build-dep python-imaging
echo "======================="

echo "desea descargar el proyecto la ultima version del proyecto [y/n]"
read option

if  [ $option == "y" ]; then
	echo "======================="
	echo "descarga del proyecto"
	mkdir FabricaWeb
	cd FabricaWeb
	git clone https://github.com/tinojcvc/FabricaWeb
	echo "======================="
fi

echo "======================="
echo "instalando mongodb"
apt-get install mongodb
echo "======================="

echo "======================="
echo "instalando python pip"
apt-get install python-pip
echo "======================="

echo "======================="
echo "instalando curl para peticiones get y post"
apt-get install curl
echo "======================="

echo "======================="
echo "instalando librerias necesarias para el proyecto"
pip install -r requirements.txt
echo "======================="

