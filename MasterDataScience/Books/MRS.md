# Manning, Raghavan, Schütze, *Introduction to Information Retrieval*

[⬅ Back to tracker](../README.md)

<a id="top"></a>

## 📑 Table of Contents

1. [Boolean Retrieval](#ch1) ⭐ *course*
2. [The Term Vocabulary and Postings Lists](#ch2) ⭐ *course*
3. [Dictionaries and Tolerant Retrieval](#ch3)
4. [Index Construction](#ch4)
5. [Index Compression](#ch5)
6. [Scoring, Term Weighting and the Vector Space Model](#ch6) ⭐ *course*
7. [Computing Scores in a Complete Search System](#ch7)
8. [Evaluation in Information Retrieval](#ch8)
9. [Relevance Feedback and Query Expansion](#ch9)
10. [XML Retrieval](#ch10)
11. [Probabilistic Information Retrieval](#ch11)
12. [Language Models for Information Retrieval](#ch12)
13. [Text Classification and Naive Bayes](#ch13)
14. [Vector Space Classification](#ch14)
15. [Support Vector Machines and Machine Learning on Documents](#ch15)
16. [Flat Clustering](#ch16)
17. [Hierarchical Clustering](#ch17)
18. [Matrix Decompositions and Latent Semantic Indexing](#ch18)
19. [Web Search Basics](#ch19)
20. [Web Crawling and Indexes](#ch20)
21. [Link Analysis](#ch21)

<a id="ch1"></a>

### Ch. 1: Boolean Retrieval (p. 1) ⭐ *course Oct 20*
- [ ] 1.1 An Example Information Retrieval Problem (p. 3) ⭐ *Oct 20*
- [ ] 1.2 A First Take at Building an Inverted Index (p. 6) ⭐ *Oct 20*
- [ ] 1.3 Processing Boolean Queries (p. 10) ⭐ *Oct 20*
- [ ] 1.4 The Extended Boolean Model versus Ranked Retrieval (p. 14) ⭐ *Oct 20*
- [ ] 1.5 References and Further Reading (p. 17)

[⬆ Back to top](#top)

<a id="ch2"></a>

### Ch. 2: The Term Vocabulary and Postings Lists (p. 19) ⭐ *course*
- [ ] 2.1 Document Delineation and Character Sequence Decoding (p. 19) ⭐ *Oct 19*
  - [ ] 2.1.1 Obtaining the Character Sequence in a Document (p. 19) ⭐ *Oct 19*
  - [ ] 2.1.2 Choosing a Document Unit (p. 20) ⭐ *Oct 19*
- [ ] 2.2 Determining the Vocabulary of Terms (p. 22) ⭐ *Oct 19*
  - [ ] 2.2.1 Tokenization (p. 22) ⭐ *Oct 19*
  - [ ] 2.2.2 Dropping Common Terms: Stop Words (p. 27) ⭐ *Oct 19*
  - [ ] 2.2.3 Normalization (Equivalence Classing of Terms) (p. 28) ⭐ *Oct 19*
  - [ ] 2.2.4 Stemming and Lemmatization (p. 32) ⭐ *Oct 19*
- [ ] 2.3 Faster Postings List Intersection via Skip Pointers (p. 36)
- [ ] 2.4 Positional Postings and Phrase Queries (p. 39)
  - [ ] 2.4.1 Biword Indexes (p. 39)
  - [ ] 2.4.2 Positional Indexes (p. 41)
  - [ ] 2.4.3 Combination Schemes (p. 43)
- [ ] 2.5 References and Further Reading (p. 45)

[⬆ Back to top](#top)

<a id="ch3"></a>

### Ch. 3: Dictionaries and Tolerant Retrieval (p. 49)
- [ ] 3.1 Search Structures for Dictionaries (p. 49)
- [ ] 3.2 Wildcard Queries (p. 51)
  - [ ] 3.2.1 General Wildcard Queries (p. 53)
  - [ ] 3.2.2 k-gram Indexes for Wildcard Queries (p. 54)
- [ ] 3.3 Spelling Correction (p. 56)
  - [ ] 3.3.1 Implementing Spelling Correction (p. 57)
  - [ ] 3.3.2 Forms of Spelling Correction (p. 57)
  - [ ] 3.3.3 Edit Distance (p. 58)
  - [ ] 3.3.4 k-gram Indexes for Spelling Correction (p. 60)
  - [ ] 3.3.5 Context-Sensitive Spelling Correction (p. 62)
- [ ] 3.4 Phonetic Correction (p. 63)
- [ ] 3.5 References and Further Reading (p. 65)

[⬆ Back to top](#top)

<a id="ch4"></a>

### Ch. 4: Index Construction (p. 67)
- [ ] 4.1 Hardware Basics (p. 68)
- [ ] 4.2 Blocked Sort-Based Indexing (p. 69)
- [ ] 4.3 Single-Pass In-Memory Indexing (p. 73)
- [ ] 4.4 Distributed Indexing (p. 74)
- [ ] 4.5 Dynamic Indexing (p. 78)
- [ ] 4.6 Other Types of Indexes (p. 80)
- [ ] 4.7 References and Further Reading (p. 83)

[⬆ Back to top](#top)

<a id="ch5"></a>

### Ch. 5: Index Compression (p. 85)
- [ ] 5.1 Statistical Properties of Terms in Information Retrieval (p. 86)
  - [ ] 5.1.1 Heaps' Law: Estimating the Number of Terms (p. 88)
  - [ ] 5.1.2 Zipf's Law: Modeling the Distribution of Terms (p. 89)
- [ ] 5.2 Dictionary Compression (p. 90)
  - [ ] 5.2.1 Dictionary as a String (p. 91)
  - [ ] 5.2.2 Blocked Storage (p. 92)
- [ ] 5.3 Postings File Compression (p. 95)
  - [ ] 5.3.1 Variable Byte Codes (p. 96)
  - [ ] 5.3.2 γ Codes (p. 98)
- [ ] 5.4 References and Further Reading (p. 105)

[⬆ Back to top](#top)

<a id="ch6"></a>

### Ch. 6: Scoring, Term Weighting and the Vector Space Model (p. 109) ⭐ *course*
- [ ] 6.1 Parametric and Zone Indexes (p. 110)
  - [ ] 6.1.1 Weighted Zone Scoring (p. 112)
  - [ ] 6.1.2 Learning Weights (p. 113)
  - [ ] 6.1.3 The Optimal Weight g (p. 115)
- [ ] 6.2 Term Frequency and Weighting (p. 117) ⭐ *Oct 20*
  - [ ] 6.2.1 Inverse Document Frequency (p. 117) ⭐ *Oct 20*
  - [ ] 6.2.2 Tf-idf Weighting (p. 118) ⭐ *Oct 20*
- [ ] 6.3 The Vector Space Model for Scoring (p. 120) ⭐ *Oct 20, Oct 22*
  - [ ] 6.3.1 Dot Products (p. 120) ⭐ *Oct 20, Oct 22*
  - [ ] 6.3.2 Queries as Vectors (p. 123) ⭐ *Oct 20, Oct 22*
  - [ ] 6.3.3 Computing Vector Scores (p. 124) ⭐ *Oct 20, Oct 22*
- [ ] 6.4 Variant tf-idf Functions (p. 126)
  - [ ] 6.4.1 Sublinear tf Scaling (p. 126)
  - [ ] 6.4.2 Maximum tf Normalization (p. 127)
  - [ ] 6.4.3 Document and Query Weighting Schemes (p. 128)
  - [ ] 6.4.4 Pivoted Normalized Document Length (p. 129)
- [ ] 6.5 References and Further Reading (p. 133)

[⬆ Back to top](#top)

<a id="ch7"></a>

### Ch. 7: Computing Scores in a Complete Search System (p. 135)
- [ ] 7.1 Efficient Scoring and Ranking (p. 135)
  - [ ] 7.1.1 Inexact Top K Document Retrieval (p. 137)
  - [ ] 7.1.2 Index Elimination (p. 137)
  - [ ] 7.1.3 Champion Lists (p. 138)
  - [ ] 7.1.4 Static Quality Scores and Ordering (p. 138)
  - [ ] 7.1.5 Impact Ordering (p. 140)
  - [ ] 7.1.6 Cluster Pruning (p. 141)
- [ ] 7.2 Components of an Information Retrieval System (p. 143)
  - [ ] 7.2.1 Tiered Indexes (p. 143)
  - [ ] 7.2.2 Query-Term Proximity (p. 144)
  - [ ] 7.2.3 Designing Parsing and Scoring Functions (p. 145)
  - [ ] 7.2.4 Putting It All Together (p. 146)
- [ ] 7.3 Vector Space Scoring and Query Operator Interaction (p. 147)
- [ ] 7.4 References and Further Reading (p. 149)

[⬆ Back to top](#top)

<a id="ch8"></a>

### Ch. 8: Evaluation in Information Retrieval (p. 151)
- [ ] 8.1 Information Retrieval System Evaluation (p. 152)
- [ ] 8.2 Standard Test Collections (p. 153)
- [ ] 8.3 Evaluation of Unranked Retrieval Sets (p. 154)
- [ ] 8.4 Evaluation of Ranked Retrieval Results (p. 158)
- [ ] 8.5 Assessing Relevance (p. 164)
  - [ ] 8.5.1 Critiques and Justifications of the Concept of Relevance (p. 166)
- [ ] 8.6 A Broader Perspective: System Quality and User Utility (p. 168)
  - [ ] 8.6.1 System Issues (p. 168)
  - [ ] 8.6.2 User Utility (p. 169)
  - [ ] 8.6.3 Refining a Deployed System (p. 170)
- [ ] 8.7 Results Snippets (p. 170)
- [ ] 8.8 References and Further Reading (p. 173)

[⬆ Back to top](#top)

<a id="ch9"></a>

### Ch. 9: Relevance Feedback and Query Expansion (p. 177)
- [ ] 9.1 Relevance Feedback and Pseudo Relevance Feedback (p. 178)
  - [ ] 9.1.1 The Rocchio Algorithm for Relevance Feedback (p. 178)
  - [ ] 9.1.2 Probabilistic Relevance Feedback (p. 183)
  - [ ] 9.1.3 When Does Relevance Feedback Work? (p. 183)
  - [ ] 9.1.4 Relevance Feedback on the Web (p. 185)
  - [ ] 9.1.5 Evaluation of Relevance Feedback Strategies (p. 186)
  - [ ] 9.1.6 Pseudo Relevance Feedback (p. 187)
  - [ ] 9.1.7 Indirect Relevance Feedback (p. 187)
  - [ ] 9.1.8 Summary (p. 188)
- [ ] 9.2 Global Methods for Query Reformulation (p. 189)
  - [ ] 9.2.1 Vocabulary Tools for Query Reformulation (p. 189)
  - [ ] 9.2.2 Query Expansion (p. 189)
  - [ ] 9.2.3 Automatic Thesaurus Generation (p. 192)
- [ ] 9.3 References and Further Reading (p. 193)

[⬆ Back to top](#top)

<a id="ch10"></a>

### Ch. 10: XML Retrieval (p. 195)
- [ ] 10.1 Basic XML Concepts (p. 197)
- [ ] 10.2 Challenges in XML Retrieval (p. 201)
- [ ] 10.3 A Vector Space Model for XML Retrieval (p. 206)
- [ ] 10.4 Evaluation of XML Retrieval (p. 210)
- [ ] 10.5 Text-Centric vs. Data-Centric XML Retrieval (p. 214)
- [ ] 10.6 References and Further Reading (p. 216)
- [ ] 10.7 Exercises (p. 217)

[⬆ Back to top](#top)

<a id="ch11"></a>

### Ch. 11: Probabilistic Information Retrieval (p. 219)
- [ ] 11.1 Review of Basic Probability Theory (p. 220)
- [ ] 11.2 The Probability Ranking Principle (p. 221)
  - [ ] 11.2.1 The 1/0 Loss Case (p. 221)
  - [ ] 11.2.2 The PRP with Retrieval Costs (p. 222)
- [ ] 11.3 The Binary Independence Model (p. 222)
  - [ ] 11.3.1 Deriving a Ranking Function for Query Terms (p. 224)
  - [ ] 11.3.2 Probability Estimates in Theory (p. 226)
  - [ ] 11.3.3 Probability Estimates in Practice (p. 227)
  - [ ] 11.3.4 Probabilistic Approaches to Relevance Feedback (p. 228)
- [ ] 11.4 An Appraisal and Some Extensions (p. 230)
  - [ ] 11.4.1 An Appraisal of Probabilistic Models (p. 230)
  - [ ] 11.4.2 Tree-Structured Dependencies Between Terms (p. 231)
  - [ ] 11.4.3 Okapi BM25: A Non-Binary Model (p. 232)
  - [ ] 11.4.4 Bayesian Network Approaches to IR (p. 234)
- [ ] 11.5 References and Further Reading (p. 235)

[⬆ Back to top](#top)

<a id="ch12"></a>

### Ch. 12: Language Models for Information Retrieval (p. 237)
- [ ] 12.1 Language Models (p. 237)
  - [ ] 12.1.1 Finite Automata and Language Models (p. 237)
  - [ ] 12.1.2 Types of Language Models (p. 240)
  - [ ] 12.1.3 Multinomial Distributions over Words (p. 241)
- [ ] 12.2 The Query Likelihood Model (p. 242)
  - [ ] 12.2.1 Using Query Likelihood Language Models in IR (p. 242)
  - [ ] 12.2.2 Estimating the Query Generation Probability (p. 243)
  - [ ] 12.2.3 Ponte and Croft's Experiments (p. 246)
- [ ] 12.3 Language Modeling versus Other Approaches in IR (p. 248)
- [ ] 12.4 Extended Language Modeling Approaches (p. 250)
- [ ] 12.5 References and Further Reading (p. 252)

[⬆ Back to top](#top)

<a id="ch13"></a>

### Ch. 13: Text Classification and Naive Bayes (p. 253)
- [ ] 13.1 The Text Classification Problem (p. 256)
- [ ] 13.2 Naive Bayes Text Classification (p. 258)
  - [ ] 13.2.1 Relation to Multinomial Unigram Language Model (p. 262)
- [ ] 13.3 The Bernoulli Model (p. 263)
- [ ] 13.4 Properties of Naive Bayes (p. 265)
  - [ ] 13.4.1 A Variant of the Multinomial Model (p. 270)
- [ ] 13.5 Feature Selection (p. 271)
  - [ ] 13.5.1 Mutual Information (p. 272)
  - [ ] 13.5.2 χ² Feature Selection (p. 275)
  - [ ] 13.5.3 Frequency-Based Feature Selection (p. 277)
  - [ ] 13.5.4 Feature Selection for Multiple Classifiers (p. 278)
  - [ ] 13.5.5 Comparison of Feature Selection Methods (p. 278)
- [ ] 13.6 Evaluation of Text Classification (p. 279)
- [ ] 13.7 References and Further Reading (p. 286)

[⬆ Back to top](#top)

<a id="ch14"></a>

### Ch. 14: Vector Space Classification (p. 289)
- [ ] 14.1 Document Representations and Measures of Relatedness in Vector Spaces (p. 291)
- [ ] 14.2 Rocchio Classification (p. 292)
- [ ] 14.3 k Nearest Neighbor (p. 297)
  - [ ] 14.3.1 Time Complexity and Optimality of kNN (p. 299)
- [ ] 14.4 Linear versus Nonlinear Classifiers (p. 301)
- [ ] 14.5 Classification with More Than Two Classes (p. 306)
- [ ] 14.6 The Bias-Variance Tradeoff (p. 308)
- [ ] 14.7 References and Further Reading (p. 314)
- [ ] 14.8 Exercises (p. 315)

[⬆ Back to top](#top)

<a id="ch15"></a>

### Ch. 15: Support Vector Machines and Machine Learning on Documents (p. 319)
- [ ] 15.1 Support Vector Machines: The Linearly Separable Case (p. 320)
- [ ] 15.2 Extensions to the SVM Model (p. 327)
  - [ ] 15.2.1 Soft Margin Classification (p. 327)
  - [ ] 15.2.2 Multiclass SVMs (p. 330)
  - [ ] 15.2.3 Nonlinear SVMs (p. 330)
  - [ ] 15.2.4 Experimental Results (p. 333)
- [ ] 15.3 Issues in the Classification of Text Documents (p. 334)
  - [ ] 15.3.1 Choosing What Kind of Classifier to Use (p. 335)
  - [ ] 15.3.2 Improving Classifier Performance (p. 337)
- [ ] 15.4 Machine Learning Methods in Ad Hoc Information Retrieval (p. 341)
  - [ ] 15.4.1 A Simple Example of Machine-Learned Scoring (p. 341)
  - [ ] 15.4.2 Result Ranking by Machine Learning (p. 344)
- [ ] 15.5 References and Further Reading (p. 346)

[⬆ Back to top](#top)

<a id="ch16"></a>

### Ch. 16: Flat Clustering (p. 349)
- [ ] 16.1 Clustering in Information Retrieval (p. 350)
- [ ] 16.2 Problem Statement (p. 354)
  - [ ] 16.2.1 Cardinality: The Number of Clusters (p. 355)
- [ ] 16.3 Evaluation of Clustering (p. 356)
- [ ] 16.4 K-means (p. 360)
  - [ ] 16.4.1 Cluster Cardinality in K-means (p. 365)
- [ ] 16.5 Model-Based Clustering (p. 368)
- [ ] 16.6 References and Further Reading (p. 372)
- [ ] 16.7 Exercises (p. 374)

[⬆ Back to top](#top)

<a id="ch17"></a>

### Ch. 17: Hierarchical Clustering (p. 377)
- [ ] 17.1 Hierarchical Agglomerative Clustering (p. 378)
- [ ] 17.2 Single-Link and Complete-Link Clustering (p. 382)
  - [ ] 17.2.1 Time Complexity of HAC (p. 385)
- [ ] 17.3 Group-Average Agglomerative Clustering (p. 388)
- [ ] 17.4 Centroid Clustering (p. 391)
- [ ] 17.5 Optimality of HAC (p. 393)
- [ ] 17.6 Divisive Clustering (p. 395)
- [ ] 17.7 Cluster Labeling (p. 396)
- [ ] 17.8 Implementation Notes (p. 398)
- [ ] 17.9 References and Further Reading (p. 399)
- [ ] 17.10 Exercises (p. 401)

[⬆ Back to top](#top)

<a id="ch18"></a>

### Ch. 18: Matrix Decompositions and Latent Semantic Indexing (p. 403)
- [ ] 18.1 Linear Algebra Review (p. 403)
  - [ ] 18.1.1 Matrix Decompositions (p. 406)
- [ ] 18.2 Term-Document Matrices and Singular Value Decompositions (p. 407)
- [ ] 18.3 Low-Rank Approximations (p. 410)
- [ ] 18.4 Latent Semantic Indexing (p. 412)
- [ ] 18.5 References and Further Reading (p. 417)

[⬆ Back to top](#top)

<a id="ch19"></a>

### Ch. 19: Web Search Basics (p. 421)
- [ ] 19.1 Background and History (p. 421)
- [ ] 19.2 Web Characteristics (p. 423)
  - [ ] 19.2.1 The Web Graph (p. 425)
  - [ ] 19.2.2 Spam (p. 427)
- [ ] 19.3 Advertising as the Economic Model (p. 429)
- [ ] 19.4 The Search User Experience (p. 432)
  - [ ] 19.4.1 User Query Needs (p. 432)
- [ ] 19.5 Index Size and Estimation (p. 433)
- [ ] 19.6 Near-Duplicates and Shingling (p. 437)
- [ ] 19.7 References and Further Reading (p. 441)

[⬆ Back to top](#top)

<a id="ch20"></a>

### Ch. 20: Web Crawling and Indexes (p. 443)
- [ ] 20.1 Overview (p. 443)
  - [ ] 20.1.1 Features a Crawler Must Provide (p. 443)
  - [ ] 20.1.2 Features a Crawler Should Provide (p. 444)
- [ ] 20.2 Crawling (p. 444)
  - [ ] 20.2.1 Crawler Architecture (p. 445)
  - [ ] 20.2.2 DNS Resolution (p. 449)
  - [ ] 20.2.3 The URL Frontier (p. 451)
- [ ] 20.3 Distributing Indexes (p. 454)
- [ ] 20.4 Connectivity Servers (p. 455)
- [ ] 20.5 References and Further Reading (p. 458)

[⬆ Back to top](#top)

<a id="ch21"></a>

### Ch. 21: Link Analysis (p. 461)
- [ ] 21.1 The Web as a Graph (p. 462)
  - [ ] 21.1.1 Anchor Text and the Web Graph (p. 462)
- [ ] 21.2 PageRank (p. 464)
  - [ ] 21.2.1 Markov Chains (p. 465)
  - [ ] 21.2.2 The PageRank Computation (p. 468)
  - [ ] 21.2.3 Topic-Specific PageRank (p. 471)
- [ ] 21.3 Hubs and Authorities (p. 474)
  - [ ] 21.3.1 Choosing the Subset of the Web (p. 477)
- [ ] 21.4 References and Further Reading (p. 480)

[⬆ Back to top](#top)
