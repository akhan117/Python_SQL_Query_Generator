import pymssql as sq
import querygenerate as qg
import difflib as dl


def select(cursor_m, tables):
    for table in tables:
        print()
        print("This is " + table)
        query = "select * from " + table
        print(query)
        cursor_m.execute(query)
        row = cursor_m.fetchone()

        try:
            while row:
                print(row)
                row = cursor_m.fetchone()
        except:
            print("Yarghh")

        save_query(query, "select " + table)


def create_ascension_table(c_info, ac_info, t_name, cursor_m):
    name = c_info["Name"].replace(" ", "_")

    columns = "(m_name varchar(255), asc_20 int, asc_40 int, asc_50 int, asc_60 int, asc_70 int, asc_80 int)"

    query = "create table " + t_name + " " + columns

    cursor_m.execute(query)

    for i in ac_info:
        ac = ac_info[i]
        query2 = "insert into " + t_name + " (m_name, asc_20, asc_40, asc_50, asc_60, asc_70, asc_80) " \
                                           " values ('" + i + "', " + str(ac[0]) + ", " + str(ac[1]) + ", " \
                 + str(ac[2]) + ", " + str(ac[3]) + ", " + str(ac[4]) + ", " + str(ac[5]) + ")"

        cursor_m.execute(query2)
        query = query + '\n' + query2

    f_name = "create " + t_name
    save_query(query, f_name)


def create_talent_table(c_info, t_info, t_name, cursor_m):
    name = c_info["Name"].replace(" ", "_")

    columns = "(m_name varchar(255), t1 int, t2 int, t3 int, t4 int, t5 int, t6 int, t7 int, t8 int, t9 int, t10 int)"

    query = "create table " + t_name + " " + columns

    cursor_m.execute(query)

    for i in t_info:
        t = t_info[i]
        query2 = "insert into " + t_name + " (m_name, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10) " \
                                           " values ('" + i + "', " + str(t[0]) + ", " + str(t[1]) + ", " \
                 + str(t[2]) + ", " + str(t[3]) + ", " + str(t[4]) + ", " + str(t[5]) + ", " + str(t[6]) + ", " \
                 + str(t[7]) + ", " + str(t[8]) + ", " + str(t[9]) + ")"

        cursor_m.execute(query2)
        query = query + '\n' + query2

    f_name = "create " + t_name
    save_query(query, f_name)


def create_tables(cursor_m):
    c_info, ac_info, ac_cum, t_info, t_cum = qg.dict_populate({}, {}, {}, {}, {})

    name = c_info["Name"].replace(" ", "_")
    t1_name = name + "_Ascension_Materials"
    create_ascension_table(c_info, ac_info, t1_name, cursor_m)

    t2_name = name + "_Cumulative_Ascension_Materials"
    create_ascension_table(c_info, ac_cum, t2_name, cursor_m)

    t3_name = name + "_Talent_Materials"
    create_talent_table(c_info, t_info, t3_name, cursor_m)

    t4_name = name + "_Cumulative_Talent_Materials"
    create_talent_table(c_info, t_cum, t4_name, cursor_m)


def create_table(cursor_m):
    c_info, ac_info, t_info, ac_cum, t_cum = qg.dict_populate({}, {}, {}, {}, {})
    qg.print_dict(c_info)
    qg.print_dict(ac_info)
    qg.print_dict(t_info)

    name = c_info["Name"].replace(" ", "_")
    table_name = name + "_" + c_info["Nationality"] + "_" + c_info["Weapon"] + "_Materials"
    print(table_name)
    columns = "(Material_Name varchar(255), Number_Needed int, " \
              "Material_Type varchar(255), Material_Rarity int)"

    query = "create table " + table_name + " " + columns

    print(query)
    cursor_m.execute(query)
    for i in ac_info:
        query2 = "insert into " + table_name + " (Material_Name, Number_Needed, Material_Type, Material_Rarity)" \
                                               " values ('" + i + "'," + str(ac_info[i][0]) + ", '" + ac_info[i][1] + \
                 "', " + str(ac_info[i][2]) + ")"
        cursor_m.execute(query2)
        query = query + '\n' + query2

    f_name = "create " + table_name
    save_query(query, f_name)


def drop_table(cursor_m, tables):
    for table in tables:
        query = "drop table " + table
        print(query)
        cursor_m.execute(query)
        save_query(query, "drop " + table)


