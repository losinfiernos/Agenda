from setuptools import setup
setup(name="Proyecto curso Python",
	version="0.1",
	description="Ejemplo de ejecución de una aplicación Python de agenda con entorno gráfico Tkinter",
	author="Grupo6",
	author_email="nadie@nadie.com",
	url="www.anexpertforyou.com",
	license="GPL",
	scripts=["agenda.py", "bbdd.py", "Contacto.py", "Fichero.py", "menu.py", "Terminal.py", "u7_menu_argentino.py"],
	platforms=["Win", "Mac", "Linux"],
	long_description = """Un texto largo iría aquí."""
)