# Data Structures and Algorithms Repository

This repository contains Python implementations of fundamental data structures and algorithms, along with solutions to selected LeetCode problems. The code is organized by category for ease of access and extensibility. Each folder is dedicated to a specific topic and can be expanded with additional implementations.

## Repository Structure

- **`algorithms/`**: Contains implementations of various algorithms. Organized by categories such as graph algorithms (e.g., BFS, DFS) and sorting algorithms (e.g., bubble sort).
- **`data_structures/`**: Includes custom implementations of foundational data structures like stacks, queues, and graphs. Also contains comparisons between different implementations.
- **`leetcode_problems/`**: Solutions to selected LeetCode problems, each implemented in standalone files for clarity and testing.
- **`tests/`**: Contains pytest-based tests for algorithms, data structures, and LeetCode problems. Organized to mirror the main structure of the code files, allowing each solution to have corresponding unit tests.

## Running Tests

All tests can be run from the root directory using:
```bash
python -m pytest
```
## Pre-commit Hook and GitHub Actions

This repository uses a pre-commit hook that runs linting and tests automatically before every commit. To run these checks manually, use:
```bash
pre-commit run --all-files
```
Additionally, a GitHub Action is set up to execute linting and tests on the server after each push, ensuring code consistency and reliability.

## Contributing

Feel free to expand on the current implementations or add new data structures, algorithms, and problem solutions. Contributions should include corresponding tests in the `tests/` folder for validation.
