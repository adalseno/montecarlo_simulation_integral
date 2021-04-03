# Monte Carlo simulation
**Monte Carlo methods, or Monte Carlo experiments,** are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle. [wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
<br>
We simulate the area of <img src="https://render.githubusercontent.com/render/math?math=sin(x) \text{from} 0 \text{to} \pi"> that is given by <img src="https://render.githubusercontent.com/render/math?math=\int_{o}^{\pi} sin(x) = -cos(x) \Big|_0^{\pi} = 2"> <br>
<br>
We can approximate the area with the formula <img src="https://render.githubusercontent.com/render/math?math=(b-a) \frac{1}{N} \sum_{i=1}^{N} f(x_i)"> in our case  <img src="https://render.githubusercontent.com/render/math?math=(b-a) \frac{1}{N} \sum_{i=1}^{N} sin(x_i)"> <br><br>

Thanks to Andrew Dotson video https://www.youtube.com/watch?v=WAf0rqwAvgg

Try it live on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/adalseno/montecarlo_simulation_integral/HEAD?filepath=Monte%20Carlo%20simulation%20for%20integral.ipynb)
