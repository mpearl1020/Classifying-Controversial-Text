## Data 

__Trigger Warning__: Some data in the attached dataset contains hateful, obscene, and/or threatening text.

Our data is a modified subset of the data available under CC licensing from the Kaggle dataset on Toxic Comment Classification. 

The data is divided into train, validation, and test sets on a respective 80/10/10 split. 

The data is formatted into 4 columns [index, id, comment\_text, contro]. The *index* is the corresponding index for the row. The *id* is the unique ASCII representation for that comment across all the data. The *comment_text* is the sentence/comment that will be treated as the sentence for which we will be predicting if it is controversial. The last column *contro* serves as the boolean indication, 0 (not controversial), 1 (controversial), of whether or not the corresponding *comment_text* can be considered controversial. 

Example header (Top 5 lines):
[index, id, comment\_text, contro]
[0, 000f35deef84dc4a, 'There's no need to apologize. A...', 0]
[1, 0016e01b742b8da3, 'Notability of Rurika Ka...', 0]
[2, 00b984b355cc9754, 'I'm focussing on doing science...', 0]
[3, 0a19319ca119d890, 'He's not a retired, he was just useless.', 1]


