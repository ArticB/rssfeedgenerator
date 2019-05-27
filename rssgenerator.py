from lxml import etree as ET    
import jinja2

RSS_FOLDER = './rss/'
parser = ET.XMLParser(remove_blank_text=True)

def append(link, title="torrent", description="some torrent"):
    tree = ET.parse(RSS_FOLDER+'/rss.xml', parser)
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
    tree.write(RSS_FOLDER+"rss.xml", xml_declaration=True)

def generate(file_name, t, l, d):
    root = ET.Element("rss")
    root.set("version", "2.0")

    channel = ET.SubElement(root, "channel")

    title = ET.SubElement(channel, "title")
    title.text = "Deep RSS" if t == "" else t

    link = ET.SubElement(channel, "link")
    link.text = "N/A" if l == "" else l

    description = ET.SubElement(channel, "description")
    description.text = "Deep's autodownloding torrent RSS" if d == "" else d

    #write to file:
    tree = ET.ElementTree(root)
    tree.write(RSS_FOLDER+file_name+'.xml', pretty_print=True, encoding='utf-8', xml_declaration=True)