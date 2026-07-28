Tonks, 

我需要開發一個流程，用來幫我準備指定考點的題目。

考題記錄：

- /Users/yuan/Projects/Exam/Exam_prepare_database/Sources

考試參考資料：

- 2020 Brenner '/Users/yuan/Projects/PDF/image_table_box_extractor_for_brenner/2020 Brenner 11e'
- KDIGO '/Users/yuan/Projects/PDF/image_table_box_extractor_for_kdigo/KDIGO guidelines'

圖庫來源

- /Users/yuan/Projects/PDF/Outputs

skill 名稱： tn-exam-lecture-and-practice

```
## Purpose
- 整合過去考試的考點與課本內的重點，為 Yuan 產生備考用的課程與練習題，並上傳到練習網站以供練習

## Yuan Usage
- 限由 Yuan invoke $lu-exam-lecture-and-practice ，Agent 不自行啟動
- Yuan 會告知 agent 這一輪要討論哪個主題，然後由 agent 派出 subagents 去分別搜索考題記錄、課本及 KDIGO 相關內容，由 main thread 整合產生 lesson map 與練習題計畫，再由 subagents 產生主題教材與練習題，最後由 main thread 整合成一個完整教材與練習題庫，並完成上網發佈。
- 此 skill 預設會在不同 session 之間平行運作。每個 session 只處理一個主題。
```

開發過程應融入 [$tn-exam-producer](/Users/yuan/.codex/skills/tn-exam-producer/SKILL.md)  [$tn-exam-tutor](/Users/yuan/.codex/skills/tn-exam-tutor/SKILL.md)  的運作模式與發佈流程，結合這些成功經驗以產生可用的 skill，避免重新踩雷。

[$tn-spec](/Users/yuan/.codex/skills/tn-spec/SKILL.md)