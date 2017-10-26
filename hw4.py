from collections import Counter

def word_count_distribution(text):
    counts_dic = count_words_fast(text)
    raw_vals = counts_dic.values()
    return Counter(raw_vals)

distribution = word_count_distribution(text)

def more_frequent(distribution):
    output = {}
    for x in distribution.keys():
        x_val = distribution[x]
        greater_than_count = 0
        for y in distribution.values():
            if y > x_val:
                greater_than_count += 1
        output[x] = greater_than_count / len(distribution)
    return output

more_frequent(distribution)

hamlets = pd.DataFrame(columns=['language', 'distribution'])
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text)
                hamlets.loc[title_num] = language, distribution
                title_num += 1
                
olors = ["crimson", "forestgreen", "blueviolet"]
handles, hamlet_languages = [], []
for index in range(hamlets.shape[0]):
    language, distribution = hamlets.language[index+1], hamlets.distribution[index+1]
    dist = more_frequent(distribution)
    plot, = plt.loglog(sorted(list(dist.keys())),sorted(list(dist.values()),
        reverse = True), color = colors[index], linewidth = 2)
    handles.append(plot)
    hamlet_languages.append(language)
plt.title("Word Frequencies in Hamlet Translations")
xlim    = [0, 2e3]
xlabel  = "Frequency of Word $W$"
ylabel  = "Fraction of Words\nWith Greater Frequency than $W$"
plt.xlim(xlim); plt.xlabel(xlabel); plt.ylabel(ylabel)
plt.legend(handles, hamlet_languages, loc = "upper right", numpoints = 1)
plt.show()





