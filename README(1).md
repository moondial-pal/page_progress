# 📘 Page Progress Tracker

This is one of the first Python apps I created, built to help track my progress while studying a book. The idea is simple: enter the total number of pages in your book, input your current page, and get instant feedback on how far you've come—along with a randomly selected, positive affirmation to keep you motivated!

## 💡 Features

- Prompts user for total number of pages in a book
- Lets you enter your current page and calculates your reading progress
- Prints an encouraging message each time you check your progress
- Input validation to keep things user-friendly
- Option to quit at any time

## 🧪 Example

```
📘 Total number of pages in the book: 350  
📖 What page are you on? (type 'q' to quit): 120  
You're at: 34.3%  
DY-NA-MITE!!

📖 What page are you on? (type 'q' to quit): q  
Goodbye and happy reading! 📚
```

## 🧠 Motivation

I made this app to stay encouraged while reading a dense textbook. The positive phrases kept me going, and the progress check-ins helped me stay on track.

## 📂 File

- `page_progress.py` — Main script containing all the logic

## 🚀 How to Run

Make sure you have Python installed, then run:

```bash
python3 page_progress.py
```

## 🔧 Ideas for Improvement

- Save progress to a file or database (like SQLite)
- Add a GUI using BeeWare or convert to a mobile app
- Track multiple books
- Visualize progress with charts or a progress bar
