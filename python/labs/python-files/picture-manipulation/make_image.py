import matplotlib.pyplot as plt
import numpy as np
import PIL


def make_diag(rows, columns, stripe_width):
    img = PIL.Image.new('RGB', (columns, rows))
    image = np.array(img)

    for row in range(rows):
        for column in range(columns):
            
            if (row+column) // stripe_width % 2 == 0:  # slanted stripes
                # (r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                # Even stripe
                image[row][column] = [255, 255, 153]
            else:
                # Odd stripe
                image[row][column] = [0, 0, 102]
    return image


def make_horizontal(rows, columns, stripe_width):
    img = PIL.Image.new('RGB', (columns, rows))
    image = np.array(img)

    for row in range(rows):
        for column in range(columns):
            if row // stripe_width % 2 == 0:
                # Even stripe
                image[row][column] = [255, 255, 153]
            else:
                # Odd stripe
                image[row][column] = [0, 0, 102]
    return image


def make_vertical(rows, columns, stripe_width):
    img = PIL.Image.new('RGB', (columns, rows))
    image = np.array(img)

    for row in range(rows):
        for column in range(columns):
            if column // stripe_width % 2 == 0:
                # Even stripe
                image[row][column] = [255, 255, 153]
            else:
                # Odd stripe
                image[row][column] = [0, 0, 102]
    return image


if __name__ == "__main__":
    image1 = make_diag(100, 100, 20)
    image2 = make_horizontal(100, 100, 20)
    image3 = make_vertical(100, 100, 20)
    
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(image1)
    ax[1].imshow(image2)
    ax[2].imshow(image3)
    plt.ioff()
    plt.show()