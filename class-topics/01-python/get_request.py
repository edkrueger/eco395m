import requests

BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"

# response = requests.request(
#     method="GET",
#     url=BASE_URL,
#     params={
#         "language": "de"
#     }
# )

response = requests.get(
    url=BASE_URL,
    params={
        "language": "de"
    }
)

print(response)
print(response.status_code)
print(response.text)
print(type(response.text))

json_ = response.json()

print(type(json_))
print(json_)
print(json_["text"])

print(response.url)
