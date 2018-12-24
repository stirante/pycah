import json

import requests

_CARDCAST_BASE_URL = "https://api.cardcastgame.com/v1/decks/"
_POLISH_CACHE = '{"name":"POLISH DUPA 1","code":"55HNH","description":"Dupa dupa dupa dupa dupa","unlisted":false,' \
                '"created_at":"2016-03-26T22:18:26+00:00","updated_at":"2017-12-28T17:04:11+00:00",' \
                '"external_copyright":false,"copyright_holder_url":null,"category":"other","call_count":"217",' \
                '"response_count":"491","author":{"id":"2c70c78a-3b18-4b65-a4d8-aba202834be8",' \
                '"username":"LordKroak"},"rating":"4.7"} '
_POLISH_CARDS_CACHE = """{
  "calls":[
    {
      "id":"0055dbc4-4632-4aa8-a3c1-77e99220b7a0",
      "text":[
        "Ni z gruszki, ni z ",
        "."
      ],
      "created_at":"2016-03-28T15:36:52+00:00",
      "nsfw":true
    },
    {
      "id":"011307b1-d1be-4107-be50-7f687a9eea93",
      "text":[
        "Kto ",
        " kopie, ten sam w nie wpada."
      ],
      "created_at":"2016-05-16T17:23:27+00:00",
      "nsfw":true
    },
    {
      "id":"02a9d997-b0c9-4ba3-97c9-2cf312f26f45",
      "text":[
        "",
        " ro\\u015bnie w miar\\u0119 jedzenia!"
      ],
      "created_at":"2016-03-28T15:31:07+00:00",
      "nsfw":true
    },
    {
      "id":"02ff87b2-5843-4180-8709-69c1333270ab",
      "text":[
        "Uczcijmy minut\\u0105 ciszy odej\\u015bcie ",
        ". Nasz brat i przyjaciel."
      ],
      "created_at":"2016-10-10T21:25:49+00:00",
      "nsfw":true
    },
    {
      "id":"037fa0bd-e7ad-4ca7-903b-f17d0bc9d67f",
      "text":[
        "Wpad\\u0142em jak \\u015bliwka w ",
        "."
      ],
      "created_at":"2016-03-26T22:52:03+00:00",
      "nsfw":true
    },
    {
      "id":"07bb1b61-3a03-4b30-bd5c-ea61c04a3e2b",
      "text":[
        "2\/",
        "=",
        ""
      ],
      "created_at":"2016-03-26T23:47:57+00:00",
      "nsfw":true
    },
    {
      "id":"0980a775-dd8b-4e7a-befd-6ac5a633aa86",
      "text":[
        "Staaaary, mam jutro klas\\u00f3wk\\u0119 z ",
        ". Nic nie umiem!"
      ],
      "created_at":"2016-10-10T20:59:24+00:00",
      "nsfw":true
    },
    {
      "id":"09fa3456-f398-4b9c-8e60-20c6bd5b93df",
      "text":[
        "Tak? Tak? Taki m\\u0105drala z Ciebie? To powiedz mi, jak cz\\u0119sto mia\\u0142e\\u015b ",
        " w ",
        "."
      ],
      "created_at":"2016-10-10T20:49:38+00:00",
      "nsfw":true
    },
    {
      "id":"0a53f6f9-7cde-4fd8-b93a-684478fd5318",
      "text":[
        "Przysz\\u0142a koza do ",
        "."
      ],
      "created_at":"2016-03-26T22:31:51+00:00",
      "nsfw":true
    },
    {
      "id":"0b3a5ad7-6001-4e81-aa39-7d0c11f8548b",
      "text":[
        "Milcz jak m\\u00f3wisz do ",
        "!"
      ],
      "created_at":"2016-03-26T23:45:29+00:00",
      "nsfw":true
    },
    {
      "id":"0c1fc107-e4ea-41a4-a597-827174580685",
      "text":[
        "Lambert, Lambert ty ",
        "."
      ],
      "created_at":"2016-03-26T22:47:30+00:00",
      "nsfw":true
    },
    {
      "id":"0d32629a-06ae-4d5d-a76d-cf9c2c7e2760",
      "text":[
        "Co, kurwa?! O co zak\\u0142ad?! O ",
        "!"
      ],
      "created_at":"2016-10-10T20:57:31+00:00",
      "nsfw":true
    },
    {
      "id":"12f806e4-56ee-418e-bc16-19d0e0ab08db",
      "text":[
        "Pi\\u0119kny obraz, ale dlaczego namalowa\\u0142e\\u015b akurat ",
        "?"
      ],
      "created_at":"2016-06-14T15:35:16+00:00",
      "nsfw":true
    },
    {
      "id":"1372abfb-c781-4760-ae08-91258e1a4055",
      "text":[
        "M\\u00f3j ulubiony raper to MC ",
        ". Mam wszystkie jego p\\u0142yty."
      ],
      "created_at":"2017-10-06T15:04:17+00:00",
      "nsfw":true
    },
    {
      "id":"1386c4a1-0566-42da-bb0e-a610f2f2652c",
      "text":[
        "Kiedy by\\u0142em na wojnie, zamiast ostrej amunicji u\\u017cywali\\u015bmy ",
        "!"
      ],
      "created_at":"2016-06-14T15:34:46+00:00",
      "nsfw":true
    },
    {
      "id":"13d691b3-626c-4a1d-b325-6a1a4e47c7b1",
      "text":[
        "Masz problemy z ",
        "? Wypr\\u00f3buj ",
        "!"
      ],
      "created_at":"2016-03-26T22:36:52+00:00",
      "nsfw":true
    },
    {
      "id":"1596ee32-9c1f-4a1b-a2bd-d30fc06eb6be",
      "text":[
        "Lubi\\u0119 czasami w\\u0142o\\u017cy\\u0107 ",
        " w ",
        "."
      ],
      "created_at":"2016-03-27T00:02:09+00:00",
      "nsfw":true
    },
    {
      "id":"1635d651-40ab-4fc0-b41f-b5dd88ae5c85",
      "text":[
        "Sraty taty dupa w ",
        "."
      ],
      "created_at":"2016-10-10T21:57:59+00:00",
      "nsfw":true
    },
    {
      "id":"176884ed-7a9a-450d-b0fe-c83837412abe",
      "text":[
        "Biega, krzyczy Pan Hilary: \\\"Gdzie s\\u0105 moje ",
        "?\\\""
      ],
      "created_at":"2016-03-26T22:27:04+00:00",
      "nsfw":true
    },
    {
      "id":"19471595-65bb-4f6f-8d6e-766db1e50509",
      "text":[
        "G\\u0142askanie psa pod ",
        "."
      ],
      "created_at":"2016-03-26T23:54:25+00:00",
      "nsfw":true
    },
    {
      "id":"19db2f34-39df-4f02-ab6b-be4999ded738",
      "text":[
        "Co Bogus\\u0142aw Linda jad\\u0142 na obiad? ",
        "."
      ],
      "created_at":"2016-03-26T23:49:08+00:00",
      "nsfw":true
    },
    {
      "id":"1a0a59b7-e5c6-4a29-af6e-f9916d4a1dfe",
      "text":[
        "Trafi\\u0107 z ",
        " pod ",
        "."
      ],
      "created_at":"2016-03-28T15:39:59+00:00",
      "nsfw":true
    },
    {
      "id":"1b1ba64a-4dc5-4b7f-be78-3a4d4fcb4443",
      "text":[
        "Nie uwierzysz!Wys\\u0142a\\u0142am go po szynk\\u0119, a kupi\\u0142 ",
        "!"
      ],
      "created_at":"2016-10-10T21:28:46+00:00",
      "nsfw":true
    },
    {
      "id":"1b5c6950-4f8a-4cc3-9db2-3ac4cc77810d",
      "text":[
        "Hola, hola! Co tam chowasz w tym plecaku?! Marcinku!!! Czy to ",
        "?!"
      ],
      "created_at":"2016-10-13T21:28:48+00:00",
      "nsfw":true
    },
    {
      "id":"1efc3942-a231-4b9d-9698-98dd75f92d1a",
      "text":[
        "Wiem! Zrobimy gr\\u0119 o ",
        "! To b\\u0119dzie arcydzie\\u0142o!"
      ],
      "created_at":"2016-10-10T21:37:46+00:00",
      "nsfw":true
    },
    {
      "id":"20a64ae6-3a7b-41b9-8bb5-c84f7befcdc2",
      "text":[
        "Kwiecie\\u0144 - plenie\\u0144, co przeplata, troch\\u0119 ",
        ", troch\\u0119 ",
        "."
      ],
      "created_at":"2016-03-28T15:35:43+00:00",
      "nsfw":true
    },
    {
      "id":"23312d7a-f8b4-440d-b657-542463814ed0",
      "text":[
        "Czym\\u017ce jest mi\\u0142o\\u015b\\u0107 bez ",
        "?"
      ],
      "created_at":"2016-03-27T00:06:39+00:00",
      "nsfw":true
    },
    {
      "id":"23ccf4dd-86ae-477c-bbba-9876c6679076",
      "text":[
        "Wysz\\u0142o ",
        " z worka."
      ],
      "created_at":"2016-03-26T22:31:57+00:00",
      "nsfw":true
    },
    {
      "id":"263cdb8c-e48e-4d76-be26-d2a1d3e657a0",
      "text":[
        "Go, go Power ",
        "!"
      ],
      "created_at":"2016-03-27T00:08:10+00:00",
      "nsfw":true
    },
    {
      "id":"269c1ba7-a708-47cb-9578-a2b7d1eeda62",
      "text":[
        "Pana ",
        " wskazuje na b\\u00f3l w okolicach ",
        "."
      ],
      "created_at":"2016-06-14T15:32:00+00:00",
      "nsfw":true
    },
    {
      "id":"26f6c1c8-bdaa-4088-b238-2e69c9390392",
      "text":[
        "Jedna ",
        " wiosny nie czyni."
      ],
      "created_at":"2016-03-28T15:34:22+00:00",
      "nsfw":true
    },
    {
      "id":"2747c1e5-372c-42ac-a5cd-a9ec05456804",
      "text":[
        "Co ma piernik do ",
        "?"
      ],
      "created_at":"2016-03-28T15:32:08+00:00",
      "nsfw":true
    },
    {
      "id":"275574de-363f-4a86-b5f9-b5a38b0a7b22",
      "text":[
        "S\\u0142ucham r\\u00f3\\u017cnych zespo\\u0142\\u00f3w... Metallica, Slayer, Testament, ",
        "."
      ],
      "created_at":"2016-10-10T21:33:08+00:00",
      "nsfw":true
    },
    {
      "id":"2818257e-8dcd-4682-b4f5-9e8b71d7283e",
      "text":[
        "",
        "! Pi\\u0105tka stary!"
      ],
      "created_at":"2016-03-26T23:47:14+00:00",
      "nsfw":true
    },
    {
      "id":"2a2da261-bb66-4b8b-8351-bfceddcaa71e",
      "text":[
        "Puk, puk. Kto tam? ",
        "."
      ],
      "created_at":"2016-03-26T22:57:40+00:00",
      "nsfw":true
    },
    {
      "id":"2c5cdde5-bc36-4c52-b44b-b3bfb2fd8dff",
      "text":[
        "Nie jest dobrze, moi bracia. Nasta\\u0142a era ",
        " i ",
        "."
      ],
      "created_at":"2016-10-10T21:04:30+00:00",
      "nsfw":true
    },
    {
      "id":"2d1c5f52-2579-408e-8318-dd5b229067b6",
      "text":[
        "Mam 2 minuty na ",
        "?! Okeeeeej, bez problemu!"
      ],
      "created_at":"2016-10-10T21:13:04+00:00",
      "nsfw":true
    },
    {
      "id":"2d62d7d4-e089-4f43-a62d-4f8de4c51397",
      "text":[
        "",
        " u\\u017cyj ",
        "!"
      ],
      "created_at":"2016-03-26T23:47:29+00:00",
      "nsfw":true
    },
    {
      "id":"328718bd-b8ab-4072-92a2-ec3a8cc9438c",
      "text":[
        "Nie martw si\\u0119! Czasami ",
        " rdzewiej\\u0105!"
      ],
      "created_at":"2017-12-28T17:04:11+00:00",
      "nsfw":true
    },
    {
      "id":"33c97db1-e763-498b-b416-1cce92fa8859",
      "text":[
        "Jako moj\\u0105 nast\\u0119pn\\u0105 sztuczk\\u0119 wyci\\u0105gn\\u0119 ",
        " z ",
        "."
      ],
      "created_at":"2016-03-26T23:46:43+00:00",
      "nsfw":true
    },
    {
      "id":"342c7d23-0162-4580-b38f-57d66c05f431",
      "text":[
        "Zap\\u0142aci\\u0142bym wiele, \\u017ceby zobaczy\\u0107 ",
        "."
      ],
      "created_at":"2016-03-27T15:09:44+00:00",
      "nsfw":true
    },
    {
      "id":"34462275-a2ff-4ed1-83a5-81f4bafc664d",
      "text":[
        "",
        " umiera, ",
        " zostaje."
      ],
      "created_at":"2016-05-16T17:21:53+00:00",
      "nsfw":true
    },
    {
      "id":"374062c6-eed5-4ff3-bdfe-fcba42c2ddc3",
      "text":[
        "Na pocz\\u0105tku by\\u0142 ",
        ". Potem B\\u00f3g rzek\\u0142: \\\"Niech stanie si\\u0119 ",
        "!\\\""
      ],
      "created_at":"2016-03-26T22:39:27+00:00",
      "nsfw":true
    },
    {
      "id":"38d4190a-89f0-49d0-aed9-0d1076c2ee94",
      "text":[
        "Grosz do grosza, a b\\u0119dzie ",
        "."
      ],
      "created_at":"2016-03-28T15:33:29+00:00",
      "nsfw":true
    },
    {
      "id":"3a6ed724-f728-4dd5-85bb-fdea84eb5f00",
      "text":[
        "Chcesz mo\\u017ce kupi\\u0107 troch\\u0119 ",
        "? Towar najlepszy w mie\\u015bcie."
      ],
      "created_at":"2016-06-14T15:31:21+00:00",
      "nsfw":true
    },
    {
      "id":"3b38f78d-8258-414a-a5c2-6965cabf6d09",
      "text":[
        "No, no, no, male\\u0144ka! Jeste\\u015b gotowa na prawdziwe ",
        "?"
      ],
      "created_at":"2016-06-14T15:40:10+00:00",
      "nsfw":true
    },
    {
      "id":"3ce7eda9-eca5-4069-bcd2-127f5d44c819",
      "text":[
        "M\\u00f3j Bo\\u017ce! Jak ja kocham ",
        "!"
      ],
      "created_at":"2016-03-27T15:08:51+00:00",
      "nsfw":true
    },
    {
      "id":"3e8d6f82-f837-4b57-87b4-87a2ece4b2e6",
      "text":[
        "Co jest zabawne dop\\u00f3ki nie stanie si\\u0119 dziwne? ",
        "."
      ],
      "created_at":"2016-03-26T22:39:02+00:00",
      "nsfw":true
    },
    {
      "id":"3eb69c12-0750-4313-95e2-14f209ca5db9",
      "text":[
        "Przygoda, romans, ",
        "."
      ],
      "created_at":"2016-03-26T22:39:38+00:00",
      "nsfw":true
    },
    {
      "id":"3f53134c-0a96-4248-969e-474275892ddb",
      "text":[
        "",
        " zniszczy\\u0142o dzieci\\u0144stwo wielu ludzi."
      ],
      "created_at":"2016-03-27T00:06:00+00:00",
      "nsfw":true
    },
    {
      "id":"4002e988-9788-4112-b124-76c8f8aefaf4",
      "text":[
        "Doda\\u0142em do zupy ",
        ", a co? Nie smakuje?"
      ],
      "created_at":"2016-10-10T21:49:33+00:00",
      "nsfw":true
    },
    {
      "id":"428f1999-ad33-48f1-81a2-930d574a9b26",
      "text":[
        "",
        " to najlepszy prezent na dzie\\u0144 dziecka!"
      ],
      "created_at":"2016-03-27T15:15:51+00:00",
      "nsfw":true
    },
    {
      "id":"42fad2c6-cccb-412d-a82c-397d4394e86b",
      "text":[
        "Leje jak z ",
        "."
      ],
      "created_at":"2016-03-28T15:35:54+00:00",
      "nsfw":true
    },
    {
      "id":"4329e26c-93ac-42e0-bea3-97db1f0ad7b5",
      "text":[
        "Albo rybki, albo ",
        "."
      ],
      "created_at":"2016-05-16T17:20:47+00:00",
      "nsfw":true
    },
    {
      "id":"434e0c08-8499-40d2-802f-8570b1cf0341",
      "text":[
        "W przysz\\u0142o\\u015bci b\\u0119d\\u0119 zajmowa\\u0107 si\\u0119 ",
        "."
      ],
      "created_at":"2016-03-26T23:48:18+00:00",
      "nsfw":true
    },
    {
      "id":"44fb1c70-b62f-4e40-9168-a33e10d6badf",
      "text":[
        "Ma\\u0142e dzieci - ma\\u0142y k\\u0142opot, du\\u017ce dzieci - ",
        "."
      ],
      "created_at":"2016-03-28T15:36:24+00:00",
      "nsfw":true
    },
    {
      "id":"4520fd06-1611-4b38-902f-6bc518801011",
      "text":[
        "Hahahha! No co Ty?! Przecie\\u017c ka\\u017cdy wie, \\u017ce Marcin lubi ",
        "!"
      ],
      "created_at":"2016-10-10T21:00:24+00:00",
      "nsfw":true
    },
    {
      "id":"462fabbb-a811-42ca-83f2-fc05561b357a",
      "text":[
        "Nie uwierzysz, co ostatnio przyni\\u00f3s\\u0142 mi m\\u00f3j pies! ",
        "!!!!!"
      ],
      "created_at":"2016-10-10T21:16:14+00:00",
      "nsfw":true
    },
    {
      "id":"4bc11f75-4a3c-4269-9511-686d5dcba7ed",
      "text":[
        "Zawsze m\\u00f3wi\\u0142em, \\u017ce ",
        " jest dobrym pomys\\u0142em na",
        "."
      ],
      "created_at":"2016-03-26T22:57:24+00:00",
      "nsfw":true
    },
    {
      "id":"4bdb27f5-40a8-48e4-9335-9907c3491d86",
      "text":[
        "",
        " przeminie, ale ",
        " przetrwa wiecznie."
      ],
      "created_at":"2016-03-26T22:40:00+00:00",
      "nsfw":true
    },
    {
      "id":"4cea95f1-dae9-4eaf-8121-5f70236e9ff2",
      "text":[
        "Dzieci przepadaj\\u0105 za ",
        " i s\\u0142odyczami."
      ],
      "created_at":"2016-10-10T20:47:44+00:00",
      "nsfw":true
    },
    {
      "id":"4d6b7d42-3941-4351-bbf2-e1708cc030f1",
      "text":[
        "Moja matka zawsze powtarza\\u0142a: \\\"Zjedz mi\\u0119so, zostaw ",
        "\\\""
      ],
      "created_at":"2016-10-10T20:55:12+00:00",
      "nsfw":true
    },
    {
      "id":"4e35c42f-3730-4c92-9595-bb25a82db0f1",
      "text":[
        "Borys, Ty \\u0142achudro! Hahaha! Da\\u0142e\\u015b mi ",
        " zamiast ",
        "!"
      ],
      "created_at":"2016-10-10T20:48:46+00:00",
      "nsfw":true
    },
    {
      "id":"4e4e8f8f-9a63-4c57-9dfa-e975d023e1bd",
      "text":[
        "Co z oczu to z ",
        "."
      ],
      "created_at":"2016-03-26T22:27:34+00:00",
      "nsfw":true
    },
    {
      "id":"4faa5b79-d02b-405e-8678-cecee4a18616",
      "text":[
        "Co za du\\u017co to nie ",
        "."
      ],
      "created_at":"2016-03-26T22:27:55+00:00",
      "nsfw":true
    },
    {
      "id":"5012475f-4726-42c5-a8b3-92a060333798",
      "text":[
        "Talon na ",
        " i ",
        "."
      ],
      "created_at":"2016-03-26T23:05:30+00:00",
      "nsfw":true
    },
    {
      "id":"508d202e-0987-4cab-92f1-094f0c68e216",
      "text":[
        "Przewaga dzi\\u0119ki ",
        "."
      ],
      "created_at":"2016-03-26T23:51:25+00:00",
      "nsfw":true
    },
    {
      "id":"509e2509-f895-44c2-bb04-6164a30f66ec",
      "text":[
        "Mia\\u0142em dzi\\u015b wyk\\u0142ady z ",
        ". Straszna nuda."
      ],
      "created_at":"2016-10-10T21:36:35+00:00",
      "nsfw":true
    },
    {
      "id":"54e13141-defb-496e-862f-cb5c7dd1fbb8",
      "text":[
        "Moja ulubiona pozycja nazywa si\\u0119 ",
        "."
      ],
      "created_at":"2016-03-27T15:08:28+00:00",
      "nsfw":true
    },
    {
      "id":"5583f579-e015-48ac-af6d-c137ceeeae7b",
      "text":[
        "Lew, czarownica i ",
        "."
      ],
      "created_at":"2016-03-27T00:07:35+00:00",
      "nsfw":true
    },
    {
      "id":"55e0fc09-b5c8-41b7-9824-7854ae31caaf",
      "text":[
        "",
        " wybieram Ci\\u0119!"
      ],
      "created_at":"2016-03-26T23:47:21+00:00",
      "nsfw":true
    },
    {
      "id":"56036384-56cc-46e7-8c64-c1903b849e64",
      "text":[
        "Twoje wiert\\u0142o potrafi przebi\\u0107 nawet ",
        "."
      ],
      "created_at":"2016-03-27T00:01:58+00:00",
      "nsfw":true
    },
    {
      "id":"56a898f3-4ca9-420f-b183-280960e1608b",
      "text":[
        "W pokoiku na stoliku sta\\u0142o ",
        " i ",
        "."
      ],
      "created_at":"2016-03-27T00:17:11+00:00",
      "nsfw":true
    },
    {
      "id":"57abcbd6-c8f8-4e81-a384-f6f4d8cb75ac",
      "text":[
        "Strach ma wielkie ",
        "."
      ],
      "created_at":"2016-03-28T15:38:46+00:00",
      "nsfw":true
    },
    {
      "id":"59a10bc4-814b-4353-b9c2-bfdf50aa63df",
      "text":[
        "Nie wywo\\u0142uj ",
        " z lasu."
      ],
      "created_at":"2016-03-28T15:38:00+00:00",
      "nsfw":true
    },
    {
      "id":"5d753054-bc6c-4fb6-a279-7540baa33eca",
      "text":[
        "Pasuje jak ",
        " do ",
        "."
      ],
      "created_at":"2016-03-26T22:31:41+00:00",
      "nsfw":true
    },
    {
      "id":"5d78834d-6da3-4332-a3c2-b0dd81d9b1bb",
      "text":[
        "Od ",
        " g\\u0142owa nie boli."
      ],
      "created_at":"2016-03-28T15:38:12+00:00",
      "nsfw":true
    },
    {
      "id":"5db97d32-8bea-4cb7-bde5-86a6dc13250f",
      "text":[
        "Mosi\\u0105dz - stop miedzi i ",
        ", zawieraj\\u0105cy 10\\u201345% cynku."
      ],
      "created_at":"2017-10-06T15:05:40+00:00",
      "nsfw":true
    },
    {
      "id":"5e67ab58-ac1c-437a-8dde-f6ce19d1499b",
      "text":[
        "Mo\\u017cesz mi possa\\u0107 ",
        "."
      ],
      "created_at":"2016-03-27T00:09:06+00:00",
      "nsfw":true
    },
    {
      "id":"5e85d8ab-485d-431d-9379-3a76f04cfcd8",
      "text":[
        "Ogie\\u0144, woda, ziemia, ",
        "."
      ],
      "created_at":"2016-03-26T22:25:49+00:00",
      "nsfw":true
    },
    {
      "id":"6011d894-96f6-4f89-a618-0b5adb6095e3",
      "text":[
        "",
        " to pu\\u0142apka!"
      ],
      "created_at":"2016-03-26T23:47:36+00:00",
      "nsfw":true
    },
    {
      "id":"610f71db-48f9-4f4b-909a-7f90daa852c7",
      "text":[
        "Opowiem Wam o ",
        " na nast\\u0119pnej lekcji. Obiecuj\\u0119!"
      ],
      "created_at":"2016-10-10T20:59:00+00:00",
      "nsfw":true
    },
    {
      "id":"61f5c397-dea7-45f3-a207-e4d3b89f77c0",
      "text":[
        "Zn\\u00f3w makaron?! Przecie\\u017c m\\u00f3wi\\u0142em, \\u017ce mam ochot\\u0119 na ",
        "!"
      ],
      "created_at":"2016-10-10T21:00:56+00:00",
      "nsfw":true
    },
    {
      "id":"647e8510-f87a-45ce-bd12-cfbb774c3f08",
      "text":[
        "Wi\\u0119cej ni\\u017c jedno zwierze to ",
        "."
      ],
      "created_at":"2016-03-27T00:03:30+00:00",
      "nsfw":true
    },
    {
      "id":"6524bdd4-2b14-48f0-a122-f6a1f812f7bb",
      "text":[
        "",
        " jest najlepsz\\u0105 obron\\u0105."
      ],
      "created_at":"2016-05-16T17:21:07+00:00",
      "nsfw":true
    },
    {
      "id":"6654068b-48a5-45be-988a-a542418bed69",
      "text":[
        "Tak, s\\u0142ysza\\u0142em. Widzia\\u0142em ich ostatnio razem i gadali o ",
        "."
      ],
      "created_at":"2016-10-10T21:00:41+00:00",
      "nsfw":true
    },
    {
      "id":"67f9226f-15ec-406a-af2d-4d91601e35c1",
      "text":[
        "Gdy zobaczy\\u0142em ",
        ", to krew odp\\u0142yn\\u0119\\u0142a mi z ",
        "."
      ],
      "created_at":"2016-03-27T00:05:35+00:00",
      "nsfw":true
    },
    {
      "id":"6a804396-b21a-4d01-9671-3805d52ec4d8",
      "text":[
        "Cierpi\\u0119 na rzadk\\u0105 chorob\\u0119 o nazwie ",
        "."
      ],
      "created_at":"2016-06-18T12:29:15+00:00",
      "nsfw":true
    },
    {
      "id":"6abad42c-5fc1-48f9-a2bf-f258306e2412",
      "text":[
        "Polacy nie ",
        " i sw\\u00f3j ",
        " maj\\u0105."
      ],
      "created_at":"2016-03-27T00:04:28+00:00",
      "nsfw":true
    },
    {
      "id":"6b43e92b-ab10-47d6-ac64-ccaa3dd02b36",
      "text":[
        "Niech to ",
        " strzeli!"
      ],
      "created_at":"2016-03-26T22:53:49+00:00",
      "nsfw":true
    },
    {
      "id":"6c4855a9-7e2f-4a34-947a-fb8e207acb84",
      "text":[
        "Kto ",
        " wojuje, ten od ",
        " ginie."
      ],
      "created_at":"2016-05-16T17:24:03+00:00",
      "nsfw":true
    },
    {
      "id":"6cef81ac-2cf8-4f8b-96c9-b43b64d8a869",
      "text":[
        "Janusz \\\"",
        "\\\" Pogorzelski to najlepszy gracz Virtus.pro!"
      ],
      "created_at":"2017-10-06T15:08:50+00:00",
      "nsfw":true
    },
    {
      "id":"6d50870c-1a0b-4568-886c-f13e148c1fc3",
      "text":[
        "W podstaw\\u00f3wce m\\u00f3wili na mnie \\\"",
        "\\\". Do dzi\\u015b nie wiem dlaczego."
      ],
      "created_at":"2017-10-06T15:06:09+00:00",
      "nsfw":true
    },
    {
      "id":"6ddadd9a-ecf3-4fb4-a654-0e133d237f2e",
      "text":[
        "Tato, dlaczego mama p\\u0142acze? ",
        "."
      ],
      "created_at":"2016-03-27T00:02:20+00:00",
      "nsfw":true
    },
    {
      "id":"6fdfefbe-7ea9-404d-9859-45b95a2b480c",
      "text":[
        "Tylko dwie rzeczy w \\u017cyciu s\\u0105 pewne: \\u015bmier\\u0107 i ",
        "."
      ],
      "created_at":"2016-03-26T22:25:20+00:00",
      "nsfw":true
    },
    {
      "id":"72294d84-bcd9-4e06-af26-7f89d370ce74",
      "text":[
        "Nauczy\\u0142em Lun\\u0119 nowej sztuczki! Nazwa\\u0142em j\\u0105 ",
        "!"
      ],
      "created_at":"2016-10-10T21:41:16+00:00",
      "nsfw":true
    },
    {
      "id":"72a06510-7acd-415e-937b-35e5d9c382c1",
      "text":[
        "Kaktus z ",
        " zamiast igie\\u0142."
      ],
      "created_at":"2016-03-26T23:58:08+00:00",
      "nsfw":true
    },
    {
      "id":"7485f9dd-4b26-45f3-9a2f-3f9b35534a58",
      "text":[
        "B\\u00f3g, honor, ",
        "!"
      ],
      "created_at":"2016-05-16T17:24:18+00:00",
      "nsfw":true
    },
    {
      "id":"754afa42-a40a-4eba-aecd-8c9bc193a0e4",
      "text":[
        "Nawet nie wiesz, jak bardzo brakuje mi ",
        ".  Tak bardzo t\\u0119skni\\u0119."
      ],
      "created_at":"2016-10-10T21:31:21+00:00",
      "nsfw":true
    },
    {
      "id":"75a6cf40-58d2-4343-9f46-5fbc8f198756",
      "text":[
        "Darowanemu koniowi w ",
        " si\\u0119 nie zagl\\u0105da."
      ],
      "created_at":"2016-03-28T15:32:45+00:00",
      "nsfw":true
    },
    {
      "id":"776b0b14-9d15-401d-b19d-3b8dc4ab7dd8",
      "text":[
        "Bez pracy nie ma ",
        "."
      ],
      "created_at":"2016-06-14T15:26:56+00:00",
      "nsfw":true
    },
    {
      "id":"7a346dce-78c7-4b0c-84b0-fc838c56b3ed",
      "text":[
        "Koniec! Do\\u015b\\u0107! Nie rozmawiamy wi\\u0119cej o ",
        "!"
      ],
      "created_at":"2016-10-10T21:34:35+00:00",
      "nsfw":true
    },
    {
      "id":"7a96a288-9f39-492c-8431-1d9c91f65ddb",
      "text":[
        "Zgoda buduje, ",
        " rujnuje."
      ],
      "created_at":"2016-03-28T15:41:42+00:00",
      "nsfw":true
    },
    {
      "id":"7b9232d6-34c6-423a-b248-f247a9323e0f",
      "text":[
        "B\\u00f3g mnie kocha za ",
        ","
      ],
      "created_at":"2016-03-27T00:05:50+00:00",
      "nsfw":true
    },
    {
      "id":"7bd15414-39fb-44f3-a487-936ffd2febb1",
      "text":[
        "Ty. Ja. ",
        ". Teraz!"
      ],
      "created_at":"2016-03-27T15:11:54+00:00",
      "nsfw":true
    },
    {
      "id":"7c84f645-009e-4fa6-ae89-dc219438f9bd",
      "text":[
        "Wpierdol t\\u0119 ",
        " do dupy kurczaka!"
      ],
      "created_at":"2016-10-10T21:20:43+00:00",
      "nsfw":true
    },
    {
      "id":"7cc518a4-e76b-4aba-8bef-e419cb26b0a1",
      "text":[
        "Zjedz ",
        ", zostaw ziemniaki."
      ],
      "created_at":"2016-03-26T22:33:32+00:00",
      "nsfw":true
    },
    {
      "id":"7e540a26-4ad0-4c8a-9364-64ad18870788",
      "text":[
        "M\\u00f3wisz Adamie, \\u017ce\\u015b narodu wieszczem, a tak naprawd\\u0119 jeste\\u015b ",
        "."
      ],
      "created_at":"2016-03-26T23:53:01+00:00",
      "nsfw":true
    },
    {
      "id":"7ef10268-ebc6-4fd4-b05b-746748f7126f",
      "text":[
        "Peda\\u0142y ju\\u017c tam s\\u0105 i kradn\\u0105 ",
        "."
      ],
      "created_at":"2016-03-26T23:04:52+00:00",
      "nsfw":true
    },
    {
      "id":"7f47fcb5-7627-4193-b6ee-72af5ae9044d",
      "text":[
        "Co dwie ",
        ", to nie jedna."
      ],
      "created_at":"2016-03-28T15:31:51+00:00",
      "nsfw":true
    },
    {
      "id":"8069bd9e-7c27-4f81-861c-dd016132cf32",
      "text":[
        "Piotrek, ratuj! Zn\\u00f3w obrazi\\u0142a si\\u0119 o ",
        "!"
      ],
      "created_at":"2016-10-10T21:51:23+00:00",
      "nsfw":true
    },
    {
      "id":"85b150f7-e7a6-4d41-991c-af36105c7782",
      "text":[
        "Radowid to ",
        "!"
      ],
      "created_at":"2016-03-26T22:48:47+00:00",
      "nsfw":true
    },
    {
      "id":"86de5b76-638d-4e56-95ab-b3dfbe4dd223",
      "text":[
        "",
        " - to droga do serca m\\u0119\\u017cczyzny."
      ],
      "created_at":"2016-03-26T22:29:10+00:00",
      "nsfw":true
    },
    {
      "id":"89fe1f2f-77e1-4249-aecb-f084399b27b1",
      "text":[
        "sin(",
        ")"
      ],
      "created_at":"2016-03-26T23:47:03+00:00",
      "nsfw":true
    },
    {
      "id":"8b4b2f4d-f0c0-4b44-ba03-f13de88b77db",
      "text":[
        "Wybacz, mamo, ale wygl\\u0105dasz dzi\\u015b jak ",
        "."
      ],
      "created_at":"2016-06-14T15:40:33+00:00",
      "nsfw":true
    },
    {
      "id":"8cc24aa7-c1c4-44f0-84ed-5f821da437da",
      "text":[
        "Nie \\u017cyj\\u0119 dla krotochwil. \\u017byj\\u0119 dla ",
        "."
      ],
      "created_at":"2016-10-10T20:54:36+00:00",
      "nsfw":true
    },
    {
      "id":"8cd88035-1f2a-41dc-b91b-2007b66a1851",
      "text":[
        "Tw\\u00f3j ",
        " jest twardy jak ",
        "!"
      ],
      "created_at":"2016-03-27T00:15:18+00:00",
      "nsfw":true
    },
    {
      "id":"8d32a180-8f0d-4326-a6c5-ba46fb9196da",
      "text":[
        "Ile razy mam Ci m\\u00f3wi\\u0107, \\u017ce ",
        " to nie zabawka."
      ],
      "created_at":"2016-03-26T22:34:00+00:00",
      "nsfw":true
    },
    {
      "id":"8d738f33-1978-4360-8566-0c7d9d1b57c1",
      "text":[
        "",
        " r\\u00f3wnie dobrze m\\u00f3g\\u0142by oznacza\\u0107 ",
        "."
      ],
      "created_at":"2016-03-26T23:03:17+00:00",
      "nsfw":true
    },
    {
      "id":"8dd8d28d-993c-4610-9b67-08f3cbf6e778",
      "text":[
        "Laski zawsze lec\\u0105 na ",
        "."
      ],
      "created_at":"2016-03-26T22:41:00+00:00",
      "nsfw":true
    },
    {
      "id":"8e2b00d2-4ca8-48c9-bf14-0038abca5c4d",
      "text":[
        "Przed lekcj\\u0105 napisali\\u015bmy na tablicy \\\"",
        "\\\". Nauczycielka by\\u0142a w\\u015bciek\\u0142a!"
      ],
      "created_at":"2017-10-06T15:03:51+00:00",
      "nsfw":true
    },
    {
      "id":"8ef944e5-ec38-4917-899b-9143e55ec036",
      "text":[
        "Nie wszystko ",
        ", co si\\u0119 \\u015bwieci."
      ],
      "created_at":"2016-03-28T15:37:44+00:00",
      "nsfw":true
    },
    {
      "id":"91057268-5feb-4294-9645-2543806b231a",
      "text":[
        "Prawdziwi ",
        "! Nie jacy\\u015b podrabia\\u0144cy!"
      ],
      "created_at":"2016-03-26T23:50:13+00:00",
      "nsfw":true
    },
    {
      "id":"918cef2c-0f22-44a4-a7d4-0f019aea4c14",
      "text":[
        "Mowa jest ",
        ", a milczenie ",
        "."
      ],
      "created_at":"2016-03-28T15:36:39+00:00",
      "nsfw":true
    },
    {
      "id":"944df516-2207-4f05-8c6f-3160f6580e43",
      "text":[
        "Normalnie nie zwracam uwagi na ",
        ", ale teraz to kurwa nie da\\u0142em rady."
      ],
      "created_at":"2016-10-10T21:47:20+00:00",
      "nsfw":true
    },
    {
      "id":"949fcbff-5318-4b34-9d86-923e4787c1ed",
      "text":[
        "Co trzymasz w chlebaku? ",
        "."
      ],
      "created_at":"2016-03-27T15:09:18+00:00",
      "nsfw":true
    },
    {
      "id":"95327569-89b3-43aa-b110-c7ae698ee421",
      "text":[
        "Przysz\\u0142a kryska na ",
        "."
      ],
      "created_at":"2016-03-28T15:38:26+00:00",
      "nsfw":true
    },
    {
      "id":"955e5763-4e8e-49a8-9d78-bc0f94d53936",
      "text":[
        "Nowy Stadion Narodowy ma jeden problem... ",
        "."
      ],
      "created_at":"2016-10-10T21:30:04+00:00",
      "nsfw":true
    },
    {
      "id":"9598b408-a2ee-48f2-863a-7c3f904a096f",
      "text":[
        "Hej. Pami\\u0119tasz mo\\u017ce jak m\\u00f3wi\\u0142o si\\u0119 na aborcj\\u0119 turbanem? ",
        "."
      ],
      "created_at":"2016-03-26T23:03:05+00:00",
      "nsfw":true
    },
    {
      "id":"95c9112f-042f-44cb-b7b2-14cd8a2b02d9",
      "text":[
        "Nie ma murzyna i nie ma",
        "."
      ],
      "created_at":"2016-03-27T00:03:07+00:00",
      "nsfw":true
    },
    {
      "id":"95ef833c-4093-4f8c-bbd8-a3fb1e145f7c",
      "text":[
        "Cholerni bandyci! Ukradli moj\\u0105 ukochan\\u0105 ",
        "!"
      ],
      "created_at":"2016-10-10T22:00:45+00:00",
      "nsfw":true
    },
    {
      "id":"96d01141-3d3c-41a9-84c2-ba4b3406c015",
      "text":[
        "Kuj ",
        " p\\u00f3ki gor\\u0105ce."
      ],
      "created_at":"2016-03-28T15:35:00+00:00",
      "nsfw":true
    },
    {
      "id":"981c45d4-7eb7-4b30-b3be-e3b39ae47d2f",
      "text":[
        "Mo\\u017ce to jej urok, a mo\\u017ce to ",
        "."
      ],
      "created_at":"2016-03-26T23:51:11+00:00",
      "nsfw":true
    },
    {
      "id":"986b6e12-7a70-49cc-b869-ababab51ea1f",
      "text":[
        "Zaplanuj trzydniowy posi\\u0142ek: ",
        ", ",
        ", ",
        "."
      ],
      "created_at":"2016-03-27T00:07:20+00:00",
      "nsfw":true
    },
    {
      "id":"99475847-c6dd-4e29-a262-c2250d08402e",
      "text":[
        "Po\\u0142amania ",
        "!"
      ],
      "created_at":"2016-03-26T22:53:59+00:00",
      "nsfw":true
    },
    {
      "id":"997cbbc2-8257-41f5-8484-429964e38bcd",
      "text":[
        "Trafi\\u0142a kosa na ",
        "."
      ],
      "created_at":"2016-03-28T15:39:08+00:00",
      "nsfw":true
    },
    {
      "id":"999c9d17-f7b9-458b-bec8-7f6b0be65728",
      "text":[
        "Biednemu zawsze ",
        " w oczy."
      ],
      "created_at":"2016-03-28T15:31:20+00:00",
      "nsfw":true
    },
    {
      "id":"9add9720-5566-4ee1-8d0d-b08144620a09",
      "text":[
        "No \\u017ce\\u017c kurwa! Od kiedy ",
        " wygl\\u0105da dla Ciebie jak ",
        "?!"
      ],
      "created_at":"2016-06-14T15:38:28+00:00",
      "nsfw":true
    },
    {
      "id":"9b4318c7-3e9a-49a2-a860-8856eea01912",
      "text":[
        "Jak rzep do ",
        "."
      ],
      "created_at":"2016-03-26T22:34:42+00:00",
      "nsfw":true
    },
    {
      "id":"9e38b7f7-d3bc-42cc-97fd-7953d3d3ac17",
      "text":[
        "Czym jest ",
        " wobec \\u015bwiata?"
      ],
      "created_at":"2016-03-26T22:58:06+00:00",
      "nsfw":true
    },
    {
      "id":"a0498f9f-8df9-4079-9140-29670c240edc",
      "text":[
        "Ostatnio w\\u0142o\\u017cy\\u0142 w ",
        ". A nie chcia\\u0142am!"
      ],
      "created_at":"2016-10-10T21:15:27+00:00",
      "nsfw":true
    },
    {
      "id":"a2f6aad2-4927-4b58-a49a-e5acc2c815b8",
      "text":[
        "Uwielbiam j\\u0105, bo ma ",
        "."
      ],
      "created_at":"2016-03-26T22:41:12+00:00",
      "nsfw":true
    },
    {
      "id":"a405be4a-92b2-4486-b296-889d8ad70181",
      "text":[
        "Puk, puk! Kto tam? ",
        "!"
      ],
      "created_at":"2016-06-14T15:34:14+00:00",
      "nsfw":true
    },
    {
      "id":"a69e4093-5357-4889-a80a-eb27b53f3e8c",
      "text":[
        "Ostatnio przeczyta\\u0142em ksi\\u0105\\u017ck\\u0119 pt.: \\\"",
        "\\\". By\\u0142a \\u015bwietna!"
      ],
      "created_at":"2016-06-14T15:29:17+00:00",
      "nsfw":true
    },
    {
      "id":"a7182238-6dd9-49c7-82f5-f59d28ccc443",
      "text":[
        "A co je\\u015bli akurat nie b\\u0119d\\u0119 mia\\u0142 ochoty na ",
        "? Co wtedy?!"
      ],
      "created_at":"2016-10-10T21:09:45+00:00",
      "nsfw":true
    },
    {
      "id":"a78eebc1-8993-42ca-99a8-18c1580ae04d",
      "text":[
        "Co wyrzuci\\u0142o morze? ",
        "."
      ],
      "created_at":"2016-03-27T00:05:06+00:00",
      "nsfw":true
    },
    {
      "id":"a7901333-144a-4a0b-b0c7-89f73b843db3",
      "text":[
        "Bracia! Nadesz\\u0142a era ",
        "! Porzu\\u0107cie ",
        " i szukajcie pocieszenia w ",
        "!"
      ],
      "created_at":"2016-03-26T22:41:45+00:00",
      "nsfw":true
    },
    {
      "id":"a7f4b4b1-c3ba-458e-a8db-31bbd02109cc",
      "text":[
        "Marsz do ",
        "!"
      ],
      "created_at":"2016-03-26T23:44:24+00:00",
      "nsfw":true
    },
    {
      "id":"a99ccb58-91e9-4e4a-941b-0a2028d8536e",
      "text":[
        "Achilles mia\\u0142 dwa s\\u0142abe punkty: pi\\u0119t\\u0119 i ",
        "."
      ],
      "created_at":"2016-03-26T22:56:57+00:00",
      "nsfw":true
    },
    {
      "id":"a9c86737-ee70-4771-8c59-2cdb20581cb3",
      "text":[
        "Chcesz mi powiedzie\\u0107, \\u017ce ",
        " to m\\u00f3j brat?!"
      ],
      "created_at":"2016-03-26T22:44:44+00:00",
      "nsfw":true
    },
    {
      "id":"aaa1129c-6cdb-4367-bfd0-7a6414c0453c",
      "text":[
        "Donald ",
        ", Tw\\u00f3j rz\\u0105d obal\\u0105 ",
        "."
      ],
      "created_at":"2016-03-27T00:03:47+00:00",
      "nsfw":true
    },
    {
      "id":"ab37458c-0bfc-4a91-a4af-983e9b852009",
      "text":[
        "Panie Piotrze... mia\\u0142 Pan zaprojektowa\\u0107 ",
        ", a nie ",
        "!"
      ],
      "created_at":"2016-06-14T15:36:51+00:00",
      "nsfw":true
    },
    {
      "id":"ab7807b3-c244-4483-b3d7-7e2bc4383dc3",
      "text":[
        "\\u017beby k\\u00f3zka nie ",
        ", to by n\\u00f3\\u017cki nie ",
        "."
      ],
      "created_at":"2016-03-26T22:32:26+00:00",
      "nsfw":true
    },
    {
      "id":"ac1a6c80-e6d5-4489-b0d9-a5f152cb08a4",
      "text":[
        "",
        ".pl"
      ],
      "created_at":"2016-03-27T00:07:02+00:00",
      "nsfw":true
    },
    {
      "id":"ac1a906d-032b-415f-b1d6-e945d1ddb623",
      "text":[
        "A ja mam to w ",
        ", kurwa!"
      ],
      "created_at":"2016-03-27T00:11:56+00:00",
      "nsfw":true
    },
    {
      "id":"acbd78fa-43bb-4a9a-95b8-56bd53f236ec",
      "text":[
        "Ostatnie s\\u0142owa Papie\\u017ca to ",
        "."
      ],
      "created_at":"2016-03-26T22:58:55+00:00",
      "nsfw":true
    },
    {
      "id":"ad160dc4-d659-44f5-8ee2-a7ecae40ccb0",
      "text":[
        "Kochana! Nie uwierzysz! Ostatnio kupi\\u0142am tak\\u0105 pi\\u0119kn\\u0105 ",
        " w Arkadii!"
      ],
      "created_at":"2016-10-10T20:53:24+00:00",
      "nsfw":true
    },
    {
      "id":"ae9070fb-aca0-4e38-9dce-adcc35af77d7",
      "text":[
        "Pr\\u0119dzej trafisz na ",
        ", ni\\u017c Ci kosa wypadnie."
      ],
      "created_at":"2016-03-27T00:04:42+00:00",
      "nsfw":true
    },
    {
      "id":"aeb31c4c-c06a-4bf6-82b9-d18f1ab9091d",
      "text":[
        "Skazuj\\u0119 Pana na ",
        "! Na tak\\u0105 kar\\u0119 Pan zas\\u0142u\\u017cy\\u0142!"
      ],
      "created_at":"2016-06-14T15:30:59+00:00",
      "nsfw":true
    },
    {
      "id":"aee795d4-a1b5-4ee0-bfdf-1167e052863b",
      "text":[
        "Nie dotykaj tego psa! On ma ",
        "!"
      ],
      "created_at":"2016-10-10T21:23:07+00:00",
      "nsfw":true
    },
    {
      "id":"afd7ff91-49f8-4890-bc2b-b17ad22e6b57",
      "text":[
        "Czy to ten prastary ",
        "?!"
      ],
      "created_at":"2016-03-26T22:55:00+00:00",
      "nsfw":true
    },
    {
      "id":"b03a324c-90e3-44e8-9940-ebf6813e70dd",
      "text":[
        "Hehe, Wiktorku! Interesuj\\u0105 Ci\\u0119 ju\\u017c dziewczynki? Czy nadal tylko ",
        " CI w g\\u0142owie?"
      ],
      "created_at":"2016-10-10T21:57:13+00:00",
      "nsfw":true
    },
    {
      "id":"b0b67869-7b6b-4733-b90d-a05e948718c1",
      "text":[
        "Podnios\\u0142em sok, a na odwrocie kartonu by\\u0142o napisane ",
        "."
      ],
      "created_at":"2016-03-27T00:01:05+00:00",
      "nsfw":true
    },
    {
      "id":"b0e9c103-972a-4be3-a9fa-f35fec09708b",
      "text":[
        "Zamiast wazeliny wzi\\u0105\\u0142bym ",
        "."
      ],
      "created_at":"2016-03-27T00:02:50+00:00",
      "nsfw":true
    },
    {
      "id":"b35b92c2-3848-405d-a524-43595eddb410",
      "text":[
        "Uwierz mi, jestem ",
        "."
      ],
      "created_at":"2016-03-27T00:03:20+00:00",
      "nsfw":true
    },
    {
      "id":"b3c54a39-51df-4264-b726-81f214bc406a",
      "text":[
        "Pokona\\u0142 go za pomoc\\u0105 ",
        "."
      ],
      "created_at":"2016-03-26T23:51:36+00:00",
      "nsfw":true
    },
    {
      "id":"b77c6e4a-608b-4ce0-b704-bd02045e4b61",
      "text":[
        "No, wiesz. Ka\\u017cdy po co\\u015b \\u017cyje. Ja na przyk\\u0142ad \\u017cyj\\u0119, bo chcia\\u0142bym zrozumie\\u0107 ",
        "."
      ],
      "created_at":"2016-10-10T21:05:08+00:00",
      "nsfw":true
    },
    {
      "id":"b7d27a88-ae82-4de6-9763-7df54ce2d4f4",
      "text":[
        "Stoi na stacji lokomotywa. Ci\\u0119\\u017cka, ogromna i ",
        "."
      ],
      "created_at":"2016-03-26T22:44:25+00:00",
      "nsfw":true
    },
    {
      "id":"b961d33e-73a9-49cc-95a7-465988a872a4",
      "text":[
        "Wybiera si\\u0119 jak ",
        " za ",
        "."
      ],
      "created_at":"2016-03-28T15:40:49+00:00",
      "nsfw":true
    },
    {
      "id":"b98cab06-a1e3-4b4c-a850-949d5fec6e7e",
      "text":[
        "",
        " to pierwszy krok do ",
        "."
      ],
      "created_at":"2016-03-26T23:48:27+00:00",
      "nsfw":true
    },
    {
      "id":"b9b28ea0-388e-47cf-a7cd-012a6fc83b1e",
      "text":[
        "Jean - Claude Van ",
        "."
      ],
      "created_at":"2016-03-27T07:13:04+00:00",
      "nsfw":true
    },
    {
      "id":"ba20e5a7-0e0f-4c4b-9c65-4cf5e00bc8d0",
      "text":[
        "Jeste\\u015b pracowity jak ",
        "."
      ],
      "created_at":"2016-03-28T15:31:35+00:00",
      "nsfw":true
    },
    {
      "id":"bd779ccf-8a80-42cd-ad1d-e9c8230cfe3f",
      "text":[
        "",
        " chodz\\u0105 parami."
      ],
      "created_at":"2016-03-28T15:37:27+00:00",
      "nsfw":true
    },
    {
      "id":"beee46c7-d969-4c21-8e70-16c479da7f3a",
      "text":[
        "Komu w drog\\u0119, temu ",
        "."
      ],
      "created_at":"2016-03-28T15:34:50+00:00",
      "nsfw":true
    },
    {
      "id":"bf09eb87-6811-4581-ba3b-a845b0738423",
      "text":[
        "Kiedy by\\u0142em ma\\u0142y ",
        ", tata powiedzia\\u0142 mi",
        "."
      ],
      "created_at":"2016-03-26T22:23:47+00:00",
      "nsfw":true
    },
    {
      "id":"bfc19e8d-0b68-4034-a766-ab596e71589e",
      "text":[
        "Twoja stara jest jak ",
        "."
      ],
      "created_at":"2016-03-26T22:54:49+00:00",
      "nsfw":true
    },
    {
      "id":"bfd0cc91-c87c-4e40-893b-0c4456d2fc93",
      "text":[
        "Elfy wykuwa\\u0142y pi\\u0119kne ",
        "."
      ],
      "created_at":"2016-03-26T22:56:36+00:00",
      "nsfw":true
    },
    {
      "id":"c13ac4a0-f4d5-4fc9-8e09-e33c812dead2",
      "text":[
        "Arnold ",
        "."
      ],
      "created_at":"2016-03-27T07:12:33+00:00",
      "nsfw":true
    },
    {
      "id":"c3144849-a31d-47d1-8503-bdd6e60084e8",
      "text":[
        "Niech mnie ",
        " \\u015bwi\\u015bnie!"
      ],
      "created_at":"2016-03-26T22:53:34+00:00",
      "nsfw":true
    },
    {
      "id":"c546c607-cf30-416a-844c-5a3d3fb818db",
      "text":[
        "Pierwsz\\u0105 rzecz\\u0105, kt\\u00f3r\\u0105 chcia\\u0142by\\u015b zobaczy\\u0107 po urodzeniu jest ",
        "."
      ],
      "created_at":"2016-03-27T00:01:33+00:00",
      "nsfw":true
    },
    {
      "id":"cb6eace7-2de8-403c-aaec-e2764d703a24",
      "text":[
        "Raz zap\\u0142aci\\u0142em za ",
        "."
      ],
      "created_at":"2016-03-27T15:08:11+00:00",
      "nsfw":true
    },
    {
      "id":"cc89b96d-05ed-4646-9fb8-cc3d4269762e",
      "text":[
        "Dzisiaj narysuj\\u0105 Pa\\u0144stwo ",
        ". Powodzenia."
      ],
      "created_at":"2016-06-14T15:36:15+00:00",
      "nsfw":true
    },
    {
      "id":"cd65a0f6-4bb9-4e8c-85e6-52bbed8bf957",
      "text":[
        "Nie kupi\\u0119 mi\\u0142o\\u015bci za pieni\\u0105dze, ale mog\\u0119 za nie kupi\\u0107 ",
        "."
      ],
      "created_at":"2016-03-26T22:36:38+00:00",
      "nsfw":true
    },
    {
      "id":"d04ae590-448d-48c4-972b-197239871713",
      "text":[
        "Kochanie. Co powiesz na ma\\u0142y ",
        "?"
      ],
      "created_at":"2016-03-26T23:50:25+00:00",
      "nsfw":true
    },
    {
      "id":"d09c6eb0-94a8-411d-b01b-931a86b4f11f",
      "text":[
        "Z dupy do ",
        "."
      ],
      "created_at":"2016-03-26T22:29:14+00:00",
      "nsfw":true
    },
    {
      "id":"d4178988-9408-4c54-804c-76c008d3860c",
      "text":[
        "Konfucjusz m\\u00f3wi: \\\"Je\\u017celi ",
        " jest Twoim problemem zawsze mo\\u017cesz u\\u017cy\\u0107 ",
        ".\\\""
      ],
      "created_at":"2016-03-26T23:51:00+00:00",
      "nsfw":true
    },
    {
      "id":"d419682d-ff3d-493c-953b-4a78ee91382b",
      "text":[
        "Starzy ludzie pachn\\u0105 jak ",
        "."
      ],
      "created_at":"2016-03-26T22:45:01+00:00",
      "nsfw":true
    },
    {
      "id":"d4b67a0c-f93a-4115-bba6-d80463decf9e",
      "text":[
        "",
        " + ",
        " = ",
        ""
      ],
      "created_at":"2016-03-26T23:46:52+00:00",
      "nsfw":true
    },
    {
      "id":"d50f3b35-b186-40e3-8239-7387a73dc386",
      "text":[
        "Czu\\u0107 si\\u0119 jak ryba w ",
        "."
      ],
      "created_at":"2016-03-28T15:32:26+00:00",
      "nsfw":true
    },
    {
      "id":"d6b492bc-036d-41ef-b8fd-20c5d569130a",
      "text":[
        "W marcu jak w ",
        "."
      ],
      "created_at":"2016-03-28T15:40:10+00:00",
      "nsfw":true
    },
    {
      "id":"d9b8e4bf-775c-4d39-aa76-0d86c986b16e",
      "text":[
        "Jezusie! Ile pracy! Ju\\u017c nie wiem w co w\\u0142o\\u017cy\\u0107 ",
        "!"
      ],
      "created_at":"2016-10-10T21:00:03+00:00",
      "nsfw":true
    },
    {
      "id":"dd167c83-d66d-44bf-baf6-a95fb8925f72",
      "text":[
        "Wiedzia\\u0142em, \\u017ce masz ",
        ", ale \\u017ceby ",
        "?!"
      ],
      "created_at":"2016-03-27T00:15:48+00:00",
      "nsfw":true
    },
    {
      "id":"ddea4627-b7a3-4a33-a1fa-017cf161afc1",
      "text":[
        "Jakie jest has\\u0142o do WiFi? ",
        "."
      ],
      "created_at":"2016-03-27T00:05:18+00:00",
      "nsfw":true
    },
    {
      "id":"df828e23-c1f2-478d-97b5-a96869168762",
      "text":[
        "M\\u00f3j ukochany klub to FC ",
        ". Mam nadziej\\u0119, \\u017ce wygraj\\u0105 wszystko w tym sezonie!"
      ],
      "created_at":"2017-08-12T21:38:10+00:00",
      "nsfw":true
    },
    {
      "id":"dfc8eae0-3114-4c96-b28b-902150d7c838",
      "text":[
        "Jajko m\\u0105drzejsze od ",
        "."
      ],
      "created_at":"2016-03-26T22:28:27+00:00",
      "nsfw":true
    },
    {
      "id":"e0dba7dd-c39a-4950-a9aa-0dd37738fdca",
      "text":[
        "",
        " z Na Wsp\\u00f3lnej."
      ],
      "created_at":"2016-03-26T22:39:49+00:00",
      "nsfw":true
    },
    {
      "id":"e7bc9172-79af-4042-9c28-36eaabfa2f21",
      "text":[
        "Dupa boli, co?! M\\u00f3wi\\u0142em, \\u017ceby\\u015b u\\u017cy\\u0142 ",
        "!"
      ],
      "created_at":"2016-10-10T20:56:06+00:00",
      "nsfw":true
    },
    {
      "id":"ed972e92-297e-4a35-837d-3074aef75730",
      "text":[
        "Gdy ",
        " nie ma, ",
        " harcuj\\u0105."
      ],
      "created_at":"2016-03-28T15:33:08+00:00",
      "nsfw":true
    },
    {
      "id":"edbcc1d4-5331-4aae-b13f-d28daac6d81a",
      "text":[
        "Lepszy ",
        " w gar\\u015bci ni\\u017c ",
        " na dachu."
      ],
      "created_at":"2016-06-03T19:59:44+00:00",
      "nsfw":true
    },
    {
      "id":"eee07e56-61cf-4c57-abb9-5a42d79934fe",
      "text":[
        "Co z Ciebie za dziewucha?! Dziewuchy maj\\u0105 ",
        "!"
      ],
      "created_at":"2016-03-26T22:46:11+00:00",
      "nsfw":true
    },
    {
      "id":"ef044205-10bb-46be-bebd-d780428b5547",
      "text":[
        "Definicj\\u0105 dobrego zwi\\u0105zku zawsze by\\u0142o ",
        "."
      ],
      "created_at":"2016-03-26T22:56:07+00:00",
      "nsfw":true
    },
    {
      "id":"f073f978-6e8b-4a5c-9b44-034d8b1ba9d6",
      "text":[
        "Na dzisiejszych zaj\\u0119ciach b\\u0119dziemy omawia\\u0107 pewn\\u0105 mityczn\\u0105 posta\\u0107. B\\u0119dzie to ",
        "!"
      ],
      "created_at":"2016-06-14T15:39:10+00:00",
      "nsfw":true
    },
    {
      "id":"f0ff8678-e278-4122-924c-857c9442fdb8",
      "text":[
        "A co ma ",
        " do ",
        "?!"
      ],
      "created_at":"2016-06-14T15:27:27+00:00",
      "nsfw":true
    },
    {
      "id":"f45399a7-347f-4441-80c3-0e72a89879e4",
      "text":[
        "Matka wesz\\u0142a bez pukania do mojego pokoju i zobaczy\\u0142a ",
        " na \\u015bcianie... Mam przejebane."
      ],
      "created_at":"2017-10-06T15:04:52+00:00",
      "nsfw":true
    },
    {
      "id":"f63f81ab-ef04-49a5-b117-e99a6d9b7d83",
      "text":[
        "",
        " w necie, ",
        " w \\u015bwiecie."
      ],
      "created_at":"2016-05-16T17:34:47+00:00",
      "nsfw":true
    },
    {
      "id":"f63fb3d7-85f1-4ff1-823c-5041e26e35b4",
      "text":[
        "Gdzie kucharek sze\\u015b\\u0107, tam nie ma ",
        "."
      ],
      "created_at":"2016-03-26T22:28:16+00:00",
      "nsfw":true
    },
    {
      "id":"f78d58de-5525-4402-b215-8420ceaa53cb",
      "text":[
        "Masakra... matka ostatnio znalaz\\u0142a ",
        " w moim pokoju. Mam przejebane."
      ],
      "created_at":"2016-10-10T20:58:03+00:00",
      "nsfw":true
    },
    {
      "id":"f93bd908-dc2f-4b46-b886-e345e1081aaa",
      "text":[
        "Na g\\u00f3rze wacki, na dole wacki. Kto kocha wacki? ",
        "."
      ],
      "created_at":"2016-03-26T23:51:48+00:00",
      "nsfw":true
    },
    {
      "id":"f94a57df-f9ab-4545-b78f-3334533b81ed",
      "text":[
        "G\\u0142upi ma zawsze ",
        "."
      ],
      "created_at":"2016-06-14T15:27:42+00:00",
      "nsfw":true
    },
    {
      "id":"faed849c-20da-4a74-919c-872e09d68763",
      "text":[
        "Albo rybki, albo ",
        "."
      ],
      "created_at":"2016-03-26T22:33:18+00:00",
      "nsfw":true
    },
    {
      "id":"fc27df32-7e71-4e0b-ba08-f789004cbd23",
      "text":[
        "Kanapka z ",
        " i  ",
        "."
      ],
      "created_at":"2016-03-26T23:44:39+00:00",
      "nsfw":true
    },
    {
      "id":"fd1af947-f818-4247-9f6a-29010fcec379",
      "text":[
        "Mam wiele imion, ale mo\\u017cesz do mnie m\\u00f3wi\\u0107 ",
        "."
      ],
      "created_at":"2016-06-14T15:32:46+00:00",
      "nsfw":true
    },
    {
      "id":"fd2156cb-7d7a-4688-8b81-6b0e469ec9d4",
      "text":[
        "Twoje danie smakuje jak ",
        "."
      ],
      "created_at":"2016-03-26T22:48:03+00:00",
      "nsfw":true
    },
    {
      "id":"fea60e19-f74f-41a0-a6a7-e60c6c08d64d",
      "text":[
        "\\u015alimak, \\u015blimak, wystaw rogi, dam Ci ",
        " na pierogi."
      ],
      "created_at":"2016-03-27T00:19:12+00:00",
      "nsfw":true
    },
    {
      "id":"3cb6be26-8c47-4de6-8544-5b02e51044c3",
      "text":[
        "Jezus ",
        "."
      ],
      "created_at":"2016-03-27T00:04:50+00:00",
      "nsfw":true
    },
    {
      "id":"770d9c28-43a2-4c3a-8824-38b877c1df91",
      "text":[
        "Obr\\u00f3\\u0107 si\\u0119 troch\\u0119 w prawo. Teraz w lewo... Tw\\u00f3j penis wygl\\u0105da jak ",
        "."
      ],
      "created_at":"2016-10-10T21:19:34+00:00",
      "nsfw":true
    },
    {
      "id":"f689003c-90e3-40d2-9d35-b8f23fc2dc5a",
      "text":[
        "Nawet Hitler mia\\u0142 sw\\u00f3j w\\u0142asny ",
        "! Ty te\\u017c musisz go mie\\u0107!"
      ],
      "created_at":"2016-10-10T21:29:44+00:00",
      "nsfw":true
    }
  ],
  "responses":[
    {
      "id":"00321a01-8f1b-4cef-996a-196fbb698d98",
      "text":[
        "Cyga\\u0144skie nagrobki."
      ],
      "created_at":"2016-03-26T23:00:52+00:00",
      "nsfw":true
    },
    {
      "id":"00a524cc-8129-464d-bc0e-936d064293c8",
      "text":[
        "Nowy biust."
      ],
      "created_at":"2016-03-26T23:49:32+00:00",
      "nsfw":true
    },
    {
      "id":"0146d6c3-a3ca-4a5d-9316-8e56219cb90a",
      "text":[
        "Deklinacja."
      ],
      "created_at":"2016-03-28T15:30:04+00:00",
      "nsfw":true
    },
    {
      "id":"0231c581-2398-4408-9abb-e9e7111eeab4",
      "text":[
        "P\\u0119dzle w d\\u0142oniach."
      ],
      "created_at":"2016-03-27T00:18:47+00:00",
      "nsfw":true
    },
    {
      "id":"0242fbad-ab7b-482d-a3ae-1a8e0977e2d4",
      "text":[
        "Przek\\u0142adnia z\\u0119bata."
      ],
      "created_at":"2016-03-26T22:31:10+00:00",
      "nsfw":true
    },
    {
      "id":"03e7b2e4-6bf6-4d88-bca1-52d33197f58b",
      "text":[
        "Anakonda."
      ],
      "created_at":"2016-03-27T00:05:42+00:00",
      "nsfw":true
    },
    {
      "id":"049e8735-ece7-4302-9d18-bfce9e3e8e72",
      "text":[
        "Sympatyczny ziemniaczek."
      ],
      "created_at":"2016-03-27T00:13:27+00:00",
      "nsfw":true
    },
    {
      "id":"06283cf0-6593-4285-88db-d3da0c85cbe5",
      "text":[
        "Wiele, wiele aborcji."
      ],
      "created_at":"2016-03-27T15:06:56+00:00",
      "nsfw":true
    },
    {
      "id":"06bec7d9-29d9-491f-93ef-c2c88f5b90d0",
      "text":[
        "Kozojebca."
      ],
      "created_at":"2016-03-26T22:43:26+00:00",
      "nsfw":true
    },
    {
      "id":"06f4aee8-66e6-4c43-be7c-040ed08be1dc",
      "text":[
        "Krzywka mimo\\u015brodowa z popychaczem talerzykowym."
      ],
      "created_at":"2016-03-26T23:50:40+00:00",
      "nsfw":true
    },
    {
      "id":"090e6754-29e2-47e6-858b-86eac9f96c96",
      "text":[
        "Burdel na rogu."
      ],
      "created_at":"2016-05-16T17:19:44+00:00",
      "nsfw":true
    },
    {
      "id":"09e3fb54-11e4-4e37-b90c-77682f80cf0b",
      "text":[
        "Szmato!"
      ],
      "created_at":"2016-03-27T00:11:23+00:00",
      "nsfw":true
    },
    {
      "id":"0a500c99-0e2b-48ca-b9ce-2b0e7640139d",
      "text":[
        "Skurwik\\u0142ak."
      ],
      "created_at":"2016-10-10T21:52:51+00:00",
      "nsfw":true
    },
    {
      "id":"0aba069e-4211-40e4-8641-6b0a0d8fdbc6",
      "text":[
        "Ropiej\\u0105ca \\u0142echtaczka."
      ],
      "created_at":"2016-05-16T17:38:18+00:00",
      "nsfw":true
    },
    {
      "id":"0c449dd8-feaa-4d41-9ebd-beae3e9535b5",
      "text":[
        "Wysoki skrzypek."
      ],
      "created_at":"2016-03-27T07:14:40+00:00",
      "nsfw":true
    },
    {
      "id":"0d676fcd-4508-4b8e-b458-1c1c148c3144",
      "text":[
        "Klej."
      ],
      "created_at":"2016-03-26T22:19:51+00:00",
      "nsfw":true
    },
    {
      "id":"0dc62cad-110e-4b43-80b3-fe981f432c3d",
      "text":[
        "Fikasz, znikasz!"
      ],
      "created_at":"2016-03-26T22:26:23+00:00",
      "nsfw":true
    },
    {
      "id":"103b0324-ccce-42f7-91ac-8c585ebd1cc5",
      "text":[
        "Siusiek W\\u0105chacz."
      ],
      "created_at":"2016-10-10T21:56:14+00:00",
      "nsfw":true
    },
    {
      "id":"10b54af1-4af2-45ac-97c5-5c24b0bcb19b",
      "text":[
        "Emilka i jej demonta\\u017c."
      ],
      "created_at":"2016-10-10T22:07:08+00:00",
      "nsfw":true
    },
    {
      "id":"10f65cca-edf7-4770-82a3-b828d2456cbe",
      "text":[
        "Dno dupy."
      ],
      "created_at":"2016-06-14T15:25:30+00:00",
      "nsfw":true
    },
    {
      "id":"11572e85-0c61-4bbc-a10a-cef13d2ae0fc",
      "text":[
        "\\u017bupan pop\\u0142ochu."
      ],
      "created_at":"2016-03-27T00:10:25+00:00",
      "nsfw":true
    },
    {
      "id":"13e059bd-96d3-425a-85e4-63795e98e84f",
      "text":[
        "Definicja rozkoszy."
      ],
      "created_at":"2016-05-16T17:18:28+00:00",
      "nsfw":true
    },
    {
      "id":"14f9c1fb-109d-47a8-884f-041bf8501c39",
      "text":[
        "Kopanie do\\u0142\\u00f3w."
      ],
      "created_at":"2016-03-27T00:09:38+00:00",
      "nsfw":true
    },
    {
      "id":"151ffd1b-a939-499c-a9a7-45a34b5f51ed",
      "text":[
        "Aaaaaa."
      ],
      "created_at":"2016-03-27T00:04:16+00:00",
      "nsfw":true
    },
    {
      "id":"15d335e6-015d-4005-841f-191094a999ae",
      "text":[
        "Przerwa na arbuza."
      ],
      "created_at":"2016-10-10T21:21:22+00:00",
      "nsfw":true
    },
    {
      "id":"16accada-8029-41b7-8286-5759f828d7a2",
      "text":[
        "\\u017beby zdech\\u0142."
      ],
      "created_at":"2016-03-26T22:57:12+00:00",
      "nsfw":true
    },
    {
      "id":"16b21c4b-fdae-4316-bce6-13c36e74ae2e",
      "text":[
        "Potop."
      ],
      "created_at":"2016-03-27T00:11:20+00:00",
      "nsfw":true
    },
    {
      "id":"16d3e751-adaf-4cf4-ad49-d031d464c72d",
      "text":[
        "Krew z odbytu."
      ],
      "created_at":"2016-06-14T15:05:48+00:00",
      "nsfw":true
    },
    {
      "id":"173e265c-d2be-49f6-9c7f-dc95c031317c",
      "text":[
        "Delta < 0"
      ],
      "created_at":"2016-03-26T22:45:30+00:00",
      "nsfw":true
    },
    {
      "id":"17502c74-d027-48f7-a437-61963062f4c8",
      "text":[
        "Margines dla polonistki."
      ],
      "created_at":"2016-03-27T00:10:53+00:00",
      "nsfw":true
    },
    {
      "id":"17bc4f91-47df-48a8-8718-5e520e88b125",
      "text":[
        "\\u017belazna R\\u0119ka Frank\\u00f3w."
      ],
      "created_at":"2016-04-09T08:39:56+00:00",
      "nsfw":true
    },
    {
      "id":"17f1e8df-771e-4cb7-8c3f-7cb3fc0cf46a",
      "text":[
        "Brak j\\u0105der."
      ],
      "created_at":"2016-03-26T22:29:29+00:00",
      "nsfw":true
    },
    {
      "id":"180cba41-1b3b-4510-8995-6ffd2f0d593f",
      "text":[
        "Konstantynopol."
      ],
      "created_at":"2016-03-26T23:57:01+00:00",
      "nsfw":true
    },
    {
      "id":"18a0575f-32bc-4c26-9df5-e294fcb8a222",
      "text":[
        "Karczmienna b\\u00f3jka."
      ],
      "created_at":"2016-05-16T17:32:11+00:00",
      "nsfw":true
    },
    {
      "id":"18f70da9-2239-458a-8d00-0db767bdfeb7",
      "text":[
        "Nie tak szybko!"
      ],
      "created_at":"2016-03-26T22:53:17+00:00",
      "nsfw":true
    },
    {
      "id":"191ddabc-21dd-48bc-9a07-2266aac863ec",
      "text":[
        "Smoczy kutas."
      ],
      "created_at":"2016-03-27T00:10:29+00:00",
      "nsfw":true
    },
    {
      "id":"1a3f35f3-7d9b-454b-ab04-92bf2d5caaf4",
      "text":[
        "Odmiana przed przypadki."
      ],
      "created_at":"2016-04-07T16:48:24+00:00",
      "nsfw":true
    },
    {
      "id":"1b04a808-4633-4814-ae69-1cb1db9843e9",
      "text":[
        "Elektrony walencyjne."
      ],
      "created_at":"2016-03-27T07:20:58+00:00",
      "nsfw":true
    },
    {
      "id":"1b0c0da9-491b-4120-9b54-4a51eb8a2854",
      "text":[
        "Przemytnik g\\u00f3wna."
      ],
      "created_at":"2016-03-26T23:57:43+00:00",
      "nsfw":true
    },
    {
      "id":"1b15c6a9-4943-402f-a0d3-a57f56b70622",
      "text":[
        "Mieszanka wedlowska."
      ],
      "created_at":"2016-03-27T00:10:01+00:00",
      "nsfw":true
    },
    {
      "id":"1b3c4482-28e3-4a3c-9c7d-f6e6f335bf75",
      "text":[
        "G\\u00f3wniany delfin."
      ],
      "created_at":"2016-03-26T23:01:52+00:00",
      "nsfw":true
    },
    {
      "id":"1eb3bcd5-aa00-44be-888e-9d7c1cc77390",
      "text":[
        "Segment miejski."
      ],
      "created_at":"2016-10-10T21:13:33+00:00",
      "nsfw":true
    },
    {
      "id":"1ec291ce-2f01-480f-973a-3230e6ccce20",
      "text":[
        "Ca\\u0142ka Wereszczagina."
      ],
      "created_at":"2016-04-12T12:57:36+00:00",
      "nsfw":true
    },
    {
      "id":"1f8ee44e-84f8-464c-b306-e19c73c3bef6",
      "text":[
        "Atak!"
      ],
      "created_at":"2016-05-16T17:39:17+00:00",
      "nsfw":true
    },
    {
      "id":"215ca9b9-7056-4016-8754-5d930bbf86b8",
      "text":[
        "Pla\\u017cowanie."
      ],
      "created_at":"2016-03-26T22:22:36+00:00",
      "nsfw":true
    },
    {
      "id":"217b8363-3440-427b-b3c0-a042e045768a",
      "text":[
        "Faraon."
      ],
      "created_at":"2016-03-28T15:28:23+00:00",
      "nsfw":true
    },
    {
      "id":"222c8df2-56ab-4914-9c32-98e4a8d2ac39",
      "text":[
        "Moc wskrzeszania zmar\\u0142ych."
      ],
      "created_at":"2016-04-12T12:59:34+00:00",
      "nsfw":true
    },
    {
      "id":"2235a3d0-0fa2-48ca-9f13-a6934d2ac457",
      "text":[
        "Odcinek l\\u0119d\\u017awiowy."
      ],
      "created_at":"2016-03-26T22:30:42+00:00",
      "nsfw":true
    },
    {
      "id":"22ea382d-fb65-4ad4-9b4e-473db16032c4",
      "text":[
        "Ma\\u0142y kolega."
      ],
      "created_at":"2016-05-16T17:30:31+00:00",
      "nsfw":true
    },
    {
      "id":"2306766b-be5d-415c-aebe-134a900307a4",
      "text":[
        "Pla\\u017ca nudyst\\u00f3w."
      ],
      "created_at":"2016-04-12T12:59:16+00:00",
      "nsfw":true
    },
    {
      "id":"233b88d8-4780-47d1-8d73-b2f2b7479fdf",
      "text":[
        "Myszka Razera."
      ],
      "created_at":"2016-03-26T23:58:40+00:00",
      "nsfw":true
    },
    {
      "id":"23f5e2cd-27e5-4f4e-87ce-8acf22432eb3",
      "text":[
        "Klej gej."
      ],
      "created_at":"2016-03-28T15:30:20+00:00",
      "nsfw":true
    },
    {
      "id":"24d58ccd-0162-45b9-9025-690cc1b41280",
      "text":[
        "Jamajscy faszy\\u015bci."
      ],
      "created_at":"2016-03-26T23:02:05+00:00",
      "nsfw":true
    },
    {
      "id":"258f2efd-ea25-4ea0-9ddc-f52e57c827f3",
      "text":[
        "Karmienie go\\u0142\\u0119bi."
      ],
      "created_at":"2016-03-27T00:08:25+00:00",
      "nsfw":true
    },
    {
      "id":"28b1e4ef-533a-4f6d-9c7a-ff8c9c3381d2",
      "text":[
        "Pan Tadeusz."
      ],
      "created_at":"2016-03-26T23:59:44+00:00",
      "nsfw":true
    },
    {
      "id":"2999d44f-0575-4801-9153-6a1ff9dce481",
      "text":[
        "Wiele odniesie\\u0144."
      ],
      "created_at":"2016-03-26T22:32:55+00:00",
      "nsfw":true
    },
    {
      "id":"2ab13d51-7ebf-418c-93ee-364a99b04baf",
      "text":[
        "Szatan."
      ],
      "created_at":"2016-03-26T22:35:15+00:00",
      "nsfw":true
    },
    {
      "id":"2b6241ce-55db-45d7-85ad-23a6da72eada",
      "text":[
        "Radioaktywny \\u017cuk."
      ],
      "created_at":"2016-03-26T23:44:50+00:00",
      "nsfw":true
    },
    {
      "id":"2bebea38-2b0e-4866-839f-62877f677579",
      "text":[
        "Napletek w cie\\u015bcie."
      ],
      "created_at":"2016-03-27T07:32:47+00:00",
      "nsfw":true
    },
    {
      "id":"2c192152-a05f-4376-85c1-7fbab4c68e13",
      "text":[
        "Odbytnica."
      ],
      "created_at":"2016-03-26T22:21:59+00:00",
      "nsfw":true
    },
    {
      "id":"2e47dd54-e7d7-4a70-ad99-739ea21d6397",
      "text":[
        "Pr\\u0119dko\\u015b\\u0107 obrotowa."
      ],
      "created_at":"2016-03-26T23:53:31+00:00",
      "nsfw":true
    },
    {
      "id":"2f33687d-bb22-4d3d-82df-80240d67386f",
      "text":[
        "Marsza\\u0142ek J\\u00f3zef Pi\\u0142sudski."
      ],
      "created_at":"2016-03-28T15:30:12+00:00",
      "nsfw":true
    },
    {
      "id":"2fa4afd5-3073-4567-839a-2abaacbc8d20",
      "text":[
        "Ptasi m\\u00f3\\u017cd\\u017cek."
      ],
      "created_at":"2016-04-07T16:48:43+00:00",
      "nsfw":true
    },
    {
      "id":"3025bbda-eb6d-487d-9f43-fc51ce542969",
      "text":[
        "Karakan."
      ],
      "created_at":"2016-03-27T00:11:48+00:00",
      "nsfw":true
    },
    {
      "id":"305e9a0e-d39e-4956-a1e1-9621041b1515",
      "text":[
        "Dom jednorodzinny."
      ],
      "created_at":"2016-10-10T21:13:27+00:00",
      "nsfw":true
    },
    {
      "id":"314935fe-c107-4394-ab98-9cef9267176b",
      "text":[
        "Topola."
      ],
      "created_at":"2016-05-16T17:22:25+00:00",
      "nsfw":true
    },
    {
      "id":"3203517d-5695-4e4e-83c0-f41ab66793ff",
      "text":[
        "Matko jedyna!"
      ],
      "created_at":"2016-10-10T20:54:12+00:00",
      "nsfw":true
    },
    {
      "id":"32a86349-3bf9-4e05-a527-49945defa739",
      "text":[
        "Sierociniec dla ps\\u00f3w."
      ],
      "created_at":"2016-06-14T15:25:49+00:00",
      "nsfw":true
    },
    {
      "id":"33af6505-b9d5-4c62-829b-8312ea6431c0",
      "text":[
        "Tak."
      ],
      "created_at":"2016-03-26T23:43:21+00:00",
      "nsfw":true
    },
    {
      "id":"3445dec8-549c-45ed-9d21-37844819985d",
      "text":[
        "Naukowy be\\u0142kot."
      ],
      "created_at":"2016-03-27T07:24:51+00:00",
      "nsfw":true
    },
    {
      "id":"34beb134-1142-4a78-82d8-8ce630443cca",
      "text":[
        "Szkicowanie cyck\\u00f3w."
      ],
      "created_at":"2016-03-27T00:08:54+00:00",
      "nsfw":true
    },
    {
      "id":"352e1705-2b98-4cea-a192-1605938e4d05",
      "text":[
        "Przyrodzenie twarde jak ksi\\u0119\\u017cycowa ska\\u0142a."
      ],
      "created_at":"2016-03-27T00:15:07+00:00",
      "nsfw":true
    },
    {
      "id":"357a9104-0b5b-4614-9f86-14aabafd49c2",
      "text":[
        "Atak na Francj\\u0119."
      ],
      "created_at":"2016-05-16T17:39:12+00:00",
      "nsfw":true
    },
    {
      "id":"35bbca27-eec0-49e1-a044-e6fe69f0210c",
      "text":[
        "Dzie\\u0144, w kt\\u00f3rym ptaki zaatakowa\\u0142y."
      ],
      "created_at":"2016-03-26T22:30:07+00:00",
      "nsfw":true
    },
    {
      "id":"35cbeff3-3f31-44bf-ba26-1ec211809045",
      "text":[
        "Murzyni na smyczy."
      ],
      "created_at":"2016-04-07T16:52:44+00:00",
      "nsfw":true
    },
    {
      "id":"35d74c54-61d5-41d4-952b-86be92702e3c",
      "text":[
        "Piesza wycieczka w g\\u00f3ry."
      ],
      "created_at":"2016-05-16T17:37:00+00:00",
      "nsfw":true
    },
    {
      "id":"36301779-f78d-416d-876a-b3aa1242a9ad",
      "text":[
        "Klaun na wrotkach."
      ],
      "created_at":"2016-04-07T16:48:48+00:00",
      "nsfw":true
    },
    {
      "id":"37c8d760-41af-415e-9f78-ba55c16ae5af",
      "text":[
        "O\\u0142\\u00f3wek koh-i-noor."
      ],
      "created_at":"2016-05-16T17:35:25+00:00",
      "nsfw":true
    },
    {
      "id":"3867e3ce-6fbf-402b-9a6e-48aa0f7a9147",
      "text":[
        "Zaka\\u0142apu\\u0107ka\\u0107 si\\u0119."
      ],
      "created_at":"2016-03-26T22:49:07+00:00",
      "nsfw":true
    },
    {
      "id":"3b5d60c1-33ca-49ac-a1e5-56dbd8a71aac",
      "text":[
        "Konrad."
      ],
      "created_at":"2016-03-26T22:19:01+00:00",
      "nsfw":true
    },
    {
      "id":"3b865682-b493-41a0-92a7-04dff82669db",
      "text":[
        "Chrzest ognia."
      ],
      "created_at":"2016-04-07T16:49:59+00:00",
      "nsfw":true
    },
    {
      "id":"3b98fdfc-4afc-41ce-be09-bfefa844e7a0",
      "text":[
        "Magiczny pocisk."
      ],
      "created_at":"2016-03-26T22:38:38+00:00",
      "nsfw":true
    },
    {
      "id":"3c09c78d-d234-4db2-b8ef-9ddb5e89a22f",
      "text":[
        "Dwie lewe r\\u0105czki."
      ],
      "created_at":"2016-03-26T22:59:52+00:00",
      "nsfw":true
    },
    {
      "id":"3d7adc86-40de-44db-8eaf-ab5b34cdff49",
      "text":[
        "Metaforyczny Byk."
      ],
      "created_at":"2016-03-27T07:29:48+00:00",
      "nsfw":true
    },
    {
      "id":"3dc91169-5942-4d68-b64a-8c6db54b6531",
      "text":[
        "Mostek tensometryczny."
      ],
      "created_at":"2016-04-07T16:54:16+00:00",
      "nsfw":true
    },
    {
      "id":"3e35a7ce-f4bc-48a9-bdbf-5cc9bdbdcbd7",
      "text":[
        "Akcja na dzielni."
      ],
      "created_at":"2016-03-27T00:16:04+00:00",
      "nsfw":true
    },
    {
      "id":"3e791285-25cc-4387-84f8-dd7325c326f3",
      "text":[
        "Gagatek."
      ],
      "created_at":"2016-03-26T22:48:55+00:00",
      "nsfw":true
    },
    {
      "id":"40017d6b-b3e6-42a1-9a39-d5f624d70abf",
      "text":[
        "Komnata tajemnic."
      ],
      "created_at":"2016-06-23T17:24:04+00:00",
      "nsfw":true
    },
    {
      "id":"40092260-34b4-4b03-b6dd-b2f4de8e320a",
      "text":[
        "Blisko\\u015b\\u0107 z nieznajom\\u0105."
      ],
      "created_at":"2016-04-12T12:59:09+00:00",
      "nsfw":true
    },
    {
      "id":"40c8e91e-493a-4d2d-9c6a-40702b5f84d5",
      "text":[
        "Mantikora."
      ],
      "created_at":"2016-03-26T23:45:19+00:00",
      "nsfw":true
    },
    {
      "id":"410abd86-537b-448d-8a85-2fc6d8814f6a",
      "text":[
        "Malowanie p\\u0142otu."
      ],
      "created_at":"2016-03-26T22:57:53+00:00",
      "nsfw":true
    },
    {
      "id":"414dabc5-d55b-4e13-8d2c-3e21bf1caec5",
      "text":[
        "Nicnierobienie."
      ],
      "created_at":"2016-05-16T17:31:08+00:00",
      "nsfw":true
    },
    {
      "id":"4183c204-2cee-41b4-a908-28f9da3cb190",
      "text":[
        "Kasa na dziwki."
      ],
      "created_at":"2016-04-07T16:49:21+00:00",
      "nsfw":true
    },
    {
      "id":"4290baf0-2c08-4d31-8ef3-bdc7c769390e",
      "text":[
        "A daj\\u017ce spok\\u00f3j."
      ],
      "created_at":"2016-03-26T22:35:45+00:00",
      "nsfw":true
    },
    {
      "id":"42ba4b0d-9ed4-4ebe-ad4e-9606695d4d32",
      "text":[
        "Babiarz Artur."
      ],
      "created_at":"2016-03-26T23:59:37+00:00",
      "nsfw":true
    },
    {
      "id":"43288e8a-f6ed-4e2e-996b-ef2b21a77e8f",
      "text":[
        "Czarny Pi\\u0105tek."
      ],
      "created_at":"2016-03-27T07:17:42+00:00",
      "nsfw":true
    },
    {
      "id":"4334409a-78ca-4f0d-97c5-dcfc8b247002",
      "text":[
        "Bimber z mlecza."
      ],
      "created_at":"2016-10-10T21:50:26+00:00",
      "nsfw":true
    },
    {
      "id":"433ce507-4063-479c-9015-a41ac4824422",
      "text":[
        "Kompletny zawodnik."
      ],
      "created_at":"2016-03-27T00:03:13+00:00",
      "nsfw":true
    },
    {
      "id":"44488071-7d45-4bda-b99c-698eb079245e",
      "text":[
        "Ukrzy\\u017cowanie Chrystusa."
      ],
      "created_at":"2016-03-27T00:01:40+00:00",
      "nsfw":true
    },
    {
      "id":"449bab8c-fe3b-4316-9dab-0a66a1c98406",
      "text":[
        "Optimus Prime."
      ],
      "created_at":"2016-03-27T00:14:49+00:00",
      "nsfw":true
    },
    {
      "id":"44d254dc-9c61-4f6e-bf4e-a40845713118",
      "text":[
        "Mistyczne ukulele."
      ],
      "created_at":"2016-06-14T15:23:10+00:00",
      "nsfw":true
    },
    {
      "id":"4583869c-0fdc-4b8f-9602-faefd28877e7",
      "text":[
        "Bank PKO."
      ],
      "created_at":"2016-06-14T15:03:39+00:00",
      "nsfw":true
    },
    {
      "id":"45a799f1-018b-4022-9def-ee72c6028242",
      "text":[
        "Royal Baby."
      ],
      "created_at":"2016-05-16T17:29:41+00:00",
      "nsfw":true
    },
    {
      "id":"45c39dca-72ad-4294-97b5-7362545080ea",
      "text":[
        "Wolny elektron."
      ],
      "created_at":"2016-03-27T07:20:48+00:00",
      "nsfw":true
    },
    {
      "id":"47297178-fb03-453e-b506-a0bb1876264e",
      "text":[
        "Sranie ig\\u0142ami."
      ],
      "created_at":"2016-03-28T15:29:04+00:00",
      "nsfw":true
    },
    {
      "id":"47347b7e-2847-4ae8-809b-d50708918cd2",
      "text":[
        "Serek topiony."
      ],
      "created_at":"2016-03-26T23:01:37+00:00",
      "nsfw":true
    },
    {
      "id":"47fc9477-9142-4161-a0cf-1db97591fc44",
      "text":[
        "Po prostu banan."
      ],
      "created_at":"2016-03-26T22:37:39+00:00",
      "nsfw":true
    },
    {
      "id":"49d99366-51fa-44ca-88c8-3170af3a595d",
      "text":[
        "Kategoryczynie nie!"
      ],
      "created_at":"2016-03-27T00:03:00+00:00",
      "nsfw":true
    },
    {
      "id":"49ff5937-24be-440e-bbf7-2b501fe0c880",
      "text":[
        "Strata czasu."
      ],
      "created_at":"2016-03-26T22:37:26+00:00",
      "nsfw":true
    },
    {
      "id":"4a251b26-7ced-4879-b30e-8bb46bb209ce",
      "text":[
        "Mimo\\u015br\\u00f3d e."
      ],
      "created_at":"2016-03-26T23:52:07+00:00",
      "nsfw":true
    },
    {
      "id":"4a3a8afc-e9a8-4127-a4c7-e9537f1ed48e",
      "text":[
        "\\u017bale Karoliny."
      ],
      "created_at":"2016-03-27T07:32:39+00:00",
      "nsfw":true
    },
    {
      "id":"4ac797b4-0bef-4317-ae5e-8184b2cdc0e2",
      "text":[
        "Klej w tubce."
      ],
      "created_at":"2016-04-07T16:49:27+00:00",
      "nsfw":true
    },
    {
      "id":"4b469d9c-4296-4b79-90b6-1d5ec671fd64",
      "text":[
        "Ksi\\u0105dz Robak."
      ],
      "created_at":"2016-03-26T22:52:55+00:00",
      "nsfw":true
    },
    {
      "id":"4b77ea66-b847-42dc-927a-2d6fb74d5b7b",
      "text":[
        "Deceptikony."
      ],
      "created_at":"2016-05-16T17:27:55+00:00",
      "nsfw":true
    },
    {
      "id":"4c998389-edbb-4e57-a037-8c91772d166b",
      "text":[
        "Ser spod napleta."
      ],
      "created_at":"2016-03-26T23:04:05+00:00",
      "nsfw":true
    },
    {
      "id":"4ca73e5c-5241-49d5-8c04-639042339e26",
      "text":[
        "Szcz\\u0119koczu\\u0142ki."
      ],
      "created_at":"2016-03-26T22:30:33+00:00",
      "nsfw":true
    },
    {
      "id":"4cba43a4-e2df-4500-9bad-f0f7877b449f",
      "text":[
        "Przemyt."
      ],
      "created_at":"2016-03-26T23:54:38+00:00",
      "nsfw":true
    },
    {
      "id":"4cbddc7c-d64c-4719-92c2-fadff3de984f",
      "text":[
        "Korespondencja z Marcinem."
      ],
      "created_at":"2016-03-26T23:58:24+00:00",
      "nsfw":true
    },
    {
      "id":"4cc3a8a7-457a-4271-94db-ee27986c2fdf",
      "text":[
        "Czopki z g\\u0142\\u00f3w!"
      ],
      "created_at":"2016-03-26T23:04:40+00:00",
      "nsfw":true
    },
    {
      "id":"4d1ae977-ed72-4cd7-bf38-9b1229b7da72",
      "text":[
        "Kolimator."
      ],
      "created_at":"2016-03-26T23:48:43+00:00",
      "nsfw":true
    },
    {
      "id":"4e2963d6-25be-4bfa-a088-d46c0acf0d53",
      "text":[
        "Flet w dupie."
      ],
      "created_at":"2016-04-07T16:53:06+00:00",
      "nsfw":true
    },
    {
      "id":"4e42dd69-cce1-4323-a1ce-9f2a36f13b7a",
      "text":[
        "Przyspieszenie obrotowe."
      ],
      "created_at":"2016-03-26T23:53:21+00:00",
      "nsfw":true
    },
    {
      "id":"4ec875ba-c4a8-4f54-b6d7-e7dbfccdf669",
      "text":[
        "Wielki problem."
      ],
      "created_at":"2016-03-26T22:29:33+00:00",
      "nsfw":true
    },
    {
      "id":"4f6086ef-b754-45c8-9eeb-19ae453425e3",
      "text":[
        "Grupy barbituran\\u00f3w."
      ],
      "created_at":"2016-03-27T07:32:16+00:00",
      "nsfw":true
    },
    {
      "id":"4f7ed8bb-c8fd-48c6-925c-c412a10b685a",
      "text":[
        "Papie\\u017c Polak."
      ],
      "created_at":"2016-06-14T15:04:43+00:00",
      "nsfw":true
    },
    {
      "id":"4fcd9747-67e2-4b3d-83ea-f9b6ccdea09c",
      "text":[
        "Rozkrok."
      ],
      "created_at":"2016-03-26T22:57:28+00:00",
      "nsfw":true
    },
    {
      "id":"5008bdb1-7a16-439a-8b01-eacf382f433b",
      "text":[
        "Prawe kolano."
      ],
      "created_at":"2016-03-26T22:25:57+00:00",
      "nsfw":true
    },
    {
      "id":"523b4fdd-8717-45d3-b47a-3d059d84c663",
      "text":[
        "Przeszczep."
      ],
      "created_at":"2016-03-26T22:59:02+00:00",
      "nsfw":true
    },
    {
      "id":"526ca804-236e-4ec9-adf8-c557289dbc5a",
      "text":[
        "Brudna \\u015bcierka."
      ],
      "created_at":"2016-03-28T15:28:48+00:00",
      "nsfw":true
    },
    {
      "id":"52b9de11-eb48-40a3-bc75-7f8ba8745a8b",
      "text":[
        "Krzywka styczna."
      ],
      "created_at":"2016-03-26T23:49:44+00:00",
      "nsfw":true
    },
    {
      "id":"53525cd8-fe09-446b-aff0-8d63d113db90",
      "text":[
        "Remont klasztoru."
      ],
      "created_at":"2017-08-12T23:29:22+00:00",
      "nsfw":true
    },
    {
      "id":"5386152a-2601-4a9f-a1f3-95b3ce89a333",
      "text":[
        "Psy w niewoli."
      ],
      "created_at":"2016-04-07T16:51:26+00:00",
      "nsfw":true
    },
    {
      "id":"54411261-12a6-4ffa-89a1-93f36ac80f8e",
      "text":[
        "Faluj\\u0105ce sad\\u0142o."
      ],
      "created_at":"2016-05-16T17:37:19+00:00",
      "nsfw":true
    },
    {
      "id":"547bc4fc-fd76-46ae-aeb9-e9ef2c3b573f",
      "text":[
        "Przep\\u0142yw turbulentny."
      ],
      "created_at":"2016-04-07T16:53:31+00:00",
      "nsfw":true
    },
    {
      "id":"548e5a85-1ad0-415e-a423-56cf020542ff",
      "text":[
        "\\u015aledzik na raz."
      ],
      "created_at":"2016-03-27T00:10:58+00:00",
      "nsfw":true
    },
    {
      "id":"55f5472b-1d63-4118-b86c-b956eb049480",
      "text":[
        "Dariusz Michalczewski."
      ],
      "created_at":"2016-03-26T22:30:23+00:00",
      "nsfw":true
    },
    {
      "id":"5664a3d1-689a-4399-88a4-8d6b8aaa168e",
      "text":[
        "Obci\\u0105ganie."
      ],
      "created_at":"2016-03-26T23:54:32+00:00",
      "nsfw":true
    },
    {
      "id":"56ea15cb-b9c9-4614-8db6-4a8fe7bd7eac",
      "text":[
        "Taka \\u015bwinia kurwa."
      ],
      "created_at":"2016-04-18T23:25:27+00:00",
      "nsfw":true
    },
    {
      "id":"57350223-5458-448f-afe1-ad8e96b7536d",
      "text":[
        "Chuj."
      ],
      "created_at":"2016-03-26T22:42:11+00:00",
      "nsfw":true
    },
    {
      "id":"58ad8adb-822d-417c-bdf3-4f9f1123ed69",
      "text":[
        "Kasa za ruchanie."
      ],
      "created_at":"2016-03-26T23:53:51+00:00",
      "nsfw":true
    },
    {
      "id":"59418c3d-50e6-4328-972d-940fdefe17d9",
      "text":[
        "Kie\\u0142baska."
      ],
      "created_at":"2016-03-26T23:01:44+00:00",
      "nsfw":true
    },
    {
      "id":"59461829-9dc6-4dcc-99fa-3505dd95c33b",
      "text":[
        "Ca\\u0142ka nieoznaczona."
      ],
      "created_at":"2016-04-12T12:57:19+00:00",
      "nsfw":true
    },
    {
      "id":"5974c2b4-1de8-4e1b-a63b-4f6acb1c68eb",
      "text":[
        "Wargi sromowe pod pach\\u0105."
      ],
      "created_at":"2016-05-16T17:38:45+00:00",
      "nsfw":true
    },
    {
      "id":"5ab38d85-6ce8-4907-ac7f-7bbdc7c9cc3c",
      "text":[
        "Egzorcyzmy w \\u015brod\\u0119."
      ],
      "created_at":"2016-03-27T07:17:50+00:00",
      "nsfw":true
    },
    {
      "id":"5ad79b8d-1495-427e-b67f-719a898666cc",
      "text":[
        "Magnetyczna liczba kwantowa."
      ],
      "created_at":"2016-03-27T07:21:50+00:00",
      "nsfw":true
    },
    {
      "id":"5b9acaa0-708a-42b2-8f23-b35068f06dfc",
      "text":[
        "Wied\\u017amin Piotr."
      ],
      "created_at":"2016-03-26T22:50:30+00:00",
      "nsfw":true
    },
    {
      "id":"5d0c668b-1ee8-4fe6-b84b-6b7c329fee44",
      "text":[
        "\\u0141o\\u017cysko."
      ],
      "created_at":"2016-03-26T22:31:24+00:00",
      "nsfw":true
    },
    {
      "id":"5d27a035-1dd4-4f7e-aebe-f1a3805dccb4",
      "text":[
        "Kamil."
      ],
      "created_at":"2016-03-26T23:44:14+00:00",
      "nsfw":true
    },
    {
      "id":"5d8d659a-5118-40df-ac46-821a05b6eac9",
      "text":[
        "Lizanie dupy psa."
      ],
      "created_at":"2016-05-16T17:28:17+00:00",
      "nsfw":true
    },
    {
      "id":"5e17d68a-1f6b-434a-a0af-772c7e65c577",
      "text":[
        "Ruskie pierogi."
      ],
      "created_at":"2016-03-26T23:03:37+00:00",
      "nsfw":true
    },
    {
      "id":"5e4176e4-c1fe-4299-a505-8ac663f7b47d",
      "text":[
        "Nicpo\\u0144 Przemek."
      ],
      "created_at":"2016-03-26T22:48:39+00:00",
      "nsfw":true
    },
    {
      "id":"5e43a1f9-18fd-4077-985e-e341f170ddfe",
      "text":[
        "Moja matka."
      ],
      "created_at":"2016-03-27T07:28:03+00:00",
      "nsfw":true
    },
    {
      "id":"5e6910e6-5570-4e2f-a18b-64a0b2d14322",
      "text":[
        "Filharmonia Narodowa."
      ],
      "created_at":"2016-03-27T07:24:28+00:00",
      "nsfw":true
    },
    {
      "id":"5ed18ef7-5e37-4d4e-85c6-e43472f5159a",
      "text":[
        "Kupa na \\u015bcianie."
      ],
      "created_at":"2016-03-26T22:59:19+00:00",
      "nsfw":true
    },
    {
      "id":"5f619122-c721-4e4a-86ac-c43852b88184",
      "text":[
        "Kurwa."
      ],
      "created_at":"2016-03-27T00:04:19+00:00",
      "nsfw":true
    },
    {
      "id":"5f6befdc-87da-43b1-9cc1-33a5cb86a01e",
      "text":[
        "Kaczka Dziwaczka."
      ],
      "created_at":"2016-04-01T22:28:52+00:00",
      "nsfw":true
    },
    {
      "id":"60140fd4-18a1-4826-b205-47e3fef02089",
      "text":[
        "Ramzes II."
      ],
      "created_at":"2016-03-27T07:30:19+00:00",
      "nsfw":true
    },
    {
      "id":"616d7976-873e-4d10-a032-8210af443d0d",
      "text":[
        "Ma\\u0142e jajca."
      ],
      "created_at":"2016-04-07T16:52:05+00:00",
      "nsfw":true
    },
    {
      "id":"61bacd03-d2f0-4734-a137-3ff5cfcf9c5f",
      "text":[
        "Kleopatra na wkurwie."
      ],
      "created_at":"2016-04-07T16:48:06+00:00",
      "nsfw":true
    },
    {
      "id":"61c8d7a7-52af-455f-a529-e8a1041ea0d2",
      "text":[
        "Arkusz A4."
      ],
      "created_at":"2016-03-27T00:10:13+00:00",
      "nsfw":true
    },
    {
      "id":"61d864e4-cb97-487d-96a2-1d9ebc45c1eb",
      "text":[
        "Tg(30)"
      ],
      "created_at":"2016-03-26T22:45:44+00:00",
      "nsfw":true
    },
    {
      "id":"61da9ff2-e006-49d8-8009-b07360a972c9",
      "text":[
        "Wymiotowanie p\\u0142odami."
      ],
      "created_at":"2016-03-27T00:07:53+00:00",
      "nsfw":true
    },
    {
      "id":"6203f5f4-31e6-464f-b1d4-feb2f2116343",
      "text":[
        "Autoboty."
      ],
      "created_at":"2016-10-10T20:46:55+00:00",
      "nsfw":true
    },
    {
      "id":"624497f3-c9a0-49f3-804f-8220cfb5d423",
      "text":[
        "Gej czarodziej."
      ],
      "created_at":"2016-03-26T23:01:13+00:00",
      "nsfw":true
    },
    {
      "id":"6244a305-27ff-40cf-8926-1b5fb0cd684d",
      "text":[
        "Bicki ze stali."
      ],
      "created_at":"2016-10-10T21:54:28+00:00",
      "nsfw":true
    },
    {
      "id":"625f6385-4a05-43e0-bc43-a878a51007cb",
      "text":[
        "Wpadka przed 18."
      ],
      "created_at":"2016-03-27T00:04:58+00:00",
      "nsfw":true
    },
    {
      "id":"6379f262-fd33-4b33-bee6-f68cf63dac69",
      "text":[
        "Grodzisk Mazowiecki."
      ],
      "created_at":"2016-10-10T21:14:16+00:00",
      "nsfw":true
    },
    {
      "id":"64bf0b4c-89cc-437c-8296-246fe5566052",
      "text":[
        "Kastracja."
      ],
      "created_at":"2016-03-26T22:22:16+00:00",
      "nsfw":true
    },
    {
      "id":"6502cbc6-bef2-4c60-8b9c-4308d92586e4",
      "text":[
        "Diablo 2."
      ],
      "created_at":"2016-03-26T22:29:57+00:00",
      "nsfw":true
    },
    {
      "id":"66ec5990-92e9-47fc-839a-61d175824543",
      "text":[
        "Woda w kiblu."
      ],
      "created_at":"2016-03-27T00:09:49+00:00",
      "nsfw":true
    },
    {
      "id":"68106bc0-05ce-47b8-a428-e6d11e1161bc",
      "text":[
        "Odradzam si\\u0119 i od razu umieram."
      ],
      "created_at":"2017-08-12T23:29:40+00:00",
      "nsfw":true
    },
    {
      "id":"689709e4-1041-4074-b14a-89e4c1bc7e19",
      "text":[
        "Klacz w stajni."
      ],
      "created_at":"2016-05-16T17:14:53+00:00",
      "nsfw":true
    },
    {
      "id":"690d136f-932a-4ae5-9899-465e1cafccce",
      "text":[
        "Nietolerancyjny wombat."
      ],
      "created_at":"2016-03-26T22:38:27+00:00",
      "nsfw":true
    },
    {
      "id":"69a56b44-e0c4-43f4-921d-4844500983ee",
      "text":[
        "Bezbo\\u017cnik."
      ],
      "created_at":"2016-03-26T22:45:57+00:00",
      "nsfw":true
    },
    {
      "id":"69c4d3dc-4602-4c0f-ad30-4b3b195612dc",
      "text":[
        "Nie, to jest s\\u0142abe."
      ],
      "created_at":"2016-03-31T21:05:44+00:00",
      "nsfw":true
    },
    {
      "id":"69dc5f0c-9648-4ba6-85c0-2eae24b45156",
      "text":[
        "Nawyki siostry ciotecznej."
      ],
      "created_at":"2016-03-28T15:29:53+00:00",
      "nsfw":true
    },
    {
      "id":"6a02d623-d79e-4016-916a-4871ff426a8e",
      "text":[
        "Baraszkowanie."
      ],
      "created_at":"2016-03-27T00:06:05+00:00",
      "nsfw":true
    },
    {
      "id":"6aa65971-0fc6-45b6-9069-605b8da9970f",
      "text":[
        "Dawne czasy."
      ],
      "created_at":"2016-03-26T23:59:10+00:00",
      "nsfw":true
    },
    {
      "id":"6aa9fd32-e83c-472c-96ce-1d45807a8b06",
      "text":[
        "Bolek."
      ],
      "created_at":"2016-03-26T22:21:38+00:00",
      "nsfw":true
    },
    {
      "id":"6c588a90-ac3c-4406-a22c-c21f157a9407",
      "text":[
        "Obraz o dupie."
      ],
      "created_at":"2016-06-14T15:22:11+00:00",
      "nsfw":true
    },
    {
      "id":"6c66060c-9b7f-45ea-95cf-17dfdc9a93dd",
      "text":[
        "Malinowy sok."
      ],
      "created_at":"2016-03-27T07:13:46+00:00",
      "nsfw":true
    },
    {
      "id":"6ce1361d-dfe0-4b6a-89e3-6820570b9382",
      "text":[
        "Orkiestra d\\u0119ta."
      ],
      "created_at":"2016-04-07T16:53:00+00:00",
      "nsfw":true
    },
    {
      "id":"6d92d4ef-3f23-4ab8-b6d4-8772dfcd5705",
      "text":[
        "Modernizacja szopy."
      ],
      "created_at":"2016-03-27T07:17:03+00:00",
      "nsfw":true
    },
    {
      "id":"6e750144-5261-4061-a047-e1fb41c9b336",
      "text":[
        "Grecja w opa\\u0142ach."
      ],
      "created_at":"2016-03-26T23:57:12+00:00",
      "nsfw":true
    },
    {
      "id":"6ecde004-7ee3-4d52-aaa3-cd556136d36f",
      "text":[
        "Lewe kolano."
      ],
      "created_at":"2016-03-26T22:29:21+00:00",
      "nsfw":true
    },
    {
      "id":"6f00a379-0e62-43dd-a731-12d5c595f283",
      "text":[
        "Mechanizm zapadkowy."
      ],
      "created_at":"2016-04-07T16:47:58+00:00",
      "nsfw":true
    },
    {
      "id":"6f433716-3bcb-4143-98a4-0f8bfd5d2461",
      "text":[
        "Liczyd\\u0142o."
      ],
      "created_at":"2016-03-27T00:17:30+00:00",
      "nsfw":true
    },
    {
      "id":"6f8e99bb-e418-4e0f-9ac5-6bcb4234d1a7",
      "text":[
        "Rozpierdalacz polny."
      ],
      "created_at":"2016-03-27T00:11:16+00:00",
      "nsfw":true
    },
    {
      "id":"6fe9e3a8-f850-4ac2-b41e-a7f822d2ec19",
      "text":[
        "Jebane psy."
      ],
      "created_at":"2016-05-05T21:46:20+00:00",
      "nsfw":true
    },
    {
      "id":"701f0b92-e3bb-4eb5-9b13-ae6b4506336b",
      "text":[
        "Aktywny zawodowo Przemek."
      ],
      "created_at":"2016-03-27T00:14:13+00:00",
      "nsfw":true
    },
    {
      "id":"702f7ba1-b9ed-4101-bd4a-fb6c9fe792e8",
      "text":[
        "Tere fere."
      ],
      "created_at":"2016-03-26T22:42:32+00:00",
      "nsfw":true
    },
    {
      "id":"708a7251-d78c-43c5-9d0a-fe465fd612f0",
      "text":[
        "Adam Mickiewicz."
      ],
      "created_at":"2016-03-26T23:55:17+00:00",
      "nsfw":true
    },
    {
      "id":"71deeac9-56b8-4741-86df-a215397f3c25",
      "text":[
        "Prorok Mohamed."
      ],
      "created_at":"2016-03-26T22:44:09+00:00",
      "nsfw":true
    },
    {
      "id":"71f57f6c-4735-4510-af91-04e2d88d5ccf",
      "text":[
        "Nat\\u0119\\u017cenie bobra."
      ],
      "created_at":"2016-10-10T21:13:53+00:00",
      "nsfw":true
    },
    {
      "id":"7224dcae-67f7-49b1-b0e1-fcd52955982a",
      "text":[
        "Pierdolony bobas."
      ],
      "created_at":"2016-03-26T23:43:33+00:00",
      "nsfw":true
    },
    {
      "id":"733130e4-53f6-424e-a55a-bb2dce7696d1",
      "text":[
        "Bezwodnik kwasowy."
      ],
      "created_at":"2016-03-27T07:18:56+00:00",
      "nsfw":true
    },
    {
      "id":"73352bb2-0c13-4780-bebc-8ff351fd7dd9",
      "text":[
        "Drewniany zagajnik."
      ],
      "created_at":"2016-03-26T22:43:00+00:00",
      "nsfw":true
    },
    {
      "id":"7342ece5-e086-405e-969a-daca183456fc",
      "text":[
        "Dwie \\u0142yse dziwki."
      ],
      "created_at":"2016-03-26T22:56:27+00:00",
      "nsfw":true
    },
    {
      "id":"7373e521-cff4-45f2-89ca-cd16628f8bb6",
      "text":[
        "Guziec kurwa z Afryki. Czaisz kurwa gu\\u017aca? Taka \\u015bwinia kurwa. Jaki guziec?!"
      ],
      "created_at":"2016-04-18T23:25:06+00:00",
      "nsfw":true
    },
    {
      "id":"73c2c385-56e2-4b3e-a240-30e04fb6f0f4",
      "text":[
        "Kangur Losu."
      ],
      "created_at":"2016-03-27T00:13:53+00:00",
      "nsfw":true
    },
    {
      "id":"74b5437b-b615-4203-abf8-92a2db8b979e",
      "text":[
        "Gotowanie zupy."
      ],
      "created_at":"2016-03-27T00:09:19+00:00",
      "nsfw":true
    },
    {
      "id":"759d4293-a11d-4e2d-8488-acf048b4d4ae",
      "text":[
        "Banialuki."
      ],
      "created_at":"2016-03-27T00:00:39+00:00",
      "nsfw":true
    },
    {
      "id":"75e43217-ac51-43f0-a62b-e7e249651101",
      "text":[
        "Kanapka z mielonk\\u0105."
      ],
      "created_at":"2016-04-12T12:58:09+00:00",
      "nsfw":true
    },
    {
      "id":"76326f2d-bbb3-4960-82e9-db6403bddbe8",
      "text":[
        "Kawa\\u0142 ch\\u0142opa."
      ],
      "created_at":"2016-03-26T22:46:36+00:00",
      "nsfw":true
    },
    {
      "id":"7638f88c-4cbf-4288-874c-7b82d8f872fe",
      "text":[
        "Heretyk."
      ],
      "created_at":"2016-10-10T21:48:02+00:00",
      "nsfw":true
    },
    {
      "id":"76ad2241-f495-4be6-8a99-bc5f952fc9aa",
      "text":[
        "Rzeczywista pr\\u0119dko\\u015b\\u0107 cz\\u0119\\u015bci czynnej pasa."
      ],
      "created_at":"2016-04-07T16:58:07+00:00",
      "nsfw":true
    },
    {
      "id":"76c9f636-eb65-4ed5-bfa0-d0c1bfd3d2ba",
      "text":[
        "Chyba ryba."
      ],
      "created_at":"2016-05-17T19:05:09+00:00",
      "nsfw":true
    },
    {
      "id":"76dea553-6f89-4c5c-bcd1-02ee9989f380",
      "text":[
        "Hehe! Jeba\\u0107 czarnych!"
      ],
      "created_at":"2016-10-10T21:58:30+00:00",
      "nsfw":true
    },
    {
      "id":"7700280b-2d13-4552-a247-7b59cf9c6533",
      "text":[
        "Pismo zwierzoludzi."
      ],
      "created_at":"2016-03-26T23:46:11+00:00",
      "nsfw":true
    },
    {
      "id":"7714e870-59b0-4879-80b2-2674ebefe5ce",
      "text":[
        "Kontratak znad Wieprza."
      ],
      "created_at":"2016-06-14T15:24:45+00:00",
      "nsfw":true
    },
    {
      "id":"77b3f39e-9f14-4860-8b91-336c14042713",
      "text":[
        "\\u015aliniaczek."
      ],
      "created_at":"2016-03-27T00:17:37+00:00",
      "nsfw":true
    },
    {
      "id":"77b70bfb-d42c-4ec8-aecf-17919ab758ba",
      "text":[
        "\\u0141opatka."
      ],
      "created_at":"2016-03-26T22:54:13+00:00",
      "nsfw":true
    },
    {
      "id":"788ca60f-3bbd-4c9d-a558-5988d9d6666b",
      "text":[
        "Bezimienny."
      ],
      "created_at":"2016-05-16T17:31:02+00:00",
      "nsfw":true
    },
    {
      "id":"789fa7f9-4446-4b6b-a71b-7329b28effc1",
      "text":[
        "Matko Bosko i 100 milicjant\\u00f3w!~"
      ],
      "created_at":"2016-10-10T21:21:45+00:00",
      "nsfw":true
    },
    {
      "id":"7adf3d67-d0ff-4f82-ad74-e835a428b9ac",
      "text":[
        "Klapsy."
      ],
      "created_at":"2016-03-26T23:55:38+00:00",
      "nsfw":true
    },
    {
      "id":"7bf0c538-c65f-431c-82fa-5029c0d65af1",
      "text":[
        "Katakan."
      ],
      "created_at":"2016-03-26T22:50:14+00:00",
      "nsfw":true
    },
    {
      "id":"7d6aa95e-827f-4196-a79b-80ebed48f8c8",
      "text":[
        "Sin(54)"
      ],
      "created_at":"2016-03-26T22:48:25+00:00",
      "nsfw":true
    },
    {
      "id":"7d7c40fc-80db-4c1b-a0d4-ca8edd55fb63",
      "text":[
        "Piotrze!"
      ],
      "created_at":"2016-03-26T22:59:13+00:00",
      "nsfw":true
    },
    {
      "id":"7d9da85f-abeb-429b-9c08-6f0b6ae91006",
      "text":[
        "Prima Aprilis."
      ],
      "created_at":"2016-03-27T00:00:33+00:00",
      "nsfw":true
    },
    {
      "id":"7dfd0238-e288-4eb5-8326-5252570fba85",
      "text":[
        "Ma\\u0142a pa\\u0142a."
      ],
      "created_at":"2016-03-26T22:25:01+00:00",
      "nsfw":true
    },
    {
      "id":"7e19bde4-0dd4-46a0-aa53-affb851f53df",
      "text":[
        "Dmuchanie balon\\u00f3w."
      ],
      "created_at":"2016-03-26T23:56:20+00:00",
      "nsfw":true
    },
    {
      "id":"7e7ebb24-76b9-4fa2-bfa2-c13e82e8bd92",
      "text":[
        "Dupa z przodu."
      ],
      "created_at":"2016-05-16T17:29:03+00:00",
      "nsfw":true
    },
    {
      "id":"7f8f9787-79dd-4006-bcb6-ee688bdb5c77",
      "text":[
        "Karmazynowy Bartek."
      ],
      "created_at":"2016-03-27T07:14:13+00:00",
      "nsfw":true
    },
    {
      "id":"811c5fb3-597d-4bf6-ab6c-5620c2ef9c17",
      "text":[
        "Wpierdol."
      ],
      "created_at":"2016-03-26T23:03:42+00:00",
      "nsfw":true
    },
    {
      "id":"812f2656-5b13-41dd-8551-d5d39fe13087",
      "text":[
        "Karuzela strachu."
      ],
      "created_at":"2016-04-07T16:48:33+00:00",
      "nsfw":true
    },
    {
      "id":"81b1a61f-705b-441b-bba6-772910f6f847",
      "text":[
        "\\u0179d\\u017ab\\u0142o trawy."
      ],
      "created_at":"2016-03-26T22:22:08+00:00",
      "nsfw":true
    },
    {
      "id":"82437108-e65f-47dd-b85e-00ed62ba74c5",
      "text":[
        "Kandydat na prezydenta."
      ],
      "created_at":"2016-05-16T17:16:45+00:00",
      "nsfw":true
    },
    {
      "id":"827861c7-33ab-4d55-b5f6-d92d32dba1eb",
      "text":[
        "Andrzej Dupa."
      ],
      "created_at":"2016-03-26T22:21:24+00:00",
      "nsfw":true
    },
    {
      "id":"827af3ec-d0f7-493d-8f08-8e37627ddab3",
      "text":[
        "\\u015aled\\u017a."
      ],
      "created_at":"2016-04-12T12:57:49+00:00",
      "nsfw":true
    },
    {
      "id":"82920ac3-eedb-4415-8f93-be7b32ed7e2a",
      "text":[
        "Balony z helem."
      ],
      "created_at":"2016-10-10T21:13:42+00:00",
      "nsfw":true
    },
    {
      "id":"82e11c93-1f05-4744-b068-1298fed12f43",
      "text":[
        "Jaki\\u015b tam Azjata."
      ],
      "created_at":"2016-03-27T15:06:32+00:00",
      "nsfw":true
    },
    {
      "id":"84bc5503-ab23-44c3-9796-abb15f671d10",
      "text":[
        "Malowanie chujem."
      ],
      "created_at":"2016-03-27T00:18:54+00:00",
      "nsfw":true
    },
    {
      "id":"84d373ca-7065-4890-a988-e9fc81165aed",
      "text":[
        "Dupa na k\\u00f3\\u0142kach."
      ],
      "created_at":"2016-03-26T22:49:43+00:00",
      "nsfw":true
    },
    {
      "id":"8504ecb0-7b34-4cee-9833-d969ce4ac0fe",
      "text":[
        "Jebane peda\\u0142y."
      ],
      "created_at":"2016-05-16T17:32:00+00:00",
      "nsfw":true
    },
    {
      "id":"860b037e-de45-486a-a4a7-ca7dd953519b",
      "text":[
        "Bardzo dobra zupa."
      ],
      "created_at":"2016-03-26T22:24:56+00:00",
      "nsfw":true
    },
    {
      "id":"8634f0b6-fd4d-4ab8-a37d-6b40704dba21",
      "text":[
        "Zapina\\u0107 kogo\\u015b w cewe."
      ],
      "created_at":"2016-03-26T23:00:37+00:00",
      "nsfw":true
    },
    {
      "id":"869db50d-8353-476e-98c7-078b967b8d56",
      "text":[
        "Nicpo\\u0144 Andrzej."
      ],
      "created_at":"2016-03-28T15:28:36+00:00",
      "nsfw":true
    },
    {
      "id":"86b8eb56-6bdb-416b-bcdc-15c0930051cf",
      "text":[
        "Napierdalanie w perkusj\\u0119."
      ],
      "created_at":"2016-03-26T23:55:48+00:00",
      "nsfw":true
    },
    {
      "id":"86bc7310-02bb-4c0c-8c59-02b1b0fb93e9",
      "text":[
        "Cycuszki."
      ],
      "created_at":"2016-03-26T22:42:41+00:00",
      "nsfw":true
    },
    {
      "id":"87098d5b-6f73-447b-bbb2-9d4e91bcfc73",
      "text":[
        "Sa\\u0142ata z dupy."
      ],
      "created_at":"2016-03-26T23:43:56+00:00",
      "nsfw":true
    },
    {
      "id":"87404629-a5cf-4b7b-ada1-57ed99e9c114",
      "text":[
        "Rzep."
      ],
      "created_at":"2016-03-26T22:34:26+00:00",
      "nsfw":true
    },
    {
      "id":"874a389f-bfd9-4cf1-a985-b1897404180b",
      "text":[
        "Barack Obama."
      ],
      "created_at":"2016-06-14T15:23:23+00:00",
      "nsfw":true
    },
    {
      "id":"87ece4dd-2515-40d7-83ad-2bd4730868c0",
      "text":[
        "Rafa\\u0142 i jego bulwersy."
      ],
      "created_at":"2016-03-26T22:50:52+00:00",
      "nsfw":true
    },
    {
      "id":"882873a1-3067-41b9-9446-cc1f42f67263",
      "text":[
        "Dorodna pyra."
      ],
      "created_at":"2016-05-30T20:08:33+00:00",
      "nsfw":true
    },
    {
      "id":"883c54f2-8b8f-445f-acff-407d5e80468f",
      "text":[
        "Rude dziecko."
      ],
      "created_at":"2016-03-26T23:43:46+00:00",
      "nsfw":true
    },
    {
      "id":"88409a91-1043-4998-8c15-14b40b660f34",
      "text":[
        "Belka statycznie niewyznaczalna."
      ],
      "created_at":"2016-03-27T07:27:56+00:00",
      "nsfw":true
    },
    {
      "id":"887b51c4-d7dd-4447-b365-6c89e27c1928",
      "text":[
        "B\\u0105bel."
      ],
      "created_at":"2016-10-10T21:54:18+00:00",
      "nsfw":true
    },
    {
      "id":"88fe3f6c-4100-4486-b6bd-1243db824ac9",
      "text":[
        "Makabryczne odkrycie."
      ],
      "created_at":"2016-03-26T23:45:44+00:00",
      "nsfw":true
    },
    {
      "id":"89599729-1869-40c1-adf0-b3d00073e116",
      "text":[
        "6 g\\u0142\\u00f3w."
      ],
      "created_at":"2016-03-26T23:45:37+00:00",
      "nsfw":true
    },
    {
      "id":"89db152c-63e1-4391-bd29-6ea1c3724771",
      "text":[
        "Chemia organiczna."
      ],
      "created_at":"2016-03-27T07:20:28+00:00",
      "nsfw":true
    },
    {
      "id":"89fc52f4-7040-4c0e-8314-1b35bf087193",
      "text":[
        "Malinowy sok."
      ],
      "created_at":"2016-03-28T15:28:43+00:00",
      "nsfw":true
    },
    {
      "id":"8a88d4df-3978-4bf1-b073-77e36e2fb5e3",
      "text":[
        "Adam"
      ],
      "created_at":"2016-03-26T22:18:53+00:00",
      "nsfw":true
    },
    {
      "id":"8b3546b1-feed-44a7-9f3f-a7eda7295295",
      "text":[
        "Rozb\\u00f3jnicy!"
      ],
      "created_at":"2016-03-27T00:12:42+00:00",
      "nsfw":true
    },
    {
      "id":"8d991bea-ff6a-48e4-b50c-fda72f17d571",
      "text":[
        "Wied\\u017ami\\u0144skie zlecenie."
      ],
      "created_at":"2016-03-27T00:11:43+00:00",
      "nsfw":true
    },
    {
      "id":"8d9d2f86-0c9f-401d-a499-152221413c5f",
      "text":[
        "\\u015awi\\u0119to Trzech Kr\\u00f3li."
      ],
      "created_at":"2016-03-26T22:40:51+00:00",
      "nsfw":true
    },
    {
      "id":"8dd1d55c-1c1e-4ffb-9bc9-7db66861d90f",
      "text":[
        "Klemens."
      ],
      "created_at":"2016-03-26T22:20:01+00:00",
      "nsfw":true
    },
    {
      "id":"91121cff-9c11-46ae-9c48-e205ae96a91c",
      "text":[
        "Zakupy w biedronce."
      ],
      "created_at":"2016-06-14T15:22:20+00:00",
      "nsfw":true
    },
    {
      "id":"936d37c4-f6d8-4961-813f-9231b6765ffa",
      "text":[
        "Dupa na twarzy."
      ],
      "created_at":"2016-04-07T16:50:12+00:00",
      "nsfw":true
    },
    {
      "id":"93e8e324-b392-4a6c-86a6-fa7edb6d6762",
      "text":[
        "Warczenie na nieznajomych."
      ],
      "created_at":"2016-04-07T16:53:20+00:00",
      "nsfw":true
    },
    {
      "id":"94172ebb-40d2-4868-b4e5-0af9718b721d",
      "text":[
        "Z\\u0142y wyb\\u00f3r."
      ],
      "created_at":"2016-03-26T23:57:32+00:00",
      "nsfw":true
    },
    {
      "id":"953fd689-a584-4f92-b5a8-93598446d6fa",
      "text":[
        "Kuracja odbytu."
      ],
      "created_at":"2016-03-26T23:56:34+00:00",
      "nsfw":true
    },
    {
      "id":"957e816b-4f4c-4748-b394-8b50bc23d709",
      "text":[
        "Knur."
      ],
      "created_at":"2016-03-26T23:59:17+00:00",
      "nsfw":true
    },
    {
      "id":"9593b919-31d9-42d9-8e4d-a955122f1035",
      "text":[
        "Pryszcz na japie."
      ],
      "created_at":"2016-05-16T17:15:44+00:00",
      "nsfw":true
    },
    {
      "id":"95a7e55d-36e0-4258-9792-a2c239f283f4",
      "text":[
        "Soki z foki."
      ],
      "created_at":"2016-04-11T20:09:15+00:00",
      "nsfw":true
    },
    {
      "id":"95b8d4d5-2e73-4ef0-8bd5-8f7f90381274",
      "text":[
        "B\\u0105k."
      ],
      "created_at":"2016-03-27T15:07:05+00:00",
      "nsfw":true
    },
    {
      "id":"95d2eb92-cd85-4e55-9ab3-f8a3e4ff4c48",
      "text":[
        "Pas tatusia."
      ],
      "created_at":"2016-03-26T22:29:51+00:00",
      "nsfw":true
    },
    {
      "id":"96473b2d-ebfa-4ff6-80d2-6774e5c421a1",
      "text":[
        "Motywacyjny wpierdol."
      ],
      "created_at":"2016-05-16T17:18:36+00:00",
      "nsfw":true
    },
    {
      "id":"969a4242-2c0c-41d2-9728-167ea8ca5a02",
      "text":[
        "Grubas na bramie."
      ],
      "created_at":"2016-03-27T00:02:38+00:00",
      "nsfw":true
    },
    {
      "id":"96b5045e-eb52-4500-a732-e7c05ff07f68",
      "text":[
        "Pedalskie mokasyny."
      ],
      "created_at":"2016-03-27T00:01:15+00:00",
      "nsfw":true
    },
    {
      "id":"97255341-4ba2-4ffc-a73a-af16fcf9e671",
      "text":[
        "Trey gej."
      ],
      "created_at":"2016-05-16T17:16:14+00:00",
      "nsfw":true
    },
    {
      "id":"97d7645d-6b8a-4e72-abb8-0a34746bb7e2",
      "text":[
        "Spocony Hagrid."
      ],
      "created_at":"2016-03-27T00:12:32+00:00",
      "nsfw":true
    },
    {
      "id":"97ddacf7-a532-467b-9311-d5f7ad187ea9",
      "text":[
        "W\\u0119dkarz \\u0141ukasz."
      ],
      "created_at":"2016-03-26T22:53:06+00:00",
      "nsfw":true
    },
    {
      "id":"97f43f8b-72f4-4996-b7c0-7abbb1b9112d",
      "text":[
        "Gradient."
      ],
      "created_at":"2016-04-12T12:58:55+00:00",
      "nsfw":true
    },
    {
      "id":"98612922-6b6c-46e6-b66c-589485f4124b",
      "text":[
        "Dionizos."
      ],
      "created_at":"2016-03-26T22:19:57+00:00",
      "nsfw":true
    },
    {
      "id":"987aaf62-7220-47f2-9f10-7ef63c00e808",
      "text":[
        "Orka w delikatesach."
      ],
      "created_at":"2016-04-12T13:00:13+00:00",
      "nsfw":true
    },
    {
      "id":"9911d945-cf75-456f-9ee8-9e249e3c7ab3",
      "text":[
        "Ten ty\\u0142eczek."
      ],
      "created_at":"2016-03-26T22:37:17+00:00",
      "nsfw":true
    },
    {
      "id":"999c51eb-17aa-46de-8beb-fe33fe3571a7",
      "text":[
        "Barach\\u0142o."
      ],
      "created_at":"2016-03-26T22:48:30+00:00",
      "nsfw":true
    },
    {
      "id":"9a8d638d-ce6d-49f3-b3da-cf8c9e63d61b",
      "text":[
        "Wikingowie."
      ],
      "created_at":"2016-03-27T00:12:36+00:00",
      "nsfw":true
    },
    {
      "id":"9ae626c0-42e2-4282-ac50-1d44d9ace2a0",
      "text":[
        "Tani obiad."
      ],
      "created_at":"2016-03-26T22:42:47+00:00",
      "nsfw":true
    },
    {
      "id":"9b1461f3-568c-4b12-a3f5-8c5c34bf2155",
      "text":[
        "Koalicja PO - PSL."
      ],
      "created_at":"2016-03-26T23:59:55+00:00",
      "nsfw":true
    },
    {
      "id":"9b724895-49d8-406c-8c45-eca448326305",
      "text":[
        "Barszcz z uszkami."
      ],
      "created_at":"2016-04-12T12:57:59+00:00",
      "nsfw":true
    },
    {
      "id":"9c6ccb5f-e884-49b4-b0e0-97b2b93e7271",
      "text":[
        "Kurczak z ro\\u017cna."
      ],
      "created_at":"2016-05-16T17:16:37+00:00",
      "nsfw":true
    },
    {
      "id":"9c8671f1-188a-4b87-a335-bf367cbe91b8",
      "text":[
        "ALLAHU AKBAR!"
      ],
      "created_at":"2016-03-26T22:43:56+00:00",
      "nsfw":true
    },
    {
      "id":"9cae982f-261c-4745-892c-d4f59e53734e",
      "text":[
        "Kupa z\\u0142omu."
      ],
      "created_at":"2016-03-28T15:29:39+00:00",
      "nsfw":true
    },
    {
      "id":"9cedad17-8723-4492-859e-1ff291d5531a",
      "text":[
        "Pstr\\u0105g."
      ],
      "created_at":"2016-03-27T07:13:26+00:00",
      "nsfw":true
    },
    {
      "id":"9e983d3f-c1e0-4ec4-b49c-6162d6280821",
      "text":[
        "Partyzantka."
      ],
      "created_at":"2016-03-26T22:34:55+00:00",
      "nsfw":true
    },
    {
      "id":"9ef60078-f10f-4617-ba76-27def0c68e84",
      "text":[
        "Piwo prawdziwego my\\u015bliwego."
      ],
      "created_at":"2016-03-26T23:05:02+00:00",
      "nsfw":true
    },
    {
      "id":"a00752d3-3346-475c-b343-37ae80d8437e",
      "text":[
        "Arcsin(12)"
      ],
      "created_at":"2016-03-26T22:45:52+00:00",
      "nsfw":true
    },
    {
      "id":"a1ecfd87-00ba-4899-87b4-b7a67369fd4d",
      "text":[
        "Ehhh... droz."
      ],
      "created_at":"2016-03-26T22:36:15+00:00",
      "nsfw":true
    },
    {
      "id":"a2a57649-7129-4425-9ba1-90125c1bb72a",
      "text":[
        "Liczba Poissona."
      ],
      "created_at":"2016-04-07T16:55:43+00:00",
      "nsfw":true
    },
    {
      "id":"a2c04379-f530-4b1f-bb85-864cc3760b99",
      "text":[
        "Lekcja \\u017cycia."
      ],
      "created_at":"2016-03-27T07:29:57+00:00",
      "nsfw":true
    },
    {
      "id":"a34b3ce1-07ea-4bf6-8c41-59403533fba2",
      "text":[
        "Nepotyzm w sp\\u00f3\\u0142kach pa\\u0144stwowych."
      ],
      "created_at":"2016-03-27T07:17:26+00:00",
      "nsfw":true
    },
    {
      "id":"a3e66cec-e43f-4962-b2a3-3c834143e95e",
      "text":[
        "Nie\\u015bmieszny kawa\\u0142."
      ],
      "created_at":"2016-03-26T22:47:13+00:00",
      "nsfw":true
    },
    {
      "id":"a4bd1884-1d21-4279-88b6-4ee3305d0f38",
      "text":[
        "Seba chuj."
      ],
      "created_at":"2016-03-27T07:32:50+00:00",
      "nsfw":true
    },
    {
      "id":"a61d0984-2c00-40c6-8960-0e1b5ad3cadd",
      "text":[
        "Gole\\u0144."
      ],
      "created_at":"2016-03-26T22:24:26+00:00",
      "nsfw":true
    },
    {
      "id":"a65de37b-cc60-4158-a062-853112f42201",
      "text":[
        "Panienka z okienka."
      ],
      "created_at":"2016-03-26T23:59:27+00:00",
      "nsfw":true
    },
    {
      "id":"a7c889b9-91dd-4e8f-9c71-476d61141f1e",
      "text":[
        "Antoni Macierewicz."
      ],
      "created_at":"2016-03-26T22:20:58+00:00",
      "nsfw":true
    },
    {
      "id":"a908f8db-098f-411a-8757-3e751c135636",
      "text":[
        "Wychudzona szkapa."
      ],
      "created_at":"2016-05-16T17:14:03+00:00",
      "nsfw":true
    },
    {
      "id":"a94e434f-46a3-4495-a457-ed0ea9ff3083",
      "text":[
        "Opalony Kamil."
      ],
      "created_at":"2016-03-27T00:06:16+00:00",
      "nsfw":true
    },
    {
      "id":"a984c0ce-8de8-49cd-b9d6-dda7895c8e8e",
      "text":[
        "Juliusz S\\u0142owacki."
      ],
      "created_at":"2016-03-26T23:55:10+00:00",
      "nsfw":true
    },
    {
      "id":"a9f817f7-d43b-48ae-96c8-b73dec15b256",
      "text":[
        "Pr\\u0105cie Elektryczno\\u015bci."
      ],
      "created_at":"2016-03-27T00:10:42+00:00",
      "nsfw":true
    },
    {
      "id":"aa3fc7f1-b867-4329-b646-42fa6df8fb36",
      "text":[
        "Bunkier rozpaczy."
      ],
      "created_at":"2016-04-07T16:49:53+00:00",
      "nsfw":true
    },
    {
      "id":"aa7388e4-7600-40e3-807f-1da067da7714",
      "text":[
        "\\u017bydzi w piwnicy."
      ],
      "created_at":"2016-03-27T00:09:43+00:00",
      "nsfw":true
    },
    {
      "id":"aac1c3fc-7645-41ca-a579-a3210fcddbe9",
      "text":[
        "Przep\\u0142yw laminarny."
      ],
      "created_at":"2016-04-07T16:53:37+00:00",
      "nsfw":true
    },
    {
      "id":"aaf6d586-1cae-4467-9228-f2146bee0d25",
      "text":[
        "Ma\\u0142om\\u00f3wna niewiasta."
      ],
      "created_at":"2016-06-14T15:26:02+00:00",
      "nsfw":true
    },
    {
      "id":"ab3e7519-75bd-4dbd-b5fa-bd0672dc9dff",
      "text":[
        "Borsuk na uwi\\u0119zi."
      ],
      "created_at":"2016-04-07T16:51:35+00:00",
      "nsfw":true
    },
    {
      "id":"aba0ad78-ed7f-4d53-9b13-2f735a4709f3",
      "text":[
        "S\\u0105d Ostateczny."
      ],
      "created_at":"2016-03-27T07:24:35+00:00",
      "nsfw":true
    },
    {
      "id":"abfa0d9c-d793-448b-8b1b-d42b760d7afd",
      "text":[
        "Ambaras."
      ],
      "created_at":"2016-03-26T22:49:30+00:00",
      "nsfw":true
    },
    {
      "id":"ac8cfae7-23a4-428a-aabe-bbeb11ffeac3",
      "text":[
        "Dupa."
      ],
      "created_at":"2016-03-26T22:21:55+00:00",
      "nsfw":true
    },
    {
      "id":"ada059a6-9cee-4b0c-9193-62e78616b19d",
      "text":[
        "Nie p\\u00f3jd\\u0119 w \\u017cadnym."
      ],
      "created_at":"2016-10-10T21:21:15+00:00",
      "nsfw":true
    },
    {
      "id":"adaf4fad-db02-4761-af7c-f1708e450467",
      "text":[
        "Wyprawa Krzy\\u017cowa."
      ],
      "created_at":"2016-06-14T15:05:18+00:00",
      "nsfw":true
    },
    {
      "id":"adb944d1-52cc-4e16-b0a4-d26743ee6f35",
      "text":[
        "Po\\u017coga zag\\u0142ady."
      ],
      "created_at":"2016-03-26T22:40:23+00:00",
      "nsfw":true
    },
    {
      "id":"ae0fda02-ab93-48fc-a441-1e1608794c97",
      "text":[
        "Lew z cia\\u0142em go\\u0142\\u0119bia i g\\u0142ow\\u0105 go\\u0142\\u0119bia."
      ],
      "created_at":"2016-04-07T16:50:43+00:00",
      "nsfw":true
    },
    {
      "id":"aedfb155-ef60-41f7-922d-ca8bcf2b074a",
      "text":[
        "Ostatni posi\\u0142ek."
      ],
      "created_at":"2016-03-27T00:12:10+00:00",
      "nsfw":true
    },
    {
      "id":"b0bda353-3ae9-41ed-bbbc-e5f3c74ae386",
      "text":[
        "Z\\u0142ocisty deszcz."
      ],
      "created_at":"2016-03-27T07:13:35+00:00",
      "nsfw":true
    },
    {
      "id":"b0f90601-dfa2-401b-9784-e2a4761456c2",
      "text":[
        "Stare sterowniki."
      ],
      "created_at":"2016-03-26T23:58:49+00:00",
      "nsfw":true
    },
    {
      "id":"b136f161-e8bb-4729-bbfd-f0e9976343bc",
      "text":[
        "Podgl\\u0105danie rodzic\\u00f3w."
      ],
      "created_at":"2016-05-16T17:36:14+00:00",
      "nsfw":true
    },
    {
      "id":"b1719217-ebb4-45d6-81a8-f862c77313ee",
      "text":[
        "Dziki w lesie."
      ],
      "created_at":"2016-03-26T22:35:12+00:00",
      "nsfw":true
    },
    {
      "id":"b17f18a6-a284-4a43-9c33-8a73a0b30f60",
      "text":[
        "Delikatesy."
      ],
      "created_at":"2016-03-26T22:51:35+00:00",
      "nsfw":true
    },
    {
      "id":"b256407a-6b2f-4749-b256-f599bfbdafa9",
      "text":[
        "Sprzedam Opla."
      ],
      "created_at":"2016-06-14T15:17:06+00:00",
      "nsfw":true
    },
    {
      "id":"b2d575b0-9064-4332-8080-bea61cf59343",
      "text":[
        "M\\u00f3j dom."
      ],
      "created_at":"2016-03-26T22:59:23+00:00",
      "nsfw":true
    },
    {
      "id":"b3452396-0e52-4a80-8608-6cb103ad4db7",
      "text":[
        "Przek\\u0142adnia falowa."
      ],
      "created_at":"2016-03-26T22:30:59+00:00",
      "nsfw":true
    },
    {
      "id":"b3b09ddd-8480-45d4-acfc-c0b77487ef58",
      "text":[
        "Pan B\\u00f3g."
      ],
      "created_at":"2016-03-27T00:01:49+00:00",
      "nsfw":true
    },
    {
      "id":"b48401ad-05ac-48fe-bd86-22295284a4b0",
      "text":[
        "Anoda."
      ],
      "created_at":"2016-03-26T22:40:30+00:00",
      "nsfw":true
    },
    {
      "id":"b4ec28da-ff60-4531-b04b-dcffaeacd53a",
      "text":[
        "Zwyk\\u0142a wiertarka."
      ],
      "created_at":"2016-03-26T22:37:50+00:00",
      "nsfw":true
    },
    {
      "id":"b514825c-14b9-4168-8a43-866a41172299",
      "text":[
        "Bolec w uszach."
      ],
      "created_at":"2016-10-10T21:15:13+00:00",
      "nsfw":true
    },
    {
      "id":"b5282e43-2e03-4a31-8629-83ebb8e297d2",
      "text":[
        "Johny Anderson."
      ],
      "created_at":"2016-03-27T00:00:50+00:00",
      "nsfw":true
    },
    {
      "id":"b583964e-dd0d-4c27-8c6d-09029ce66d15",
      "text":[
        "Pantomima."
      ],
      "created_at":"2016-03-27T00:00:16+00:00",
      "nsfw":true
    },
    {
      "id":"b613de33-84a1-40f2-8923-9c3ab633444d",
      "text":[
        "G\\u0142upi cham."
      ],
      "created_at":"2016-03-26T23:55:03+00:00",
      "nsfw":true
    },
    {
      "id":"b649c7ac-8a0e-4109-8860-9c01975e76c7",
      "text":[
        "Pumpcia."
      ],
      "created_at":"2017-08-13T00:09:12+00:00",
      "nsfw":true
    },
    {
      "id":"b64fea17-2f4f-4633-bafa-5afde95ff493",
      "text":[
        "Statek matka."
      ],
      "created_at":"2016-04-07T16:51:58+00:00",
      "nsfw":true
    },
    {
      "id":"b6ea6028-c557-476c-b85f-0b4e816f98d1",
      "text":[
        "Na\\u0107pana \\u0142ania."
      ],
      "created_at":"2016-05-16T17:31:33+00:00",
      "nsfw":true
    },
    {
      "id":"b9f95f1b-4ffc-41bd-88c9-a23fc83c0a83",
      "text":[
        "Hipoteza Hubera \\u2013 Misesa- Hencky\\u2019ego."
      ],
      "created_at":"2016-03-27T07:22:42+00:00",
      "nsfw":true
    },
    {
      "id":"bae85f80-075e-4b92-807d-c900f5746e09",
      "text":[
        "Pocenie si\\u0119 krwi\\u0105."
      ],
      "created_at":"2016-03-27T00:12:54+00:00",
      "nsfw":true
    },
    {
      "id":"bb6bca88-b416-48a0-b87b-80da662d01b2",
      "text":[
        "Zew godowy warchlak."
      ],
      "created_at":"2016-03-27T00:14:20+00:00",
      "nsfw":true
    },
    {
      "id":"bbed4214-958b-4c1f-9ff8-e218f206a7b5",
      "text":[
        "Detektyw z lup\\u0105 na czole."
      ],
      "created_at":"2016-03-26T23:45:52+00:00",
      "nsfw":true
    },
    {
      "id":"bc442e22-c51e-4c1a-a8a0-3e92dff480ac",
      "text":[
        "Papie\\u017c Benedykt XVI."
      ],
      "created_at":"2016-03-26T23:00:12+00:00",
      "nsfw":true
    },
    {
      "id":"bcd19074-16ee-4bf5-82a8-714a6aa7feea",
      "text":[
        "D\\u0142ugi u matki."
      ],
      "created_at":"2016-03-26T23:57:26+00:00",
      "nsfw":true
    },
    {
      "id":"bcdd0699-4061-4520-b0d6-6efc5654f51a",
      "text":[
        "Damian."
      ],
      "created_at":"2016-03-26T22:20:11+00:00",
      "nsfw":true
    },
    {
      "id":"bdf42161-f133-470a-8870-4b1b15b039ed",
      "text":[
        "\\u0141ono."
      ],
      "created_at":"2016-03-26T22:31:45+00:00",
      "nsfw":true
    },
    {
      "id":"be8aa7e9-082b-4049-819a-1472dcc81eb3",
      "text":[
        "Reakcja na wpierdol."
      ],
      "created_at":"2016-03-27T07:17:14+00:00",
      "nsfw":true
    },
    {
      "id":"bea0f115-8df7-43f8-a6ef-edd8b5573032",
      "text":[
        "Krwawa orgia."
      ],
      "created_at":"2016-05-16T17:28:11+00:00",
      "nsfw":true
    },
    {
      "id":"bf04257a-5234-4700-9c13-af095b19ab1a",
      "text":[
        "Rezolutny Micha\\u0142."
      ],
      "created_at":"2016-03-27T07:14:56+00:00",
      "nsfw":true
    },
    {
      "id":"c00baa4d-aac4-4429-8b4c-83e0940eb420",
      "text":[
        "Przesta\\u0107 ju\\u017c pierdoli\\u0107!"
      ],
      "created_at":"2016-03-26T22:49:15+00:00",
      "nsfw":true
    },
    {
      "id":"c0a237a8-1959-4089-af36-84e57fe14eea",
      "text":[
        "Kazamaty Nienawi\\u015bci."
      ],
      "created_at":"2016-10-10T21:15:01+00:00",
      "nsfw":true
    },
    {
      "id":"c0a84ca9-d9bf-4fb8-a8fe-ff537a804e39",
      "text":[
        "Dwie \\u015blepe dziwki."
      ],
      "created_at":"2016-03-26T22:55:48+00:00",
      "nsfw":true
    },
    {
      "id":"c18d4b0f-fe5e-4654-8132-55cf4b0f69d9",
      "text":[
        "Kamie\\u0144."
      ],
      "created_at":"2016-03-26T22:20:51+00:00",
      "nsfw":true
    },
    {
      "id":"c1a10806-6718-492f-96f6-6927859a66f0",
      "text":[
        "Babajaga w naturalnym \\u015brodowisku."
      ],
      "created_at":"2016-10-10T21:18:29+00:00",
      "nsfw":true
    },
    {
      "id":"c23e87f1-d267-4bee-af3b-e80ec3263d29",
      "text":[
        "Rudy murzyn."
      ],
      "created_at":"2016-03-26T22:59:59+00:00",
      "nsfw":true
    },
    {
      "id":"c2666a9c-f731-4e77-a9f0-bb5acc5b17e7",
      "text":[
        "Matematyczna zagwozdka."
      ],
      "created_at":"2016-03-26T22:32:07+00:00",
      "nsfw":true
    },
    {
      "id":"c2e24ecd-5d2d-452d-88dd-37ffefd04323",
      "text":[
        "4 lata."
      ],
      "created_at":"2016-06-14T15:22:34+00:00",
      "nsfw":true
    },
    {
      "id":"c347897e-615d-4ac9-ac4e-09fdd4fde79c",
      "text":[
        "Kradn\\u0105cy kwiaty z cmentarzy cyganie."
      ],
      "created_at":"2016-03-26T23:01:08+00:00",
      "nsfw":true
    },
    {
      "id":"c47d2c4e-87a6-4d7b-9147-5dcc432f0536",
      "text":[
        "GOOOLLLL!!!"
      ],
      "created_at":"2016-06-14T15:22:52+00:00",
      "nsfw":true
    },
    {
      "id":"c481d90f-6603-4307-9366-36d91e1d4b8a",
      "text":[
        "Piotr \\u0142otr."
      ],
      "created_at":"2016-05-16T17:25:42+00:00",
      "nsfw":true
    },
    {
      "id":"c57775ad-112c-4c2f-acb4-ceb4fd733521",
      "text":[
        "Frank Gehry"
      ],
      "created_at":"2016-03-27T07:16:35+00:00",
      "nsfw":true
    },
    {
      "id":"c60b5c9b-c91a-4478-9013-6db6181d1fdb",
      "text":[
        "Rachowanie."
      ],
      "created_at":"2016-03-27T00:17:22+00:00",
      "nsfw":true
    },
    {
      "id":"c68b9591-d4b0-43b6-b3a3-5fb353e7a751",
      "text":[
        "Linia Curzona."
      ],
      "created_at":"2016-03-27T07:25:02+00:00",
      "nsfw":true
    },
    {
      "id":"c6bdcbbe-ad4f-4062-a35b-4aea79885e09",
      "text":[
        "Wszystkie kurwa choroby \\u015bwiata."
      ],
      "created_at":"2016-07-05T21:37:33+00:00",
      "nsfw":true
    },
    {
      "id":"c70bbfe6-548f-4323-81ed-891e317dac47",
      "text":[
        "Zatarg z s\\u0105siadem."
      ],
      "created_at":"2016-06-14T15:04:10+00:00",
      "nsfw":true
    },
    {
      "id":"c7a41e38-182b-405b-bc9c-6f0421b3307f",
      "text":[
        "Na ziemi\\u0119!"
      ],
      "created_at":"2016-06-14T15:23:56+00:00",
      "nsfw":true
    },
    {
      "id":"c7fad884-f310-4789-ae39-3bcf962e7bdb",
      "text":[
        "Bekanie pod nadzorem."
      ],
      "created_at":"2016-10-10T21:50:35+00:00",
      "nsfw":true
    },
    {
      "id":"c8462f05-f22d-4441-84eb-957871dfc1b6",
      "text":[
        "Idealny ty\\u0142eczek."
      ],
      "created_at":"2016-05-16T17:17:26+00:00",
      "nsfw":true
    },
    {
      "id":"c8a099a5-78cc-4825-a71b-30272f81aac4",
      "text":[
        "Ba\\u0142agan w pokoju."
      ],
      "created_at":"2016-10-10T21:20:06+00:00",
      "nsfw":true
    },
    {
      "id":"c8ceb1bb-cddc-4047-8541-0cf6431e864a",
      "text":[
        "Szparka Arka."
      ],
      "created_at":"2016-03-26T23:01:48+00:00",
      "nsfw":true
    },
    {
      "id":"c92dc020-d6f6-4e55-958a-2ab9a5ffa10a",
      "text":[
        "Kochanie si\\u0119."
      ],
      "created_at":"2016-03-27T00:06:24+00:00",
      "nsfw":true
    },
    {
      "id":"ca060f65-450d-4e58-bff4-4c035282c36d",
      "text":[
        "Nak\\u0142adanie g\\u0142adzi."
      ],
      "created_at":"2016-03-27T00:08:45+00:00",
      "nsfw":true
    },
    {
      "id":"cb6df083-a4fc-4ad0-8fbd-b7f911ef0dc9",
      "text":[
        "Modu\\u0142 Younga."
      ],
      "created_at":"2016-04-07T16:55:28+00:00",
      "nsfw":true
    },
    {
      "id":"cb83d99e-b381-4fb1-a0f3-219b270858d7",
      "text":[
        "Karmnik dla ptak\\u00f3w."
      ],
      "created_at":"2016-03-26T22:35:20+00:00",
      "nsfw":true
    },
    {
      "id":"cbab44f9-8227-41d0-9e38-b7f1a04f3f52",
      "text":[
        "Niemowlaczek."
      ],
      "created_at":"2016-03-27T00:17:43+00:00",
      "nsfw":true
    },
    {
      "id":"cbf6711d-ce3a-4fdc-b81e-04264ecff58b",
      "text":[
        "W chuj wielkie kule."
      ],
      "created_at":"2016-07-05T21:56:26+00:00",
      "nsfw":true
    },
    {
      "id":"cc260b2e-3106-43f9-b8db-448294c92429",
      "text":[
        "Kapcie po tacie."
      ],
      "created_at":"2016-03-27T00:03:56+00:00",
      "nsfw":true
    },
    {
      "id":"cc5c9156-af48-4841-9472-cde2eeb79ae0",
      "text":[
        "G\\u0119sty las li\\u015bciasty."
      ],
      "created_at":"2016-05-16T17:22:13+00:00",
      "nsfw":true
    },
    {
      "id":"ccb0e00f-e636-4ac9-b0d8-599991bb5849",
      "text":[
        "Kolaboracja."
      ],
      "created_at":"2016-03-26T22:34:48+00:00",
      "nsfw":true
    },
    {
      "id":"cd553ff8-863b-41d3-8aea-bc6c5f14723a",
      "text":[
        "Problem z Chinami."
      ],
      "created_at":"2016-05-16T17:33:12+00:00",
      "nsfw":true
    },
    {
      "id":"cdd1b043-9f98-4616-841c-679ac0477ddb",
      "text":[
        "Lech Wa\\u0142\\u0119sa."
      ],
      "created_at":"2016-03-26T22:21:31+00:00",
      "nsfw":true
    },
    {
      "id":"ce85d5d2-6ba3-49b3-bf81-406fcc7d48ed",
      "text":[
        "Oj, Anno."
      ],
      "created_at":"2016-03-26T22:35:05+00:00",
      "nsfw":true
    },
    {
      "id":"ceaa952b-bd37-49f5-8ffd-00add3f164c7",
      "text":[
        "Kolekcja z\\u0119b\\u00f3w pokonanych wrog\\u00f3w."
      ],
      "created_at":"2016-10-10T21:04:01+00:00",
      "nsfw":true
    },
    {
      "id":"cfba7a03-6fb6-4472-b7e3-3cd031cbfe4e",
      "text":[
        "No po prostu delicje!"
      ],
      "created_at":"2016-03-26T22:47:44+00:00",
      "nsfw":true
    },
    {
      "id":"cfec0512-11c3-43bd-8db0-9a93f877d76e",
      "text":[
        "We\\u017a spierdalaj..."
      ],
      "created_at":"2016-03-27T00:11:06+00:00",
      "nsfw":true
    },
    {
      "id":"cfef9485-c09e-4fbe-87ea-08b9edabcd4b",
      "text":[
        "Perpetuum mobile."
      ],
      "created_at":"2016-03-26T22:49:55+00:00",
      "nsfw":true
    },
    {
      "id":"d0426815-f0c0-4386-aac5-5ef8ad07e21d",
      "text":[
        "Kwadratowa Anna."
      ],
      "created_at":"2016-03-26T22:42:02+00:00",
      "nsfw":true
    },
    {
      "id":"d0ba8872-6e74-4f6c-8ec7-396b79a663da",
      "text":[
        "Fenomenologia Husserla."
      ],
      "created_at":"2016-03-27T07:19:07+00:00",
      "nsfw":true
    },
    {
      "id":"d104e3cf-0459-4b91-a9a0-9bc30b3026b2",
      "text":[
        "Guziec kurwa z Afryki."
      ],
      "created_at":"2016-04-18T23:25:21+00:00",
      "nsfw":true
    },
    {
      "id":"d261645f-6122-41d4-881c-8266ff3eee7d",
      "text":[
        "Zawa\\u0142 kolana."
      ],
      "created_at":"2016-03-27T00:14:42+00:00",
      "nsfw":true
    },
    {
      "id":"d2d98d13-87a6-4b03-bbb0-63cd220098fb",
      "text":[
        "Narastaj\\u0105ce napi\\u0119cie."
      ],
      "created_at":"2016-10-10T21:13:48+00:00",
      "nsfw":true
    },
    {
      "id":"d302b7d1-5c45-4b63-b1c5-254a58f9b7f3",
      "text":[
        "Utalentowana kaczka."
      ],
      "created_at":"2016-05-16T17:33:36+00:00",
      "nsfw":true
    },
    {
      "id":"d382c29e-4713-455f-9e11-3f28ba2bd269",
      "text":[
        "3,14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 06286 20899 86280 34825 34211 70679 82148 08651 32823 06647 09384 46095 50582 23172 53594 08128 48111 74502 84102 70193 85211 05559 64462 29489 54930"
      ],
      "created_at":"2016-03-27T07:31:09+00:00",
      "nsfw":true
    },
    {
      "id":"d3d14505-6b4e-40b9-96da-f8fbc789a2e5",
      "text":[
        "Ma\\u0142e kanie."
      ],
      "created_at":"2016-10-10T21:14:21+00:00",
      "nsfw":true
    },
    {
      "id":"d4452ec2-78ed-4479-97af-25dc846acac7",
      "text":[
        "Babranie si\\u0119 w g\\u00f3wnie."
      ],
      "created_at":"2016-03-27T00:08:02+00:00",
      "nsfw":true
    },
    {
      "id":"d479e402-70a1-4334-8544-2aa0cdd63a0e",
      "text":[
        "Monstrualne g\\u00f3wno."
      ],
      "created_at":"2016-03-26T23:00:46+00:00",
      "nsfw":true
    },
    {
      "id":"d49ce860-7d75-4691-a347-ce6eea242945",
      "text":[
        "Murzyn Marcin."
      ],
      "created_at":"2016-03-26T22:29:41+00:00",
      "nsfw":true
    },
    {
      "id":"d4bba18c-fcf7-452e-884a-481336bcafee",
      "text":[
        "Marek \\u0141owca Szparek."
      ],
      "created_at":"2016-03-27T07:15:09+00:00",
      "nsfw":true
    },
    {
      "id":"d59d8556-5457-4c1e-aef7-2dae29c2b12f",
      "text":[
        "Padanie na ryj."
      ],
      "created_at":"2016-03-26T23:55:31+00:00",
      "nsfw":true
    },
    {
      "id":"d6e3ca07-cc4f-4d0f-9b19-79ca87a8f765",
      "text":[
        "Perfidne pedalstwo."
      ],
      "created_at":"2016-05-16T17:31:56+00:00",
      "nsfw":true
    },
    {
      "id":"d7845b9e-7fba-4399-aa14-c4ee4d384017",
      "text":[
        "Ale akcja!"
      ],
      "created_at":"2016-03-27T00:14:55+00:00",
      "nsfw":true
    },
    {
      "id":"d7c70237-4af6-4677-8aea-46362b801b9d",
      "text":[
        "Cie\\u0107wierz."
      ],
      "created_at":"2016-03-26T23:59:21+00:00",
      "nsfw":true
    },
    {
      "id":"d8048211-05e6-401e-9ce1-7553c86f00a9",
      "text":[
        "Niemyty chuj."
      ],
      "created_at":"2016-03-26T23:54:47+00:00",
      "nsfw":true
    },
    {
      "id":"d979bf21-d75f-4cb1-a78e-60efba3e6137",
      "text":[
        "Flaczki u rodziny."
      ],
      "created_at":"2016-05-16T17:29:15+00:00",
      "nsfw":true
    },
    {
      "id":"da878fdc-6f08-42e4-97ad-2b3527dd6547",
      "text":[
        "Pingwin w d\\u017cungli."
      ],
      "created_at":"2016-03-27T07:18:18+00:00",
      "nsfw":true
    },
    {
      "id":"da9da27c-844c-4157-85b4-3c7dd196dca6",
      "text":[
        "Rycerz Kamil."
      ],
      "created_at":"2016-03-26T23:46:33+00:00",
      "nsfw":true
    },
    {
      "id":"dadf3493-0c5c-483c-bb3a-91bcc784ee0e",
      "text":[
        "Matecznik."
      ],
      "created_at":"2016-03-26T23:59:14+00:00",
      "nsfw":true
    },
    {
      "id":"db7c7cf8-6ed4-4404-ae5a-c486682768c7",
      "text":[
        "Okradanie grob\\u00f3w."
      ],
      "created_at":"2016-03-26T22:56:19+00:00",
      "nsfw":true
    },
    {
      "id":"db875986-83b2-4d60-abe2-f5bc2ac6c15d",
      "text":[
        "Czarna dupa."
      ],
      "created_at":"2016-03-27T00:15:57+00:00",
      "nsfw":true
    },
    {
      "id":"dc2aa41c-7be9-462a-be87-8fafaaf01dac",
      "text":[
        "W\\u0142osy na pi\\u0119tach."
      ],
      "created_at":"2016-03-26T23:44:06+00:00",
      "nsfw":true
    },
    {
      "id":"dd0f89ed-3d1d-4491-945a-867285d035f5",
      "text":[
        "\\u015alinienie si\\u0119."
      ],
      "created_at":"2016-03-26T23:56:25+00:00",
      "nsfw":true
    },
    {
      "id":"dd573731-2462-4a71-a93d-37c9d250da0c",
      "text":[
        "Jacek Soplica."
      ],
      "created_at":"2016-03-26T22:52:31+00:00",
      "nsfw":true
    },
    {
      "id":"de023c8f-3d61-464f-91ab-e370acb2670b",
      "text":[
        "Prosty banan."
      ],
      "created_at":"2016-03-27T00:11:32+00:00",
      "nsfw":true
    },
    {
      "id":"de1ddd3e-d96b-4209-9699-5ac09301a639",
      "text":[
        "Nie."
      ],
      "created_at":"2016-03-26T23:43:15+00:00",
      "nsfw":true
    },
    {
      "id":"de9d38a0-5140-4144-b2ca-423beaffd494",
      "text":[
        "Chodzi\\u0107 g\\u0119siego."
      ],
      "created_at":"2016-04-07T16:48:56+00:00",
      "nsfw":true
    },
    {
      "id":"decdaf67-6edf-4c34-8ab3-263f1328b68b",
      "text":[
        "Jaros\\u0142aw Kaczy\\u0144ski."
      ],
      "created_at":"2016-03-26T22:21:12+00:00",
      "nsfw":true
    },
    {
      "id":"deea3664-2f72-453f-8dd3-05dff1a5c912",
      "text":[
        "Supersi\\u0142a."
      ],
      "created_at":"2016-04-12T12:59:41+00:00",
      "nsfw":true
    },
    {
      "id":"df77f223-60c6-4ee4-8040-f3b0d73191a9",
      "text":[
        "Z\\u0142odziej na targu."
      ],
      "created_at":"2016-05-16T17:32:28+00:00",
      "nsfw":true
    },
    {
      "id":"e05039d7-b936-4616-84b3-6c7def38460f",
      "text":[
        "Strata matki."
      ],
      "created_at":"2016-04-07T16:49:37+00:00",
      "nsfw":true
    },
    {
      "id":"e18c715b-9af5-48dc-a68e-cbafb3d9cec1",
      "text":[
        "Grzech ci\\u0119\\u017cki."
      ],
      "created_at":"2016-06-14T15:11:40+00:00",
      "nsfw":true
    },
    {
      "id":"e207a42e-f2f7-4970-afab-c63c38f2953b",
      "text":[
        "Nawet o tym nie my\\u015bl."
      ],
      "created_at":"2016-03-27T07:17:57+00:00",
      "nsfw":true
    },
    {
      "id":"e2641360-2948-4578-9fa7-2a19a973ebc3",
      "text":[
        "Bia\\u0142a dupa."
      ],
      "created_at":"2016-03-27T00:15:52+00:00",
      "nsfw":true
    },
    {
      "id":"e286d441-04c9-48fe-9cb0-42cf806b7a1f",
      "text":[
        "Papa Smerf."
      ],
      "created_at":"2016-05-16T17:19:28+00:00",
      "nsfw":true
    },
    {
      "id":"e37f6f64-eeef-4a72-8ffa-2c0809d76186",
      "text":[
        "Dioda."
      ],
      "created_at":"2016-03-26T23:48:51+00:00",
      "nsfw":true
    },
    {
      "id":"e423ae7c-06d1-42fe-b2d0-2c263bc02451",
      "text":[
        "Branie do buzi."
      ],
      "created_at":"2016-03-27T00:06:30+00:00",
      "nsfw":true
    },
    {
      "id":"e50c081d-e9e7-4090-8569-73b0fa089f0d",
      "text":[
        "Katoda."
      ],
      "created_at":"2016-03-26T22:40:26+00:00",
      "nsfw":true
    },
    {
      "id":"e72415e4-3ca7-4dd9-9100-e683837fd24a",
      "text":[
        "Pierwsza godzina gratis."
      ],
      "created_at":"2016-03-26T22:51:55+00:00",
      "nsfw":true
    },
    {
      "id":"e7302216-f952-444c-8fda-037c3cc399ea",
      "text":[
        "Mo\\u017cesz?"
      ],
      "created_at":"2016-03-27T00:11:10+00:00",
      "nsfw":true
    },
    {
      "id":"e75fee6d-0bb8-40c9-93d3-57dc3c0f5b96",
      "text":[
        "6 aborcji."
      ],
      "created_at":"2016-03-27T15:13:22+00:00",
      "nsfw":true
    },
    {
      "id":"e772bcc8-8e33-4909-a0e4-73e31ecba18f",
      "text":[
        "Kaszlenie krwi\\u0105."
      ],
      "created_at":"2016-03-27T00:07:45+00:00",
      "nsfw":true
    },
    {
      "id":"e795f5d1-9148-40ca-8511-b73efa41ef5a",
      "text":[
        "Riki tiki."
      ],
      "created_at":"2016-03-27T00:04:05+00:00",
      "nsfw":true
    },
    {
      "id":"e8610059-4d23-4836-be8c-eb169f290a16",
      "text":[
        "Komandor Alojzy."
      ],
      "created_at":"2016-03-26T22:52:26+00:00",
      "nsfw":true
    },
    {
      "id":"e8e26276-2e6b-4ebf-804d-c303f9122b17",
      "text":[
        "S\\u0142odziutki kocyk."
      ],
      "created_at":"2016-03-27T14:56:15+00:00",
      "nsfw":true
    },
    {
      "id":"e9653261-7c57-4a40-849c-ccdcf9341ddf",
      "text":[
        "Panda."
      ],
      "created_at":"2016-10-10T21:03:38+00:00",
      "nsfw":true
    },
    {
      "id":"e99344c4-b7d9-4b1f-848a-7b23a3478970",
      "text":[
        "Rachunek prawdopodobie\\u0144stwa."
      ],
      "created_at":"2016-03-27T07:29:31+00:00",
      "nsfw":true
    },
    {
      "id":"ea5cf53e-4700-431d-95ba-fb45fbf0d62b",
      "text":[
        "Glizda ludzka."
      ],
      "created_at":"2016-03-26T22:35:26+00:00",
      "nsfw":true
    },
    {
      "id":"ea9d63bb-1788-4365-b8d1-2eff40d9fb74",
      "text":[
        "Jod\\u0142owanie."
      ],
      "created_at":"2016-03-27T00:00:23+00:00",
      "nsfw":true
    },
    {
      "id":"eab43b30-abef-4b60-b73d-c462f4d5b536",
      "text":[
        "Mam 3 garnitury."
      ],
      "created_at":"2016-10-10T21:21:02+00:00",
      "nsfw":true
    },
    {
      "id":"eac87bfd-fa59-4554-a028-99058890efa0",
      "text":[
        "Kana\\u0142y pod Wiedniem."
      ],
      "created_at":"2016-05-16T17:36:52+00:00",
      "nsfw":true
    },
    {
      "id":"eb0d6a76-8466-4a6b-8a1a-9652f489245d",
      "text":[
        "Nieust\\u0119powanie miejsca starszym."
      ],
      "created_at":"2016-03-27T00:08:35+00:00",
      "nsfw":true
    },
    {
      "id":"eb4efedb-88f7-4fe5-a30e-e8ceafec0624",
      "text":[
        "T\\u0142umik samochodowy."
      ],
      "created_at":"2016-04-07T16:52:24+00:00",
      "nsfw":true
    },
    {
      "id":"ec8148bf-ada0-4f3b-acdf-e86611ac18bf",
      "text":[
        "Andrzej."
      ],
      "created_at":"2016-03-26T22:19:08+00:00",
      "nsfw":true
    },
    {
      "id":"ecaf4f66-cddb-41e7-8eb3-52f26450dccd",
      "text":[
        "\\u017bbik na wakacjach."
      ],
      "created_at":"2016-06-14T15:14:13+00:00",
      "nsfw":true
    },
    {
      "id":"ed336426-9620-4354-bd98-99b229e6fa36",
      "text":[
        "Zbawiciel."
      ],
      "created_at":"2016-03-27T00:01:45+00:00",
      "nsfw":true
    },
    {
      "id":"ee7d36e1-b7ce-4feb-b306-d04a18e5d04e",
      "text":[
        "Ty wieprzu!"
      ],
      "created_at":"2016-06-14T15:24:58+00:00",
      "nsfw":true
    },
    {
      "id":"eef34784-18fa-4ce8-a1dd-af9e7c98dc40",
      "text":[
        "Gwint drobnozwojny."
      ],
      "created_at":"2016-03-26T22:30:53+00:00",
      "nsfw":true
    },
    {
      "id":"ef8ba3bc-ba5f-447a-bc89-7bd08e52c618",
      "text":[
        "Pomidorowa mamy."
      ],
      "created_at":"2016-05-16T17:29:27+00:00",
      "nsfw":true
    },
    {
      "id":"ef8dbe2b-0847-46aa-b128-4c2829110ff7",
      "text":[
        "Atencyjna dziwka."
      ],
      "created_at":"2016-03-26T22:32:43+00:00",
      "nsfw":true
    },
    {
      "id":"effb1e53-811c-4ba6-877f-ba2057652203",
      "text":[
        "\\u0141awica \\u015bledzi."
      ],
      "created_at":"2016-03-27T00:10:08+00:00",
      "nsfw":true
    },
    {
      "id":"f0e12683-a6be-4edc-a2f3-470b78f9f307",
      "text":[
        "R\\u00f3\\u017cd\\u017cka z kamienia."
      ],
      "created_at":"2016-03-27T00:12:24+00:00",
      "nsfw":true
    },
    {
      "id":"f16e903e-2c71-4bd3-b2eb-080e0dd9d1f4",
      "text":[
        "Iloczyn rozpuszczalno\\u015bci."
      ],
      "created_at":"2016-03-27T07:21:17+00:00",
      "nsfw":true
    },
    {
      "id":"f1a2507c-ff78-4c34-a4bd-ece76461832f",
      "text":[
        "Matematyczny pierdolnik."
      ],
      "created_at":"2016-03-26T22:46:31+00:00",
      "nsfw":true
    },
    {
      "id":"f2b8a6a9-b420-4329-8bdd-1c8b1c1cfd33",
      "text":[
        "Podpalanie."
      ],
      "created_at":"2016-03-27T00:06:54+00:00",
      "nsfw":true
    },
    {
      "id":"f3260989-7e69-4858-ab8e-4e7019b92f78",
      "text":[
        "Go\\u0142a baba."
      ],
      "created_at":"2016-03-27T00:08:59+00:00",
      "nsfw":true
    },
    {
      "id":"f32d68c7-3d00-4d93-b18b-1abcd267b11e",
      "text":[
        "Pogrzeb dziecka."
      ],
      "created_at":"2016-03-27T15:13:00+00:00",
      "nsfw":true
    },
    {
      "id":"f333d16b-3645-420e-858d-4b6bcdcb7193",
      "text":[
        "Siusiaczek."
      ],
      "created_at":"2016-03-26T22:26:31+00:00",
      "nsfw":true
    },
    {
      "id":"f37640fc-f3d0-42d8-ad33-8d9a8ca552b8",
      "text":[
        "S\\u0142aba kondycja."
      ],
      "created_at":"2016-03-26T22:25:34+00:00",
      "nsfw":true
    },
    {
      "id":"f4644574-671b-49df-b4cb-518fce153147",
      "text":[
        "Cerber."
      ],
      "created_at":"2016-10-10T21:46:10+00:00",
      "nsfw":true
    },
    {
      "id":"f4892896-74b6-4502-bce1-7e469de0210e",
      "text":[
        "Dupsko."
      ],
      "created_at":"2016-03-26T23:54:01+00:00",
      "nsfw":true
    },
    {
      "id":"f48b0b6a-209b-4b2f-a0df-44d10a0b81ab",
      "text":[
        "Ca\\u0142ka oznaczona."
      ],
      "created_at":"2016-04-12T12:57:24+00:00",
      "nsfw":true
    },
    {
      "id":"f4c7a6a2-6b5b-4f0c-9df3-9c1c06407d91",
      "text":[
        "Maria Magdalena."
      ],
      "created_at":"2016-03-26T22:20:07+00:00",
      "nsfw":true
    },
    {
      "id":"f4dc60eb-6e56-47e7-b3eb-b3e54a16b8d7",
      "text":[
        "Serio, mamo?"
      ],
      "created_at":"2016-03-27T00:13:35+00:00",
      "nsfw":true
    },
    {
      "id":"f5771bc1-4641-4c8e-b91e-0b822843d00b",
      "text":[
        "Karmienie go\\u0142\\u0119bi."
      ],
      "created_at":"2016-04-07T16:49:07+00:00",
      "nsfw":true
    },
    {
      "id":"f5888afd-537f-4b99-abfd-181741ba8fe0",
      "text":[
        "Kapibara w zamku."
      ],
      "created_at":"2016-04-12T13:00:02+00:00",
      "nsfw":true
    },
    {
      "id":"f59497ed-d1f3-4d3b-b5c6-633d3186a817",
      "text":[
        "Sia\\u0142a baba mak."
      ],
      "created_at":"2016-03-27T00:16:18+00:00",
      "nsfw":true
    },
    {
      "id":"f5970beb-94ce-4e7a-a6a9-661dcb01e19c",
      "text":[
        "Krzywka mimo\\u015brodowa z popychaczem rolkowym."
      ],
      "created_at":"2016-03-26T23:50:00+00:00",
      "nsfw":true
    },
    {
      "id":"f7971ee4-ae9e-4fbe-86c4-40de9be1c2fa",
      "text":[
        "Szybko\\u015b\\u0107 czasu."
      ],
      "created_at":"2016-03-28T15:30:43+00:00",
      "nsfw":true
    },
    {
      "id":"f800b410-780a-4c4e-90e7-772a6f4e80b4",
      "text":[
        "Stosunek z koz\\u0105."
      ],
      "created_at":"2016-05-16T17:36:34+00:00",
      "nsfw":true
    },
    {
      "id":"f8102036-a217-4e6d-8a56-14d4341d4b79",
      "text":[
        "Dawanie na lewo i prawo."
      ],
      "created_at":"2016-03-28T15:29:15+00:00",
      "nsfw":true
    },
    {
      "id":"f85bade7-84c8-4f9a-b0b5-21365d98dadb",
      "text":[
        "Cichy zak\\u0105tek."
      ],
      "created_at":"2016-03-26T23:03:52+00:00",
      "nsfw":true
    },
    {
      "id":"f8616be0-d253-40bc-86d4-b25bdc3acc86",
      "text":[
        "P\\u0142\\u00f3d."
      ],
      "created_at":"2016-03-27T00:07:56+00:00",
      "nsfw":true
    },
    {
      "id":"fa5593a8-468d-4d8c-a847-b9cff593f5ca",
      "text":[
        "Halo! Halooooo!"
      ],
      "created_at":"2016-03-26T22:33:40+00:00",
      "nsfw":true
    },
    {
      "id":"fa5a685b-e091-4546-9d42-d5f589996747",
      "text":[
        "Nibylandia."
      ],
      "created_at":"2016-03-27T07:15:17+00:00",
      "nsfw":true
    },
    {
      "id":"fa5b3af6-42b0-4c27-9f04-87496fb13d45",
      "text":[
        "Szynka."
      ],
      "created_at":"2016-03-26T23:01:40+00:00",
      "nsfw":true
    },
    {
      "id":"fa894f2c-a7a9-43ee-aee8-22482249ca64",
      "text":[
        "Dawaj na longa!"
      ],
      "created_at":"2016-10-10T21:34:57+00:00",
      "nsfw":true
    },
    {
      "id":"fb1e3b0f-4e8a-4a6f-9d02-9f66c5a729bd",
      "text":[
        "Jebane poduszki."
      ],
      "created_at":"2016-03-27T00:14:26+00:00",
      "nsfw":true
    },
    {
      "id":"fb4e9f23-1af5-41e7-864c-021117fa7833",
      "text":[
        "Pole \\u015bledziowe."
      ],
      "created_at":"2016-03-27T07:13:18+00:00",
      "nsfw":true
    },
    {
      "id":"fc0e9528-b5de-4218-a9a3-ea9144bc6781",
      "text":[
        "Santiago Calatrava."
      ],
      "created_at":"2016-03-27T07:16:53+00:00",
      "nsfw":true
    },
    {
      "id":"fcf950bf-c781-4ac6-9b75-a64571058144",
      "text":[
        "Naprawd\\u0119 fajny kapelusz."
      ],
      "created_at":"2016-03-26T22:38:33+00:00",
      "nsfw":true
    },
    {
      "id":"fd9443f3-0fbe-4cc0-b1b5-7b20594ec05c",
      "text":[
        "Opalanie si\\u0119 na balkonie."
      ],
      "created_at":"2016-03-26T23:56:11+00:00",
      "nsfw":true
    },
    {
      "id":"fdea0e44-2082-49f5-acfe-3e944dd65b03",
      "text":[
        "Ma\\u0142y Ksi\\u0105\\u017c\\u0119."
      ],
      "created_at":"2016-04-07T16:51:14+00:00",
      "nsfw":true
    },
    {
      "id":"fdf3b510-48f7-44a9-bb53-2cc283bc36f6",
      "text":[
        "Magiczny Maciej."
      ],
      "created_at":"2016-03-26T23:01:32+00:00",
      "nsfw":true
    },
    {
      "id":"fe0a1267-672e-41d1-a212-39b2ec0ce546",
      "text":[
        "Wysyp cziter\\u00f3w."
      ],
      "created_at":"2016-04-28T18:32:02+00:00",
      "nsfw":true
    },
    {
      "id":"fe376687-cf5e-4f83-8cb0-5d47609398ef",
      "text":[
        "M\\u00f3j kurczak."
      ],
      "created_at":"2016-05-16T17:19:20+00:00",
      "nsfw":true
    },
    {
      "id":"fe417390-c29d-40e4-942c-645286b5b768",
      "text":[
        "Liczba stechiometryczna reakcji."
      ],
      "created_at":"2016-03-27T07:21:39+00:00",
      "nsfw":true
    },
    {
      "id":"fe677751-f2fa-42c1-a325-7151cb415bde",
      "text":[
        "Pot\\u0119\\u017cny mag ognia."
      ],
      "created_at":"2016-03-26T23:01:22+00:00",
      "nsfw":true
    },
    {
      "id":"fe6ae954-602c-4488-b7c0-6f1cbdce21e7",
      "text":[
        "Deszcz dreszcz."
      ],
      "created_at":"2016-03-26T22:43:13+00:00",
      "nsfw":true
    },
    {
      "id":"fed7c798-7f34-4453-be5b-a4bab3d5b29c",
      "text":[
        "Opel Astra."
      ],
      "created_at":"2016-05-16T17:15:29+00:00",
      "nsfw":true
    },
    {
      "id":"ffa541f8-b4c9-4de3-8953-959732637b08",
      "text":[
        "Antyczny kredens."
      ],
      "created_at":"2016-03-26T23:46:16+00:00",
      "nsfw":true
    },
    {
      "id":"266d971e-ef80-45b2-9204-143442a3277e",
      "text":[
        "Kot w pude\\u0142ku."
      ],
      "created_at":"2016-04-28T18:32:21+00:00",
      "nsfw":true
    },
    {
      "id":"5bd86a1e-ec1c-49e6-a041-ad97aecea79f",
      "text":[
        "Porno dla rudych."
      ],
      "created_at":"2016-03-26T23:45:02+00:00",
      "nsfw":true
    },
    {
      "id":"5d2b29e7-dfb9-480e-ad8e-72b81aa764ed",
      "text":[
        "Ryba, kt\\u00f3ry umar\\u0142 na zawa\\u0142 penisa."
      ],
      "created_at":"2016-03-26T23:00:28+00:00",
      "nsfw":true
    },
    {
      "id":"771e15b9-ed26-41b4-b40d-27bca432b0ed",
      "text":[
        "Zrobienie sobie kuku."
      ],
      "created_at":"2016-03-26T22:37:05+00:00",
      "nsfw":true
    },
    {
      "id":"89380a2d-3cf6-40a5-b106-38422581d675",
      "text":[
        "Jezus Chrystus."
      ],
      "created_at":"2016-03-27T00:02:29+00:00",
      "nsfw":true
    },
    {
      "id":"c97679c1-a137-4a8a-ad18-fdac1b8bcc68",
      "text":[
        "Penisylina."
      ],
      "created_at":"2016-03-26T23:00:56+00:00",
      "nsfw":true
    },
    {
      "id":"d78da89b-cad9-413e-9204-c1bcc6de0b8c",
      "text":[
        "Mycie si\\u0119 w sobot\\u0119."
      ],
      "created_at":"2016-03-26T23:55:55+00:00",
      "nsfw":true
    },
    {
      "id":"fb4b7a09-0264-4f67-a017-7f924fd457dd",
      "text":[
        "Kamper jebany!"
      ],
      "created_at":"2016-03-26T22:43:21+00:00",
      "nsfw":true
    }
  ]
}"""
_DEFAULT_CACHE = ''
_DEFAULT_CARDS_CACHE = """
            this.wcList = ["A bucket of fish heads.", "Silence.", "The unstoppable tide of Islam.", "Growing a pair.", "Famine.", "Flesh-eating bacteria.", "Flying sex snakes.", "Not giving a shit about the Third World.", "Magnets.", "Shapeshifters.", "Our first chimpanzee President.", "Crucifixion.", "72 virgins.", "A live studio audience.", "A time travel paradox.", "Authentic Mexican cuisine.", "Hip hop jewels.", "Synergistic management solutions.", "Crippling debt.", "Daddy issues.", "Used panties.", "Dropping a chandelier on your enemies and riding the rope up.", "Former President George W.Bush.", "Full frontal nudity.", "Hormone injections.", "Laying an egg.", "Getting naked and watching Nickelodeon.", "Pretending to care.", "Public ridicule.", "Seeing Grandma naked.", "Boogers.", "The inevitable heat death of the universe.", "The miracle of childbirth.", "The Rapture.", "Whipping it out.", "White privilege.", "Wifely duties.", "The Hamburglar.", "AXE Body Spray.", "The Blood of Christ.", "Horrifying laser hair removal accidents.", "BATMAN!!!", "Agriculture.", "A robust mongoloid.", "Natural selection.", "Coat hanger abortions.", "Sex with Patrick Stewart.", "Michelle Obama\u2019s arms.", "Penis breath.", "The World of Warcraft.", "Swooping.", "The morbidly obese.", "A homoerotic volleyball montage.", "Lockjaw.", "A mating display.", "Testicular torsion.", "All-you-can-eat shrimp for $4.99.", "Domino\u2019s\u2122 Oreo\u2122 Dessert Pizza.", "Kanye West.", "Hot cheese.", "Raptor attacks.", "Taking off your shirt.", "Smegma.", "Alcoholism.", "A middle-aged man on roller skates.", "The Care Bear Stare.", "Bingeing and purging.", "An oversized lollipop.", "Self-loathing.", "Children on leashes.", "Half-assed foreplay.", "The Holy Bible.", "German dungeon porn.", "Being on fire.", "Teenage pregnancy.", "Gandhi.", "Your weird brother.", "A Fleshlight.", "A pyramid of severed heads.", "An erection that lasts longer than four hours.", "My genitals.", "An endless stream of diarrhea.", "Science.", "Not reciprocating oral sex.", "Flightless birds.", "A good sniff.", "50,000 volts straight to the nipples.", "A balanced breakfast.", "Historically black colleges.", "The cool, refreshing taste of Pepsi.\xae", "The Make-A-Wish\xae Foundation.", "A tribe of warrior women.", "Passive-aggressive Post-it notes.", "The Chinese gymnastics team.", "Switching to Geico.\xae", "Peeing a little bit.", "Home video of Oprah sobbing into a Lean Cuisine.\xae", "Wet dreams.", "The Jews.", "My humps.", "Powerful thighs.", "Winking at old people.", "Mr.Clean, right behind you.", "A gentle caress of the inner thigh.", "Sexual tension.", "An M16 assault rifle.", "Skeletor.", "Fancy Feast.\xae", "Being rich.", "Sweet, sweet vengeance.", "Republicans.", "A gassy antelope.", "Natalie Portman.", "Copping a feel.", "Kamikaze pilots.", "Sean Connery.", "The homosexual agenda.", "The hardworking Mexican.", "A falcon with a cap on its head.", "Altar boys.", "The Kool-Aid Man.", "Getting so angry that you pop a boner.", "Free samples.", "Funky fresh rhymes.", "Doing the right thing.", "The Three-Fifths compromise.", "Lactation.", "World peace.", "RoboCop.", "Advice from a wise, old black man.", "Justin Bieber.", "Oompa-Loompas.", "Inappropriate yodeling.", "Puberty.", "Ghosts.", "An asymmetric boob job.", "Vigorous jazz hands.", "Fingering.", "Rush Limbaugh\u2019s soft, shitty body.", "GoGurt.\xae", "Police brutality.", "John Wilkes Booth.", "Preteens.", "White-man scalps.", "Helplessly giggling at the mention of Hutus and Tutsis.", "The light of a billion suns.", "Darth Vader.", "A sad handjob.", "Exactly what you\u2019d expect.", "Expecting a burp and vomiting on the floor.", "Adderall.\u2122", "Embryonic stem cells.", "Tasteful sideboob.", "Panda sex.", "An icepick lobotomy.", "Tom Cruise.", "Mouth herpes.", "Sperm whales.", "Homeless people.", "Third base.", "Incest.", "Pac-Man uncontrollably guzzling cum.", "A mime having a stroke.", "Running out of semen.", "God.", "The wonders of the Orient.", "Sexual peeing.", "Emotions.", "Licking things to claim them as your own.", "Jobs.", "The placenta.", "Spontaneous human combustion.", "Establishing dominance.", "Finger painting.", "Old-people smell.", "Dying of dysentery.", "My inner demons.", "A Super Soaker\u2122 full of cat pee.", "Aaron Burr.", "Cuddling.", "The chronic.", "Battlefield amputations.", "Friendly fire.", "Ronald Reagan.", "A disappointing birthday party.", "A sassy black woman.", "Becoming a blueberry.", "A tiny horse.", "William Shatner.", "Riding off into the sunset.", "An M.Night Shyamalan plot twist.", "Brown people.", "Mutually assured destruction.", "Pedophiles.", "Yeast.", "Grave robbing.", "Eating the last known bison.", "Catapults.", "Poor people.", "Destroying the evidence.", "The Hustle.", "The Force.", "Wiping her butt.", "Getting married, having a few kids, buying some stuff, retiring to Florida, and dying.", "Some god damn peace and quiet.", "AIDS.", "Pictures of boobs.", "Strong female characters.", "Emma Watson.", "Hospice care.", "Getting really high.", "Scientology.", "Penis envy.", "Praying the gay away.", "Frolicking.", "Two midgets shitting into a bucket.", "The KKK.", "Genghis Khan.", "Crystal meth.", "Serfdom.", "Holding down a child and farting all over him.", "A Bop It.\u2122", "Shaquille O\u2019Neal\u2019s acting career.", "Prancing.", "Vigilante justice.", "Overcompensation.", "Pixelated bukkake.", "A lifetime of sadness.", "Racism.", "Menstrual rage.", "Sunshine and rainbows.", "A monkey smoking a cigar.", "Court-ordered rehab.", "Lance Armstrong\u2019s missing testicle.", "Dry heaving.", "The terrorists.", "Miley Cyrus at 55.", "The rhythms of Africa.", "Breaking out into song and dance.", "Leprosy.", "Gloryholes.", "Nipple blades.", "The heart of a child.", "Puppies!", "Waking up half-naked in a Denny\u2019s parking lot.", "Bio-engineered assault turtles with acid breath.", "Toni Morrison\u2019s vagina.", "Daniel Radcliffe\u2019s delicious asshole.", "Active listening.", "Ethnic cleansing.", "The Little Engine That Could.", "The invisible hand.", "Waiting \u2019til marriage.", "Unfathomable stupidity.", "Shiny objects.", "The Devil himself.", "Autocannibalism.", "Erectile dysfunction.", "My collection of high-tech sex toys.", "The Pope.", "White people.", "Tentacle porn.", "Having anuses for eyes.", "The penny whistle solo from 'My Heart Will Go On.'", "Seppuku.", "Same-sex ice dancing.", "Cheating in the Special Olympics.", "Throwing a virgin into a volcano.", "Keanu Reeves.", "Sean Penn.", "Nickelback.", "Being fat and stupid.", "Pooping back and forth.Forever.", "A subscription to Men\u2019s Fitness.", "Kids with ass cancer.", "A salty surprise.", "The South.", "The violation of our most basic human rights.", "YOU MUST CONSTRUCT ADDITIONAL PYLONS.", "Consensual sex.", "Being fabulous.", "Necrophilia.", "Centaurs.", "Bill Nye the Science Guy.", "Black people.", "The Boy Scouts of America.", "Lunchables.\u2122", "Bitches.", "The profoundly handicapped.", "Heartwarming orphans.", "MechaHitler.", "Fiery poops.", "Saying 'I love you.'", "Inserting a Mason jar into my anus.", "The true meaning of Christmas.", "Estrogen.", "A zesty breakfast burrito.", "Joe Biden.", "The pirate\u2019s life.", "A bleached asshole.", "Michael Jackson.", "Cybernetic enhancements.", "Dark and mysterious forces beyond our control.", "Smallpox blankets.", "Masturbation.", "Classist undertones.", "Queefing.", "Concealing a boner.", "Edible underpants.", "Viagra.\xae", "Soup that is too hot.", "Muhammad (Praise Be Unto Him).", "Surprise sex!", "Five-Dollar Footlongs.\u2122", "Drinking alone.", "Dick fingers.", "Multiple stab wounds.", "Poopy diapers.", "Child abuse.", "Anal beads.", "Civilian casualties.", "Pulling out.", "Robert Downey, Jr.", "Horse meat.", "A really cool hat.", "Stalin.", "A stray pube.", "Jewish fraternities.", "The token minority.", "Doin\u2019 it in the butt.", "My ex-wife.", "Teaching a robot to love.", "A can of whoop-ass.", "A windmill full of corpses.", "Count Chocula.", "The wrath of Vladimir Putin.", "The Patriarchy.", "The glass ceiling.", "A cooler full of organs.", "The American Dream.", "Not wearing pants.", "When you fart and a little bit comes out.", "Take-backsies.", "Dead babies.", "Foreskin.", "A saxophone solo.", "Italians.", "A fetus.", "Firing a rifle into the air while balls deep in a squealing hog.", "Dick Cheney.", "Amputees.", "Eugenics.", "My relationship status.", "Christopher Walken.", "Bees?", "Harry Potter erotica.", "Giving birth to the Antichrist.", "Three dicks at the same time.", "Nazis.", "8 oz.of sweet Mexican black-tar heroin.", "Stephen Hawking talking dirty.", "Dead parents.", "Object permanence.", "Opposable thumbs.", "Racially-biased SAT questions.", "The Great Depression.", "Chainsaws for hands.", "Nicolas Cage.", "Child beauty pageants.", "Explosions.", "Sniffing glue.", "A man on the brink of orgasm.", "Repression.", "Invading Poland.", "My vagina.", "Assless chaps.", "A murder most foul.", "Giving 110%.", "Her Majesty, Queen Elizabeth II.", "The Trail of Tears.", "Being marginalized.", "Goblins.", "Hope.", "The Rev.Dr.Martin Luther King, Jr.", "A micropenis.", "My soul.", "A ball of earwax, semen, and toenail clippings.", "Vikings.", "Hot people.", "The art of seduction.", "An Oedipus complex.", "Geese.", "Extremely tight pants.", "New Age music.", "Hot Pockets.\xae", "Making a pouty face.", "Vehicular manslaughter.", "Women\u2019s suffrage.", "A defective condom.", "Judge Judy.", "African children.", "This year\u2019s mass shooting.", "Barack Obama.", "Asians who aren\u2019t good at math.", "Elderly Japanese men.", "The female orgasm.", "Heteronormativity.", "Crumbs all over the god damn carpet.", "Arnold Schwarzenegger.", "Road head.", "Spectacular abs.", "Figgy pudding.", "A mopey zoo lion.", "A bag of magic beans.", "Poor life choices.", "My sex life.", "Auschwitz.", "A snapping turtle biting the tip of your penis.", "A thermonuclear detonation.", "The clitoris.", "The Big Bang.", "Land mines.", "The entire Mormon Tabernacle Choir.", "A micropig wearing a tiny raincoat and booties.", "Jerking off into a pool of children\u2019s tears.", "Man meat.", "Me time.", "The Underground Railroad.", "Poorly-timed Holocaust jokes.", "A sea of troubles.", "Lumberjack fantasies.", "Morgan Freeman\u2019s voice.", "Women in yogurt commercials.", "Natural male enhancement.", "Being a motherfucking sorcerer.", "My black ass.", "Genuine human connection.", "Sexy pillow fights.", "Balls.", "Grandma.", "Friction.", "Chunks of dead hitchhiker.", "Farting and walking away.", "Being a dick to children.", "One trillion dollars.", "The Tempur-Pedic\xae Swedish Sleep System.\u2122", "Dying.", "Hurricane Katrina.", "The gays.", "The folly of man.", "Men.", "The Amish.", "An ugly face.", "A bitch slap.", "A brain tumor.", "Cards Against Humanity.", "Fear itself.", "Lady Gaga.", "The milkman.", "David Bowie flying in on a tiger made of lightning.", "A low standard of living.", "Gladiatorial combat.", "Mom.", "Scrotum tickling.", "Clenched butt cheeks.", "The harsh light of day.", "A crappy little hand.", "Neil Patrick Harris.", "Quivering jowls.", "Hipsters.", "The ooze.", "Insatiable bloodlust.", "One thousand Slim Jims.", "The hiccups.", "Syphilitic insanity.", "Ominous background music.", "Just the tip.", "An Etsy steampunk strap-on.", "Carnies.", "A rival dojo.", "Andre The Giant's enormous, leathery scrotum.", "Deflowering the princess.", "Nubile slave boys.", "A smiling black man, a latina businesswoman, a cool Asian, and some whites.", "Shaft.", "Being a dinosaur.", "Genetically engineered super-soldiers.", "Getting in her pants, politely.", "Fabricating statistics.", "Eating an albino.", "Jafar.", "Santa Claus.", "Zeus\u2019s sexual appetites.", "Revenge fucking.", "Making the penises kiss.", "A bloody pacifier.", "Sanding off a man's nose.", "A passionate Latino lover.", "Words, words, words.", "Historical revisionism.", "Medieval Times\xae Dinner & Tournament.", "Walking in on Dad peeing into Mom's mouth.", "Sexual humiliation.", "Ripping into a man\u2019s chest and pulling out his still-beating heart.", "George Clooney\u2019s musk.", "The economy.", "Leveling up.", "Having a penis.", "Savagely beating a mascot.", "Literally eating shit.", "Tripping balls.", "A big black dick.", "Mad hacky-sack skills.", "Getting abducted by Peter Pan.", "Quiche.", "Overpowering your father.", "The shambling corpse of Larry King.", "Suicidal thoughts.", "Gandalf.", "Statistically validated stereotypes.", "The four arms of Vishnu.", "Jean-Claude Van Damme in slow motion.", "Being a busy adult with many important things to do.", "The Gulags.", "Moral ambiguity.", "The boners of the elderly.", "An evil man in evil clothes.", "A web of lies.", "Bosnian chicken farmers.", "Dorito breath.", "Clams.", "My machete.", "Enormous Scandinavian women.", "Stockholm Syndrome.", "A nuanced critique.", "Ryan Gosling riding in on a white horse.", "A plunger to the face.", "Sudden Poop Explosion Disease.", "A fat bald man from the Internet.", "24-hour media coverage.", "A 55-gallon drum of lube.", "A pi\xf1ata full of scorpions.", "A fortuitous turnip harvest.", "Loki, the trickster god.", "The mere concept of Applebee's\xae.", "A Burmese tiger pit.", "Existing.", "Tongue.", "A dollop of sour cream.", "My first kill.", "Special musical guest, Cher.", "Making a friend.", "Living in a trashcan.", "Getting hilariously gang-banged by the Blue Man Group.", "Swiftly achieving orgasm.", "A sweet spaceship.", "Scrotal frostbite.", "Crushing Mr.Peanut's brittle body.", "Mild autism.", "Intimacy problems.", "Bullshit.", "One Ring to rule them all.", "Rising from the grave.", "Pumping out a baby every nine months.", "Death by Steven Seagal.", "Dining with cardboard cutouts of the cast of 'Friends.'", "Subduing a grizzly bear and making her your wife.", "Whipping a disobedient slave.", "Taking a man's eyes and balls out and putting his eyes where his balls go and then his balls in the eye holes.", "Grandpa\u2019s ashes.", "Hillary Clinton's death stare.", "A bigger, blacker dick.", "All of this blood.", "A sweaty, panting leather daddy.", "Maximal insertion.", "An ether-soaked rag.", "Weapons-grade plutonium.", "The human body.", "Wearing an octopus for a hat.", "A squadron of moles wearing aviator goggles.", "Fetal alcohol syndrome.", "A soulful rendition of 'Ol' Man River.'", "Pretty Pretty Princess Dress-Up Board Game.", "The mixing of the races.", "A magic hippie love cloud.", "The day the birds attacked.", "A sad fat dragon with no friends.", "A sofa that says 'I have style, but I like to be comfortable.'", "Tiny nipples.", "Finding Waldo.", "Basic human decency.", "The black Power Ranger.", "An unhinged ferris wheel rolling toward the sea.", "Some really fucked-up shit.", "Me.", "Whining like a little bitch.", "Graphic violence, adult language, and some sexual content.", "Survivor's guilt.", "A slightly shittier parallel universe.", "An army of skeletons.", "Double penetration.", "Boris the Soviet Love Hammer.", "Oncoming traffic.", "Being awesome at sex.", "Power.", "Nunchuck moves.", "Daddy's belt.", "Jeff Goldblum.", "Catastrophic urethral trauma.", "Mooing.", "Fuck Mountain.", "Beefin' over turf.", "Another shot of morphine.", "The new Radiohead album.", "A man in yoga pants with a ponytail and feather earrings.", "A vagina that leads to another dimension.", "A cat video so cute that your eyes roll back and your spine slides out of your anus.", "Going around punching people.", "The systematic destruction of an entire people and their way of life.", "Filling every orifice with butterscotch pudding.", "Slapping a racist old lady.", "Actually getting shot, for real.", "My manservant, Claude.", "Girls that always be textin'.", "A surprising amount of hair.", "Eating Tom Selleck's mustache to gain his powers.", "Samuel L.Jackson.", "An ass disaster.", "Indescribable loneliness.", "Blood farts.", "Unlimited soup, salad, and breadsticks.", "Mufasa's death scene.", "Chugging a lava lamp.", "A cop who is also a dog.", "Spending lots of money.", "A spontaneous conga line.", "The land of chocolate.", "Fisting.", "Cock.", "Crying into the pages of Sylvia Plath.", "Self-flagellation.", "The moist, demanding chasm of his mouth.", "The Harlem Globetrotters.", "Putting an entire peanut butter and jelly sandwich into the VCR.", "Letting everyone down.", "Not contributing to society in any meaningful way.", "Racial profiling.", "All my friends dying.", "Warm, velvety muppet sex.", "Dying alone and in pain.", "Bill Clinton, naked on a bearskin rug with a saxophone.", "A boo-boo.", "A greased-up Matthew McConaughey.", "Drinking ten 5-hour ENERGY\xaes to get 50 continuous hours of energy.", "An all-midget production of Shakespeare's Richard III.", "Some douche with an acoustic guitar.", "Disco fever.", "Screaming like a maniac.", "Flying robots that kill people.", "A botched circumcision.", "Jumping out at people.", "That ass.", "Demonic possession.", "Vomiting mid-blowjob.", "Sneezing, farting, and cumming at the same time.", "Three months in the hole.", "Having sex on top of a pizza.", "A pile of squirming bodies.", "Blowing some dudes in an alley.", "Getting your dick stuck in a Chinese finger trap with another dick.", "The entire Internet.", "The primal, ball-slapping sex your parents are having right now.", "Buying the right pants to be cool.", "The thin veneer of situational causality that underlies porn.", "Velcro\u2122.", "Reverse cowgirl.", "The Quesadilla Explosion Salad\u2122 from Chili\u2019s\xae.", "Nothing.", "An unstoppable wave of fire ants.", "Having shotguns for legs.", "Shutting the fuck up.", "The way white people is.", "A PowerPoint presentation.", "Roland the Farter, flatulist to the king.", "Vietnam flashbacks.", "A lamprey swimming up the toilet and latching onto your taint.", "Some kind of bird man.", "Running naked through a mall, pissing and shitting everywhere.", "Gay aliens.", "Not having sex.", "Prince Ali, fabulous he, Ali Ababwa.", "Sharks with legs.", "Interspecies marriage.", "Moderate to severe joint pain.", "Child Protective Services.", "A sex comet from Neptune that plunges the Earth into eternal sexiness.", "Exploding pigeons.", "The euphoric rush of strangling a drifter.", "Angelheaded hipsters burning for the ancient heavenly connection to the starry dynamo in the machinery of night.", "Ambiguous sarcasm.", "The peaceful and nonthreatening rise of China.", "The tiniest shred of evidence that God is real.", "Jizz.", "A bunch of idiots playing a card game instead of interacting like normal humans.", "Africa.", "Bouncing up and down.", "Blackula.", "A dance move that's just sex.", "Unquestioning obedience.", "The secret formula for ultimate female satisfaction.", "Whispering all sexy.", "Smoking crack, for instance.", "Some sort of Asian.", "My worthless son.", "A kiss on the lips.", "A shiny rock that proves I love you.", "A Ugandan warlord.", "Whatever a McRib is made of.", "10 Incredible Facts About the Anus.", "Actual mutants with medical conditions and no superpowers.", "A Native American who solves crimes by going into the spirit world.", "Sugar madness.", "Three consecutive seconds of happiness.", "Party Mexicans.", "Drinking responsibly.", "Crazy opium eyes.", "A hopeless amount of spiders.", "The complex geopolitical quagmire that is the Middle East.", "Fucking a corpse back to life.", "Lots and lots of abortions.", "A horse with no legs.", "Neil Diamond's greatest hits.", "Falling into the toilet.", "My dad's dumb fucking face.", "How awesome I am.", "Dem titties.", "Finally finishing off the Indians.", "My sex dungeon.", "Injecting speed into one arm and horse tranquilizer into the other.", "A manhole.", "No clothes on, penis in vagina.", "Snorting coke off a clown's boner.", "Calculating every mannerism so as not to suggest homosexuality.", "Khakis.", "A gender identity that can only be conveyed through slam poetry.", "All the single ladies.", "Doo-doo.", "The size of my penis.", "A for-real lizard that spits blood from its eyes.", "The safe word.", "Depression.", "An interracial handshake.", "Ass to mouth.", "Almost giving money to a homeless person.", "Sports.", "Stuffing a child's face with Fun Dip until he starts having fun.", "A fart.", "What Jesus would do.", "A sex goblin with a carnival penis.", "Grammar nazis who are also regular Nazis.", "Not believing in giraffes.", "Mom's new boyfriend.", "AIDS monkeys.", "Getting eaten alive by Guy Fieri.", "All these decorative pillows.", "A one-way ticket to Gary, Indiana.", "Ennui.", "Oil!", "A crazy little thing called love.", "40 acres and a mule.", "Blowjobs for everyone.", "Genghis Khan's DNA.", "An uninterrupted history of imperialism and exploitation.", "Going to a high school reunion on ketamine.", "Slowly easing down onto a cucumber.", "The eight gay warlocks who dictate the rules of fashion.", "Seeing things from Hitler's perspective.", "Anal fissures like you wouldn't believe.", "My first period.", "A giant powdery manbaby.", "Boring vaginal sex.", "A powered exoskeleton.", "Denzel.", "Out-of-this-world bazongas.", "Butt stuff.", "The white half of Barack Obama.", "Vegetarian options.", "Child support payments.", "An unforgettable quincea\xf1era.", "Too much cocaine.", "The black half of Barack Obama.", "Unrelenting genital punishment.", "Daddy's credit card.", "Deez nuts.", "A whole new kind of porn.", "Ancient Athenian boy-fucking.", "P.F. Chang himself.", "An inability to form meaningful relationships.", "Ejaculating live bees and the bees are angry.", "Blackface.", "A zero-risk way to make $2,000 from home.", "Getting drive-by shot.", "Seeing my village burned and my family slaughtered before my eyes.", "The passage of time.", "The swim team, all at once.", "Being nine years old.", "A team of lawyers.", "A face full of horse cum.", "Free ice cream, yo.", "Figuring out how to have sex with a dolphin.", "Cutting off a flamingo's legs with garden shears.", "Being paralyzed from the neck down.", "Russian super-tuberculosis.", "Being worshipped as the one true God.", "Some shit-hot guitar licks.", "Changing a person's mind with logic and facts.", "The Abercrombie & Fitch lifestyle.", "My boyfriend's stupid penis.", "The basic suffering that pervades all of existence.", "A mouthful of potato salad.", "The tiger that killed my father.", "The unbelievable world of mushrooms.", "Wearing glasses and sounding smart.", "Doing the right stuff to her nipples.", "Western standards of beauty.", "Having been dead for a while.", "A disappointing salad.", "My dead son's baseball glove.", "Getting caught by the police and going to jail.", "Giant sperm from outer space.", "A reason not to commit suicide.", "Social justice warriors with flamethrowers of compassion.", "The ghost of Marlon Brando.", "September 11th, 2001.", "Backwards knees."],
            this.bcList = ["What ended my last relationship?", "__________. It\u2019s a trap!", "__________. High five, bro.", "I got 99 problems but __________ ain\u2019t one.", "How am I maintaining my relationship status?", "The new Chevy Tahoe. With the power and space to take __________ everywhere you go.", "When Pharaoh remained unmoved, Moses called down a Plague of __________.", "In the new Disney Channel Original Movie, Hannah Montana struggles with __________ for the first time.", "While the United States raced the Soviet Union to the moon, the Mexican government funneled millions of pesos into research on __________.", "This is the way the world ends / This is the way the world ends / Not with a bang but with __________.", "Dear Abby, I\u2019m having some trouble with __________ and would like your advice.", "__________. Betcha can\u2019t have just one!", "A romantic, candlelit dinner would be incomplete without __________.", "Coming to Broadway this season, __________: The Musical.", "What am I giving up for Lent?", "What will always get you laid?", "The Smithsonian Museum of Natural History has just opened an interactive exhibit on __________.", "What are my parents hiding from me?", "Maybe she\u2019s born with it. Maybe it\u2019s __________.", "Next from J.K. Rowling: Harry Potter and the Chamber of __________.", "What\u2019s that smell?", "Today on Maury: 'Help! My son is __________!'", "What gives me uncontrollable gas?", "__________. That\u2019s how I want to die.", "What\u2019s my anti-drug?", "War! What is it good for?", "What's George W. Bush thinking about right now?", "What don't you want to find in your Kung Pao chicken?", "I\u2019m sorry, Professor, but I couldn\u2019t complete my homework because of __________.", "What would grandma find disturbing, yet oddly charming?", "What helps Obama unwind?", "A recent laboratory study shows that undergraduates have 50% less sex after being exposed to _____.", "What\u2019s that sound?", "Introducing Xtreme Baseball! It's like baseball, but with ______!", "What\u2019s my secret power?", "When I am President of the United States, I will create the Department of __________.", "After the earthquake, Sean Penn brought __________ to the people of Haiti.", "Next on ESPN2: The World Series of __________.", "What did the US airdrop to the children of Afghanistan?", "What\u2019s a girl\u2019s best friend?", "What\u2019s the new fad diet?", "What gets better with age?", "Why can\u2019t I sleep at night?", "What is Batman\u2019s guilty pleasure?", "Life for American Indians was forever changed when the White Man introduced them to __________.", "What\u2019s Teach for America using to inspire inner city students to succeed?", "I do not know with what weapons World War III will be fought, but World War IV will be fought with __________.", "White people like __________.", "What did Vin Diesel eat for dinner?", "In 1,000 years, when paper money is a distant memory, how will we pay for goods and services?", "Why am I sticky?", "__________: Kid-tested, mother-approved.", "Fun tip! When your man asks you to go down on him, try surprising him with __________ instead.", "It\u2019s a pity that kids these days are all getting involved with __________.", "What\u2019s there a ton of in heaven?", "Alternative medicine is now embracing the curative powers of __________.", "What did I bring back from Mexico?", "Why do I hurt all over?", "What\u2019s the next Happy Meal\xae toy?", "TSA guidelines now prohibit __________ on airplanes.", "Instead of coal, Santa now gives the bad children __________.", "What never fails to liven up the party?", "MTV\u2019s new reality show features eight washed-up celebrities living with __________.", "But before I kill you, Mr. Bond, I must show you __________.", "When I am a billionaire, I shall erect a 50-foot statue to commemorate __________.", "What will I bring back in time to convince people that I am a powerful wizard?", "During sex, I like to think about __________.", "In L.A. County Jail, word is you can trade 200 cigarettes for __________.", "The class field trip was completely ruined by __________.", "I get by with a little help from ______.", "Daddy, why is mommy crying?", "__________: Good to the last drop.", "I drink to forget __________.", "Here is the church / Here is the steeple / Open the doors / And there is __________.", "What\u2019s the most emo?", "How did I lose my virginity?", "The secret to a lasting marriage is communication, communication, and __________.", "My plan for world domination begins with __________.", "Next season on Man vs. Wild, Bear Grylls must survive in the depths of the Amazon with only __________ and his wits.", "Science will never explain __________.", "The CIA now interrogates enemy agents by repeatedly subjecting them to __________.", "In Rome, there are whisperings that the Vatican has a secret room devoted to __________.", "When all else fails, I can always masturbate to __________.", "I learned the hard way that you can\u2019t cheer up a grieving friend with __________.", "In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated __________.", "The socialist governments of Scandinavia have declared that access to __________ is a basic human right.", "In his new self-produced album, Kanye West raps over the sounds of __________.", "What\u2019s the gift that keeps on giving?", "When I pooped, what came out of my butt?", "In the distant future, historians will agree that __________ marked the beginning of America\u2019s decline.", "What has been making life difficult at the nudist colony?", "And I would have gotten away with it, too, if it hadn\u2019t been for __________.", "What brought the orgy to a grinding halt?", "A remarkable new study has shown that chimps have evolved their own primitive version of __________.", "Your persistence is admirable, my dear Prince. But you cannot win my heart with __________ alone.", "During his midlife crisis, my dad got really into __________.", "My new favorite porn star is Joey '__________' McGee.", "Before I run for president, I must destroy all evidence of my involvement with __________.", "This is your captain speaking. Fasten your seatbelts and prepare for __________.", "In his newest and most difficult stunt, David Blaine must escape from __________.", "The Five Stages of Grief: denial, anger, bargaining, __________, acceptance.", "Members of New York's social elite are paying thousands of dollars just to experience __________.", "This month's Cosmo: 'Spice up your sex life by bringing __________ into the bedroom.'", "Little Miss Muffet  Sat on a tuffet,  Eating her curds and __________.", "My country, 'tis of thee, sweet land of __________.", "Next time on Dr. Phil: How to talk to your child about __________.", "Only two things in life are certain: death and __________.", "The healing process began when I joined a support group for victims of __________.", "What's harshing my mellow, man?", "Charades was ruined for me forever when my mom had to act out __________.", "Tonight on 20/20: What you don't know about __________ could kill you.", "__________. Awesome in theory, kind of a mess in practice.", "A successful job interview begins with a firm handshake and ends with __________.", "And what did _you_ bring for show-and-tell?", "As part of his contract, Prince won't perform without __________ in his dressing room.", "As part of his daily regimen, Anderson Cooper sets aside 15 minutes for __________.", "Call the law offices of Goldstein and Goldstein, because no one should have to tolerate  __________ in the workplace.", "During high school, I never really fit in until I found __________ Club.", "Finally! A service that delivers __________ right to your door.", "Hey baby, come back to my place and I'll show you __________.", "I'm not like the rest of you. I'm too rich and busy for __________.", "In the seventh circle of Hell, sinners must endure __________ for all eternity.", "Lovin' you is easy 'cause you're __________.", "Money can't buy me love, but it can buy me __________.", "My gym teacher got fired for adding __________ to the obstacle course.", "The blind date was going horribly until we discovered our shared interest in __________.", "To prepare for his upcoming role, Daniel Day-Lewis immersed himself in the world of __________.", "Turns out that __________-Man was neither the hero we needed nor wanted.", "What left this stain on my couch?", "The Japanese have developed a smaller, more efficient version of __________.", "I'm pretty sure I'm high right now, because I'm absolutely mesmerized by __________.", "What's fun until it gets weird?", "Man, this is bullshit. Fuck __________.", "2 AM in the city that never sleeps. The door swings open and *she* walks in, legs up to here. Something in her eyes tells me she's looking for __________.", "I'm sorry, sir, but we don't allow __________ at the country club.", "It lurks in the night. It hungers for flesh. This summer, no one is safe from __________.", "As King, how will I keep the peasants in line?", "Wes Anderson's new film tells the story of a precocious child coming to terms with __________.", "She's up all night for good fun. I'm up all night for __________.", "Alright, bros. Our frat house is condemned and all the hot slampieces are over at Gamma Phi. The time has come to commence Operation __________.", "How am I compensating for my tiny penis?", "Dear Leader Kim Jong Un, our village praises your infinite wisdom with a humble offering of __________.", "Do not fuck with me! I am literally __________ right now.", "This is the prime of my life. I'm young, hot, and full of __________.", "You've seen the bearded lady! You've seen the ring of fire! Now, ladies and gentlemen, feast your eyes upon __________!", "Yo' mama so fat she __________!", "Hi, this is Jim from accounting. We noticed a $1,200 charge labeled '__________.' Can you explain?", "Having the worst day EVER. #__________", "Hi MTV! My name is Kendra, I live in Malibu, I'm into __________, and I love to have a good time.", "In his farewell address, George Washington famously warned Americans about the dangers of __________.", "Life's pretty tough in the fast lane. That's why I never leave the house without __________.", "Don't forget! Beginning this week, Casual Friday will officially become '__________ Friday.'", "What's making things awkward in the sauna?", "Now in bookstores: 'The Audacity of __________,' by Barack Obama.", "Armani suit: $1,000. Dinner for two at that swanky restaurant: $300. The look on her face when you surprise her with __________: priceless.", "Do the Dew\xae with our most extreme flavor yet! Get ready for Mountain Dew __________!", "Don't miss the action comedy of the year! One cop plays by the book. The other's only interested in one thing: __________.", "Here at the Academy for Gifted Children, we allow students to explore __________ at their own pace.", "Why am I broke?", "Well what do you have to say for yourself, Casey? This is the third time you've been sent to the principal's office for ___________.", "And today's soup is Cream of __________.", "I don't mean to brag, but they call me the Michael Jordan of __________.", "Help me doctor, I've got _____ in my butt!", "In his new action comedy, Jackie Chan must fend off ninjas while also dealing with _____.", "WHOOO! God damn I love _____!", "What killed my boner?", "Do you lack energy? Does it sometimes feel like the whole world is _____? Zoloft.\xae"],
"""


