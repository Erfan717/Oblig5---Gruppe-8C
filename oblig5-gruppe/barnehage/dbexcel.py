# dbexcel module
import pandas as pd



kgdata = pd.ExcelFile('kgdata.xlsx')
barnehage = pd.read_excel(kgdata, 'barnehage', index_col=0)
forelder = pd.read_excel(kgdata, 'foresatt', index_col=0)
barn = pd.read_excel(kgdata, 'barn', index_col=0)
soknad = pd.read_excel(kgdata, 'soknad', index_col=0)
statistikk = pd.read_excel(kgdata, 'statistikk', index_col=0)



# Forutsetter at barnehagedataene er lagret i en sheet med navn "barnehage" i kgdata.xlsx
barnehage_df = pd.read_excel('kgdata.xlsx', sheet_name='barnehage')

def select_ledige_plasser(barnehage_navn):
    """
    Returnerer antall ledige plasser for en gitt barnehage.
    :param barnehage_navn: Navnet på barnehagen vi vil sjekke.
    :return: Antall ledige plasser eller 0 hvis barnehagen ikke finnes.
    """
    barnehage = barnehage_df[barnehage_df['barnehage_navn'] == barnehage_navn]
    if not barnehage.empty:
        return int(barnehage.iloc[0]['barnehage_ledige_plasser'])
    else:
        return 0



"""
Referanser
[] https://www.geeksforgeeks.org/list-methods-python/
"""