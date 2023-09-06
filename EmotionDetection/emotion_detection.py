import requests


def emotion_detector(text_to_analyse) -> dict:
    json_return = {
        "anger": None,
        "disgust ": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    if response:
        formatted_response: dict = (
            response.json().get("emotionPredictions")[0].get("emotion")
        )
        json_return.update(formatted_response)
        dominant_emotion = {"emotion": "anger", "value": json_return.get("anger")}
        for key, value in formatted_response.items():
            if value > dominant_emotion.get("value"):
                print(key)
                print(value)
                dominant_emotion.update({"emotion": key, "value": value})
        json_return["dominant_emotion"] = dominant_emotion.get("emotion")
    return json_return
