company_dict = \
    {
        "王力鸿": {"部门": "科技部", "工资": 3000, "级别": 1},
        "周杰轮": {"部门": "市场部", "工资": 5000, "级别": 2},
        "林俊节": {"部门": "市场部", "工资": 7000, "级别": 3},
        "张学油": {"部门": "科技部", "工资": 4000, "级别": 1},
        "刘得滑": {"部门": "市场部", "工资": 6000, "级别": 2}
    }
print(company_dict)
for key in company_dict:
    a = company_dict[key]["级别"]
    if a == 1:
        company_dict[key]["级别"] += 1
        company_dict[key]["工资"] += 1000
print(company_dict)




