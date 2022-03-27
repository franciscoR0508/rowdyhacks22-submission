import dataScraper

def welcomeMsg():
    print("""Welcome to On the Spot!
In this game, we will test your music knowledge, using YOUR music!
Let's get started...""")

def goodbyeMsg():
    print("Thanks for playing!")


userNameScore = {}

question1 = "1"
question2 = "2"
question3 = "3"
question4 = "4"
question5 = "5"
questionList = [question1, question2, question3, question4, question5]

def main():
    welcomeMsg()
    while True:
        playListInfo = dataScraper.get_playlist('3r4wfURTAooB0Hapr6epub')
        # PlayListInfo = {artist_name : {album_name : track_name}}
        count = 0
        for key in playListInfo:
            artist_name = key
            album_song_dict = playListInfo[key]
            for key2 in album_song_dict:
                album_name = key2
            for value2 in album_song_dict.values():
                track_name = value2
            questionList[
                count] = "What song by " + artist_name + " is in the album " + album_name + "? a.) " + track_name + " or b.) BabyShark"
            count += 1
        #Getting the user started:
        userPoints = 0
        userName = input("Enter a Username, or \'q\' to Quit: ")
        if userName == "q":
            goodbyeMsg()
            break

        #Question 1:
        while True:
            answer1 = input("\n"+questionList[0])
            if answer1 == "a":
                print("Correct!\n")
                userPoints += 1
                break
            elif answer1 == "b":
                print("Dummy!\n")
                break
            else:
                print("Oops! Type \'a\' or \'b\' as your answer.")

        #Question 2:
        while True:
            answer2 = input(questionList[1])
            if answer2 == "a":
                print("Correct!\n")
                userPoints += 1
                break
            elif answer2 == "b":
                print("Dummy!\n")
                break
            else:
                print("Oops! Type \'a\' or \'b\' as your answer.")

        #Question 3:
        while True:
            answer3 = input(questionList[2])
            if answer3 == "a":
                print("Correct!\n")
                userPoints += 1
                break
            elif answer3 == "b":
                print("Dummy!\n")
                break
            else:
                print("Oops! Type \'a\' or \'b\' as your answer.")

        #Question 4:
        while True:
            answer4 = input(questionList[3])
            if answer4 == "a":
                print("Correct!\n")
                userPoints += 1
                break
            elif answer4 == "b":
                print("Dummy!\n")
                break
            else:
                print("Oops! Type \'a\' or \'b\' as your answer.")

        #Question 5:
        while True:
            answer5 = input(questionList[4])
            if answer5 == "a":
                print("Correct!\n")
                userPoints += 1
                break
            elif answer5 == "b":
                print("Dummy!\n")
                break
            else:
                print("Oops! Type \'a\' or \'b\' as your answer.")

        #Points Tallying:
        print("You earned ", str(userPoints), " points!")
        if userPoints == 0:
            print("Oof! Do better!\n")
        elif userPoints == 1:
            print("Try again to get better!\n")
        elif userPoints == 2:
            print("Not the worst!\n")
        elif userPoints == 3:
            print("Pretty good!\n")
        elif userPoints == 4:
            print("Nice!\n")
        else:
            print("You're goated with the sauce!\n")

        #Leader Score Board:
        userNameScore[userName] = userPoints
        print("Leaderboard:")
        for nameUser, scoreUser in userNameScore.items():
            print(nameUser, scoreUser)
        print("")

        playAgain = input("To play again, press <Enter>; to Quit, press q: ")
        if playAgain == "q":
            goodbyeMsg()
            break

if __name__ == "__main__":
    main()
