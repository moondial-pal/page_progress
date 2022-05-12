
# Going to be a Beeware Mobile App potentially
# Could also make a web app.
# Could include sqlite db to save progress

""" Incorporate dictionary with uplifting, positive phrases.
Randomly select phrase from dictionary each time a percentage is printed."""


# User must enter total number of pages in book
def pg_prog(total_pages: int):
    # Ask user what page they are on
    page = input("What page are you on?")
    page_number = int(page)

    # Calculates and creates a percentage value
    percent = page_number/total_pages * 100
    progress = "%g%%" % percent

    print("Absolute Legend!! You're at: " + progress)


pg_prog(100)

     Incorporate dictionary with uplifting, positive phrases.
     Randomly select phrase from dictionary each time a percentage is printed.
