# Flask 專案架構與整合 Huey

> 🔔 此 Repository 存放的內容為 2021-11-17 於 [TaichungPy](https://www.facebook.com/groups/780250978715991/) 分享所使用的 Demo Code。

## 簡介

此專案涵蓋了 Flask & Huey 的使用方式，並且也提及如何將 Flask 來的 Request 加入到 Huey 的工作佇列中。

此外，也有提供 Flask 與 Huey 的測試範例供大家做參考。

## 使用的套件

1. [Huey：輕量級的 Task Queue](https://github.com/coleifer/huey)
2. [Flask：輕量級的 WSGI Web 框架](https://github.com/pallets/flask)

### 安裝

```sh
pip install -r requirements.txt
```

## 啟動本專案

```sh
python main.py
```

## 使用 Pytest 進行測試

> 💡因有使用 time.sleep() 故測試時間會拉長至24秒以上。

```sh
python -m pytest .
```

## Docker

1. 打包成 Image

```sh
docker build . -t huey_flask_lab:1.0.0
```

2. 啟動 Docker

```sh
docker run -it -p 8989:8989 huey_flask_lab:1.0.0
```