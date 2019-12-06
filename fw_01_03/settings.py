def ENGINE(engine):
    ENGINE = True
    if engine == "json":
        ENGINE = True
    elif engine == "csv":
        ENGINE = False
    else:
        print("Wrong input, json or csv expected")
    return ENGINE



