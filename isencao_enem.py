# Fonte: https://www.thehuxley.com/problem/2099?locale=pt_BR

def checar_enceja(fez_enceja, nota_enceja):
    if fez_enceja == "s" and nota_enceja >= 400:
        return True
    else:
        return False

def checar_ultima_serie_publica(situacao_em, tipo_escola):
    if situacao_em == "CVC" and tipo_escola == "PUB":
        return True
    else:
        return False

def checar_bolsista(situacao_em, tipo_escola, renda):
    if situacao_em == "CLD" and ((tipo_escola == "PPB") or (tipo_escola == "PCB") or (tipo_escola == "PUB")) and renda <= 1431:
        return True
    else:
        return False

def checar_elegibilidade(situacao_em, fez_enceja, nota_enceja, tipo_escola, renda):
    if checar_enceja(fez_enceja, nota_enceja) or checar_bolsista(situacao_em, tipo_escola, renda) or checar_ultima_serie_publica(situacao_em, tipo_escola):
        return True
    else:
        return False


SITUACOES_POSSIVEIS = ["CLD", "CVC", "CSC", "NCC"]
FEZ_ENCEJA_POSSIVEIS = ["s", "n"]
TIPOS_ESCOLA_POSSIVEIS = ["PUB", "PCB", "PSB", "PPS", "PPB", "NFE"]


situacao_em = input()

fez_enceja = input()

nota_enceja = int(input())

tipo_escola = input()

renda = float(input())

if (situacao_em in SITUACOES_POSSIVEIS and fez_enceja in FEZ_ENCEJA_POSSIVEIS and tipo_escola in TIPOS_ESCOLA_POSSIVEIS and nota_enceja >= -1 and nota_enceja <= 800):
    
    if checar_elegibilidade(situacao_em, fez_enceja, nota_enceja, tipo_escola, renda):
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")
        
else:
    print("Informacao sobre ensino medio invalida")


# if checar_enceja(fez_enceja, nota_enceja) or checar_bolsista(situacao_em, tipo_escola, renda) or checar_ultima_serie_publica(situacao_em, tipo_escola):
#     print("Voce terah direito a isencao")
# else:
#     print("Infelizmente voce nao tem direito a isencao")

