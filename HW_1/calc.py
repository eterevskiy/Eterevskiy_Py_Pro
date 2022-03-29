import ast
import re
pi=3.14
e=2.71
operators=['*','**','//','/','+','-','%']
def input_number() :
    while True :
        try :
            number=input("enter num :").strip().replace(',', '.')
            if re.fullmatch('[-+]?(?:\d+(?:\.\d*)?|\.\d+)|(\bpi|\be)',number):
                break
            raise Exception("Invalid value")
        except Exception as err:
            print(str(err))
    return number
def input_operator() :
    while True :
        try :
            operator=input("enter op :").strip()
            if re.fullmatch('[*/]{,2}|[-+%]',operator):
                break
            raise Exception("Invalid value")
        except Exception as err:
            print(str(err))
    return operator
def create_expression(num:int):
    if num==1:
        a=input_number()
        b=input_number()
        op=input_operator()
        return a+op+b
    elif num==2 :
        col=int(input("enter element count :"))
        expression=''
        for i in range(col) :
                expression+=input_number()
                if i!=col-1 :
                    expression+=input_operator()
        return expression
    elif num==3 :
        expression=input("enter expression :").strip().replace(',', '.')
        return expression

class MyOptimizer(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name):
        if node.id == 'pi':
            result = ast.Num(n=pi)
            result.lineno = node.lineno
            result.col_offset = node.col_offset
            return result
        elif node.id == 'e' :
            result = ast.Num(n=e)
            result.lineno = node.lineno
            result.col_offset = node.col_offset
            return result
        return node
def main(expression):
    try:
        tree = ast.parse(f"print({expression})")
        optimizer = MyOptimizer()
        tree = optimizer.visit(tree)
        code = compile(tree, "<string>", "exec")
        exec(code)
    except :
        print("Invalid expression")

if __name__=="__main__" :
    print("1)2 operands\n2)multiple operands\n3)expression")
    while True :
        try :
            num=input("select calculator :")
            if re.findall(r'[1-3]', num) :
                break
            raise Exception("Invalid value")
        except Exception as err:
                print(str(err))
    main(create_expression(int(num)))