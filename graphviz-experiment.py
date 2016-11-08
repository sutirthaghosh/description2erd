from graphviz import Graph,Digraph

g = Graph(format='svg',engine='dot',graph_attr={'splines': 'false'})
g.body.extend(['rankdir=LR'])
g.node('STUDENT', shape='rectangle', style='filled', fillcolor='red')
g.node('Name', shape='ellipse')
g.node('address', shape='ellipse')
g.node('Roll Number', shape='ellipse')

g.edge('STUDENT', 'Name')
g.edge('STUDENT', 'address')
g.edge('STUDENT', 'Roll Number')

g.node('COURSE', shape='rectangle', style='filled', fillcolor='red')
g.node('Title', shape='ellipse')
g.node('Level', shape='ellipse')
g.node('Credits', shape='ellipse')
g.node('Course_Id', shape='ellipse')

g.edge('COURSE', 'Title')
g.edge('COURSE', 'Level')
g.edge('COURSE', 'Credits')
g.edge('COURSE', 'Course_Id')

g.node('TAKES', shape='diamond', style='filled', fillcolor='green')
g.edge('STUDENT', 'TAKES:w')
g.edge('COURSE', 'TAKES:e')

#g.render('example.svg')

g.view()
