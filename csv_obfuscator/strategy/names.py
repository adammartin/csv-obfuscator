import random


__FIRST_NAMES__ = [
    'Aegnor',
    'Aerin',
    'Aina',
    'Aldon',
    'Alma',
    'Anna',
    'Aragorn',
    'Aredhel',
    'Arod',
    'Balin',
    'Baron',
    'Beleg',
    'Calen',
    'Callon',
    'Curdan',
    'Draug',
    'Earendil',
    'Elanor',
    'Elbereth',
    'Eldacar',
    'Eldarion',
    'Elladan',
    'Elrand',
    'Elrohir',
    'Elva',
    'Eowyn',
    'Eryn',
    'Estel',
    'Ethuil',
    'Galadriel',
    'Gandalf',
    'Garrett',
    'Gildor',
    'Glueredhel',
    'Haldir',
    'Haleth',
    'Idril',
    'Iorhael',
    'Iston',
    'Ithil',
    'Legolas',
    'Lia',
    'Lindir',
    'Logon',
    'Luthien',
    'Melian',
    'Mithrandir',
    'Morwen',
    'Nessa',
    'Nienna',
    'Perhael',
    'Poldo',
    'Rina',
    'Rohan',
    'Ronda',
    'Tara',
    'Tauriel',
    'Thalias',
    'Thalin',
    'Theoden',
    'Tinuviel',
    'Tuilu',
    'Voronwu',
    'Yavanna'
]

__LAST_NAMES__ = [
    'Aafje',
    'Albina',
    'Alfdus',
    'Alfiva',
    'Alfreda',
    'Alruna',
    'Alva',
    'Alvara',
    'Alvina',
    'Aubrette',
    'Aubriana',
    'Elba',
    'Elfie',
    'Elvene',
    'Elvinia',
    'Luell',
    'Nisse',
    'Odiane',
    'Siofra',
    'Aoibheann',
    'Dryadalis',
    'Livi',
    'Ordella',
    'Vilde',
    'Aranel',
    'Turi',
    'Brethil',
    'Varda',
    'Aelfraed',
    'Alberad',
    'Albwin',
    'Alf',
    'Alfie',
    'Alfur',
    'Alvin',
    'Batf',
    'Cutter',
    'Duwende',
    'Elegast',
    'Elfas',
    'Elving',
    'Elwyn',
    'Ingilvur',
    'Joralf',
    'Keijo',
    'Noralf',
    'Ysei',
    'Ailwi',
    'Algar',
    'Alvurs',
    'Duende',
    'Gunnalf',
    'Alary',
    'Albrun',
    'Alfsol',
    'Alvgjerd',
    'Alwine',
    'Ave',
    'Aveley',
    'Filifi',
    'Kukudh',
    'Oillill',
    'Parf',
    'Xelfai'
]


class FirstName:
    def __init__(self, arguments):
        self._strategy_type = arguments['strategy']

    # pylint: disable=unused-argument, no-self-use
    def obfuscate(self, value):
        return random.choice(__FIRST_NAMES__)
