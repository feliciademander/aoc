
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

// Mix your encrypted file exactly once.

public class Mix {
	static String fname = "input.txt";
	final static int ELEMENTS = (fname == "input.txt") ? 5000 : 7;
	static int[] numbers = new int[ELEMENTS];

	public static void main(String args[]) throws IOException {
		int arguments;

		System.out.println("AOC Day 20");
		arguments = args.length;

		if (arguments > 0) {
			fname = args[0];

			if (arguments > 1) {
				System.out.println("Ignoring " + (arguments - 1) + " arguments");
			}
		}

		read_input();
		mix();
		print_grove_sum();
	}

	private static void read_input() throws IOException {
		int i = 0; // Next empty index in numbers

		try {
			FileInputStream in = new FileInputStream(fname);
			Scanner sc = new Scanner(in);

			// Read lines
			while (sc.hasNextLine()) {
				String line = sc.nextLine();

				// Convert to int and add to array
				if (isNumeric(line) && i < ELEMENTS) {
					try {
						int num = Integer.parseInt(line);
						numbers[i++] = num;
					} catch (NumberFormatException ex) {
						ex.printStackTrace();
					}
				} else if (!line.isEmpty()) {
					System.out.println("Skipped line: " + line);
				}
			}
			sc.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static boolean isNumeric(String str) {
		return str != null && str.matches("^[-]?[0-9]+");
	}

	private static void mix() {
		int value, new_index;
		int[] numbers_copy = numbers.clone();

		// print();

		// Move each number (in original order) forward or backward in the file
		// a number of positions equal to the value of the number being moved
		// TODO: maintain original order of numbers
		for (int index = 0; index < ELEMENTS; index++) {
			value = numbers_copy[index];
			new_index = (index + value) % ELEMENTS;

			// System.out.println("\nMoving value " + value + " (indices " + index + " & " +
			// new_index + "):");
			swap(index, new_index);
			// print();
		}
	}

	// TODO
	private static void swap(int i, int j) {
		if (i == j) {
			return;
		}
		if (i < 0 || i >= ELEMENTS) {
			System.out.println("swap: i out of range");
			return;
		}
		if (j >= ELEMENTS) {
			System.out.println("swap: j out of range");
			return;
		}
		if (j < 0) {
			// System.out.println("swap: resetting j=" + j + " to " + (i + j)); // Debug
			j += i;
		}

		if (j > -1) {
			int temp = numbers[i];
			numbers[i] = numbers[j];
			numbers[j] = temp;
		}
	}

	// What is the sum of the three numbers that form the grove coordinates?
	private static void print_grove_sum() {
		int x = 0, y = 0, z = 0;

		// The grove coordinates can be found by looking at the 1000th, 2000th, and
		// 3000th numbers after the value 0, wrapping around the list as necessary
		for (int i = 0; i < ELEMENTS; i++) {
			if (numbers[i] == 0) {
				x = numbers[(i + 1000) % ELEMENTS];
				y = numbers[(i + 2000) % ELEMENTS];
				z = numbers[(i + 3000) % ELEMENTS];
				System.out.println("\nSum of the grove coordinates: " + (x + y + z));
				break;
			}
		}
	}

	private static void print() {
		for (int n : numbers) {
			System.out.print(n + " ");
		}
		System.out.println();
	}
}
