# ДЗ8: Алгоритми контролю потоку та обмеження швидкості

## Опис

Проєкт імітує роботу чат-системи з обмеженням частоти повідомлень двома способами:

- Sliding Window — точне вікно часу з max N повідомлень
- Throttling — фіксований мінімальний інтервал між повідомленнями

## Завдання 1: Sliding Window

### Реалізація

- Клас `SlidingWindowRateLimiter`
- Методи: `_cleanup_window`, `can_send_message`, `record_message`, `time_until_next_allowed`
- Використовується `collections.deque` для збереження історії повідомлень

### Тест

- 20 повідомлень від 5 користувачів
- Очікуване блокування та дозволи після очищення вікна

## Завдання 2: Throttling

### Реаліз

- Клас `ThrottlingRateLimiter`
- Методи: `can_send_message`, `record_message`, `time_until_next_allowed`
- Зберігає час останнього повідомлення у `Dict[str, float]`

### Тестування

- Користувач не може відправити повідомлення раніше ніж через 10 секунд

## Як запускати

```bash
python3 test_sliding.py      
python3 test_throttling.py   
```

Затримка між повідомленнями імітується через time.sleep(...)

## Авторка

Катанова Леся
