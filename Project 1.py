# os library
from nltk.stem.porter import PorterStemmer
from collections import Counter
from nltk.corpus import stopwords as stopWords
import os

# math library
import math

# nltk library
import nltk

# tokenizer library
from nltk.tokenize import RegexpTokenizer as regexpTokenizer

# starting tokenizer for later purpose
tokenizer_model = regexpTokenizer(r'[a-zA-Z]+')

# stopwords library

# downloading stop words
nltk.download('stopwords')

# making list of all stop words
list_of_all_stop_words = stopWords.words('english')

# counter library

# starting a word counter for all unique words
all_unique_word_counter = Counter()

# starting a file wise unique word counter
file_wise_unique_word_fquency_counter = Counter()

# stemmer library

# starting stemming object
stemming_model = PorterStemmer()

# path
path = './P1'

# getting names of all files we have in the folder
names_of_text_file = os.listdir(path + '/US_Inaugural_Addresses')

# getting total number of files
total_no_of_text_files = len(names_of_text_file)

# list to save final file names
list_of_final_names_of_file = []

# making list to save the content of the files
all_content_of_all_documents = []

# starting dictionary to save tf weights
term_frequency_weight = {}

# starting dictionary to save the final calulated weight
all_over_weight = {}

# starting counter for complete weight of a  file
complete_weight_per_file = Counter()

# startinf dictionart to save the final weight calculations
last_complete_weight = {}

# function to add folder name to file


def file_name_completer(
    file_name): return "US_Inaugural_Addresses/" + file_name


# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # getting file name
    loop_file_name = names_of_text_file[file_number]
    # appending folder name to file name
    loop_file_name = "US_Inaugural_Addresses/" + loop_file_name
    # saving the final name of the list
    list_of_final_names_of_file.append(loop_file_name)
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # getting file name
    loop_file_name = list_of_final_names_of_file[file_number]
    # opening file
    loop_file_content = open(path + "/"+loop_file_name, mode="r")
    # reading data from file
    read_loop_file_content = loop_file_content.read()
    # converting the data in smaller case
    Small_read_loop_file_content = read_loop_file_content.lower()
    # saving the final data in the last
    all_content_of_all_documents.append(Small_read_loop_file_content)
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # reading final data from file
    loop_file_data = all_content_of_all_documents[file_number]
    # tokenizing the file data
    toeknized_loop_file_data = tokenizer_model.tokenize(loop_file_data)
    # putting it back in main file
    all_content_of_all_documents[file_number] = toeknized_loop_file_data
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # reading final data from file
    loop_file_data = all_content_of_all_documents[file_number]
    # starting list to save data after stop word removal
    list_without_stop_words = []
    # loop to iterate complete word list
    for every_word in loop_file_data:
        # check if it stop word
        if every_word not in list_of_all_stop_words:
            # adding it to list
            list_without_stop_words.append(every_word)
    # putting it back in main file
    all_content_of_all_documents[file_number] = list_without_stop_words
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # reading final data from file
    loop_file_data = all_content_of_all_documents[file_number]
    # starting list to save stemmed data
    list_of_words = []
    # loop to iterate complete word list
    for every_word in loop_file_data:
        # stemming word
        every_word = stemming_model.stem(every_word)
        # adding it to list
        list_of_words.append(every_word)
    # putting it back in main file
    all_content_of_all_documents[file_number] = list_of_words
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # picking the data of the file
    loop_file_data_ins = all_content_of_all_documents[file_number]
    # making the counter from the complete data
    loop_ins_counter = Counter(loop_file_data_ins)
    # now adding this to file wise counter
    file_wise_unique_word_fquency_counter[loop_file_name_ins] = loop_ins_counter
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking the data of the file
    loop_file_data_ins = all_content_of_all_documents[file_number]
    # making the counter from the complete data
    loop_ins_counter = Counter(loop_file_data_ins)
    # now adding this to complete unique words data
    all_unique_word_counter = all_unique_word_counter + loop_ins_counter
    # increasing counter
    file_number = file_number + 1

