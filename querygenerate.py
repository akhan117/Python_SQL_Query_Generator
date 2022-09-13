import copy
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

# Book 1, Book 2, Book 3, Enemy 1, Enemy 2, Enemy 3, Weekly, Mora, Crown
talent_levels = {1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 2: [3, 0, 0, 6, 0, 0, 0, 12500, 0],
                 3: [0, 2, 0, 0, 3, 0, 0, 17500, 0],
                 4: [0, 4, 0, 0, 4, 0, 0, 25000, 0],
                 5: [0, 6, 0, 0, 6, 0, 0, 30000, 0],
                 6: [0, 9, 0, 0, 9, 0, 0, 37500, 0],
                 7: [0, 0, 4, 0, 0, 4, 1, 120000, 0],
                 8: [0, 0, 6, 0, 0, 6, 1, 260000, 0],
                 9: [0, 0, 12, 0, 0, 9, 2, 450000, 0],
                 10: [0, 0, 16, 0, 0, 12, 2, 700000, 1]}

# sliver, shard, chunk, gem, enemy 1, enemy 2, enemy 3, local, boss, Mora]
ascension_levels = {20: [1, 0, 0, 0, 3, 0, 0, 3, 0, 20000 + 24200],
                    40: [0, 3, 0, 0, 15, 0, 0, 10, 2, 40000 + 115800],
                    50: [0, 6, 0, 0, 0, 12, 0, 20, 4, 60000 + 116000],
                    60: [0, 0, 3, 0, 0, 18, 0, 30, 8, 80000 + 171000],
                    70: [0, 0, 6, 0, 0, 0, 12, 45, 12, 100000 + 239200],
                    80: [0, 0, 0, 6, 0, 0, 24, 60, 20, 120000 + 322400]}


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


def dict_append(appender, appendee):
    if appender:
        appender.append(appendee)
    else:
        appender = [appendee]


def ascension(c_info, ac_info, acl, a_suc):
    if c_info["Element"] != "Unknown":
        gem_type = gem_relations[c_info["Element"]]
        ac_info.setdefault(gem_type + " Sliver", []).append(a_suc[acl][0])
        ac_info.setdefault(gem_type + " Fragment", []).append(a_suc[acl][1])
        ac_info.setdefault(gem_type + " Chunk", []).append(a_suc[acl][2])
        ac_info.setdefault(gem_type + " Gemstone", []).append(a_suc[acl][3])

    if c_info["Common Materials"] != "Unknown":
        com_mat = common_material_relations[c_info["Common Materials"]]
        for n, i in enumerate(com_mat):
            ac_info.setdefault(i, []).append(a_suc[acl][4 + n])

    if c_info["Local Materials"] != "Unknown":
        ac_info.setdefault(c_info["Local Materials"], []).append(a_suc[acl][7])

    if c_info["World Boss Materials"] != "Unknown":
        ac_info.setdefault(c_info["World Boss Materials"], []).append(a_suc[acl][8])

    ac_info.setdefault("Mora", []).append(a_suc[acl][9])


def talents(c_info, t_info, tl, t_suc):
    if c_info["Talent Materials"] != "Unknown":
        talent_type = c_info["Talent Materials"]
        t_info.setdefault("Teachings of " + talent_type, []).append(t_suc[tl][0])
        t_info.setdefault("Guide to " + talent_type, []).append(t_suc[tl][1])
        t_info.setdefault("Philosophies of " + talent_type, []).append(t_suc[tl][2])

    if c_info["Common Materials"] != "Unknown":
        com_mat = common_material_relations[c_info["Common Materials"]]
        for n, i in enumerate(com_mat):
            t_info.setdefault(i, []).append(t_suc[tl][3 + n])

    if c_info["Weekly Boss Materials"] != "Unknown":
        t_info.setdefault(c_info["Weekly Boss Materials"], []).append(t_suc[tl][6])

    t_info.setdefault("Mora", []).append(t_suc[tl][7])
    t_info.setdefault("Crowns", []).append(t_suc[tl][8])


