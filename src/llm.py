from openai import OpenAI
from flask import Blueprint

llm_api = Blueprint('llm_api', __name__, )


@llm_api.route('/insights/', methods=['GET'])
def insights():
    # store key?
    client = OpenAI(api_key='')

    # replace with input via url
    enjoyed_artists = ["Eyedress", "d4vd", "Alex G", "Crumb", "Melody's Echo Chamber"]
    string_version = ",".join(enjoyed_artists)

    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      response_format={"type": "json_object"},
      messages=[
        {"role": "system", "content": "You are a helpful assistant whose purpose is to predict the way a user thinks, acts, and dresses based on their music tastes. You must format your response in JSON."},
        {"role": "user", "content": "Given that I enjoy listening to {}, please dynamically describe the way you think I act, think, and dress based on my music taste?".format(string_version)}
      ]
    )

    print(response.choices[0].message.content)

    return response.choices[0].message.content


if __name__ == '__main__':
    insights()