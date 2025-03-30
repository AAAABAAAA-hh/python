# 此种写法较为巧妙应用了i的值

def sort_choice(lst):
      for i,item in enumerate(lst):
          min_idx = len(lst)-1
          for j in range(i, len(lst)):
               if lst[j] < lst[min_idx]:
                   min_idx = j
          if min_idx != i:
              lst[i], lst[min_idx] = lst[min_idx], lst[i]



























