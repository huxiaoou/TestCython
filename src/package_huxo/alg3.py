# cython: annotation_typing = False

from typedef import CQuant
from typing import List
import numpy as np


def cal_average_salary(quants: List[CQuant]) -> float:
    # def cal_average_salary(quants: list[CQuant]) -> float:
    salary_sum = 0
    for quant in quants:
        salary_sum += quant.salary
    count = len(quants)
    return salary_sum / count if count > 0 else np.nan
