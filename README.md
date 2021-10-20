# poptree
Make family trees with Graphviz (on python)
  
### To execute:
```
pip install git+https://github.com/acheul/poptree.git<br>
from pop_tree import *
```  

### details
* What you need is a tidily organized pandas dataframe, which has information on linkages between wife-husband and child-father.
* The dataframe should have following columns.  
  
|id|name|birth_year|sex|det|bold|xlabel|fa|hs|rl01_id|rl01_lab|rl02_id|rl02_lab|
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|1|김조부\n(金造釜)|1720|1|"김조부는 신등면 사람으로, 조선시대 사람이다."|1|1732\n1735\n1738|NaN|NaN|NaN|NaN|NaN|NaN|  
  
> * *id* - Each person should have its own unique id.
> * *name* - This value will be the main label of the person.
> * *birth_year* - This value will be a part of the main label. If you don't want to reveal it, just left it Nan.
> * *sex* - Assign 1 for male, 2 for female and 3 for uncertain.
> * *det* - Describe some details on the person. This value will be indicated with a *mouse hover*. If you don't assign this value, the *name* value will be used as a mouse hover label.
> * *bold* - If you wand to make *style: bold* for the person's node, assign value 1.
> * *xlabel* - This value will be the sub-label, marked outside of a node.
> * *fa* - Assign *id* of the father of the person.
> * *hs* - Assign *id* of the husband of the person.
> * *rl01_id* - If you wand to indicate different relationship then *fa* or *hs*, assign the *id* of that relationship. This value must be paired with *rl01_lab*
> * *rl01_lab* - Assign the name of the relationship in *rl01_id*
> * *rl02_id*, *rl02_lab* - They are same as *rl01_id*, *rl01_lab*  
  
* You can reassign keyword arguments:
> * *format* of the Graph, *graph_name*, *graph_attr*, *node_attr*, *edge_attr*
> * You can transform the *Shape* dictionary, which links sex(1, 2, 3) and the shape of node. Currently it's "Shape={1:'box', 2:'ellipse', 3:'egg'}"
> * Also you can transform *Bold* dictionary, which links bold(1, 0) and the style of node. On default it is "Bold={0:'solid', 1:'bold'}"
> * If you designate "use_rllab=False", the *rl01* and *rl02* relationship will not be marked on the graph. "True" is the default.
> * If you designate "use_bold=False", the *bold* columns will not work on the graph. "True" is the default.

* The *Tree* function returns a Graph object. If you want to render and save it, you have to execute that process outside of the function. For example,
```
dot = Tree(df=dft, use_rllab=True) # Tree function works.
dot.render('tree', view=True) # render and save it as 'tree'. (defualt format is .svg)
display(dot) # To display it right away.
```
  
### Notes
* I higly recommend to work on Google Colab, which have graphviz installed from the first. Otherwise, it would be quite picky to install and use graphviz.  
* Designing this pack was initially inspired from a work of Ahsen Parwez https://medium.com/@ahsenparwez/building-a-family-tree-with-python-and-graphviz-e4afb8367316
* The main purpose for this pack is to restore and visualize family geneologies from premodern historic data. This is why the family tree here are mainly structured on paternal linkage, that is, on wife-husband and father-child connections.
* In the latest version, graphviz distinguishes *cluster* and *subgraph*. I got this point thanks to a StackFlow Q&A, https://stackoverflow.com/questions/55561635/problem-with-rank-same-in-subgraphs-and-clusters
  
### Examples
![treexample](./image/treexample.png)
