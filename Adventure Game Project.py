from operator import truediv
import random
def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)
    # This function will print a message and pause the program to easily read it
score = 0 # This will be the score of the game but for show only i made the game depend on the story path
# This game is about a young boy and his brother. They are great team and always beat the enemies. They are very strong and smart team. They are going to find their brother who is lost in the forest. They are going to face many challenges and decisions. They have to make right choices otherwise they will lose the game. They will learn a lot about their strengths and weaknesses. They will find their brother at the end. Enjoy the game!
while True:
    import time
    time.sleep(1)
    print("Once upon a time, you and your brother were a great team")
    time.sleep(2)
    print("that could defeat all the enemies standing against you, day after day you and your brother made friends they are side by side to you on every step you take")
    time.sleep(3)
    team_names = ["the Ghosts", "the punishers","the cathers","the killers"]
    team_name = random.choice(team_names)
    print(f"You and your brother are leading {team_name}")
    # Here i put a random choice of team names to every time the user ply a different name is printed 
    time.sleep(3)
    print("You as a leader to the team what the first decision ?")
    while True:
                choice = int(input("1. Start a very hard mission\n2. Ask your dad what to do\n3. Go play with your brother\n"))
                if choice not in [1, 2, 3]: # This will make sure that the user can only enter 1, 2 or 3
                 print("Please enter 1, 2 or 3 only")
                 time.sleep(2)
                else:
                 break
    if choice == 1:
         score == score-1
         print("When you start a very hard mission that needs very high skills and you don't have these skills so you went to the town and the police there was finding a group of people to help them catch someone dangerous so you and your team helped them but your brother got stabbed by someone and your father knew but thank God he helped him and cured him and you got punished")
         time.sleep(4)
         print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}")
         print("you lost the game")
         play_again = input("Do you want to play again? (yes/no): ")
         if play_again.lower() != "yes":
          break
    # The above code is a part of the game's story. It's a series of questions and choices that will lead to different outcomes. The player will make choices and the game will provide feedback based on the choices made. The story will continue until the player decides to quit the game. The code is well structured and easy to understand. It's a great example of using loops and conditionals to create a game.
    elif choice == 2:
          score == score+3
          print(" your dad told you that you're still very young to do anything so he ordered you to stay and do nothing")
          time.sleep(2)
          choice = int(input("1. Listen to your dad\n2. Don't listen and do what is in your head\n"))
          time.sleep(2)
          if choice not in [1, 2]:
            print("Please enter 1 or 2 only")
            break  
          elif choice == 1:
            score == score-1 
            print("you have listened to your dad so you stayed at home")
            time.sleep(2)
            print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                 break
          elif choice == 2:
            score == score+1
            print(" you sneak out of your home with your team and go find a mission to do  On your way you found someone hate your team and started a fight with him and at the end you kicked his head and you have now to decision")
            time.sleep(2)
            choice = int(input("1. Kill him\n2. Forgive him\n"))
            if choice not in [1, 2]:
                    print("Please enter 1 or 2 only")
                    time.sleep(2)
                    break
            elif choice == 1:
                score == score-1
                print("after you killed him your dad knew what you had done and came to you and you were punished for staying at home for at least 2 weeks")
                time.sleep(4)
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() != "yes":
                     break 
            elif choice == 2:
                   score == score+3
                   print("after you forgived him he became your friend and joined your team You have reached the town and you found to things to do")
                   time.sleep(2)
                   places=["a very fancy apartment", "a very fancy villa", "a castle"]
                   places=random.choice(places) # Randomly choosing one of the places
                   helping = ["a very rich family", "a poor family", "some people with moving furniture"]
                   helping = random.choice(helping)
                   choice = int(input(f"1.Stealing {places}\n2. Help {helping} \n"))
                   time.sleep(2)
                   if choice not in [1, 2]:
                       print("Please enter 1 or 2 only")
                       time.sleep(2)
                   if choice == 1:
                         score == score-1
                         print(f"you went to the {places} and started to steal all the rare things that have a value but the police finds out and took you for prison")
                         print("you have lost the game")
                         print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}")
                         play_again = input("Do you want to play again? (yes/no): ")
                         if play_again.lower() != "yes":
                          break
                       
                   elif choice == 2:
                         score == score+3
                         print(f"you helped {helping} and gained some money and you went back to your dad and proved to him that you're a very big boy and he is very proud of you")
                         print("Congratulations! You have won the game!")
                         print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}") 
                         play_again = input("Do you want to play again? (yes/no): ")
                         if play_again.lower() != "yes":
                          break
    elif choice == 3:
        time . sleep(2)         
        print("You went with your brother to a playing area and you had a really Joyable time after a while you and your brother got hungry and there are plenty of restaurants here so... ")
        time . sleep(2)
        food = random.choice(["sushi", "pizza", "burger", "shawerma"])
        print(f"You decided to eat {food}")
        time . sleep(2)
        print("After you had eaten you and your brother went for an adventure in the forest.. after plenty of time you reached a really beautiful lake and you sat beside it for a while Your brother asked you if he can go swimming or not ? ")
        time . sleep(2)
        while True:
            choice = input("1.you agreed\n2 you refused \n") 
            if choice not in ["1", "2"]:
                print("Please enter 1 or 2 only")
            else:
                break
        if choice == "1":
                score = score - 2
                print("you agreed to let him go swimming and after that he had so much fun with the water but suddenly he started to scream something is catching his legs and he is shouting for your help and you went in water although you are scared of water and helped him at the last second for losing him after all of that you went back home ")
                time.sleep(5)
                print("you have lost the game")
                print(f"Your score is {sum(filter(lambda x: x == 0, [score]))}")
                while True:
                 play_again = input("Do you want to play again? (yes/no): ")
                 if play_again.lower() == "yes":
                  break
        elif choice == "2":
                score = score + 2
                print(" you refused to let him so he got very angry and stayed beside you and you slept after a short time you awakened and you can't find your brother...he disappeared but you have decided to go look for him and you have searched all the forest until you found something his socks so... ")
                time.sleep(4)
                choice = input("1. There is a high way to a mountain \n2. There is a low way to another forest\n")
                time.sleep(3)
                if choice not in ["1", "2"]:
                 print("Please enter 1 or 2 only")
                 time.sleep(2)
                if choice == "1":
                 score = score + 2
                 print(" after you head up to the mountain a huge rock was very close to knocking you on the ground but thank god it didn't hit you...You continue walking until you find a big dog that is staring at you...")
                 time.sleep(4)
                 choice = input("1. You go back \n2. You move forward to the dog to kiss him \n")
                 time.sleep(3)
                 if choice == "1":
                  score = score - 2
                  print("there is a huge rock like the one in the past and this time it hit you and you can't move anywhere now until someone has found and returned you to the town")
                  time.sleep(3)
                  print("you have lost the game")
                  time.sleep(2)
                  print(f"Your score is {sum(filter(lambda x: x == 0, [score]))}")
                  play_again = input("Do you want to play again? (yes/no): ")
                  if play_again.lower() != "yes":
                    break 
                 elif choice == "2":
                    score = score + 2
                    print("you went for him and kissed him and you and the dog became friends now and started to look for your brother again but now you lit your dog sniff the socks to help you after a while you found your brother finally. ")
                    time.sleep(2)
                    print("Congratulations! You have won the game!")
                    print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}")
                    time.sleep(3)
                    play_again = input("Do you want to play again? (yes/no): ")
                    if play_again.lower() != "yes":
                         break 
            
                elif choice == "2":
                     score = score - 1
                     print("You went the low way heading to the forest then you walked for too long until you found yourself at the lake and then you walked until you reached the lake again ! You are in a maze ! ")
                     time.sleep(3)
                     print("There is a new sign shown in front of you that says : if you need to exit be the exit. You didn't understand something but you have found a key in your pocket so this means that something needs to be opened by this key") 
                     time.sleep(6)
                     print("so you have searched a lot but you didn't find something so an old man has just started to show in front of you and he helped you by telling you the use of the key he was having a secret box to open by this key")
                     time.sleep(5)
                     choice = input("1. Open the box\n2. Leave him because you found something weird\n")
                     if choice not in ["1", "2"]:
                      print("Please enter 1 or 2 only")
                      time.sleep(2)
                     if choice == "1":
                        score = score + 2
                        print(" you opened it and you found a glass ball that shows where is your brother ")
                        time.sleep(1)
                        print("you went for him and used the glass ball as a map until you found him")
                        time.sleep(3)
                        print("Congratulations! You have won the game!")
                        print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}")
                        play_again = input("Do you want to play again? (yes/no): ")
                        if play_again.lower() != "yes":
                           break
                     elif choice == "2":
                      score = score - 2
                      print(" you left him and stayed in the forest all your life")
                      time.sleep(1)
                      print(f"Your score is {sum(filter(lambda x: x > 0, [score]))}")
                      if sum(filter(lambda x: x < 0, [score])) :
                        print("you lost the game")
                        play_again = input("Do you want to play again? (yes/no): ")
                        if play_again.lower() != "yes":
                         break 
                      else :
                        print("you won the game")    
                        play_again = input("Do you want to play again? (yes/no): ")
                        if play_again.lower() == "yes":
                         break 
                         
# This is the end of the game. The player has reached the goal and their journey comes to an end. The player has made choices and decisions that have led them to this point. They have learned and grown from their experiences. The player can choose to play again or choose to end the game. It is a great feeling to have completed a game and to have learned something new.