class CardSet:
    def __init__(self, code):
        print("Getting code", code)
        if str.upper(code) == '55HNH':
            info = json.loads(_POLISH_CACHE)
        else:
            info = json.loads(requests.get(_CARDCAST_BASE_URL + code).text)
        self.name = info["name"]
        if str.upper(code) == '55HNH':
            cards = json.loads(_POLISH_CARDS_CACHE)
        else:
            cards = json.loads(requests.get(_CARDCAST_BASE_URL + code + "/cards").text)
        self.questions = []
        self.answers = []
        for question in cards["calls"]:
            if len(question["text"]) == 2:
                self.questions.append("___".join(question["text"]))
        for answer in cards["responses"]:
            self.answers.append(answer["text"][0])


DEFAULT_SET = CardSet.__new__(CardSet)
DEFAULT_SET.name = "Default set"
DEFAULT_SET.answers = ["A bucket of fish heads.", "Silence.", "The unstoppable tide of Islam.", "Growing a pair.",
                       "Famine.", "Flesh-eating bacteria.", "Flying sex snakes.",
                       "Not giving a shit about the Third World.", "Magnets.", "Shapeshifters.",
                       "Our first chimpanzee President.", "Crucifixion.", "72 virgins.", "A live studio audience.",
                       "A time travel paradox.", "Authentic Mexican cuisine.", "Hip hop jewels.",
                       "Synergistic management solutions.", "Crippling debt.", "Daddy issues.", "Used panties.",
                       "Dropping a chandelier on your enemies and riding the rope up.",
                       "Former President George W.Bush.", "Full frontal nudity.", "Hormone injections.",
                       "Laying an egg.", "Getting naked and watching Nickelodeon.", "Pretending to care.",
                       "Public ridicule.", "Seeing Grandma naked.", "Boogers.",
                       "The inevitable heat death of the universe.", "The miracle of childbirth.", "The Rapture.",
                       "Whipping it out.", "White privilege.", "Wifely duties.", "The Hamburglar.", "AXE Body Spray.",
                       "The Blood of Christ.", "Horrifying laser hair removal accidents.", "BATMAN!!!", "Agriculture.",
                       "A robust mongoloid.", "Natural selection.", "Coat hanger abortions.",
                       "Sex with Patrick Stewart.", "Michelle Obama\u2019s arms.", "Penis breath.",
                       "The World of Warcraft.", "Swooping.", "The morbidly obese.", "A homoerotic volleyball montage.",
                       "Lockjaw.", "A mating display.", "Testicular torsion.", "All-you-can-eat shrimp for $4.99.",
                       "Domino\u2019s\u2122 Oreo\u2122 Dessert Pizza.", "Kanye West.", "Hot cheese.", "Raptor attacks.",
                       "Taking off your shirt.", "Smegma.", "Alcoholism.", "A middle-aged man on roller skates.",
                       "The Care Bear Stare.", "Bingeing and purging.", "An oversized lollipop.", "Self-loathing.",
                       "Children on leashes.", "Half-assed foreplay.", "The Holy Bible.", "German dungeon porn.",
                       "Being on fire.", "Teenage pregnancy.", "Gandhi.", "Your weird brother.", "A Fleshlight.",
                       "A pyramid of severed heads.", "An erection that lasts longer than four hours.", "My genitals.",
                       "An endless stream of diarrhea.", "Science.", "Not reciprocating oral sex.", "Flightless birds.",
                       "A good sniff.", "50,000 volts straight to the nipples.", "A balanced breakfast.",
                       "Historically black colleges.", "The cool, refreshing taste of Pepsi.\xae",
                       "The Make-A-Wish\xae Foundation.", "A tribe of warrior women.",
                       "Passive-aggressive Post-it notes.", "The Chinese gymnastics team.", "Switching to Geico.\xae",
                       "Peeing a little bit.", "Home video of Oprah sobbing into a Lean Cuisine.\xae", "Wet dreams.",
                       "The Jews.", "My humps.", "Powerful thighs.", "Winking at old people.",
                       "Mr.Clean, right behind you.", "A gentle caress of the inner thigh.", "Sexual tension.",
                       "An M16 assault rifle.", "Skeletor.", "Fancy Feast.\xae", "Being rich.",
                       "Sweet, sweet vengeance.", "Republicans.", "A gassy antelope.", "Natalie Portman.",
                       "Copping a feel.", "Kamikaze pilots.", "Sean Connery.", "The homosexual agenda.",
                       "The hardworking Mexican.", "A falcon with a cap on its head.", "Altar boys.",
                       "The Kool-Aid Man.", "Getting so angry that you pop a boner.", "Free samples.",
                       "Funky fresh rhymes.", "Doing the right thing.", "The Three-Fifths compromise.", "Lactation.",
                       "World peace.", "RoboCop.", "Advice from a wise, old black man.", "Justin Bieber.",
                       "Oompa-Loompas.", "Inappropriate yodeling.", "Puberty.", "Ghosts.", "An asymmetric boob job.",
                       "Vigorous jazz hands.", "Fingering.", "Rush Limbaugh\u2019s soft, shitty body.", "GoGurt.\xae",
                       "Police brutality.", "John Wilkes Booth.", "Preteens.", "White-man scalps.",
                       "Helplessly giggling at the mention of Hutus and Tutsis.", "The light of a billion suns.",
                       "Darth Vader.", "A sad handjob.", "Exactly what you\u2019d expect.",
                       "Expecting a burp and vomiting on the floor.", "Adderall.\u2122", "Embryonic stem cells.",
                       "Tasteful sideboob.", "Panda sex.", "An icepick lobotomy.", "Tom Cruise.", "Mouth herpes.",
                       "Sperm whales.", "Homeless people.", "Third base.", "Incest.",
                       "Pac-Man uncontrollably guzzling cum.", "A mime having a stroke.", "Running out of semen.",
                       "God.", "The wonders of the Orient.", "Sexual peeing.", "Emotions.",
                       "Licking things to claim them as your own.", "Jobs.", "The placenta.",
                       "Spontaneous human combustion.", "Establishing dominance.", "Finger painting.",
                       "Old-people smell.", "Dying of dysentery.", "My inner demons.",
                       "A Super Soaker\u2122 full of cat pee.", "Aaron Burr.", "Cuddling.", "The chronic.",
                       "Battlefield amputations.", "Friendly fire.", "Ronald Reagan.",
                       "A disappointing birthday party.", "A sassy black woman.", "Becoming a blueberry.",
                       "A tiny horse.", "William Shatner.", "Riding off into the sunset.",
                       "An M.Night Shyamalan plot twist.", "Brown people.", "Mutually assured destruction.",
                       "Pedophiles.", "Yeast.", "Grave robbing.", "Eating the last known bison.", "Catapults.",
                       "Poor people.", "Destroying the evidence.", "The Hustle.", "The Force.", "Wiping her butt.",
                       "Getting married, having a few kids, buying some stuff, retiring to Florida, and dying.",
                       "Some god damn peace and quiet.", "AIDS.", "Pictures of boobs.", "Strong female characters.",
                       "Emma Watson.", "Hospice care.", "Getting really high.", "Scientology.", "Penis envy.",
                       "Praying the gay away.", "Frolicking.", "Two midgets shitting into a bucket.", "The KKK.",
                       "Genghis Khan.", "Crystal meth.", "Serfdom.", "Holding down a child and farting all over him.",
                       "A Bop It.\u2122", "Shaquille O\u2019Neal\u2019s acting career.", "Prancing.",
                       "Vigilante justice.", "Overcompensation.", "Pixelated bukkake.", "A lifetime of sadness.",
                       "Racism.", "Menstrual rage.", "Sunshine and rainbows.", "A monkey smoking a cigar.",
                       "Court-ordered rehab.", "Lance Armstrong\u2019s missing testicle.", "Dry heaving.",
                       "The terrorists.", "Miley Cyrus at 55.", "The rhythms of Africa.",
                       "Breaking out into song and dance.", "Leprosy.", "Gloryholes.", "Nipple blades.",
                       "The heart of a child.", "Puppies!", "Waking up half-naked in a Denny\u2019s parking lot.",
                       "Bio-engineered assault turtles with acid breath.", "Toni Morrison\u2019s vagina.",
                       "Daniel Radcliffe\u2019s delicious asshole.", "Active listening.", "Ethnic cleansing.",
                       "The Little Engine That Could.", "The invisible hand.", "Waiting \u2019til marriage.",
                       "Unfathomable stupidity.", "Shiny objects.", "The Devil himself.", "Autocannibalism.",
                       "Erectile dysfunction.", "My collection of high-tech sex toys.", "The Pope.", "White people.",
                       "Tentacle porn.", "Having anuses for eyes.",
                       "The penny whistle solo from 'My Heart Will Go On.'", "Seppuku.", "Same-sex ice dancing.",
                       "Cheating in the Special Olympics.", "Throwing a virgin into a volcano.", "Keanu Reeves.",
                       "Sean Penn.", "Nickelback.", "Being fat and stupid.", "Pooping back and forth.Forever.",
                       "A subscription to Men\u2019s Fitness.", "Kids with ass cancer.", "A salty surprise.",
                       "The South.", "The violation of our most basic human rights.",
                       "YOU MUST CONSTRUCT ADDITIONAL PYLONS.", "Consensual sex.", "Being fabulous.", "Necrophilia.",
                       "Centaurs.", "Bill Nye the Science Guy.", "Black people.", "The Boy Scouts of America.",
                       "Lunchables.\u2122", "Bitches.", "The profoundly handicapped.", "Heartwarming orphans.",
                       "MechaHitler.", "Fiery poops.", "Saying 'I love you.'", "Inserting a Mason jar into my anus.",
                       "The true meaning of Christmas.", "Estrogen.", "A zesty breakfast burrito.", "Joe Biden.",
                       "The pirate\u2019s life.", "A bleached asshole.", "Michael Jackson.", "Cybernetic enhancements.",
                       "Dark and mysterious forces beyond our control.", "Smallpox blankets.", "Masturbation.",
                       "Classist undertones.", "Queefing.", "Concealing a boner.", "Edible underpants.", "Viagra.\xae",
                       "Soup that is too hot.", "Muhammad (Praise Be Unto Him).", "Surprise sex!",
                       "Five-Dollar Footlongs.\u2122", "Drinking alone.", "Dick fingers.", "Multiple stab wounds.",
                       "Poopy diapers.", "Child abuse.", "Anal beads.", "Civilian casualties.", "Pulling out.",
                       "Robert Downey, Jr.", "Horse meat.", "A really cool hat.", "Stalin.", "A stray pube.",
                       "Jewish fraternities.", "The token minority.", "Doin\u2019 it in the butt.", "My ex-wife.",
                       "Teaching a robot to love.", "A can of whoop-ass.", "A windmill full of corpses.",
                       "Count Chocula.", "The wrath of Vladimir Putin.", "The Patriarchy.", "The glass ceiling.",
                       "A cooler full of organs.", "The American Dream.", "Not wearing pants.",
                       "When you fart and a little bit comes out.", "Take-backsies.", "Dead babies.", "Foreskin.",
                       "A saxophone solo.", "Italians.", "A fetus.",
                       "Firing a rifle into the air while balls deep in a squealing hog.", "Dick Cheney.", "Amputees.",
                       "Eugenics.", "My relationship status.", "Christopher Walken.", "Bees?", "Harry Potter erotica.",
                       "Giving birth to the Antichrist.", "Three dicks at the same time.", "Nazis.",
                       "8 oz.of sweet Mexican black-tar heroin.", "Stephen Hawking talking dirty.", "Dead parents.",
                       "Object permanence.", "Opposable thumbs.", "Racially-biased SAT questions.",
                       "The Great Depression.", "Chainsaws for hands.", "Nicolas Cage.", "Child beauty pageants.",
                       "Explosions.", "Sniffing glue.", "A man on the brink of orgasm.", "Repression.",
                       "Invading Poland.", "My vagina.", "Assless chaps.", "A murder most foul.", "Giving 110%.",
                       "Her Majesty, Queen Elizabeth II.", "The Trail of Tears.", "Being marginalized.", "Goblins.",
                       "Hope.", "The Rev.Dr.Martin Luther King, Jr.", "A micropenis.", "My soul.",
                       "A ball of earwax, semen, and toenail clippings.", "Vikings.", "Hot people.",
                       "The art of seduction.", "An Oedipus complex.", "Geese.", "Extremely tight pants.",
                       "New Age music.", "Hot Pockets.\xae", "Making a pouty face.", "Vehicular manslaughter.",
                       "Women\u2019s suffrage.", "A defective condom.", "Judge Judy.", "African children.",
                       "This year\u2019s mass shooting.", "Barack Obama.", "Asians who aren\u2019t good at math.",
                       "Elderly Japanese men.", "The female orgasm.", "Heteronormativity.",
                       "Crumbs all over the god damn carpet.", "Arnold Schwarzenegger.", "Road head.",
                       "Spectacular abs.", "Figgy pudding.", "A mopey zoo lion.", "A bag of magic beans.",
                       "Poor life choices.", "My sex life.", "Auschwitz.",
                       "A snapping turtle biting the tip of your penis.", "A thermonuclear detonation.",
                       "The clitoris.", "The Big Bang.", "Land mines.", "The entire Mormon Tabernacle Choir.",
                       "A micropig wearing a tiny raincoat and booties.",
                       "Jerking off into a pool of children\u2019s tears.", "Man meat.", "Me time.",
                       "The Underground Railroad.", "Poorly-timed Holocaust jokes.", "A sea of troubles.",
                       "Lumberjack fantasies.", "Morgan Freeman\u2019s voice.", "Women in yogurt commercials.",
                       "Natural male enhancement.", "Being a motherfucking sorcerer.", "My black ass.",
                       "Genuine human connection.", "Sexy pillow fights.", "Balls.", "Grandma.", "Friction.",
                       "Chunks of dead hitchhiker.", "Farting and walking away.", "Being a dick to children.",
                       "One trillion dollars.", "The Tempur-Pedic\xae Swedish Sleep System.\u2122", "Dying.",
                       "Hurricane Katrina.", "The gays.", "The folly of man.", "Men.", "The Amish.", "An ugly face.",
                       "A bitch slap.", "A brain tumor.", "Cards Against Humanity.", "Fear itself.", "Lady Gaga.",
                       "The milkman.", "David Bowie flying in on a tiger made of lightning.",
                       "A low standard of living.", "Gladiatorial combat.", "Mom.", "Scrotum tickling.",
                       "Clenched butt cheeks.", "The harsh light of day.", "A crappy little hand.",
                       "Neil Patrick Harris.", "Quivering jowls.", "Hipsters.", "The ooze.", "Insatiable bloodlust.",
                       "One thousand Slim Jims.", "The hiccups.", "Syphilitic insanity.", "Ominous background music.",
                       "Just the tip.", "An Etsy steampunk strap-on.", "Carnies.", "A rival dojo.",
                       "Andre The Giant's enormous, leathery scrotum.", "Deflowering the princess.",
                       "Nubile slave boys.",
                       "A smiling black man, a latina businesswoman, a cool Asian, and some whites.", "Shaft.",
                       "Being a dinosaur.", "Genetically engineered super-soldiers.", "Getting in her pants, politely.",
                       "Fabricating statistics.", "Eating an albino.", "Jafar.", "Santa Claus.",
                       "Zeus\u2019s sexual appetites.", "Revenge fucking.", "Making the penises kiss.",
                       "A bloody pacifier.", "Sanding off a man's nose.", "A passionate Latino lover.",
                       "Words, words, words.", "Historical revisionism.", "Medieval Times\xae Dinner & Tournament.",
                       "Walking in on Dad peeing into Mom's mouth.", "Sexual humiliation.",
                       "Ripping into a man\u2019s chest and pulling out his still-beating heart.",
                       "George Clooney\u2019s musk.", "The economy.", "Leveling up.", "Having a penis.",
                       "Savagely beating a mascot.", "Literally eating shit.", "Tripping balls.", "A big black dick.",
                       "Mad hacky-sack skills.", "Getting abducted by Peter Pan.", "Quiche.",
                       "Overpowering your father.", "The shambling corpse of Larry King.", "Suicidal thoughts.",
                       "Gandalf.", "Statistically validated stereotypes.", "The four arms of Vishnu.",
                       "Jean-Claude Van Damme in slow motion.", "Being a busy adult with many important things to do.",
                       "The Gulags.", "Moral ambiguity.", "The boners of the elderly.", "An evil man in evil clothes.",
                       "A web of lies.", "Bosnian chicken farmers.", "Dorito breath.", "Clams.", "My machete.",
                       "Enormous Scandinavian women.", "Stockholm Syndrome.", "A nuanced critique.",
                       "Ryan Gosling riding in on a white horse.", "A plunger to the face.",
                       "Sudden Poop Explosion Disease.", "A fat bald man from the Internet.", "24-hour media coverage.",
                       "A 55-gallon drum of lube.", "A pi\xf1ata full of scorpions.", "A fortuitous turnip harvest.",
                       "Loki, the trickster god.", "The mere concept of Applebee's\xae.", "A Burmese tiger pit.",
                       "Existing.", "Tongue.", "A dollop of sour cream.", "My first kill.",
                       "Special musical guest, Cher.", "Making a friend.", "Living in a trashcan.",
                       "Getting hilariously gang-banged by the Blue Man Group.", "Swiftly achieving orgasm.",
                       "A sweet spaceship.", "Scrotal frostbite.", "Crushing Mr.Peanut's brittle body.", "Mild autism.",
                       "Intimacy problems.", "Bullshit.", "One Ring to rule them all.", "Rising from the grave.",
                       "Pumping out a baby every nine months.", "Death by Steven Seagal.",
                       "Dining with cardboard cutouts of the cast of 'Friends.'",
                       "Subduing a grizzly bear and making her your wife.", "Whipping a disobedient slave.",
                       "Taking a man's eyes and balls out and putting his eyes where his balls go and then his balls in the eye holes.",
                       "Grandpa\u2019s ashes.", "Hillary Clinton's death stare.", "A bigger, blacker dick.",
                       "All of this blood.", "A sweaty, panting leather daddy.", "Maximal insertion.",
                       "An ether-soaked rag.", "Weapons-grade plutonium.", "The human body.",
                       "Wearing an octopus for a hat.", "A squadron of moles wearing aviator goggles.",
                       "Fetal alcohol syndrome.", "A soulful rendition of 'Ol' Man River.'",
                       "Pretty Pretty Princess Dress-Up Board Game.", "The mixing of the races.",
                       "A magic hippie love cloud.", "The day the birds attacked.", "A sad fat dragon with no friends.",
                       "A sofa that says 'I have style, but I like to be comfortable.'", "Tiny nipples.",
                       "Finding Waldo.", "Basic human decency.", "The black Power Ranger.",
                       "An unhinged ferris wheel rolling toward the sea.", "Some really fucked-up shit.", "Me.",
                       "Whining like a little bitch.", "Graphic violence, adult language, and some sexual content.",
                       "Survivor's guilt.", "A slightly shittier parallel universe.", "An army of skeletons.",
                       "Double penetration.", "Boris the Soviet Love Hammer.", "Oncoming traffic.",
                       "Being awesome at sex.", "Power.", "Nunchuck moves.", "Daddy's belt.", "Jeff Goldblum.",
                       "Catastrophic urethral trauma.", "Mooing.", "Fuck Mountain.", "Beefin' over turf.",
                       "Another shot of morphine.", "The new Radiohead album.",
                       "A man in yoga pants with a ponytail and feather earrings.",
                       "A vagina that leads to another dimension.",
                       "A cat video so cute that your eyes roll back and your spine slides out of your anus.",
                       "Going around punching people.",
                       "The systematic destruction of an entire people and their way of life.",
                       "Filling every orifice with butterscotch pudding.", "Slapping a racist old lady.",
                       "Actually getting shot, for real.", "My manservant, Claude.", "Girls that always be textin'.",
                       "A surprising amount of hair.", "Eating Tom Selleck's mustache to gain his powers.",
                       "Samuel L.Jackson.", "An ass disaster.", "Indescribable loneliness.", "Blood farts.",
                       "Unlimited soup, salad, and breadsticks.", "Mufasa's death scene.", "Chugging a lava lamp.",
                       "A cop who is also a dog.", "Spending lots of money.", "A spontaneous conga line.",
                       "The land of chocolate.", "Fisting.", "Cock.", "Crying into the pages of Sylvia Plath.",
                       "Self-flagellation.", "The moist, demanding chasm of his mouth.", "The Harlem Globetrotters.",
                       "Putting an entire peanut butter and jelly sandwich into the VCR.", "Letting everyone down.",
                       "Not contributing to society in any meaningful way.", "Racial profiling.",
                       "All my friends dying.", "Warm, velvety muppet sex.", "Dying alone and in pain.",
                       "Bill Clinton, naked on a bearskin rug with a saxophone.", "A boo-boo.",
                       "A greased-up Matthew McConaughey.",
                       "Drinking ten 5-hour ENERGY\xaes to get 50 continuous hours of energy.",
                       "An all-midget production of Shakespeare's Richard III.", "Some douche with an acoustic guitar.",
                       "Disco fever.", "Screaming like a maniac.", "Flying robots that kill people.",
                       "A botched circumcision.", "Jumping out at people.", "That ass.", "Demonic possession.",
                       "Vomiting mid-blowjob.", "Sneezing, farting, and cumming at the same time.",
                       "Three months in the hole.", "Having sex on top of a pizza.", "A pile of squirming bodies.",
                       "Blowing some dudes in an alley.",
                       "Getting your dick stuck in a Chinese finger trap with another dick.", "The entire Internet.",
                       "The primal, ball-slapping sex your parents are having right now.",
                       "Buying the right pants to be cool.",
                       "The thin veneer of situational causality that underlies porn.", "Velcro\u2122.",
                       "Reverse cowgirl.", "The Quesadilla Explosion Salad\u2122 from Chili\u2019s\xae.", "Nothing.",
                       "An unstoppable wave of fire ants.", "Having shotguns for legs.", "Shutting the fuck up.",
                       "The way white people is.", "A PowerPoint presentation.",
                       "Roland the Farter, flatulist to the king.", "Vietnam flashbacks.",
                       "A lamprey swimming up the toilet and latching onto your taint.", "Some kind of bird man.",
                       "Running naked through a mall, pissing and shitting everywhere.", "Gay aliens.",
                       "Not having sex.", "Prince Ali, fabulous he, Ali Ababwa.", "Sharks with legs.",
                       "Interspecies marriage.", "Moderate to severe joint pain.", "Child Protective Services.",
                       "A sex comet from Neptune that plunges the Earth into eternal sexiness.", "Exploding pigeons.",
                       "The euphoric rush of strangling a drifter.",
                       "Angelheaded hipsters burning for the ancient heavenly connection to the starry dynamo in the machinery of night.",
                       "Ambiguous sarcasm.", "The peaceful and nonthreatening rise of China.",
                       "The tiniest shred of evidence that God is real.", "Jizz.",
                       "A bunch of idiots playing a card game instead of interacting like normal humans.", "Africa.",
                       "Bouncing up and down.", "Blackula.", "A dance move that's just sex.",
                       "Unquestioning obedience.", "The secret formula for ultimate female satisfaction.",
                       "Whispering all sexy.", "Smoking crack, for instance.", "Some sort of Asian.",
                       "My worthless son.", "A kiss on the lips.", "A shiny rock that proves I love you.",
                       "A Ugandan warlord.", "Whatever a McRib is made of.", "10 Incredible Facts About the Anus.",
                       "Actual mutants with medical conditions and no superpowers.",
                       "A Native American who solves crimes by going into the spirit world.", "Sugar madness.",
                       "Three consecutive seconds of happiness.", "Party Mexicans.", "Drinking responsibly.",
                       "Crazy opium eyes.", "A hopeless amount of spiders.",
                       "The complex geopolitical quagmire that is the Middle East.", "Fucking a corpse back to life.",
                       "Lots and lots of abortions.", "A horse with no legs.", "Neil Diamond's greatest hits.",
                       "Falling into the toilet.", "My dad's dumb fucking face.", "How awesome I am.", "Dem titties.",
                       "Finally finishing off the Indians.", "My sex dungeon.",
                       "Injecting speed into one arm and horse tranquilizer into the other.", "A manhole.",
                       "No clothes on, penis in vagina.", "Snorting coke off a clown's boner.",
                       "Calculating every mannerism so as not to suggest homosexuality.", "Khakis.",
                       "A gender identity that can only be conveyed through slam poetry.", "All the single ladies.",
                       "Doo-doo.", "The size of my penis.", "A for-real lizard that spits blood from its eyes.",
                       "The safe word.", "Depression.", "An interracial handshake.", "Ass to mouth.",
                       "Almost giving money to a homeless person.", "Sports.",
                       "Stuffing a child's face with Fun Dip until he starts having fun.", "A fart.",
                       "What Jesus would do.", "A sex goblin with a carnival penis.",
                       "Grammar nazis who are also regular Nazis.", "Not believing in giraffes.",
                       "Mom's new boyfriend.", "AIDS monkeys.", "Getting eaten alive by Guy Fieri.",
                       "All these decorative pillows.", "A one-way ticket to Gary, Indiana.", "Ennui.", "Oil!",
                       "A crazy little thing called love.", "40 acres and a mule.", "Blowjobs for everyone.",
                       "Genghis Khan's DNA.", "An uninterrupted history of imperialism and exploitation.",
                       "Going to a high school reunion on ketamine.", "Slowly easing down onto a cucumber.",
                       "The eight gay warlocks who dictate the rules of fashion.",
                       "Seeing things from Hitler's perspective.", "Anal fissures like you wouldn't believe.",
                       "My first period.", "A giant powdery manbaby.", "Boring vaginal sex.", "A powered exoskeleton.",
                       "Denzel.", "Out-of-this-world bazongas.", "Butt stuff.", "The white half of Barack Obama.",
                       "Vegetarian options.", "Child support payments.", "An unforgettable quincea\xf1era.",
                       "Too much cocaine.", "The black half of Barack Obama.", "Unrelenting genital punishment.",
                       "Daddy's credit card.", "Deez nuts.", "A whole new kind of porn.",
                       "Ancient Athenian boy-fucking.", "P.F. Chang himself.",
                       "An inability to form meaningful relationships.",
                       "Ejaculating live bees and the bees are angry.", "Blackface.",
                       "A zero-risk way to make $2,000 from home.", "Getting drive-by shot.",
                       "Seeing my village burned and my family slaughtered before my eyes.", "The passage of time.",
                       "The swim team, all at once.", "Being nine years old.", "A team of lawyers.",
                       "A face full of horse cum.", "Free ice cream, yo.",
                       "Figuring out how to have sex with a dolphin.",
                       "Cutting off a flamingo's legs with garden shears.", "Being paralyzed from the neck down.",
                       "Russian super-tuberculosis.", "Being worshipped as the one true God.",
                       "Some shit-hot guitar licks.", "Changing a person's mind with logic and facts.",
                       "The Abercrombie & Fitch lifestyle.", "My boyfriend's stupid penis.",
                       "The basic suffering that pervades all of existence.", "A mouthful of potato salad.",
                       "The tiger that killed my father.", "The unbelievable world of mushrooms.",
                       "Wearing glasses and sounding smart.", "Doing the right stuff to her nipples.",
                       "Western standards of beauty.", "Having been dead for a while.", "A disappointing salad.",
                       "My dead son's baseball glove.", "Getting caught by the police and going to jail.",
                       "Giant sperm from outer space.", "A reason not to commit suicide.",
                       "Social justice warriors with flamethrowers of compassion.", "The ghost of Marlon Brando.",
                       "September 11th, 2001.", "Backwards knees."]
