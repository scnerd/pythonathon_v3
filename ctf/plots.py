import plotly
from plotly.graph_objs import *
from plotly.offline import plot

from .models import *

from itertools import groupby


def leaderboard_timeline(cur_user):
    solutions = Solution.objects.filter(success=True)
    plots = []
    for user, sols in groupby(sorted(solutions, key=lambda s: s.user)):
        sols = [s for u, s in sols]
        sols = list(sorted(sols, key=lambda s: s.timestamp))

        cur_score = 0.0
        x = []
        y = []

        for s in sols:
            cur_score += s.net_score
            x.append(s.timestamp)
            y.append(cur_score)

        plots.append(Scatter(
            x=x,
            y=y,
            name=user.username,
            mode='lines+markers',
            line=Line(color='blue' if user != cur_user else 'red'),
        ))

    layout = Layout()
    fig = Figure(data=plots, layout=layout)

    return plot(fig, show_link=False, output_type='div', auto_open=False)
