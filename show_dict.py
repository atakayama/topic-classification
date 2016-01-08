#!/usr/local/bin/python
#coding:utf-8

import matplotlib.pyplot as plt;
import numpy as np;
from gensim import corpora;
from optparse import OptionParser;

'''
 棒グラフを表示します。
'''
def show_bar_graph(labels, values, title):
	index = np.arange(len(labels));
	plt.figure();
	plt.title(title.decode("utf-8"));
	plt.bar(index, values);
	plt.xticks(index+0.4, labels);
	plt.show();

'''
 辞書に含まれる単語のヒストグラムを作成
'''
def show_dict_data(dictionary, title, num_tops=15):
	labels=[];
	values=[];
	for k, v in sorted(dictionary.dfs.items(), key=lambda x:x[1], reverse=True):
		labels.append(dictionary.get(k));
		values.append(v);
	show_bar_graph(labels[0:num_tops], values[0:num_tops], title);

'''
 エントリポイント
'''
if (__name__ == "__main__"):
	# 引数指定
	optParser = OptionParser();
	optParser.add_option("-d", dest="dict_file", default="work/dictionary");
	optParser.add_option("-t", dest="title", default="アンケートワード");
	(options, args) = optParser.parse_args();
	print("dictionary=%s" % (options.dict_file));

	num_tops = 25;
	show_dict_data(corpora.Dictionary.load_from_text(options.dict_file), options.title + "(top%d)" % (num_tops), num_tops);
