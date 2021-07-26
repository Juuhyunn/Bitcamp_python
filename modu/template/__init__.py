from common.menu import print_menu
from modu.template.basic import plot_show, plot_two_list_show, scatter

if __name__ == '__main__':
    while 1:
        menu = print_menu(['Exit', 'Plot_show', 'Plot_two_list_show', 'Scatter'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            scatter()
