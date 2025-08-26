# Global settings for font and color palettes
import matplotlib as mpl

# Set global font size and style for plots
mpl.rcParams['font.size'] = 10
mpl.rcParams['font.family'] = 'serif'

# Set global color map
DEFAULT_CMAP = "coolwarm"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_mm(mm_array, output_file=None, off_diag_limits=(-0.1, 0.1), figsize=(6, 6), print_mean=False):
    """
    Plot Mueller matrices (MMs) with formatted text and color palettes suitable for papers.

    Parameters:
        mm_array (numpy.ndarray): A 4x4xXxY array representing Mueller matrices for each pixel.
        output_file (str, optional): Path to save the plot. If None, the plot is shown interactively.
        off_diag_limits (tuple, optional): Limits for off-diagonal elements. Defaults to (-0.1, 0.1).

    Raises:
        ValueError: If the input array shape is not (4, 4, X, Y).
    """
    if mm_array.shape[:2] != (4, 4):
        raise ValueError("The input array must have a shape of (4, 4, X, Y).")

    fig, axes = plt.subplots(4, 4, figsize=figsize)
    cmap = plt.get_cmap(DEFAULT_CMAP)

    for idx, ax in enumerate(axes.ravel()):
        i, j = divmod(idx, 4)
        data = mm_array[i, j, :, :]
        if i == j:
            im = ax.imshow(data, cmap=cmap, vmin=-1, vmax=1)
        else:
            im = ax.imshow(data, cmap=cmap, vmin=off_diag_limits[0], vmax=off_diag_limits[1])
        # ax.set_title(f"m{i+1}{j+1}", fontsize=10)
        ax.axis("off")

        if print_mean:
            mean_value = np.mean(data)
            text_color = "white" if abs(mean_value) > 0.5 else "black"
            ax.text(0.5, 0.5, f"{mean_value:.3f}", color=text_color, fontsize=10,
                    ha="center", va="center", transform=ax.transAxes)

    cbar = fig.colorbar(im, ax=axes, orientation="horizontal", fraction=0.02, pad=0.1)
    cbar.set_label("MM Value", fontsize=12)

    # fig.suptitle("Mueller Matrices", fontsize=16)

    if output_file:
        fig.savefig(output_file, dpi=300, bbox_inches="tight")
    else:
        fig.show()