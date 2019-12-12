#!/usr/bin/env python2
import io
import os
from lxml import html


def main():
    DIR = os.environ["DIR"]
    if "review-drafts" not in DIR:
        return
    specFilename = os.path.join(DIR, "index.html")
    w3cFilename = "w3c-status.html"
    specFile = io.open(specFilename, 'r+', encoding='utf-8')
    w3cFile = io.open(w3cFilename, 'r+', encoding='utf-8')
    doc = html.parse(io.StringIO(unicode(specFile.read())))
    w3c = html.fragments_fromstring(unicode(w3cFile.read()))
    logo = w3c[0]
    ipr = w3c[1]
    status = w3c[2]
    logoParagraph = doc.xpath("//body/div[@class='head']/p")[0]
    logoParagraph.append(logo)
    iprParagraph = doc.xpath("(//body/div[@class='head']/" +
                             "details[@class='annoying-warning']/p)[2]")[0]
    iprParagraph.append(ipr)
    body = doc.xpath("//body")[0]
    body.append(status)
    specFile.seek(0)
    specFile.write(unicode(html.tostring(doc)))
    specFile.truncate()
    specFile.close()

main()
