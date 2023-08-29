class PersonalDiary:
    def __init__(self, filename):
        self.filename = filename

    def write_entry(self, entry):
        with open(self.filename, 'a') as file:
            file.write(entry + '\n')
        print("Entry saved successfully.")

    def read_entries(self):
        with open(self.filename, 'r') as file:
            entries = file.readlines()
        return entries

diary = PersonalDiary(filename="diary.txt")

while True:
    print("1. Write Entry")
    print("2. Read Entries")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        entry = input("Write your entry: ")
        diary.write_entry(entry)
    elif choice == '2':
        entries = diary.read_entries()
        if entries:
            print("Diary Entries:")
            for i, entry in enumerate(entries, start=1):
                print(f"{i}. {entry.strip()}")
        else:
            print("No entries to display.")
    elif choice == '3':
        print("Exiting the personal diary system.")
        break
    else:
        print("Invalid choice. Please try again.")
