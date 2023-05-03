



Create a class named **TinyStatistician** that implements the following methods: 

 -  mean(x): computes the mean of a given non-empty list or array x, using a for-loop. The method returns the mean as a float, otherwise None if x is an empty list or array. Given a vector x of dimension m × 1, the mathematical formula of its mean is: <br/> $$µ = \frac{ 1}{m}\sum_{i=1}^{m} x_i$$ 


 - median(x): computes the median of a given non-empty list or array x. The method returns the median as a float, otherwise None if x is an empty list or array. 

 - quartiles(x): computes the 1 st and 3 rd quartiles of a given non-empty array x. The method returns the quartile as a float, otherwise None if x is an empty list or array. 

 - var(x): computes the variance of a given non-empty list or array x, using a forloop. The method returns the variance as a float, otherwise None if x is an empty list or array. Given a vector x of dimension m × 1, the mathematical formula of its variance is:<br/> $$σ^2 = \frac{1} {m}\sum_{i=1}^{m} (x_i - µ)^2  = \frac{1} {m}\sum_{i=1}^{m} [x_i - (\frac{1} {m}\sum_{j=1}^{m} x_j)]^2$$  

 - std(x) : computes the standard deviation of a given non-empty list or array x, using a for-loop. The method returns the standard deviation as a float, otherwise None if x is an empty list or array. Given a vector x of dimension m × 1, the mathematical formula of its standard deviation is:<br/> $$σ^2 = \sqrt{\frac{1} {m}\sum_{i=1}^{m} (x_i - µ)^2}  = \sqrt{\frac{1} {m}\sum_{i=1}^{m} [x_i - (\frac{1} {m}\sum_{j=1}^{m} x_j)]^2}$$

 &emsp; All methods take a **list** or a **numpy.ndarray** as parameter. We are assuming that all inputs have a correct format, i.e. a list or array of numeric type or empty list or array. You don’t have to protect your functions against input errors.
