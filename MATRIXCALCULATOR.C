#include <stdio.h>

// Function to add two matrices
void addMatrices(int rows, int cols, int mat1[][10], int mat2[][10], int result[][10]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = mat1[i][j] + mat2[i][j];
        }
    }
}

// Function to subtract two matrices
void subtractMatrices(int rows, int cols, int mat1[][10], int mat2[][10], int result[][10]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = mat1[i][j] - mat2[i][j];
        }
    }
}

// Function to multiply two matrices
void multiplyMatrices(int rows1, int cols1, int rows2, int cols2, int mat1[][10], int mat2[][10], int result[][10]) {
    if (cols1 != rows2) {
        printf("Cannot multiply: Columns of first matrix must equal rows of second.\n");
        return;
    }
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < cols1; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

// Function to print a matrix
void printMatrix(int rows, int cols, int mat[][10]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
}

// Function to input a matrix
void inputMatrix(int rows, int cols, int mat[][10]) {
    printf("Enter the elements:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &mat[i][j]);
        }
    }
}

int main() {
    int choice;
    int rows1, cols1, rows2, cols2;
    int mat1[10][10], mat2[10][10], result[10][10];

    printf("Welcome to Matrix Calculator!\n");
    printf("Matrices up to 10x10 size.\n");

    while (1) {
        printf("\nMenu:\n");
        printf("1. Add two matrices\n");
        printf("2. Subtract two matrices\n");
        printf("3. Multiply two matrices\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        if (choice == 4) {
            break;
        }

        if (choice == 1 || choice == 2) {
            printf("Enter rows and columns for matrices: ");
            scanf("%d %d", &rows1, &cols1);
            rows2 = rows1;
            cols2 = cols1;

            printf("Enter first matrix:\n");
            inputMatrix(rows1, cols1, mat1);

            printf("Enter second matrix:\n");
            inputMatrix(rows2, cols2, mat2);

            if (choice == 1) {
                addMatrices(rows1, cols1, mat1, mat2, result);
                printf("Result:\n");
                printMatrix(rows1, cols1, result);
            } else {
                subtractMatrices(rows1, cols1, mat1, mat2, result);
                printf("Result:\n");
                printMatrix(rows1, cols1, result);
            }
        } else if (choice == 3) {
            printf("Enter rows and columns for first matrix: ");
            scanf("%d %d", &rows1, &cols1);

            printf("Enter rows and columns for second matrix: ");
            scanf("%d %d", &rows2, &cols2);

            if (cols1 != rows2) {
                printf("Cannot multiply these matrices.\n");
                continue;
            }

            printf("Enter first matrix:\n");
            inputMatrix(rows1, cols1, mat1);

            printf("Enter second matrix:\n");
            inputMatrix(rows2, cols2, mat2);

            multiplyMatrices(rows1, cols1, rows2, cols2, mat1, mat2, result);
            printf("Result:\n");
            printMatrix(rows1, cols2, result);
        } else {
            printf("Invalid choice.\n");
        }
    }

    printf("Goodbye!\n");
    return 0;
}