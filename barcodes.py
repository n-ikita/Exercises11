import pandas as pd


class Ean13:
    country_by_code = {}
    __df = pd.read_excel('ean13.xlsx')

    for index, row in __df.iterrows():

        if not isinstance(row['code'], int):

            code1, code2 = map(int, row['code'].split('– '))
            for i in range(code1, code2+1):
                country_by_code[i] = row['country']
        else:
            country_by_code[int(row['code'])] = row['country']
