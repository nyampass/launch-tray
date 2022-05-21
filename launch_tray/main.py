import os
import rumps
import json

rumps.debug_mode(True)

configure_path = os.path.expanduser("~/.launch-tray.json")
with open(configure_path, encoding="utf-8", mode="r") as f:
    menus = json.load(f)

processes = [nil] * len(menus)

def register_menu(menu):
    @rumps.clicked(menu['name'])
    def clicked(_):
        app.title = menu['name']

for menu in menus:
    register_menu(menu)

app = rumps.App(name='', icon='resources/app.png', quit_button=rumps.MenuItem('Quit Launch Tray', key='q'))
app.menu = [item['name'] for item in menus]
app.run()
