import json

FILENAME = "notes.json"

def save_notes(notes: list[str]):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)

def load_notes(): 
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]


def main():
    notes = load_notes()

    while True:
        print("oerhhuiofeifeef")
        print("1. visa ant")
        print("2. lägg till ant")
        print("3. ta bort ant")
        print("4. avsluta")

        choice = input("välj 1-4: ")

        if choice == "1":
            print("\ndina ant")
            if not notes:
                print("du ahr inte ant")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {notes}")

        elif choice == "2":
            text= input("skriv en ant: ")
            notes.append(text)
            save_notes(notes)
            print("ant är sparad")

        elif choice == "3":
            notes.clear()
            save_notes(notes)
            print("alla ant är borta")

        elif choice == "4":
            print("avslutar...")
            break

        else:
            print("Ogiltigt val")



if __name__ =="__main__":
    main()
