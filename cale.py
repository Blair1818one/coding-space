def calculate_rectangle_properties(length, width):
    area = length * width
    premeter = 2 * (length + width)
    return area, premeter
def main():
    length = float(input("Enter the length of the rectangle:"))
    width = float(input("Enter the width of rectangle:"))
    area, premeter = calculate_rectangle_properties(length, width)
    print(f"Area: {area}")
    print(f"premeter: {premeter}")
if __name__=="__main__":
    main()
