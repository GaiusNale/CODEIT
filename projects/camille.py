# A terminal based program that takes input from the user and tells them what chinese zodiac sign they are and the descpription of their zodiac sign(personality)

""""Create a dictionary that contain the zodiac signs and the corresponding personality
Ask of the users input 
conditional staement that picks the year and prints out the personality"""

# A dictionary containing all the zodiac personalities
zodiac_signs = {
    "Rat": "Quick-witted, resourceful, and versatile. You are also charming and outgoing.",
    "Ox": "Diligent, dependable, strong, and determined. You are also methodical and patient.",
    "Tiger": "Brave, competitive, and confident. You have a strong sense of justice and are natural leaders.",
    "Rabbit": "Gentle, quiet, and elegant. You are compassionate and responsible.",
    "Dragon": "Confident, intelligent, and enthusiastic. You are natural leaders and charismatic.",
    "Snake": "Enigmatic, wise, and graceful. You are deep thinkers and talented.",
    "Horse": "Energetic, independent, and impatient. You love freedom and adventure.",
    "Goat": "Calm, gentle, and sympathetic. You have a strong sense of justice and are very creative.",
    "Monkey": "Witty, intelligent, and playful. You are curious and have a strong desire to learn.",
    "Rooster": "Observant, hardworking, and courageous. You are straightforward and honest.",
    "Dog": "Loyal, honest, and cautious. You are known for your strong sense of responsibility.",
    "Pig": "Generous, compassionate, and diligent. You are known for your calm nature and good manners."
}
# A list containing the Zodiac signs
zodiac_cycle = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

# This function basically takes the year they were born and divides it by 12 looking for the remainder which will always correspond to the zodiac sign
def get_zodiac_sign(year):
    index = (year - 1924) % 12
    return zodiac_cycle[index]

def main():
    year = int(input("Enter the year you were born: "))

    zodiac_sign = get_zodiac_sign(year)

    # print out the result 
    print(f"Your Chinese zodiac sign is: {zodiac_sign}")
    print(f"Your personality is {zodiac_signs[zodiac_sign]}")

if __name__ == "__main__":
    main()

# This was fun 
