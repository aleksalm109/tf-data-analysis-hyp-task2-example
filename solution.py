import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 881258336 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = st.mannwhitneyu(x, y, alternative='two-sided').pvalue/2
    if p < 0.03:
        return True
    else:
        return False
