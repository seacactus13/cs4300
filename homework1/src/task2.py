def demonstrate_data_types():
    integer_var = 42
    float_var = 3.14
    string_var = "Python"
    bool_var = True
    return integer_var, float_var, string_var, bool_var

def main():
    integer_var, float_var, string_var, bool_var = demonstrate_data_types()
    print("Integer:", integer_var)
    print("Float:", float_var)
    print("String:", string_var)
    print("Boolean:", bool_var)

if __name__ == "__main__":
    main()
