from cover_generator import generate_card_images
from text_generator import generate_card_text


def main():
    while True:
        reason = input("What is this card for? ")
        person = input("Who is this card for? ")
        likes = input("What does this person like? (optional) ")
        tones = input("What tones do you want to use? (optional) ")
        orientation = input(
            "What orientation do you want? (optional, portrait / landscape, default : portrait)"
        )
        clean = input("do you want the images to be cleaned? (y/n) ")

        print()
        print("Message : " + generate_card_text(reason, person, likes, tones))
        print()

        card_images = generate_card_images(reason, orientation, clean)
        if clean == "y":
            original_cleaned = card_images["cleaned"]
            upscaled_cleaned = card_images["cleaned_upscaled"]
        else:
            original_cleaned = "None"
            upscaled_cleaned = "None"

        print(
            f"Original: {card_images['original']}",
            f"Original + Cleaned: {original_cleaned}",
            f"Upscaled: {card_images['original_upscaled']}",
            f"Upscaled + Cleaned: {upscaled_cleaned}",
            sep="\n\n",
        )
        regenerate = input("Try again ? (y/n)")
        regenerate = regenerate.lower().strip()

        if regenerate == "n":
            break


if __name__ == "__main__":
    main()
