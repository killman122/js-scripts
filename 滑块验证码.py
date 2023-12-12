import ddddocr,requests
import base64
base64.b64decode("")

det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

with open('target.png', 'rb') as f:
    target_bytes = f.read()

with open('background.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes, simple_target=True)
print(res)

