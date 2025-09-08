
# AI Coding Agent 指南

## 專案架構與開發重點

- 本專案為 Flask 應用，主程式為 `app.py`，啟動後提供一個簡單首頁（/），可擴充更多路由。
- 前端模板放於 `templates/` 目錄，目前僅有 `home.html`，採用三欄響應式設計。
- 所有依賴管理於 `requirements.txt`，目前僅需 `flask` 與 `python-dotenv`。
- 無 notebook 或多檔案模組，所有邏輯集中於 `app.py`。

## 環境與啟動

- 請務必於 Conda 環境 `data_1` 下開發與執行：
  ```cmd
  conda activate data_1
  ```
- 安裝依賴：
  ```cmd
  pip install -r requirements.txt
  ```
- 啟動 Flask 伺服器：
  ```cmd
  python app.py
  ```
  預設為 `debug=True`，可即時反映程式變更。

## 重要慣例與注意事項

- 路由與視圖函式請集中於 `app.py`，如需擴充，建議以 blueprint 分模組（目前未實作）。
- 前端模板請放於 `templates/`，並使用 `render_template`。
- 若需新增靜態資源，請建立 `static/` 目錄（目前未建立）。
- 請勿新增 notebook 或與現有結構無關的檔案。
- 若需環境變數，請使用 `.env` 並搭配 `python-dotenv`。

## 範例：新增一個路由

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

## 參考檔案

- `app.py`：Flask 主程式
- `templates/home.html`：首頁模板
- `requirements.txt`：依賴清單

如需擴充功能，請遵循上述結構與慣例。
