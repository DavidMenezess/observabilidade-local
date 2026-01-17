# Guia de Comandos Git para Push

## 1. Configurar Git (primeira vez apenas)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

## 2. Inicializar o repositório Git
```bash
cd /home/david/Documentos/Estudo
git init
```

## 3. Adicionar arquivos ao staging
```bash
# Adicionar todos os arquivos (respeitando .gitignore)
git add .

# OU adicionar arquivos específicos:
git add Projeto/
git add windows/
git add .gitignore
```

## 4. Fazer commit
```bash
git commit -m "Descrição das mudanças"
```

## 5. Adicionar repositório remoto (GitHub/GitLab/etc)
```bash
# Substitua pela URL do seu repositório
git remote add origin https://github.com/seu-usuario/seu-repositorio.git

# OU se já existe, verificar:
git remote -v
```

## 6. Fazer push
```bash
# Primeira vez (criar branch main e fazer push)
git branch -M main
git push -u origin main

# Próximas vezes
git push
```

## Comandos úteis
```bash
# Ver status dos arquivos
git status

# Ver diferenças
git diff

# Ver histórico
git log --oneline

# Desfazer mudanças não commitadas
git restore <arquivo>
```
