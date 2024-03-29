import xml.etree.ElementTree as ET
import glob
import os

#################### 設定 ####################
domain = "https://example.com/"
url_path = "C:/xampp/htdocs/example/"
url_ftype = "php"

output_dir = "C:/xampp/htdocs/createXML/xml/"
output_filenm = "sample.xml"
lastmod_date = '2024-03-29'

#################### 自動生成 ####################
output_fpath = output_dir + output_filenm
print(output_fpath)

urls = glob.glob(url_path + "*." + url_ftype)
print(urls)

urlset = ET.Element('urlset')
urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
tree = ET.ElementTree(element=urlset)

for url in urls:
    url_element = ET.SubElement(urlset, 'url')
    loc = ET.SubElement(url_element, 'loc')
    loc.text = domain + os.path.split(url)[1]
    lastmod = ET.SubElement(url_element, 'lastmod')
    lastmod.text =lastmod_date

tree.write(output_fpath, encoding='utf-8', xml_declaration=True)