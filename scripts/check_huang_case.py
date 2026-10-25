#!/usr/bin/env python3
"""Exact finite diagnostics for the Huang case; not an attribution evaluator."""
import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'data/cases/huang-sensitivity-checks.json'


def signed_cube(n):
    if n == 1:
        return [[0, 1], [1, 0]]
    previous = signed_cube(n - 1)
    size = len(previous)
    return [
        [previous[i][j] for j in range(size)]
        + [int(i == j) for j in range(size)]
        for i in range(size)
    ] + [
        [int(i == j) for j in range(size)]
        + [-previous[i][j] for j in range(size)]
        for i in range(size)
    ]


def square(matrix):
    size = len(matrix)
    return [[sum(matrix[i][k] * matrix[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]


def adjacent(x, y):
    return (x ^ y).bit_count() == 1


def max_degree(vertices):
    return max((sum(adjacent(x, y) for y in vertices) for x in vertices), default=0)


def sensitivity(values, n):
    return max(sum(values[x] != values[x ^ (1 << i)] for i in range(n))
               for x in range(1 << n))


def walsh(values, n):
    # Integer numerators, avoiding floating point and normalization by 2^n.
    return [sum(values[x] * (-1 if (x & mask).bit_count() % 2 else 1)
                for x in range(1 << n)) for mask in range(1 << n)]


def checks():
    matrices = []
    for n in range(1, 7):
        matrix = signed_cube(n)
        size = 1 << n
        assert len(matrix) == size and all(len(row) == size for row in matrix)
        assert all(matrix[i][j] == matrix[j][i] for i in range(size) for j in range(size))
        assert all(abs(matrix[i][j]) == int(adjacent(i, j))
                   for i in range(size) for j in range(size))
        assert all(matrix[i][i] == 0 for i in range(size))
        product = square(matrix)
        assert all(product[i][j] == (n if i == j else 0)
                   for i in range(size) for j in range(size))
        matrices.append({'n': n, 'dimension': size, 'support_symmetry_and_square': 'pass'})

    subgraphs = []
    for n in range(1, 5):
        size = 1 << n
        threshold = size // 2 + 1
        degrees = Counter(max_degree(vertices)
                          for vertices in combinations(range(size), threshold))
        assert all(degree * degree >= n for degree in degrees)
        subgraphs.append({'n': n, 'vertices': threshold, 'subsets_checked': sum(degrees.values()),
                          'minimum_maximum_degree': min(degrees)})

    functions = []
    for n in range(4):
        count, nonconstant = 0, 0
        for table in range(1 << (1 << n)):
            values = [1 if (table >> x) & 1 else -1 for x in range(1 << n)]
            coefficients = walsh(values, n)
            degree = max(mask.bit_count() for mask, value in enumerate(coefficients) if value)
            s = sensitivity(values, n)
            assert s * s >= degree
            count += 1
            if degree == 0:
                continue
            nonconstant += 1
            mask = next(mask for mask, value in enumerate(coefficients)
                        if value and mask.bit_count() == degree)
            coordinates = [i for i in range(n) if (mask >> i) & 1]
            restricted = [values[sum(((x >> j) & 1) << i for j, i in enumerate(coordinates))]
                          for x in range(1 << degree)]
            assert walsh(restricted, degree)[-1] == coefficients[mask] // (1 << (n - degree))
            restricted_s = sensitivity(restricted, degree)
            assert restricted_s <= s
            transformed = [value * (-1 if x.bit_count() % 2 else 1)
                           for x, value in enumerate(restricted)]
            assert sum(transformed) != 0
            majority = 1 if sum(transformed) > 0 else -1
            vertices = [x for x, value in enumerate(transformed) if value == majority]
            assert len(vertices) > (1 << degree) // 2
            assert all(restricted[x] != restricted[y]
                       for x in vertices for y in vertices if adjacent(x, y))
            assert degree <= max_degree(vertices) ** 2 <= restricted_s ** 2
        functions.append({'n': n, 'truth_tables_checked': count,
                          'nonconstant_reductions_checked': nonconstant})

    # Actual graph counterexamples for the relaxed threshold.
    boundary = []
    for n in range(1, 7):
        even = [x for x in range(1 << n) if x.bit_count() % 2 == 0]
        assert len(even) == (1 << n) // 2 and max_degree(even) == 0
        boundary.append({'n': n, 'vertices': len(even), 'maximum_degree': 0})

    unsigned = [[int(adjacent(i, j)) for j in range(4)] for i in range(4)]
    unsigned_squared = square(unsigned)
    assert unsigned_squared[0][3] == 2
    kernel_vector = [1, 0, 0, -1]
    assert all(sum(row[j] * kernel_vector[j] for j in range(4)) == 0 for row in unsigned)
    # This is a numerical countermodel to an invalid inference, not a hypercube graph.
    n, parameter, delta = 4, 3, 1
    assert delta <= parameter and parameter * parameter >= n and delta * delta < n

    return {
        'purpose': 'Exact finite mathematical diagnostics; no model or historical novelty evaluation.',
        'method': 'Python standard library; integer arithmetic and exhaustive enumeration.',
        'signed_matrices': matrices,
        'threshold_subgraphs': subgraphs,
        'boolean_functions': functions,
        'half_threshold_counterexamples': boundary,
        'negative_controls': {
            'unsigned_cube_n2_square_off_diagonal': unsigned_squared[0][3],
            'unsigned_cube_n2_nonzero_kernel_vector': kernel_vector,
            'invalid_parameter_inference_numerical_countermodel': {
                'n': n, 'parameter_bound': parameter, 'hypothetical_delta': delta,
                'interpretation': 'Only a countermodel to the two numerical premises; not a graph.'
            }
        },
        'limits': ['No general theorem is established by finite enumeration.',
                   'No Lean compilation or independent expert review was performed.',
                   'No attribution pipeline, model accuracy or priority claim was evaluated.']
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = checks()
    content = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.check:
        assert OUTPUT.read_text() == content, f'Regenerate {OUTPUT.relative_to(ROOT)}'
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(content)
    print(f'Checked 6 signed matrices, {sum(r["subsets_checked"] for r in result["threshold_subgraphs"])} '
          f'threshold subgraphs, {sum(r["truth_tables_checked"] for r in result["boolean_functions"])} '
          'Boolean functions and negative controls. No attribution performance measured.')


if __name__ == '__main__':
    main()