# function to find the idf


def getidf(random_func_word):
    # checking if the word exist or not
    if random_func_word not in all_unique_word_counter:
        # return -1 in this case
        return -1
    # writing else part
    else:
        # let's find out how many sentences have this term
        word_frequency_in_documents = 0
        # loop file number
        file_number = 0
        # while loop
        while file_number < total_no_of_text_files:
            # reading final data from file
            loop_file_data = all_content_of_all_documents[file_number]
            # checking if the word is in the file data or not
            if random_func_word in loop_file_data:
                # increasing word frequency variable
                word_frequency_in_documents = word_frequency_in_documents + 1
            # increasing counter
            file_number = file_number + 1
        # finding half calculations
        partial_answer = total_no_of_text_files / word_frequency_in_documents
        # solving the final expression
        final_answer = math.log10(partial_answer)
        # returning final answer
        return final_answer


# print
print("*"*30)
print("GetIdf Function Run")
print("*"*30)

# running example 1
print("Running getidf for - british")
# calling function
print("%.12f" % getidf('british'))
print("*"*30)

# running example 2
print("Running getidf for - union")
# calling function
print("%.12f" % getidf('union'))
print("*"*30)

# running example 3
print("Running getidf for - war")
# calling function
print("%.12f" % getidf('war'))
print("*"*30)

# running example 4
print("Running getidf for - power")
# calling function
print("%.12f" % getidf('power'))
print("*"*30)

# running example 5
print("Running getidf for - great")
# calling function
print("%.12f" % getidf('great'))
print("*"*30)

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # starting blank counters
    term_frequency_weight[loop_file_name_ins] = Counter()
    # starting blank counters
    all_over_weight[loop_file_name_ins] = Counter()
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # picking unique word list from this file name
    loop_word_collection = file_wise_unique_word_fquency_counter[loop_file_name_ins]
    # picking every word from this
    for every_word in loop_word_collection:
        # particla calculations
        partial_ans = file_wise_unique_word_fquency_counter[loop_file_name_ins][every_word]
        # final answer
        final_answer = 1 + math.log10(partial_ans)
        # saving final answer
        term_frequency_weight[loop_file_name_ins][every_word] = final_answer
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # picking unique word list from this file name
    loop_word_collection = file_wise_unique_word_fquency_counter[loop_file_name_ins]
    # picking every word from this
    for every_word in loop_word_collection:
        # partial calculations
        partial_ans = term_frequency_weight[loop_file_name_ins][every_word]
        # another partial answer
        partial_idf = getidf(every_word)
        # final answer
        final_answer = partial_ans * partial_idf
        # saving it in final dict
        all_over_weight[loop_file_name_ins][every_word] = final_answer
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # making temo list
    temp_list = []
    # loop to pick words
    for Ins_Word in file_wise_unique_word_fquency_counter[loop_file_name_ins]:
        # finding square
        temp_ans_2 = (term_frequency_weight[loop_file_name_ins][Ins_Word]) ** 2
        # appening element to list
        temp_list.append(temp_ans_2)
    # partial answer
    partial_answer = sum(temp_list)
    # calculating final answer
    final_answer = math.sqrt(partial_answer)
    # saving the final answer
    last_complete_weight[loop_file_name_ins] = final_answer
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # making temo list
    temp_list = []
    # loop to iterate every word
    for Ins_Word in file_wise_unique_word_fquency_counter[loop_file_name_ins]:
        # finding square
        temp_ans_1 = (all_over_weight[loop_file_name_ins][Ins_Word]) ** 2
        # appending data to list
        temp_list.append(temp_ans_1)
    # partial answer
    partial_answer = sum(temp_list)
    # finding final answer
    final_answer = math.sqrt(partial_answer)
    # saving the final answer
    last_complete_weight[loop_file_name_ins] = final_answer
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # picking all words
    set_of_all_words_in_given_file = file_wise_unique_word_fquency_counter[loop_file_name_ins]
    # loop tp pick every word
    for random_word_loop in set_of_all_words_in_given_file:
        # finding term frequency
        tf_w = term_frequency_weight[loop_file_name_ins][random_word_loop]
        # finding weight
        com_w = last_complete_weight[loop_file_name_ins]
        # partial answer
        partial_calculated_weight = tf_w / com_w
        # saving final answer
        term_frequency_weight[loop_file_name_ins][random_word_loop] = partial_calculated_weight
    # increasing counter
    file_number = file_number + 1

