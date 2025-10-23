import random
def create_card(rank:str,suite:str) -> dict:
    d = {}
    d["rank"] = rank
    d["suite"] = suite
    ls = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    for k in ls:
        if k == rank:
            d["value"] = ls[k]
            return d

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"
    else:
        return "war"

data = []
def create_deck() -> list[dict]:
    suite = ["H", "C", "D", "S"]
    dictionary = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    ls = []
    for i in suite:
        for v in dictionary:
            d = {"rank": "A", "suite": "S", "value": 14}
            d["rank"] = v
            d["suite"] = i
            d["value"] = dictionary[v]
            ls.append(d)
    global data
    data = ls
    return ls
create_deck()


def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        index1 = random.randint(1,52)
        index2 = random.randint(1, 52)
        if index1 == index2:
            print("pick again")
        else:
            print(f"index 1 = {index1} index 2 = {index2}")
            temp_index = index1
            data[index2] = data[index1]
            data[temp_index] = data[index2]
            return data

