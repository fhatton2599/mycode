#!/bin/env pyhton3


import html


trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }


question = trivia["question"]

#correct
D = trivia["correct_answer"]

#incorrect
A = trivia["incorrect_answers"][0]
B = trivia["incorrect_answers"][1]
C = trivia["incorrect_answers"][2]


def main():
    
    #print(f"{question"})
    print(html.unescape(question))
    print("A", html.unescape(A))
    print("B", html.unescape(B))
    print("C", html.unescape(C))
    print("D", html.unescape(D))

    input("What is the correct answer?\n")

    
main()
