
# my_dict = {"黑马":99,"白马":98}
# score = my_dict["黑马"]
# print(score)
stu_score_dict = \
    {
    "王":{"语文":77,"数学":88,"英语":99},
    "周":{"语文":88,"数学":88,"英语":99}
 }

print(f"学生的考试信息为{stu_score_dict}")

for key in stu_score_dict:
    print(f"{key}:{stu_score_dict[key]}")





















