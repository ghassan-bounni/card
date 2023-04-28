import os
import logging
from flask import Flask, request, render_template
from cover_generator import generate_card_images
from text_generator import generate_card_text
from const import occasion_keyword_map, catalog_urls

app = Flask(__name__, static_folder="static")

data = {
    "reason": "",
    "person": "",
    "likes": "",
    "tone": "",
    "orientation": "",
    "clean": "",
    "message": ""
}


def generate_art(reason, orientation, clean):
    print("Waiting for images to be generated...")
    card_images = generate_card_images(occasion_keyword_map[reason], orientation, clean)
    if clean == "y":
        cleaned = card_images["cleaned"]
        upscale_cleaned = card_images["cleaned_upscale"]
    else:
        cleaned = "None"
        upscale_cleaned = "None"

    return (
        card_images["original"],
        cleaned,
        card_images["upscale"],
        upscale_cleaned,
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/catalog")
def catalog():
    return render_template("catalog.html", catalog_urls=catalog_urls)


@app.route("/generate_message", methods=["POST"])
def generate_message():
    logging.info("Generate request received!")
    data["reason"] = request.form["reason"]
    data["person"] = request.form["person"]
    data["likes"] = request.form["likes"]
    data["tone"] = request.form["tone"]
    data["orientation"] = request.form["orientation"]

    reason, person, likes, tone, orientation, clean, message = data.values()

    data['message'] = generate_card_text(reason, person, likes, tone)

    return (
        render_template(
            "result.html",
            message=data['message'],
        ),
        200,
    )


@app.route("/generate_cover_art", methods=["GET"])
def generate_cover_art():
    if "clean" in request.args.keys():
        data["clean"] = request.args.get("clean")
    else:
        data["clean"] = "n"

    reason, person, likes, tone, orientation, clean, message = data.values()

    original, cleaned, upscale, upscale_cleaned = generate_art(reason, orientation, clean)

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
    print("Regenerating Images...")

    if "clean" in request.args.keys():
        data["clean"] = request.args.get("clean")
    else:
        data["clean"] = "n"

    reason, person, likes, tone, orientation, clean, message = data.values()

    original, cleaned, upscale, upscale_cleaned = generate_art(reason, orientation, clean)

    return (
        render_template(
            "result.html",
            message=data['message'],
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
