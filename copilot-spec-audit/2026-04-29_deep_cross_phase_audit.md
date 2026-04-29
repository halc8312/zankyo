# copilot-spec 完了状況・横断監査レポート（2026-04-29）

## 1. 監査対象
- 仕様: `/home/runner/work/zankyo/zankyo/copilot-spec/`
- 成果物: `/home/runner/work/zankyo/zankyo/zankyo/`
- 補助メタ: `/home/runner/work/zankyo/zankyo/zankyo/_meta/`

## 2. 監査方法
1. `copilot-spec` の Phase 0〜11 と `_meta` の必須ファイルを実在確認
2. 総ファイル数・総文字数・検索回数・研究ノート数・主要ID数を集計
3. 実装済み Phase 0〜3 は代表ファイルを精査し、仕様が要求する中身まで入っているかを確認
4. ID参照、後続Phase依存、反映先パス、監査フェーズ未実施の影響を横断確認
5. 進捗メタ (`progress.md`, `manifest.md`, `search_log.md`) と実ファイル群の整合を確認

## 3. 総合判定
**結論: 「全フェーズ完了」ではありません。Phase 0〜3 と `_meta` は概ね着手済みですが、Phase 4〜11 は構造的に未完了です。Definition of Done は未達です。**

### 即断できる理由
- 実在するトップレベル成果ディレクトリは `00_research`, `01_core`, `02_history`, `03_present`, `_meta` のみ
- `04_civilizations` 以降のディレクトリが存在しない
- 総Markdownファイル数は **75** で、DoD の **120以上** に未達
- Root要求の `README.md`, `GLOSSARY.md`, `MAP.md`, `TIMELINE_MASTER.md`, `INDEX_BY_ID.md`, `READING_PATHS.md`, `QUICKSTART_FOR_WRITERS.md`, `CANON_SUMMARY.md` が未作成
- `10_review/` が存在せず、自己批評3周・AI臭監査・命名監査・孤立参照監査が未実施

## 4. 定量監査サマリ

| 項目 | 実測 | 仕様 | 判定 |
|---|---:|---:|---|
| 総Markdownファイル数 | 75 | 120以上 | 未達 |
| 総文字数 | 204,314 | 200,000以上 | 達成 |
| Web検索ログ件数 | 44 | 40以上 | 達成 |
| 研究ノート | 23 | 20以上 | 達成 |
| 主要地方 | 12 | 12以上 | 達成 |
| 主要都市 | 25 | 25以上 | 達成 |
| 王朝・国家 | 18 | 15以上 | 達成 |
| 戦争 | 24 | 20以上 | 達成 |
| 残響対応 | 90 | 80以上 | 達成 |
| 言語系統 | 5 | 5以上 | 達成 |
| 主要勢力ファイル | 0 | 8以上 | 未達 |
| 宗教ファイル | 0 | 6以上 | 未達 |
| 主要人物 | 0 | 25以上 | 未達 |
| 脇役 | 0 | 60以上 | 未達 |
| 諺 | 0 | 80以上 | 未達 |
| 料理 | 0 | 40以上 | 未達 |
| 民謡・詩 | 0 | 15以上 | 未達 |
| 都市伝説独立成果物 | 0 | 20以上 | 未達 |
| 用語集 | 0 | 300以上 | 未達 |
| 自己批評ループ | 0 | 3周以上 | 未達 |

## 5. フェーズ別監査結果

### `_meta`
**判定: 構造上は概ね存在**

存在確認できた主要ファイル:
- `workplan.md`
- `style_bible.md`
- `naming_rules.md`
- `id_registry.md`
- `consistency_matrix.md`
- `search_log.md`
- `manifest.md`
- `quality_rubric.md`
- `assumptions.md`

ただし問題:
- `manifest.md` 冒頭は「現在段階: Phase 2 完了」のままで、`progress.md` の「Phase 3 完了」と食い違う
- `id_registry.md` では `CITY-01〜30`, `REL-01〜08`, `FAC-01〜18`, `CHR-001〜120` を予約しているが、後続フェーズが未作成のため予約だけが先行している

### Phase 0: `00_research`
**判定: 量的には達成、運用上は一部未解消**

