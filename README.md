# python_toolkits
Scenario: Building a Smart Data Aggregator
You have been hired by a startup working on a Smart Data Aggregator tool. The goal
of the tool is to manage and analyze large sets of user data efficiently. The startup
focuses on different types of collections (List, Tuple, Set, and Dictionary) to handle
various tasks such as real-time analytics, tracking data, and reporting. Your task is to
develop different modules for the aggregator using Python.

---

# User and Transaction Data Utilities

A collection of Python functions designed to perform common data operations on user information, transaction logs, and feedback data. The repository is divided into four sections, each handling different aspects of data manipulation and processing.

## Part 1: User Data Functions

This section contains functions for filtering and sorting user data, as well as identifying duplicates.

- **`filter_users(lst)`**: Filters users by age (> 30) and location (USA, Canada), returning a list of user names.
- **`top_10_oldest(lst)`**: Sorts users by age in descending order and returns the top 10 oldest users.
- **`find_duplicates(lst)`**: Identifies duplicate user names in the list.

## Part 2: Transaction Data Functions

Functions that work with transaction data, including finding unique users, identifying the largest transaction, and splitting data into separate lists.

- **`unique_users(trans)`**: Returns the count of unique user IDs from transaction data.
- **`max_transaction(trans)`**: Identifies the transaction with the highest amount.
- **`split_ids(trans)`**: Splits transactions into two lists: transaction IDs and user IDs.

## Part 3: Set Operations

Functions designed for working with sets, useful for comparing user visit data.

- **`both_visited(A, B)`**: Finds common elements (e.g., users who visited both sites).
- **`either_both(A, C)`**: Finds elements that belong to either of the sets or both but excludes common elements.
- **`update_set(A, new_ids)`**: Adds new elements to set `A`.
- **`remove_set(B, ids)`**: Removes specified elements from set `B`.

## Part 4: Feedback Processing

Functions for processing feedback data stored in dictionaries, including filtering by rating, selecting top feedback, and combining multiple feedback sources.

- **`filter_feedback(dic)`**: Filters feedback with ratings >= 4.
- **`top_5_feedback(dic)`**: Retrieves the top 5 feedback entries by rating.
- **`combine_feedback(dic_list)`**: Combines feedback from multiple dictionaries, updating ratings and appending comments where applicable.
- **`dict_comp(dic)`**: Creates a dictionary comprehension for feedback with ratings > 3.

## Usage

Each function can be used independently for data processing tasks. Simply pass the required data format (list, set, or dictionary) as per the function’s requirements.