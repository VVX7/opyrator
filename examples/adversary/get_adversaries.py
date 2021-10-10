from opyrator.api import API

client = API(url="http://localhost:8888",
             key="operator_session_key_here",
             ssl=False)

adversaries = client.get_adversaries()

for adversary in adversaries:
    print(adversary.to_json(sort_keys=True, indent=4))
