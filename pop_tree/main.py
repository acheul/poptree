'''
Graphviz must be installed ahead.
This function works on graphviz.Graph

please run
  > from graphviz import Graph 
before execute this fucntion.

If you do not assign a different dataframe, the function will use a default dataframe.
The dataframe assigned must follow a proper format to be organized. 
'''

def init():
  global dft
  dft = pd.read_csv("testtable.csv")

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
