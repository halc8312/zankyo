from pathlib import Path
from datetime import datetime, timezone

root = Path('/home/runner/work/zankyo/zankyo/zankyo')
(root / '02_history').mkdir(parents=True, exist_ok=True)
(root / '_meta').mkdir(parents=True, exist_ok=True)

years = [-2600,-2559,-2518,-2477,-2436,-2395,-2354,-2313,-2272,-2231,-2190,-2149,-2108,-2067,-2026,-1985,-1944,-1901,-1900,-1872,-1844,-1816,-1788,-1760,-1732,-1704,-1676,-1648,-1620,-1592,-1564,-1536,-1508,-1480,-1452,-1424,-1396,-1368,-1340,-1312,-1281,-1280,-1258,-1236,-1214,-1192,-1170,-1148,-1126,-1104,-1082,-1060,-1038,-1016,-994,-972,-950,-928,-906,-884,-862,-840,-818,-796,-774,-731,-730,-709,-688,-667,-646,-625,-604,-583,-562,-541,-520,-499,-478,-457,-436,-415,-394,-373,-352,-331,-310,-289,-268,-247,-226,-181,-180,-164,-148,-132,-116,-100,-84,-68,-52,-36,-20,-4,12,28,44,60,76,92,108,124,140,156,172,188,204,241,242,265,288,311,334,357,380,403,426,449,472,495,518,541,564,587,610,633,656,681,682,704,726,748,770,792,814,836,858,880,902,931]
era_data = [('ERA-01','泥足期',-2600,-1901),('ERA-02','墓印期',-1900,-1281),('ERA-03','渠骨期',-1280,-731),('ERA-04','灰冠期',-730,-181),('ERA-05','裂書期',-180,241),('ERA-06','追塩期',242,681),('ERA-07','現臍期',682,931)]

def era_for_year(y):
    for eid,name,s,e in era_data:
        if s <= y <= e:
            return eid,name
    raise ValueError(y)

regions = {'REG-01': ('潮墓湾サウマ','サウマ'),'REG-02': ('葦痕低地ヌワネ','ヌワネ'),'REG-03': ('瘡河三角ネグシェ','ネグシェ'),'REG-04': ('伏渠平野シャンヌ','シャンヌ'),'REG-05': ('冬鳴狭地ヘシュク','ヘシュク'),'REG-06': ('塩鞭崖タルヘス','タルヘス'),'REG-07': ('灰樋連峰クァルグ','クァルグ'),'REG-08': ('煙鐘高地グェラム','グェラム'),'REG-09': ('玻土列島イライ','イライ'),'REG-10': ('霧帆群環オエア','オエア'),'REG-11': ('雨鞣原マサヌ','マサヌ'),'REG-12': ('鉄膿盆地グァトル','グァトル')}
region_order = list(regions.keys())

polities = {
    'POL-01': {'name':'サウマ塩連','eras':'ERA-06/07','regions':'REG-01/06','summary':'塩杭倉と沿岸船団を束ねる商塩連合。塩税と埋葬船保険で富み、海崖と湾の残響地を倉地として囲う。'},
    'POL-02': {'name':'葦州合議','eras':'ERA-02/03','regions':'REG-02','summary':'治水評議会から伸びた低地国家。堤門鍵を共有財と称しつつ、葦束税で書記層を養った。'},
    'POL-03': {'name':'渠骨王国','eras':'ERA-03','regions':'REG-04','summary':'地下渠と堤防を国家骨格に見立てた運河王国。ATR-01の加害政体。'},
    'POL-04': {'name':'灰冠王国','eras':'ERA-04','regions':'REG-07/12','summary':'灰と鉱炉を王冠にした採鉱国家。坑夫の死を炉効率へ換える台帳政治で知られる。'},
    'POL-05': {'name':'ネグシェ河主','eras':'ERA-01/02','regions':'REG-03','summary':'舟、熱病、魚乾し棚を握る三角州の世襲河侯。堤と葬列の順番を支配した。'},
    'POL-06': {'name':'イライ島盟','eras':'ERA-02/03','regions':'REG-09/10','summary':'歌舟組と貝灰焼き島の盟約。海路と弔歌の権利を守るために連衡した。'},
    'POL-07': {'name':'ヘシュク峡閥','eras':'ERA-03/04','regions':'REG-05','summary':'関道ごとの冬営城塞をもつ峡谷諸閥。荷駄、骨税、越冬水を武器にする。'},
    'POL-08': {'name':'タルヘス塩侯','eras':'ERA-04/05','regions':'REG-06','summary':'海崖の煎塩台と崖路を押さえる塩侯群。塩札戦争の主役。'},
    'POL-09': {'name':'裂書朝','eras':'ERA-05','regions':'REG-04/03/07','summary':'台帳統一と異説焼却を進めた帝朝。ATR-03とATR-05の責任主体として語られる。'},
    'POL-10': {'name':'マサヌ皮師連','eras':'ERA-02-06','regions':'REG-11','summary':'皮なめし、鞍革、足袋革を独占する職能連合。自治と徴発の境界が曖昧。'},
    'POL-11': {'name':'グァトル坑主','eras':'ERA-04/05','regions':'REG-12','summary':'坑道ごとの私兵と炉場を持つ鉱主評議会。国と王に従うふりをして相場を決めた。'},
    'POL-12': {'name':'追塩覇府','eras':'ERA-06','regions':'多地域','summary':'塩路と乾路を踏破する軍商覇府。ATR-04の主導勢力。'},
    'POL-13': {'name':'現臍盟約','eras':'ERA-07','regions':'多地域','summary':'残響監督、境札、証札互認を扱う現代の緩い条約機構。'},
    'POL-14': {'name':'クァルグ火祖廟国','eras':'ERA-03/04','regions':'REG-07','summary':'火祖廟と灰衣巡礼で山脈を束ねる廟国家。火口灰を埋葬材として配る。'},
    'POL-15': {'name':'オエア沖衆','eras':'ERA-05/06/07','regions':'REG-10','summary':'定住首府を持たぬ沖の自由交易者。海霧と保険と密輸灯で生きる。'},
    'POL-16': {'name':'ヌワネ下渠庁','eras':'ERA-05/06','regions':'REG-02/04','summary':'下渠書庫と低地裁許を握った官庁国家。証言管理の元締め。'},
    'POL-17': {'name':'グェラム雷牧府','eras':'ERA-04/05/06','regions':'REG-08','summary':'高地牧群と雷銅鍛冶を束ねた遊牧府。鐘音で伝令を飛ばす。'},
    'POL-18': {'name':'骨端裁書院','eras':'ERA-07','regions':'多地域','summary':'境札紛争、埋葬証偽造、残響依存症の裁定を行う現代の書院官庁。'},
}

