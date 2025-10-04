
# !guessing game

import random
import os
import time
import pygame

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def word4():
    print(
    """================Level 4 started================""")
    input("Press Enter to start the level 4")


def word3():
    input("Press Enter to start the level 3")
    screen_clear()
    print("""
            ===================Level 3 Started====================
        """)

    words3 = ["newton", "einstein", "galilei", "Nikolas Tesla","Marie Curie ","Charles Darwin", "Stephen Hawking ", "Alexander Fleming","Michael Faraday", "Thomas Edison"]   # keep lowercase to match
    random_word3 = random.choice(words3)
    attempts3 = 0

    while attempts3 < 5:
        if random_word3 == "newton":
            print("Question: Who discovered the law of universal gravitation?")
        elif random_word3 == "einstein":
            print("Question: Who discovered the theory of relativity?")
        elif random_word3 == "galilei":
            print("Question: Who discovered the law of motion?")
        elif random_word3 == "Nikolas Tesla":
            print("Question: Who discovered the Tesla coil?")
        elif random_word3 == "Marie Curie":
            print("Question: Who discovered the Curie law?")
        elif random_word3 == "Charles Darwin":
            print("Question: Who discovered Darwin's theory of evolution?")
        elif random_word3 == "Stephen Hawking":
            print("Question: Who discovered Hawking's theory of black holes?")
        elif random_word3 == "Alexander Fleming":
            print("Question: Who discovered the penicillin?")
        elif random_word3 == "Michael Faraday":
            print("Question: Who discovered the Faraday effect?")
        elif random_word3 == "Thomas Edison":    
            print("Question: Who discovered the light bulb?")    
        
        choice = input("your answer: ").strip().lower()

        attempts3 += 1

        if choice == "end":
            print("ending game...")
            exit()

        if choice == random_word3:
            print("You guessed it!")
            print("The word was", random_word3)
            print("""
            ====================Level 3 acquired!===================
            """)
            next_level = input("Do you want to play the next level? (yes/no): ")
            if next_level.lower() == "yes":
                word4()
            break
        else:
            print("Try again!")   # no answer reveal
            time.sleep(0.5)
            screen_clear()

        if attempts3 == 5:
            print("You've used all your attempts. The word was", random_word3)
            break

def word2():
    input("Press Enter to start the level 2")
    screen_clear()
    print("""
          ===================Level 2 Started====================
          """)
    words2 = ["dog","cat","lion","tiger","elephant","monkey","zebra","peacock","gorilla","ostrich","pigeon","parrot"]
    random_word2 = random.choice(words2).strip().lower()
    attempts2 = 0
    while attempts2 < 5:
        if random_word2[0] in ["d","l","t","z","e","m","g","c"]: 
            print(f"Hint: The first letter of the word is {random_word2[0]}. The Animal is mammal.")
        else:
            print(f"Hint: The first letter of the word is {random_word2[0]}. The Animal is bird.")
        choice = input("Enter an animal: ").lower()   # fixed wording
        attempts2 += 1
        if choice == "end":
            print("ending game...")
            exit()
        if choice == random_word2:
            print("You guessed it!")
            print("The word was", random_word2)
            print("""
        ====================Level 2 acquired!===================
            """)
            input("Press Enter to start the level 3")
            word3()
            screen_clear()
        else:
            print("Try again!")   # removed answer reveal
            time.sleep(0.5)
            screen_clear()

        if attempts2 == 5:   # fixed mismatch
            print("You've used all your attempts. The word was", random_word2)
            break

def word():
    attempts = 0
    words = ["boy","girl","friend","brother","sister","mom","dad","uncle","aunt","grandma","grandpa","grandson","granddaughter","nephew","niece"]
    random_word = random.choice(words)
    while attempts < 5:
        choice = input("Enter a relatives role: ").lower()
        attempts += 1
        if choice == "end":
            print("ending game...")
            time.sleep(2)
            exit()
        if choice == random_word:
            print("You guessed it!")
            print("The word was", random_word)
            print("""
        ====================Level 1 acquired!===================
            """)
            next_level = input("Do you want to play the next level? (yes/no): ")
            if next_level.lower() == "yes":
                word2()
            break
        else:
            print("Try again!", random_word)  # removed answer reveal
            time.sleep(0.5)
            screen_clear()

        if attempts == 5:   # fixed mismatch
            print("You've used all your attempts. The word was", random_word)
            break

        if choice not in words:
            print("Invalid choice. Please try again.")
            continue
word()
