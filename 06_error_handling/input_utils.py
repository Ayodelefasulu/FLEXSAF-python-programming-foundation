def get_score():
    try: 
        scores = int(input("Enter score: "))
    except ValueError:
        print("Please enter a whole number")
        raise SystemExit(1)

    return scores
        