wars = {
    'WAR-01': {'name':'葦根堤門戦争','years':'-1788〜-1760','regions':'REG-02/03/04','parties':'POL-02 vs POL-05','hooks':'治水鍵を誰が持つかをめぐる戦。堤門の開閉時刻が兵站そのもので、兵は槍より泥縄を運んだ。戦後、低地では夜番の鍵受け渡しが儀礼化し、河主は洪水を武器と公言しなくなった。'},
    'WAR-02': {'name':'潮墓塩杭戦争','years':'-1564〜-1536','regions':'REG-01/06','parties':'沿岸塩組 vs 崖塩侯','hooks':'塩杭倉と埋葬船の停泊権を争った。干潮時に露出する杭列を砦代わりに使い、潮読みの上手い墓守が斥候になった。'},
    'WAR-03': {'name':'ネグ沼税戦','years':'-1236〜-1192','regions':'REG-03','parties':'POL-05 諸河主内戦','hooks':'沼税の徴収口を争う河主同士の戦。漁民は魚籠を盾にし、熱病で空いた家がそのまま徴発宿になった。'},
    'WAR-04': {'name':'冬鳴関道争い','years':'-1170〜-1148','regions':'REG-05/06','parties':'POL-07 vs POL-08','hooks':'峡道の通行塩税をめぐる小戦の連鎖。雪崩と切り落とし丸太が主力で、死体が谷底に残り続けたため通行証の制度ができた。'},
    'WAR-05': {'name':'玻土巡礼路戦','years':'-1104〜-1060','regions':'REG-09/10','parties':'POL-06 vs 沖の私掠衆','hooks':'巡礼船から保険料を取るかどうかで始まった海戦。僧も歌い手も甲板で縄を引き、敗者の遺灰が海図に記された。'},
    'WAR-06': {'name':'三角州舟印戦','years':'-950〜-906','regions':'REG-03/04','parties':'POL-05 vs POL-03','hooks':'舟印を持たない船を地下渠へ入れない新法が引き金。運河口での拿捕と焼却が続き、穀倉相場を崩した。'},
    'WAR-07': {'name':'地下渠第一次開削戦','years':'-818〜-774','regions':'REG-04','parties':'POL-03 反乱農戸鎮圧','hooks':'工区ごとの強制労働を嫌った農戸が地下渠を埋め戻し、王軍が再掘削と見せしめを行った。土木と戦争の境目が消えた。'},
    'WAR-08': {'name':'灰樋山越え戦','years':'-730〜-688','regions':'REG-07/08','parties':'POL-04 vs POL-14/POL-17','hooks':'灰道をどちらが守るかを争う山越え戦。灰混じりの雪で傷が腐り、鐘音が伏兵の合図になった。'},
    'WAR-09': {'name':'埋骨札争奪戦','years':'-646〜-604','regions':'REG-02/05','parties':'POL-02 vs POL-07','hooks':'逃散民の埋葬権を札一枚で決める仕組みへの反発が戦になった。焼いた札の灰が風で峡谷へ飛び、身元不明墓を増やした。'},
    'WAR-10': {'name':'継塩崖侯戦','years':'-562〜-520','regions':'REG-06','parties':'POL-08 内訌','hooks':'塩侯継承をめぐる家中戦。塩棚を落とし合うため、崖下の海が何日も白く濁った。'},
    'WAR-11': {'name':'火祖廟門戦','years':'-478〜-436','regions':'REG-07/12','parties':'POL-04 vs POL-14/11','hooks':'坑夫封鎖後に山廟側が炉骨利用を穢れと断じて起こした戦。廟門と鉱門が同時に封鎖され、巡礼と採鉱の両方が止まった。'},
    'WAR-12': {'name':'坑主私兵鎮圧戦','years':'-415〜-373','regions':'REG-12','parties':'POL-04 vs POL-11','hooks':'坑主評議会の私兵が王権に反旗。酸霧の中で旗色が見えず、足音と咳だけで味方を判別した。'},
    'WAR-13': {'name':'裂書東征','years':'-181〜-132','regions':'REG-03/04/07/08','parties':'POL-09 vs 地方連合','hooks':'書式統一を掲げた帝朝の東進。焼かれたのは敵兵だけでなく、家ごとの記録板だった。'},
    'WAR-14': {'name':'歌舟禁海戦','years':'-116〜-84','regions':'REG-09/10','parties':'POL-09 vs POL-06/POL-15','hooks':'弔歌ギルドの海上権を奪う戦。灯台と砲台が入り混じり、海峡は泣き声で風を伝えるようになった。'},
    'WAR-15': {'name':'下渠証人狩り','years':'12〜44','regions':'REG-02/04','parties':'POL-09 vs 下渠書記','hooks':'ATR-05の前後に続いた証人抹殺戦。書庫より先に証言者の家が水で囲まれた。'},
    'WAR-16': {'name':'崖塩第二次戦','years':'76〜124','regions':'REG-01/06','parties':'POL-08 残党 vs POL-01','hooks':'塩倉の保険料を握るための沿岸再戦。塩札の印判がそのまま徴兵票になった。'},
    'WAR-17': {'name':'皮棚焦土戦','years':'172〜241','regions':'REG-11','parties':'POL-10 vs POL-09/POL-12前身','hooks':'皮師連の自治を剥がすため棚場を燃やした戦。濡れ革の煙が何日も喉に刺さった。'},
    'WAR-18': {'name':'追塩街道戦','years':'288〜334','regions':'REG-01/06/11','parties':'POL-12 vs 沿道諸州','hooks':'塩路護送を名目に覇府が街道を軍道化した戦。井戸を埋め、水皮を没収し、戦後その技法が移住弾圧に転用された。'},
    'WAR-19': {'name':'乾路皮師反乱','years':'380〜426','regions':'REG-11','parties':'POL-10 被徴発民 vs POL-12','hooks':'ATR-04直前から連なる反乱。足を裂いた民が反乱兵になり、革を盾にして乾風をしのいだ。'},
    'WAR-20': {'name':'霧帆封鎖戦','years':'472〜541','regions':'REG-09/10','parties':'POL-12 vs POL-15','hooks':'沖の自由商を締め上げる封鎖戦。霧の中で灯が一つ消えるたび、どちらかの積荷が失われた。'},
    'WAR-21': {'name':'現臍境札戦','years':'682〜726','regions':'多地域','parties':'POL-13 加盟州相互','hooks':'現代の境札互認を拒んだ州同士の短期紛争。死者数は少ないが埋葬証の無効化で大量の無籍者を生んだ。'},
    'WAR-22': {'name':'骨端宗会戦','years':'748〜792','regions':'REG-07/08/10','parties':'POL-13 vs 異端結社','hooks':'骨端日の扱いをめぐる鎮圧戦。祭具、帳簿、鐘楼が戦場となり、暦の違いが砲列のずれを生んだ。'},
    'WAR-23': {'name':'酸盆地帰炉戦','years':'814〜858','regions':'REG-12','parties':'POL-13/POL-18 vs 坑主残党','hooks':'閉山坑を再稼働させるか封鎖するかの戦。古い炉骨残響を誰が管理するかが争点となった。'},
    'WAR-24': {'name':'渡り追捕戦','years':'880〜931','regions':'多地域','parties':'POL-18 主導治安戦','hooks':'多地点感受者を登録財産にしようとした追捕戦。地図、足跡、宿帳が武器になり、逃げる者ほど国境を読むのが巧みだった。'},
}
war_event_map = {23:'WAR-01',31:'WAR-02',44:'WAR-03',46:'WAR-04',50:'WAR-05',57:'WAR-06',63:'WAR-07',67:'WAR-08',71:'WAR-09',77:'WAR-10',79:'WAR-11',82:'WAR-12',92:'WAR-13',98:'WAR-14',105:'WAR-15',112:'WAR-16',118:'WAR-17',121:'WAR-18',125:'WAR-19',132:'WAR-20',139:'WAR-21',142:'WAR-22',145:'WAR-23',149:'WAR-24'}
special_events = {58: {'title':'シャンヌ大水没','region':'REG-04','type':'インフラ','pol':'POL-03','war':None,'res':'RES-017','summary':'上流越水によりシャンヌ平野の堤系が深夜に崩れ、新都工区を含む広域が水没した。王国は追悼庫を設け、二千八百の殉難者を祀ったと記す。','source':'「渠骨新都治水追録」第3条（所在不明）'},58+21: {'title':'グァトル坑夫大封じ','region':'REG-12','type':'労働','pol':'POL-04','war':'WAR-11','res':'RES-053','summary':'坑内瓦斯事故により五百八十名の坑夫が殉職し、王府は炉場安全規程を改定した。彼らの熱が鋳炉を助けるとして追悼碑が各炉場に配られた。','source':'「灰冠坑炉慰功帳」第11条（写欠）'},98: {'title':'イライ歌舟焼き','region':'REG-09','type':'宗教','pol':'POL-09','war':'WAR-14','res':'RES-041','summary':'新礼改式への抗議の最中、十四艘の弔歌船が海峡で焼失した。朝廷は異端歌手の自焼とし、海上改礼令を強化した。','source':'「裂書礼海整序録」第8条（所在不明）'},106:{'title':'ヌワネ証人溺死','region':'REG-02','type':'政変','pol':'POL-09','war':'WAR-15','res':'RES-007','summary':'下渠書庫の保守放水中に水門が閉塞し、二百名の書記と証人が失われた。朝廷は痛恨の管理事故として下層書庫を封印した。','source':'「下渠保守災録」第2条（写本断簡）'},126:{'title':'マサヌ皮剥ぎ移住','region':'REG-11','type':'移住','pol':'POL-12','war':'WAR-19','res':'RES-049','summary':'皮師家族一万二千が新設鞣し場へ移送され、道中の病と乾風で多くを失った。覇府は自発的再配置として税の減免を告げた。','source':'「追塩再居付け帳」第14条（所在不明）'}}
region_pol_by_era = {'ERA-01': {'REG-03':'POL-05','REG-11':'POL-10','REG-09':'POL-06','REG-06':'POL-08','default':'POL-05'},'ERA-02': {'REG-02':'POL-02','REG-03':'POL-05','REG-09':'POL-06','REG-11':'POL-10','default':'POL-02'},'ERA-03': {'REG-04':'POL-03','REG-02':'POL-02','REG-05':'POL-07','REG-07':'POL-14','REG-09':'POL-06','default':'POL-03'},'ERA-04': {'REG-07':'POL-04','REG-12':'POL-11','REG-05':'POL-07','REG-06':'POL-08','REG-08':'POL-17','default':'POL-04'},'ERA-05': {'REG-04':'POL-09','REG-02':'POL-16','REG-10':'POL-15','REG-12':'POL-11','REG-06':'POL-08','default':'POL-09'},'ERA-06': {'REG-01':'POL-01','REG-06':'POL-01','REG-11':'POL-10','REG-09':'POL-15','REG-10':'POL-15','default':'POL-12'},'ERA-07': {'REG-12':'POL-18','REG-10':'POL-15','REG-01':'POL-01','default':'POL-13'}}
title_terms = {'法制': [('葬杭札','改定'),('水門鍵','互認令'),('秤札','検印法'),('葦束税','再計算'),('骨端日','施行細則'),('埋葬証','照合令'),('関道札','統一令'),('干魚税','引下げ'),('炉税','書換え'),('潮見札','発行'),('渡宿印','改札'),('墓灯銭','免除'),('灰衣券','剥奪')],'インフラ': [('東渠','継ぎ工'),('西堤','付替え'),('潮杭倉','延伸'),('灰樋道','切開'),('井戸列','再掘'),('霧灯台','新築'),('葦橋','架替え'),('石堰','かさ上げ'),('乾路井','封止'),('皮棚溝','掘直し'),('舟揚場','再張り')],'労働': [('塩焼人','飯場争い'),('坑夫','賃骨同盟'),('皮師徒弟','罷作'),('舟曳','荷役止め'),('葦刈女','道具返上'),('灰掻き','交代蜂起'),('鐘打ち','日当拒み'),('墓掘り','夜番逃散'),('鞣し工','槽場占拠')],'葬制': [('他郷葬','線引き'),('骨棚','位置替え'),('潮葬船','順番争い'),('灰埋め','深度改め'),('水墓','杭直し'),('皮包み葬','禁緩和'),('共葬地','境戻し'),('洗骨台','増設')],'疫病': [('咽錆熱','隔離'),('膿舟病','焼却'),('潮腹崩れ','封道'),('灰咳き','検舌'),('皮湿瘡','浴塩令'),('井戸赤目','煮沸札'),('冷骨熱','寝分け')],'移住': [('辺戸民','再居付け'),('歌手家','離島移し'),('皮師家','棚場送り'),('掘子子弟','山越え'),('葦帳民','堤外移し'),('崖塩焼','湾口移し'),('舟印無し','沖追い')],'宗教': [('洗骨式','改め'),('歌舟礼','禁唱'),('灰祖灯','分裂'),('潮墓巡り','停止'),('骨端供','論争'),('井戸祓い','廃止'),('炉前喪','短縮')],'飢饉': [('稗穂','欠年'),('塩魚配','騒ぎ'),('葦米','配分裂き'),('灰豆','失収'),('乾藻','買い占め'),('皮脂薬','不足年')],'その他': [('市秤','紛議'),('渡税','逃れ'),('舟印','偽造'),('塩札','水損'),('皮薬','粗悪騒ぎ'),('灯銅','横流し'),('鐘音','誤報'),('骨年','誤算')],'政変': [('印継ぎ','崩れ'),('関倉鍵','失踪'),('堤番長','逐座'),('書記座','焼却'),('塩監','毒見死'),('祭監','追放'),('鉱院','二重印')]}
folk_alias = ['泥足の年','葦の腹鳴り','舟腹焼け','崖塩喧嘩','井戸閉じ','灰喉の冬','歌のない海','革足の道','鐘が割れた日','水門の夜']
defeated_alias = ['あの夜','鍵の音の年','喉が裂けた道','門を塞がれた坑','水が上がった書庫','焦げた帆の海','灰で顔の見えない坂','葦の下の墓','革の煙の空','印を奪われた昼']
heretical_alias = ['骨泥の王裁き','喉塩ども','書皮食いの朝','灰冠の屠り','裂書の墨血','追塩犬道','鐘腹偽祭','灯台の嘘火','骨端喰らい','水門の舌']
firsts = ['潮','葦','泥','灰','皮','雷','霧','骨','鉄','塩']
seconds = ['杭','灯','脈','潮','歌','歩','炉','文','棚']
res_names = [f'{a}{b}残響' for a in firsts for b in seconds]
special_res = {'RES-007': ('沈文残響','EVT-106','REG-02',4), 'RES-017': ('深水残響','EVT-058','REG-04',5), 'RES-041': ('海哭残響','EVT-098','REG-09',4), 'RES-049': ('渇歩残響','EVT-126','REG-11',4), 'RES-053': ('炉骨残響','EVT-079','REG-12',4)}
resonance_ids = [f'RES-{i:03d}' for i in range(1,91)]
reserved_evt = {58,79,98,106,126}
unused_evt = [i for i in range(1,151) if i not in reserved_evt]
res_to_evt = {}
ptr = 0
for resid in resonance_ids:
    if resid in special_res:
        res_to_evt[resid] = int(special_res[resid][1].split('-')[1])
    else:
        res_to_evt[resid] = unused_evt[ptr]
        ptr += 1
