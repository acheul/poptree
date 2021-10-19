'''
Graphviz must be installed ahead.
This function works on graphviz.Graph

please run
  > from graphviz import Graph 
before execute this fucntion.

If you do not assign a different dataframe, the function will use a default dataframe.
The dataframe assigned must follow a proper format to be organized. 
'''

import pandas as pd
dft = {'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], 'name': ['김조부\n(金造釜)', '박씨\n(朴氏)', '김조일\n(金照一)', '이씨\n(李氏)', '김조이\n(金照二)', '김성\n(金姓)', '박소사\n(朴召史)', '김조삼\n(金照三)', '강성\n(康姓)', '김소사\n(金召史)', '김부일\n(金富一)', '김소사\n(金召史)', '김아지\n(金兒只)', '김구일\n(金具一)', '김부이\n(金富二)', '진씨\n(陳氏)', '김부삼\n(金富三)', '박씨\n(朴氏)', '김구이\n(金具二)', '김구삼\n(金具三)', '김부사\n(金富四)', '김부오\n(金富五)', '김부륙\n(金富六)', '박씨\n(朴氏)', '김구성\n(金具晟)', '박주일\n(朴周一)', '유씨\n(柳氏)', '이증일\n(李曾一)', '이조일\n(李藻一)', '강소사\n(姜召史)', '이조이\n(李藻二)', '이주일\n(李珠一)', '소씨\n(蘇氏)', '이소사\n(李召史)', '박참\n(朴參)', '강유의\n(康有爲)', '김사촌\n(金四寸)'], 'birth_year': [1720.0, 1723.0, 1740.0, 1742.0, 1742.0, 1742.0, 1750.0, 1748.0, 1747.0, 1760.0, 1763.0, 1761.0, nan, 1782.0, 1760.0, 1758.0, 1764.0, 1764.0, 1780.0, 1782.0, 1768.0, 1770.0, 1772.0, 1772.0, 1791.0, 1750.0, 1747.0, 1717.0, 1742.0, 1745.0, 1740.0, 1762.0, 1764.0, 1784.0, 1778.0, 1762.0, 1762.0], 'sex': [1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, nan, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0], 'det': ['"김조부는 신등면 사람으로, 조선시대 사람이다."', '"박씨는 김조부의 부인으로, 조선시대 사람이다."', '"김조일은 김조부와 박씨의 자로, 조선시대 사람이다."', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], 'bold': [1.0, nan, 1.0, nan, nan, nan, nan, 1.0, 1.0, nan, 1.0, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], 'xlabel': ['1732\\n1735\\n1738', nan, 1774, nan, nan, nan, nan, 1786, '1792\\n1801', nan, '1792\\n1798\\n1801\\n1804\\n1813', nan, nan, '1810\\n1813', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, '1783\\n1792\\n1801', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], 'fa': [nan, nan, 1.0, nan, 1.0, nan, nan, 1.0, nan, 3.0, 3.0, nan, 11.0, 11.0, 5.0, nan, 5.0, nan, 15.0, 15.0, 8.0, 8.0, 8.0, 26.0, 23.0, nan, nan, nan, 28.0, nan, 28.0, 29.0, nan, 32.0, 26.0, nan, nan], 'hs': [nan, 1.0, nan, 3.0, nan, 5.0, 5.0, nan, 8.0, nan, nan, 11.0, nan, nan, nan, 15.0, nan, 17.0, nan, nan, nan, nan, nan, 23.0, nan, nan, 26.0, nan, nan, 29.0, nan, nan, 32.0, 20.0, nan, nan, nan], 'rl01_id': [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 9.0, 15.0], 'rl01_lab': [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, '사촌', '사촌'], 'rl02_id': [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 32.0], 'rl02_lab': [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, '친구']}
dft = pd.DataFrame(dft)

def Tree(dft, format='svg', graph_name='OnceUponATimeInChosun',
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
