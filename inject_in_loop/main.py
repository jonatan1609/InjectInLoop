if __name__ == '__main__':
    from inject_in_loop import Base
    from time import sleep

    class PrintNewLine(Base):
        function = print

    class Sleep(Base):
        function = sleep


    class Mixin(Base):
        functions = [sleep, print]

    for Sleep(0.3).range1.range2 in zip(range(10), range(10)):
        print(range1 + range2, "[obj.a.b] a + b")

    print("-" * 15)

    for Sleep(0.3).a_index, b_index in zip(range(10), range(10)):
        print(a_index * b_index, "[obj.a, b] a * b")

    print("-" * 15)

    for Sleep(0.3).index in zip(range(10), range(10)):
        print(index, "[obj.a] a")

    print("\nThe next for loop will print a new line in each iteration:")

    for PrintNewLine().item in ("a", "b", "c"):
        print(item)

    for Mixin(f_params={"sleep": (1,),"print": ()}).element in range(10):
        print(element)

    for Sleep(0.3, unpack="b").a.b.c in [["a", "b", "c", "d"]]*5:
        print(a, b, c)