達成点:
- `R-01`〜`R-23` の研究ノート 23 本あり
- `inspiration_safeguards.md`, `fantasy_cliche_rejection_matrix.md` あり
- `search_log.md` は 44 件あり、40回以上を満たす

注意点:
- 研究ノート本文は概ね「要約 / 論点 / 転用 / 注意 / 出典 / 反映メモ」を持つが、表記名は仕様の見出しと完全一致していない
- 研究ノート中の `反映先ファイル` に、現行成果物に存在しないパスが多数残る
  - 例: `01_world_core/resonance_theory.md`
  - 例: `04_society/languages.md`
  - 例: `10_audit/differentiation.md`
- これは **後続Phase未完了** と **旧パス名の残存** を同時に示している

### Phase 1: `01_core`
**判定: ファイル存在は達成、仕様密度は部分達成**

存在確認:
- `premise.md`
- `geography_overview.md`
- `cosmology.md`
- `resonance_theory.md`
- `core_taboos.md`
- `calendar_and_timekeeping.md`
- `measurement_and_value.md`
- `foundational_terms.md`
- `seasonality.md`

達成点:
- 必須9ファイルはすべて存在
- `resonance_theory.md` には強度5段階、居住閾値、距離減衰、時間減衰、季節係数、年齢差、干渉、飽和、逆残響、法/軍事/医療/依存の記述がある
- `seasonality.md` には季節係数表があり、原事件と季節の接続は書かれている

不足点:
- `resonance_theory.md` は仕様が要求する下記を**明示的には完了していない**
  - 残響相性表 最低10組
  - `notable_resonances.md` へのランク別実例5件ずつ
  - 偽装・誤認残響の独立整理
  - 共同体残響と個人残響の整理
  - 婚姻・育児・都市設計への展開の明文化
- `seasonality.md` は概念的には近いが、仕様語の
  - 「残響が眠る季節」
  - 「残響が荒れる季節」
  - 「移動禁止期 / 祈祷期 / 市場期」
  を独立節としては固定していない
- `foundational_terms.md` は代替語彙集として機能するが、仕様が例示した「魔法 / 呪い / 霊魂 / 祝福」の置換体系を明示対応表にはしていない

### Phase 2: `02_history`
**判定: 量は強いが、イベント単位の必須項目は未充足**

存在確認:
- `chronicle_official.md`
- `chronicle_folk.md`
- `chronicle_defeated.md`
- `chronicle_heretical.md`
- `chronicle_silence.md`
- `eras.md`
- `resonance_map.md`
- `dynasties.md`
- `wars.md`
- `historiography.md`
- `archives_and_censorship.md`
- `memory_sites.md`
- `engineered_atrocities.md`

実測:
- 公式編年イベント: 150
- 民間編年イベント: 65
- 敗者編年イベント: 55
- 異端編年イベント: 35
- 時代区分: 7
- 戦争: 24
- 残響対応: 90
- 人工悲劇: 5

達成点:
- 仕様の最低件数をほぼ上回る
- `engineered_atrocities.md` は 5件を明確に実装
- `consistency_matrix.md` は人工悲劇5件が複数史型へ横断接続されていることを示す

不足点:
- `chronicle_official.md` の各イベントは、仕様必須の
  - なぜ起きたか
  - 誰が得をしたか
  - 何が隠されたか
  - 現在に残る残響
  - 記録の食い違い
  をイベントごとに全項目で持っていない
- つまり **件数は達成しているが、1イベントあたりの必須情報密度は未達**
- `resonance_map.md` は 90件あるが、Phase 5 の `notable_resonances.md` が無いため、数値モデル実例側の閉ループが未完成

### Phase 3: `03_present`
**判定: 構造上は達成、後続Phase依存が強い**

存在確認:
- `regions.md`
- 地方詳細 12件
- `cities.md`
- `borders_disputes.md`

実測:
- 地方詳細ファイル: 12
- 都市ID: 25

達成点:
- 地方数・都市数は仕様下限を達成
- 各地域ファイルは気候、感覚、労働、主要都市、言語、宗教、食、服飾、建築、残響、法慣習、歴史的傷、庶民スケッチ、旅人違和感などを持つ
- `cities.md` は25都市とも仕様の基本項目を満たしている