DEFAULT_SET.questions = ["What ended my last relationship?", "__________. It\u2019s a trap!",
                         "__________. High five, bro.", "I got 99 problems but __________ ain\u2019t one.",
                         "How am I maintaining my relationship status?",
                         "The new Chevy Tahoe. With the power and space to take __________ everywhere you go.",
                         "When Pharaoh remained unmoved, Moses called down a Plague of __________.",
                         "In the new Disney Channel Original Movie, Hannah Montana struggles with __________ for the first time.",
                         "While the United States raced the Soviet Union to the moon, the Mexican government funneled millions of pesos into research on __________.",
                         "This is the way the world ends / This is the way the world ends / Not with a bang but with __________.",
                         "Dear Abby, I\u2019m having some trouble with __________ and would like your advice.",
                         "__________. Betcha can\u2019t have just one!",
                         "A romantic, candlelit dinner would be incomplete without __________.",
                         "Coming to Broadway this season, __________: The Musical.", "What am I giving up for Lent?",
                         "What will always get you laid?",
                         "The Smithsonian Museum of Natural History has just opened an interactive exhibit on __________.",
                         "What are my parents hiding from me?",
                         "Maybe she\u2019s born with it. Maybe it\u2019s __________.",
                         "Next from J.K. Rowling: Harry Potter and the Chamber of __________.",
                         "What\u2019s that smell?", "Today on Maury: 'Help! My son is __________!'",
                         "What gives me uncontrollable gas?", "__________. That\u2019s how I want to die.",
                         "What\u2019s my anti-drug?", "War! What is it good for?",
                         "What's George W. Bush thinking about right now?",
                         "What don't you want to find in your Kung Pao chicken?",
                         "I\u2019m sorry, Professor, but I couldn\u2019t complete my homework because of __________.",
                         "What would grandma find disturbing, yet oddly charming?", "What helps Obama unwind?",
                         "A recent laboratory study shows that undergraduates have 50% less sex after being exposed to _____.",
                         "What\u2019s that sound?", "Introducing Xtreme Baseball! It's like baseball, but with ______!",
                         "What\u2019s my secret power?",
                         "When I am President of the United States, I will create the Department of __________.",
                         "After the earthquake, Sean Penn brought __________ to the people of Haiti.",
                         "Next on ESPN2: The World Series of __________.",
                         "What did the US airdrop to the children of Afghanistan?",
                         "What\u2019s a girl\u2019s best friend?", "What\u2019s the new fad diet?",
                         "What gets better with age?", "Why can\u2019t I sleep at night?",
                         "What is Batman\u2019s guilty pleasure?",
                         "Life for American Indians was forever changed when the White Man introduced them to __________.",
                         "What\u2019s Teach for America using to inspire inner city students to succeed?",
                         "I do not know with what weapons World War III will be fought, but World War IV will be fought with __________.",
                         "White people like __________.", "What did Vin Diesel eat for dinner?",
                         "In 1,000 years, when paper money is a distant memory, how will we pay for goods and services?",
                         "Why am I sticky?", "__________: Kid-tested, mother-approved.",
                         "Fun tip! When your man asks you to go down on him, try surprising him with __________ instead.",
                         "It\u2019s a pity that kids these days are all getting involved with __________.",
                         "What\u2019s there a ton of in heaven?",
                         "Alternative medicine is now embracing the curative powers of __________.",
                         "What did I bring back from Mexico?", "Why do I hurt all over?",
                         "What\u2019s the next Happy Meal\xae toy?",
                         "TSA guidelines now prohibit __________ on airplanes.",
                         "Instead of coal, Santa now gives the bad children __________.",
                         "What never fails to liven up the party?",
                         "MTV\u2019s new reality show features eight washed-up celebrities living with __________.",
                         "But before I kill you, Mr. Bond, I must show you __________.",
                         "When I am a billionaire, I shall erect a 50-foot statue to commemorate __________.",
                         "What will I bring back in time to convince people that I am a powerful wizard?",
                         "During sex, I like to think about __________.",
                         "In L.A. County Jail, word is you can trade 200 cigarettes for __________.",
                         "The class field trip was completely ruined by __________.",
                         "I get by with a little help from ______.", "Daddy, why is mommy crying?",
                         "__________: Good to the last drop.", "I drink to forget __________.",
                         "Here is the church / Here is the steeple / Open the doors / And there is __________.",
                         "What\u2019s the most emo?", "How did I lose my virginity?",
                         "The secret to a lasting marriage is communication, communication, and __________.",
                         "My plan for world domination begins with __________.",
                         "Next season on Man vs. Wild, Bear Grylls must survive in the depths of the Amazon with only __________ and his wits.",
                         "Science will never explain __________.",
                         "The CIA now interrogates enemy agents by repeatedly subjecting them to __________.",
                         "In Rome, there are whisperings that the Vatican has a secret room devoted to __________.",
                         "When all else fails, I can always masturbate to __________.",
                         "I learned the hard way that you can\u2019t cheer up a grieving friend with __________.",
                         "In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated __________.",
                         "The socialist governments of Scandinavia have declared that access to __________ is a basic human right.",
                         "In his new self-produced album, Kanye West raps over the sounds of __________.",
                         "What\u2019s the gift that keeps on giving?", "When I pooped, what came out of my butt?",
                         "In the distant future, historians will agree that __________ marked the beginning of America\u2019s decline.",
                         "What has been making life difficult at the nudist colony?",
                         "And I would have gotten away with it, too, if it hadn\u2019t been for __________.",
                         "What brought the orgy to a grinding halt?",
                         "A remarkable new study has shown that chimps have evolved their own primitive version of __________.",
                         "Your persistence is admirable, my dear Prince. But you cannot win my heart with __________ alone.",
                         "During his midlife crisis, my dad got really into __________.",
                         "My new favorite porn star is Joey '__________' McGee.",
                         "Before I run for president, I must destroy all evidence of my involvement with __________.",
                         "This is your captain speaking. Fasten your seatbelts and prepare for __________.",
                         "In his newest and most difficult stunt, David Blaine must escape from __________.",
                         "The Five Stages of Grief: denial, anger, bargaining, __________, acceptance.",
                         "Members of New York's social elite are paying thousands of dollars just to experience __________.",
                         "This month's Cosmo: 'Spice up your sex life by bringing __________ into the bedroom.'",
                         "Little Miss Muffet  Sat on a tuffet,  Eating her curds and __________.",
                         "My country, 'tis of thee, sweet land of __________.",
                         "Next time on Dr. Phil: How to talk to your child about __________.",
                         "Only two things in life are certain: death and __________.",
                         "The healing process began when I joined a support group for victims of __________.",
                         "What's harshing my mellow, man?",
                         "Charades was ruined for me forever when my mom had to act out __________.",
                         "Tonight on 20/20: What you don't know about __________ could kill you.",
                         "__________. Awesome in theory, kind of a mess in practice.",
                         "A successful job interview begins with a firm handshake and ends with __________.",
                         "And what did _you_ bring for show-and-tell?",
                         "As part of his contract, Prince won't perform without __________ in his dressing room.",
                         "As part of his daily regimen, Anderson Cooper sets aside 15 minutes for __________.",
                         "Call the law offices of Goldstein and Goldstein, because no one should have to tolerate  __________ in the workplace.",
                         "During high school, I never really fit in until I found __________ Club.",
                         "Finally! A service that delivers __________ right to your door.",
                         "Hey baby, come back to my place and I'll show you __________.",
                         "I'm not like the rest of you. I'm too rich and busy for __________.",
                         "In the seventh circle of Hell, sinners must endure __________ for all eternity.",
                         "Lovin' you is easy 'cause you're __________.",
                         "Money can't buy me love, but it can buy me __________.",
                         "My gym teacher got fired for adding __________ to the obstacle course.",
                         "The blind date was going horribly until we discovered our shared interest in __________.",
                         "To prepare for his upcoming role, Daniel Day-Lewis immersed himself in the world of __________.",
                         "Turns out that __________-Man was neither the hero we needed nor wanted.",
                         "What left this stain on my couch?",
                         "The Japanese have developed a smaller, more efficient version of __________.",
                         "I'm pretty sure I'm high right now, because I'm absolutely mesmerized by __________.",
                         "What's fun until it gets weird?", "Man, this is bullshit. Fuck __________.",
                         "2 AM in the city that never sleeps. The door swings open and *she* walks in, legs up to here. Something in her eyes tells me she's looking for __________.",
                         "I'm sorry, sir, but we don't allow __________ at the country club.",
                         "It lurks in the night. It hungers for flesh. This summer, no one is safe from __________.",
                         "As King, how will I keep the peasants in line?",
                         "Wes Anderson's new film tells the story of a precocious child coming to terms with __________.",
                         "She's up all night for good fun. I'm up all night for __________.",
                         "Alright, bros. Our frat house is condemned and all the hot slampieces are over at Gamma Phi. The time has come to commence Operation __________.",
                         "How am I compensating for my tiny penis?",
                         "Dear Leader Kim Jong Un, our village praises your infinite wisdom with a humble offering of __________.",
                         "Do not fuck with me! I am literally __________ right now.",
                         "This is the prime of my life. I'm young, hot, and full of __________.",
                         "You've seen the bearded lady! You've seen the ring of fire! Now, ladies and gentlemen, feast your eyes upon __________!",
                         "Yo' mama so fat she __________!",
                         "Hi, this is Jim from accounting. We noticed a $1,200 charge labeled '__________.' Can you explain?",
                         "Having the worst day EVER. #__________",
                         "Hi MTV! My name is Kendra, I live in Malibu, I'm into __________, and I love to have a good time.",
                         "In his farewell address, George Washington famously warned Americans about the dangers of __________.",
                         "Life's pretty tough in the fast lane. That's why I never leave the house without __________.",
                         "Don't forget! Beginning this week, Casual Friday will officially become '__________ Friday.'",
                         "What's making things awkward in the sauna?",
                         "Now in bookstores: 'The Audacity of __________,' by Barack Obama.",
                         "Armani suit: $1,000. Dinner for two at that swanky restaurant: $300. The look on her face when you surprise her with __________: priceless.",
                         "Do the Dew\xae with our most extreme flavor yet! Get ready for Mountain Dew __________!",
                         "Don't miss the action comedy of the year! One cop plays by the book. The other's only interested in one thing: __________.",
                         "Here at the Academy for Gifted Children, we allow students to explore __________ at their own pace.",
                         "Why am I broke?",
                         "Well what do you have to say for yourself, Casey? This is the third time you've been sent to the principal's office for ___________.",
                         "And today's soup is Cream of __________.",
                         "I don't mean to brag, but they call me the Michael Jordan of __________.",
                         "Help me doctor, I've got _____ in my butt!",
                         "In his new action comedy, Jackie Chan must fend off ninjas while also dealing with _____.",
                         "WHOOO! God damn I love _____!", "What killed my boner?",
                         "Do you lack energy? Does it sometimes feel like the whole world is _____? Zoloft.\xae"]

# Just testing getting cards
if __name__ == '__main__':
    set = CardSet("55HNH")
    print(set.name)
    for question in set.questions:
        print("Question: " + question)
    for answer in set.answers:
        print("Answer: " + answer)
