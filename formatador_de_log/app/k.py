data_final = ""
def main():
    global data_final
    data_final = ""

    with open("../resources/lista.txt", "r", encoding="utf-8") as arquivo:
        TEXTO = arquivo.readlines()
    data = []

    for l in TEXTO:
         data.append(l)

    format_data(data)
    print(data_final)

    with open("../resources/data.txt", "w") as arquivo:
        arquivo.write(data_final)



def format_data(data: list):
    global data_final
    iterador = ""
    trigger = False
    for i in data:
        if i[0] == "@":
            a = i
            iterador += i[0:-2] + (" " * (20 - len(i[0:-2])))
            if iterador == "@message            ":
                trigger = True
            else:
                trigger = False
            continue
        if i == "1\n":
            iterador += i[0] + "                   "
            continue
        if i == "Campo	Valor\n":
            i = "Campo               Valor\n"
        # if i == "@message            ":
        #     trigger = True
        #     iterar()
        #     continue

        if trigger:
            if not iterador == "@message            ":
                i = (" " * 20) + i

        iterar(iterador, i)
        iterador = ""


def iterar(iterador: str, i: str):
    global data_final
    iterador += i
    data_final += iterador

if __name__ == "__main__":
    main()