def table_choose():
    table = ""
    print("Which table would you like to work on? (Tables may take a while to show up.)")
    cursor.execute("select * from sys.tables")
    row = cursor.fetchone()
    tables = []
    count = 1
    while row:
        print(str(count) + ": " + row[0])
        tables.append(row[0])
        row = cursor.fetchone()
        count += 1

    inp2 = input("Which table: ")

    numb = [int(s) for s in inp2.split() if s.isdigit()]

    if numb:
        table = qg.match_num_list(tables, numb[0])

    else:
        if inp2 in tables:
            table = inp2
        else:
            first_names = [(x.split('_'))[0] for x in tables]
            close = dl.get_close_matches(inp2, first_names)

            close_tables = []
            for i in close:
                for j in tables:
                    if i.casefold() in j.casefold():
                        close_tables.append(j)

            for cap in close_tables:
                ans = input("Sorry, did you mean " + cap + "? (y/n): ")
                if ans == 'y':
                    table = cap
                    break

                elif cap == close_tables[-1]:
                    raise Exception("Invalid Table!")

                else:
                    continue

    if table == "":
        raise Exception("Table name cannot be empty")
    return table


def tables_choose():
    print("Which Character? (Tables may take a while to show up.)")
    cursor.execute("select * from sys.tables")
    row = cursor.fetchone()
    tables = []
    tables_trunc = []
    count = 1
    while row:
        r_name = (row[0].split('_'))[0]
        tables_trunc.append(r_name)
        tables.append(row[0])
        row = cursor.fetchone()
        count += 1

    tables_trunc = list(set(tables_trunc))
    qg.print_list(tables_trunc)
    inp_m = input()
    sel = qg.match_num_list(tables_trunc, int(inp_m))

    cursor.execute("select * from sys.tables")
    row = cursor.fetchone()
    tables = []
    while row:
        r_name = (row[0].split('_'))[0]
        if r_name == sel:
            tables.append(row[0])
        row = cursor.fetchone()

    return tables


def save_query(query, f_name):
    with open("Queries/" + f_name + ".sql", "w+") as f:
        f.write("use " + database + '\n')
        f.write(query)


if __name__ == '__main__':
    database = r'test'
    conn = sq.connect(host=r'DESKTOP-202JPF7\TESTINST', user=r'DESKTOP-202JPF7\EPIR1001',
                      password=r'2022', database=database)
    cursor = conn.cursor()

    inp = input("1. Create a Character Entry, 2. Drop, 3. Select, 4. Advanced Access :")

    if inp == '1':
        create_tables(cursor)

    elif inp == '2':
        table_names = tables_choose()
        qg.print_list(table_names)
        confirm = input("Are you sure you want to delete these table(s)?(y/n): ")
        if confirm == 'y':
            drop_table(cursor, table_names)

    elif inp == '3':
        table_names = tables_choose()
        print("Selected: ")
        qg.print_list(table_names)
        select(cursor, table_names)

    elif inp == '4':
        tables_names = tables_choose()
        print("What ascension level? (Enter the Ascension number)")
        asc_p = ("Ascension 1: (20+)", "Ascension 2: (40+)", "Ascension 3: (50+)", "Ascension 4: (60+)",
                 "Ascension 5: (70+)", "Ascension 6: (80+)")
        asc_i = (20, 40, 50, 60, 70, 80,)
        qg.print_list(asc_p)
        inp_m = input()
        sel_m = qg.match_num_list(asc_i, int(inp_m))
        print("asc_" + str(sel_m))

        t_lev = input("What talent levels? (e.g, 10-9-10 or 6, 10, 10): ")
        if '-' in t_lev:
            t_lev = t_lev.split('-')
        elif ',' in t_lev:
            t_lev = t_lev.split(',')

        t_lev = ['t' + x.strip() for x in t_lev]
        print(t_lev)

    conn.commit()
    conn.close()
    # print("Which table would you like to work on?")
    # cursor.execute("select * from sys.tables")
    # row = cursor.fetchone()
    # while row:
    #     print(row)
    #     row = cursor.fetchone()
    #
    # print("What would you like to do? 1. Insert, 2. Delete 3. Update")
    # inp = input()
    # if inp == "1":
    #     print("Insert 1. No of Mats, 2. Mat Name, 3. Mat Location, 4. Mat Rarity")
    #     noMat = input()
    #     matName = input()
    #     matLocation = input()
    #     matRarity = input()
    #
    #     insert(cursor, noMat, matName, matLocation, matRarity)
    # elif inp == "2":
    #     print("Delete what Mat Name?")
    #     toDel = input()
    #     delete(cursor, toDel)
    #
    # select(cursor)
    #
