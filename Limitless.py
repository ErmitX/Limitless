import random
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.015):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def bar(value, maximum=100, width=25):
    filled = int((value / maximum) * width)
    return "[" + "█" * filled + "░" * (width - filled) + "]"

def status(player):
    clear()
    print("=" * 58)
    print("                         LIMITLESS")
    print("=" * 58)
    print()
    print(f"Focus       {bar(player['focus'])} {player['focus']}/100")
    print(f"Confidence  {bar(player['confidence'])} {player['confidence']}/100")
    print(f"Money       ${player['money']:,}")
    print(f"Reputation  {player['reputation']}/100")
    print(f"Health      {player['health']}/100")
    print(f"Days        {player['days']}")
    print()
    print("=" * 58)

def pause():
    input("\nPress ENTER to continue...")

def choose(options):
    while True:
        choice = input("\n> ").strip()
        if choice in options:
            return choice
        print("Choose a valid option.")

player = {
    "focus": 25,
    "confidence": 20,
    "money": 120,
    "reputation": 5,
    "health": 100,
    "days": 1,
    "nzt": False
}

clear()
print("=" * 58)
print("                         LIMITLESS")
print("=" * 58)
print()
type_text("You wake up in a small apartment.")
type_text("Another day. Another blank page.")
type_text("You have ideas, but never enough focus to turn them into reality.")
print()
type_text("Then you remember the pill.")
type_text("NZT-48.")
type_text("One pill. Supposedly unlimited potential.")
print()
print("1. Take the pill")
print("2. Throw it away")
choice = choose(["1", "2"])

if choice == "2":
    clear()
    type_text("You throw the pill into the trash.")
    type_text("Maybe ordinary is safer.")
    print()
    type_text("But as you walk away, you wonder what could have happened.")
    print()
    print("THE END")
    raise SystemExit

player["nzt"] = True
player["focus"] = 95
player["confidence"] = 85

clear()
type_text("You swallow the pill.")
time.sleep(1)
type_text("The room becomes silent.")
type_text("Every detail becomes sharp.")
type_text("Every thought connects to another.")
type_text("You suddenly remember everything you've ever seen.")
type_text("You understand everything.")
print()
type_text("You smile.")
pause()

