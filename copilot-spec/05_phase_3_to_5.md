# 05. Phase 3〜5

## Phase 3: 現在の地理と勢力 → `zankyo/03_present/`
- `regions.md`
- 地方別ファイル `region_XX_<name>.md` を最低12
- `cities.md`（主要都市最低25）
- `borders_disputes.md`

### 各地方ファイルの必須項目
- 地形、気候、植生、水系
- 季節ごとの暮らし
- 音、匂い、湿度、病、虫害
- 労働の中心
- 主要都市
- 身体的特徴
- 言語
- 宗教
- 産業
- 食
- 服飾
- 建築
- 残響の系統
- 法と慣習
- 他地方からの偏見
- その地方の人間が当然と思っている異様さ
- 歴史的傷
- 典型的な庶民1名の生活スケッチ
- 旅人が最初に感じる違和感

### 各都市の必須項目
- 成立史
- 区画構造
- 水と衛生
- 夜の明かり
- 市場
- 支配階層
- 危険地域
- 残響関連産業
- 民間信仰
- ひとつの噂
- ひとつの都市伝説
- ひとつの匂い
- ひとつの音

---

## Phase 4: 文明・社会 → `zankyo/04_civilizations/`
- 主要勢力最低8、各別ファイル
- `religions.md`（最低6）
- `languages.md`（最低5）
- `economy.md`
- `social_classes.md`

### 各勢力ファイルの必須項目
政体、法、経済、階級、宗教、家族制度、教育、軍事、外交、芸術、食、服飾、建築、葬制、性規範、子育て、医療、刑罰、祝祭、タブー、歴史的後ろめたさ、残響を巡る国家方針、悲劇を起こすことが国力増強になる問題への公式見解と非公式実態。

### languages.md / 言語設計の必須要件
各言語ごとに以下を作ること。
- 音韻ルール
- 音節構造
- 禁止される音の並び
- 強勢やリズム
- 語順
- 文法概略
- 名詞・動詞の形態
- 敬語/卑語
- 罵倒表現
- 祈祷語
- 地名形成ルール
- 人名形成ルール
- 80語以上の語彙サンプル
- 10文以上の例文
- 文字体系
- 方言差
- 借用語の流れ
- 言語と支配/差別の関係

---

## Phase 5: 残響と能力体系 → `zankyo/05_resonance_systems/`
- `resonance_categories.md`
- `notable_resonances.md`（最低50）
- `cost_and_corruption.md`
- `forbidden_practices.md`

### notable_resonances.md の各項目必須
- ID
- 名称
- 発現土地
- 由来事件
- 必要居住年数
- 発現条件
- 具体的な作用
- 応用例
- 軍事利用
- 日常利用
- 副作用
- 精神負荷
- 失われ方
- 現在の社会評価
- 所有者/使い手の典型像
- 関連禁忌
- 数値モデル上の位置（強度ランク、影響半径、減衰など）

### Phase 5 追加必須
- `legal_status_of_resonances.md`: 国家別の法的位置づけ
- `resonance_medicine.md`: 治療、鎮静、依存、宗教療法
- `resonance_economics.md`: 売買、賃貸、地価、強制移住、観光、巡礼

### 「渡り」専用パート → `zankyo/05_resonance_systems/migrants/`
独立サブディレクトリを作成し、以下を作れ。

- `migrants_overview.md`: 渡りの定義、起源、人口推計、地域分布
- `migrants_codex.md`: 渡りの内部規範、暗黙ルール、信義、裏切り者の扱い
- `migrants_argot.md`: 渡り独自の隠語・符牒・身振り（最低60語）
- `migrants_rites.md`: 入門儀礼、別れの作法、亡骸の扱い
- `migrants_routes.md`: 主要な巡回路 最低5本、季節と残響強度に応じた最適ルート
- `migrants_persecution.md`: 渡りへの差別と迫害の歴史、現在の法的地位（地方ごとに違う）
- `migrants_economy.md`: 残響傭兵、情報売買、密輸、巡礼案内、芸能
- `migrants_famous.md`: 伝説的な渡り 最低10名（Phase 7 主要人物とは別人で構わない）
