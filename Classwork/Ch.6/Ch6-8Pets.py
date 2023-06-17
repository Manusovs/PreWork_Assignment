Pili={"name":"Pili",
      "kind":"Miniature Rat Terrier",
      "owner":"Paola"}
Brazil={"name":"Brazil",
        "kind":"Chihuahua",
      "owner":"Scott"}
Hakuna={"name":"Hakuna",
        "kind":"Laborador Retriever",
      "owner":"SAVE"}
pets = [Pili, Brazil, Hakuna]

for pet in pets:
    print(pet["name"] + ":\n\tKind: " + pet["kind"] + ":\n\tOnwer: " + pet["owner"])

