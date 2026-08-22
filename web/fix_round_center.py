with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Центрируем панель и поднимаем выше
old = '''.round-switcher {
  position: fixed;
  bottom: 18px;
  right: 190px;
  z-index: 100;
  display: flex;
  gap: 10px;
  background: transparent;
  padding: 0;
  border: none;
  border-radius: 0;
  box-shadow: none;
}'''

new = '''.round-switcher {
  position: fixed;
  bottom: 70px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 100;
  display: flex;
  gap: 12px;
  background: transparent;
  padding: 0;
  border: none;
  border-radius: 0;
  box-shadow: none;
}'''

if old in content:
    content = content.replace(old, new)
    print('OK: Панель отцентрирована и поднята выше')
else:
    print('NOT FOUND')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Файл сохранён')
