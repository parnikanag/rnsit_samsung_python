def min_coins_notes(amount):
    currency = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  
    print("Coins and Notes Required:")
    for note in currency:
        if amount >= note:
            count = amount // note
            print(note, ":", count)
            amount %= note  

amount = int(input("Enter the amount: "))
min_coins_notes(amount)