# loop file number
file_number = 0
# while loop
while file_number < total_no_of_text_files:
    # picking file name of the file
    loop_file_name_ins = list_of_final_names_of_file[file_number]
    # picking all words
    set_of_all_words_in_given_file = file_wise_unique_word_fquency_counter[loop_file_name_ins]
    # loop to iterate
    for random_word_loop in set_of_all_words_in_given_file:
        # all over weight
        all_wei = all_over_weight[loop_file_name_ins][random_word_loop]
        # last complete weight on given reference
        last_com = last_complete_weight[loop_file_name_ins]
        # final calculations
        random_tf_idf_value = all_wei / last_com
        # saving final value
        all_over_weight[loop_file_name_ins][random_word_loop] = random_tf_idf_value
    # increasing counter
    file_number = file_number + 1

# function for getweight


def getweight(func_file_name, func_random_word):
    # adding the folder name to file name
    func_file_name = file_name_completer(func_file_name)
    # fetching dala of teh file name recived
    instant_data_rx = all_over_weight[func_file_name]
    # checking if the word exist in data or not
    if func_random_word not in instant_data_rx:
        # return 0
        return 0
    # writing else part
    else:
        # getting weight
        func_weight = instant_data_rx[func_random_word]
        # returning weight
        return func_weight


# print
print("*"*70)
print("GetWeight Function Run")
print("*"*70)

# running example 1
print("Running getweight for - '02_washington_1793.txt', 'arrive'")
# calling function
print("%.12f" % getweight('02_washington_1793.txt', 'arrive'))
print("*"*70)

# running example 2
print("Running getweight for - '07_madison_1813.txt', 'war'")
# calling function
print("%.12f" % getweight('07_madison_1813.txt', 'war'))
print("*"*70)

# running example 3
print("Running getweight for - '12_jackson_1833.txt', 'union'")
# calling function
print("%.12f" % getweight('12_jackson_1833.txt', 'union'))
print("*"*70)

# running example 4
print("Running getweight for - '09_monroe_1821.txt', 'great'")
# calling function
print("%.12f" % getweight('09_monroe_1821.txt', 'great'))
print("*"*70)

# running example 5
print("Running getweight for - '05_jefferson_1805.txt', 'public'")
# calling function
print("%.12f" % getweight('05_jefferson_1805.txt', 'public'))
print("*"*70)

# writing query function


