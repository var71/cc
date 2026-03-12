import requests
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/tempconvert.asmx"
temp = input("Enter temperature in Fahrenheit: ")

soap = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{temp}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>"""

headers = {
    "Content-Type": "text/xml",
    "SOAPAction": "https://www.w3schools.com/xml/FahrenheitToCelsius"
}

response = requests.post(url, data=soap, headers=headers)

root = ET.fromstring(response.text)

for i in root.iter("{https://www.w3schools.com/xml/}FahrenheitToCelsiusResult"):
    print(f"{temp} Fahrenheit = {i.text} Celsius")