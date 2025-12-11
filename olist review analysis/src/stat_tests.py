from scipy.stats import levene,ttest_ind,chi2_contingency,shapiro,mannwhitneyu
import numpy as np

def check_variance(data, group_col, value_col, val):
    g1 = data[data[group_col] == val][value_col].dropna()
    g2 = data[data[group_col] != val][value_col].dropna()
    p = levene(g1, g2)[1]
    return {
        "levene_p": p,
        "equal_variance": (p >= 0.05)
    }


def check_normality(data, group_col, value_col, val):
    g1 = data[data[group_col] == val][value_col].dropna()
    g2 = data[data[group_col] != val][value_col].dropna()
    n1, n2 = len(g1), len(g2)
    # If sample size too large → skip Shapiro
    if n1 > 5000 or n2 > 5000:
        return {
            "g1_p": None,
            "g2_p": None,
            "normal": True,        # Treat as normal for t-test
            "reason": "Sample size > 5000, Shapiro skipped"
        }
    # Normal case → use Shapiro
    p1 = shapiro(g1)[1]
    p2 = shapiro(g2)[1]
    return {
        "g1_p": p1,
        "g2_p": p2,
        "normal": (p1 >= 0.05 and p2 >= 0.05),
        "reason": "Shapiro used"
    }


def ttest(first,second,equal_variance):
    stat,p=ttest_ind(np.array(first),np.array(second),equal_var=equal_variance)
    result = "Reject null (groups different)" if p < 0.05 else "Fail to reject null (groups similar)"
    print(f"T-test p-value: {p:.5f} → {result}")
    return {"statistic": stat, "p": p, "result": result}


def run_mannwhitney(data, group_col, value_col, val):
    g1 = data[data[group_col] == val][value_col].dropna()
    g2 = data[data[group_col] != val][value_col].dropna()
    u, p = mannwhitneyu(g1, g2, alternative="two-sided")
    n1, n2 = len(g1), len(g2)
    rbc = 1 - (2 * u) / (n1 * n2)
    ar = abs(rbc)
    if ar < 0.1: strength = "very weak"
    elif ar < 0.3: strength = "weak"
    elif ar < 0.5: strength = "medium"
    else: strength = "strong"
    return {
        "p": p,
        "rank_biserial": rbc,
        "strength": strength
    }

def ttest_strength(data, group_col, value_col, val):
    """
    Returns Cohen's d and its strength classification.
    """
    g1 = data[data[group_col] == val][value_col].dropna()
    g2 = data[data[group_col] != val][value_col].dropna()
    # Cohen's d
    pooled_std = np.sqrt((g1.std()**2 + g2.std()**2) / 2)
    d = (g1.mean() - g2.mean()) / pooled_std
    # Classification
    if abs(d) < 0.2:
        strength = "very weak"
    elif abs(d) < 0.5:
        strength = "weak"
    elif abs(d) < 0.8:
        strength = "medium"
    else:
        strength = "strong"
    return d, strength

#_____________________________________________________________________________


def numerical_test(data, group_col, value_col, val):
    # 1. Normality check
    norm = check_normality(data, group_col, value_col, val)
    g1 = data[data[group_col] == val][value_col].dropna()
    g2 = data[data[group_col] != val][value_col].dropna()
    if norm["normal"]:   # both normal → t-test path
        print('Data has normal distribution so doing ttest_ind ->')
        var = check_variance(data, group_col, value_col, val)
        if var["equal_variance"]:
            print("Data has equal variance")
            ttest(g1, g2, equal_variance=True)
        else:
            print("Data do not have equal variance")
            print("Doing ttest - with equal variance false...")
            ttest(g1, g2, equal_variance=False)
        d, strength = ttest_strength(data, group_col, value_col, val)
        print(f"Strength of ttest: {strength}")
    else:   # NOT normal → Mann–Whitney
        print("Data do not have normal distribution so doing mann_whiteny_u test...")
        mw = run_mannwhitney(data, group_col, value_col, val)
        print(f"Strength of Mann-Whiteny U test is: {mw["strength"]}")


def chi_sqared_test(ct):
    stat, p, dof, expected = chi2_contingency(ct)
    n = ct.sum().sum()
    r, k = ct.shape
    result = "Reject null (groups different)" if p < 0.05 else "Fail to reject null (groups similar)"
    cramer_v = np.sqrt(stat / (n * (min(r, k) - 1)))
    # Strength interpretation
    if cramer_v < 0.1:
        strength = "Weak"
    elif 0.1 <= cramer_v < 0.3:
        strength = "Moderate"
    else:
        strength = "Strong"
    print(f"Chi-square p-value: {p:.5f}")
    print(result)
    print(f"Cramer's V: {cramer_v:.3f} → {strength}")


