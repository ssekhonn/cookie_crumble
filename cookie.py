"""
PSEUDOCODE / GAME PLAN
----------------------
1. Greet player, get their name.
2. Initialize stats: hp, xp, energy, inventory, snack_points.
3. DECISION 1: Get out of bed or stay under covers.
   - If stay: Dormancy Charm → fail.
   - If get out: gain xp, continue.
4. DECISION 2: Inspect the crumbs or ignore them.
   - If ignore: roommate eats snack → fail.
   - If inspect: find rainbow trail → gain xp.
5. DECISION 3: Dash unprepared or retrieve wand.
   - If dash: sprain ankle, lose hp → fail.
   - If retrieve wand: gain wand in inventory → continue.
6. DECISION 4: Follow the wand’s beam into kitchen or sneak behind Imp.
   - If sneak: crash into glaze → fail.
   - If follow: enter kitchen → gain xp.
7. DECISION 5: Ask politely or trade sugar‐gem.
   - If ask: Imp returns biscuit → success, gain snack_points.
   - If trade: lose one gem, gain biscuit → success, gain snack_points.
8. END GAME: Show final stats and a victory/defeat message.
"""

# ------------------------------
# 1. SETUP & PLAYER INTRODUCTION
# ------------------------------
# Ask for player's name, clean and format it.
player_name = input("Enter your name, brave snacker: ").strip().title()
print(f"\nWelcome to the Academy of Snacks and Sorcery, {player_name}!\n")

# ------------------------------
# 2. INITIALIZE PLAYER STATS
# ------------------------------
hp = 10                 # Health points
xp = 0                  # Experience points
energy = 5.0            # Energy level (float to demonstrate type)
inventory = []          # List for items (e.g., wand, sugar-gem)
snack_points = 0        # Points for retrieving the biscuit

# Give the player a sugar-gem to potentially trade
inventory.append("Sugar-Gem")

# ------------------------------
# 3. HELPER FUNCTION TO END GAME
# ------------------------------
def end_game(success: bool):
    """Ends the game, printing final stats and outcome."""
    print("\n--- FINAL STATS ---")
    print(f"HP: {hp}")
    print(f"XP: {xp}")
    print(f"Energy: {energy}")
    print(f"Inventory: {inventory}")
    print(f"Snack Points: {snack_points}")
    if success:
        print("\nCongratulations! You secured your Bubble Berry Biscuit!")
    else:
        print("\nAlas, your quest for the Bubble Berry Biscuit has failed.")
    exit()  # Terminate the script

# ------------------------------
# 4. DECISION 1
# ------------------------------
choice1 = input("You wake up in your dorm—your Bubble Berry Biscuit is gone! Get out of bed? (yes/no) ")
choice1 = choice1.strip().lower()  # sanitize input

if choice1 == "no":
    # Stay under covers: instant fail
    print("\nA Dormancy Charm lulls you back to sleep... You wake up hours later with no biscuit.")
    end_game(success=False)
elif choice1 == "yes":
    # Gain experience for bravery
    xp += 5
    print("\nYou swing your legs out of bed, spotting glittering sugar-crumbs on the floor.")
else:
    # Handle unexpected input
    print("\nIndecision costs you time—your roommate eats the last crumb. Quest over.")
    end_game(success=False)

# ------------------------------
# 5. DECISION 2
# ------------------------------
choice2 = input("\nInspect the empty plate or ignore the crumbs? (inspect/ignore) ")
choice2 = choice2.strip().lower()

if choice2 == "ignore":
    print("\nYou slip under the covers again... Your roommate finds and devours the last biscuit.")
    end_game(success=False)
elif choice2 == "inspect":
    xp += 5
    print("\nTiny rainbow crumbs lead toward the door. The trail awaits!")
else:
    print("\nHesitation causes the trail to vanish—no biscuit to be found.")
    end_game(success=False)

# ------------------------------
# 6. DECISION 3
# ------------------------------
print("\nYou must decide quickly: dash after the crumbs unprepared, or arm yourself.")
choice3 = input("Type 'dash' or 'wand': ").strip().lower()

if choice3 == "dash":
    # Sprain ankle: lose hp and fail
    hp -= 7
    print(f"\nYou sprint, slip on a toffee shard, and tumble down the stairs! HP is now {hp}.")
    print("Your ankle is sprained—no snack quest for you.")
    end_game(success=False)
elif choice3 == "wand":
    # Retrieve Wand of Snack-Seeking
    inventory.append("Wand of Snack-Seeking")
    xp += 10
    print("\nYou grasp your ivory wand; it pulses to life, revealing a glowing path.")
else:
    print("\nWithout a plan, you're lost in the halls. The trail fades. Quest failed.")
    end_game(success=False)

# ------------------------------
# 7. DECISION 4
# ------------------------------
print("\nThe wand’s beam leads you to the Spiced Sorcery Kitchen.")
choice4 = input("Sneak behind the Imp or follow the beam politely? (sneak/follow) ")
choice4 = choice4.strip().lower()

if choice4 == "sneak":
    # Fail path: crash into glaze
    print("\nYou tiptoe, crash into a cauldron of bubbling glaze. The Imp laughs and vanishes.")
    end_game(success=False)
elif choice4 == "follow":
    xp += 5
    print("\nYou follow the glowing beam inside. Cinnamon steam fills the air.")
else:
    print("\nConfusion reigns as you wander... the Imp disappears, biscuit lost.")
    end_game(success=False)

# ------------------------------
# 8. DECISION 5
# ------------------------------
print("\nYou see the Kitchen Imp cackling, holding your Bubble Berry Biscuit.")
print(f"Inventory: {inventory}")
choice5 = input("Do you ask politely or trade your sugar-gem? (ask/trade) ")
choice5 = choice5.strip().lower()

if choice5 == "ask":
    xp += 10
    snack_points += 1
    # Demonstrating .capitalize() when echoing the player's choice
    print(f"\nYou politely ask the Imp. It {choice5.capitalize()}s and hands over the biscuit.")
    end_game(success=True)

elif choice5 == "trade":
    # Remove sugar-gem, grant biscuit
    if "Sugar-Gem" in inventory:
        inventory.remove("Sugar-Gem")
        snack_points += 1
        xp += 5
        # Demonstrating .upper() on success message
        print("\nTRADE COMPLETE: The Imp nods and hands you the biscuit.")
        end_game(success=True)
    else:
        print("\nYou have nothing to trade! The Imp vanishes, taking the biscuit.")
        end_game(success=False)

else:
    print("\nThe Imp is confused by your answer and zaps you out. Biscuit gone.")
    end_game(success=False)
