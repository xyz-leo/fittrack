# FitTrack

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=flat&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Prototipo-orange?style=flat)

FitTrack é um protótipo de aplicação web para acompanhamento fitness desenvolvido com Django.  
Foi criado como projeto acadêmico para demonstrar a estrutura de uma aplicação web simples e mobile-first voltada para academias e personal trainers.  
O projeto foca em design limpo, funcionalidades essenciais e simplicidade.

---

## Integrantes do Projeto

<!-- Adicione os nomes dos membros da equipe abaixo -->

-   **[LEONARDO OLIVEIRA DA SILVA ALMEIDA]** - [GitHub](https://github.com/xyz-leo)
-   **[MATEUS PRIETE RIBEIRO COPETTI]** - [GitHub](https://github.com)
-   **[RODRIGO BREZOLIN BUQUERA]** - [GitHub](https://github.com/Rodrigo-Brezolin-Buquera)
-   **[ROGERIO APARECIDO CORDEIRO DA SILVA]** - [GitHub](https://github.com/RogerioCordeiro)

<!-- Adicione mais membros conforme necessário -->

---

## Sobre o Projeto

Este projeto é um **protótipo** desenvolvido como **produto mínimo viável (MVP)** para demonstrar a estrutura e funcionalidade de uma aplicação web de acompanhamento fitness construída com Django.  
Foi criado para fins educacionais e de apresentação, mostrando como conceitos centrais como registro de usuários, navegação básica e exibição de dados podem ser implementados dentro de um framework web.

O sistema **não inclui recursos de nível de produção**, como autenticação avançada, medidas de segurança robustas ou persistência de dados para implantação real.  
Seu objetivo é ilustrar um fluxo de design funcional e a integração de componentes backend e frontend em uma interface limpa e mobile-first.

---

## Funcionalidades

-   **Registro de Usuários**: Criação de perfil com nome, altura, peso, idade, nível de experiência, frequência e objetivo fitness
-   **Simulação de Login**: Login simples com redirecionamento para o dashboard do usuário
-   **Página Inicial do Usuário**: Exibe dados mockados como plano atual, dias de treino por mês e últimos treinos
-   **Página de Treinos**: Lista informações estáticas de treinamento para demonstração
-   **Design Responsivo**: Layout mobile-first com tema claro e laranja como cor primária

---

## Tecnologias Utilizadas

### Backend

-   **Python 3.12+**
-   **Django 5.0+**

### Frontend

-   **HTML5**
-   **CSS3**
-   **Fonte Poppins (Google Fonts)**

### Banco de Dados

-   **SQLite** (padrão do Django para desenvolvimento)

---

## Estrutura do Projeto

```
fittrack/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── fittrack/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── core/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    │
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    │
    ├── templates/core/
    │   ├── base.html
    │   ├── landing.html
    │   ├── login.html
    │   ├── register.html
    │   ├── home.html
    │   └── trainings.html
    │
    └── static/core/
        └── css/
            └── style.css
```

---

## Como Executar o Projeto

### Pré-requisitos

-   Python 3.12 ou superior instalado
-   pip (gerenciador de pacotes do Python)
-   Git

### Passo a Passo

1. **Clone o repositório**

    ```bash
    git clone https://github.com/xyz-leo/fittrack.git
    cd fittrack
    ```

2. **Crie e ative um ambiente virtual**

    No Windows (PowerShell):

    ```powershell
    # Primeiro, crie o ambiente virtual
    python -m venv venv

    # Depois, ative o ambiente virtual
    .\venv\Scripts\Activate.ps1
    ```

    > **Nota para Windows**: Se você receber um erro de política de execução no PowerShell, use uma das seguintes alternativas:
    >
    > **Opção 1 (Recomendado)** - Use o Command Prompt (CMD) ao invés do PowerShell:
    >
    > ```cmd
    > # Crie o ambiente virtual
    > python -m venv venv
    >
    > # Ative o ambiente virtual
    > venv\Scripts\activate.bat
    > ```
    >
    > **Opção 2** - Ou habilite a execução de scripts temporariamente no PowerShell:
    >
    > ```powershell
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    > ```
    >
    > Depois execute os comandos de criação e ativação normalmente.

    No Linux/Mac:

    ```bash
    # Crie o ambiente virtual
    python3 -m venv venv

    # Ative o ambiente virtual
    source venv/bin/activate
    ```

3. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute as migrações do banco de dados**

    ```bash
    cd fittrack
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento**

    ```bash
    python manage.py runserver
    ```

6. **Acesse a aplicação**

    Abra seu navegador e acesse: `http://localhost:8000`

---

## Observações Importantes

-   Este é um protótipo desenvolvido para fins educacionais
-   A autenticação é simulada para demonstração e **não é segura**
-   Dados como estatísticas de usuários e treinos são mockados para apresentação
-   **Não utilize este código em ambiente de produção sem implementar medidas de segurança adequadas**

---

## Modelo de Dados

### Modelo `Student`

O modelo `Student` representa um usuário dentro do protótipo FitTrack.  
Armazena informações essenciais sobre os atributos físicos do estudante, preferências de treinamento e dados de login (apenas para fins de demonstração).

| Campo                | Tipo                    | Descrição                                                                       |
| -------------------- | ----------------------- | ------------------------------------------------------------------------------- |
| `full_name`          | `CharField`             | Nome completo do estudante                                                      |
| `email`              | `EmailField` (único)    | Usado como identificador único para login                                       |
| `password`           | `CharField`             | Armazenado em texto simples — **não seguro**, aceitável apenas em protótipos    |
| `height_cm`          | `PositiveIntegerField`  | Altura em centímetros (opcional)                                                |
| `weight_kg`          | `DecimalField`          | Peso em quilogramas, suporta valores decimais (opcional)                        |
| `age`                | `PositiveIntegerField`  | Idade do estudante (opcional)                                                   |
| `level`              | `CharField` com choices | Indica nível de treinamento: _Iniciante_, _Intermediário_ ou _Avançado_         |
| `frequency_per_week` | `PositiveIntegerField`  | Quantas vezes por semana o estudante treina (padrão: 3)                         |
| `objective`          | `CharField` com choices | Define o objetivo fitness: _Ganho de Massa_, _Perda de Gordura_ ou _Manutenção_ |
| `created_at`         | `DateTimeField`         | Armazena automaticamente a data/hora de criação do registro                     |

**Métodos auxiliares:**

-   `first_name()`: Retorna o primeiro nome do estudante, extraído de `full_name`
-   `__str__()`: Retorna uma representação legível, ex: `João Silva <joao@exemplo.com>`

---

## Integração com Templates

Os dados do modelo `Student` são passados das views do Django para os templates usando o contexto do template.  
Dentro do template, a linguagem de template do Django é usada para exibir dados dinamicamente.

Exemplo de trecho de um template:

```html
<h2>{{ student.first_name }}</h2>
<p class="muted">{{ student.level|title }} • {{ student.objective|cut:"_"|title }}</p>
```

**Explicação:**

-   `{{ student.first_name }}`  
    Chama o método `first_name()` do modelo e exibe apenas a primeira palavra do campo `full_name`.  
    Exemplo: `"João Silva"` → `"João"`

-   `{{ student.level|title }}`  
    Usa o filtro embutido `title` do Django para capitalizar a primeira letra de cada palavra.  
    Exemplo: `"beginner"` → `"Beginner"`

-   `{{ student.objective|cut:"_"|title }}`  
    Primeiro substitui underscores (`_`) por espaços, depois aplica o filtro `title`.  
    Exemplo: `"mass_gain"` → `"Mass Gain"`

Essas expressões de template renderizam dinamicamente as informações do estudante, aplicando formatação diretamente na camada HTML, mantendo o modelo Python limpo e focado nos dados.

---

## CSS e Abordagem de Design

O CSS foi escrito com uma mentalidade **mobile-first**, garantindo que a interface pareça limpa e funcional em telas pequenas, como smartphones, antes de escalar para layouts desktop.  
O design usa um **tema claro** com **laranja como cor de destaque**, combinado com **cinzas neutros** para equilíbrio. A tipografia é baseada em **Poppins**, uma fonte sans-serif amigável e moderna que proporciona boa legibilidade e apelo visual.

Principais escolhas de design:

-   **Layout responsivo**: Usa containers flexíveis e unidades relativas (`%`, `rem`) para se adaptar a diferentes tamanhos de tela
-   **Menu hambúrguer**: Ícone simplificado que aparece tanto em mobile quanto em desktop para consistência
-   **Espaçamento consistente**: Padding e margins garantem espaço adequado entre elementos
-   **Seções baseadas em cards**: Informações como o plano do usuário e resumo de treinos são apresentadas dentro de caixas arredondadas com sombras suaves para melhorar a hierarquia visual
-   **Paleta de cores minimalista**: Fundos claros, acentos laranjas e texto preto para contraste e legibilidade ideais

O objetivo foi manter o CSS **simples, legível e fácil de estender**, enquanto ainda alcança um resultado visualmente coeso adequado para uma demonstração de MVP.

---

## Licença

Este projeto foi desenvolvido para fins educacionais como parte de um projeto acadêmico.
