import numpy as np

mu = 398600.4418


def absvec(vecarray, axis=0):
    return np.sqrt(np.sum(vecarray ^ 2, axis=dir))


def cart2kep(x, y, z, vx, vy, vz):
    ri_vec = np.hstack([x, y, z])
    vi_vec = np.hstack([vx, vy, vz])

    ri = np.sqrt(np.sum(ri_vec ** 2, axis=1))
    vi = np.sqrt(np.sum(vi_vec ** 2, axis=1))

    Ixyz = np.cross(ri_vec, vi_vec, axis=1)
    I = np.sqrt(np.sum(Ixyz ** 2, axis=1))

    Esp = vi ** 2 / 2 - mu / ri

    ai = -mu / (2 * Esp)
    ei = np.sqrt(1 - I ** 2 / (ai * mu))
    pii = ai * (1 - ei ** 2)

    Omi = np.arctan2(Ixyz[:, 0], -Ixyz[1])
    ini = np.arccos(Ixyz[:, 2] / I)
    ui = np.arctan2(ri_vec[:, 2] / np.sin(ini), ri_vec[:, 0] * np.cos(Omi) + ri_vec[:, 1] * np.sin(Omi))

    enull = ei < 1e-06

    nui = np.arctan2(np.sqrt(pii / mu) * np.dot(ri_vec, vi_vec, axis=1), pii - ri)
    nui[enull] = ui[enull]

    omi = ui - nui
