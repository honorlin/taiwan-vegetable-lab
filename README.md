# 台灣蔬菜種植研究室

研究證據、台灣氣候與可操作的蔬菜栽培知識庫。

內容涵蓋作物、播種曆、環境、土壤、肥培、灌溉、育苗、害蟲、病害、設施、採收與研究解讀。文章標示作物、學名、證據層級、審閱日期、原始來源與研究限制。每篇正文至少 1,200 字元、至少 3 張合法授權照片、至少 3 個可靠來源（其中至少 2 個官方來源），並須包含栽培條件、操作步驟、觀察紀錄、常見問題與研究限制。

```bash
python3 scripts/validate_content.py
bundle exec jekyll build
```

正式站由 GitHub Actions 部署；每日自動營運走 Issue、PR、內容驗證、CI/CD 與 production smoke test。
