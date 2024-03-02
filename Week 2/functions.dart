void main() {
  int addTwo(int num1, int num2) {
    return num1 + num2;
  }

  int subtractTwo(int num1, int num2) {
    return num1 - num2;
  }

  int multiplyTwo(int num1, int num2) {
    return num1 * num2;
  }

  double divideTwo(double num1, double num2) {
    return num1 / num2;
  }

  int stringLength(String inputVal) {
    return inputVal.length;
  }

  dynamic getFirstElement(List<dynamic> list) {
    if (list.isNotEmpty) {
      return list[0];
    }
  }
}
