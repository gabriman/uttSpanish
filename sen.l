%{

  void print_EOS(void);
  void set_position(void);

  int pos=0;
  int len=0;

%}

openQ	[ø]
openE	[°]
ul      [A-Z¡…Õ”⁄—]
ll	[a-z·ÈÌÛ˙Ò]
l       ul|ll
n       [0-9]+
s       [ \t]+



ab1     (Abg|a.C|d.C|adm√≥n|prof|adm|Arq|Arz|atte|atto|av|avd|avda|Bibl|c|cap|Cap|Cdad|cent|cent|c√≥d|Comte|coord|crec|cta|D|D.¬™|diag|dicc|depto|D√±a|doc|Dr|Dra|Dr.¬™|dto|edit|EE. UU|EE.UU|Excmo|Excma|F. C|F.C|Fdo|Gral|Hno|Hna|impto|incl|Ing|Inst|JJ. OO|JJ.OO|Lcdo|Lcda|Ldo|Lda|Ltd|m√°x|m√≠n|n√∫m|No|Ob|p|pg|p√°g|p√°rr|P. D|P.D|pdo|ej|pl|plza|ppal|pr√≥l|prov|pza|Rep|R.I.P|D.E.P|RR. HH|RR.HH|Rte|sig|Srta|tel|tel√©f|tfno|trad|V|Vd|Vds|V. O|V.O|V. O. S|V.O.S)
ab2     (ul|pl|al)

abrv    (ab1|ab2)

SEG     .*\n
N       {n}{s}{n}{s}N{s}.*\n
S       {n}{s}{n}{s}S{s}.*\n
P       {n}{s}{n}{s}P{s}.*\n
W       {n}{s}{n}{s}W{s}.*\n
UL      {n}{s}{n}{s}W{s}{ul}.*\n
Cap     {n}{s}{n}{s}W{s}{ul}{ll}*.*\n
POINT   {n}{s}{n}{s}P{s}\.({s}.*)?\n
QMARK   {n}{s}{n}{s}P{s}\?({s}.*)?\n
EXCL    {n}{s}{n}{s}P{s}\!({s}.*)?\n
DASH    {n}{s}{n}{s}P{s}\-({s}.*)?\n
POINTS  {POINT}+

ABRV    {n}{s}{n}{s}W{s}{abrv}({s}.*)?\n

EOS     {POINT}|{POINTS}|{QMARK}|{EXCL}


%%


{N}({POINT}{N})+          { ECHO; set_position(); }
({UL}{POINT}{S}?)+{Cap}   { ECHO; set_position(); }
{ABRV}{POINT}             { ECHO; set_position(); }


{P}/{S}{DASH}             { ECHO; set_position(); print_EOS(); }
{EOS}/{S}({Cap}|{P}|{N})  { ECHO; set_position(); print_EOS(); }

.*                        { ECHO; set_position(); }

<<EOF>>                   { printf("%04d 00 EOS *\n",pos+len); exit(1); }

%%

int main()
{
  printf("0000 00 BOS *\n");
  yylex();
  return 0;
}

int yywrap()
{
  return 1;
}

void set_position()
{
  char *lastseg;
  char *tmp;

  yytext[yyleng-1] = '\0';

  tmp = strrchr(yytext, '\n');
  if( tmp )
  {
    lastseg = tmp + 1;
  }
  else
  {
    lastseg = yytext;
  }

  sscanf(lastseg, "%d %d", &pos, &len);
  yytext[yyleng-1] = '\n';

}

void print_EOS()
{
  printf("%04d 00 EOS *\n%04d 00 BOS *\n", pos+len, pos+len);
}
