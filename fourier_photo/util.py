import torch
import plotly
import plotly.graph_objects as go



def plot_fourier(positive_radii, negative_radii, positive_offsets, negative_offsets, mean_position, num_time_points: int = 1000, fig = None):
    N = len(positive_radii)
    assert len(negative_radii) == N
    assert len(positive_offsets) == N
    assert len(negative_offsets) == N

    freq = torch.arange(N, dtype=float)+1.
    t = torch.linspace(0,1, num_time_points)
    mx = mean_position[0]
    my = mean_position[1]
    px = torch.sum(positive_radii*torch.cos(2*torch.pi*torch.outer(t, freq)+positive_offsets), axis = 1)
    py = torch.sum(positive_radii*torch.sin(2*torch.pi*torch.outer(t, freq)+positive_offsets), axis = 1)
    nx = torch.sum(negative_radii*torch.cos(-2*torch.pi*torch.outer(t, freq)+negative_offsets), axis = 1)
    ny = torch.sum(negative_radii*torch.sin(-2*torch.pi*torch.outer(t, freq)+negative_offsets), axis = 1)

    x = px+nx+mx
    y = py+ny+my
    if fig is None:
        fig = go.Figure()
    fig.add_trace(go.Scatter(x = x, y = y))
    return fig
