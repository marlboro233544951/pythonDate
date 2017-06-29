import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from matplotlib.cbook import get_sample_data
import numpy as np

# fname = get_sample_data('percent_bachelors_degrees_women_usa.csv')
# gender_degree_data = csv2rec(fname)
width = 0.4
ind = np.linspace(0.5, 9.5, 9)
font = {'family': 'serif',
            # 'color'  : 'darkred',
            'weight': 'normal',
            'size': 18,
            }

quants1 = [2, 95, 110, 100, 123, 756, 810, 500, 512]
quants2 = [4, 623 ,763 , 462, 370, 3179, 3179, 1213, 1135]
quants3 = [4, 1011 , 1019, 845, 924, 6189, 6176, 1804, 1997]
quants4 = [8, 4435, 5739, 3823, 3106, 26795, 25795, 2148, 2335]
qlabels = ['Random', 'Popu', 'Rank', 'Markov', 'Markov-Rank', 'MarkovPath', 'MarkovPath-Rank', 'TRED-L', 'TRED-G']
def readquant(qlabels,quants1,quants2,quants3,quants4):
    new = [ [0 for i in range(4)] for i in range(9)]
    for rank,colum in enumerate(qlabels):
        # new[rank][0]=colum
        # new[rank][1]=quants1[rank]
        # new[rank][2]=quants2[rank]
        # new[rank][3]=quants3[rank]
        # new[rank][4]=quants4[rank]
        new[rank][0] = quants1[rank]
        new[rank][1] = quants2[rank]
        new[rank][2] = quants3[rank]
        new[rank][3] = quants4[rank]
    tli = []
    for i in new:
        i = tuple(i)
        tli.append(i)
    return tli


li = readquant(qlabels,quants1,quants2,quants3,quants4)
# gender_degree_data = np.array([('Random', 2, 4, 4, 8), ('Popu', 95, 623, 1011, 4435), ('Rank', 110, 763, 1019, 5739), ('Markov', 100, 462, 845, 3823), ('Markov-Rank', 123, 370, 924, 3106), ('MarkovPath', 756, 3179, 6189, 26795), ('MarkovPath-Rank', 810, 3179, 6176, 25795), ('TRED-L', 500, 1213, 1804, 2148), ('TRED-G', 512, 1135, 1997, 2335)], dtype=[('label', str), ('f@100', int),('f@200', int),('f@400', int),('f@800', int)])

gender_degree_data = np.array(li, dtype=[('f@100', int),('f@200', int),('f@400', int),('f@800', int)])
# These are the colors that will be used in the plot
# color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
#                   '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
#                   '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
#                   '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']
color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd']
# You typically want your plot to be ~1.33x wider than tall. This plot
# is a rare exception because of the number of lines being plotted on it.
# Common sizes: (10, 7.5) and (12, 9)
fig, ax = plt.subplots(1, 1, figsize=(12, 9))

# Remove the plot frame lines. They are unnecessary here.
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

fig.subplots_adjust(left=.06, right=.75, bottom=.02, top=.94)
# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
# ax.set_xlim(1969.5, 2011.1)
# ax.set_ylim(-0.25, 90)

# Make sure your axis ticks are large enough to be easily read.
# You don't want your viewers squinting to read your plot.
# plt.xticks(range(1970, 2011, 10), fontsize=14)
# plt.yticks(range(0, 91, 10), fontsize=14)

# ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
# ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))

# Provide tick lines across the plot to help your viewers trace along
# the axis ticks. Make sure that the lines are light and small so they
# don't obscure the primary data lines.
plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

# Remove the tick marks; they are unnecessary with the tick lines we just
# plotted.
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='on', left='off', right='off', labelleft='on')

# Now that the plot is prepared, it's time to actually plot the data!
# Note that I plotted the majors in order of the highest % in the final year.
# majors = ['Health Professions', 'Public Administration', 'Education',
#           'Psychology', 'Foreign Languages', 'English',
#           'Communications\nand Journalism', 'Art and Performance', 'Biology',
#           'Agriculture', 'Social Sciences and History', 'Business',
#           'Math and Statistics', 'Architecture', 'Physical Sciences',
#           'Computer Science', 'Engineering']
#
# y_offsets = {'Foreign Languages': 0.5, 'English': -0.5,
#              'Communications\nand Journalism': 0.75,
#              'Art and Performance': -0.25, 'Agriculture': 1.25,
#              'Social Sciences and History': 0.25, 'Business': -0.75,
#              'Math and Statistics': 0.75, 'Architecture': -0.75,
#              'Computer Science': 0.75, 'Engineering': -0.25}
majors =['F@100', 'F@200', 'F@400', 'F@800']
y_offsets = {'F@100':0, 'F@200':0, 'F@400':0, 'F@800':0}
dataset = ['F@100', 'F@200', 'F@400', 'F@800']

ax.set_xticklabels(dataset,fontdict=font)
for rank, column in enumerate(majors):
    # Plot each line separately with its own color.
    column_rec_name = column.replace('\n', '_').replace(' ', '_').lower()

    # line = plt.plot(gender_degree_data.year,
    #                 gender_degree_data[column_rec_name],
    #                 lw=2.5,
    #                 color=color_sequence[rank])
    line = plt.plot(ind - width / 2,
                    gender_degree_data[column_rec_name],
                    lw=2.5,
                    color=color_sequence[rank])

    # Add a text label to the right end of every line. Most of the code below
    # is adding specific offsets y position because some labels overlapped.
    y_pos = gender_degree_data[rank][-1] - 0.5

    if column in y_offsets:
        y_pos += y_offsets[column]

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(2011.5, y_pos, column, fontsize=14, color=color_sequence[rank])
    # plt.text(2011.5, column, fontsize=14, color=color_sequence[rank])

# Make the title big enough so it spans the entire plot, but don't make it
# so big that it requires two lines to show.

# Note that if the title is descriptive enough, it is unnecessary to include
# axis labels; they are self-evident, in this plot's case.
fig.suptitle('Percentage of Bachelor\'s degrees conferred to women in '
             'the U.S.A. by major (1970-2011)\n', fontsize=18, ha='center')

# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
# plt.savefig('percent-bachelors-degrees-women-usa.png', bbox_inches='tight')
plt.show()