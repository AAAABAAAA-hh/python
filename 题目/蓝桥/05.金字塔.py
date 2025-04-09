# 蓝桥   py   金字塔
#
#用python的多赋值，线性递推，观察到当前金字塔所需的弹珠应该是上一个金字塔的弹珠加上一层的弹珠
# 所加的这一层弹珠应该是上一个金字塔的最后一层加上当前的层数。如果用for循环线性递推到所需值是不是算法复杂度也是o(n)
def max_pyramid_height_optimized_recursive(total_beads):
    if total_beads < 1:
        return 0
    if total_beads == 1:
        return 1

    height = 1
    prev_beads = 1
    prev_prev_beads = 0

    while True:
        height += 1
        current_beads = 2 * prev_beads - prev_prev_beads + 1

        if current_beads > total_beads:
            return height - 1
        elif current_beads == total_beads:
            return height

        prev_prev_beads = prev_beads
        prev_beads = current_beads

total_beads = 20230610
max_height = max_pyramid_height_optimized_recursive(total_beads)
print(f"使用 {total_beads} 颗弹珠可以搭建的最高金字塔高度为: {max_height}")