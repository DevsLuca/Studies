## Chapter 1: Combinatorial Analysis

### 1.2 The Basic Principle of Counting
- **Multiplication Principle:**  
$$\text{Total outcomes} = n_1 \cdot n_2 \cdot ... \cdot n_k$$
- **Addition Principle (mutually exclusive events):**  
$$P(A \cup B) = P(A) + P(B)$$

### 1.3 Permutations
- Permutations of \(n\) distinct objects:  
$$P(n) = n!$$
- r-permutations of n objects:  
$$P(n,r) = \frac{n!}{(n-r)!}$$
- Permutations with repetitions (n objects, with groups of identical objects \(n_1, n_2, ..., n_k\)):  
$$\frac{n!}{n_1! n_2! ... n_k!}$$

### 1.4 Combinations
- r-combinations of n objects:  
$$C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$
- Properties:  
$$\binom{n}{r} = \binom{n}{n-r}, \quad \binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$$

### 1.5 Multinomial Coefficients and Theorem
- Multinomial coefficient:  
$$\binom{n}{n_1, n_2, ..., n_k} = \frac{n!}{n_1! n_2! ... n_k!}$$
- Multinomial theorem:  
$$(x_1 + x_2 + ... + x_k)^n = \sum_{n_1 + ... + n_k = n} \binom{n}{n_1, ..., n_k} \prod_{i=1}^k x_i^{n_i}$$

#### 1.4.1 Binomial Theorem
$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$$
- Application to probability (Binomial PMF):  
$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0,1,...,n$$

### 1.6 Number of Integer Solutions
- Non-negative integer solutions to \(x_1 + x_2 + ... + x_r = n\):  
$$\binom{n+r-1}{r-1}$$
- Positive integer solutions:  
$$\binom{n-1}{r-1}$$

---

## Chapter 2: Axioms of Probability

### 2.3 Axioms of Probability
1. Non-negativity:  
$$P(A) \ge 0$$
2. Normalization:  
$$P(S) = 1$$
3. Additivity (for mutually exclusive events):  
$$P(A \cup B) = P(A) + P(B)$$

#### Derived Formulas
- Complement:  
$$P(A^c) = 1 - P(A)$$
- Union:  
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
- Inclusion–Exclusion (for n events):  
$$P\Big(\bigcup_{i=1}^{n} A_i\Big) = \sum_i P(A_i) - \sum_{i<j} P(A_i \cap A_j) + ... + (-1)^{n+1} P(A_1 \cap ... \cap A_n)$$

### 2.5 Sample Spaces with Equally Likely Outcomes
$$P(A) = \frac{\text{num of favorable outcomes}}{\text{num of total outcomes}}$$

---

## Chapter 3: Conditional Probability and Independence

### 3.2 Conditional Probability
$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

### 3.3 Bayes’ Theorem
- Total probability formula:  
$$P(B) = \sum_{i=1}^{n} P(B|A_i)P(A_i)$$
- Bayes’ formula:  
$$P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum_{j=1}^{n} P(A_j)P(B|A_j)}$$

### 3.4 Independent Events
- Two events are independent if:  
$$P(A \cap B) = P(A) P(B)$$
- For multiple events: pairwise vs mutual independence

---

## Chapter 4: Random Variables

### 4.1 Random Variables
- **Discrete RV**:  
pmf $$\(P(X=x)\)$$  
- **Continuous RV**:  
pdf $$\(f_X(x)\)$$
- **CDF**:  
$$F_X(x) = P(X \le x)$$

### 4.3 Expected Value
- **Discrete**:  
$$E[X] = \sum_x x P(X=x)$$
- **Continuous**:  
$$E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$$
- **Linearity**:  
$$E[aX + bY] = a E[X] + b E[Y]$$
- Constant:  
$$E[c] = c$$

### 4.4 Expectation of a Function of a Random Variable
- **Discrete**:  
$$E[g(X)] = \sum_x g(x) P(X=x)$$
- **Continuous**:  
$$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$$

### 4.5 Variance
- Definition:  
$$Var(X) = E[(X-E[X])^2] = E[X^2] - (E[X])^2$$
- Properties:  
  - $$\(Var(aX+b) = a^2 Var(X)\)$$  
  - $$\(Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)\)$$
- Standard deviation:  
$$\sigma_X = \sqrt{Var(X)}$$