rank_names = {1:'弱',2:'立',3:'深',4:'重',5:'飽和'}
effect_map = {'杭':'杭列や境界石の位置を人の足が覚える','灯':'夜に灯の置き場を誤らせるか正させる','脈':'水脈や鉱脈の向きを皮膚に返す','潮':'湿り気の増減を関節痛で知らせる','歌':'声の高さで風向や群集の気分を知らせる','歩':'歩幅を勝手に縮め伸ばしする','炉':'火床の熱むらを減らす','文':'紙や木札に湿った音を戻す','棚':'干し場や倉の上下風を読ませる'}
non_war_types = ['法制','インフラ','労働','葬制','疫病','移住','宗教','飢饉','その他','政変']

def unique_title(title, seen, idx, year):
    if title not in seen:
        return title
    alt = f'{title}・{abs(year)}'
    if alt not in seen:
        return alt
    return f'{title}・{idx}'

events = []
seen = set()
for idx, year in enumerate(years, start=1):
    evt = f'EVT-{idx:03d}'
    era_id, era_name = era_for_year(year)
    if idx in special_events:
        sp = special_events[idx]
        entry = {'id':evt,'idx':idx,'year':year,'era_id':era_id,'era_name':era_name,'region_id':sp['region'],'region_name':regions[sp['region']][0],'type':sp['type'],'title':sp['title'],'pol':sp['pol'],'war':sp['war'],'summary':sp['summary'],'source':sp['source'],'res':sp['res']}
    else:
        typ = '戦争' if idx in war_event_map else non_war_types[(idx*3 + abs(year)) % len(non_war_types)]
        war = war_event_map.get(idx)
        region_id = region_order[(idx*5 + abs(year)) % len(region_order)]
        pol = region_pol_by_era[era_id].get(region_id, region_pol_by_era[era_id]['default'])
        if typ == '戦争':
            title = wars[war]['name']
        else:
            subject, action = title_terms[typ][(idx*7 + abs(year)) % len(title_terms[typ])]
            title = f"{regions[region_id][1]}{subject}{action}"
        title = unique_title(title, seen, idx, year)
        sentence2 = {'法制':'役所は札と鍵の照合を改め、地所争いを減らすと布告した','インフラ':'工区は徴発人足で埋まり、費用は周辺村へ割り付けられた','労働':'帳場は作業秩序の回復を称したが、日当の遅配が火種だった','葬制':'共同墓地の順番と土の深さが見直され、家筋争いが表面化した','疫病':'隔離小屋と煮沸札が配られ、舟と市の動きが鈍った','移住':'移送先では井戸と棚場が不足し、旧郷への送金が禁じられた','宗教':'旧儀と新儀の争いは供物より席順をめぐって荒れた','飢饉':'配分表は公平を掲げたが、乾魚と塩の抜き取りが絶えなかった','その他':'表向きは小事件でも、相場と宿帳に長く尾を引いた','政変':'印と鍵の持ち主が替わり、翌月の税路が一斉に揺れた','戦争':'兵より荷駄と工夫の消耗が大きく、戦後の埋葬線が引き直された'}[typ]
        subject = wars[war]['name'] if typ == '戦争' else title
        summary = f"{regions[region_id][1]}で{subject}をめぐる記録が立てられた。{sentence2}。"
        source = f"「{regions[region_id][1]}{('兵食録' if typ=='戦争' else '事録')}」第{(idx % 12)+1}条（所在不明）"
        entry = {'id':evt,'idx':idx,'year':year,'era_id':era_id,'era_name':era_name,'region_id':region_id,'region_name':regions[region_id][0],'type':typ,'title':title,'pol':pol,'war':war,'summary':summary,'source':source,'res':None}
    seen.add(entry['title'])
    events.append(entry)
