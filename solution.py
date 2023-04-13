import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 881258336 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    a = st.anderson_ksamp([x, y]).significance_level
    return a < alpha
