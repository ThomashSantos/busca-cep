import buscacep.src.rpa.utilities.constants as const
import http.client
import csv


class ViaCep:

    def __init__(self) -> None:
        self.list_cep = []
        with open(const.CSV_PATH) as csv_file:
            file = csv.reader(csv_file, delimiter=',')
            [self.list_cep.append(cep[0]) for cep in file]

    def receive_address(self, cep: str) -> str:
        conn = http.client.HTTPConnection(const.URL_VIA_CEP)
        conn.request("GET", f"/ws/{cep}/xml")
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        return data
