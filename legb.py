# LEGB Rules

# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-In

a = 1  # G


def f():
    b = 1  # E

    def g():
        b = 100  # L
        print(b)
        print(__name__)  # B
    b = 20
    g()

f()

