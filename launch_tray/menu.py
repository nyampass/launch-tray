from subprocess import Popen

class Menu:
    def __init__(self, name, exec, shell):
        self.name = name
        self.exec = exec
        self.shell = shell
        self.process = None

    def toggle(self):
        if self.process is None:
            print([self.shell, "-c", self.exec])
            self.process = Popen([self.shell, "-c", self.exec])
            return
        self.process.terminate()
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