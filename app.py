from cover_generator import generate_card_images
from text_generator import generate_card_text


def main():
    reason = input("What is this card for? ")
    person = input("Who is this card for? ")
    likes = input("What does this person like? (optional) ")
    tones = input("What tones do you want to use? (optional) ")
    orientation = input(
        "What orientation do you want? (optional, portrait / landscape, default : portrait)"
    )
    clean = input("do you want the images to be cleaned? (y/n) ")

    while True:
        print()
        print("Message : " + generate_card_text(reason, person, likes, tones))
        print()

        card_images = generate_card_images(reason, orientation, clean)
        if clean == "y":
            original_cleaned = card_images["cleaned"]
            upscale_cleaned = card_images["cleaned_upscale"]
        else:
            original_cleaned = "None"
            upscale_cleaned = "None"

        print(
            f"Original: {card_images['original']}",
            f"Original + Cleaned: {original_cleaned}",
            f"Upscale: {card_images['original_upscale']}",
            f"Upscale + Cleaned: {upscale_cleaned}",
            sep="\n\n",
        )
        print()
        regenerate = input("Try again ? (y/n)")
        regenerate = regenerate.lower().strip()

        if regenerate == "n":
            break


if __name__ == "__main__":
    main()
