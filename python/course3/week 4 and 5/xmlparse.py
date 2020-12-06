import xml.etree.ElementTree as ET
data = '''<person>
<name>Anna</name>
<age>12</age>
<sister>
Vaishnavi
</sister>
</person>'''
tree = ET.fromstring(data)
print(tree)
print("Name:", tree.find('name').text)
print("Age:", tree.find('age').text)