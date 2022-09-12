import difflib as dl

weapons = ["sword", "claymore", "polearm", "bow", "catalyst"]

elements = ["pyro", "hydro", "anemo", "electro", "dendro", "cryo", "geo"]

nations = ["monstadt", "liyue", "inazuma", "sumeru", "fontaine", "natlan", "snezhnaya", "khaenriah"]

talents_books = ["freedom", "resistance", "ballad", "prosperity", "diligence", "gold", "transience",
                 "elegance", "light", "admonition", "ingenuity", "praxis"]

local_material = ["wolfhook", "valberry", "cecilia", "windwheel aster", "philanemo mushroom", "jueyun chili",
                  "noctilucous jade", "silk flower", "glaze lily", "qingxin", "starconch", "violetgrass",
                  "small lamp grass", "calla lily", "dandelion seed", "cor lapis", "onikabuto", "sakura bloom",
                  "crystal marrow", "dendrobium", "naku weed", "sea ganoderma", "sango pearl", "amakumo fruit",
                  "fluorescent fungus", "rukkhashava mushrooms", "padisarah", "nilotpala lotus", "kalpalata lotus",
                  "redcrest", "scarab"]

common_material = ["slime condensate", "damaged mask", "divining scroll", "firm arrowhead", "recruit's insignia",
                   "treasure hoarder insignia", "whopperflower nectar", "old handguard", "spectral husk",
                   "fungal spores", "faded red satin"]

world_boss_drops = ["hurricane seed", "lightning prism", "basalt pillar", "hoarfrost core", "everflame seed",
                    "cleansing heart", "juvenile jade", "crystalline bloom", "marionette core", "perpetual heart",
                    "smoldering pearl", "dew of repudiation", "storm beads", "riftborn regalia",
                    "dragonheir's false fin", "runic fang", "majestic hooked beak", "thunderclap fruitcore",
                    "perpetual caliber", "light guiding tetrahedron"]

weekly_boss_drops = ["dvalin's plume", "dvalin's claw", "dvalin's sigh", "tail of boreas", "ring of boreas",
                     "spirit locket of boreas", "tusk of monoceros caeli", "shard of a foul legacy",
                     "shadow of the warrior", "dragon lord's crown", "bloodjade branch", "gilded scale",
                     "molten moment", "hellfire butterfly", "ashen heart", "mudra of the malefic general",
                     "tears of the calamitous god", "the meaning of aeons"]

relations = {'Weapon': weapons,
             'Element': elements,
             'Nationality': nations,
             'Talent Materials': talents_books,
             'Local Materials': local_material,
             'Common Materials': common_material,
             'Weekly Boss Materials': weekly_boss_drops,
             'World Boss Materials': world_boss_drops
             }

gem_relations = {'Pyro': 'Agnidus Agate',
                 'Hydro': 'Varunada Lazurite',
                 'Anemo': ' Vayuda Turquoise',
                 'Electro': 'Vajrada Amethyst',
                 'Dendro': 'Nagadus Emerald',
                 'Cryo': 'Shivada Jade',
                 'Geo': 'Prithvia Topaz',
                 }

common_material_relations = {'Slime Condensate': ['Slime Condensate', 'Slime Secretions', 'Slime Concentrate'],
                             'Damaged Mask': ['Damaged Mask', 'Stained Mask', 'Ominous Mask'],
                             'Divining Scroll': ['Divining Scroll', 'Sealed Scroll', 'Forbidden Curse Scroll'],
                             'Firm Arrowhead': ['Firm Arrowhead', 'Sharp Arrowhead', 'Weathered Arrowhead'],
                             "Recruit'S Insignia": ["Recruit's Insignia", "Sergeant's Insignia",
                                                    "Lieutenant's Insignia"],
                             'Treasure Hoarder Insignia': ['Treasure Hoarder Insignia', 'Silver Raven Insignia',
                                                           'Gold Raven Insignia'],
                             'Whopperflower Nectar': ['Whopperflower Nectar', 'Shimmering Nectar', 'Energy Nectar'],
                             'Old Handguard': ['Old Handguard', 'Kageuchi Handguard', 'Famed Handguard'],
                             'Spectral Husk': ['Spectral Husk', 'Spectral Heart', 'Spectral Nucleus'],
                             'Fungal Spores': ['Fungal Spores', 'Luminescent Pollen', 'Crystalline Cyst Dust'],
                             'Fungal Red Satin': ['Fungal Red Satin', 'Trimmed Red Silk', 'Rich Red Brocade'],
                             }


def insert_name(c_info):
    c_info['Name'] = input("What's the characters Name?: ").title()


def insert_weapon(c_info):
    print("What Weapon does this character use?")
    print_list(weapons)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(weapons, numb[0])
        close_insert(c_info, inp, "Weapon")

    else:
        if inp == "lance" or inp == "spear":
            inp = "polearm"
        close_insert(c_info, inp, "Weapon")


def insert_element(c_info):
    print("What's the characters Element?")
    print_list(elements)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(elements, numb[0])
        close_insert(c_info, inp, "Element")

    else:
        close_insert(c_info, inp, "Element")


