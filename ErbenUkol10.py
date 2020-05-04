import argparse
import sys


def main():
    prg_parser = argparse.ArgumentParser(description='Program počítající znaky, slova a řádky.')
    prg_parser.add_argument('soubor', help = "název vstupního souboru")
    prg_parser.add_argument("--slova", help="Spočítat slova", action="store_true")
    prg_parser.add_argument("--radky", help="Spočítat řádky", action="store_true")
    prg_parser.add_argument("--znaky", help="Spočítat znaky", action="store_true")
	
    arguments = prg_parser.parse_args()
    try:

        f = open(arguments.soubor, "r")
        soubor = f.read()
        flag = False

        if arguments.radky:
            pocet_radku = soubor.count("\n") + 1
            print(f"Počet řádků: {pocet_radku}")
            flag = True

        if arguments.slova:
            pocet_slov = soubor.count(" ") + pocet_radku
            print(f"Počet slov: {pocet_slov}")
            flag = True

        if arguments.znaky:
            pocet_znaku = len(soubor)
            print(f"Počet znaků: {pocet_znaku}")
            flag = True

        if not flag:
            pocet_radku = soubor.count("\n") + 1
            pocet_slov = soubor.count(" ") + pocet_radku
            pocet_znaku = len(soubor)
            print(f"Počet slov: {pocet_slov}\nPočet znaků: {pocet_znaku}\nPočet řádků: {pocet_radku}")
    except:
        print("Pokazilo se to")
        sys.exit(1)

    main ()