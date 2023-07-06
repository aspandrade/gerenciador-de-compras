print("=" * 30)
print("\033[1;31;40mGERENCIADOR DE PAGAMENTOS\033[m")
print("=" * 30)


valor = float(input("\033[1;33;40mValor do produto:\033[m \033[1;36;40mR$\033[m"))
print("")
print('''\033[1;31;40mSELECIONE O MÉTODO DE PAGAMENTO\033[m


\033[1;32;40m[ 1 ] - Pagamento à vista (Dinheiro/Cheque)
[ 2 ] - Cartão (à vista)
[ 3 ] - Cartão (Parcelado)\033[m

''')

pagamento = int(input("\033[1;33;40mDigite aqui:\033[m"))

if pagamento == 1:
    desconto = (100-10) / 100 * valor
    print("")
    print("\033[1;32;40mVocê terá um desconto de 10%\033[m!")
    print("")
    print("\033[1;33;40mValor a ser pago:\033[m \033[1;36;40mR$\033[m\033[1;36;40m{:.2f}\033[m\033[1;33;40m.\033[m".format(desconto))
    print("")
if pagamento == 2:
    desconto = (100-5) / 100 * valor
    print("")
    print("\033[1;32;40mVocê terá um desconto de 5%\033[m!")
    print("")
    print("\033[1;33;40mValor a ser pago:\033[m \033[1;36;40mR$\033[m\033[1;36;40m{:.2f}\033[m\033[1;33;40m.\033[m".format(desconto))
    print("")

if pagamento == 3:
    print("")
    print("")
    print("\033[1;33;40mEm quantas parcelas você deseja dividir?\033[m")
    print("")
    print("")
       
    parcelas = int(input("\033[1;33;40mDigite aqui:\033[m"))

    if parcelas <= 2:
        print("")
        print("\033[1;32;40mO preço permanece o mesmo.\033[m")
        print("")
        print("\033[1;33;40mValor a ser pago: \033[1;36;40mR$\033[m\033[1;36;40m{:.2f}\033[m\033[1;33;40m.\033[m".format(valor))
        print("")

    elif parcelas >= 3:
        print("")
        print("")
        print("\033[1;31;40mATENÇÃO\033[m: \033[31;40mVOCÊ TERÁ 20% DE JUROS NESSAS PARCELAS!\033[m")
        print("")
        print("\033[1;33;40mDeseja verificar quanto ficariam as parcelas?\033[m")
        print("")
        
        p1 = str(input("\033[1;33;40mDigite aqui:\033[m")).lower()

        if p1 == "nao" or p1 == "não" or p1 == "n" or p1 == "nn":
            print("")
            print("\033[1;32;40mTudo bem, sem problemas.\033[m")
        
        if p1 == "sim" or p1 == "s":
            pagamento = valor / parcelas
            valor_parcela = (100+20) / 100 * pagamento
            print("")
            print("\033[1;33;40mFicarão {} parcelas de\033[m \033[1;36;40mR${:.2f}\033[m.".format(parcelas, valor_parcela))