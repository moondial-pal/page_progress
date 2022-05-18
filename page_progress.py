import random
# Going to be a Beeware Mobile App potentially
# Could also make a web app.
# Could include sqlite db to save progress

""" Incorporate dictionary with uplifting, positive phrases.
Randomly select phrase from dictionary each time a percentage is printed."""


def get_pos_phrase():

    pos_phrases = (
        'Excellent!!',
        'DY-NA-MITE!!',
        'Yippee-kay-yeah progress conductor!',
        'Absolute Legend!!'
    )

    print(random.choice(pos_phrases))


# User must enter total number of pages in book
def pg_prog(total_pages: int):
    # Ask user what page they are on
    page = input("What page are you on? ")
    page_number = int(page)

    # Calculates and creates a percentage value then delivers a positive compliment
    percent = page_number/total_pages * 100
    progress = "%g%%" % percent
    print("You're at: " + progress)
    get_pos_phrase()


if __name__ == '__main__':
    pg_prog(100)