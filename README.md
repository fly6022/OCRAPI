# OCRAPI

Based on Flask &amp; CnOcr. 🎨✨可在局域网部署一个轻量级的光学字符识别系统。

## 部署

只需要在程序所在目录运行以下命令，即可在 ``10000``端口完成部署。

```bash
py ./app.py
```

## 使用

客户端与服务端采用 ``POST``方法连接。

提供了2个接口，可通过``Postman``进行测试。

### 接口1

API请求地址:``http://127.0.0.1:10000/api/ocr/v1``

| Content-Type        | Key   | Value |
| ------------------- | ----- | ----- |
| multipart/form-data | image | URL   |

### 接口2

API请求地址:``http://127.0.0.1:10000/api/ocr/v2``

| Content-Type        | Key   | Value |
| ------------------- | ----- | ----- |
| multipart/form-data | image | file  |

## 示例

### 接口1

API请求地址:``http://127.0.0.1:10000/api/ocr/v1``

| Content-Type        | Key   | Value |
| ------------------- | ----- | ----- |
| multipart/form-data | image | https://cnocr.readthedocs.io/zh/latest/examples/multi-line_cn1.png   |

### 接口2

API请求地址:``http://127.0.0.1:10000/api/ocr/v2``

| Content-Type        | Key   | Value |
| ------------------- | ----- | ----- |
| multipart/form-data | image | file  |