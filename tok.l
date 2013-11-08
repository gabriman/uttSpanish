%{
	#include <stdio.h>
	#include <locale.h>
	#include "tok_cmdline.h"

	int filepos=0;

	struct gengetopt_args_info args;

%}


%%

[a-zA-Z·¡È…ÌÕÛ”˙⁄¸‹Ò—]{1,64}	{
					printf("%04d %02d W %s\n", filepos, yyleng, yytext);
					filepos+=yyleng;
					if(args.interactive_flag) fflush(stdout);
				}

[[:digit:]]{1,64}		{
					printf("%04d %02d N %s\n", filepos, yyleng, yytext);
					filepos+=yyleng;
					if(args.interactive_flag) fflush(stdout);
				}

[[:space:]\n]{1,64}			{
					int i;
					printf("%04d %02d S ", filepos, yyleng);
					for(i=0; i<yyleng; ++i)
						switch(yytext[i])
						{
							case ' ' : putchar('_'); break;
							case '\t': printf("\\t"); break;
							case '\n': printf("\\n"); break;
							case '\r': printf("\\t"); break;
							case '\f': printf("\\n"); break;
						}
					putchar('\n');
					filepos+=yyleng;
					if(args.interactive_flag) fflush(stdout);
				}

[[:punct:]]			{
					printf("%04d %02d P %c\n", filepos, yyleng, *yytext);
					filepos+=yyleng;
					if(args.interactive_flag) fflush(stdout);
				}

[°ø]				{
					printf("%04d %02d P %c\n", filepos, yyleng, *yytext);
					filepos+=yyleng;
					if(args.interactive_flag) fflush(stdout);
				}

.				{
					printf("%04d %02d B \\x%02X\n", filepos, yyleng, (unsigned char)*yytext);
					filepos+=yyleng;
					if(args.interactive_flag) fflush(stdout);
				}

%%

int main(int argc, char** argv)
{
  if (cmdline_parser(argc, argv, &args) != 0) return 1;
  setlocale(LC_CTYPE,"");
  setlocale(LC_COLLATE,"");
  yylex();
  return 0;
}

int yywrap()
{
	return 1;
}

