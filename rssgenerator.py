import uuid
from lxml import etree as ET    

RSS_FOLDER = './rss/'
parser = ET.XMLParser(remove_blank_text=True)

def append(link, title, description, filename):
    filepath = RSS_FOLDER+filename
    tree = ET.parse(filepath+'.xml', parser)
    channel = tree.getroot()
    item = ET.SubElement(channel,"item")
    _title = ET.SubElement(item, "title")
    _title.text = title
    _link = ET.SubElement(item, "link")
    _link.text = link
    _description = ET.SubElement(item, "description")
    _description.text = description
    _comments = ET.SubElement(item, "comments")
    _comments.text = "downloading"
    channel.find(".//description").addnext(item)
    tree = ET.ElementTree(channel)
    print(ET.tostring(channel, pretty_print=True, encoding='utf-8',xml_declaration=True))
    tree.write(filepath+".xml", xml_declaration=True)

def generate_new_rss(new_title):

    root = ET.Element("rss")
    root.set("version", "2.0")

    channel = ET.SubElement(root, "channel")

    
    title = ET.SubElement(channel, "title")
    title.text = new_title

    link = ET.SubElement(channel, "link")
    link.text = "NA"

    description = ET.SubElement(channel, "description")
    description.text = "NA"

    _uuid = uuid.uuid1().hex
    
    file_save = RSS_FOLDER+_uuid+'.xml'
    #write to file:
    tree = ET.ElementTree(root)
    tree.write( file_save, pretty_print=True, encoding='utf-8', xml_declaration=True)
    return _uuid

def get_all_items(filename):
    filepath = RSS_FOLDER+filename
    tree = ET.parse(filepath+'.xml', parser)
    channel = tree.getroot()
    dict_item = {}
    l = []
    for lists in channel:
        for items in lists:
            if items.tag != 'channel' and items.tag != 'title' and items.tag != 'link' and items.tag != 'description' :
                print(items.tag)
                for item in items.iter():
                    if item.tag != 'item':
                        dict_item[item.tag] = item.text
                l.append(dict_item)
                dict_item = {}
    
    return l
                
    