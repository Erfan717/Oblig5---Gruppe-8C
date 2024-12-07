# initiate script
import pandas as pd
from kgmodel import Barnehage

def initiate_db(db_name):
    kg1 = Barnehage(1,"Askeladden barnehage",38,0)
    kg2 = Barnehage(2,"Auglandstjønn barnehage",70,3)
    kg3 = Barnehage(3,"Bamsebo barnehage",83,10)
    kg4 = Barnehage(4,"Bergtorasvei barnehage",61,0)
    kg5 = Barnehage(5,"Birkelid barnehage",54,23)
    kg6 = Barnehage(6,"Bjørnungen barnehage",74,0)
    kg7 = Barnehage(7,"Eventyrheia barnehage",92,24)
    kg8 = Barnehage(8,"Finsland barnehage",53,35)
    kg9 = Barnehage(9,"Havlimyra barnehage",148,50)
    kg10 = Barnehage(10,"Havåsen barnehage",98,0)
    kg11 = Barnehage(11,"Hellemyr barnehage",47,2)
    kg12 = Barnehage(12,"Hellinga barnehage",73,3)
    kg13 = Barnehage(13,"Jordbærveien barnehage",60,10)
    kg14 = Barnehage(14,"Karuss barnehage",59,20)
    kg15 = Barnehage(15,"Linerla barnehage",66,0)
    kg16 = Barnehage(16,"Lømslands vei barnehage",35,4)
    kg17 = Barnehage(17,"Mosby oppvekstsenter",82,9)
    kg18 = Barnehage(18,"Møllestua barnehage",96,1)
    kg19 = Barnehage(19,"Odderøya barnehage",51,8)
    kg20 = Barnehage(20,"Ravndalen barnehage",40,7)
    kg21 = Barnehage(21,"Roligheden gård barnehage",206,50)
    kg22 = Barnehage(22,"Sjøstjerna barnehage",83,0)
    kg23 = Barnehage(23,"Skårungen barnehage",50,3)
    kg24 = Barnehage(24,"Solstrålen barnehage",61,4)
    kg25 = Barnehage(25,"Søm barnehage",31,5)
    kg26 = Barnehage(26,"Taremareskogen barnehage",43,3)
    kg27 = Barnehage(27,"Tinnstua barnehage",59,0)
    kg28 = Barnehage(28,"Torvmoen barnehage",64,34)
    kg29 = Barnehage(29,"Trollhaugen barnehage",40,2)
    kg30 = Barnehage(30,"Tunballen barnehage",67,66)
    kg31 = Barnehage(31,"Veslefrikk barnehage",72,0)
    kg32 = Barnehage(32,"Voietun barnehage",51,1)
    kg33 = Barnehage(33,"Øvre Slettheia barnehage",71,2)
    kg34 = Barnehage(34,"Åros barnehage",67,6)
    
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
    kolonner_statistikk = ['kom',
                           'y15',
                           'y16',
                           'y17',
                           'y18',
                           'y19',
                           'y20',
                           'y21',
                           'y22',
                           'y23']
    
    forelder = pd.DataFrame(columns = kolonner_forelder)
    barnehage = pd.DataFrame(barnehage_liste, columns = kolonner_barnehage)
    barn = pd.DataFrame(columns = kolonner_barn)
    soknad  = pd.DataFrame(columns = kolonner_soknad)
    statistikk  = pd.DataFrame(columns = kolonner_statistikk)
    
    with pd.ExcelWriter(db_name) as writer:  
        forelder.to_excel(writer, sheet_name='foresatt')
        barnehage.to_excel(writer, sheet_name='barnehage')
        barn.to_excel(writer, sheet_name='barn')
        soknad.to_excel(writer, sheet_name='soknad')
        statistikk.to_excel(writer, sheet_name='statistikk')
    """
    b1 = Barn(1, "09012356472")
    f1 = Foresatt(1, "Ole Nordmann", "Bekkeveien 100", "98434344", "09079089332")
    f2 = Foresatt(2, "Solveig Imsdal", "Bekkeveien 100", "98434312", "09079233221")
    """

initiate_db("kgdata.xlsx")


