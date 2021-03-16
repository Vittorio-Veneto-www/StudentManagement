import random

n = 30
lst = []
lst1 = []
namelst = ['劳元青', '蒲修能', '卓睿博', '石正祥', '终冠玉', '庾宏畅', '莘信鸿', '慕开畅', '贡奇伟', '乔阳云', '雍飞英', '糜浩思', '堵高扬', '莘俊楚', '融翰墨',
 '戈晓旋', '池光文', '曹文茵', '傅寒荷', '通陶宜', '汪路英', '阴子丹', '戌春霞', '王幻波', '龚晓灵', '车津文', '郗雅隽', '莘雨珍', '姚丹洁', '晃晓玉']
schoollist = ['数学科学学院', '物理学院', '化学与分子工程学院', '生命科学学院', '城市与环境学院', '地球与空间科学学院', '信息科学技术学院', '工学院']
classlist = ['高等数学', '线性代数', '力学', '计算概论', '光学', '大学国文', '抽象代数']

for i in range(n):
    x = schoollist[random.randint(0, len(schoollist) - 1)]
    lst.append({'name': namelst[i], 'id': str(random.randint(17, 20)) + '000' + str(random.randint(10000, 99999)),
     'birthym': str(random.randint(1997, 2002)) + (lambda x: '0' + str(x) if x < 10 else str(x))(random.randint(1, 12)),
     'school': x, 'department': x})

import os, json
with open(os.path.join(os.path.dirname(__file__), "infolist.db"), "w") as f:
    json.dump(lst, f, indent=4, separators=(',', ':'))

for i in range(n):
    random.shuffle(classlist)
    for j in range(random.randint(2, 4)):
        lst1.append({'id': lst[i]["id"], 'class': classlist[j], 'score': str(random.randint(50, 100))})

import os, json
with open(os.path.join(os.path.dirname(__file__), "scorelist.db"), "w") as f:
    json.dump(lst1, f, indent=4, separators=(',', ':'))