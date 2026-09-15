#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate HIT 2011 and 2012 graduation list HTML (Light Mode) and CSV.
"""

import re, csv, sys, subprocess
from collections import OrderedDict

# ==============================================================================
# 1. PARSE 2012 DATA (from hit2011_layout.txt)
# ==============================================================================
def parse_2012():
    with open('hit2011_layout.txt', 'r', encoding='utf-8') as f:
        raw = f.read()

    def compact(s):
        return re.sub(r'\s+', '', s)

    def is_name(s):
        c = compact(s)
        return bool(re.fullmatch(r'[\u4e00-\u9fff]{2,4}', c))

    COLLEGES = [
        (r'航\s*天\s*学\s*院',            '航天学院'),
        (r'电\s*子\s*与\s*信\s*息\s*工\s*程\s*学\s*院', '电子与信息工程学院'),
        (r'机\s*电\s*工\s*程\s*学\s*院',  '机电工程学院'),
        (r'材\s*料\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '材料科学与工程学院'),
        (r'能\s*源\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '能源科学与工程学院'),
        (r'电\s*气\s*工\s*程\s*及\s*(其\s*)?自\s*动\s*化\s*学\s*院', '电气工程及自动化学院'),
        (r'理\s*学\s*院',                 '理学院'),
        (r'生\s*命\s*科\s*学\s*与\s*技\s*术\s*学\s*院', '生命科学与技术学院'),
        (r'经\s*济\s*与\s*管\s*理\s*学\s*院', '经济与管理学院'),
        (r'人\s*文\s*与\s*社\s*会\s*科\s*学\s*学\s*院', '人文与社会科学学院'),
        (r'土\s*木\s*工\s*程\s*学\s*院',  '土木工程学院'),
        (r'市\s*政\s*环\s*境\s*工\s*程\s*学\s*院', '市政环境工程学院'),
        (r'建\s*筑\s*学\s*院',            '建筑学院'),
        (r'交\s*通\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '交通科学与工程学院'),
        (r'计\s*算\s*机\s*科\s*学\s*与\s*技\s*术\s*学\s*院', '计算机科学与技术学院'),
        (r'软\s*件\s*学\s*院',            '软件学院'),
        (r'法\s*学\s*院',                 '法学院'),
        (r'外\s*国\s*语\s*学\s*院',       '外国语学院'),
        (r'化\s*工\s*学\s*院',            '化工学院'),
        (r'食\s*品\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '食品科学与工程学院'),
        (r'媒\s*体\s*技\s*术\s*与\s*艺\s*术\s*系', '媒体技术与艺术系'),
        (r'英\s*才\s*学\s*院',            '英才学院'),
        (r'哈\s*尔\s*滨\s*工\s*业\s*大\s*学\s*威\s*海', '哈尔滨工业大学威海校区'),
    ]

    KNOWN_MAJORS = {
        compact(k): v for k, v in [
            ('自动化专业', '自动化专业'),
            ('探测制导与控制技术专业', '探测制导与控制技术专业'),
            ('工程力学专业', '工程力学专业'),
            ('飞行器设计与工程专业', '飞行器设计与工程专业'),
            ('电子科学与技术专业', '电子科学与技术专业'),
            ('电子信息科学与技术专业', '电子信息科学与技术专业'),
            ('复合材料与工程专业', '复合材料与工程专业'),
            ('空间科学与技术专业', '空间科学与技术专业'),
            ('电子信息工程专业', '电子信息工程专业'),
            ('通信工程专业', '通信工程专业'),
            ('信息对抗技术专业', '信息对抗技术专业'),
            ('光学专业', '光学专业'),
            ('光科学与技术专业', '光科学与技术专业'),
            ('机械设计制造及其自动化专业', '机械设计制造及其自动化专业'),
            ('工业工程专业', '工业工程专业'),
            ('飞行器制造工程专业', '飞行器制造工程专业'),
            ('工业设计专业', '工业设计专业'),
            ('材料成型及控制工程专业', '材料成型及控制工程专业'),
            ('材料科学与工程专业', '材料科学与工程专业'),
            ('焊接技术与工程专业', '焊接技术与工程专业'),
            ('材料化学专业', '材料化学专业'),
            ('电子封装技术专业', '电子封装技术专业'),
            ('光信息科学与技术专业', '光信息科学与技术专业'),
            ('软件工程专业', '软件工程专业'),
            ('土木工程专业', '土木工程专业'),
            ('船舶与海洋工程专业', '船舶与海洋工程专业'),
            ('热能与动力工程专业', '热能与动力工程专业'),
            ('核反应堆工程', '核反应堆工程专业'),
            ('飞行器动力工程专业', '飞行器动力工程专业'),
            ('电气工程及其自动化专业', '电气工程及其自动化专业'),
            ('测控技术与仪器专业', '测控技术与仪器专业'),
            ('光电信息工程专业', '光电信息工程专业'),
            ('应用化学专业', '应用化学专业'),
            ('应用物理学专业', '应用物理学专业'),
            ('数学与应用数学专业', '数学与应用数学专业'),
            ('信息与计算科学专业', '信息与计算科学专业'),
            ('核化工与核燃料工程', '核化工与核燃料工程专业'),
            ('核物理', '核物理专业'),
            ('生物技术专业', '生物技术专业'),
            ('生物工程专业', '生物工程专业'),
            ('信息管理与信息系统专业', '信息管理与信息系统专业'),
            ('工商管理专业', '工商管理专业'),
            ('市场营销专业', '市场营销专业'),
            ('会计学专业', '会计学专业'),
            ('金融学专业', '金融学专业'),
            ('国际经济与贸易专业', '国际经济与贸易专业'),
            ('工程管理专业', '工程管理专业'),
            ('财务管理专业', '财务管理专业'),
            ('社会学专业', '社会学专业'),
            ('法学专业', '法学专业'),
            ('英语专业', '英语专业'),
            ('俄语专业', '俄语专业'),
            ('日语专业', '日语专业'),
            ('高分子材料与工程专业', '高分子材料与工程专业'),
            ('化学工程与工艺专业', '化学工程与工艺专业'),
            ('食品科学与工程专业', '食品科学与工程专业'),
            ('广播电视编导专业', '广播电视编导专业'),
            ('广告学专业', '广告学专业'),
            ('建筑学专业', '建筑学专业'),
            ('艺术设计专业', '艺术设计专业'),
            ('城市规划专业', '城市规划专业'),
            ('交通工程专业', '交通工程专业'),
            ('交通运输专业', '交通运输专业'),
            ('道路桥梁与渡河工程专业', '道路桥梁与渡河工程专业'),
            ('给水排水工程专业', '给水排水工程专业'),
            ('环境工程专业', '环境工程专业'),
            ('环境科学专业', '环境科学专业'),
            ('建筑环境与设备工程专业', '建筑环境与设备工程专业'),
            ('理论与应用力学专业', '理论与应用力学专业'),
            ('计算机科学与技术专业', '计算机科学与技术专业'),
            ('生物信息技术专业', '生物信息技术专业'),
            ('信息安全专业', '信息安全专业'),
            ('汉语言文学专业', '汉语言文学专业'),
            ('车辆工程专业', '车辆工程专业'),
            ('给排水科学与工程专业', '给排水科学与工程专业'),
        ]
    }

    def try_college(c):
        for pat, name in COLLEGES:
            if re.search(pat, c):
                return name
        return None

    def try_major(c):
        if c in KNOWN_MAJORS:
            return KNOWN_MAJORS[c]
        if c.endswith('专业') and len(c) <= 15:
            return c
        if re.fullmatch(r'[\u4e00-\u9fff]{4,12}工\s*程', c):
            return c + '专业'
        return None

    records = []
    current_college = '航天学院'
    current_major = ''

    JUNK = re.compile(
        r'^\s*(?:[１２０-９]{4,}|哈\s*尔\s*滨\s*工\s*业\s*大\s*学\s*年\s*鉴|毕\s*业\s*生\s*及\s*出\s*站\s*博\s*士\s*后|普\s*通\s*本|[Ｚ＼，＾Ｙ＂＇]{1}|[￣—=＝]{2,}|\s*\f\s*)\s*$',
        re.MULTILINE
    )

    lines = raw.split('\n')
    for line in lines:
        c = compact(line)
        if not c or JUNK.match(line):
            continue
        if re.search(r'[Ｚ＼＾Ｙ]', line) or re.search(r'[￣—]{2,}', line) or re.search(r'２０１２', c):
            continue
        col = try_college(c)
        if col:
            current_college = col
            continue
        if len(c) <= 18:
            maj = try_major(c)
            if maj:
                current_major = maj
                continue
        if not current_major:
            continue
        parts = re.split(r'[ \t]{2,}', line)
        for part in parts:
            pc = compact(part)
            if is_name(pc):
                if pc in {'专业', '学院', '毕业', '出站', '博士', '普通', '名单', '年鉴', '哈尔', '滨工', '大学', '及出', '站博', '士后', '本专', '科毕', '工程', '技术', '科学'}:
                    continue
                records.append({'college': current_college, 'major': current_major, 'name': pc})

    seen = set()
    unique = []
    for r in records:
        key = (r['college'], r['major'], r['name'])
        if key not in seen:
            seen.add(key)
            unique.append(r)
    return unique

# ==============================================================================
# 2. PARSE 2011 DATA (from 哈尔滨工业大学年鉴_谢大纲_主编_普通本、专科毕业生名单.pdf)
# ==============================================================================
def parse_2011():
    xml_str = subprocess.run(['pdftotext', '-bbox', '哈尔滨工业大学年鉴_谢大纲_主编_普通本、专科毕业生名单.pdf', '-'], capture_output=True, text=True).stdout
    pages_xml = xml_str.split('<page ')[1:]

    COLLEGES = [
        (re.compile(r'哈\s*尔\s*滨\s*工\s*业\s*大\s*学\s*[（(]?\s*威\s*海'), '哈尔滨工业大学威海校区'),
        (re.compile(r'计\s*算\s*机\s*科\s*学\s*与\s*技\s*术\s*学\s*院'), '计算机科学与技术学院'),
        (re.compile(r'电\s*气\s*工\s*程\s*及\s*(其\s*)?自\s*动\s*化\s*学\s*院'), '电气工程及自动化学院'),
        (re.compile(r'材\s*料\s*科\s*学\s*与\s*工\s*程\s*学\s*院'), '材料科学与工程学院'),
        (re.compile(r'交\s*通\s*科\s*学\s*与\s*工\s*程\s*学\s*院'), '交通科学与工程学院'),
        (re.compile(r'电\s*子\s*与\s*信\s*息\s*工\s*程\s*学\s*院'), '电子与信息工程学院'),
        (re.compile(r'食\s*品\s*科\s*学\s*与\s*工\s*程\s*学\s*院'), '食品科学与工程学院'),
        (re.compile(r'能\s*源\s*科\s*学\s*与\s*工\s*程\s*学\s*院'), '能源科学与工程学院'),
        (re.compile(r'人\s*文\s*与\s*社\s*会\s*科\s*学\s*学\s*院'), '人文与社会科学学院'),
        (re.compile(r'市\s*政\s*环\s*境\s*工\s*程\s*学\s*院'), '市政环境工程学院'),
        (re.compile(r'经\s*济\s*与\s*管\s*理\s*学\s*院'), '经济与管理学院'),
        (re.compile(r'机\s*电\s*工\s*程\s*学\s*院'), '机电工程学院'),
        (re.compile(r'土\s*木\s*工\s*程\s*学\s*院'), '土木工程学院'),
        (re.compile(r'汽\s*车\s*工\s*程\s*学\s*院'), '汽车工程学院'),
        (re.compile(r'媒\s*体\s*技\s*术\s*与\s*艺\s*术\s*系'), '媒体技术与艺术系'),
        (re.compile(r'外\s*国\s*语\s*学\s*院'), '外国语学院'),
        (re.compile(r'航\s*天\s*学\s*院'), '航天学院'),
        (re.compile(r'软\s*件\s*学\s*院'), '软件学院'),
        (re.compile(r'建\s*筑\s*学\s*院'), '建筑学院'),
        (re.compile(r'化\s*工\s*学\s*院'), '化工学院'),
        (re.compile(r'实\s*验\s*学\s*院'), '实验学院'),
        (re.compile(r'理\s*学\s*院'), '理学院'),
        (re.compile(r'法\s*学\s*院'), '法学院'),
    ]

    MAJOR_FIXES = {
        '自 动化专业': '自动化专业',
        '自 动 化 专业': '自动化专业',
        '自动化专业': '自动化专业',
        '探测制导与控制技术专业、': '探测制导与控制技术专业',
        '探测制导与控制技术专业': '探测制导与控制技术专业',
        '工程力学专业': '工程力学专业',
        '工程 力 学专 业': '工程力学专业',
        '飞行器设计与工程专业': '飞行器设计与工程专业',
        '飞 行 器设 计 与 工 程专业': '飞行器设计与工程专业',
        '电子科学与技术专业': '电子科学与技术专业',
        '电子信息科学与技术专业': '电子信息科学与技术专业',
        '复合材料与工程专业': '复合材料与工程专业',
        '空间科学与技术专业': '空间科学与技术专业',
        '电子信息工程专业': '电子信息工程专业',
        '通信工程专业': '通信工程专业',
        '信息对抗技术专业': '信息对抗技术专业',
        '遥感科学与技术': '遥感科学与技术专业',
        '机械设计制造及其自动化专业': '机械设计制造及其自动化专业',
        '机械设计制造及其自 动化专业': '机械设计制造及其自动化专业',
        '工业设计专业': '工业设计专业',
        '飞行器制造工程专业': '飞行器制造工程专业',
        '工业工程专业': '工业工程专业',
        '材料成型及控制工程专业': '材料成型及控制工程专业',
        '材料科学与工程专业': '材料科学与工程专业',
        '焊接技术与工程专业': '焊接技术与工程专业',
        '材料物理专业': '材料物理专业',
        '热能与动力工程专业': '热能与动力工程专业',
        '飞行器动力工程专业': '飞行器动力工程专业',
        '核反应堆工程': '核反应堆工程专业',
        '车辆工程': '车辆工程专业',
        '车辆工程专业': '车辆工程专业',
        '电气工程及其自动化专业': '电气工程及其自动化专业',
        '测控技术与仪器专业': '测控技术与仪器专业',
        '光电信息工程专业': '光电信息工程专业',
        '应用化学专业': '应用化学专业',
        '材料化学专业': '材料化学专业',
        '应用物理学专业': '应用物理学专业',
        '数学与应用数学专业': '数学与应用数学专业',
        '信息与计算科学专业': '信息与计算科学专业',
        '生物技术专业': '生物技术专业',
        '生物工程专业': '生物工程专业',
        '光信息科学与技术专业': '光信息科学与技术专业',
        '核化工与核燃料专业': '核化工与核燃料工程专业',
        '核物理': '核物理专业',
        '信息管理与信息系统专业': '信息管理与信息系统专业',
        '信 息 管 理 与 信息 系 统 专 业': '信息管理与信息系统专业',
        '工商管理专业': '工商管理专业',
        '市场营销专业': '市场营销专业',
        '市场营销 专业': '市场营销专业',
        '会计学专业': '会计学专业',
        '金融学专业': '金融学专业',
        '国际经济与贸易专业': '国际经济与贸易专业',
        '工程管理专业': '工程管理专业',
        '财务管理专业': '财务管理专业',
        '社会学专业': '社会学专业',
        '土木工程专业、': '土木工程专业',
        '土木工程专业': '土木工程专业',
        '理论与应用力学专业': '理论与应用力学专业',
        '给水排水工程专业': '给水排水工程专业',
        '环境工程专业': '环境工程专业',
        '环境科学专业': '环境科学专业',
        '建筑环境与设备工程专业': '建筑环境与设备工程专业',
        '建筑学专业': '建筑学专业',
        '艺术设计专业': '艺术设计专业',
        '城市规划专业': '城市规划专业',
        '交通工程专业': '交通工程专业',
        '交通运输专业': '交通运输专业',
        '道路桥梁与渡河工程专业': '道路桥梁与渡河工程专业',
        '计算机科学与技术专业': '计算机科学与技术专业',
        '生物信息技术专业': '生物信息技术专业',
        '信息安全专业': '信息安全专业',
        '软件工程专业': '软件工程专业',
        '法学专业': '法学专业',
        '英语专业': '英语专业',
        '俄语专业': '俄语专业',
        '曰语专业': '日语专业',
        '日语专业': '日语专业',
        '高分子材料与工程专业': '高分子材料与工程专业',
        '化学工程与工艺专业': '化学工程与工艺专业',
        '食品科学与工程专业': '食品科学与工程专业',
        '广播电视编导专业': '广播电视编导专业',
        '广告学专业': '广告学专业',
        '给排水科学与工程专业': '给排水科学与工程专业',
        '遥感科学与技术专业': '遥感科学与技术专业',
        '电子ｋ装技术专业': '电子封装技术专业',
        '电子封装技术专业': '电子封装技术专业',
        '电子封装技术': '电子封装技术专业',
        '飞行器设十与工程专业': '飞行器设计与工程专业',
        '电子科学与按术专业': '电子科学与技术专业',
        '计算■学与技术专业': '计算机科学与技术专业',
        '信息管理与信息统专业': '信息管理与信息系统专业',
        '化学工程与工艺ｔｔ': '化学工程与工艺专业',
        '生物街龙专业': '生物技术专业',
        '光信息科学与Ｍ专业': '光信息科学与技术专业',
        '汉语主文学专业': '汉语言文学专业',
        '汉语Ｑ文学专业': '汉语言文学专业',
        '土木工专业': '土木工程专业',
        '船 舶 与 洋 工 群 业': '船舶与海洋工程专业',
        '船舶与海洋工程专业': '船舶与海洋工程专业',
    }

    KNOWN_MAJOR_MAP = {re.sub(r'\s+', '', k): v for k, v in MAJOR_FIXES.items()}

    def try_major(s):
        c = re.sub(r'[\s、，,]+', '', s)
        if c in KNOWN_MAJOR_MAP:
            return KNOWN_MAJOR_MAP[c]
        if c.endswith('专业') and len(c) <= 15:
            return c
        return None

    def try_college(s):
        c = re.sub(r'\s+', '', s)
        for pat, name in COLLEGES:
            if pat.search(c):
                return name
        return None

    def clean_student_name(n):
        n = re.sub(r'[？\?]+', '·', n)
        n = re.sub(r'^[·\s、，,\._\-—]+|[·\s、，,\._\-—]+$', '', n)
        if n in ('夏·Ｌ祥宁', '夏Ｌ祥宁', '夏祥宁'):
            return '夏祥宁'
        if n == '朱１鸣':
            return '朱一鸣'
        if n == '陶宇Ｉｔ':
            return '陶宇'
        if n == '赵更一顾明':
            return ['赵更一', '顾明']
        if n == '张杰一张兴权':
            return ['张杰一', '张兴权']
        if n == '陈一哲':
            return '陈一哲'
        if n == '吴一鹏':
            return '吴一鹏'
        if n == '李国一':
            return '李国一'
        if '木合塔依' in n and '申丽辉' in n:
            return ['塔依尔江·木合塔依', '申丽辉']
        if n == 'ｉ楠':
            return '宋楠'
        return n

    def extract_names_from_line(words):
        chunks = []
        curr = [words[0]]
        for w in words[1:]:
            gap = w[0] - curr[-1][1]
            if gap < 8:
                curr.append(w)
            else:
                chunks.append(''.join(x[2] for x in curr))
                curr = [w]
        if curr:
            chunks.append(''.join(x[2] for x in curr))
        
        names = []
        i = 0
        while i < len(chunks):
            c = chunks[i]
            c_clean = re.sub(r'^[？\?、，, \._\-—\ue5cf\ue5d2]+|[？\?、，, \._\-—\ue5cf\ue5d2]+$', '', c)
            if not c_clean:
                i += 1
                continue
            if len(c_clean) == 1 and '\u4e00' <= c_clean <= '\u9fff':
                if i + 1 < len(chunks):
                    next_c = re.sub(r'^[？\?、，, \._\-—\ue5cf\ue5d2]+|[？\?、，, \._\-—\ue5cf\ue5d2]+$', '', chunks[i+1])
                    if len(next_c) == 1 and '\u4e00' <= next_c <= '\u9fff':
                        names.append(c_clean + next_c)
                        i += 2
                        continue
            names.append(c_clean)
            i += 1
        return names

    records = []
    cur_col = '航天学院'
    cur_maj = ''

    for p_idx, p_xml in enumerate(pages_xml, 1):
        words = re.findall(r'<word xMin=\"([^\"]+)\" yMin=\"([^\"]+)\" xMax=\"([^\"]+)\" yMax=\"([^\"]+)\">([^<]+)</word>', p_xml)
        parsed = []
        for x1, y1, x2, y2, t in words:
            t = re.sub(r'[\ue000-\uf8ff\ufeff]', ' ', t).strip()
            if t:
                parsed.append((float(x1), float(y1), float(x2), float(y2), t))
        lines = []
        for x1, y1, x2, y2, t in parsed:
            placed = False
            for line in lines:
                if abs(line['y'] - y1) < 4.5:
                    line['words'].append((x1, x2, t))
                    line['y'] = (line['y'] + y1) / 2
                    placed = True
                    break
            if not placed:
                lines.append({'y': y1, 'words': [(x1, x2, t)]})
        lines.sort(key=lambda l: l['y'])
        valid = [l for l in lines if 55 < l['y'] < 670]
        
        for l in valid:
            if p_idx == 29 and l['y'] > 330:
                continue
            # Overrides for bottom 3 rows on page 26
            if p_idx == 26 and l['y'] > 620:
                continue

            l['words'].sort(key=lambda w: w[0])
            raw_text = ' '.join(w[2] for w in l['words'])
            compact_text = re.sub(r'\s+', '', raw_text)
            
            if any(k in compact_text for k in ['哈尔滨工业大学年鉴', '毕业生及出站博士后', '普通本、专科毕业生名单', '普通本专科毕业生名单', '授予硕士学位']):
                continue
            
            col = try_college(compact_text)
            if col:
                cur_col = col
                continue
                
            maj = try_major(compact_text)
            if maj:
                cur_maj = maj
                continue
                
            if not cur_maj:
                continue
                
            names = extract_names_from_line(l['words'])
            for n in names:
                fixed = clean_student_name(n)
                if isinstance(fixed, list):
                    for fn in fixed:
                        records.append({'college': cur_col, 'major': cur_maj, 'name': fn})
                else:
                    if not fixed or fixed in ['专业', '学院', '名单', '、', '．', '■', '｜', '＿', '（', '）', 'Ｑ', 'ｉ']:
                        continue
                    records.append({'college': cur_col, 'major': cur_maj, 'name': fixed})

        if p_idx == 26:
            # Verified rows 1, 2, 3 on page 26 from original scanned document image
            p26_verified = [
                '刘栋', '刘佳龙', '刘阳', '罗艳路', '蒲琳娜', '石好', '孙顺', '滕晓旭', '王斌腾',
                '王洪彩', '王晓倩', '杨林', '袁晓宝', '张娇龙', '赵峥', '郑侠', '祝艳龙', '白鸿叶',
                '岑鹏', '陈淑一', '崔莹', '付珂玮', '何魁', '贾方娜', '江旭', '雷杰', '李维'
            ]
            for name in p26_verified:
                records.append({'college': '哈尔滨工业大学威海校区', 'major': '化学工程与工艺专业', 'name': name})

    seen = set()
    unique = []
    for r in records:
        k = (r['college'], r['major'], r['name'])
        if k not in seen:
            seen.add(k)
            unique.append(r)
    return unique

# ==============================================================================
# 3. HTML BUILDER (LIGHT MODE)
# ==============================================================================
def generate_html(year, records, source_book, csv_filename):
    total = len(records)
    college_data = OrderedDict()
    for r in records:
        c, m = r['college'], r['major']
        college_data.setdefault(c, OrderedDict()).setdefault(m, []).append(r['name'])

    n_colleges = len(college_data)
    n_majors = sum(len(m) for m in college_data.values())
    college_counts = {c: sum(len(v) for v in ms.values()) for c, ms in college_data.items()}

    college_opts = '\n'.join(
        f'      <option value="{c}">{c}（{college_counts[c]}人）</option>'
        for c in college_data
    )

    icons = ['🏛','🔬','⚡','🛸','🔧','📡','🌊','🏗','🚀','💻',
             '📐','🧬','📊','🌿','🎓','⚗','🍎','📺','🔭','🎨','🚗','🌐']
    
    card_html = ''
    for idx, (college, majors) in enumerate(college_data.items()):
        icon = icons[idx % len(icons)]
        cnt  = college_counts[college]
        card_html += f'  <section class="college-section" data-college="{college}">\n'
        card_html += f'    <div class="college-header"><div class="college-icon">{icon}</div><div class="college-name">{college}</div><div class="college-count">{cnt} 人</div></div>\n'
        for major, names in majors.items():
            card_html += f'    <div class="major-block" data-major="{major}">\n'
            card_html += f'      <div class="major-header" onclick="toggleMajor(this.parentElement)"><span class="major-title">{major}</span><span class="major-badge">{len(names)} 人</span><span class="major-toggle">▼</span></div>\n'
            card_html += '      <div class="names-grid">\n'
            for name in names:
                card_html += f'        <div class="name-chip" data-name="{name}">{name}</div>\n'
            card_html += '      </div>\n    </div>\n'
        card_html += '  </section>\n'

    table_rows = ''
    for idx, r in enumerate(records, 1):
        table_rows += (f'        <tr data-college="{r["college"]}" data-major="{r["major"]}" data-name="{r["name"]}">'
                       f'<td>{idx}</td><td class="td-college">{r["college"]}</td>'
                       f'<td class="td-major">{r["major"]}</td><td>{r["name"]}</td></tr>\n')

    # Note the Hugo front matter at top to ensure Hugo never evaluates .Summary on large files
    front_matter = f'''---
title: "{year}年哈尔滨工业大学普通本、专科毕业生名单"
description: "{year}年哈尔滨工业大学普通本科及专科毕业生完整名单，共{total}人，按学院和专业分类。"
summary: "{year}年哈尔滨工业大学普通本科及专科毕业生完整名单，共{total}人，按学院和专业分类。"
---
'''

    content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{year}年哈尔滨工业大学普通本、专科毕业生名单</title>
<meta name="description" content="{year}年哈尔滨工业大学普通本科及专科毕业生完整名单，共{total}人，按学院和专业分类。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #f8fafc;
  --bg-card: #ffffff;
  --bg-card2: #f1f5f9;
  --primary: #003366;
  --primary-light: #0d4a82;
  --primary-subtle: #e8eff7;
  --gold: #b38226;
  --gold-light: #d4a347;
  --gold-dim: rgba(179, 130, 38, 0.12);
  --text: #1e293b;
  --text-muted: #64748b;
  --dim: #94a3b8;
  --border: rgba(0, 51, 102, 0.15);
  --border-dim: rgba(0, 0, 0, 0.08);
  --radius: 10px;
  --shadow: 0 2px 10px rgba(0, 51, 102, 0.04);
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Noto Serif SC', 'PingFang SC', sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.6;
}}

/* HERO */
.hero {{
  background: linear-gradient(135deg, #ffffff 0%, #f0f5fa 60%, #e6eff8 100%);
  border-bottom: 1px solid var(--border);
  padding: 56px 24px 44px;
  text-align: center;
  position: relative;
  overflow: hidden;
}}
.hero::before {{
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 70% 50% at 50% 0%, rgba(0, 51, 102, 0.05), transparent 70%);
  pointer-events: none;
}}
.badge {{
  display: inline-block;
  background: var(--primary-subtle);
  border: 1px solid rgba(0, 51, 102, 0.2);
  color: var(--primary);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 1.5px;
  padding: 5px 16px;
  border-radius: 999px;
  margin-bottom: 20px;
}}
.hero h1 {{
  font-family: 'Noto Serif SC', 'Songti SC', serif;
  font-size: clamp(22px, 4vw, 34px);
  font-weight: 700;
  color: #003366;
  letter-spacing: 1.5px;
  margin-bottom: 10px;
}}
.hero-sub {{
  color: var(--text-muted);
  font-size: 13.5px;
  margin-bottom: 30px;
}}
.stats {{
  display: flex;
  justify-content: center;
  gap: 40px;
  flex-wrap: wrap;
}}
.stat-num {{
  font-size: 32px;
  font-weight: 700;
  color: var(--primary);
  line-height: 1;
}}
.stat-label {{
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 5px;
  letter-spacing: 0.5px;
}}

/* CONTROLS */
.controls {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-dim);
  padding: 12px 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
}}
.ctrl {{
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
}}
.sw {{
  flex: 1;
  min-width: 200px;
  position: relative;
}}
.sw svg {{
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--dim);
  pointer-events: none;
}}
#search {{
  width: 100%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  color: var(--text);
  font-size: 14px;
  padding: 9px 12px 9px 36px;
  outline: none;
  transition: all .2s;
}}
#search:focus {{
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(0, 51, 102, 0.1);
}}
#search::placeholder {{
  color: var(--dim);
}}
select {{
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  color: var(--text);
  font-size: 13.5px;
  padding: 9px 12px;
  outline: none;
  cursor: pointer;
  min-width: 150px;
  transition: border .2s;
}}
select:focus {{
  border-color: var(--primary);
}}
.rc {{
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
}}
.rc span {{
  color: var(--primary);
  font-weight: 700;
}}
.vt {{
  display: flex;
  gap: 2px;
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 3px;
}}
.vb {{
  background: none;
  border: none;
  color: var(--text-muted);
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all .2s;
}}
.vb.active {{
  background: #ffffff;
  color: var(--primary);
  font-weight: 700;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}}
.btn-dl {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  color: var(--text);
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  text-decoration: none;
  font-weight: 500;
  transition: all .2s;
}}
.btn-dl:hover {{
  background: var(--primary-subtle);
  border-color: var(--primary);
  color: var(--primary);
}}

/* MAIN */
.main {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 24px 80px;
}}

/* COLLEGE */
.college-section {{
  margin-bottom: 44px;
}}
.college-header {{
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--primary-subtle);
}}
.college-icon {{
  width: 38px;
  height: 38px;
  background: var(--primary-subtle);
  border: 1px solid rgba(0, 51, 102, 0.15);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 17px;
  flex-shrink: 0;
}}
.college-name {{
  font-family: 'Noto Serif SC', serif;
  font-size: 19px;
  font-weight: 700;
  color: var(--primary);
  flex: 1;
}}
.college-count {{
  font-size: 12.5px;
  color: var(--text-muted);
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 3px 10px;
  white-space: nowrap;
}}

/* MAJOR */
.major-block {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius);
  margin-bottom: 12px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: border .2s;
}}
.major-block:hover {{
  border-color: #cbd5e1;
}}
.major-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 18px;
  background: #f8fafc;
  cursor: pointer;
  user-select: none;
  gap: 10px;
  border-bottom: 1px solid transparent;
}}
.major-block:not(.collapsed) .major-header {{
  border-bottom-color: #f1f5f9;
}}
.major-title {{
  font-size: 14.5px;
  font-weight: 600;
  color: #1e293b;
  flex: 1;
}}
.major-badge {{
  font-size: 12px;
  color: var(--primary);
  background: var(--primary-subtle);
  border-radius: 999px;
  padding: 2px 10px;
  white-space: nowrap;
  font-weight: 600;
}}
.major-toggle {{
  color: var(--dim);
  font-size: 11px;
  transition: transform .25s ease;
}}
.major-block.collapsed .major-toggle {{
  transform: rotate(-90deg);
}}
.names-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(72px, 1fr));
  gap: 8px;
  padding: 14px 18px 18px;
}}
.major-block.collapsed .names-grid {{
  display: none;
}}
.name-chip {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 7px;
  padding: 7px 4px;
  text-align: center;
  font-family: 'Noto Serif SC', serif;
  font-size: 14px;
  color: #1e293b;
  cursor: default;
  transition: all .15s;
  white-space: nowrap;
}}
.name-chip:hover {{
  background: var(--primary-subtle);
  border-color: var(--primary);
  color: var(--primary);
}}
.name-chip.hl {{
  background: #fef3c7;
  border-color: #f59e0b;
  color: #92400e;
  font-weight: 600;
  animation: pop .3s ease;
}}
@keyframes pop {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.08); }} }}

/* TABLE */
.table-wrap {{
  overflow-x: auto;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}}
table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}}
thead th {{
  background: #f8fafc;
  color: #475569;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 0.5px;
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
  position: sticky;
  top: 0;
}}
tbody tr {{
  border-bottom: 1px solid #f1f5f9;
  transition: background .15s;
}}
tbody tr:hover {{
  background: #f8fafc;
}}
tbody tr:last-child {{
  border-bottom: none;
}}
td {{
  padding: 10px 16px;
  color: #334155;
}}
td:first-child {{
  color: var(--dim);
  font-size: 12.5px;
  width: 65px;
}}
td:last-child {{
  font-family: 'Noto Serif SC', serif;
  font-size: 14.5px;
  font-weight: 500;
  color: #0f172a;
}}
.td-college {{
  color: var(--primary);
  font-size: 13.5px;
  font-weight: 500;
}}
.td-major {{
  color: var(--text-muted);
  font-size: 13.5px;
}}

.hidden {{ display: none !important; }}
footer {{
  text-align: center;
  padding: 32px 24px;
  color: var(--dim);
  font-size: 12.5px;
  border-top: 1px solid var(--border-dim);
  background: #ffffff;
}}

@media(max-width:600px) {{
  .hero {{ padding: 36px 16px 28px; }}
  .stats {{ gap: 20px; }}
  .main {{ padding: 18px 12px 60px; }}
  .names-grid {{ grid-template-columns: repeat(auto-fill, minmax(62px, 1fr)); gap: 6px; }}
}}
</style>
</head>
<body>

<section class="hero">
  <div class="badge">哈尔滨工业大学 · {year}届</div>
  <h1>普通本、专科毕业生名单</h1>
  <p class="hero-sub">{source_book} · 本科及专科毕业生名录</p>
  <div class="stats">
    <div class="stat"><div class="stat-num" id="total-count">{total}</div><div class="stat-label">毕业生总数</div></div>
    <div class="stat"><div class="stat-num">{n_colleges}</div><div class="stat-label">学院数</div></div>
    <div class="stat"><div class="stat-num">{n_majors}</div><div class="stat-label">专业数</div></div>
  </div>
</section>

<div class="controls">
  <div class="ctrl">
    <div class="sw">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <input type="search" id="search" placeholder="搜索姓名、专业或学院…" autocomplete="off">
    </div>
    <select id="college-filter">
      <option value="">全部学院</option>
{college_opts}
    </select>
    <div class="vt">
      <button class="vb active" id="btn-card" onclick="setView('card')">卡片</button>
      <button class="vb" id="btn-table" onclick="setView('table')">列表</button>
    </div>
    <a class="btn-dl" href="{csv_filename}" download>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      下载 CSV
    </a>
    <div class="rc">显示 <span id="shown-count">0</span> 人</div>
  </div>
</div>

<main class="main">
<div id="card-view">
{card_html}</div>

<div id="table-view" class="hidden">
  <div class="table-wrap"><table>
    <thead><tr><th>序号</th><th>学院</th><th>专业</th><th>姓名</th></tr></thead>
    <tbody id="tb">
{table_rows}    </tbody>
  </table></div>
</div>
</main>

<footer>{year}年哈尔滨工业大学普通本、专科毕业生名单 &nbsp;|&nbsp; 数据来源：{source_book}</footer>

<script>
let VIEW = 'card';
function setView(v) {{
  VIEW = v;
  document.getElementById('card-view').classList.toggle('hidden', v !== 'card');
  document.getElementById('table-view').classList.toggle('hidden', v !== 'table');
  document.getElementById('btn-card').classList.toggle('active', v === 'card');
  document.getElementById('btn-table').classList.toggle('active', v === 'table');
  updateCount();
}}
function toggleMajor(b) {{
  b.classList.toggle('collapsed');
}}
function updateCount() {{
  let n = 0;
  if (VIEW === 'card') {{
    document.querySelectorAll('.nc:not(.hidden)').forEach(() => n++);
  }} else {{
    document.querySelectorAll('#tb tr:not(.hidden)').forEach(() => n++);
  }}
  document.getElementById('shown-count').textContent = n;
}}
function applyFilters() {{
  const q = document.getElementById('search').value.trim();
  const cf = document.getElementById('college-filter').value;
  document.querySelectorAll('.college-section').forEach(sec => {{
    const col = sec.dataset.college;
    if (cf && col !== cf) {{
      sec.classList.add('hidden');
      return;
    }}
    sec.classList.remove('hidden');
    let secVisible = false;
    sec.querySelectorAll('.major-block').forEach(blk => {{
      const maj = blk.dataset.major;
      let blkVisible = false;
      blk.querySelectorAll('.name-chip').forEach(chip => {{
        const nm = chip.dataset.name;
        const ok = !q || (nm.includes(q) || maj.includes(q) || col.includes(q));
        chip.classList.toggle('hidden', !ok);
        chip.classList.toggle('hl', !!q && nm.includes(q));
        if (ok) blkVisible = true;
      }});
      blk.classList.toggle('hidden', !blkVisible);
      if (blkVisible) {{
        blk.classList.remove('collapsed');
        secVisible = true;
      }}
    }});
    sec.classList.toggle('hidden', !secVisible);
  }});
  document.querySelectorAll('#tb tr').forEach(tr => {{
    const ok = (!cf || tr.dataset.college === cf) &&
               (!q || (tr.dataset.name.includes(q) || tr.dataset.major.includes(q) || tr.dataset.college.includes(q)));
    tr.classList.toggle('hidden', !ok);
  }});
  updateCount();
}}
document.getElementById('search').addEventListener('input', applyFilters);
document.getElementById('college-filter').addEventListener('change', applyFilters);
updateCount();
</script>
</body>
</html>'''

    return front_matter + content

# ==============================================================================
# MAIN DRIVER
# ==============================================================================
def main():
    print("Parsing 2012 data...")
    records_2012 = parse_2012()
    print(f"2012 total unique: {len(records_2012)}")

    csv_2012_path = '2012年哈尔滨工业大学普通本、专科毕业生名单.csv'
    with open(csv_2012_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['序号', '学院', '专业', '姓名'])
        w.writeheader()
        for idx, r in enumerate(records_2012, 1):
            w.writerow({'序号': idx, '学院': r['college'], '专业': r['major'], '姓名': r['name']})
    print(f"Wrote {csv_2012_path}")

    html_2012 = generate_html('2012', records_2012, '《哈尔滨工业大学年鉴 2012》', '2012年哈尔滨工业大学普通本、专科毕业生名单.csv')
    html_2012_path = '2012年哈尔滨工业大学普通本、专科毕业生名单.html'
    with open(html_2012_path, 'w', encoding='utf-8') as f:
        f.write(html_2012)
    print(f"Wrote {html_2012_path}")

    print("\nParsing 2011 data...")
    records_2011 = parse_2011()
    print(f"2011 total unique: {len(records_2011)}")

    csv_2011_path = '2011年哈尔滨工业大学普通本、专科毕业生名单.csv'
    with open(csv_2011_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['序号', '学院', '专业', '姓名'])
        w.writeheader()
        for idx, r in enumerate(records_2011, 1):
            w.writerow({'序号': idx, '学院': r['college'], '专业': r['major'], '姓名': r['name']})
    print(f"Wrote {csv_2011_path}")

    html_2011 = generate_html('2011', records_2011, '《哈尔滨工业大学年鉴》谢大纲 主编', '2011年哈尔滨工业大学普通本、专科毕业生名单.csv')
    html_2011_path = '2011年哈尔滨工业大学普通本、专科毕业生名单.html'
    with open(html_2011_path, 'w', encoding='utf-8') as f:
        f.write(html_2011)
    print(f"Wrote {html_2011_path}")

    print("\nAll files successfully generated!")

if __name__ == '__main__':
    main()
