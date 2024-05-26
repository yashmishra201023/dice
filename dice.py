import random


response = "y"

while response == "y":
    
    no = random.randint(1, 6)
    
    
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[*    ]")
        print("[     ]")
        print("[    *]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[*    ]")
        print("[  *  ]")
        print("[    *]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[*   *]")
        print("[     ]")
        print("[*   *]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[*   *]")
        print("[  *  ]")
        print("[*   *]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[* * *]")
        print("[     ]")
        print("[* * *]")
        print("[-----]")
    
    response = input("Do you want to roll the dice again? (y/n): ").lower()
    while response not in ["y", "n"]:
        response = input("Invalid input. Please enter 'y' to roll again or 'n' to stop: ").lower()
