import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path


def plot_utilities_2d(u,
                      xlims,
                      ylims,
                      actions,
                      domain,
                      title="",
                      cmap="Spectral",
                      save=False,
                      save_dir="",
                      filename="",
                      show_plot=True):
    xmin, xmax = xlims
    ymin, ymax = ylims
    num_actions = len(actions)
    xlabel = 'Agent 1 actions'
    ylabel = 'Agent 2 actions'

    u1_vals = u[0](domain)
    u1_reshaped = np.transpose(
        np.reshape(u1_vals, [num_actions, num_actions]))
    u2_vals = u[1](domain)
    u2_reshaped = np.transpose(
        np.reshape(u2_vals, [num_actions, num_actions]))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title, size=20)
    fig.set_size_inches(8, 4)
    fig.set_dpi(200)

    im1 = ax1.imshow(u1_reshaped,
                     interpolation='nearest',
                     extent=(xmin, xmax, ymin, ymax),
                     origin='lower',
                     cmap=cmap,
                     aspect=(xmax - xmin) / (ymax - ymin))
    ax1.set_title("Agent 1 utility", size=16)
    ax1.set_xlabel(xlabel, size=12)
    ax1.set_ylabel(ylabel, size=12)
    fig.colorbar(im1, ax=ax1)

    im2 = ax2.imshow(u2_reshaped,
                     interpolation='nearest',
                     extent=(xmin, xmax, ymin, ymax),
                     origin='lower',
                     cmap=cmap,
                     aspect=(xmax - xmin) / (ymax - ymin))
    ax2.set_title("Agent 2 utility", size=16)
    ax2.set_xlabel(xlabel, size=12)
    ax2.set_ylabel(ylabel, size=12)
    fig.colorbar(im2, ax=ax2)

    fig.tight_layout()
    if save:
        Path(save_dir).mkdir(parents=True, exist_ok=True)
        plt.savefig(save_dir + filename, bbox_inches='tight')
    if show_plot:
        plt.show()


def plot_func_2d(f,
                 xlims,
                 ylims,
                 actions,
                 title="",
                 cmap="Spectral",
                 save=False,
                 save_dir="",
                 filename="",
                 show_plot=True):
    xmin, xmax = xlims
    ymin, ymax = ylims
    num_actions = len(actions)
    xlabel = 'Agent 1 actions'
    ylabel = 'Agent 2 actions'

    f_reshaped = np.transpose(
        np.reshape(f, [num_actions, num_actions]))  # f needs to have shape (num_actions ** 2) or (num_actions ** 2, 1)

    fig, (ax1) = plt.subplots(1, 1)
    fig.suptitle(title, size=12)
    fig.set_size_inches(6, 3)
    fig.set_dpi(200)

    im1 = ax1.imshow(f_reshaped,
                     interpolation='nearest',
                     extent=(xmin, xmax, ymin, ymax),
                     origin='lower',
                     cmap=cmap,
                     aspect=(xmax - xmin) / (ymax - ymin))
    ax1.set_xlabel(xlabel, size=8)
    ax1.set_ylabel(ylabel, size=8)
    fig.colorbar(im1, ax=ax1)

    fig.tight_layout()
    if save:
        Path(save_dir).mkdir(parents=True, exist_ok=True)
        plt.savefig(save_dir + filename, bbox_inches='tight')
    if show_plot:
        plt.show()


def plot_models_2d(models,
                   xlims,
                   ylims,
                   actions,
                   domain,
                   X=None,
                   title="",
                   cmap="Spectral",
                   save=False,
                   save_dir="",
                   filename="",
                   show_plot=True):
    xmin, xmax = xlims
    ymin, ymax = ylims
    num_actions = len(actions)
    xlabel = 'Agent 1 actions'
    ylabel = 'Agent 2 actions'

    g1_mean, g1_var = models[0].predict_f(domain)
    g1_mean_reshaped = np.transpose(
        np.reshape(g1_mean, [num_actions, num_actions]))
    g1_var_reshaped = np.transpose(
        np.reshape(g1_var, [num_actions, num_actions]))
    g2_mean, g2_var = models[1].predict_f(domain)
    g2_mean_reshaped = np.transpose(
        np.reshape(g2_mean, [num_actions, num_actions]))
    g2_var_reshaped = np.transpose(
        np.reshape(g2_var, [num_actions, num_actions]))

    fig, axs = plt.subplots(2, 2)
    fig.suptitle(title, size=10)
    fig.set_size_inches(5, 4)
    fig.set_dpi(200)

    offset = (1 / num_actions) / 2
    for i in range(2):
        for j in range(2):
            if i == 0:
                if j == 0:
                    f = g1_mean_reshaped
                    title = "Agent 1 GP mean"
                elif j == 1:
                    f = g2_mean_reshaped
                    title = "Agent 2 GP mean"
            elif i == 1:
                if j == 0:
                    f = g1_var_reshaped
                    title = "Agent 1 GP variance"
                elif j == 1:
                    f = g2_var_reshaped
                    title = "Agent 2 GP variance"
            ax = axs[i, j]
            im = ax.imshow(f,
                           interpolation='None',
                           extent=(xmin - offset, xmax + offset, ymin - offset, ymax + offset),
                           origin='lower',
                           cmap=cmap,
                           aspect=(xmax - xmin) / (ymax - ymin))
            if X is not None:
                ax.plot(X[:, 0], X[:, 1], 'x', mew=1, c='black')
            ax.set_title(title, size=8)
            ax.set_xlabel(xlabel, size=8)
            ax.set_ylabel(ylabel, size=8)
            fig.colorbar(im, ax=ax)

    fig.tight_layout()
    if save:
        Path(save_dir).mkdir(parents=True, exist_ok=True)
        plt.savefig(save_dir + filename, bbox_inches='tight')
    if show_plot:
        plt.show()
