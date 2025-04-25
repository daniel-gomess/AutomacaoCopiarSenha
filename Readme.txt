Script de Automação com PyAutoGUI – Inserção de E-mail e Senha

Este script foi desenvolvido com o objetivo de automatizar a digitação de credenciais (e-mail e senha) em um editor de texto (Notepad), utilizando as bibliotecas pyautogui, time e pyperclip.

- Funcionalidades
Solicita ao usuário que informe um e-mail e uma senha.

Copia e cola os dados de forma segura utilizando a área de transferência (pyperclip).

Abre o Bloco de Notas automaticamente através do comando Win + R.

Digita o e-mail e a senha no editor com espaçamento controlado entre as ações.

Emite um alerta de finalização da automação.

- Como funciona
Ao executar o script, o usuário verá uma janela solicitando o e-mail.

Em seguida, será exibida outra janela para inserção da senha (com os caracteres ocultos).

O script abrirá o Notepad automaticamente usando Win + R.

Após abrir o Notepad, o e-mail será colado, seguido da senha em uma nova linha.

Ao final, será exibida uma mensagem de conclusão da automação.

- Bibliotecas Utilizadas
pyautogui: Para controlar o teclado e o mouse.

pyperclip: Para manipular a área de transferência.

time: Para controlar o tempo de espera entre as ações.

⚠️ Aviso de Segurança
Este script é apenas para fins educacionais. Evite armazenar ou automatizar o uso de senhas em texto simples em ambientes inseguros. Para aplicações reais, é recomendável o uso de práticas seguras de autenticação e armazenamento de credenciais.