def query(random_string):
    # starting list to save cosine similarities
    list_of_cosine_similarity = []
    # variabel to save index value of teh file having highest cosine similarity
    final_highest_simi_index = None
    # converting string into lower case
    random_string = random_string.lower()
    # splittign to ak eit list
    random_string = random_string.split()
    # removing stop words
    final_string = []
    # loop to iterate words
    for every_word in random_string:
        # checking if it is as stop word or not
        if every_word not in list_of_all_stop_words:
            # appending word
            final_string.append(every_word)
    # stemming the final words
    stemmed_collection_of_words = []
    # loop to iterate words
    for every_word in final_string:
        # perform stemming
        stemmed_word = stemming_model.stem(every_word)
        # appending the word again
        stemmed_collection_of_words.append(stemmed_word)
    # loop file number
    file_number = 0
    # while loop
    while file_number < total_no_of_text_files:
        # picking file name of the file
        loop_file_name_ins = list_of_final_names_of_file[file_number]
        # accessing the file data
        function_temp_file_content = all_content_of_all_documents[file_number]
        # set of all stemmed words
        set_new_query = list(set(stemmed_collection_of_words))
        # set of all words in the file
        set_all_words = list(set(function_temp_file_content))
        # makign the final set
        final_set_of_words = list(set(set_new_query + set_all_words))
        # list to find the tf weight
        list_random_word_tf_weight = []
        # iterate the rtandom word
        for every_word in final_set_of_words:
            # checking condition
            if every_word in stemmed_collection_of_words:
                # append 1
                list_random_word_tf_weight.append(1)
            # writing else part
            else:
                # else append 0
                list_random_word_tf_weight.append(0)
        # let's find idfs of all words
        idf_of_all_words = []
        # iterate words
        for every_word in final_set_of_words:
            # find idf values
            temp_idf_value = getidf(every_word)
            # checking if it is -1 or not
            if temp_idf_value == -1:
                # appending 0
                idf_of_all_words.append(0)
            # else part
            else:
                # else append the correct idf
                idf_of_all_words.append(temp_idf_value)
        # let's find out all the weights
        list_final_weights = []
        # length of words
        length_words = len(final_set_of_words)
        # loop
        word_icc = 0
        # loop
        while word_icc < length_words:
            # find tf weight
            tf_wei = list_random_word_tf_weight[word_icc]
            # finding idfs
            idf_wei = idf_of_all_words[word_icc]
            # finding the temp ans
            temp_ans = tf_wei * idf_wei
            # appending final weight
            list_final_weights.append(temp_ans)
            # increasing vector
            word_icc = word_icc + 1
        # starting list for normalized weight
        complete_normalized_weights = []
        # iterate words
        for every_word in final_set_of_words:
            # condition
            if every_word not in function_temp_file_content:
                # appending zero
                complete_normalized_weights.append(0)
            # writing else part
            else:
                # finding tf weight
                temp_ans = term_frequency_weight[loop_file_name_ins][every_word]
                # appending final answer
                complete_normalized_weights.append(temp_ans)
        # finding last answer
        last_answers = []
        # length of words
        length_words = len(final_set_of_words)
        # loop
        word_icc = 0
        # loop
        while word_icc < length_words:
            #
            ins_wei = list_final_weights[word_icc]
            # finding normalized weight
            ins_nor = complete_normalized_weights[word_icc]
            # finding multiplication
            temp_ans = ins_wei * ins_nor
            # appending final answer
            last_answers.append(temp_ans)
            # increasing vector
            word_icc = word_icc + 1
        # finding sum
        sum_of_cos = sum(last_answers)
        # adding data to list of cosines
        list_of_cosine_similarity.append(sum_of_cos)
        # find the amximum cos simi
        final_val_1 = max(list_of_cosine_similarity)
        # findsing index
        final_index = list_of_cosine_similarity.index(final_val_1)
        # changing value
        final_highest_simi_index = final_index
        # increasing counter
        file_number = file_number + 1
    # checking if zero similarity
    check_simi = list_of_cosine_similarity[final_highest_simi_index]
    # comparing
    if check_simi == 0.0:
        # return 0
        return "Need more fetching", 0
    # writing else part
    else:
        # pick the name of teh file
        temp_file_name = list_of_final_names_of_file[final_highest_simi_index]
        # final name
        final_file_name = temp_file_name.split("/")[1]
        # find simi
        final_simi = list_of_cosine_similarity[final_highest_simi_index]
        # return statement
        return final_file_name, final_simi


# print
print("*"*60)
print("Query Function Run")
print("*"*60)

# running example 1
print("Running query for - pleasing people")
# calling function
print("(%s, %.12f)" % query("pleasing people"))
print("*"*60)

# running example 2
print("Running query for - british war")
# calling function
print("(%s, %.12f)" % query("british war"))
print("*"*60)

# running example 3
print("Running query for - false public")
# calling function
print("(%s, %.12f)" % query("false public"))
print("*"*60)

# running example 4
print("Running query for - people institutions")
# calling function
print("(%s, %.12f)" % query("people institutions"))
print("*"*60)

# running example 5
print("Running query for - violated willingly")
# calling function
print("(%s, %.12f)" % query("violated willingly"))
print("*"*60)
