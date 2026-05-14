from pyscript import display  # type: ignore
from js import document  # type: ignore

import numpy as np
import matplotlib.pyplot as plt


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absences = np.zeros(len(days), dtype=int)


def get_value(element_id):
    return document.getElementById(element_id).value


def draw_graph():

    plt.close("all")  # important fix for PyScript

    x = np.arange(len(days))

    plt.bar(x, absences, width=0.6)

    plt.xticks(x, days)

    plt.ylim(0, 5)

    plt.grid(axis="y", linestyle="--", alpha=0.3)

    plt.title("Weekly Absences", pad=10)

    plt.xlabel("Days")

    plt.ylabel("Absences")

    display(plt.gcf(), target="plot", append=False)

def submit_data(*args):

    day = get_value("day")

    try:
        value = int(get_value("value") or 0)

    except ValueError:
        return

    if day not in days:
        return

    index = days.index(day)

    absences[index] = min(value, 5)

    value_input = document.getElementById("value")

    if value_input:
        value_input.value = ""

    draw_graph()


draw_graph()