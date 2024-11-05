# initiate script
import pandas as pd
from kgmodel import Barnehage

def initiate_db(db_name):
    kg1 = Barnehage(1,"Askeladden barnehage",50,15)
    kg2 = Barnehage(2,"Auglandstjønn barnehage",25,2)
    kg3 = Barnehage(3,"Bamsebo barnehage",35,4)
    kg4 = Barnehage(4,"Bergtorasvei barnehage",12,0)
    kg5 = Barnehage(5,"Birkelid barnehage",15,5)
    kg6 = Barnehage(6,"Bjørnungen barnehage",10,0)
    kg7 = Barnehage(7,"Eventyrheia barnehage",40,6)
    kg8 = Barnehage(7,"Finsland barnehage",40,6)
    kg9 = Barnehage(7,"Havlimyra barnehage",40,6)
    kg10 = Barnehage(7,"Havåsen barnehage",40,6)
    kg11 = Barnehage(7,"Hellemyr barnehage",40,6)
    kg12 = Barnehage(7,"Hellinga barnehage",40,6)
    kg13 = Barnehage(7,"Jordbærveien barnehage",40,6)
    kg14 = Barnehage(7,"Karuss barnehage",40,6)
    kg15 = Barnehage(7,"Linerla barnehage",40,6)
    kg16 = Barnehage(7,"Lømslands vei barnehage",40,6)
    kg17 = Barnehage(7,"Mosby oppvekstsenter",40,6)
    kg18 = Barnehage(7,"Møllestua barnehage",40,6)
    kg19 = Barnehage(7,"Odderøya barnehage",40,6)
    kg20 = Barnehage(7,"Ravndalen barnehage",40,6)
    kg21 = Barnehage(7,"Roligheden gård barnehage",40,6)
    kg22 = Barnehage(7,"Sjøstjerna barnehage",40,6)
    kg23 = Barnehage(7,"Skårungen barnehage",40,6)
    kg24 = Barnehage(7,"Solstrålen barnehage",40,6)
    kg25 = Barnehage(7,"Søm barnehage",40,6)
    kg26 = Barnehage(7,"Taremareskogen barnehage",40,6)
    kg27 = Barnehage(7,"Tinnstua barnehage",40,6)
    kg28 = Barnehage(7,"Torvmoen barnehage",40,6)
    kg29 = Barnehage(7,"Trollhaugen barnehage",40,6)
    kg30 = Barnehage(7,"Tunballen barnehage",40,6)
    kg31 = Barnehage(7,"Veslefrikk barnehage",40,6)
    kg32 = Barnehage(7,"Voietun barnehage",40,6)
    kg33 = Barnehage(7,"Øvre Slettheia barnehage",40,6)
    kg34 = Barnehage(7,"Åros barnehage",40,6)
    
    barnehage_liste = [kg1, kg2, kg3, kg4, kg5, kg6, kg7, kg8, kg9, kg10, kg11, kg12, kg13, kg14, kg15, kg16, kg17, kg18, kg19, kg20, kg21, kg22, kg23, kg24, kg25, kg26, kg27, kg28, kg29, kg30, kg31, kg32, kg33, kg34]
    
    
    kolonner_forelder =  ['foresatt_id',
                          'foresatt_navn',
                          'foresatt_adresse',
                          'foresatt_tlfnr',
                          'foresatt_pnr']
    kolonner_barnehage = ['barnehage_id',
                          'barnehage_navn',
                          'barnehage_antall_plasser',
                          'barnehage_ledige_plasser']
    kolonner_barn = ['barn_id',
                     'barn_pnr']
    kolonner_soknad = ['sok_id',
                       'foresatt_1',
                       'foresatt_2',
                       'barn_1',
                       'fr_barnevern',
                       'fr_sykd_familie',
                       'fr_sykd_barn',
                       'fr_annet',
                       'barnehager_prioritert',
                       'sosken__i_barnehagen',
                       'tidspunkt_oppstart',
                       'brutto_inntekt']
    
    forelder = pd.DataFrame(columns = kolonner_forelder)
    barnehage = pd.DataFrame(barnehage_liste, columns = kolonner_barnehage)
    barn = pd.DataFrame(columns = kolonner_barn)
    soknad  = pd.DataFrame(columns = kolonner_soknad)
    
    
    with pd.ExcelWriter(db_name) as writer:  
        forelder.to_excel(writer, sheet_name='foresatt')
        barnehage.to_excel(writer, sheet_name='barnehage')
        barn.to_excel(writer, sheet_name='barn')
        soknad.to_excel(writer, sheet_name='soknad')
    
    """
    b1 = Barn(1, "09012356472")
    f1 = Foresatt(1, "Ole Nordmann", "Bekkeveien 100", "98434344", "09079089332")
    f2 = Foresatt(2, "Solveig Imsdal", "Bekkeveien 100", "98434312", "09079233221")
    """

initiate_db("kgdata.xlsx")