不足点:
- 地域ファイルが `REL-01`〜`REL-06` などを参照しているが、Phase 4 の `religions.md` が無いため**宗教参照が定義に着地していない**
- 同様に、政治・人物・生活・物語への接続先が後続Phase未作成のため、現代地理は「舞台の器」まではできているが、全体完成状態ではない

### Phase 4: `04_civilizations`
**判定: 未着手**

ディレクトリ自体が存在しない。したがって以下はすべて未達:
- `religions.md`
- `languages.md`
- `economy.md`
- `social_classes.md`
- 主要勢力最低8件の個別ファイル

### Phase 5: `05_resonance_systems`
**判定: 未着手**

ディレクトリ自体が存在しない。したがって以下はすべて未達:
- `resonance_categories.md`
- `notable_resonances.md`（最低50）
- `cost_and_corruption.md`
- `forbidden_practices.md`
- `legal_status_of_resonances.md`
- `resonance_medicine.md`
- `resonance_economics.md`
- `migrants/` 配下8ファイル

この未達は Phase 1 の理論完成度にも直接波及している。

### Phase 6: `06_politics`
**判定: 未着手**

未達:
- `factions.md`
- `current_conflicts.md`
- `shadow_powers.md`
- `the_question.md`
- 派閥15件
- 紛争7件

### Phase 7: `07_characters`
**判定: 未着手**

未達:
- 主要人物25名の個別ファイル
- `relationships.md`
- `minor_characters.md`
- 脇役60名

`id_registry.md` の人物予約はあるが、実体化されていない。

### Phase 8: `08_texture`
**判定: 未着手**

未達:
- `daily_life.md`
- `food.md`
- `idioms_proverbs.md`
- `songs_poems.md`
- `urban_legends.md`
- `humor.md`
- `fashion.md`
- `sensory.md`
- `funeral_customs.md`
- `children.md`
- `gestures_and_body_habits.md`
- `swears_and_curses.md`
- `work_songs_and_tools.md`
- `weather_and_seasonal_fears.md`

### Phase 9: `09_story_seeds`
**判定: 未着手**

未達:
- `main_plot_candidates.md`
- `subplots.md`
- `mysteries.md`
- `themes_motifs.md`

### Phase 10: `10_review`
**判定: 未着手**

未達:
- `round_1_issues.md`
- `round_2_issues.md`
- `round_3_issues.md`
- `differentiation.md`
- `ai_smell_audit.md`
- `consistency_audit.md`
- `naming_audit.md`
- `orphan_reference_audit.md`
- `scorecard.md`
- `scorecard_history.md`

これは DoD 上かなり致命的で、**AI臭監査0件、命名重大逸脱0件、孤立参照0件** を現時点では証明できない。

### Phase 11: ルート索引・入門文書
**判定: 未着手**

未達:
- `README.md`
- `GLOSSARY.md`
- `MAP.md`
- `TIMELINE_MASTER.md`
- `INDEX_BY_ID.md`
- `READING_PATHS.md`
- `QUICKSTART_FOR_WRITERS.md`
- `CANON_SUMMARY.md`
- `11_entry/first_3000_chars.md`
- `11_entry/world_in_one_page.md`
- `11_entry/pitch_30_seconds.md`
- `11_entry/sample_scene_per_region.md`

## 6. 横断監査で見つかった重要問題

### 6-1. 宗教・派閥・人物は「予約だけ存在」
- `REL`, `FAC`, `CHR` はID予約がある
- しかし定義ファイル・個別成果物が存在しない
- 地域記述がすでに宗教IDへ依存しているため、**参照先不在の先行記述** が発生している

### 6-2. Phase 1 の理論が Phase 5 不在で閉じていない
- `resonance_theory.md` は定量モデルを導入している
- しかし、それを検証する `notable_resonances.md` と各ランク実例群が存在しない
- よって「理論だけ先にある状態」で、仕様が要求する検証可能性には未到達

### 6-3. 研究ノートの反映先に旧構成/未作成先が残る
- 研究ノートの `反映先ファイル` には、現行フォルダ構成に存在しないパスが多数残る
- これは
  - 旧構想名の残留
  - 将来ファイルへの先行参照
  - 実際には未反映の可能性
  を含む

