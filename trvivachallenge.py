#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html

URL = "https://opentdb.com/api.php?amount=10&category=23&difficulty=hard&type=multiple"

def main():
    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL).json()

    # Level 1 - Print questions and answers
    questions = data['results']

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {html.unescape(question['question'])}")

        # Print the answers
        answers = question['incorrect_answers'] + [question['correct_answer']]
        for j, answer in enumerate(answers, start=1):
            print(f"{j}. {html.unescape(answer)}")

if __name__ == "__main__":
    main()

