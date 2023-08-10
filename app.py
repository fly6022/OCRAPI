# -*- coding: utf-8 -*-
# @name   : OCRAPI/app.py
# @author : fly6022
# @date   : 2023/7/28
# @Email  : i@fly6022.fun
# @version: 1.0.0
# @license: BSD 3-Clause

from flask import Flask, request
from cnocr import CnOcr
import requests as req
from PIL import Image
from io import BytesIO

app = Flask(__name__);
app.jinja_env.auto_reload = True;
app.config['TEMPLATES_AUTO_RELOAD'] = True;

@app.route("/")
def index():
    print("233!")
    return                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          render_template("index.html")

@app.route('/api/ocr/v1', methods=["POST"]) # API
def api_get_text_v1():
    if request.method == "POST":
        image_src = request.form.get("image");
        response = req.get(image_src);
        image = Image.open(BytesIO(response.content));
        ocr = CnOcr('densenet_lite_136-gru', det_model_name='ch_PP-OCRv3_det', det_more_configs={'use_angle_clf': True});
        outdata = ocr.ocr(image);
        t = [];
        for a in outdata:
            t.append(a.get("text"));
        text = "".join(t);
    return text;

@app.route('/api/ocr/v2', methods=["POST"]) # API
def api_get_text_v2():
    if request.method == "POST":
        image = Image.open(request.files.get('image'))
        ocr = CnOcr('densenet_lite_136-gru', det_model_name='ch_PP-OCRv3_det', det_more_configs={'use_angle_clf': True});
        outdata = ocr.ocr(image);
        t = [];
        for a in outdata:
            t.append(a.get("text"));
        text = "".join(t);
    return text;

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="10000");
    print("Good Bye!!");  