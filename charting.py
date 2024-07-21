Try this. Note up front:
lw = 2.0  # Line Weight 
ms = 7    # Marker Size 
mk = 'o'  # Marker
import matplotlib.pyplot as plt
# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10,20))

lw = 2.0  # Line Weight
ms = 7    # Marker Size
mk = 'o'  # Marker

# First subplot
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
deltascf = [0.0,    0.06,   0.33,   0.2,    0.23,   0.17,   0.09,   0.19,   0.208,  0.3   ]
s1       = [2.7292, 2.6788, 2.9796, 2.8057, 2.9038, 2.8720, 2.7708, 2.8238, 2.8796, 2.9294]
s2       = [3.5568, 3.5449, 3.2665, 3.3889, 3.4861, 3.8101, 3.5161, 3.4058, 3.5686, 3.8821]
s3       = [3.6151, 3.5490, 3.6890, 3.4140, 3.5913, 3.8525, 3.6620, 3.4340, 3.6218, 3.9911]
s4       = [3.8885, 3.8750, 3.9418, 3.8330, 3.6464, 3.9605, 3.9251, 3.8749, 3.7200, 4.2304]
s11      = [5.0501, 5.2439, 5.5008, 5.3996, 5.1980, 4.7968, 5.0084, 5.4019, 5.0356, 5.0478]
T1       = [1.6919, 1.7053, 1.9295, 1.8674, 1.8603, 1.8054, 1.6069, 1.8764, 1.8306, 1.8306]
T2       = [2.8341, 2.8040, 2.6895, 2.6366, 2.8003, 3.1215, 2.8674, 2.6117, 2.8931, 3.4198]
T3       = [3.0023, 2.9503, 3.03,   2.8232, 2.9999, 3.2762, 3.0530, 2.8000, 3.0799, 3.2189]
T5       = [3.8662, 3.8738, 4.0019, 3.8877, 3.7068, 3.6796, 3.9009, 3.8927, 3.6489, 4.5413]
T16      = [4.8615, 4.8814, 5.2926, 5.1716, 5.1903, 4.8794, 4.7777, 5.1811, 5.1042, 4.6314]
ax1.plot(x1, deltascf, linestyle='dashed', marker=mk, markersize=ms, color='orange',   alpha=1, linewidth=lw)
ax1.plot(x1, s1,       linestyle='dashed', marker=mk, markersize=ms, color='black',    alpha=1, linewidth=lw)
ax1.plot(x1, s2,       linestyle='dashed', marker=mk, markersize=ms, color='black',    alpha=1, linewidth=lw)
ax1.plot(x1, s3,       linestyle='dashed', marker=mk, markersize=ms, color='black',    alpha=1, linewidth=lw)
ax1.plot(x1, s4,       linestyle='dashed', marker=mk, markersize=ms, color='red',      alpha=1, linewidth=lw)
ax1.plot(x1, s11,      linestyle='dashed', marker=mk, markersize=ms, color='blue',     alpha=1, linewidth=lw)
ax1.plot(x1, T1,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray', alpha=1, linewidth=lw)
ax1.plot(x1, T2,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray', alpha=1, linewidth=lw)
ax1.plot(x1, T3,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray', alpha=1, linewidth=lw)
ax1.plot(x1, T5,       linestyle='dashed', marker=mk, markersize=ms, color='m',        alpha=1, linewidth=lw)
ax1.plot(x1, T16,      linestyle='dashed', marker=mk, markersize=ms, color='turquoise',         linewidth=lw)
ax1.set_xticks(x1)
x_labels = [r'$\mathrm{S_{0}}$',
            r'$\mathrm{S_{1}}$',
            r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
            r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
            r'$\mathrm{S}(\pi_{\mathrm{Ph}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
            r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{Ph}}^*)$',
            r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
            r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
            r'$\mathrm{T}(\pi_{\mathrm{Ph}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
            r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{Ph}}^*)$']
ax1.set_xticklabels(x_labels, fontsize=15, fontweight='bold', rotation=5)
my_colors = ['orange', 'black', 'black', 'black', "red", 'blue', 'darkgray', 'darkgray', "m", "turquoise"]
for ticklabel, tickcolor in zip(ax1.get_xticklabels(), my_colors):
    ticklabel.set_color(tickcolor)
