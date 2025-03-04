grammar MatchingLanguage;
// java -jar /home/giacomo/Scaricati/antlr-4.13.2-complete.jar -visitor  -Dlanguage=Python3 MatchingLanguage.g4
language: (rule ';')+;

rule: NESTED? MATCHING query=object
       (EXTEND (extension ',')+ extension )?
       (WHERE prop)?
       (replacement)*
       AS (object|variable|jpath)
      ;

prop: LPAR prop RPAR #p_par
    | prop AND prop  #p_and
    | prop OR  prop  #p_or
    | prop IMPL prop #p_impl
    | NOT prop       #p_not
    | prop EQ EMPTY  #p_isempty
    | prop EQ prop   #p_eq
    | prop NEQ prop   #p_neq
    | prop LEQ prop   #p_leq
    | prop LT prop   #p_lt
    | prop GEQ prop   #p_geq
    | prop GT prop   #p_gt
    | prop ISIN prop #p_gt
    | variable       #p_var
    | jpath          #p_jpath
    | PYTHON STRING  #p_json
    ;

extension: fun=STRING OVERMODULE module=STRING;
object: ALPHANAME LPAR ((object ',')+ object)? RPAR  OVERMODULE module=STRING                     #actual_object
      | ALPHANAME LPAR ((STRING EQ object ',')+ STRING EQ object)? RPAR  OVERMODULE module=STRING #actual_tuple_of_type_and_args
      |  variable                                                                                 #actual_variable
      |  IGNORE                                                                                   #ignoring_argument
      ;
jpath : JSONPATH STRING;
variable: 'var' LPAR ALPHANAME RPAR ;
replacement: REPLACE repl=variable|jpath WITH as=object|variable|jpath;

AS: 'as';
VAR: 'var';
MATCHING: 'match';
NESTED: 'nested';
WHERE: 'where';
EXTEND: 'extend-with';
REPLACE: 'replace';
WITH: 'with';
OVERMODULE: 'in-module';
AND: '&&';
OR: '||';
LEQ: '⩽'|'≤';
GEQ: '≥'|'⩾';
LT: '<';
GT: '>';
IMPL: '→';
LPAR: '(';
RPAR: ')';
NEQ: '≠';
NOT: '!';
EQ: '=';
ISIN: '∈';
EMPTY: '∅';
JSONPATH: 'jsonpath';
PYTHON: 'python';
ALPHANAME: [a-zA-Z]+;
IGNORE: '_';

STRING : '"' (~[\\"] | '\\' [\\"])* '"';
SPACE : [ \t\r\n]+ -> skip;

COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;
