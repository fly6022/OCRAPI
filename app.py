# -*- coding: utf-8 -*-
# @name   : OCRAPI/app.py
# @author : fly6022
# @date   : 2023/7/15
# @Email  : i@fly6022.fun
# @version: 0.1.0
# @license: BSD 3-Clause

from flask import Flask, request
from cnocr import CnOcr
import requests as req
from PIL import Image
from io import BytesIO

app = Flask(__name__);
app.jinja_env.auto_reload = True;
app.config['TEMPLATES_AUTO_RELOAD'] = True;

@app.route('/api/ocr', methods=["POST"]) # API
def api_get_text():
    if request.method == "POST":
        image_src = request.form.get("image");
        response = req.get(image_src);
        image = Image.open(BytesIO(response.content));
        ocr = CnOcr(det_more_configs={'use_angle_clf': True});
        outdata = ocr.ocr(image);
        t = [];
        for a in outdata:
            t.append(a.get("text"));
        text = "".join(t);
    return text;

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="10000");
    print("Good Bye!!");  