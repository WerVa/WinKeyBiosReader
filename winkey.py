import sys


def find_windows_key(file_path):
    # Wczytanie zawartości pliku binarnego
    with open(file_path, "rb") as file:
        data = file.read()

    # Konwersja ciągu heksadecymalnego na postać bajtową
    search_pattern = bytes.fromhex(
        "01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 1d 00 00 00"
    )

    # Wyszukiwanie indeksu pasującego wzorca w danych binarnych
    index = data.find(search_pattern)

    if index != -1:
        # Wyciągnięcie klucza Windowsa z danych binarnych
        windows_key = data[
            index + len(search_pattern) : index + len(search_pattern) + 29
        ].decode("utf-8")

        return windows_key
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Podaj ścieżkę do pliku wsadu BIOSu jako argument.")
        print("Przykład użycia: python winkey.py bios.bin")
    else:
        wsad_biosu_path = sys.argv[1]
        windows_key = find_windows_key(wsad_biosu_path)

        if windows_key is not None:
            print("Znaleziono klucz Windowsa:", windows_key)
        else:
            print("Nie znaleziono klucza Windowsa w podanym pliku binarnym.")
