# Portfólio de Kalleby Evangelho Mota

Bem-vindo ao repositório oficial do meu portfólio pessoal! Este projeto apresenta minha trajetória, valores, projetos desenvolvidos e oferece um formulário guiado para que clientes possam descrever suas ideias de software de forma clara e acessível.

---

## 🪀 Objetivo

Criar um site responsivo, elegante e funcional que atue como:
- **Portfólio público**
- **Cartão de visitas vivo**
- **Canal de contato inteligente com coleta de briefing**

---

## 🎓 Sobre mim

Sou estudante de Engenharia Biomédica e entusiasta de Tecnologia da Informação com experiência em desenvolvimento web Fullstack, tecnologias assistivas, IA aplicada à saúde e educação. Fundador da startup **Biomove**.

> **CNPJ**: 49.549.704/0001-07

---

## 📁 Estrutura do Projeto

```bash
meu-portfolio-kalleby/
├── index.html
├── sobre.html
├── projetos.html
├── formulario.html
├── contato.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── img/
│   └── (imagens dos projetos e perfil)
├── pdf/
│   └── curriculo-kalleby.pdf
├── backend/
│   ├── app.py
│   └── .env
├── .gitignore
├── README.md
```

---

## 🌐 Tecnologias Utilizadas

- HTML5, CSS3 e JavaScript
- Bootstrap 5
- Font Awesome & AOS.js
- Flask + Flask-Mail (envio de emails)
- Python-dotenv (.env seguro)

---

## 🚫 Proteção de Dados

Este projeto utiliza variáveis de ambiente sensíveis via `.env`. Não suba esse arquivo para repositórios públicos.

**Exemplo do `.env`:**
```env
MAIL_USERNAME=seuemail@gmail.com
MAIL_PASSWORD=senha-do-app
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
```

---

## 🔧 Como rodar localmente

1. Clone este repositório:
```bash
git clone https://github.com/KallebyX/meu-portfolio-kalleby.git
```

2. Crie e ative um ambiente virtual (na pasta `backend/`):
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

> Se o `requirements.txt` ainda não existir, crie com:
> ```bash
> pip freeze > requirements.txt
> ```

4. Execute o servidor:
```bash
python app.py
```

5. Abra `index.html` no navegador e acesse normalmente. O formulário irá se comunicar com `localhost:5000`.

---

## 🙏 Agradecimentos

Este projeto foi concebido com foco em acessibilidade, impacto social e profissionalismo. Agradeço a todos que acompanham meu trabalho e incentivam a inovação com empatia.

---

Feito com ❤️ por [Kalleby Evangelho](https://github.com/KallebyX) - 2025
