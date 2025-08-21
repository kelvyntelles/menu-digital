# 🍽️ Menu Digital

O **Menu Digital** é um sistema de cardápio web desenvolvido para **restaurantes, bares e lanchonetes**, com foco em oferecer uma experiência simples e intuitiva tanto para os administradores quanto para os clientes.  
O projeto foi desenvolvido em **Django**, com interface administrativa personalizada usando **AdminLTE** e o cardápio desenhado com abordagem **mobile first**.

---

## ✨ Funcionalidades

### 👨‍💻 Administração
- Gestão completa dos **estabelecimentos** pelo **painel admin do Django**.
- Cada **usuário** possui **um estabelecimento**, e pode gerenciá-lo pelo painel administrativo customizado.
- O **administrador principal** do sistema tem controle sobre todos os estabelecimentos.
- Possibilidade de definir se uma empresa está **ativa ou inativa**:
  - **Ativa** → consegue exibir seu cardápio aos clientes.
  - **Inativa** → não consegue exibir o cardápio.

### 🏪 Estabelecimentos
- Cada estabelecimento possui:
  - **Categorias de produtos** independentes.
  - **Produtos** que podem estar relacionados a **uma ou várias categorias**.
  - Destaque para **produtos promocionais** e **produtos em destaque**.

### 📱 Cardápio Digital (Mobile First)
- Focado em **experiência mobile** (aberto direto no celular do cliente).
- Telas principais:
  - **Tela inicial**: Exibe categorias, produtos relacionados, destaques e promoções.
  - **Tela de detalhes**: Informações completas do produto selecionado.

---

## 🛠️ Tecnologias Utilizadas
- **Backend:** Django (Python)
- **Painel admin do dono do projeto:** Django Admin
- **Painel admin do usuário dono de estabelecimento: AdminLTE
- **Banco de Dados:** MySQL
- **Frontend (Cardápio):** HTML5, CSS3, JavaScript, Bootstrap
- **Gerenciamento de Usuários:** Django Auth

🖼️ Imagens do Projeto
<br><br>
🔑 Login Admin
<div style="display: flex; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/de444503-555f-4c34-b907-de4deed37a39" alt="Painel Admin 1" width="49%" />
  <img src="https://github.com/user-attachments/assets/09f61e8e-a06f-4ca9-8404-e3f9dc58edec" alt="Painel Admin 2" width="49%" />
</div>
<br>
📊 Painel Admin (AdminLTE)
<div style="display: flex; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/d6ba9722-f109-4e37-aa69-26a3481cbb85" alt="Painel Admin 1" width="49%" />
  <img src="https://github.com/user-attachments/assets/e844d6ee-a383-4928-aa51-b3a196cc7abf" alt="Painel Admin 2" width="49%" />
</div>
<br>
🏪 Cardápio - Tela Inicial | 🍔 Cardápio - Detalhes do Produto
<div style="display: flex; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/a0e526dc-5ba8-4ed0-be50-4c7c3b69cb0d" alt="Painel Admin 1" width="200" height="350" />
  <img src="https://github.com/user-attachments/assets/eb84c82d-05a5-47b4-a94b-a8d84bb86f5b" alt="Painel Admin 2" width="200" height="350" />
  <img src="https://github.com/user-attachments/assets/8cf7df6d-5b9e-43c9-ae48-4c1800d6a596" alt="Painel Admin 1" width="200" height="350"/>
</div>

📌 Observações

O sistema suporta múltiplos estabelecimentos, mas cada um possui categorias e produtos independentes.

Somente estabelecimentos ativos conseguem exibir o cardápio.

<hr>
👨‍💻 Autor

Desenvolvido por Kelvyn Telles 🚀
