import matplotlib.pyplot as plt

def plotloss(F1score_list,recall_list,prec_list,index):
    x_list = list(range(len(F1score_list)))
    plt.plot(x_list, F1score_list)
    plt.xlabel('batches/10')
    plt.ylabel('F1score')
    plt.title('The F1 score')
    plt.show()
    plt.savefig(f'./autodl-tmp/output/lossimage/F1score_{index}.png')
    plt.close()
    
    plt.plot(x_list, recall_list)
    plt.xlabel('batches/10')
    plt.ylabel('recall')
    plt.title('The recall')
    plt.show()
    plt.savefig(f'./autodl-tmp/output/lossimage/recall_{index}.png')
    plt.close()

    plt.plot(x_list, prec_list)
    plt.xlabel('batches/10')
    plt.ylabel('prec')
    plt.title('The prec')
    plt.show()
    plt.savefig(f'./autodl-tmp/output/lossimage/prec_{index}.png')
    plt.close()