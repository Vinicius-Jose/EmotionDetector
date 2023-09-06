from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def analyze_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    try:
        response = emotion_detector(text_to_analyze)
    except Exception as e:
        print(e)
        response = {}
    anger = response.get("anger")
    if anger:
        message = (
            f"For the given statement, the system response is 'anger': {response.get('anger')}, "
            + f"'disgust': {response.get('disgust')}, 'fear': {response.get('fear')}, 'joy': {response.get('joy')}"
            + f" and 'sadness': {response.get('sadness')}. The dominant emotion is {response.get('dominant_emotion')}. "
        )
    else:
        message = "Invalid text! Please try again!."
    return message


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    """This functions executes the flask app and deploys it on localhost:5000"""
    app.run("0.0.0.0", port=5000)