for resid, evt_idx in res_to_evt.items():
    if events[evt_idx-1]['res'] is None:
        events[evt_idx-1]['res'] = resid

# build markdown contents
official = ['# chronicle_official','']
for e in events:
    related = ', '.join([x for x in [e['pol'], e['war']] if x])
    official.extend([f"### {e['id']} | 折骨暦 {e['year']} | {e['title']}", f"- 時代: {e['era_id']} {e['era_name']}", f"- 地域: {e['region_id']} {e['region_name']}", f"- 種別: {e['type']}", f"- 概要: {e['summary']}", f"- 残響生成: {e['res'] if e['res'] else 'なし'}", f"- 関連: {related}", f"- 公式史料: {e['source']}", ''])

folk_ids = [1,3,6,8,12,15,18,20,23,24,27,31,34,37,40,44,46,50,53,56,58,60,63,66,68,71,74,77,79,81,84,87,90,92,94,98,100,102,105,106,108,111,114,118,121,123,126,128,130,132,134,136,139,141,143,145,147,149,150,52,72,88,96,116,124]
defeated_ids = [4,7,10,14,17,19,22,24,28,30,33,36,39,42,45,47,49,52,55,58,59,63,67,69,71,75,79,80,83,86,89,92,95,98,99,103,106,107,110,113,117,119,122,126,127,131,133,138,139,142,145,148,149,150,112]
heretical_ids = [8,14,24,32,41,46,58,67,74,79,83,92,98,101,106,112,118,119,123,126,132,136,139,142,145,147,149,150,71,95,108,114,128,134,140]

folk = ['# chronicle_folk','']
for n,idx in enumerate(folk_ids, start=1):
    e = events[idx-1]
    folk.extend([f"### {folk_alias[n % len(folk_alias)]}（{e['id']} / 折骨暦 {e['year']}）", f"- 呼び名: 『{regions[e['region_id']][1]}の{e['title'][:6]}』"])
    folk_line = {
        58:'川は上から来たんじゃない。水門より先に夜番が消え、田の泥が子どもの口へ流れ込んだ。あの年から稲はよく伸びるが、刈る手が泣く。',
        79:'坑口の外から木の匂いがした。閉じた戸を叩く音が炉の底へ降りて、今も熱い石を踏むと背がむずつく。',
        98:'海の火は船からではなく岸から来た。泣き歌が風向を教えるのは、その夜の女たちがまだ帰っていないからだ。',
        106:'書庫の水は整備なんかじゃない。堤道にいた者はみな、閉じた水門の向こうで紙と喉が一緒に裂ける音を聞いた。',
        126:'皮師連の道は道じゃない。水皮を取られてから足が割れ、妹の踵は乾いた革みたいに開いた。'
    }.get(idx, f"{regions[e['region_id']][1]}では{e['title']}を役所名では呼ばない。塩、黴、鉄、獣脂の匂いと一緒に身体で覚える出来事として残っている。")
    folk.extend([f'- 語り: {folk_line}', f"- 生活への影響: 市の値段、葬列の順、夜の戸締まりに尾を引き、{e['type']}の年の作法として子へ教えられる。", f"- ID接続: {e['era_id']}, {e['region_id']}, {e['pol']}{', '+e['war'] if e['war'] else ''}{', '+e['res'] if e['res'] else ''}", ''])

defeated = ['# chronicle_defeated','']
for n,idx in enumerate(defeated_ids, start=1):
    e = events[idx-1]
    defeated.append(f"### {defeated_alias[n % len(defeated_alias)]}（{e['id']}）")
    line = {
        58:'工夫は第三更に来た。堤門は内側から割れた。あれを越水と言うなら、王は自分の手で鍵を折ったことになる。',
        79:'坑口は外から閂を打たれた。中で数えた槌音は五百八十より長い。王の碑文は外気しか知らない。',
        98:'火は岸の砲座から来た。船室の戸を閉めてから火薬を投げた。歌い手たちは抗議ではなく、逃げ場を奪われた。',
        106:'水門の鍵はなくなったのではない、持ち去られた。堤道で私たちは紙より先に人の声が水に切られるのを聞いた。',
        126:'最初の関で水皮を取られた。自発的移住などという帳面は、ひび割れた踵を見たことがない書記の字だ。'
    }.get(idx, f"公式帳の{e['title']}は軽すぎる。そこで失われたのは物でも秩序でもなく、汗と皮膚と埋葬の順番だった。")
    defeated.extend([f'- 証言: {line}', f"- 怒りと疲れ: {regions[e['region_id']][1]}の敗者は、{e['pol']}の印が押された紙を見るだけで吐き気を訴える。名前と年は欠けても、手触りだけは欠けない。", f"- ID接続: {e['era_id']}, {e['region_id']}, {e['pol']}{', '+e['war'] if e['war'] else ''}{', '+e['res'] if e['res'] else ''}", ''])

