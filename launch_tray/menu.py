from subprocess import Popen

class Menu:
    def __init__(self, name, exec):
        self.name = name
        self.exec = exec
        self.process = None

    def clicked(self):
        if self.process is None:
            self.process = Popen(["/bin/bash", "-c", self.exec])
            return
        self.terminate()
        self.process = None

    @property
    def checked(self):
        return self.process != None

    def update(self):
        if self.process is None:
            return
        self.process.poll()
        if self.process.returncode != None:
            self.process = None