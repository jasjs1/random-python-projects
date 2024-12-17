import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to Mad Lib")
time.sleep(0.5)
print("Starting game...")
time.sleep(0.5)

def run_verbs():
    noun = input("Noun: ")
    adjective = input("Adjective: ")
    verb = input("Verb: ")
    adverb = input("Adverb: ")
    place = input("Place: ")
    return noun, adjective, verb, adverb, place
noun, adjective, verb, adverb, place = run_verbs()

print("Got your results")
print("Creating Mad Lib...")
time.sleep(1.5)

os.system('cls' if os.name == 'nt' else 'clear')

story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb} in the {place}."
print(story)

print("")
print("")

print("Type N to start a new game.")
new_Game = input("")

if new_Game == "n":
    run_verbs()
else:
    print("")
