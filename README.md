# Readable pylint messages 
Prepared with `pylint --list-msgs` for pylint v1.6.4
##blacklisted-name 
####C0102 - Black listed name "%s" 
Used when the name is listed in the black list (unauthorized names). 
##invalid-name 
####C0103 - Invalid %s name "%s"%s 
Used when the name doesn't match the regular expression associated to its type
  (constant, variable, class...). 
##missing-docstring 
####C0111 - Missing %s docstring 
Used when a module, function, class or method has no docstring.Some special
  methods like __init__ doesn't necessary require a docstring. 
##empty-docstring 
####C0112 - Empty %s docstring 
Used when a module, function, class or method has an empty docstring (it would
  be too easy 
##unneeded-not 
####C0113 - Consider changing "%s" to "%s" 
Used when a boolean expression contains an unneeded negation. 
##singleton-comparison 
####C0121 - Comparison to %s should be %s 
Used when an expression is compared to singleton values like True, False or
  None. 
##misplaced-comparison-constant 
####C0122 - Comparison should be %s 
Used when the constant is placed on the left sideof a comparison. It is
  usually clearer in intent to place it in the right hand side of the
  comparison. 
##consider-using-enumerate 
####C0200 - Consider using enumerate instead of iterating with range and len 
Emitted when code that iterates with range and len is encountered. Such code
  can be simplified by using the enumerate builtin. 
##bad-classmethod-argument 
####C0202 - Class method %s should have %s as first argument 
Used when a class method has a first argument named differently than the value
  specified in valid 
##bad-mcs-method-argument 
####C0203 - Metaclass method %s should have %s as first argument 
Used when a metaclass method has a first agument named differently than the
  value specified in valid 
##bad-mcs-classmethod-argument 
####C0204 - Metaclass class method %s should have %s as first argument 
Used when a metaclass class method has a first argument named differently than
  the value specified in valid 
##trailing-whitespace 
####C0303 - Trailing whitespace 
Used when there is whitespace between the end of a line and the newline. 
##missing-final-newline 
####C0304 - Final newline missing 
Used when the last line in a file is missing a newline. 
##trailing-newlines 
####C0305 - Trailing newlines 
Used when there are trailing blank lines in a file. 
##multiple-statements 
####C0321 - More than one statement on a single line 
Used when more than on statement are found on the same line. 
##superfluous-parens 
####C0325 - Unnecessary parens after %r keyword 
Used when a single item in parentheses follows an if, for, or other keyword. 
##bad-whitespace 
####C0326 - %s space %s %s %s 
Used when a wrong number of spaces is used around an operator, bracket or
  block opener. 
##mixed-line-endings 
####C0327 - Mixed line endings LF and CRLF 
Used when there are mixed (LF and CRLF) newline signs in a file. 
##invalid-characters-in-docstring 
####C0403 - Invalid characters %r in a docstring 
Used when a word in docstring cannot be checked by enchant. 
##wrong-import-order 
####C0411 - %s comes before %s 
Used when PEP8 import order is not respected (standard imports first, then
  third 
##ungrouped-imports 
####C0412 - Imports from package %s are not grouped 
Used when imports are not grouped by packages 
##wrong-import-position 
####C0413 - Import "%s" should be placed at the top of the module 
Used when code and imports are mixed 
##unrecognized-inline-option 
####E0011 - Unrecognized file option %r 
Used when an unknown inline option is encountered. 
##bad-option-value 
####E0012 - Bad option value %r 
Used when a bad value for an inline option is encountered. 
##init-is-generator 
####E0100 - __init__ method is a generator 
Used when the special class method __init__ is turned into a generator by a
  yield in its body. 
##return-in-init 
####E0101 - Explicit return in __init__ 
Used when the special class method __init__ has an explicit return value. 
##function-redefined 
####E0102 - %s already defined line %s 
Used when a function 
##not-in-loop 
####E0103 - %r not properly in loop 
Used when break or continue keywords are used outside a loop. 
##return-outside-function 
####E0104 - Return outside function 
Used when a 
##yield-outside-function 
####E0105 - Yield outside function 
Used when a 
##return-arg-in-generator 
####E0106 - Return with argument inside generator 
Used when a 
##duplicate-argument-name 
####E0108 - Duplicate argument name %s in function definition 
Duplicate argument names in function definitions are syntax errors. 
##abstract-class-instantiated 
####E0110 - Abstract class %r with abstract methods instantiated 
Used when an abstract class with 
##method-hidden 
####E0202 - An attribute defined in %s line %s hides this method 
Used when a class defines a method which is hidden by an instance attribute
  from an ancestor class or set by some client code. 
##access-member-before-definition 
####E0203 - Access to member %r before its definition line %s 
Used when an instance member is accessed before it's actually assigned. 
##no-method-argument 
####E0211 - Method has no argument 
Used when a method which should have the bound instance as first argument has
  no argument defined. 
##no-self-argument 
####E0213 - Method should have "self" as first argument 
Used when a method has an attribute different the 
##assigning-non-slot 
####E0237 - Assigning to attribute %r not defined in class slots 
Used when assigning to an attribute not defined in the class slots. 
##invalid-slots 
####E0238 - Invalid __slots__ object 
Used when an invalid __slots__ is found in class. Only a string, an iterable
  or a sequence is permitted. 
##inconsistent-mro 
####E0240 - Inconsistent method resolution order for class %r 
Used when a class has an inconsistent method resolutin order. 
##duplicate-bases 
####E0241 - Duplicate bases for class %r 
Used when a class has duplicate bases. 
##import-error 
####E0401 - Unable to import %s 
Used when pylint has been unable to import a module. 
##used-before-assignment 
####E0601 - Using variable %r before assignment 
Used when a local variable is accessed before it's assignment. 
##undefined-variable 
####E0602 - Undefined variable %r 
Used when an undefined variable is accessed. 
##undefined-all-variable 
####E0603 - Undefined variable name %r in __all__ 
Used when an undefined variable name is referenced in __all__. 
##no-name-in-module 
####E0611 - No name %r in module %r 
Used when a name cannot be found in a module. 
##raising-bad-type 
####E0702 - Raising %s while only classes or instances are allowed 
Used when something which is neither a class, an instance or a string is
  raised (i.e. a 
##misplaced-bare-raise 
####E0704 - The raise statement is not inside an except clause 
Used when a bare raise is not used inside an except clause. This generates an
  error, since there are no active exceptions to be reraised. An exception to
  this rule is represented by a bare raise inside a finally clause, which might
  work, as long as an exception is raised inside the try block, but it is
  nevertheless a code smell that must not be relied upon. 
##slots-on-old-class 
####E1001 - Use of __slots__ on an old style class 
Used when an old style class uses the __slots__ attribute. This message can't
  be emitted when using Python 
##super-on-old-class 
####E1002 - Use of super on an old style class 
Used when an old style class uses the super builtin. This message can't be
  emitted when using Python 
##no-member 
####E1101 - %s %r has no %r member 
Used when a variable is accessed for an unexistent member. 
##not-callable 
####E1102 - %s is not callable 
Used when an object being called has been inferred to a non callable object 
##no-value-for-parameter 
####E1120 - No value for argument %s in %s call 
Used when a function call passes too few arguments. 
##too-many-function-args 
####E1121 - Too many positional arguments for %s call 
Used when a function call passes too many positional arguments. 
##unexpected-keyword-arg 
####E1123 - Unexpected keyword argument %r in %s call 
Used when a function call passes a keyword argument that doesn't correspond to
  one of the function's parameter names. 
##redundant-keyword-arg 
####E1124 - Argument %r passed by position and keyword in %s call 
Used when a function call would result in assigning multiple values to a
  function parameter, one value from a positional argument and one from a
  keyword argument. 
##assignment-from-none 
####E1128 - Assigning to function call which only returns None 
Used when an assignment is done on a function call but the inferred function
  returns nothing but None. 
##repeated-keyword 
####E1132 - Got multiple values for keyword argument %r in function call 
Emitted when a function call got multiple values for a keyword. 
##logging-format-truncated 
####E1201 - Logging format string ends in middle of conversion specifier 
Used when a logging statement format string terminates before the end of a
  conversion specifier. 
##logging-too-many-args 
####E1205 - Too many arguments for logging format string 
Used when a logging format string is given too few arguments. 
##logging-too-few-args 
####E1206 - Not enough arguments for logging format string 
Used when a logging format string is given too many arguments 
##truncated-format-string 
####E1301 - Format string ends in middle of conversion specifier 
Used when a format string terminates before the end of a conversion specifier. 
##mixed-format-string 
####E1302 - Mixing named and unnamed conversion specifiers in format string 
Used when a format string contains both named (e.g. ' 
##missing-format-string-key 
####E1304 - Missing key %r in format string dictionary 
Used when a format string that uses named conversion specifiers is used with a
  dictionary that doesn't contain all the keys required by the format string. 
##too-many-format-args 
####E1305 - Too many arguments for format string 
Used when a format string that uses unnamed conversion specifiers is given too
  many arguments. 
##too-few-format-args 
####E1306 - Not enough arguments for format string 
Used when a format string that uses unnamed conversion specifiers is given too
  few arguments 
##print-statement 
####E1601 - print statement used 
Used when a print statement is used ( 
##parameter-unpacking 
####E1602 - Parameter unpacking specified 
Used when parameter unpacking is specified for a function(Python 3 doesn't
  allow it) This message can't be emitted when using Python 
##unpacking-in-except 
####E1603 - Implicit unpacking of exceptions is not supported in Python 3 
Python3 will not allow implicit unpacking of exceptions in except clauses. See
  http 
##long-suffix 
####E1606 - Use of long suffix 
Used when 
##old-octal-literal 
####E1608 - Use of old octal literal 
Usen when encountering the old octal syntax, removed in Python 3. To use the
  new syntax, prepend 0o on the number. This message can't be emitted when using
  Python 
##bad-inline-option 
####I0010 - Unable to consider inline option %r 
Used when an inline option is either badly formatted or can't be used inside
  modules. 
##file-ignored 
####I0013 - Ignoring entire file 
Used to inform that the file will not be checked 
##useless-suppression 
####I0021 - Useless suppression of %s 
Reported when a message is explicitly disabled for a line or a block of code,
  but never triggered. 
##simplifiable-if-statement 
####R0102 - The if statement can be replaced with %s 
Used when an if statement can be replaced with 'bool(test)'. 
##no-self-use 
####R0201 - Method could be a function 
Used when a method doesn't use its bound instance, and so could be written as
  a function. 
##no-classmethod-decorator 
####R0202 - Consider using a decorator instead of calling classmethod 
Used when a class method is defined without using the decorator syntax. 
##no-staticmethod-decorator 
####R0203 - Consider using a decorator instead of calling staticmethod 
Used when a static method is defined without using the decorator syntax. 
##redefined-variable-type 
####R0204 - Redefinition of %s type from %s to %s 
Used when the type of a variable changes inside a method or a function. 
##duplicate-code 
####R0801 - Similar lines in %s files 
Indicates that a set of similar lines has been detected among multiple file.
  This usually means that the code should be refactored to avoid this
  duplication. 
##unreachable 
####W0101 - Unreachable code 
Used when there is some code behind a 
##dangerous-default-value 
####W0102 - Dangerous default value %s as argument 
Used when a mutable value as list or dictionary is detected in a default value
  for an argument. 
##pointless-statement 
####W0104 - Statement seems to have no effect 
Used when a statement doesn't have (or at least seems to) any effect. 
##pointless-string-statement 
####W0105 - String statement has no effect 
Used when a string is used as a statement (which of course has no effect).
  This is a particular case of W0104 with its own message so you can easily
  disable it if you're using those strings as documentation, instead of
  comments. 
##expression-not-assigned 
####W0106 - Expression "%s" is assigned to nothing 
Used when an expression that is not a function call is assigned to nothing.
  Probably something else was intended. 
##unnecessary-pass 
####W0107 - Unnecessary pass statement 
Used when a 
##unnecessary-lambda 
####W0108 - Lambda may not be necessary 
Used when the body of a lambda expression is a function call on the same
  argument list as the lambda itself 
##duplicate-key 
####W0109 - Duplicate key %r in dictionary 
Used when a dictionary expression binds the same key multiple times. 
##useless-else-on-loop 
####W0120 - Else clause on loop without a break statement 
Loops should only have an else clause if they can exit early with a break
  statement, otherwise the statements under else should be on the same scope as
  the loop itself. 
##exec-used 
####W0122 - Use of exec 
Used when you use the 
##eval-used 
####W0123 - Use of eval 
Used when you use the 
##using-constant-test 
####W0125 - Using a conditional statement with a constant value 
Emitted when a conditional statement (If or ternary if) uses a constant value
  for its test. This might not be what the user intended to do. 
##lost-exception 
####W0150 - %s statement in finally block may swallow exception 
Used when a break or a return statement is found inside the finally clause of
  a try...finally block 
##attribute-defined-outside-init 
####W0201 - Attribute %r defined outside __init__ 
Used when an instance attribute is defined outside the __init__ method. 
##bad-staticmethod-argument 
####W0211 - Static method with %r as first argument 
Used when a static method has 
##protected-access 
####W0212 - Access to a protected member %s of a client class 
Used when a protected member (i.e. class member with a name beginning with an
  underscore) is access outside the class or a descendant of the class where
  it's defined. 
##arguments-differ 
####W0221 - Arguments number differs from %s %r method 
Used when a method has a different number of arguments than in the implemented
  interface or in an overridden method. 
##signature-differs 
####W0222 - Signature differs from %s %r method 
Used when a method signature is different than in the implemented interface or
  in an overridden method. 
##abstract-method 
####W0223 - Method %r is abstract in class %r but is not overridden 
Used when an abstract method (i.e. raise NotImplementedError) is not
  overridden in concrete class. 
##super-init-not-called 
####W0231 - __init__ method from base class %r is not called 
Used when an ancestor class method has an __init__ method which is not called
  by a derived class. 
##no-init 
####W0232 - Class has no __init__ method 
Used when a class has no __init__ method, neither its parent classes. 
##non-parent-init-called 
####W0233 - __init__ method from a non direct base class %r is called 
Used when an __init__ method is called on a class which is not in the direct
  ancestors for the analysed class. 
##unnecessary-semicolon 
####W0301 - Unnecessary semicolon 
Used when a statement is ended by a semi 
##mixed-indentation 
####W0312 - Found indentation with %ss instead of %ss 
Used when there are some mixed tabs and spaces in a module. 
##lowercase-l-suffix 
####W0332 - Use of "l" as long integer identifier 
Used when a lower case 
##wildcard-import 
####W0401 - Wildcard import %s 
Used when 
##deprecated-module 
####W0402 - Uses of a deprecated module %r 
Used a module marked as deprecated is imported. 
##import-self 
####W0406 - Module import itself 
Used when a module is importing itself. 
##misplaced-future 
####W0410 - __future__ import is not the first non docstring statement 
Python 2.5 and greater require __future__ import to be the first non docstring
  statement in the module. 
##global-variable-undefined 
####W0601 - Global variable %r undefined at the module level 
Used when a variable is defined through the 
##global-variable-not-assigned 
####W0602 - Using global for %r but no assignment is done 
Used when a variable is defined through the 
##global-statement 
####W0603 - Using the global statement 
Used when you use the 
##global-at-module-level 
####W0604 - Using the global statement at the module level 
Used when you use the 
##unused-import 
####W0611 - Unused %s 
Used when an imported module or variable is not used. 
##unused-variable 
####W0612 - Unused variable %r 
Used when a variable is defined but not used. 
##unused-argument 
####W0613 - Unused argument %r 
Used when a function or method argument is not used. 
##unused-wildcard-import 
####W0614 - Unused import %s from wildcard import 
Used when an imported module or variable is not used from a 
##redefine-in-handler 
####W0623 - Redefining name %r from %s in exception handler 
Used when an exception handler assigns the exception to an existing name 
##undefined-loop-variable 
####W0631 - Using possibly undefined loop variable %r 
Used when an loop variable (i.e. defined by a for loop or a list comprehension
  or a generator expression) is used outside the loop. 
##cell-var-from-loop 
####W0640 - Cell variable %s defined in loop 
A variable used in a closure is defined in a loop. This will result in all
  closures using the same value for the closed 
##broad-except 
####W0703 - Catching too general exception %s 
Used when an except catches a too general exception, possibly burying
  unrelated errors. 
##duplicate-except 
####W0705 - Catching previously caught exception type %s 
Used when an except catches a type that was already caught by a previous
  handler. 
##binary-op-exception 
####W0711 - Exception to catch is the result of a binary "%s" operation 
Used when the exception to catch is of the form 
##property-on-old-class 
####W1001 - Use of "property" on an old style class 
Used when Pylint detect the use of the builtin 
##logging-not-lazy 
####W1201 - Specify string format arguments as logging function parameters 
Used when a logging statement has a call form of 
##logging-format-interpolation 
####W1202 - Use % formatting in logging functions and pass the % parameters as arguments 
Used when a logging statement has a call form of 
##unused-format-string-key 
####W1301 - Unused key %r in format string dictionary 
Used when a format string that uses named conversion specifiers is used with a
  dictionary that contains keys not required by the format string. 
##bad-format-string 
####W1302 - Invalid format string 
Used when a PEP 3101 format string is invalid. This message can't be emitted
  when using Python 
##missing-format-argument-key 
####W1303 - Missing keyword argument %r for format string 
Used when a PEP 3101 format string that uses named fields doesn't receive one
  or more required keywords. This message can't be emitted when using Python 
##unused-format-string-argument 
####W1304 - Unused format argument %r 
Used when a PEP 3101 format string that uses named fields is used with an
  argument that is not required by the format string. This message can't be
  emitted when using Python 
##format-combined-specification 
####W1305 - Format string contains both automatic field numbering and manual field specification 
Usen when a PEP 3101 format string contains both automatic field numbering
  (e.g. ' 
##missing-format-attribute 
####W1306 - Missing format attribute %r in format specifier %r 
Used when a PEP 3101 format string uses an attribute specifier ( 
##invalid-format-index 
####W1307 - Using invalid lookup key %r in format specifier %r 
Used when a PEP 3101 format string uses a lookup specifier ( 
##redundant-unittest-assert 
####W1503 - Redundant use of %s with constant value %r 
The first argument of assertTrue and assertFalse is a condition. If a constant
  is passed as parameter, that condition will be always true. In this case a
  warning should be emitted. 
##coerce-method 
####W1614 - __coerce__ method defined 
Used when a __coerce__ method is defined (method is not used by Python 3) This
  message can't be emitted when using Python 
##delslice-method 
####W1615 - __delslice__ method defined 
Used when a __delslice__ method is defined (method is not used by Python 3)
  This message can't be emitted when using Python 
##getslice-method 
####W1616 - __getslice__ method defined 
Used when a __getslice__ method is defined (method is not used by Python 3)
  This message can't be emitted when using Python 
##setslice-method 
####W1617 - __setslice__ method defined 
Used when a __setslice__ method is defined (method is not used by Python 3)
  This message can't be emitted when using Python 
##indexing-exception 
####W1624 - Indexing exceptions will not work on Python 3 
Indexing exceptions will not work on Python 3. Use 
##raising-string 
####W1625 - Raising a string exception 
Used when a string exception is raised. This will not work on Python 3. This
  message can't be emitted when using Python 
##oct-method 
####W1627 - __oct__ method defined 
Used when a __oct__ method is defined (method is not used by Python 3) This
  message can't be emitted when using Python 
##hex-method 
####W1628 - __hex__ method defined 
Used when a __hex__ method is defined (method is not used by Python 3) This
  message can't be emitted when using Python 
##nonzero-method 
####W1629 - __nonzero__ method defined 
Used when a __nonzero__ method is defined (method is not used by Python 3)
  This message can't be emitted when using Python 
##cmp-method 
####W1630 - __cmp__ method defined 
Used when a __cmp__ method is defined (method is not used by Python 3) This
  message can't be emitted when using Python 
