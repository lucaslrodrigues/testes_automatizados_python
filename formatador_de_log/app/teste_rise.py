

def main():
    var = "Returned value 10"
    raise ValueError(f"ERRO, valor retornado invalido. {var}")

if __name__ == "__main__":
    try:
        v = main()
        print("in try")
    except Exception as e:
        print("in exception")
        print(e)
    print("continue code")

    validate_row = True
    key_errors = []
    valid_keys = ["EAN/DUN", "Preço mínimo (R$)", "Preço padrão (R$)", "Tamanho da embalagem (un)",
                  "Tamanho da embalagem (un)"]
    for i in valid_keys:
        if i not in row:
            validate_keys = False
            key_errors.append(i)

    if validate_row:
        preco_minimo = row["Preço mínimo (R$)"]
        preco_padrao = row["Preço padrão (R$)"]
        pallet_multiplo_dun = row["Pallet Multiplo de DUN"]
        tamanho_embalagem = row["Tamanho da embalagem (un)"]

        data.append(
            {
                "ean_ou_dun": row["EAN/DUN"],
                "tamanho_embalagem": int(tamanho_embalagem),
                "pallet_multiplo_dun": int(pallet_multiplo_dun),
                "preco_minimo": float(preco_minimo),
                "preco_padrao": float(preco_padrao),
                **lista_grupos,
            }
        )
    else:
        raise ValueError(f"Arquivo sem os campos: {key_errors}")
return data