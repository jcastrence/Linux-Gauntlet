import random, sys

def getCommands(filename):
    with open(filename, 'r') as file:
        commands = {}
        commandStrings = file.readlines()
        
        for commandString in commandStrings:
            commandName, commandDescription = commandString.strip().split(sep='|')
            commands[commandName] = commandDescription

        return commands

def printCorrect():
    responses = [
            "Correct!",
            "Nice work!",
            "Good job!",
            "Excellent!",
            "That's right!",
            ]
    print(responses[random.randint(0, len(responses) - 1)])

def printWrong():
    responses = [
            "Not quite...",
            "That's not right...",
            "Try again...",
            "Hmmm...",
            "Let's try another...",
            ]
    print(responses[random.randint(0, len(responses) - 1)])

def correct():
    pass

def wrong():
    pass

def printTitle():
    title_filename = "title.txt"
    with open(title_filename, 'r') as title_file:
        print(title_file.read())

def printGauntletStart():
    filename = "gauntlet_start.txt"
    with open(filename, 'r') as file:
        print(file.read())

def printVictory():
    filename = "victory.txt"
    with open(filename, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    commands = getCommands("descriptions.txt")
    commandNames = list(commands.keys())

    printTitle()

    print("""Welcome to Linux Gauntlet!
          
In this game, there are 85 rounds and 85 Linux commands. In each round, you will get the description of an action you can perform in Linux. Your goal is to type the correct Linux command that performs the described action.

Type the correct command to advance to the next round.

Type the wrong command and lose a life.

You get 3 lives. Once your lives reaches 0, the game is over! Can you make it to the end?""")

    while True:
        print("\nPress y when you're ready!")
        ready_response = input().lower()
        while ready_response != 'y' and ready_response != 'yes':
            print("Press y when you're ready!")
            ready_response = input().lower()
        
        printGauntletStart()
    
        rounds, correct_count, wrong_count = 0, 0, 0
        lives = 3
        total_command_count = len(commandNames)
        command_indices = list(range(total_command_count))
        random.shuffle(command_indices)

        wrong_responses = []
    
        while lives > 0 and rounds < 86:
            rounds += 1
            commandName = commandNames[command_indices[rounds - 1]]
            commandDesc = commands[commandName]
    
            print(f"======= Round: {rounds}    Lives: {lives}    Correct: {correct_count}    Wrong: {wrong_count} =======")
            print(f"Action: {commandDesc}")
            response = input("> ").strip()
            print()
    
            if response == commandName:
                printCorrect()
                correct_count += 1
            else:
                printWrong()
                wrong_count += 1
                lives -= 1
                print(f"Expected Command: {commandName}")
                wrong_responses.append((response, commandName))
    
            print()
    
        if lives == 0:
            print("You ran out of lives! Better luck next time!")
        else:
            printVictory()
            print("\nCongratulations! You finished the Linux Gauntlet!")

        print("\n======= Game Stats =======\n")
        print(f"Total Rounds: {rounds}    Lives Left: {lives}    Total Correct: {correct_count}    Total Wrong: {wrong_count}\n")
        if lives < 3:
            print("======= Loss Rounds Recap =======\n")
            for response, answer in wrong_responses:
                print(f"Command Description: {commands[answer]}")
                print(f"Command Name: {answer}")
                print(f"Your Response: {response}\n")


            
        print("\nWant to play again? (y/n)")
        continue_response = input().strip().lower()
    
        if continue_response != 'y' and continue_response != 'yes':
            print("\nThanks for playing!")
            sys.exit(0)
    
