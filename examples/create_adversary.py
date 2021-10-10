from opyrator.api import API, Adversary

if __name__ == '__main__':
    client = API(url="http://localhost:8888",
                 key="operator_session_key_here",
                 ssl=False)

    adversary = Adversary()
    adversary.id = "5a1af2c9-8b39-48c6-bc5f-a87653b0cb2c"
    adversary.name = "File Hunter 2"
    adversary.ttps = ["90c2efaa-8205-480d-8bb6-61d90dbaf81b",
                      "6469befa-748a-4b9c-a96d-f191fde47d89",
                      "4e97e699-93d7-4040-b5a3-2e906a58199e",
                      "300157e5-f4ad-4569-b533-9d1fa0e74d74"]

    print(client.create_adversary(adversary))
