#!/usr/bin/env python3
"""Recreate the CLT tutorial QR from the unchanged original slide's hyperlink.
Maintainer dependency: qrcode (python -m pip install qrcode). No student dependency.
"""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import json, hashlib
from urllib.parse import urlsplit, parse_qs
import qrcode
from qrcode.image.svg import SvgPathImage
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'sources/slides/307102-inferential-02-original.pptx'
with ZipFile(source) as z:
    relations=ET.fromstring(z.read('ppt/slides/_rels/slide12.xml.rels'))
    links={r.attrib['Id']:r.attrib['Target'] for r in relations if r.attrib['Type'].endswith('/hyperlink')}
    video_original=links['rId6']
    video_id=parse_qs(urlsplit(video_original).query)['v'][0]
    video='https://www.youtube.com/watch?v='+video_id
    assert video_id=='NTq0BO6pbbg'
    interactive=links['rId2']
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=8,border=4)
qr.add_data(video); qr.make(fit=True)
output=ROOT/'assets/inferential-statistics/clt-video-qr.svg'
qr.make_image(image_factory=SvgPathImage).save(str(output))
(ROOT/'instructor/clt-tutorial-source.json').write_text(json.dumps({
    'source_deck':str(source.relative_to(ROOT)), 'source_slide':12,
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'original_video_hyperlink':video_original,'display_and_qr_url':video,
    'original_interactive_hyperlink':interactive,
    'note':'Playlist parameters omitted from display/QR; original video ID retained. Original assets unchanged. Compact size exceptions explicitly authorized by the user on 21 November 2026.'
},indent=2)+'\n')
print(video)