ax1.set_xlabel("GeometryBodipyphenyl")
ax1.set_ylabel("Energie(eV)")
ax1.tick_params(axis='x',which='major',pad=13, rotation=18, color='black')
for x_labels in ax1.get_xticklabels():
    x_labels.set_verticalalignment('center')  # Center align vertically
    x_labels.set_horizontalalignment('center')  # Center align horizontally
for x_labels in ax1.get_xticklabels():
    x_labels.set_ha('right')
    x_labels.set_rotation_mode('anchor')
ax1.tick_params(axis='y', labelsize=9)

# Second subplot
x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deltaSCF = [0.0,    0.05,   0.32,   0.21,   0.28,   0.097,  0.191,  0.319,  0.16  ]
S1       = [2.7327, 2.6823, 2.9325, 2.8328, 3.0023, 2.7831, 2.8296, 2.9737, 2.8306]
S2       = [3.2737, 3.2786, 3.0071, 3.2405, 3.8169, 3.3271, 3.2832, 3.2992, 3.5178]
S3       = [3.5643, 3.5538, 3.6384, 3.41,   3.9636, 3.5326, 3.4187, 3.6049, 3.8081]
S4       = [3.6410, 3.5987, 3.7483, 3.4567, 4.0640, 3.6833, 3.51,   3.7451, 3.9049]
S11      = [5.1595, 5.2008, 5.6436, 5.5005, 4.8641, 5.1724, 4.9181, 5.1177, 5.0979]
T1       = [1.7072, 1.7148, 1.95811,1.8532, 1.9256, 1.6235, 1.8972, 2.0300, 1.7445]
T2       = [2.8443, 2.8140, 2.9234, 2.71,   3.2881, 2.8938, 2.6347, 3.0172, 3.1299]
T3       = [3.0038, 3.0927, 3.1381, 2.833,  3.4389, 3.0794, 2.8259, 3.2003, 3.2793]
T4       = [3.1260, 2.9419, 2.9808, 3.1108, 3.7029, 3.3273, 3.1398, 2.6833, 3.4051]
T16      = [4.8626, 4.8666, 5.2455, 5.180,  5.1859, 4.7751, 5.1852, 5.2264, 4.6828]
ax2.plot(x2, deltaSCF, linestyle='dashed', marker=mk, markersize=ms, color='orange',    linewidth=lw)
ax2.plot(x2, S1,       linestyle='dashed', marker=mk, markersize=ms, color='black',     linewidth=lw)
ax2.plot(x2, S2,       linestyle='dashed', marker=mk, markersize=ms, color='red',       linewidth=lw)
ax2.plot(x2, S4,       linestyle='dashed', marker=mk, markersize=ms, color='black',     linewidth=lw)
ax2.plot(x2, S11,      linestyle='dashed', marker=mk, markersize=ms, color='blue',      linewidth=lw)
ax2.plot(x2, T1,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray',  linewidth=lw)
ax2.plot(x2, T3,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray',  linewidth=lw)
ax2.plot(x2, T4,       linestyle='dashed', marker=mk, markersize=ms, color='m',         linewidth=lw)
ax2.plot(x2, T16,      linestyle='dashed', marker=mk, markersize=ms, color='turquoise', linewidth=lw)
ax2.set_xticks(x2)
x_labels2 = [r'$\mathrm{S_{0}}$',
             r'$\mathrm{S_{1}}$',
             r'$\mathrm{S}(\pi_{\mathrm{Ph}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{Ph}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{Ph}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{Ph}}^*)$']
ax2.set_xticklabels(x_labels2, fontsize=15, fontweight='bold', rotation=10)
my_colors2 = ['orange', 'black', 'red', 'black', "blue", 'darkgray', 'darkgray',"m",'turquoise']
for ticklabel, tickcolor in zip(ax2.get_xticklabels(), my_colors2):
    ticklabel.set_color(tickcolor)
ax2.set_xlabel("GeometryBodipyphenylOH")
ax2.set_ylabel("Energie(eV)")
ax2.tick_params(axis='x',which='major',pad=13, rotation=18, color='black')
for x_labels2 in ax2.get_xticklabels():
    x_labels2.set_verticalalignment('center')  # Center align vertically
    x_labels2.set_horizontalalignment('center')  # Center align horizontally
for x_labels2 in ax2.get_xticklabels():
    x_labels2.set_ha('right')
    x_labels2.set_rotation_mode('anchor')
ax2.tick_params(axis='y', labelsize=9)

# Third subplot
x3 = [1, 2, 3, 4, 5, 6, 7, 8]
deltascf = [0.0,    0.11,  0.3756,  0.273,  0.09,   0.22,   0.371,  0.28]
S1       = [2.6898, 2.5948, 3.0586, 2.7293, 2.7009, 2.7409, 3.0552, 2.9240]
S2       = [3.4922, 3.4301, 4.0308, 3.2832, 3.4209, 3.3220, 4.0131, 3.5440]
S3       = [3.5418, 3.6604, 3.0990, 3.9768, 4.3008, 3.9204, 3.1108, 3.8447]
S4       = [3.5569, 3.4309, 4.0705, 3.2982, 3.5542, 3.3284, 4.0539, 4.1949]
S9       = [4.3986, 4.2092, 4.8631, 4.0700, 4.3147, 4.5549, 4.8000, 4.1465]
T1       = [1.6451, 1.6535, 1.9630, 1.8245, 1.5699, 1.8224, 1.9613, 1.8729]
T2       = [2.7895, 2.7638, 3.3391, 2.5837, 2.8055, 2.5543, 3.3190, 2.8328]
T3       = [2.9494, 2.8818, 3.4702, 2.7540, 2.9871, 2.7320, 3.4530, 3.0308]
T6       = [3.4991, 3.5750, 4.3654, 3.8981, 3.5233, 3.8685, 3.0904, 3.8323]
T15      = [4.4791, 4.7059, 4.9294, 4.7746, 4.5422, 4.5850, 4.8715, 4.4660]
ax3.plot(x3, deltascf, linestyle='dashed', marker=mk, markersize=ms, color="orange",    alpha=1, linewidth=lw)
ax3.plot(x3, S1,       linestyle='dashed', marker=mk, markersize=ms, color='black',     alpha=1, linewidth=lw)
ax3.plot(x3, S3,       linestyle='dashed', marker=mk, markersize=ms, color='blue',      alpha=1, linewidth=lw)
ax3.plot(x3, S4,       linestyle='dashed', marker=mk, markersize=ms, color='black',     alpha=1, linewidth=lw)
ax3.plot(x3, T1,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray',  alpha=1, linewidth=lw)
ax3.plot(x3, T3,       linestyle='dashed', marker=mk, markersize=ms, color='darkgray',  alpha=1, linewidth=lw)
ax3.plot(x3, T6,       linestyle='dashed', marker=mk, markersize=ms, color='turquoise', alpha=1, linewidth=lw)
ax3.plot(x3, T15,      linestyle='dashed', marker=mk, markersize=ms, color='m',         alpha=1, linewidth=lw)
ax3.set_xticks(x3)
x_labels3 = [r'$\mathrm{S_{0}}$',
             r'$\mathrm{S_{1}}$',
             r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{Ph}}^*)$',
             r'$\mathrm{S}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{BOD}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{BOD}} \rightarrow\pi_{\mathrm{Ph}}^*)$',
             r'$\mathrm{T}(\pi_{\mathrm{Ph}} \rightarrow\pi_{\mathrm{BOD}}^*)$']
ax3.set_xticklabels(x_labels3, fontsize=15, fontweight='bold', rotation=10)
my_colors3 = ['orange', 'black', 'blue', 'black', 'darkgray', 'darkgray', 'turquoise', "m"]
for ticklabel, tickcolor in zip(ax3.get_xticklabels(), my_colors3):
    ticklabel.set_color(tickcolor)
ax3.set_xlabel("GeometryBodipyphenylno2")
ax3.set_ylabel("Energie(eV)")
ax3.tick_params(axis='x', which='major', pad=13, rotation=18, color='black')
for x_labels3 in ax3.get_xticklabels():
    x_labels3.set_verticalalignment('center')  # Center align vertically
    x_labels3.set_horizontalalignment('center')  # Center align horizontally
for x_labels3 in ax3.get_xticklabels():
    x_labels3.set_ha('right')
    x_labels3.set_rotation_mode('anchor')
ax3.tick_params(axis='y', labelsize=9)

# Adjust layout
plt.tight_layout()
# Show or save the figure
plt.savefig('Bodipyverticalenergies.png', dpi=100, bbox_inches='tight')
plt.show()
