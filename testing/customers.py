from collections import namedtuple

from enum import IntEnum

class suburb(IntEnum):
    Long_Bay = 0
    Browns_bay = 1
    Torbay = 2
    Albany = 3
    Silverdale = 4


customer = namedtuple('Customer', ('name', 'phonenumber', 'address', 'suburb'))

Emile_Matthews = customer('Emile_Matthews', '0789121980', '4c_Pongola_Rd', suburb.Torbay)
Marissa_Moore = customer('Marissa_Moore', '0783456236', '2b_Capecod_Rd', suburb.Long_Bay)
Sandra_Koen = customer('Sandra_Koen', '0201457836', '30_Tui_Rd', suburb.Browns_bay)
Koos_Koombuis = customer('Koos_Kombuis', '0208963773', '777_Kiwi_Ln', suburb.Albany)
Jan_Blauukaas = customer('Jan_Blauukaas', '0220982454', '776_Kiwi_Ln', suburb.Albany)
Pieter_Pan = customer('Pieter_Pan', '02215568903', '9_Pamela_Cres', suburb.Silverdale)

Custmers = [Emile_Matthews, Marissa_Moore, Sandra_Koen, Koos_Koombuis, Jan_Blauukaas, Pieter_Pan]

print(Custmers)