public class MissingNumberFinder {
    public static int findMissingBySum(int[] arr) {
        int n = arr.length + 1;
        long expectedSum = (long) n * (n + 1) / 2;
        long actualSum = 0;
        for (int num : arr) {
            actualSum += num;
        }
        return (int) (expectedSum - actualSum);
    }

    public static int findMissingByXOR(int[] arr) {
        int n = arr.length + 1;
        int xorResult = 0;
        for (int i = 1; i <= n; i++) {
            xorResult ^= i;
        }
        for (int num : arr) {
            xorResult ^= num;
        }
        return xorResult;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5};
        System.out.println(findMissingBySum(arr));
        System.out.println(findMissingByXOR(arr));
    }
}
