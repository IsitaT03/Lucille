'''
Wedding Bouquet Flowers:
Chervil: Sincerity
Honeysuckle: Generous and devoted affection.
White and Red Roses: Unity
'''
import random

#flag variables
correct_tally = 0
good_ending = True
easy_mode = False

##FUNCTIONS
def action(prompt):
    action = " "
    while action != "x" and action != "X":
        string = "ACTION: Press x to " + prompt + ": "
        action = input(string)

def choice(choice_list, output_list):
    global correct_tally
    print("CHOICE: Select from the following options: ")
    #first choice of choice_list always correct
    dict_choice = dict(zip(range(1,len(choice_list)+1),choice_list))
    print_choices = list(dict_choice.keys())
    random.shuffle(print_choices)
    count  = 1
    for choice in print_choices:
        print("Press ", count, " to ", dict_choice[choice])
        count+=1
    user_choice = int(input("Your choice, please? "))
    if user_choice > len(output_list):
        print("Don't do that, Lucille. Please listen to the choices I give you? It won't end well if you don't.")
        correct_tally-=1
        return False
    print(output_list[print_choices[user_choice-1]-1])
    if print_choices[user_choice-1]-1 == 0:
        correct_tally+=1
        return True
    else:
        correct_tally-=1
        return False

def rock_paper_scissors():
    print("MINIGAME: Let's Play Rock, Paper, Scissors!")
    moves = {1: "Rock", 2: "Paper", 3: "Scissor"}
    computer_choice = random.randint(1, 3)
    user = (int)(input("Press 1 for Rock.Press 2 for Paper.Press 3 for Scissors."))
    if (computer_choice == user):
        print("You had a tie!")
    elif (computer_choice == 1 and user == 3) or (computer_choice == 2 and user == 1) or (computer_choice == 3 and user == 2):
        print("You lost, silly goose!")
    else:
        print("You won, Lucille! How grand!")

def guessing_game():
    print("MINIGAME: Let's Play A Guessing Game! I'm thinking of a number from 1 to 13~")
    computer_choice = random.randint(1, 13)
    user = 0
    user = (int)(input("Guess a number: "))
    while user != computer_choice:
        if user > computer_choice:
            print("Guess lower!")
        else:
            print("Guess higher!")
        print("Try again, silly goose!")
        user = (int)(input("Guess a number: "))
    print("You've got it, Lucille! You're smart as a whip!")

# code taken from my own Python Practice 2, written from scratch
def guess_word():
    print("MINIGAME: Let's Play A Word Game! I'm thinking of a 4 letter flower (lowercase), it starts with an eye~")
    key_code = "iris"
    guess = "==="
    while guess != key_code:
        guess = str(input("Please enter a guess: "))
        if(len(guess) != 4):
            print("4 letters please")
            continue
        right = 0
        wrong = 0
        for i in range(len(key_code)):
            if guess[i] == key_code[i]:
                right+=1
            else:
                wrong+=1
        print(right, " correct, ", wrong," wrong")

    print("You did it, Lucille!")



# Intro
print("Welcome to Lucille, an interactive python text-based choose-your-own adventure game.\nPlease enjoy yourself and remember. Love makes you do irrational things.")
print("Before we begin, we give you a choice, the only one in this game that is not meant to toy with your mind.")
print("Press e to play in easy mode, where you will be told if you've chosen an answer leading you to a good ending or bad ending.")
print("Press n to play in normal mode, where you will be NOT told the impact of your decisions")
user_mode = input("Which experience do you wish for? Press n or e: ")
if user_mode == "e" or user_mode == "E":
    print("You have chosen easy mode.")
    easy_mode = True
elif user_mode == "n" or user_mode == "N":
    print("You have chosen normal mode.")
    easy_mode = False
else:
    print("Why did you not listen to me? I said only two letters. I suppose it means you don't want my help.")
    print("You have chosen normal mode.")
    easy_mode = False
if easy_mode:
    print("CORRECT choices will lead you to a good ending. INCORRECT choices to the bad ending.")
    print("You can get one or none of the three choices wrong and still win, I am quite forgiving after all.")
