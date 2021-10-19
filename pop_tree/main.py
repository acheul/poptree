'''
Graphviz must be installed ahead.
This function works on graphviz.Graph

please run
  > from graphviz import Graph 
before execute this fucntion.

If you do not assign a different dataframe, the function will use a default dataframe.
The dataframe assigned must follow a proper format to be organized. 
'''

dft = {'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37}, 'name': {0: '김조부\n(金造釜)', 1: '박씨\n(朴氏)', 2: '김조일\n(金照一)', 3: '이씨\n(李氏)', 4: '김조이\n(金照二)', 5: '김성\n(金姓)', 6: '박소사\n(朴召史)', 7: '김조삼\n(金照三)', 8: '강성\n(康姓)', 9: '김소사\n(金召史)', 10: '김부일\n(金富一)', 11: '김소사\n(金召史)', 12: '김아지\n(金兒只)', 13: '김구일\n(金具一)', 14: '김부이\n(金富二)', 15: '진씨\n(陳氏)', 16: '김부삼\n(金富三)', 17: '박씨\n(朴氏)', 18: '김구이\n(金具二)', 19: '김구삼\n(金具三)', 20: '김부사\n(金富四)', 21: '김부오\n(金富五)', 22: '김부륙\n(金富六)', 23: '박씨\n(朴氏)', 24: '김구성\n(金具晟)', 25: '박주일\n(朴周一)', 26: '유씨\n(柳氏)', 27: '이증일\n(李曾一)', 28: '이조일\n(李藻一)', 29: '강소사\n(姜召史)', 30: '이조이\n(李藻二)', 31: '이주일\n(李珠一)', 32: '소씨\n(蘇氏)', 33: '이소사\n(李召史)', 34: '박참\n(朴參)', 35: '강유의\n(康有爲)', 36: '김사촌\n(金四寸)'}, 'birth_year': {0: 1720.0, 1: 1723.0, 2: 1740.0, 3: 1742.0, 4: 1742.0, 5: 1742.0, 6: 1750.0, 7: 1748.0, 8: 1747.0, 9: 1760.0, 10: 1763.0, 11: 1761.0, 12: nan, 13: 1782.0, 14: 1760.0, 15: 1758.0, 16: 1764.0, 17: 1764.0, 18: 1780.0, 19: 1782.0, 20: 1768.0, 21: 1770.0, 22: 1772.0, 23: 1772.0, 24: 1791.0, 25: 1750.0, 26: 1747.0, 27: 1717.0, 28: 1742.0, 29: 1745.0, 30: 1740.0, 31: 1762.0, 32: 1764.0, 33: 1784.0, 34: 1778.0, 35: 1762.0, 36: 1762.0}, 'sex': {0: 1.0, 1: 2.0, 2: 1.0, 3: 2.0, 4: 1.0, 5: 2.0, 6: 2.0, 7: 1.0, 8: 2.0, 9: 2.0, 10: 1.0, 11: 2.0, 12: nan, 13: 1.0, 14: 1.0, 15: 2.0, 16: 1.0, 17: 2.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 2.0, 24: 1.0, 25: 1.0, 26: 2.0, 27: 1.0, 28: 1.0, 29: 2.0, 30: 1.0, 31: 1.0, 32: 2.0, 33: 2.0, 34: 1.0, 35: 1.0, 36: 1.0}, 'det': {0: '"김조부는 신등면 사람으로, 조선시대 사람이다."', 1: '"박씨는 김조부의 부인으로, 조선시대 사람이다."', 2: '"김조일은 김조부와 박씨의 자로, 조선시대 사람이다."', 3: nan, 4: nan, 5: nan, 6: nan, 7: nan, 8: nan, 9: nan, 10: nan, 11: nan, 12: nan, 13: nan, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan}, 'bold': {0: 1.0, 1: nan, 2: 1.0, 3: nan, 4: nan, 5: nan, 6: nan, 7: 1.0, 8: 1.0, 9: nan, 10: 1.0, 11: nan, 12: nan, 13: 1.0, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: 1.0, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan}, 'xlabel': {0: '1732\\n1735\\n1738', 1: nan, 2: 1774, 3: nan, 4: nan, 5: nan, 6: nan, 7: 1786, 8: '1792\\n1801', 9: nan, 10: '1792\\n1798\\n1801\\n1804\\n1813', 11: nan, 12: nan, 13: '1810\\n1813', 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: '1783\\n1792\\n1801', 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan}, 'fa': {0: nan, 1: nan, 2: 1.0, 3: nan, 4: 1.0, 5: nan, 6: nan, 7: 1.0, 8: nan, 9: 3.0, 10: 3.0, 11: nan, 12: 11.0, 13: 11.0, 14: 5.0, 15: nan, 16: 5.0, 17: nan, 18: 15.0, 19: 15.0, 20: 8.0, 21: 8.0, 22: 8.0, 23: 26.0, 24: 23.0, 25: nan, 26: nan, 27: nan, 28: 28.0, 29: nan, 30: 28.0, 31: 29.0, 32: nan, 33: 32.0, 34: 26.0, 35: nan, 36: nan}, 'hs': {0: nan, 1: 1.0, 2: nan, 3: 3.0, 4: nan, 5: 5.0, 6: 5.0, 7: nan, 8: 8.0, 9: nan, 10: nan, 11: 11.0, 12: nan, 13: nan, 14: nan, 15: 15.0, 16: nan, 17: 17.0, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: 23.0, 24: nan, 25: nan, 26: 26.0, 27: nan, 28: nan, 29: 29.0, 30: nan, 31: nan, 32: 32.0, 33: 20.0, 34: nan, 35: nan, 36: nan}, 'rl01_id': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan, 6: nan, 7: nan, 8: nan, 9: nan, 10: nan, 11: nan, 12: nan, 13: nan, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: 9.0, 36: 15.0}, 'rl01_lab': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan, 6: nan, 7: nan, 8: nan, 9: nan, 10: nan, 11: nan, 12: nan, 13: nan, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: '사촌', 36: '사촌'}, 'rl02_id': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan, 6: nan, 7: nan, 8: nan, 9: nan, 10: nan, 11: nan, 12: nan, 13: nan, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: 32.0}, 'rl02_lab': {0: nan, 1: nan, 2: nan, 3: nan, 4: nan, 5: nan, 6: nan, 7: nan, 8: nan, 9: nan, 10: nan, 11: nan, 12: nan, 13: nan, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: '친구'}}
dft = pd.DataFrame(dft)

def Tree(df=dft, format='svg', graph_name='OnceUponATimeInChosun',
         graph_attr={'pad':'1.4, 1', 'splines':'spline', 'nodesep':'.2', 'ranksep':'1.2', 'ratio':'auto', 'fontname':"NanumSquareRound", 'fontsize':"14pt"},
         node_attr={'fontname':"NanumSquareRound", 'fontsize':"14pt"}, edge_attr={'fontname':"NanumSquareRound", 'fontsize':"14pt"},
         Shape={1:'box', 2:'ellipse', 3:'egg'}, Bold={0:'solid', 1:'bold'},
         use_rllab=True, use_bold=True):
    
    id_list = list(df['id'])
    id2name = dict((i, n) for i, n in zip(df['id'], df.fillna("")['name']))
    id2sex = dict((i, int(n)) if n != "" else (i, 3) for i, n in zip(df['id'], df.fillna("")['sex']))
    id2by = dict((i, int(n)) if n != "" else (i, "") for i, n in zip(df['id'], df.fillna("")['birth_year']))
    id2det = dict((i, n) for i, n in zip(df['id'], df.fillna("")['det']))
    id2bold = dict((i, 1) if n==1 else (i, 0) for i, n in zip(df['id'], df.fillna("")['bold']))
    id2xlab = dict((i, n) for i, n in zip(df['id'], df.fillna("")['xlabel']))
    id2hs = dict((i, int(n)) for i, n in zip(df['id'], df.fillna("")['hs']) if n != "")
    id2fa = dict((i, int(n)) for i, n in zip(df['id'], df.fillna("")['fa']) if n != "")
    id2rl01cp = dict((i, (int(n), lab)) for i, n, lab in zip(df['id'], df.fillna("")['rl01_id'], df.fillna("")['rl01_lab']) if n != "")
    id2rl02cp = dict((i, (int(n), lab)) for i, n, lab in zip(df['id'], df.fillna("")['rl02_id'], df.fillna("")['rl02_lab']) if n != "")

    if use_bold==False:
        Bold={0:'solid', 1:'solid'}
    if use_rllab==False:
        id2rl01cp, id2rl02cp = {}, {}
        id_connected = list(id2hs.keys()) + list(id2hs.values()) + list(id2fa.keys()) + list(id2fa.values())
        id_connected = list(Counter(id_connected))
        id_list = [i for i in id_list if i in id_connected]

    dot = Graph(format=format, name=graph_name, graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr)

    for id in id_list:
        name, sex, by = id2name[id], id2sex[id], id2by[id]
        main_lab = name + "\n" + str(by)
        det = id2det[id] if id2det[id]!="" else main_lab
        bold = id2bold[id]
        xlab = id2xlab[id]
        hs, fa = id2hs.get(id), id2fa.get(id)
        # declare a dot
        dot.node(str(id), label=main_lab, tooltip=det, shape=Shape[sex], xlabel=str(xlab), style=Bold[bold])
        # if with hs
        if hs != None:
            sub1 = Graph(name=f"cluster{id}")
            sub1.attr(style='invis')
            sub2 = Graph()
            sub2.attr(rank="same")
            sub2.edge(str(hs), str(id))
            sub1.subgraph(sub2)
            dot.subgraph(sub1)
        # if with fa
        if fa != None:
            dot.edge(str(fa), str(id))
        # if with rl01, rl02
        rl01cp, rl02cp = id2rl01cp.get(id), id2rl02cp.get(id)
        if rl01cp != None:
            rl, lab = rl01cp
            dot.edge(str(rl), str(id), label=lab, style='dashed')
        if rl02cp != None:
            rl, lab = rl02cp
            dot.edge(str(rl), str(id), label=lab, style='dashed')
    return dot
