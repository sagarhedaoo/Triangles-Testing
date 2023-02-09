# Triangles Testing 

[![<sagarhedaoo>](https://circleci.com/gh/<sagarhedaoo>/<Triangles-Testing>.svg?style=svg)](https://app.circleci.com/pipelines/github/<sagarhedaoo>/<Triangles-Tesing>?branch=main&filter=all)

Repository for HW 02-A

Deliverable 1 Intial Testing with buggy classifyTriangle():


| Test ID | Input         | Expected Results | Actual Result | Pass or Fail |
| ------- | ------------- | ---------------- | ------------- | ------------ |
| 1       | 1, 1, 1       | Equilateral      | InvalidInput  | Fail         |
| 2       | 3, 4, 5       | Right            | InvalidInput  | Fail         |
| 3       | 5, 3, 4       | Right            | InvalidInput  | Fail         |
| 4       | 23, 24, 7     | Scalene          | InvalidInput  | Fail         |
| 5       | 400, 400, 400 | InvalidInput     | InvalidInput  | Pass         |
| 6       | a, b, d       | InvalidInput     | Error         | Fail         |
| 7       | -4, -6, 0     | InvalidInput     | InvalidInput  | Pass         |
| 8       | 0, 0, 0       | InvalidInput     | InvalidInput  | Pass         |



Deliverable 5 Updated Logic for classifyTriangle():


| Test ID | Input         | Expected Results | Actual Result | Pass or Fail |
| ------- | ------------- | ---------------- | ------------- | ------------ |
| 1       | 1, 1, 1       | Equilateral      | Equilateral   | Pass         |
| 2       | 3, 4, 5       | Right            | Right         | Pass         |
| 3       | 5, 3, 4       | Right            | Right         | Pass         |
| 4       | 23, 24, 7     | Scalene          | Scalene       | Pass         |
| 5       | 400, 400, 400 | InvalidInput     | InvalidInput  | Pass         |
| 6       | a, b, d       | InvalidInput     | InvalidInput  | Pass         |
| 7       | -4, -6, 0     | InvalidInput     | InvalidInput  | Pass         |
| 8       | 0, 0, 0       | InvalidInput     | InvalidInput  | Pass         |
