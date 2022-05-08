def pg_prog(page_number: int, total_pages: int):
    percent = page_number/total_pages * 100
    progress = "%g%%" % percent
    print("Absolute Legend!! You're at: " + progress)

    # Incorporate dictionary with uplifting, positive phrases.
    # Randomly select phrase from dictionary each time a percentage is printed.
