# result={"aa":[0,0],"bb":[0,1]}
# for i in result.keys():
#     print (i)
#
# result["aa"][0]=result["aa"][0]+2
# print (result["aa"])
#
# if "cc" not in result.keys():
#     result["cc"]=[0,0]
# print (result)
# import matplotlib.pyplot as plt
#
# name_list = ['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
# num_list = [52.4, 57.8, 59.1, 54.6]
# rects=plt.bar(range(len(num_list)), num_list, color='rgby')
#
# index=[0,1,2,3]
# index=[float(c)+0.4 for c in index]
# plt.ylim(ymax=80, ymin=0)
# plt.xticks(index, name_list)
# plt.ylabel("arrucay(%)")
# for rect in rects:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height, str(height)+'%', ha='center', va='bottom')
# plt.show()
# from matplotlib import pyplot as plt
# plt.bar([1,2,3,4],[2,3,45,4],align="center",width=0.4)
# plt.xticks([1,2,3,4],["fjd","fds","fgd","fd"])
# plt.show()

txt = open("test.txt","w")
for i in range(10):
    j = str(i)
    txt.write("\n" + j)
