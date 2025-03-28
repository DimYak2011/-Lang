def run_code(cmd):
    translations = {
        'абоюдна': 'print',
        'обидно': 'else',
        'абидна': 'if',
        'абаюдно': 'input',
        'абаюнда': 'for',
        'абоюнда': 'while'
    }

    for value in translations.values():
        cmd = cmd.replace(value, "")
            
    for key, value in translations.items():
        cmd = cmd.replace(key, value)

    try:
        exec(cmd)
    except Exception as e:
        print("Вы инвалид")



if __name__ == "__main__":
    while True:
        try:
            cmd = input(">>> ")
        except EOFError:
            print("\nВыход")
            break
        except KeyboardInterrupt:
            print("\nВыход")
            break

        if cmd == "выход":
            break

        run_code(cmd)

