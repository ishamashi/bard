from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()

token1 = "aQhsCCtwb3nGUYZ2d4MkzkLlqIt27UAzT7NWD1DuHUVdVfQONds0Jc67al6H9mIJYo_s8w." # os.getenv("BARD_API_KEY")

bard = Bard(token = token1)
promt = input("Tanya sama mamang bard:")

result = bard.get_answer(promt)
print(result)

# os.environ["_BARD_API_KEY"] = "ZwhsCEpab-GJiz4Aa4ogdrEtO3Rtsvwujz3oMIUnZlesERE0w3SS6nHGtmY-uzOubC7q-Q."

# message = input("Masukan promt:")
# print(Bard().get_answer(str(message)))