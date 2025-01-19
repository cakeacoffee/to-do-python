# database documentation
## Research Questions
* What type of database?
    * SQL
    * NOSQL
    * Graph
* Database structure/Design

## Database Types
* 👀 Looking for something lightweight and that is suitable for the to do structure (only saving text and boolean, lists do not need to link)

### 1. Relational Databases (SQL)
#### Description:
Relational databases store structured data in tables with predefined schemas. Data is organised into rows and columns, and relationships between data are managed through keys (primary and foreign keys).

#### Examples:
SQLite
MySQL
PostgreSQL
Microsoft SQL Server

#### Advantages:
Structured and predictable data organisation.
Strong support for relationships using foreign keys.
Mature ecosystems with many tools and libraries.
Standardised query language (SQL).
Data integrity ensured through constraints (e.g., unique, not null).

#### Disadvantages:
Requires predefined schemas (less flexible for unstructured data).
Scaling horizontally is harder compared to NoSQL.
Complex for handling hierarchical or unstructured data.

### 2. NoSQL Databases
##### Description:
NoSQL databases handle unstructured, semi-structured, or hierarchical data. They are schema-less or have flexible schemas, offering scalability and high performance for specific use cases.

#### Types:
Document Stores: Store data as JSON-like documents (e.g., MongoDB, CouchDB).
Key-Value Stores: Simple key-value pairs (e.g., Redis, DynamoDB).
Column-Family Stores: Store data in columns for fast aggregation (e.g., Cassandra, HBase).
Graph Databases: Model data as nodes and edges for complex relationships (e.g., Neo4j)

#### Examples:
MongoDB (Document Store)
Redis (Key-Value Store)
Cassandra (Column-Family Store)
Neo4j (Graph Database)

#### Advantages:
Flexible schemas for dynamic or evolving data.
Optimised for specific data models and queries (e.g., JSON, graphs).
Easier to scale horizontally (distributed systems).
High performance for read and write-heavy workloads.

#### Disadvantages:
May lack ACID (atomicity, consistency, isolation, durability) properties.
Less standardisation compared to SQL (query languages vary).
Learning curve for specific NoSQL types.

### 3. Graph Databases
#### Description:
Graph databases store data as nodes (entities) and edges (relationships) to represent complex, interconnected data. They are ideal for scenarios like social networks, recommendation systems, and fraud detection.

#### Examples:
Neo4j
Amazon Neptune
ArangoDB

#### Advantages:
Natural representation of relationships.
Fast traversal of complex relationships (e.g., shortest path, recommendation systems).
Schema flexibility.
Rich query languages like Cypher (for Neo4j).

#### Disadvantages:
Less efficient for bulk operations and large-scale analytical queries.
Smaller ecosystem compared to relational databases.
Complexity in scaling for massive datasets.

### 4. In-Memory Databases
Description:
In-memory databases store all data in RAM for ultra-fast read and write operations. They are commonly used for caching, session storage, and real-time analytics.

#### Examples:
Redis
Memcached

#### Advantages:
Extremely fast data access due to RAM storage.
Suitable for low-latency, high-throughput applications.
Simple key-value models are easy to implement.

#### Disadvantages:

Data is volatile unless persistence is configured.
Limited storage size due to RAM dependency.
Not ideal for complex queries or large datasets.

### 5. Column-Family Databases
Description:
Column-family databases store data in a columnar format, enabling fast reads and writes for large datasets. They are often used in analytics and distributed systems.

#### Examples:
Apache Cassandra
HBase

#### Advantages:
Highly scalable for distributed systems.
Fast aggregation of large datasets.
Designed for high write throughput.

#### Disadvantages:
Limited support for complex queries and relationships.
Learning curve due to unique data model.
Requires careful design for optimal performance.

### Conclusion
SQL (SQLite)

**Why?**
- Perfect for small-scale projects with structured data (e.g., lists and tasks with relationships).
- Self-contained and requires no separate installation; runs directly in the Python environment.
- Supports simple schema designs (e.g., a Lists table and a Tasks table linked by a foreign key).
- Easy to migrate to more robust SQL databases (e.g., MySQL, PostgreSQL) in the future if needed.