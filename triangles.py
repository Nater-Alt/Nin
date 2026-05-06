# Copyright TU Wien (2022) - EVC: Task2
# Institute of Computer Graphics and Algorithms.

import numpy as np


def define_triangle() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Defines a triangle. The points are determined by your
    matriculation number - see task description.

    Returns:
        A tuple (P1, P2, P3), where
          - P1: A vector with 3 elements. Shape: (3,).
          - P2: A vector with 3 elements. Shape: (3,).
          - P3: A vector with 3 elements. Shape: (3,).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1 = np.array([1 + 4, -(1 + 1), -(1 + 1)], dtype=float)
    P2 = np.array([-(1 + 2), -(1 + 2), 1 + 3], dtype=float)
    P3 = np.array([-(1 + 2), 1 + 9, -(1 + 2)], dtype=float)

    ### END STUDENT CODE

    return P1, P2, P3


def define_triangle_edges(
    P1: np.ndarray, P2: np.ndarray, P3: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculates the edges of the triangle by defining the vectors
    P1P2, P2P3, P3P1.

    Args:
        P1: A vector with 3 elements. Shape: (3,).
        P2: A vector with 3 elements. Shape: (3,).
        P3: A vector with 3 elements. Shape: (3,).

    Returns:
        A tuple (P1P2, P2P3, P3P1), where
          - P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
          - P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
          - P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1P2 = P2 - P1
    P2P3 = P3 - P2
    P3P1 = P1 - P3

    ### END STUDENT CODE

    return P1P2, P2P3, P3P1


def compute_lengths(
    P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray
) -> list[float]:
    """
    Computes the lengths of the triangle's edges given the vertices.

    Args:
        P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
        P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
        P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).

    Returns:
        A list with the lengths of the edges P1P2, P2P3, P3P1.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    norms = [
        np.sqrt(P1P2[0]**2 + P1P2[1]**2 + P1P2[2]**2),
        np.sqrt(P2P3[0]**2 + P2P3[1]**2 + P2P3[2]**2),
        np.sqrt(P3P1[0]**2 + P3P1[1]**2 + P3P1[2]**2)
    ]

    ### END STUDENT CODE

    return norms


def compute_normal_vector(
    P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculates the normal vector as well as the normal vector with length = 1.

    Args:
        P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
        P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
        P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).

    Returns:
        A tuple (n, n_normalized), where
          - n: A vector with 3 elements, defining the normal vector of the triangle.
            Shape: (3,).
          - n_normalized: A vector with 3 elements, defining the normalized normal vector.
            Shape: (3,).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    n = np.cross(P1P2, P2P3)
    n_normalized = n / np.linalg.norm(n)

    ### END STUDENT CODE

    return n, n_normalized


def compute_triangle_area(n: np.ndarray) -> float:
    """
    Returns the area of the triangle given its normal vector.

    Args:
        n: A vector with 3 elements, defining the normal vector of the triangle. Shape: (3,).

    Returns:
        The area of the triangle.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    area = np.linalg.norm(n) / 2.0

    ### END STUDENT CODE

    return area


def compute_angles(
    P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray
) -> tuple[float, float, float]:
    """
    Computes the angles of the triangle given its vertices. The angles should be
    returned in degrees.

    Args:
        P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
        P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
        P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).

    Returns:
        A tuple (alpha, beta, gamma), where
          - alpha: The angle at vertex P1.
          - beta: The angle at vertex P2.
          - gamma: The angle at vertex P3.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    cos_alpha = np.dot(P1P2, -P3P1) / (np.linalg.norm(P1P2) * np.linalg.norm(P3P1))
    alpha = np.degrees(np.arccos(cos_alpha))
 
    cos_beta = np.dot(P2P3, -P1P2) / (np.linalg.norm(P2P3) * np.linalg.norm(P1P2))
    beta = np.degrees(np.arccos(cos_beta))
 
    cos_gamma = np.dot(P3P1, -P2P3) / (np.linalg.norm(P3P1) * np.linalg.norm(P2P3))
    gamma = np.degrees(np.arccos(cos_gamma))

    ### END STUDENT CODE

    return alpha, beta, gamma