print("\n=========================================\n")
real_name = ""
print("You are lying in the University Berkeley Botanical Garden, \
the just setting sun just barely tickling your eyes. You sit up next to a student's belongings,\n\
a water flask, notebooks, and a filled satchel. What is your name?") 
real_name = input("\n...What is your name? Please, remember your name? ")
if real_name == "Lucille" or real_name == "lucille":
    print("Aha~ What a smart little thing you are. Continue, continue, I have no more to say. But darling, \
 where's your bouquet? You're to be married at the first moonlight!")
else:
    print("You silly goose, that's not your name! Your name is Lucille! But darling,\
where's your bouquet? You're to be married at the first moonlight!")
action("look for your bouquet")
print("You can't see anything slightly reminscent of a bouquet and you certainly aren't carrying one.")
print("You'd better find that bouquet, precious! You can't be late to your own wedding, how unlucky that would be...")
print("While there isn't a bouquet in sight, there is an abundance of flowers, \
though they are still attached to their stems. It'd be easy to just pick them,\
 a quick pinch and pull. \nYou can't be late to your wedding after all...")
action("start looking for flowers")

#Body 
print("\n=========================================\n")
print("You walk through the garden for a while trying to remember what \
flowers were in the bouquet. Obviously, ones that meant love, adoration, but which ones?")
print("You come across a Pieris Rapae butterfly flitting around you, cream colored and small, what do you do?")
check_first = choice(['wait for it to land on a leaf and outstretch your finger for it to \
land', 'follow where it flits, careful not to lose sight', 'ignore it, what \
use is it to chase after butterflies when you have so many in your stomach? \
You\'re getting married!'], ['The butterfly lands on a leaf and inches onto \
you, splindly legs tickling your fingertip. Then, it flutters over to a bush\
 of Chervil. You remember Kate Greenaway wrote it meant sincerity,\nwhat a \
perfect representation of the feelings in both your and your \
darling love\'s heart.', 'You try to follow the butterfly but it soon disappears, far too fast for you.\
 Sometimes you wonder, when you were a child, wasn\'t it easier?', 'You let the butterfly pass, at ease with your lack of\
 distraction. Your wedding is far more important.'])
if check_first:
    if easy_mode:
        print("HINT: This was the CORRECT choice. You acquired flowers for your bouquet.")
    action("pick a few Chervil leaves and continue on")
else:
    if easy_mode:
        print("HINT: This was an INCORRECT choice. You did NOT acquire flowers for your bouquet.")
    action("continue on")

#MINI GAME 1
print("\n=========================================\n")
rock_paper_scissors()
print("\n=========================================\n")

print("You admiring a Vanessa annabella butterfly, orange with artiful blotches and dots of black and white, when suddenly, a rattlesnake appears, slithering out from a nearby bush, your heart trembles in\
 fear as you hear the hissing and rattling. Time is of the essence, what do you do?")
check_second = choice(['Lie down on the ground and close your eyes.', 'Stab it with a fallen branch within hand\'s reach\
', 'Calmly walk away, you suppose it is much more scared of you than you are of it.'],['\
The snake slithers onto you and you wonder just what has possessed you. You dare open your eyes for but a moment to see a beautiful man with golden,\
 serpentine cuffs curving around taut,\nmuscled arms. He cups your cheek and gives you a bunch of Honeysuckle, admitting that he is a touch jealous\
 you will not be his. And before you can say a word, he disappears in sparkling light and\nthe sound of a conch.', 'Somehow, you are just fast enough.\
 The snake twitches in its dying moments and then slumps. Its eyes look oddly human,\
 but the hint of regret is washed away by a flood of relief.', 'The snake does not follow, darting back into the shade of the bushes. You suppose\
 this could be a story to tell over tea on a lazy afternoon of married life.'])
if check_second:
    if easy_mode:
        print("HINT: This was the CORRECT choice. You acquired flowers for your bouquet.")
    action("clasp the Honeysuckle to your heart and continue on")
else:
    if easy_mode:
        print("HINT: This was an INCORRECT choice. You did NOT acquire flowers for your bouquet.")
    action("continue on")

