import matplotlib.pyplot as plt
import numpy as np


class DonutBarChart:
    def __init__(self, 
                names: list, 
                groups: list,
                group_colors: list = None, 
                group_names: list = None,
                scale_lim: int = 22,
                scale_major: int = 2,
                r_lim: int = 20,
                bottom: int = 10,
                fontsize: float = 2.5,
                linewidth: float = 0.5,
                graphic: bool = True,
                inside: bool = True
                ) -> None:
        '''
        :param names: list of names of the data
        >>>[['name1', 'name2', 'name3'], ['name4', 'name5', 'name6']]
        :param groups: list of data, the same structure as names
        >>>[[1, 2, 3], [4, 5, 6]]
        :param group_colors: list of colors of the groups
        >>>['#000000', '#000000']
        :param group_names: list of names of the groups
        >>>['group1', 'group2'], default: ['', '', '']
        '''
        self.names = names
        self.groups = groups
        if group_colors is None:
            import sys
            sys.path.insert(0, sys.path[0]+"/../")
            from colorStyle import DefaultColorScheme
            color_scheme = DefaultColorScheme()
            select_colors = ['#ff706d', '#7baf06', '#01bfc5', '#cb7bf6', '#d1ba74']
            if len(groups) > len(select_colors):
                select_colors = color_scheme.NPG
            # 选择同样长度的颜色
            group_colors = select_colors[:len(groups)]
        
        if group_names is None:
            group_names = ['' for _ in range(len(groups))]
        self.group_colors = group_colors
        self.group_names = group_names

        self.scale_lim = scale_lim
        self.scale_major = scale_major
        self.r_lim = r_lim
        self.bottom = bottom
        self.fontsize = fontsize
        self.linewidth = linewidth
        self.graphic = graphic
        self.inside = inside
       

    def patch(self) -> tuple:
        radii = [0]
        name_l = ['']
        colors = ['white']
        for g, n, c in zip(self.groups, self.names, self.group_colors):
            radii.extend(g)
            name_l.extend(n)
            colors.extend([c]*len(g))
            radii.append(0)
            name_l.append('')
            colors.append('white')
        radii.pop()
        colors.pop()
        name_l.pop()
        N = len(radii)
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        width = 2 * np.pi / (N + 9)
        return radii, name_l, colors, theta, width


    def scale(self, ax, theta, width):
        t = np.linspace(theta-width/2, theta+width/2, 6)
        for i in range(int(self.bottom), int(self.bottom+self.scale_lim+self.scale_major), self.scale_major):
            ax.plot(t, [i]*6, linewidth=1, color='gray', alpha=0.8)


    def scale_value(self, ax, theta):
        for i in range(int(self.bottom), int(self.bottom+self.scale_lim+self.scale_major), self.scale_major):
            ax.text(theta,
                    i,
                    f'{i-self.bottom}',
                    fontsize=self.fontsize,
                    alpha=0.8,
                    va='center',
                    ha='center'
                    )
            
    def display_polar(self, theta, radii, name_l, ax, width):
        s_list = []
        g_no = 0
        for t, r , n in zip(theta, radii, name_l):

            if r == 0:
                s_list.append(t)
                if t == 0:
                    self.scale_value(ax, t)
                else:
                    self.scale(ax, t, width)
            else:
                t2 = np.rad2deg(t)
                # 标出每根柱的名称
                ax.text(t, r + self.bottom + self.scale_major*0.6,
                        n,
                        fontsize=self.fontsize,
                        rotation=90-t2 if t < np.pi else 270-t2,
                        rotation_mode='anchor',
                        va='center',
                        ha='left' if t < np.pi else 'right',
                        color='black',
                        clip_on=False
                        )
                g_no += 1

        s_list.append(2 * np.pi)
        return s_list


    def add_graphical(self, ax):
        # 增加图例，每个图例的名称和颜色
        for i in range(len(self.group_colors)):
            ax.plot([0], [0], color=self.group_colors[i], label=self.group_names[i])
        ax.legend(loc='upper right', fontsize=self.fontsize, frameon=False)
        


    def render(self):
        fig = plt.figure(figsize=(8, 8), dpi=300, facecolor='white')
        ax = fig.add_subplot(projection='polar')

        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)

        # 绘制柱状图
        radii, name_l, colors, theta, width = self.patch()
        ax.bar(theta, radii, width=width, bottom=self.bottom, color=colors)
        s_list = self.display_polar(theta, radii, name_l, ax, width)

        # 绘制刻度和环形图
        for i in range(len(s_list)-1):
            t = np.linspace(s_list[i]+width, s_list[i+1]-width, 50)
            ax.plot(t, [self.bottom-self.scale_major*0.4]*50, linewidth=self.linewidth, color='black')
            if self.inside:
                ax.text(s_list[i]+(s_list[i+1]-s_list[i])/2,
                        self.bottom-self.scale_major*1.2,
                        self.group_names[i],
                        fontsize=self.fontsize,
                        va='center',
                        ha='center'
                        )

        ax.set_rlim(0, self.bottom+self.scale_lim+self.scale_major)

        if self.graphic:
            self.add_graphical(ax)
        ax.axis('off')

        plt.show()