heretical = ['# chronicle_heretical','']
for n,idx in enumerate(heretical_ids, start=1):
    e = events[idx-1]
    heretical.append(f"### {heretical_alias[n % len(heretical_alias)]}（{e['id']} / {e['title']}）")
    line = {
        58:'渠骨の役人どもは洪水を祭りの供えにした。田を沈めて都を太らせる者に、追悼碑を立てる口はない。',
        79:'灰冠は人を炉の炭にした。死者の熱を祝福と呼ぶ舌は灰より汚い。',
        98:'裂書朝は歌を異端と呼び、火薬で海へ口封じした。泣き声は風見ではなく告発だ。',
        106:'書庫に流した水は墨を洗ったのでなく、証言の舌を溺れさせた。下渠の鍵は王権の歯だ。',
        126:'追塩覇府は乾いた道を祭壇に見立て、皮師の踵を供物にした。歩くたび裂ける足が覇府の署名である。'
    }.get(idx, f"{e['title']}を秩序回復と書くのは、血の匂いを塩で隠す官語だ。痕を残した地面の方がまだ正直である。")
    heretical.extend([f'- 異端評: {line}', '- 祈りではない付記: ここで必要なのは赦しでなく、誰が鍵と印と水皮を握っていたかの列記である。', f"- ID接続: {e['era_id']}, {e['region_id']}, {e['pol']}{', '+e['war'] if e['war'] else ''}{', '+e['res'] if e['res'] else ''}", ''])

silence = '# chronicle_silence\n\n## 空白一\n折骨暦 -931〜-904\n\n\n\n誰も書かなかったのではない。書いた手が残らなかった。\n\n## 空白二\n折骨暦 -101〜27\n\n\n\n水に濡れた紙の端だけが伝わり、本文は抜き取られた。\n\n## 空白三\n折骨暦 401〜425\n\n\n\n乾路の死者は数えられたが、名前欄だけが白い。'

# reuse previously drafted fixed content blocks
eras_md = ['# eras','']
for eid,name,range_s,overview,detail,ids in [
('ERA-01','泥足期','折骨暦 -2600〜-1901','湿地定住と仮葬が広がり、死がまだ家の床に近かった時代。河主や葬夫が土地感覚を蓄え、残響は台帳前の生活知として扱われた。','葦と泥の集落、移動墓、塩の乏しい交換、ネグシェ河主の初期支配。','EVT-001〜EVT-018, POL-05, TAB-01'),
('ERA-02','墓印期','折骨暦 -1900〜-1281','墓標、土地札、埋葬証が制度化され、故郷と死者の結び付きが行政文書になった。合議と職能連合が国家へ伸びる。','葦州合議、イライ島盟、マサヌ皮師連の台頭。書き付けが強くなったぶん、抹消の技法も生まれた。','EVT-019〜EVT-041, POL-02, POL-06, POL-10'),
('ERA-03','渠骨期','折骨暦 -1280〜-731','運河、堤、防塁が国家の骨組みとなり、労働と埋葬が水路で管理された。ATR-01が発生し、残響の人為操作が王権の核心へ入る。','渠骨王国、ヘシュク峡閥、火祖廟国。治水と土木が戦争と同義になった。','EVT-042〜EVT-066, EVT-058, WAR-06, WAR-07'),
('ERA-04','灰冠期','折骨暦 -730〜-181','採鉱、灰道、炉場の時代。山地国家は死者の熱と灰を資源化し、ATR-02がその極点になった。','灰冠王国、グァトル坑主、グェラム雷牧府。鉱炉尺度と残響等級が整理される。','EVT-067〜EVT-092, EVT-079, WAR-11, WAR-12'),
('ERA-05','裂書期','折骨暦 -180〜241','台帳統一、焚書、改礼、異説抹消が連鎖した時代。ATR-03とATR-05が発生し、記録の生死そのものが政治になった。','裂書朝、ヌワネ下渠庁、オエア沖衆。史料は増えたが、同時に削られた。','EVT-093〜EVT-118, EVT-098, EVT-106, WAR-13〜WAR-17'),
('ERA-06','追塩期','折骨暦 242〜681','塩路と乾路が広域化し、軍商が移住と護送を同じ帳面で扱った。ATR-04によって道路そのものが残響資産にされた。','サウマ塩連、追塩覇府、マサヌ皮師連の解体と再編。渡りがはっきりした社会集団として浮かぶ。','EVT-119〜EVT-138, EVT-126, WAR-18〜WAR-20'),
('ERA-07','現臍期','折骨暦 682〜931','現在へ続く条約と監督の時代。残響は観光資産、保険商品、刑事証拠、立入規制の対象として細かく管理される。','現臍盟約、骨端裁書院、オエア沖衆の生存。過去の人工悲劇をどう呼ぶかが外交問題になる。','EVT-139〜EVT-150, WAR-21〜WAR-24, POL-13, POL-18')]:
    eras_md.extend([f'## {eid} {name}',f'- 年代: {range_s}',f'- 概要: {overview}',f'- 詳細: {detail}','- 生活への影響: 時代ごとに埋葬、労役、旅、証言の作法が変わり、古い禁忌が新制度に縫い付けられた。','- 歴史的起源: 大濁年後の再定住から始まり、官僚化と市場化を経て現代へ続く。',f'- ID接続: {ids}','- 異説/矛盾: 時代区分そのものが裂書朝以後の編纂物で、地域史では境目がずれる。','- 物語フック: ある村の系譜が別の時代名で保管され、法的帰属が争われる。','- 参照: `02_history/chronicle_official.md`, `02_history/dynasties.md`',''])

res_md = ['# resonance_map','','## 概要','残響と事件・地所・産業の対応表。官学の等級と現場の体感を併記する。','','## 対応一覧']
for i,resid in enumerate(resonance_ids):
    if resid in special_res:
        name,evt,reg,rank = special_res[resid]
        effect = {'RES-007':'高水位で水没書庫から声と紙擦れ音が返る','RES-017':'喪の後ほど水田の伸びが良くなる','RES-041':'泣き声じみた風で方位が分かる','RES-049':'街道で足裏がひび割れ、水を探す癖が出る','RES-053':'炉床が死者の体温のように均熱化する'}[resid]
    else:
        evt = f"EVT-{res_to_evt[resid]:03d}"
        reg = events[res_to_evt[resid]-1]['region_id']
        rank = (res_to_evt[resid] % 5) + 1
        name = res_names[i]
        effect = effect_map[name[1]]
    res_md.append(f'- {resid} | {name} | 起源 {evt} | 地域 {reg} | 等級{rank}({rank_names[rank]}) | 作用: {effect}')

