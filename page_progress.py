import random

def get_pos_phrase():
    pos_phrases = (
        'Excellent!!',
        'DY-NA-MITE!!',
        'Yippee-kay-yeah progress conductor!',
        'Absolute Legend!!',
        'Keep going, you’re crushing it!',
        'Every page counts!',
        'Page by page, you’re winning!',
        'You’ve got this!'
    )
    print(random.choice(pos_phrases))

def pg_prog():
    try:
        total_pages = int(input("📘 Total number of pages in the book: "))
        if total_pages <= 0:
            print("Total pages must be greater than 0.")
            return

        while True:
            page = input("📖 What page are you on? (type 'q' to quit): ")
            if page.lower() == 'q':
                print("Goodbye and happy reading! 📚")
                break

            try:
                page_number = int(page)
                if page_number < 0:
                    print("Please enter a positive page number.")
                    continue
                if page_number > total_pages:
                    print("That’s more pages than the book has! Try again.")
                    continue

                percent = page_number / total_pages * 100
                progress = f"{percent:.1f}%"
                print(f"You're at: {progress}")
                get_pos_phrase()

            except ValueError:
                print("Please enter a valid number or 'q' to quit.")

    except ValueError:
        print("Invalid input for total number of pages. Must be an integer.")

if __name__ == '__main__':
    pg_prog()