while player["days"] <= 10 and player["health"] > 0:

    status(player)

    if player["money"] >= 1000000:
        print("You have reached $1,000,000.")
        print()
        print("1. Keep pushing")
        print("2. Walk away")
        choice = choose(["1", "2"])

        if choice == "2":
            clear()
            type_text("You stop.")
            type_text("For the first time, you realize something important.")
            type_text("Being limitless means nothing if you lose yourself.")
            print()
            print(f"Final fortune: ${player['money']:,}")
            print(f"Final reputation: {player['reputation']}/100")
            print()
            print("THE END")
            break

    print("Your next move:")
    print()
    print("1. Trade on the market")
    print("2. Build a business")
    print("3. Study and improve yourself")
    print("4. Attend an elite party")
    print("5. Take a dangerous shortcut")
    print("6. Rest")

    choice = choose(["1", "2", "3", "4", "5", "6"])

    if choice == "1":
        clear()
        type_text("You analyze the market.")
        time.sleep(1)
        type_text("Patterns appear where everyone else sees chaos.")
        gain = random.randint(15000, 80000)
        player["money"] += gain
        player["reputation"] += random.randint(2, 6)
        player["health"] -= random.randint(3, 8)
        type_text(f"You make ${gain:,}.")
        pause()

    elif choice == "2":
        clear()
        type_text("You see an opportunity nobody else noticed.")
        type_text("You build a company around it.")
        gain = random.randint(10000, 60000)
        player["money"] += gain
        player["reputation"] += random.randint(5, 12)
        player["confidence"] = min(100, player["confidence"] + 5)
        player["health"] -= random.randint(5, 12)
        type_text(f"The company generates ${gain:,}.")
        pause()

    elif choice == "3":
        clear()
        type_text("You spend the day learning.")
        type_text("Languages. Mathematics. Psychology. Economics.")
        player["focus"] = min(100, player["focus"] + 5)
        player["confidence"] = min(100, player["confidence"] + 10)
        player["reputation"] += 3
        type_text("Your mind becomes even sharper.")
        pause()

    elif choice == "4":
        clear()
        type_text("You enter a room filled with billionaires.")
        type_text("Nobody knows who you are.")
        type_text("Five minutes later, everyone does.")
        player["reputation"] += random.randint(8, 18)
        player["confidence"] = min(100, player["confidence"] + 8)
        player["money"] += random.randint(1000, 10000)
        player["health"] -= random.randint(2, 6)
        type_text("Your network expands overnight.")
        pause()

    elif choice == "5":
        clear()
        type_text("You discover a shortcut.")
        type_text("It's extremely profitable.")
        type_text("It's also extremely dangerous.")
        roll = random.randint(1, 100)

        if roll > 35:
            gain = random.randint(50000, 250000)
            player["money"] += gain
            player["reputation"] += random.randint(5, 15)
            player["health"] -= random.randint(10, 25)
            type_text(f"You pull it off and make ${gain:,}.")
        else:
            loss = min(player["money"], random.randint(10000, 90000))
            player["money"] -= loss
            player["reputation"] -= random.randint(5, 15)
            player["health"] -= random.randint(20, 40)
            type_text("The plan collapses.")
            type_text(f"You lose ${loss:,}.")
        pause()

    elif choice == "6":
        clear()
        type_text("You put everything aside.")
        type_text("No business. No money. No pressure.")
        type_text("Just sleep.")
        player["health"] = min(100, player["health"] + 25)
        player["focus"] = min(100, player["focus"] + 10)
        type_text("You wake up feeling stronger.")
        pause()

    player["days"] += 1

    if player["health"] <= 25:
        clear()
        type_text("Your body is starting to fail.")
        type_text("NZT gives you an incredible mind.")
        type_text("But it cannot make you immortal.")
        print()
        print("1. Rest")
        print("2. Keep going")
        choice = choose(["1", "2"])

        if choice == "1":
            player["health"] = min(100, player["health"] + 35)
            player["focus"] = max(0, player["focus"] - 10)
            type_text("You finally allow yourself to recover.")
            pause()

        else:
            player["health"] -= 15
            type_text("You ignore the warning.")
            type_text("The world keeps moving.")
            pause()

if player["health"] <= 0:
    clear()
    type_text("Your body finally gives in.")
    print()
    print("You had the ability to become limitless.")
    print("You simply forgot that you were human.")
    print()
    print(f"Final fortune: ${player['money']:,}")
    print(f"Final reputation: {player['reputation']}/100")
    print()
    print("THE END")

elif player["days"] > 10:
    clear()
    print("=" * 58)
    print("                         LIMITLESS")
    print("=" * 58)
    print()
    type_text("Ten days have passed.")
    type_text("Your life is completely different.")
    print()
    print(f"Money:       ${player['money']:,}")
    print(f"Reputation:  {player['reputation']}/100")
    print(f"Confidence:  {player['confidence']}/100")
    print(f"Health:      {player['health']}/100")
    print()
    
    if player["money"] >= 500000 and player["reputation"] >= 50:
        type_text("You became the person everyone wanted to know.")
        type_text("The world is finally playing by your rules.")
        print()
        print("ENDING: THE NEW EDDIE")
    elif player["money"] >= 250000:
        type_text("You became incredibly wealthy.")
        type_text("But you still wonder how long it can last.")
        print()
        print("ENDING: POWER")
    elif player["reputation"] >= 60:
        type_text("Your name became more valuable than money.")
        print()
        print("ENDING: INFLUENCE")
    else:
        type_text("You survived.")
        type_text("Maybe that is the real achievement.")
        print()
        print("ENDING: HUMAN")
