#include <stdint.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
    srand(time(NULL));
    printf("Это вторая сделанная мной игра на C!\nАвтор MichiTheCat\nТГ: https://t.me/TeaTechnology\nДобро пожаловать в Подземелье!\n");

    int usr;    // Козёл отпущения всех scanf в коде
    while (1) {         // Основное меню
        printf("\n1. Спуститься в подземелье\n2. Информация\n3. Выйти\n> ");
        scanf("%d", &usr);
        if (usr == 1) {
            break;
        } else if (usr == 2) {
            printf("\nЭто вторая сделанная мной игра на C!\nАвтор MichiTheCat\nТГ: https://t.me/TeaTechnology\nДобро пожаловать в Подземелье!\n");
        } else if (usr == 3) {
            break;
        } else {
            int usr;
        }
    }

    if (usr == 1) {     // Основная игра
        int Health = 5;
        int Health_Bottle = 3;
        int Money = 0;
        int Enemy_Health = 1;
        int steps = 0;
        printf("\nВы спускаетесь в подземелье...\n");
        while (Health > 0) {
            printf("\nЗдоровье: %d/10\nЛечебных зелий: %d\nЗдоровье врага: %d\n", Health, Health_Bottle, Enemy_Health);
            printf("\nВаши действия?\n1. Атаковать\n2. Лечиться\n3. Выйти\n> ");
            scanf("%d", &usr);
            printf("\n");
            int atk = rand() % 4;
            int heal = rand() % 4;
            if (usr == 1) {             // Ход игрока
                Enemy_Health -= atk;
                printf("\nВы ударили врага и нанесли ему %d урона!\nУ него осталось %d здоровья\n", atk, Enemy_Health);
            } else if (usr == 2) {
                if (Health_Bottle > 0) {
                   Health += heal;
                   if (Health > 10) {
                    Health = 10;
                   }
                   Health_Bottle -= 1;
                   printf("\nВы успешно полечились и теперь у вас %d здоровья!\n", Health);
                } else {
                    printf("\nУ вас <= 0 лечебных зелий!\n");
                }
            } else if (usr == 3) {
                printf("\nУдачи вам! До следующей встречи!");
                break;
            } else {
                int usr;
            }
            if (Enemy_Health > 0) {     // Ход врага
                int atk = rand() % 3;
                Health -= atk;
                printf("Вам нанесли %d урона!\n", atk);
            } else {
                int coins = rand() % 5;
                Money += coins;
                printf("\nВы победили врага и получаетет золото: %d штук! Теперь у вас %d золота!\n", coins, Money);
                Enemy_Health = (rand() % 7)+1;

                if ((rand() % 10) < 3) {   // Случайное событие с шансом 30% - магазин
                    int price = (rand() % 20) + 1;
                    int count = (rand() % 5) + 1;
                    printf("\nВы нашли магазин: %d лечебных зелий стоит %d монет, а у вас %d монет\n1. Купить\n2. Отказаться\n> ", count, price, Money);
                    scanf("%d", &usr);
                    if (usr == 1) {
                        if (Money >= price) {
                            Money -= price;
                            Health_Bottle += count;
                            printf("\nСделка состоялась!\n");
                        } else {
                            printf("\nУ вас недостаточно денег!\n");
                        }
                    } else if (usr == 2) {
                        printf("\nВы отказались от сделки\n");
                    } else {
                        int usr;
                    }
                }
            }
            steps += 1;
        }
        if (Health <= 0) {
            printf("\n\nВы умерли, прискорбно, но перед смертью сделали %d шагов\n", steps);
        }
    }

    printf("\nНажмите [ENTER] для выхода ");
    scanf("%d", &usr);
    return 0;
}