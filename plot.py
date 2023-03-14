import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
acc = [0.7012232415902141,0.6944639103013315]
fig,ax = plt.subplots()
# plt.xticks(["Bert-base-uncased-dev","RoBERTa-base-dev","Bert-base-uncased-test",'RoBERTa-base-test'], rotation = 'vertical')
ax.bar(["T5-small-dev","T5-small-test"], acc, width = 0.4)
# for i, v in enumerate(acc):
#     ax.text(v, i-1, str(v), va = 'center', fontweight='bold')
# plt.text(str(0.7012232415902141), str(0.6944639103013315))
plt.xlabel('Evaluation Type')
plt.xticks(fontsize = 8)
plt.ylabel('Accuracy')
plt.show()
plt.savefig('q8.png')
plt.close()