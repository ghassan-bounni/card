import os
import logging
import numpy as np
from flask import Flask, request, render_template
from cover_generator import generate_card_images
from text_generator import generate_card_text
from const import occasion_keyword_map

app = Flask(__name__)

data = {
    "reason": "",
    "person": "",
    "likes": "",
    "tone": "",
    "orientation": "",
    "clean": "",
}


def generate(reason, person, likes, tones, orientation, clean):
    message = generate_card_text(reason, person, likes, tones)

    print("Waiting for images to be generated...")
    card_images = generate_card_images(occasion_keyword_map[reason], orientation, clean)
    if clean == "y":
        cleaned = card_images["cleaned"]
        upscale_cleaned = card_images["cleaned_upscale"]
    else:
        cleaned = "None"
        upscale_cleaned = "None"

    return (
        message,
        card_images["original"],
        cleaned,
        card_images["upscale"],
        upscale_cleaned,
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_cards():
    logging.info("Generate request received!")
    data["reason"] = request.form["reason"]
    data["person"] = request.form["person"]
    data["likes"] = request.form["likes"]
    data["tone"] = request.form["tone"]
    data["orientation"] = request.form["orientation"]
    if "clean" in request.form.keys():
        data["clean"] = request.form["clean"]
    else:
        data["clean"] = "n"

    reason, person, likes, tone, orientation, clean = data.values()

    message, original, cleaned, upscale, upscale_cleaned = generate(
        reason, person, likes, tone, orientation, clean
    )

    return (
        render_template(
            "result.html",
            message=message,
            original=original,
            cleaned=cleaned,
            upscale=upscale,
            upscale_cleaned=upscale_cleaned,
        ),
        200,
    )


@app.route("/regenerate", methods=["GET"])
def regenerate():
    logging.info("Regenerate request received!")

    reason, person, likes, tone, orientation, clean = data.values()

    message, original, cleaned, upscale, upscale_cleaned = generate(
        reason, person, likes, tone, orientation, clean
    )

    return (
        render_template(
            "result.html",
            message=message,
            original=original,
            cleaned=cleaned,
            upscale=upscale,
            upscale_cleaned=upscale_cleaned,
        ),
        200,
    )


def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=True)


if __name__ == "__main__":
    main()
