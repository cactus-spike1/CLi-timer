# ASCII Art Timer

Простой консольный таймер с ASCII-арт отображением времени, написанный на Python.

[Пример работы таймера](https://imgur.com/vAUiu28)
https://imgur.com/vAUiu28

## Особенности

- Красивое ASCII-арт отображение времени
    
- Поддержка форматов:
    
    - `MM:SS` (для времени меньше часа)
        
    - `HH:MM:SS` (для времени от часа и больше)
        
- Настраиваемое сообщение по завершении
    
- Опция звукового сигнала
    
- Обработка прерывания (Ctrl+C)
    

## Требования

- Python 3.6+
    
- Совместим с Linux, macOS и Windows
    

## Установка

1. Склонируйте репозиторий:  
```bash
git clone https://github.com/ваш-username/ascii-timer.git 
cd ascii-timer```

    
2. (Опционально) Сделайте скрипт исполняемым:  
```bash
chmod +x timer.py
```
   

## Использование

### Базовое использование
```bash
./timer.py [секунды]  
```
или  
```bash
python3 timer.py [секунды]
```

### Примеры

Запустить таймер на 5 минут (300 секунд):  
```bash
./timer.py 300
```

Таймер на 1 час 30 минут с сообщением и звуком: 
```bash
./timer.py 5400 --finished "Время вышло!" --sound
```

### Все параметры


```markdown
usage: timer.py [-h] [-f FINISHED] [--sound] seconds

CLI таймера

positional arguments:
  seconds               Общее время таймера в секундах.

options:
  -h, --help            show this help message and exit
  -f FINISHED, --finished FINISHED
                        Сообщение после завершения отсчёта.
  --sound               Воспроизвести звуковой сигнал по завершении таймера.
```
