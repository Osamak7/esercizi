def fabbricatore_macchina(casa_produtrice: str, modello: str, **caratteristiche: str) -> dict:
    info_macchina: dict[str] = {
        "casa produtrice": casa_produtrice,
        "modello": modello
    }
    info_macchina.update(caratteristiche)
    return info_macchina