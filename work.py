import xlrd
from matplotlib import pyplot as plt

xls = xlrd.open_workbook("ML_data2.xlsx")
sheet=xls.sheets()[0]
nrows = sheet.nrows
ncols = sheet.ncols
# val = sheet.row_values(8)[ncols-1]
# if val == ">50K":
#     print ("yes")
# else:
#     print ("no")
#
# print (type(val))
# print (val)

def get_MP(xls):
    sheet = xls.sheets()[0]
    all_number = sheet.nrows - 1
    ncols = sheet.ncols
    s = 0
    for i in range(1,all_number+1):
        if sheet.row_values(i)[ncols-1] == ">50K":
            s = s + 1
    return s/(1.0*all_number)

def get_statics(xls,sheet_num,number_col):
    results={}
    sheet = xls.sheets()[sheet_num]
    nrows = sheet.nrows
    for i in range(1,nrows):
        name = sheet.row_values(i)[number_col]
        if name not in results.keys():
            results[name]=[0,0]
        results[name][0] = results[name][0]+1
        if sheet.row_values(i)[14] == ">50K":
            results[name][1] = results[name][1] + 1
    return results

def get_proportion(result):
    xlabel = []
    ylabel = []
    number = []
    for key in result.keys():
        xlabel.append(key)
        number.append(result[key][1])
        ylabel.append(float(result[key][1]/(1.0*result[key][0])))
    nums = len(ylabel)
    num_list=[c for c in range(nums)]
    s = sum(number)
    weight = [i/(1.0*s) for i in number]
    return xlabel,ylabel,num_list,weight

def get_MSE(MP,weight,p):
    s = 0
    counts = len(weight)
    for i in range(counts):
        s = s + weight[i] * (p[i]-MP)*(p[i]-MP)
    return s

chosed = [1,3,5,6,7,8,9]
xlabels = []
ylabels = []
weights = []
mses = []

MP = get_MP(xls)
for i in chosed:
    result= get_statics(xls,0,i)
    xl,yl,nothing,weight = get_proportion(result)
    xlabels.append(xl)
    ylabels.append(yl)
    weights.append(weight)
    mse = get_MSE(MP,weight,yl)
    mses.append(mse)

weight_values = []
s = sum(mses)
for i in range(7):
    weight_values.append(mses[i]/s)

in_weight = []
for i in range(7):
    values = []
    temp_yvalues = ylabels[i]
    sum_yvalues = sum(temp_yvalues)
    length_temp_yvalues = len(temp_yvalues)
    for j in range(length_temp_yvalues):
        values.append(weight_values[i]*temp_yvalues[j]/sum_yvalues)
    in_weight.append(values)

all_dict={}
for i in range(7):
    single_dict={}
    lengthOfxlabel = len(xlabels[i])
    for j in range(lengthOfxlabel):
        single_dict[xlabels[i][j]] = in_weight[i][j]
    all_dict[chosed[i]] = single_dict

best_thresh = 0.0
temp_thresh_value = 0
high_now = 0.0
for h in range(80):
    right = 0
    error = 0
    for i in range(1,nrows):
        judge = 0
        for j in range(7):
            judge = judge + all_dict[chosed[j]][sheet.row_values(i)[chosed[j]]]
        if judge > temp_thresh_value:
            if sheet.row_values(i)[ncols-1] == ">50K":
                right = right + 1
        else:
            if sheet.row_values(i)[ncols-1] == "<=50K":
                right = right+1

    if right/(1.0*nrows)>high_now:
        high_now = right/(1.0*nrows)
        best_thresh = temp_thresh_value
    temp_thresh_value = temp_thresh_value + 0.01

test_sheet=xls.sheets()[1]
test_nrows = test_sheet.nrows
test_ncols = test_sheet.ncols

test_right = 0
test_error = 0
for i in range(1,test_nrows):
    judge = 0
    for j in range(7):
        judge = judge + all_dict[chosed[j]][test_sheet.row_values(i)[chosed[j]]]
    if judge > best_thresh:
        if test_sheet.row_values(i)[ncols-1] == ">50K":
            test_right = test_right + 1
    else:
        if test_sheet.row_values(i)[ncols-1] == "<=50K":
            test_right = test_right+1

print (test_right/(1.0*test_nrows))
