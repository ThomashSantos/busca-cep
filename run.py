from buscacep.src.rpa.robot.notepad import NotepadAutomation
from buscacep.src.rpa.webservice.via_cep import ViaCep
from buscacep import logging


try:
    via = ViaCep()
    notepad = NotepadAutomation()
    for cep in via.list_cep:
        logging.info(f"Capture cep: {cep}")
        data = via.receive_address(cep)
        notepad.open_new_file()
        notepad.write_text(data)
        notepad.save_file(cep)
except Exception:
    logging.exception("Message")
else:
    logging.info("Proccess completed successfully")
finally:
    notepad.close_notepad()
