#include <stdint.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h> // Для UTF-8

int main() {

    SetConsoleOutputCP(CP_UTF8);    // А вот и UTF-8 части
    SetConsoleCP(CP_UTF8);          // Для нормального вывода в терминал

    srand(time(NULL));
    int num = rand() % 101;
    printf("Это первая сделанная мной игра на C!\nАвтор MichiTheCat\nТГ: https://t.me/TeaTechnology\nЗагадано число от 0 до 100!\n");
    
    while (1) {
        int usr;
        printf("\nВведите предполагаемое число: ");
        scanf("%d", &usr);
        if (usr == num) {
            printf("\nВы угадали!");
            break;
        } else if (num < usr) {
            printf("\nЗагадано число меньше");
        } else if (num > usr) {
            printf("\nЗагадано число больше");
        }
    }
    
    scanf("\nОтгадано! ");
    return 0;
}