### 6-4. メタ進捗に軽い食い違いがある
- `progress.md` は Phase 3 完了を記録
- しかし `manifest.md` 冒頭はなお「Phase 2 完了」
- 進捗ログとマニフェストの同期が崩れている

### 6-5. Root導線が無いため、完成物として読めない
- Phase 11 未実装のため、README導線・索引・用語集・タイムライン・入門文書がない
- したがって、Phase 0〜3 が存在していても **「使える設定資料群」** という最終目的には未到達

## 7. Definition of Done 判定

| DoD項目 | 判定 | 根拠 |
|---|---|---|
| Phase 0–11 全ファイル存在 | 未達 | 04〜11未作成 |
| `_meta/` 配下ファイル存在 | 達成 | 主要制御ファイルあり |
| 総ファイル数120以上 | 未達 | 75 |
| 総文字数20万字以上 | 達成 | 204,314字 |
| Web検索40回以上 | 達成 | 44件 |
| 研究ノート20本以上 | 達成 | 23本 |
| 主要地方12以上 | 達成 | 12 |
| 主要都市25以上 | 達成 | 25 |
| 王朝・国家15以上 | 達成 | 18 |
| 戦争20以上 | 達成 | 24 |
| 残響対応80以上 | 達成 | 90 |
| 主要勢力8以上 | 未達 | Phase 4 未作成 |
| 宗教6以上 | 未達 | `religions.md` 未作成 |
| 言語5以上 | 達成 | `LNG-01`〜`LNG-05` |
| 主要人物25以上 | 未達 | Phase 7 未作成 |
| 脇役60以上 | 未達 | Phase 7 未作成 |
| 諺80以上 | 未達 | Phase 8 未作成 |
| 料理40品以上 | 未達 | Phase 8 未作成 |
| 民謡・詩15篇以上 | 未達 | Phase 8 未作成 |
| 都市伝説20以上 | 未達 | Phase 8 未作成 |
| 用語集300項目以上 | 未達 | Phase 11 未作成 |
| 自己批評ループ3周完了 | 未達 | Phase 10 未作成 |
| AI臭監査で禁則違反0件 | 未達 | 監査ファイルなし |
| 音韻監査で重大逸脱0件 | 未達 | 監査ファイルなし |
| 人物・地域・事件・残響の孤立参照0件 | 未達 | 監査ファイルなし / 後続Phase欠落 |
| READMEから全ファイル到達可能 | 未達 | README未作成 |
| PR説明文に達成チェックリスト記載 | このリポジトリ成果物からは確認不可 | Phase 11/PR成果物未整備 |

## 8. 完了率の実務判断

### 構造完了
- `_meta`: 高
- Phase 0: 高
- Phase 1: 中
- Phase 2: 中〜高
- Phase 3: 中〜高
- Phase 4〜11: 0

### 総体
**仕様全体に対する完了率は、量では進んでいるものの、フェーズ完走基準では中盤手前です。**

実務上は次の状態:
- **世界の骨格・歴史・現代地理の基盤はある**
- **社会・能力体系・政治・人物・生活・物語・監査・索引が無い**
- よって **「設定プロジェクトの前半成果」ではあるが、「全フェーズ完了成果物」ではない**

## 9. 最重要未完ポイント
1. Phase 4〜11 の未作成
2. Phase 10 未実施により品質保証不能
3. Phase 11 未実施により読者導線ゼロ
4. Phase 5 不在により残響理論の検証系が未閉鎖
5. 研究ノートの反映先パスに旧構成/未作成先が残存
6. `manifest.md` と `progress.md` の段階表示不整合

## 10. 最終結論
**copilot-spec フォルダが要求する「各フェーズなどが全て確実に完了している」状態ではありません。**

現状は:
- Phase 0〜3 と `_meta` はかなり進んでいる
- しかし Phase 4〜11 が抜けているため、仕様全体では未完
- DoD は多数未達
- 特に監査フェーズと索引フェーズが無いため、「完成保証」と「利用可能性」の両面で未完了

したがって、本リポジトリの現状は **「仕様前半の大規模実装済み、だが全体完了ではない」** という判定になる。
