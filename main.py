import os
import json
import rumps

from launch_tray.menu import Menu

rumps.debug_mode(True)

configure_path = os.path.expanduser("~/.launch-tray.json")
with open(configure_path, encoding="utf-8", mode="r") as f:
    configure = json.load(f)

shell = configure['shell'] or '/bin/bash'
menus = [Menu(m['name'], m['exec'], shell) for m in configure['menus']]

def register_menu(menu):
    @rumps.clicked(menu.name)
    def clicked(m):
        menu.clicked()
        m.state = menu.checked

for menu in menus:
    register_menu(menu)

@rumps.timer(2)
def update_menu_state(_):
    for index, m in enumerate(app.menu.values()):
        if index < len(menus):
            menus[index].update()
            m.state = menus[index].checked

app = rumps.App(name='', icon='resources/app.png', quit_button=rumps.MenuItem('Quit Launch Tray', key='q'))
app.menu = [menu.name for menu in menus]
app.run()