#MINI GAME 2
print("\n=========================================\n")
guessing_game()
print("\n=========================================\n")


print("Rather flustered by your last encounter, you find a bench to rest on and smile at the sight of a Erynnis tristis butterfly,\
 mottled all shades of brown with a delicate white fringe. You see a bunch of white roses, remembering fondly the meaning \'I am worthy of you.\'.\
 You muse that worthiness is born of sacrifice in a brief bout of philosophical pondering. What do you do?")
check_third = choice(["wrap your fingers around the stem, sharpest thorns and all and pick one.", "tear only the bloom and the willow green stretch\
 of stem that remains thorn free.", "ignore the roses, you have no clippers and if you got blood on you before the wedding, you can't imagine it \
would be good luck."],["The thorns pierce your skin, carving a line on your palm, blood pooling in beads and then staining the petals of the rose with\
 speckles of red. Red and white roses mean unity, perhaps even more fitting than worthiness. The pain in your hand is barely perceptible as you remember\
 just how close your unity is. In your haste, your hand catches on the thorns, and a thin, jagged cut bleeds on your palm.", "The rose you pick, though it is easy to wrench away is too short for a bouquet, you are forced to throw it on the ground.\
", "You can't help yourself from taking just one look at the roses, cupping them for a moment, but wincing as you accidently\
 cut your palm against the thorns. No matter, this can easily be bandaged later, the wedding is most important. Your steps\
 are fast, almost as if you are floating on clouds, little puffs guiding your steps to wedding bells."])
if check_third:
    if easy_mode:
        print("HINT: This was the CORRECT choice. You acquired flowers for your bouquet.")
    action("kiss the Red and White Roses and continue on")
else:
    if easy_mode:
        print("HINT: This was an INCORRECT choice. You did NOT acquire flowers for your bouquet.")
    action("continue on")

#MINI GAME 3
print("\n=========================================\n")
guess_word()
print("\n=========================================\n")

#Conclusion
print("Aha, Lucille you've arrived! Do you have your bouquet? I have a ribbon waiting for those pretty blooms. I wonder if you saw any butterflies in the garden.\n\
I do quite like them.")
action("show me the bouquet")
if correct_tally > 0:
    print("My goodness Lucille, they look so beautiful, and you'll be an even more beautiful bride with them in your hands. Come, come, your happiest moment awaits!")
    action("continue on")
    print("You blink and look around, the sun just gone below the horizon. You're nowhere near your things, weren't you studying for a CS61A final? Yes, yes you were!")
    action("continue on")
    print("You weave through the garden and find your waterbottle, notes, and tote bag signed \'Belongs To " + real_name + "' abandoned. In your haste to pick them up, you barely\
 notice that your bag stains red when you grip the strap. There's a cut there. You'll have to get out of here and ask for a bandaid. It's funny how\
 the garden seems to remove you from your life, it's almost like you're not even in the present, drifting through the dreams of an idyllic past.")
    action("to continue, for the last time, " + real_name)
else:
    print("Lucille, Lucille, Lucille ... didn't I tell you that you need a bouquet? How do you expect to walk the aisle?")
    print("Silly goose, I told you to listen, oh Lucille, why didn't you listen?")
    action("continue on")
    print("You have to keep looking, you need those flowers, the marriage, you need it, you need it so bad you'll spend your whole life in this garden for them. \
There's nothing else you can do, nothing at all. It's the only thing left in your heart. The sun sets, leaving you shrouded in darkness, tears on your cheeks.")
    action("continue on")
    print("There is a WarnMe notice, that a UC Berkeley Student named " + real_name + " has disappeared in the Botanical Garden. Weeks pass, and search\
 parties soon begin to dwindle in size. No one finds " + real_name + ". But sometimes, after sun set, a student might meet someone named Lucille,\
 with a bleeding scar on their palm. Those silly gooses never come back.")
    action("to continue, for the last time, Lucille")

print("\n=========================================\n")

print("Thank you for playing Lucille! I hope you liked it! This was created by Isita Talukdar from scratch at CS Kickstart 2022.")
print("Flower meanings were taken from \"Language of Flowers\" by Kate Greenaway (1884)")