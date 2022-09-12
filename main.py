import pymssql as sq
import querygenerate as qg
import difflib as dl


def select(cursor, table):
    query = "select * from " + table
    print(query)
    cursor.execute(query)
    row = cursor.fetchone()

    try:
        while row:
            print(row)
            row = cursor.fetchone()
    except:
        print("Yarghh")

    save_query(query, "select " + table)


def delete(cursor, matName):
    cursor.execute("delete from Nmats where MatName = '" + matName + "'")
    try:
        cursor.fetchone()
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
    except:
        print("No return statement")


def create_table(cursor):
    c_info, ac_info = qg.dict_populate({}, {})
    qg.print_dict(c_info)
    qg.print_dict(ac_info)
    name = c_info["Name"].replace(" ", "_")
    table_name = name + "_" + c_info["Nationality"] + "_" + c_info["Weapon"] + "_Materials"
    print(table_name)

    columns = "(Material_Name varchar(255), Number_Needed int)"

    query = "create table " + table_name + " " + columns

    print(query)
    cursor.execute(query)
    for i in ac_info:
        query2 = "insert into " + table_name + " (Material_Name, Number_Needed) values ('" + i + "'," + str(
                ac_info[i]) + ")"
        cursor.execute(query2)
        query = query + '\n' + query2

    f_name = "create " + table_name
    save_query(query, f_name)


def drop_table(cursor, table):
    query = "drop table " + table
    print(query)
    cursor.execute(query)
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


def save_query(query, f_name):
    with open("Queries/" + f_name + ".sql", "w+") as f:
        f.write("use " + database + '\n')
        f.write(query)


if __name__ == '__main__':
    database = r'test'
    conn = sq.connect(host=r'DESKTOP-202JPF7\TESTINST', user=r'DESKTOP-202JPF7\EPIR1001',
                      password=r'2022', database=database)
    cursor = conn.cursor()

    inp = input("1. Create, 2. Drop, 3. Select :")

    if inp == '1':
        create_table(cursor)
    elif inp == '2':
        table_name = table_choose()
        print("Selected: " + table_name)
        confirm = input("Are you sure you want to delete this table?(y/n): ")
        if confirm == 'y':
            drop_table(cursor, table_name)

    elif inp == '3':
        table_name = table_choose()
        print("Selected: " + table_name)
        select(cursor, table_name)

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
