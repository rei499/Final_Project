import random
import os

money = 0
friendship = 50
knowledge = 50


while True:
    os.system('cls')
    print("=" * 30)
    print("          HELL WEEK")
    print("=" * 30)

    print("\nThe final exam will be next week, you have exactly 7 days to earn ₱1000.0 and to prepare for the exam.")
    user_input = input("Please type ENTER to continue... ").upper()

    if user_input == "ENTER":

        while True:
            os.system('cls')
            print("[Day 1]\nYou still have an unpaid balance and your promissory note has been rejected.")
            print("For you to pay your balance, you plan to sideline as a rider.")
            print("But before leaving, your friends invite you to play basketball.")
            print("\nWhat will you choose?")

            print("\nChoose your path:")
            print("[1] - Sideline as a rider to pay tuition\n      (Money+150)")
            print("[2] - Go with your friends to play basketball\n      (Friendship+10)")

            path = input("\nEnter choice: ")


            if path == "1":
                os.system('cls')
                print("\nYour friends left and started to say something about you...\nYou can't clearly hear what they're saying...")
                print("\nYou worked for 4hrs and managed to earn ₱150.0!\nBut...A stranger offers you a risky booking.")
                money += 150

                choice1 = input("\nAccept it? [Yes or No]: ").upper()


                if choice1 == "YES":
                    os.system('cls')
                    print("\nOh no! There was a checkpoint and you got apprehended. You paid a fine.")
                    print("(Money-100)")
                    money -= 100
                    print("\n--- CURRENT STATUS ---")
                    print(f"Money = P{money}")
                    print(f"Knowledge = {knowledge}")


                elif choice1 == "NO":
                    print("\nYou chose to do the right thing.")
                    print("You refused the risky booking.")






            #         print("\n--- CURRENT STATUS ---")
            #         print(f"Money = P{money}")
            #         print(f"Knowledge = {knowledge}")

            #         print("\nUnfortunately, your tuition remained unpaid.")

            #     else:
            #         print("\nInvalid choice.")

            # # ==================================================
            # # SITUATION 2
            # # ==================================================

            # elif path == "2":

            #     print("\nYour friends invited you to play basketball.")
            #     print("But final exams are tomorrow.")

            #     choice2 = input("\nStudy or Play? (STUDY/PLAY): ").upper()



            #     if choice2 == "STUDY":

            #         print("\nYou stayed home and reviewed your lessons.")

            #         knowledge += 30
            #         loyalty -= 10


            #     elif choice2 == "PLAY":

            #         print("\nYou played basketball with your friends.")

            #         loyalty += 30
            #         knowledge -= 10

            #     else:
            #         print("\nInvalid choice.")

            #     print("\nEXAM DAY HAS ARRIVED.")

            #     print("\n--- CURRENT STATUS ---")
            #     print(f"Knowledge = {knowledge}%")
            #     print(f"Loyalty = {loyalty}%")

            #     print("\nDuring the exam, you saw your friends cheating.")

            #     final_choice = input("\nReport or Cover for them? (REPORT/COVER): ").upper()


            #     if final_choice == "REPORT":

            #         print("\nYou reported the cheating incident.")
            #         print("The professor praised your honesty.")

            #         integrity += 20
            #         loyalty -= 20


            #     elif final_choice == "COVER":

            #         print("\nYou covered for your friends.")
            #         print("Your friends appreciated your loyalty.")

            #         loyalty += 20
            #         integrity -= 20

            #     else:
            #         print("\nInvalid choice.")

            #     print("\n--- FINAL RESULT ---")
            #     print(f"Integrity = {integrity}%")
            #     print(f"Knowledge = {knowledge}%")
            #     print(f"Loyalty = {loyalty}%")

            # else:
            #     print("\nInvalid path.")

            # retry = input("\nDo you want to try again? (YES/NO): ").upper()

            # if retry == "NO":
            #     print("\nTHANK YOU FOR PLAYING!")
            #     break

            print("\nRestarting game...\n")

        break

    else:
        print("\nInvalid input. Please type ENTER.\n")