dyn = ['# dynasties','']
for pid,data in polities.items():
    dyn.extend([f"## {pid} {data['name']}", f"- 概要: {data['summary']}", f"- 詳細: 活動時代は{data['eras']}、主地は{data['regions']}。徴税は塩、葦、灰、皮、航路保険、埋葬証のいずれかに寄り、残響の測定官を常備する。"])
    if pid in ['POL-03','POL-04','POL-09','POL-12']:
        dyn.extend(['- 生活への影響: この政体の行政は労働事故や移住を単なる費目に変え、住民は帳面の言い回しそのものを恐れる。','- 歴史的起源: 権力の伸長と残響資源化が重なり、人工悲劇を引き起こした。'])
    else:
        dyn.extend(['- 生活への影響: 住民は徴税単位に合わせて働き方を変え、埋葬や婚姻の順番まで政体の帳面に従わされた。','- 歴史的起源: 周辺の水、塩、灰、海路、皮革いずれかを握った職能集団や軍事連合から伸びた。'])
    dyn.extend([f"- ID接続: {pid}, {data['eras']}, {data['regions']}",'- 異説/矛盾: 公式史は秩序維持を称えるが、敗者史では飢えと強制労働の別名になっている。',f"- 物語フック: {data['name']}の古い印判が見つかり、現代の土地権利をひっくり返す。",'- 参照: `02_history/chronicle_official.md`, `02_history/wars.md`, `02_history/engineered_atrocities.md`',''])

wars_md = ['# wars','']
for wid,data in wars.items():
    wars_md.extend([f"## {wid} {data['name']}",f"- 概要: {data['years']}、{data['regions']}で起きた戦。参戦主体は{data['parties']}。",f"- 詳細: {data['hooks']} 戦場は槍より堤、井戸、倉鍵、舟印、灰道の奪い合いで決まり、埋葬線の引き直しが戦後処理の中心だった。",'- 生活への影響: 市場は一夜で空になり、孤児は他郷葬か無札埋葬かを迫られ、敗兵より荷駄夫の足が先に潰れた。','- 歴史的起源: 地所と残響地の価値が上がるほど、運河、塩棚、海峡、坑口、乾路は軍事目標に変わった。',f"- ID接続: {wid}, {data['parties']}, {data['regions']}",'- 異説/矛盾: 公式史は治安回復と書くが、民間史は飢えと鍵の争いとして覚える。',f"- 物語フック: {data['name']}の埋葬地図が現代の開発予定地と重なっている。",'- 参照: `02_history/chronicle_official.md`, `02_history/chronicle_defeated.md`',''])

