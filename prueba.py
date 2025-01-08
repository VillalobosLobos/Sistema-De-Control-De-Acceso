import requests
from PIL import Image
from io import BytesIO

nombre='2021123456.png'

url=f'http://127.0.0.1:8000/imagen/{nombre}'
response=requests.get(url)
if response.status_code==200:
	image=Image.open(BytesIO(response.content))
	image.show()
else:
	print(f"Error: {response.status_code} - {response.json()}")


