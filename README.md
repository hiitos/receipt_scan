# レシートスキャン

firest commitになってるhahahaha

gcp環境準備  
- DocumentAI のプロセッサー作成
- プロセッサーIDコピペ

`poetry run python test.py`

`data/`  
にjpgかpdf入れる。(pngなどはめんどくさかったのでやってない)  

`.env`  
- PROJECT_ID
- LOCATION
- PROCESSOR_ID
  - コピペしたプロセッサーID
- FILE_PATH
  - ./data/test.jpgみたいな感じ