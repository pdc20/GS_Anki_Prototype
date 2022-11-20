# Google Sheets to Anki Prototype
Yeah I know the title is generic but this is just a prototype. I'll deal with that later.

This is a custom app that lets you join two CSV files where the first has a column that has IDs of rows in the second file (analogous to foreign keys in database entities).

For example, suppose one CSV file named `words.csv` has the following data
```
Kanji, Hiragana, Meaning, SentenceID
入り口, いりぐち, Entrance, 1
, ある, To exist, 1
```
and suppose we have another CSV file named `sentences.csv` that has the following data
```
ID, Sentence, Translation (English)
1, 私の家は入り口がありません。, My house doesn't have an entrance.
```
Then the program will output the following CSV file:
```
Kanji, Hiragana, Meaning, Sentence, Translation (English)
入り口, いりぐち, Entrance, 私の家は入り口がありません。, My house doesn't have an entrance.
ある, ある, To exist, 私の家は入り口がありません。, My house doesn't have an entrance.
```
This saves you the hassle of copy-pasting the same sentences and their translations over multiple word entries. You only need to write the ID of the sentence you want to reference. 

Notice how word entries with no kanji are automatically filled in with the corresponding Hiragana. This saves you the need to copy paste or repeat typing the word in.
