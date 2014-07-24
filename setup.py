from distutils.core import setup
import py2exe
setup(name="Ejemplo Python de aplicación .exe",
	version="0.1",
	description="Ejemplo de ejecución de una aplicación Python con un fichero .exe",
	author="Grupo 6",
	author_email="nadie@nadie.com",
	url="www.anexpertforyou.com",
	license="GPL",
	scripts=["agenda.py", "bbdd.py", "Contacto.py", "Fichero.py", "menu.py", "Terminal.py", "u7_menu_argentino.py"],
	console=["agenda.py", "bbdd.py", "Contacto.py", "Fichero.py", "menu.py", "Terminal.py", "u7_menu_argentino.py"],
	platforms=["Win", "Mac", "Linux"],
	long_description = """Un texto largo iría aquí.""",
	options={"py2exe":{"bundle_files":1, "excludes": ['tkinter']}},
	zipfile=None
)