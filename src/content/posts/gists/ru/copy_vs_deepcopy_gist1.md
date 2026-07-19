---
title: 'copy numbers'
pubDate: 2026-07-03 17:34:49
description: "copy numbers"
tags: ["python", "copy", "deepcopy"]
---
numbers = [[1, 2], [3, 4]]

copy = numbers.copy()

copy[0].append(99)

print(numbers)
