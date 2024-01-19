# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.animation as animation
# import imageio

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# def init():
#     ax.set_xlim(-1, 1)
#     ax.set_ylim(-1, 1)
#     ax.set_zlim(-1, 1)
#     return fig,

# def animate(i):
#     ax.clear()
#     ax.set_xlim(-1, 1)
#     ax.set_ylim(-1, 1)
#     ax.set_zlim(-1, 1)

#     theta = i * 2*np.pi / 100
#     x = [np.cos(theta), np.cos(theta + 2*np.pi/3), np.cos(theta + 4*np.pi/3), np.cos(theta)]
#     y = [np.sin(theta), np.sin(theta + 2*np.pi/3), np.sin(theta + 4*np.pi/3), np.sin(theta)]
#     z = [0, 0, 0, 0]

#     ax.plot(x, y, z, color='b')

#     return fig,

# ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

# # Save animation frames as individual images
# with imageio.get_writer('C:/Users/Admin/Documents/MCTest/examples/Matrix/modules/convert video/rotating_triangle.mp4', fps=30) as writer:
#     for i in range(100):
#         animate(i)
#         fig.canvas.draw()
#         image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
#         image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
#         writer.append_data(image)


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import imageio

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    return fig,

def animate(i):
    ax.clear()  # Clear the previous plot
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    theta = i * 2*np.pi / 100
    x = np.array([np.cos(theta), np.cos(theta + 2*np.pi/3), np.cos(theta + 4*np.pi/3), np.cos(theta)])
    y = np.array([np.sin(theta), np.sin(theta + 2*np.pi/3), np.sin(theta + 4*np.pi/3), np.sin(theta)])
    z = np.array([0, 0, 0, 0])

    ax.plot(x, y, z, color='b')

    return (ax,)

ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

# Save animation frames as individual images
with imageio.get_writer('C:/Users/Admin/Documents/MCTest/examples/Matrix/modules/convert video/rotating_triangle.mp4', fps=30) as writer:
    for i in range(100):
        animate(i)
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        writer.append_data(image)