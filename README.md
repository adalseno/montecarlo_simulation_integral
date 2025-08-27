# Monte Carlo simulation
**Monte Carlo methods, or Monte Carlo experiments,** are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle. [wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)


We simulate the area of $\sin(x) \textrm{ from } 0 \textrm{ to } \pi$ that is given by $\int_0^{\pi} \sin(x) = -\cos(x) \Big|_0^{\pi} = 2 $  

<br>
We can approximate the area with the formula:

$$(b-a) \frac {1}{N} \sum_{i=1}^{N} f(x_i) \rightarrow (b-a) \frac {1}{N} \sum_{i=1}^{N} \sin(x_i)$$

Thanks to Andrew Dotson video https://www.youtube.com/watch?v=WAf0rqwAvgg

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://montecarlosimulationintegral-5xfuc7etwstxpo5cxqfqu.streamlitapp.com/)
