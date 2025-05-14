# 🚀 Portfólio Evolutivo - Kalleby Evangelho

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Evolu%C3%A7%C3%A3o-blue" alt="Status Em Evolução" />
  <img src="https://img.shields.io/badge/AWS-Integrado-success" alt="AWS Integrado" />
  <img src="https://img.shields.io/badge/Roadmap-Aberto-brightgreen" alt="Roadmap Aberto" />
  <img src="https://img.shields.io/badge/Deploy-Render.com-blueviolet" alt="Deploy no Render" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="Licença MIT" />
</p>

---

## 📜 Sobre o Projeto

Este projeto visa transformar o portfólio pessoal de **Kalleby Evangelho** em uma **plataforma viva de tecnologia, comunicação e inovação**.

A missão é evoluir continuamente, adicionando segurança, inteligência, automação e APIs abertas, tornando o portfólio uma vitrine real de capacidades técnicas e visão de futuro.

---

## 🧩 Estrutura de Evolução

O roadmap do projeto está dividido em cinco fases:

| Fase | Objetivo |
|:----|:---------|
| **Fase 1** - Blindagem Profissional | Estabilizar, proteger e estruturar |
| **Fase 2** - Comunicação Avançada | Melhorar a interação usuário-website |
| **Fase 3** - Transformação em Produto | Evoluir para SaaS pessoal |
| **Fase 4** - Plataforma Aberta | APIs, multiusuários e dados públicos |
| **Fase 5** - Visão Futurista | IA, automação e inteligência comercial |

---

## 🛠️ Tecnologias Utilizadas

### Front-end
- **HTML5** - Estruturação semântica
- **CSS3** - Estilização responsiva
- **JavaScript Vanilla** - Funcionalidades básicas dinâmicas
- **Bootstrap 5** - Framework para design responsivo e moderno

### Back-end
- **Python 3.13**
- **Flask** - Framework para criação de aplicações web rápidas e seguras
- **Flask-Mail** - Envio de e-mails via SMTP
- **SQLAlchemy** - ORM para manipulação de banco de dados
- **PostgreSQL** - Banco de dados relacional (Render PostgreSQL Service)

### Infraestrutura e Deploy
- **AWS S3** - Armazenamento escalável de imagens de projetos
- **Render.com** - Deploy automático e hospedagem contínua
- **Gunicorn** - Servidor WSGI para produção
- **GitHub** - Controle de versão e gestão de projeto com GitHub Projects 2.0

---

## ✨ Funcionalidades do Site

- Página inicial apresentando resumo pessoal
- Seção de Projetos com imagens armazenadas na AWS S3
- Formulário de contato inteligente, com e-mail automático e futuro sistema de resposta
- Upload seguro de imagens (em desenvolvimento)
- Layout 100% Responsivo (Desktop, Tablet, Mobile)
- Área administrativa para gestão de projetos (planejado)
- Integração contínua e roadmap público de evolução

---

## 📂 Estrutura do Projeto

```bash
Portifolio/
├── backend/
│   ├── app.py              # Instanciação principal do app Flask
│   ├── extensions.py       # Extensões como Mail, LoginManager
│   ├── routes/             # Blueprints separados por função
│   ├── templates/          # Páginas HTML Jinja2
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   └── utils/              # Upload S3, Helpers
├── requirements.txt        # Dependências do projeto
├── run.py                  # Arquivo principal para iniciar o servidor
├── README.md               # Documentação do projeto
└── .env                    # Variáveis de ambiente (não versionado)
```

---

## 📈 Roadmap Atual

| Mês | Prioridades |
|:----|:------------|
| Novembro 2024 | Implementação de segurança: reCAPTCHA, uploads limitados, logs de e-mails |
| Dezembro 2024 | Melhoria da comunicação: Auto-respostas, Painel de Administração |
| 2025 | Transformação em Plataforma SaaS e API pública |

Mais detalhes no [Roadmap Público](https://github.com/KallebyX/Portifolio/projects).

---

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

Você é livre para usar, modificar e distribuir este projeto, desde que preserve os créditos.

---

## ✨ Autor

Desenvolvido e mantido por [Kalleby Evangelho](https://www.kallebyevangelho.com.br/) — **Engenharia, Inovação e Futuro.**

---