# def level_90_ascension(c_info, ac_info, t_info):
#     a_cum = ascension_addition()
#     t_cum = talent_addition()
#     a_suc = ascension_levels
#     c_suc = talent_levels
#
#     if c_info["Element"] != "Unknown":
#         gem_type = gem_relations[c_info["Element"]]
#         ac_info[gem_type + " Sliver"] = 1
#         ac_info[gem_type + " Fragment"] = 9
#         ac_info[gem_type + " Chunk"] = 9
#         ac_info[gem_type + " Gemstone"] = 6
#
#     if c_info["Talent Materials"] != "Unknown":
#         talent_type = c_info["Talent Materials"]
#         t_info["Teachings of " + talent_type] = 9
#         t_info["Guide to " + talent_type] = 63
#         t_info["Philosophies of " + talent_type] = 114
#
#     if c_info["Common Materials"] != "Unknown":
#         com_mat = common_material_relations[c_info["Common Materials"]]
#         com_mat_num_asc = [18, 30, 36]
#         com_mat_num_tal = [6 * 3, 22 * 3, 31 * 3]
#         for n, i in enumerate(com_mat):
#             ac_info[i] = com_mat_num_asc[n]
#             t_info[i] = com_mat_num_tal[n]
#
#     if c_info["Local Materials"] != "Unknown":
#         ac_info[c_info["Local Materials"]] = 168
#
#     if c_info["World Boss Materials"] != "Unknown":
#         ac_info[c_info["World Boss Materials"]] = 46
#
#     if c_info["Weekly Boss Materials"] != "Unknown":
#         t_info[c_info["Weekly Boss Materials"]] = 18
#
#     ac_info["Mora"] = 1673400 + 420000
#     t_info["Mora"] = 3 * 1652500
#     t_info["Crown of Insight"] = 3


def print_dict(char_dict):
    print()
    for var in char_dict:
        print(str(var) + ": " + str(char_dict[var]))

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


def talent_addition():
    talent_cumulative = {}
    talent_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 11):
        for j in range(0, 9):
            talent_sum[j] = talent_sum[j] + talent_levels[i][j]

        talent_cumulative[i] = copy.copy(talent_sum)
    return talent_cumulative


def ascension_addition():
    ascension_cumulative = {}
    ascension_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ascensions = [20, 40, 50, 60, 70, 80]
    for i in ascensions:
        for j in range(0, 10):
            ascension_sum[j] = ascension_sum[j] + ascension_levels[i][j]

        ascension_cumulative[i] = copy.copy(ascension_sum)
    return ascension_cumulative


def dict_populate(c_info, ac_info, t_info, ac_info_cum, t_info_cum):
    insert_name(c_info)
    insert_weapon(c_info)
    insert_element(c_info)
    insert_location(c_info)
    insert_talents(c_info)
    insert_local_mat(c_info)
    insert_common_mat(c_info)
    insert_world_boss_drop(c_info)
    insert_weekly_boss_drop(c_info)

    asc = [20, 40, 50, 60, 70, 80]
    for i in asc:
        ascension(c_info, ac_info, i, ascension_levels)
        ascension(c_info, ac_info_cum, i, ascension_addition())

    for i in range(1, 11):
        talents(c_info, t_info, i, talent_levels)
        talents(c_info, t_info_cum, i, talent_addition())

    # level_90_ascension(c_info, ac_info, t_info)
    print_dict(c_info)

    print("Ascension Information")
    print_dict(ac_info)
    print("Cumulative Ascension Information")
    print_dict(ac_info_cum)
    print("Talent Information")
    print_dict(t_info)
    print("Cumulative Talent Information")
    print_dict(t_info_cum)

    inp = input("Are these correct? (y/n)")
    if inp != 'y':
        raise Exception("Then do it again")
    return [c_info, ac_info, ac_info_cum, t_info, t_info_cum]


if __name__ == '__main__':
    character_info = {}
    ascension_info = {}
    talent_info = {}
    ascension_info_cum = {}
    talent_info_cum = {}

    dict_populate(character_info, ascension_info, talent_info, ascension_info_cum, talent_info_cum)
