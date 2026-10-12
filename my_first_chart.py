import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic" 

lank = [4, 10, 9, 8, 8, 8, 7, 8]
days = [3, 4, 5, 6, 7, 8, 9, 10]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, lank)
for i, p in enumerate(lank):
    ax.annotate(f"{p:,}", (days[i], p), textcoords="offset points",
                xytext=(0, 8), ha="center")
    
ax.invert_yaxis() # y축 뒤집기
ax.set_title("내 야구팀 순위 변화")
fig.savefig("my_first_chart.png")