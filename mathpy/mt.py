import re
from mathpy.grammar.complex.parser import parser as cmpx
from mathpy.grammar.paranthesis.parser import parser as paran
from plotly import tools
from plotly.offline import plot as ply
import plotly.graph_objs as go
import os

try:
    os.mkdir('plots')
except OSError:
    pass

def cal(s):
    s = paran.parse(s)
    result = cmpx.parse(s)
    return result

def equation(s):
    result = paran.parse(s)
    try:
        if result.index(';'):
            parts = result.split(';')
            chars = re.findall(r'(?![sin|cos|sec|cosec|tan|cot|log|ln|e|asin|acos|atan|sinh|cosh|tanh|asinh|acosh|atanh|j])[a-zA-Z][0-9a-zA-Z]*', parts[0])
            unique = sorted(set(chars), key=chars.index)
            vals = parts[1].split(',')
            for i in range(0, len(unique)):
                vals[i] = str(cmpx.parse(vals[i]))
                vals[i] = vals[i].replace('(', '')
                vals[i] = vals[i].replace(')', '')
                parts[0] = parts[0].replace(unique[i], vals[i])
            res = cmpx.parse(parts[0])
            return res
    except ValueError:
        pass
    return result

def plot(s, min=-100.0, max=100.0, name='Plot', val=[], valname='vals'):
    step = 0.5
    x = []
    y = []
    t = min
    while t != max:
        x.append(t)
        t+= step
    for e in x:
        v = equation(s + ';' + str(e))
        y.append(v.real)
    t = go.Scatter(x=x, y=y, mode='lines', name=s + ' ' + name)
    data = [t]
    if len(val) != 0:
        t1 = go.Scatter(x=val[0], y=val[1], mode='markers', name=valname)
        fig = tools.make_subplots(rows=1, cols=2, subplot_titles=(name + ' Plot', valname + ' Plot'))
        fig.append_trace(t, 1, 1)
        fig.append_trace(t1, 1, 2)
        fig['layout'].update(title=name + ' and ' + valname + ' Plots')
        ply(fig, filename='plots/' + name + ' and ' + valname + ' Plots.html')
    else:
        ply(data, filename='plots/' + s + ' ' + name + '.html')