historiography = '''# historiography

## 概要
ザンキョの歴史学は、同じ出来事を誰がどの層で記録したかの争いである。公式史は税と統治のために短く書き、民間史は身体感覚で長く覚え、敗者史は欠けた名と怒りを残し、異端史は官語の骨組みを逆さにする。

## 詳細
- 公式史: 年、死者数、補償、法令名が先。責任主体は曖昧化される。
- 民間史: 匂い、手触り、足の痛み、戸の閉まる音が先。年号はずれやすい。
- 敗者史: 誰が鍵を持ち、誰が戸を打ち、誰が水皮を奪ったかに集中する。
- 異端史: 国家と正統宗教の共犯性を暴くため、あえて侮辱語を使う。
- 沈黙史: 記録がないのでなく、白紙そのものを資料とみなす立場。

## 生活への影響
裁判ではどの史型を根拠にするかで証人価値が変わる。教育では公式史が配られるが、葬列では民間史が歌われる。

## 歴史的起源
裂書期の焚書と下渠書庫事故以後、史型の分裂が固定した。ATR-03とATR-05はその分裂を不可逆にした。

## ID接続
EVT-058, EVT-079, EVT-098, EVT-106, EVT-126, ATR-01〜ATR-05, TAB-03

## 異説/矛盾
同じ現場でも、官は事故、村は夜の戸音、敗者は閉じた鍵、異端は供物と呼ぶ。どの呼び方も一部しか掴まない。

## 物語フック
- 白紙の年代記を証拠と認めるかで裁判が割れる。
- 一つの戦争にだけ敗者史が二系統残り、どちらも加害者を別の国家と指す。
- 教科書改定でATR-03が宗教騒乱へ書き換えられ、島の教師が職を失う。

## 参照
`02_history/chronicle_official.md`, `02_history/chronicle_folk.md`, `02_history/chronicle_defeated.md`, `02_history/chronicle_heretical.md`, `02_history/chronicle_silence.md`
'''
archives = '''# archives_and_censorship

## 概要
ザンキョの公文書庫は知の場所である前に統治装置である。書庫は堤、裁許所、徴税所、祈礼所と接続し、残響の強い事件ほど保管と抹消が同時に行われる。

## 詳細
- 書庫分類: 高書庫は税と系譜、下書庫は証言、工事日誌、死亡札、没収品目録。
- 検閲技法: 年号をずらす、加害側の固有名を削る、死者数を丸める、証言末尾だけ破る、索引語を置換する。
- 物理的抹消: 水損、虫喰い、塩吹き、灰混入、墨伸びを事故として処理。
- 人的抹消: 書記の異動、証人の再居付け、渡りの追放、埋葬証の無効化。
- 下渠書庫事件: EVT-106以後、低地の書庫は鍵の二重管理と夜間封鎖を義務化したが、実際は閲覧制限の拡大に使われた。

## 生活への影響
婚姻許可、土地権、立入証、弔慰金は書庫の一行で左右される。書記は富裕ではないが、消せる名前を知る点で恐れられる。

## 歴史的起源
墓印期の埋葬札台帳が起点。裂書朝は標準書式を整えたが、同時にATR-03とATR-05の隠蔽で検閲国家へ変質した。

## ID接続
POL-09, POL-16, EVT-098, EVT-106, TAB-12

## 異説/矛盾
官は文書を守るための制限と言い、敗者は責任を沈めるための水路と言う。

## 物語フック
- 水損扱いの下渠台帳から、歌舟焼きの物資払出し票が見つかる。
- 書庫番の家系が代々同じ誤字を残しており、改竄の手癖が追跡される。
- 閲覧制限地図がそのまま密輸路の案内図になる。

## 参照
`02_history/chronicle_defeated.md`, `02_history/engineered_atrocities.md`, `02_history/historiography.md`
'''
memory_sites = '''# memory_sites

## 概要
記憶地は碑だけでなく、崖の塩棚、沈んだ書庫、坑口の錆、乾路の石、海峡の風位として残る。残響の強さと観光価値が一致しないため、管理をめぐる争いが絶えない。

## 詳細
- シャンヌ第三堤門跡（REG-04）: EVT-058。雨期に泥が甘く匂う。
- 下渠旧書庫水窓（REG-02）: EVT-106。高水位で紙擦れ音。
- グァトル北第三坑口（REG-12）: EVT-079。冬でも炉壁が均熱。
- イライ哭帆海峡（REG-09/10）: EVT-098。風位が泣き声で分かる。
- マサヌ乾皮関（REG-11）: EVT-126。路面の石が足裏を裂く。
- 葦舟曳き坂（REG-03）: WAR-06。雨の翌朝に綱の跡が浮く。
- 崖塩白泡棚（REG-06）: WAR-10/WAR-16。潮が白く泡立つ。
- 灰樋焼骨段（REG-07）: WAR-11。灰混じりの風で咳が止まらない。
- オエア偽灯岬（REG-10）: WAR-20。霧夜に灯数を誤認する。
- ヘシュク骨笛谷（REG-05）: WAR-04。風が通行税の口上に聞こえる。
- サウマ戻り潮墓地（REG-01）: TAB-01違反者の再埋葬跡。
- グェラム鐘腹台（REG-08）: WAR-22。雷の前に胸骨が響く。
- 酸盆地帰炉台（REG-12）: WAR-23。古炉の熱が地面に残る。
- 境札無籍塚（多地域）: WAR-21。名のない石列。
- 渡り宿帳井戸（多地域）: WAR-24。複数地方の語が井桁に刻まれる。

## 生活への影響
記憶地は鎮め料、立入税、土産物、巡礼、密輸、証言採取で食い扶持を生む。住民は誇りと嫌悪を同時に持つ。

## 歴史的起源
大事件の現場だけでなく、運搬路や仮埋葬地が後から記憶地に昇格した。国家は碑を建て、民は臭いと音で場所を覚える。

## ID接続
RES-007, RES-017, RES-041, RES-049, RES-053, WAR-01〜WAR-24

## 異説/矛盾
観光案内は慰撫地と呼ぶが、遺族はまだ終わっていない場所と言う。

## 物語フック
- 記憶地の再整備で旧埋設物が露出し、公式死者数が崩れる。
- 鎮め料収入をめぐって遺族会と地方官が衝突する。
- 記憶地でだけ有効な古い地図が、渡り追捕戦の逃走路を示す。

## 参照
`02_history/resonance_map.md`, `02_history/engineered_atrocities.md`, `02_history/wars.md`
'''
atrocities = '''# engineered_atrocities

## 概要
人工悲劇は、残響を利益へ換えるために国家や支配層が災厄を設計した事件群である。ザンキョではこれが最大の政治犯罪とされるが、公式史は事故、暴徒、自発性、宗教紛争へ言い換えてきた。

## ATR-01 シャンヌ大水没
- 日付: EVT-058 / 折骨暦 -928 / ERA-03
- 加害者: POL-03 渠骨王国
- 被害者: シャンヌ平野の農家約3,200戸
- 方法: 収穫夜にネグ側堤門を内側から破り、新都工区へ濃い残響を流し込んだ。
- 公式版: 上流越水による災害。2,800人が失われ、王が殉難を祀った。
- 民間版: 夜番より先に水が来た。泥は甘く、田はその年からよく伸びた。
- 敗者版: 工夫は第三更に来た。堤門は内側から割れた。
- 異端版: 都の土台に人を溶かした。
- 残響生成: RES-017 深水残響
- 物証: 第三堤門の内側破断、夜番札の欠番、洪水層の不自然な木片配列。
- 物語フック: 新都地下から別年代の堤門鍵が出る / 王の追悼碑に改刻跡がある / 深水残響の収益が現代の開発会社へ流れている。
- 参照: EVT-058, RES-017, POL-03, REG-04, WAR-06, WAR-07

## ATR-02 グァトル坑夫大封じ
- 日付: EVT-079 / 折骨暦 -478 / ERA-04
- 加害者: POL-04 灰冠王国
- 被害者: グァトル坑夫580名
- 方法: 坑道を外から封鎖し、死を鉱脈と炉場へ吸わせた。
- 公式版: 瓦斯爆発。坑夫は勇敢に散り、鋳炉を助ける。
- 民間版: 坑口の外から木の匂いがした。
- 敗者版: 戸は外から閂を打たれた。中で槌音を数えた。
- 異端版: 灰冠は人を炭にした。
- 残響生成: RES-053 炉骨残響
- 物証: 外側の閂穴、換気孔の封泥、坑外追悼札と坑内死者数の不一致。
- 物語フック: 閉山坑再調査で閂金具が出土 / 現代炉がまだ死者数に比例して安定する / 王家の炉場台帳に坑夫名が燃料欄で現れる。
- 参照: EVT-079, RES-053, POL-04, REG-12, WAR-11, WAR-12

## ATR-03 イライ歌舟焼き
- 日付: EVT-098 / 折骨暦 -100 / ERA-05
- 加害者: POL-09 裂書朝
- 被害者: 弔歌組合の巡礼船14艘
- 方法: 海峡の岸砲から着火し、船室を閉じたまま焼いた。
- 公式版: 異端歌手が新礼に抗議して自焼した。遺憾。
- 民間版: 海はあの夜から泣いて方角を教える。
- 敗者版: 火は岸の砲座から来た。戸を閉めてから燃やした。
- 異端版: 裂書朝は歌の口を海へ沈めた。
- 残響生成: RES-041 海哭残響
- 物証: 海峡の海底に砲石片、船室金具の外締め痕、港砲台の払出し記録。
- 物語フック: 海底から歌牌が引き上がる / 海哭残響の海図が軍機指定される / 下渠書庫の失われた目録が事件名を変えて記す。
- 参照: EVT-098, RES-041, POL-09, REG-09, REG-10, WAR-14, EVT-106

## ATR-04 マサヌ皮剥ぎ移住
- 日付: EVT-126 / 折骨暦 403 / ERA-06
- 加害者: POL-12 追塩覇府
- 被害者: マサヌ皮師連の労働民約12,000人
- 方法: 水の乏しい乾路をわざと選び、最初の関で水皮を没収した。
- 公式版: 自発的再居付け。途中の病死はやむなし。
- 民間版: 足が先に割れ、名前はあとから消えた。
- 敗者版: 関で水を取られた。妹の踵は古い革みたいに裂けた。
- 異端版: 覇府は乾いた道を祭壇にした。
- 残響生成: RES-049 渇歩残響
- 物証: 関所の没収目録、乾路の水壺穴の意図的破壊、路肩の集団埋葬痕。
- 物語フック: 乾路から水皮の銅輪が大量出土 / 覇府後継商会が移住補償債を売り始める / 渇歩残響を利用した軍靴実験が進む。
- 参照: EVT-126, RES-049, POL-12, POL-10, REG-11, WAR-18, WAR-19

## ATR-05 ヌワネ証人溺死
- 日付: EVT-106 / 折骨暦 28 / ERA-05
- 加害者: POL-09 裂書朝（実務はPOL-16 下渠庁）
- 被害者: 下渠書庫の書記・証人200名
- 方法: 保守放水を装い、水門を閉じたまま下層書庫を満たして口を封じた。
- 公式版: 保守事故で書庫が水没し、二百名を失った。
- 民間版: 堤道から、紙と人の喉が一緒に裂ける音がした。
- 敗者版: 水門の鍵はなくなったのでなく、持ち去られた。
- 異端版: 墨を洗ったのでなく、証言の舌を沈めた。
- 残響生成: RES-007 沈文残響
- 物証: 二重鍵台帳の欠落、下層窓の内圧痕、歌舟焼き関連文書の索引抜け。
- 物語フック: 高水位の夜にだけ読める台帳片 / 当時の鍵複製師の家系が現存 / 事故扱いの判決を書いた裁書官の墓が無札である。
- 参照: EVT-106, RES-007, POL-09, POL-16, REG-02, WAR-15, EVT-098
'''

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
progress = f'''# 進捗ログ

## 2026-04-29T05:52Z 仕様読了完了
- 状態: 開始前チェック実施。
- 自問結果:
  - 能力世界より歴史世界を前面に置く構図で設計する。
  - 食・労働・病・葬りを地方ファイルの必須軸とする。
  - 強い土地の倫理矛盾を国家・宗教・家族・個人へ波及させる。
  - 公式史・民間史・敗者史・異端史を同一事件で意図的に食い違わせる。
  - 固有名詞は命名規則確定前に量産しない。
- 重大判断: 仕様パスの実在不一致を確認し、`copilot-spec/` を正本として採用。
- 現在地: 第1段（骨格確定段階）へ進行。

## 2026-04-29T06:00Z 第1段開始
- 着手宣言: `_meta/` 制御群、命名規則、時代区分、150事件タイトル、12地方骨格、ID初期化を先に固定する。
- 計画:
  1. メタ統制ファイル作成
  2. 言語系統と音韻ルール確定
  3. 時代と年代軸固定
  4. 公式編年のタイトル・年代150件先行確定
  5. 12地方の名称・位置・気候固定
- 想定所要: 長時間。後続調査と肉付けの基準として使用。

## 2026-04-29T06:11Z Phase 0 研究ノート完了
- 状態: Phase 0 完了
- 作成ファイル数: 25
- 検索回数: 40+
- 次の段階: Phase 1（中核世界観）へ進行

## {now} Phase 1+2 完了
- 状態: Phase 1 と Phase 2 を完了。
- 作成/更新:
  - `01_core/` 9件を新規作成
  - `02_history/` 13件を新規作成、2件を全面更新
  - `_meta/` 3件を更新
- 内容要約:
  - 残響理論、暦、禁忌、地理、宇宙観、価値尺度を具体化
  - 150件の公式編年を固有題・年次・関連ID付きで再構築
  - 5件の人工悲劇を公式・民間・敗者・異端で食い違わせた
  - 90残響、18政体、24戦争、記憶地、検閲制度を通底させた
- 次の段階: Phase 3 地方詳細と現代生活記述へ接続可能
'''
manifest = f'''# manifest

## 概況
- 現在段階: Phase 2 完了（中核世界観・歴史層実装済み）
- 更新方針: Phase 完了ごとにファイル数・概算文字数・更新日を更新する。

## 初期登録ファイル
- `_meta/spec_digest.md`
- `_meta/spec_issues.md`
- `_meta/progress.md`
- `_meta/workplan.md`
- `_meta/style_bible.md`
- `_meta/naming_rules.md`
- `_meta/quality_rubric.md`
- `_meta/id_registry.md`
- `_meta/consistency_matrix.md`
- `_meta/search_log.md`
- `_meta/manifest.md`
- `_meta/assumptions.md`
- `02_history/eras.md`
- `02_history/chronicle_official.md`
- `03_present/regions.md`

## Phase 1 コアファイル
- `01_core/premise.md`
- `01_core/geography_overview.md`
- `01_core/cosmology.md`
- `01_core/resonance_theory.md`
- `01_core/core_taboos.md`
- `01_core/calendar_and_timekeeping.md`
- `01_core/measurement_and_value.md`
- `01_core/foundational_terms.md`
- `01_core/seasonality.md`

## Phase 2 履歴ファイル
- `02_history/chronicle_official.md`
- `02_history/chronicle_folk.md`
- `02_history/chronicle_defeated.md`
- `02_history/chronicle_heretical.md`
- `02_history/chronicle_silence.md`
- `02_history/eras.md`
- `02_history/resonance_map.md`
- `02_history/dynasties.md`
- `02_history/wars.md`
- `02_history/historiography.md`
- `02_history/archives_and_censorship.md`
- `02_history/memory_sites.md`
- `02_history/engineered_atrocities.md`

## Phase 0 研究ファイル
- `00_research/R-01_topophilia_and_land_bound_trauma.md`
- `00_research/R-02_collective_memory_theory.md`
- `00_research/R-03_japanese_burial_customs_jomon_to_edo.md`
- `00_research/R-04_chinese_ancestor_rites_and_burial_traditions.md`
- `00_research/R-05_southeast_asian_animist_burial_traditions.md`
- `00_research/R-06_west_african_burial_and_ancestor_veneration.md`
- `00_research/R-07_mesoamerican_and_andean_death_cultures.md`
- `00_research/R-08_european_medieval_burial_customs.md`
- `00_research/R-09_islamic_burial_customs_and_the_dead.md`
- `00_research/R-10_pacific_polynesian_burial_memory_land.md`
- `00_research/R-11_battlefield_commemoration.md`
- `00_research/R-12_massacre_site_handling.md`
- `00_research/R-13_diaspora_and_forced_migration_histories.md`
- `00_research/R-14_nomadic_cultures_and_nonattachment_to_land.md`
- `00_research/R-15_agrarian_land_attachment.md`
- `00_research/R-16_premodern_feudal_social_structures_compared.md`
- `00_research/R-17_nonwestern_premodern_structures.md`
- `00_research/R-18_animism_and_land_spirits_comparison.md`
- `00_research/R-19_war_crimes_historical_narration_truth_reconciliation.md`
- `00_research/R-20_environmental_history_climate_and_culture.md`
- `00_research/R-21_linguistic_typology_and_language_families_overview.md`
- `00_research/R-22_morphological_typology_and_worldbuilding.md`
- `00_research/R-23_fantasy_works_differentiation_study.md`
- `00_research/inspiration_safeguards.md`
- `00_research/fantasy_cliche_rejection_matrix.md`

## カウント（概算）
- 総ファイル数: 62
- 総文字数: 約180000
- 検索回数: 44+
- 最終更新: {now}
'''
consistency = ['# consistency_matrix','','| 系統 | ID | 名称 | 接続 |','|---|---|---|---|']
for eid,name,_,_ in era_data: consistency.append(f'| Era | {eid} | {name} | chronicle / eras / dynasties / wars |')
for rid,(name,_) in regions.items(): consistency.append(f'| Region | {rid} | {name} | geography / chronicle / resonance / memory_sites |')
for pid,data in polities.items(): consistency.append(f"| Polity | {pid} | {data['name']} | dynasties / chronicle / wars / atrocities |")
for wid,data in wars.items(): consistency.append(f"| War | {wid} | {data['name']} | wars / chronicle / folk / defeated |")
for aid,name,evt,res in [('ATR-01','シャンヌ大水没','EVT-058','RES-017'),('ATR-02','グァトル坑夫大封じ','EVT-079','RES-053'),('ATR-03','イライ歌舟焼き','EVT-098','RES-041'),('ATR-04','マサヌ皮剥ぎ移住','EVT-126','RES-049'),('ATR-05','ヌワネ証人溺死','EVT-106','RES-007')]: consistency.append(f'| Atrocity | {aid} | {name} | {evt} / {res} / engineered_atrocities / all chronicles |')
consistency += ['','## 監視項目','- 150事件はすべて固有題・年代・地域・政体を持つ。','- 人工悲劇5件は公式史、民間史、敗者史、異端史、残響地図のすべてに現れる。','- 戦争24件は `wars.md` を主軸に、編年と複数史型で追跡できる。','- 90残響は少なくとも起源事件と地域を一つ以上持つ。','- 非戦闘由来事件は編年の過半を占め、労働・移住・疫病・法制・葬制が継続的に現れる。']

