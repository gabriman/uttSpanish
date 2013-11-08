UAM Text Tools adaptation to Spanish
Gabriel Rodríguez Rodríguez
1. Learn and try examples with UAM text tools http://utt.amu.edu.pl/
2. Search for a spanish morphologic dictionary
? We found it in the FreeLing project http://nlp.lsi.upc.edu/freeling/
? You can download the tar.gz with the files and search the spanish morphologic
dictionary in FreeLing-2.2.2/data/es/dicc.src
3. Convert our dictionary to the UTT dictionary format, needed for use it in the utt tools.
	3.1 I did a python script for analyze the dictionary and create a new file in the correct
format
	3.2 Before, we have to do a table conversion because there aren’t the same kind of
verbs, prepositions, adverbs... in spanish than in polish
	3.3 In the spanish dicctionary, when we have more than one kind of word for the
same word, the are in the same line. For our new dictionary, same words will be
splitted in different words, with only one word per line
	3.4 This will be the code of the python script. You have to specified the input file and
the name of the output file:

	<Code here, see code files or pdf report>

4. Change program tok (for tokenizer) adding spanish characters and removing polish
characters. We also added “¡” and “¿” characters as punctuation characters. We will
work always with latin1.

	<Code here, see code files or pdf report>

5. For use the “sen” program (for split text in sentences), we add spanish abreviations in
the sen.l file and tried to do that detect the “¿¡” characters like start sentences characters

ab1 (Abg|a.C|d.C|admÃ³n|prof|adm|Arq|Arz|atte|atto|av|avd|avda|Bibl|c|cap|Cap|Cdad|cent|
cent|cÃ³d|Comte|coord|crec|cta|D|D.Âª|diag|dicc|depto|DÃ±a|doc|Dr|Dra|Dr.Âª|dto|edit|EE. UU|
EE.UU|Excmo|Excma|F. C|F.C|Fdo|Gral|Hno|Hna|impto|incl|Ing|Inst|JJ. OO|JJ.OO|Lcdo|Lcda|
Ldo|Lda|Ltd|mÃ¡x|mÃ-n|nÃºm|No|Ob|p|pg|pÃ¡g|pÃ¡rr|P. D|P.D|pdo|ej|pl|plza|ppal|prÃ³l|prov|
pza|Rep|R.I.P|D.E.P|RR. HH|RR.HH|Rte|sig|Srta|tel|telÃ©f|tfno|trad|V|Vd|Vds|V. O|V.O|V. O. S|
V.O.S)

6. For use our diccionary in lem program, we must to compile our dictionary,
because it’s so big for use it directly like text .dic file. We will do it with “compdic”
tool
	6.1 First, we must recode our dicctionary from utf8 to latin1 with “recode u8..l1
file”
	6.2 We also have to edit the compdic program adding new spanish characters
that they are in our dictionary and remove polish characters. The new
compdic file will be like this:

	<Code here, see code files or pdf report>
	
7. We will compile our dictionary with “compdic dicname.dic dicname.bin”
8. We can use the “sen” comand with parameter -d dicname.bin for use the new
dictionary compiled