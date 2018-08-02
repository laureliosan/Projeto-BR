import xlrd

import json


workbook = xlrd.open_workbook("teste.xlsx")

worksheet = workbook.sheet_by_name("Planilha1")

#worksheet = workbook.sheet_by_index(0)


#(worksheet.col(0)):

pns = (worksheet.col_values(0))


def ola():
    x = input("Agora, qual PN deseja consultar? ")
    x = str(x)
    print("")
    if x in pns:
        print("O PN esta na Price-list Brasil")
        print("")
        return ola()
    else:
        print("O PN nao esta na Price-list Brasil ou ele foi digitado errado ")
        print("")
        return ola()









          





          
        

		

		