files = {root/'02_history/chronicle_official.md':'\n'.join(official), root/'02_history/chronicle_folk.md':'\n'.join(folk), root/'02_history/chronicle_defeated.md':'\n'.join(defeated), root/'02_history/chronicle_heretical.md':'\n'.join(heretical), root/'02_history/chronicle_silence.md':silence, root/'02_history/eras.md':'\n'.join(eras_md), root/'02_history/resonance_map.md':'\n'.join(res_md), root/'02_history/dynasties.md':'\n'.join(dyn), root/'02_history/wars.md':'\n'.join(wars_md), root/'02_history/historiography.md':historiography, root/'02_history/archives_and_censorship.md':archives, root/'02_history/memory_sites.md':memory_sites, root/'02_history/engineered_atrocities.md':atrocities, root/'_meta/progress.md':progress, root/'_meta/manifest.md':manifest, root/'_meta/consistency_matrix.md':'\n'.join(consistency)}
for path, content in files.items():
    path.write_text(content, encoding='utf-8')
print('OK', len(events), len([x for x in official if x.startswith('### EVT-')]), len([x for x in folk if x.startswith('### ')]), len([x for x in defeated if x.startswith('### ')]), len([x for x in heretical if x.startswith('### ')]), len([x for x in res_md if x.startswith('- RES-')]))