def insert_location(c_info):
    print("What's the characters nationality?")
    print_list(nations)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(nations, numb[0])
        close_insert(c_info, inp, "Nationality")

    else:
        close_insert(c_info, inp, "Nationality")


def insert_talents(c_info):
    print("What Talent Materials does the character use?")
    print_list(talents_books)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(talents_books, numb[0])
        close_insert(c_info, inp, "Talent Materials")

    else:
        close_insert(c_info, inp, "Talent Materials")


def insert_local_mat(c_info):
    print("What Local Materials does the character use?")
    print_list(local_material)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(local_material, numb[0])
        close_insert(c_info, inp, "Local Materials")

    else:
        close_insert(c_info, inp, "Local Materials")


def insert_common_mat(c_info):
    print("What Common Materials does the character use?")
    print_list(common_material)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(common_material, numb[0])
        close_insert(c_info, inp, "Common Materials")

    else:
        close_insert(c_info, inp, "Common Materials")


def insert_world_boss_drop(c_info):
    print("What World Boss Drops does the character use?")
    print_list(world_boss_drops)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(world_boss_drops, numb[0])
        close_insert(c_info, inp, "World Boss Materials")

    else:
        close_insert(c_info, inp, "World Boss Materials")


def insert_weekly_boss_drop(c_info):
    print("What Weekly Boss Drops does the character use?")
    print_list(weekly_boss_drops)
    inp = input('\n').casefold()

    numb = [int(s) for s in inp.split() if s.isdigit()]
    if numb:
        inp = match_num_list(weekly_boss_drops, numb[0])
        close_insert(c_info, inp, "Weekly Boss Materials")

    else:
        close_insert(c_info, inp, "Weekly Boss Materials")


def close_insert(c_info, inp, key):
    if inp in relations[key]:
        c_info[key] = inp.title()

    elif inp == "":
        c_info[key] = "Unknown"

    else:
        close = dl.get_close_matches(inp, relations[key])

        for cap in close:
            close_cap = cap.title()
            ans = input("Sorry, did you mean " + close_cap + "? (y/n): ")
            if ans == 'y':
                c_info[key] = close_cap
                return

            else:
                continue

        raise Exception("Invalid " + key + "!'")


def level_90_ascension(c_info, ac_info):
    if c_info["Element"] != "Unknown":
        gem_type = gem_relations[c_info["Element"]]
        ac_info[gem_type + " Sliver"] = (1, "Elemental Jewel", 2)
        ac_info[gem_type + " Fragment"] = (9, "Elemental Jewel", 3)
        ac_info[gem_type + " Chunk"] = (9, "Elemental Jewel", 4)
        ac_info[gem_type + " Gemstone"] = (6, "Elemental Jewel", 5)

    if c_info["Talent Materials"] != "Unknown":
        talent_type = c_info["Talent Materials"]
        ac_info["Teachings of " + talent_type] = (9, "Talent Book", 2)
        ac_info["Guide to " + talent_type] = (63, "Talent Book", 3)
        ac_info["Philosophies of " + talent_type] = (114, "Talent Book", 4)

    if c_info["Common Materials"] != "Unknown":
        com_mat = common_material_relations[c_info["Common Materials"]]
        com_mat_num = [36, 96, 129]
        for n, i in enumerate(com_mat):
            ac_info[i] = (com_mat_num[n], "Enemy Drop",  n + 1)

    if c_info["Local Materials"] != "Unknown":
        ac_info[c_info["Local Materials"]] = (168, "Local Speciality", 1)

    if c_info["World Boss Materials"] != "Unknown":
        ac_info[c_info["World Boss Materials"]] = (46, "World Boss Material", 4)

    if c_info["Weekly Boss Materials"] != "Unknown":
        ac_info[c_info["Weekly Boss Materials"]] = (18, "Weekly Boss Drop", 5)

    ac_info["Mora"] = (1673400 + (3 * 1652500) + 420000, "Mora", 3)
    ac_info["Crown of Insight"] = (3, "Crown", 5)


def print_dict(char_dict):
    print()
    for var in char_dict:
        print(var + ": " + str(char_dict[var]))

    print()


def print_list(mat_list):
    for i, mat in enumerate(mat_list, 1):
        print(str(i) + "." + mat.title())


def match_num_list(mat_list, num):
    # if num == 1 and len(mat_list) == 1:
    #     return mat_list[0]

    for i, mat in enumerate(mat_list, 1):
        if num == i:
            return mat

    raise Exception("Number was not between the confines of 1 and " + str(i))


def dict_populate(c_info, ac_info):

    insert_name(c_info)
    insert_weapon(c_info)
    insert_element(c_info)
    insert_location(c_info)
    insert_talents(c_info)
    insert_local_mat(c_info)
    insert_common_mat(c_info)
    insert_world_boss_drop(c_info)
    insert_weekly_boss_drop(c_info)
    level_90_ascension(c_info, ac_info)
    print_dict(c_info)
    print_dict(ac_info)

    inp = input("Are these correct? (y/n)")
    if inp != 'y':
        raise Exception("Then do it again")
    return [c_info, ac_info]


if __name__ == '__main__':
    c1_info = {}
    ac1_info = {}
    dict_populate(c1_info, ac1_info)