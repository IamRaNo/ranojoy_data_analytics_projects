from scipy.stats import levene,ttest_ind,chi2_contingency
import numpy as np

def is_var_same(first_series,second_series):
    '''
        function for checking the vaiance of 2 groups and returns p-stats
        p < 0.5 means not equal variance
    '''
    stat, p =levene(first_series,second_series)
    result = "Equal variance" if p >= 0.05 else "Not equal variance"
    print(f"Levene p-value: {p:.5f} → {result}")
    return {"statistic": stat, "p": p, "result": result}


def chi_sqared_test(ct):
    stat, p, dof, expected = chi2_contingency(ct)
    n = ct.sum().sum()
    r, k = ct.shape
    cramer_v = np.sqrt(stat / (n * (min(r, k) - 1)))

    # Strength interpretation
    if cramer_v < 0.1:
        strength = "Weak"
    elif 0.1 <= cramer_v < 0.3:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"Chi-square p-value: {p:.5f}")
    print(f"Cramer's V: {cramer_v:.3f} → {strength}")

    return {
        "statistic": stat,
        "p": p,
        "dof": dof,
        "cramers_v": cramer_v,
        "strength": strength,
        "expected": expected
    }


def ttest(first,second):
    stat,p=ttest_ind(np.array(first),np.array(second),equal_var=False)
    result = "Reject null (groups different)" if p < 0.05 else "Fail to reject null (groups similar)"
    print(f"T-test p-value: {p:.5f} → {result}")
    return {"statistic": stat, "p": p, "result": result}

