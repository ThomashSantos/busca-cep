from pywinauto.application import Application
import os


class NotepadAutomation:
    def __init__(self) -> None:
        self.app = Application().start("notepad.exe")
        self.notepad = self.app.window(class_name="Notepad")

    def write_text(self, text):
        self.notepad.Edit.set_text(text)

    def save_file(self, file_name):
        self.notepad.menu_select("Arquivo->Salvar")
        self.app.SalvarComo.edit.wait("visible")
        self.app.SalvarComo.edit.set_text(fr'{os.getcwd()}\buscacep\data\exit\{file_name}.xml')
        self.app.SalvarComo.Salvar.click()
        try:
            self.app.ConfirmarSalvarComo.wait('visible', timeout=2)
            self.app.ConfirmarSalvarComo.Sim.click()
        except Exception:
            ...

    def open_new_file(self):
        self.notepad.menu_select("Arquivo->Novo")

    def close_notepad(self):
        self.notepad.menu_select("Arquivo->Sair")
