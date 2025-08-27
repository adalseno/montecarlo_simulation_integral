import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from numba import njit


@njit(parallel=True, fastmath=True, cache=True)
def compute_area(a: float, b: float, N: int) -> np.ndarray:
    """
    Compute an array of Monte Carlo approximations of the area of a function
    within given bounds.

    Parameters
    ----------
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    N : int
        The number of Monte Carlo approximations to perform.

    Returns
    -------
    areas : np.ndarray
        An array of `N` Monte Carlo approximations of the area of the function
        within the given bounds.
    """

    areas = np.empty(N)
    for i in range(N):
        areas[i] = (b - a) / N * np.sin(np.random.uniform(a, b, N)).sum()
    return areas


# Limits
a = 0  # lower
b = np.pi  # upper
# Number of iterations (for 10K ≈ 2 sec, for 100K it takes 10*10 more time ≈ 3 minutes on my PC)
N = 10_000

# Title and subtitle
st.title("Monte Carlo simulation")
st.html("<p>We simulate the area of sin(x) from 0 to &pi; that is given by:</p>")
st.latex(r"\int_{o}^{\pi} sin(x) = -cos(x) \Big|_0^{\pi} = 2")
st.text(
    "We can approximate the area with the formula:"
)
st.latex(r'''
    (b-a) \frac{1}{N} \sum_{i=1}^{N} f(x_i) \rightarrow (b-a) \frac{1}{N} \sum_{i=1}^{N} sin(x_i)
''')

# Get data
data_load_state = st.text("Computing data...")
areas = compute_area(a, b, N)
data_load_state.text("Done!")

# Add statistics
avg = np.round(np.mean(areas), 2)  # Mean
sigma = np.round(np.std(areas),2)  # Std
lowb = np.round(avg - 1.96 * sigma / np.sqrt(N),2)  # Low Bound
upb = np.round(avg + 1.96 * sigma / np.sqrt(N),2)  # Upper Bound
width = np.round(upb - lowb,2)  # Width

# Create DataFrame with statistics
stat_df = pd.DataFrame(
    {
        "Trials": f"{N:,}",
        "Average": f" {avg:.2f}",
        "St. Dev": f" {sigma:.2f}",
        "Upper Bound": f" {upb:.2f}",
        "Low Bound": f" {lowb:.2f}",
        "Width": f" {width:.2f}",
    },
    index=["Monte Carlo Simulation"],
)


# Display statistics (the values are strings)
st.text("Statistics with 95% confidence interval (rounded to 2 decimals):")
st.table(stat_df)

fig, ax = plt.subplots(figsize=(10,8))

textstr = '\n'.join((
    fr'$\mu=${avg:.2f}',
    fr'$\sigma=${sigma:.2f}' ))

ax.hist(areas, bins=31, ec='b')
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='blue', alpha=0.1)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.title("Distribution of calculated areas")
plt.xlabel("Areas")

# Plot histogram
st.pyplot(fig)
