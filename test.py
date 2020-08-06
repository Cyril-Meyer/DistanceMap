import time
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from distancemap import distance_map, distance_map_from_binary_matrix
import functions

BENCHMARK = False
EXAMPLE = True


def benchmark():
    # 1024 x 1024 with 10 points
    input = np.zeros((1024, 1024)).astype(np.bool)
    input[256, 256] = True
    input[256, 512] = True
    input[256, 768] = True
    input[512, 512] = True
    input[768, 768] = True
    input[0, 0] = True
    input[0, 200] = True
    input[900, 900] = True
    input[950, 900] = True
    input[1000, 0] = True

    # Create CPU load
    for i in range(50):
        distance_map_from_binary_matrix(input)

    time1 = time.time()
    for i in range(10):
        distance_map_from_binary_matrix(input)
    time2 = time.time()
    time_dmfbm_2d_1024_1024_10 = (time2 - time1)*1000

    points = np.argwhere(input)
    time1 = time.time()
    for i in range(10):
        distance_map(input.shape, points)
    time2 = time.time()
    time_dm_2d_1024_1024_10 = (time2 - time1)*1000

    # 1024 x 1024 with 5 points
    input = np.zeros((1024, 1024)).astype(np.bool)
    input[512, 512] = True
    input[768, 768] = True
    input[0, 200] = True
    input[900, 900] = True
    input[1000, 0] = True

    time1 = time.time()
    for i in range(10):
        distance_map_from_binary_matrix(input)
    time2 = time.time()
    time_dmfbm_2d_1024_1024_5 = (time2 - time1)*1000

    points = np.argwhere(input)
    time1 = time.time()
    for i in range(10):
        distance_map(input.shape, points)
    time2 = time.time()
    time_dm_2d_1024_1024_5 = (time2 - time1)*1000

    print(time_dmfbm_2d_1024_1024_10)
    print(time_dm_2d_1024_1024_10)
    print(time_dmfbm_2d_1024_1024_5)
    print(time_dm_2d_1024_1024_5)

    # 128 x 128 x 128 with 10 points
    time_dmfbm_3d_256_256_256_25 = 0
    time_dm_3d_256_256_256_25 = 0
    for i in range(10):
        input = np.zeros((128, 128, 128)).astype(np.bool)
        for j in range(10):
            x = random.randint(0, 128-1)
            y = random.randint(0, 128-1)
            z = random.randint(0, 128-1)
            input[x, y, z] = True
        points = np.argwhere(input)

        time1 = time.time()
        distance_map_from_binary_matrix(input)
        time2 = time.time()
        time_dmfbm_3d_256_256_256_25 += (time2 - time1)*1000

        time1 = time.time()
        distance_map(input.shape, points)
        time2 = time.time()
        time_dm_3d_256_256_256_25 += (time2 - time1)*1000

    print(time_dmfbm_3d_256_256_256_25)
    print(time_dm_3d_256_256_256_25)


def example():
    input = np.zeros((1024, 1024)).astype(np.bool)
    input[256, 256] = True
    input[256, 512] = True
    input[256, 768] = True
    input[512, 512] = True
    input[768, 768] = True
    input[20, 20] = True
    input[20, 200] = True
    input[900, 900] = True
    input[950, 900] = True
    input[1000, 20] = True

    input_visible = input
    points = np.argwhere(input_visible)
    for p in points:
        input_visible[p[0]-15:p[0]+15, p[1]-15:p[1]+15] = True

    plt.figure(1)
    plt.subplot(231)
    plt.imshow(input_visible, cmap="Greys")
    plt.title("original (each square represent a single pixel)")
    plt.subplot(232)
    plt.imshow(distance_map_from_binary_matrix(input), cmap="Greys", vmin=0, vmax=255)
    plt.title("default")
    plt.subplot(233)
    plt.imshow(distance_map_from_binary_matrix(input, distance="manhattan"), cmap="Greys", vmin=0, vmax=255)
    plt.title("manhattan")
    plt.subplot(234)
    plt.imshow(distance_map_from_binary_matrix(input, alpha="square", omega=255.0), cmap="Greys", vmin=0, vmax=255)
    plt.title("alpha square")
    plt.subplot(235)
    functions.set_a(0.5)
    plt.imshow(distance_map_from_binary_matrix(input, alpha="linear"), cmap="Greys", vmin=0, vmax=255)
    plt.title("linear 0.5*x")
    plt.subplot(236)
    plt.imshow(distance_map_from_binary_matrix(input, distance="manhattan", alpha="linear", omega=100.0), cmap="Greys", vmin=0, vmax=255)
    plt.title("manhattan linear 0.5*x omega=100")
    plt.show()


    input = np.zeros((1024, 1024)).astype(np.bool)
    for i in range(10):
        x = random.randint(20, 1024-20)
        y = random.randint(20, 1024-20)
        input[x, y] = True

    input_visible = input
    points = np.argwhere(input_visible)
    for p in points:
        input_visible[p[0]-15:p[0]+15, p[1]-15:p[1]+15] = True

    plt.figure(1)
    plt.subplot(231)
    plt.imshow(input_visible, cmap="Greys")
    plt.title("original (each square represent a single pixel)")
    plt.subplot(232)
    plt.imshow(distance_map_from_binary_matrix(input), cmap="Greys", vmin=0, vmax=255)
    plt.title("default")
    plt.subplot(233)
    plt.imshow(distance_map_from_binary_matrix(input, distance="manhattan"), cmap="Greys", vmin=0, vmax=255)
    plt.title("manhattan")
    plt.subplot(234)
    plt.imshow(distance_map_from_binary_matrix(input, alpha="square", omega=255.0), cmap="Greys", vmin=0, vmax=255)
    plt.title("alpha square")
    plt.subplot(235)
    functions.set_a(0.5)
    plt.imshow(distance_map_from_binary_matrix(input, alpha="linear"), cmap="Greys", vmin=0, vmax=255)
    plt.title("linear 0.5*x")
    plt.subplot(236)
    plt.imshow(distance_map_from_binary_matrix(input, distance="manhattan", alpha="linear", omega=100.0), cmap="Greys", vmin=0, vmax=255)
    plt.title("manhattan linear 0.5*x omega=100")
    plt.show()


if BENCHMARK:
    benchmark()

if EXAMPLE:
    example()
