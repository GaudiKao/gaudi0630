# AI 代理指示文件

## 環境設定
- 本專案使用 Conda 虛擬環境進行開發
- 主要開發環境: `data_1`
- 在執行任何終端機命令前，必須先啟動 Conda 環境：
  ```bash
  conda activate data_1
  ```

## 專案結構
- `lesson21_1.ipynb`: Jupyter notebook 檔案，用於互動式開發和實驗
- `lesson21_2.py`: Python 腳本檔案
- `.github/`: 包含專案配置和 AI 代理指示
- `AGENTS.md`: 基本環境設定說明

## 開發工作流程
1. 所有開發工作必須在 `data_1` Conda 環境中進行
2. Jupyter notebooks 用於實驗性開發和數據分析
3. 穩定的功能應該遷移到 `.py` 檔案中

## 注意事項
- 確保在執行任何 Python 相關命令前已啟動正確的 Conda 環境
- Notebook 檔案應該包含適當的 markdown 說明以提高可讀性
- 保持程式碼風格一致性和清晰的文件結構
