import re
def find_entities(text):

    result = {
        'URLs': re.findall(r'https?://\S+|www\.\S+', text),
        'IP Addresses': re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
        'Dates': re.findall(r'([1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}', text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
    }
    return result

# Example usage:
sample_text = """
First Dataset
Visit our website at https://www.w3school.com.
For support, contact us at support@example.com.
IP address: 192.168.20.5
Date: 11/02/2023
PAN number: ABCDE4325L

Second Dataset
Visit our website at https://www.javatpoint.com.
For more info connect with  info@example.com.
IP address: 187.76.5.3
Date: 26/09/2023
PAN number: AXNPQ9321H
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")


"""
Output:
URLs: ['https://www.w3school.com.', 'https://www.javatpoint.com.']
IP Addresses: ['192.168.20.5', '187.76.5.3']
Dates: [('11', '02', '20'), ('26', '09', '20')]
PAN Numbers: ['ABCDE4325L', 'AXNPQ9321H']

"""