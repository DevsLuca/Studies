# Graph Theory: Key Theorems and Algorithms (Chapters 1–4)
This document provides a structured, chapter-aligned summary of the most important **theorems, algorithms, and concepts** from *Graph Theory with Applications* by Bondy & Murty.  
The table below organizes each item according to the **chapter and topic**, includes the **type** (theorem, algorithm, or concept), the **name**, the **inventor or contributor**, and a concise statement or purpose.  

---

- **Chapter 1** – **Graphs and Simple Graphs**: Vertex degrees, Handshaking Lemma, basic connectivity.
- **Chapter 2** – **Graph Isomorphism / Matrices**: Sperner’s Lemma, Brouwer Fixed Point (topological applications), adjacency/incidence concepts (practical algorithms).
- **Chapter 3** – **Subgraphs, Paths, and Connection**: Trees, Cayley, Prüfer, BFS, DFS.
- **Chapter 4** – **Cycles, Euler, Hamilton, and Spanning Trees**: Eulerian and Hamiltonian results, Dijkstra, Prim, Kruskal, cycle decomposition, Dirac, Ore, Chvátal.

| Chapter / Topic                                       | Type      | Name                        | Inventor                   | Core Statement / Purpose                                                            |
| ----------------------------------------------------- | --------- | --------------------------- | -------------------------- | ----------------------------------------------------------------------------------- |
| **Ch. 1 – Graphs and Simple Graphs / Vertex Degrees** | Theorem   | Handshaking Lemma           | Leonhard Euler             | $(\sum_{v \in V} \deg(v) = 2E)$; the number of odd-degree vertices is even          |
| **Ch. 1 – Graphs and Simple Graphs / Connectivity**   | Theorem   | Path–Connectivity Theorem   | Standard                   | A graph is connected iff every pair of vertices is joined by a path                 |
| **Ch. 2 – Graph Isomorphism / Topology**              | Theorem   | Sperner’s Lemma             | Emanuel Sperner            | Guarantees existence of a fully labeled simplex                                     |
| **Ch. 2 – Graph Isomorphism / Topology**              | Theorem   | Brouwer Fixed Point Theorem | L. E. J. Brouwer           | Every continuous map from a compact convex set to itself has a fixed point          |
| **Ch. 3 – Trees / Enumeration**                       | Theorem   | Cayley’s Formula            | Arthur Cayley              | Number of labeled trees on $(n)$ vertices is $(n^{n-2})$                              |
| **Ch. 3 – Trees / Enumeration**                       | Algorithm | Prüfer Code                 | Heinz Prüfer               | Bijective encoding of labeled trees; constructive proof of Cayley’s formula         |
| **Ch. 3 – Connectivity / Traversals**                 | Algorithm | Breadth-First Search (BFS)  | E. F. Moore                | Explores graph level-by-level; shortest paths in unweighted graphs                  |
| **Ch. 3 – Connectivity / Traversals**                 | Algorithm | Depth-First Search (DFS)    | C. A. R. Hoare / R. Tarjan | Recursive exploration; cycle and component detection                                |
| **Ch. 3 – Trees / Connectivity**                      | Theorem   | Tree Characterization       | Standard                   | A graph is a tree iff it is connected and has $(n-1)$ edges                           |
| **Ch. 4 – Eulerian Graphs / Circuit & Trail**         | Theorem   | Euler’s Theorem (Circuit)   | Leonhard Euler             | A connected graph has an Eulerian circuit iff all vertex degrees are even           |
| **Ch. 4 – Eulerian Graphs / Circuit & Trail**         | Theorem   | Euler’s Theorem (Trail)     | Leonhard Euler             | A connected graph has an Eulerian trail iff exactly 0 or 2 vertices have odd degree |
| **Ch. 4 – Eulerian Graphs / Algorithms**              | Algorithm | Fleury’s Algorithm          | H. Fleury                  | Constructs an Eulerian trail by avoiding bridges when possible                      |
| **Ch. 4 – Eulerian Graphs / Algorithms**              | Algorithm | Hierholzer’s Algorithm      | Carl Hierholzer            | Efficient construction of an Eulerian circuit via cycle decomposition               |
| **Ch. 4 – Cycle Structure**                           | Theorem   | Cycle Decomposition Theorem | Euler / Standard           | Every even-degree graph decomposes into edge-disjoint cycles                        |
| **Ch. 4 – Hamiltonian Graphs / Concept**              | Concept   | Hamiltonian Path / Cycle    | W. R. Hamilton             | Path or cycle visiting every vertex exactly once                                    |
| **Ch. 4 – Hamiltonian Graphs / Degree Conditions**    | Theorem   | Dirac’s Theorem             | G. A. Dirac                | If $(n\ge3)$ and $(\deg(v)\ge n/2)$ for all $(v)$, the graph is Hamiltonian            |
| **Ch. 4 – Hamiltonian Graphs / Degree Conditions**    | Theorem   | Ore’s Theorem               | Øystein Ore                | If $(\deg(u) + \deg(v) \ge n)$ for all nonadjacent $(u,v)$, the graph is Hamiltonian    |
| **Ch. 4 – Hamiltonian Graphs / Degree Conditions**    | Theorem   | Chvátal’s Theorem           | Václav Chvátal             | Hamiltonicity characterized via degree-sequence closure                             |
| **Ch. 4 – Shortest Paths / Weighted Graphs**          | Algorithm | Dijkstra’s Algorithm        | Edsger W. Dijkstra         | Computes shortest paths in weighted graphs with nonnegative weights                 |
| **Ch. 4 – Spanning Trees / Optimization**             | Algorithm | Prim’s Algorithm            | Robert C. Prim             | Greedy construction of a minimum spanning tree                                      |
| **Ch. 4 – Spanning Trees / Optimization**             | Algorithm | Kruskal’s Algorithm         | Joseph Kruskal             | Builds a minimum spanning tree by adding edges of increasing weight                 |

