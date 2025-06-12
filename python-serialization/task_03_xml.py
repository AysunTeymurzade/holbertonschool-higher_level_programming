import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            element = ET.SubElement(root, key)
            element.text = str(value)  # Hər şeyi string kimi yazırıq

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Serialization error: {e}")
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text  # Bütün dəyərlər string kimi oxunur

        return result
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None