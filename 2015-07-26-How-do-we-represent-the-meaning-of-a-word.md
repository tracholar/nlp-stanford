---
layout: post
title: "How do we represent the meaning of a word"
description: ""
category: "NLP"
tags: ["NLP","deep learning"]
---
![˹̹��CS224d Lecture2](http://cs224d.stanford.edu/lectures/CS224d-Lecture2.pdf)

## �������ô���һ��word?
- ���÷���ϵͳ��wordnet(NLTK)
	- wordnet���մ���(ͬ���)�ʹ��Եı�ﵥ��
	- ���⣺
		- ��Դ�൫��û������
		- �µĵ���
		- ����
		- ��Ҫ�˹�ά��
		- ���Ծ�ȷ���㵥�ʵ����ƶ�
	
- one-hot�������ʱ��Ϊһ������
	- ά�� 20K(speech) 50K(PTB) 500K(big vocab) 13M(Google 1T)

- ���ڷֲ�ʽ���ƶȵı��
	- ���õ��ʵ��ھӱ�ﵥ�ʣ�����NLP��ɹ���idea

- ���������ھӱ��
	- cooccurence matrix
	- full document (Latent Semantic Analysis)
	- window (5-10)
	- eg. �ο�PPT��7ҳ
	- ���⣺ά��̫�ߡ��洢�ռ�̫�ࡢģ��Ϥ�����ȶ�
	- �����ʹ�þ������ֵĵ��ʣ�25-1000ά
	
- ��ά
	- SVD
- ���ʱ����Ϊ��������dense verctor
- hack:
	- ignore the he �ȵ���
	- Pearson ���ƶȶ�����counts
	
[1]An Improved Model of Seman3c Similarity Based on Lexical CoKOccurrence Rohde et al. 2005 

- ֱ��ѧϰ��ά�ĵ�������
	- Learning representa3ons by backKpropaga3ng errors. 
	(Rumelhart et al., 1986) 
	- A neural probabilis3c language model (Bengio et al., 2003)   
	- NLP from Scratch (Collobert & Weston, 2008) 
	- A recent and even simpler model:  
	 word2vec (Mikolov et al. 2013) ! intro now
	 [2]Glove: Global Vectors for Word Representation

## word2vec
- Ԥ�ⳤ��Ϊc�Ĵ������ÿһ������
- Ŀ�꺯�������ÿһ�������ڸ��������ĵ����µ��ܸ���
![J](word2vec001.png)

	 