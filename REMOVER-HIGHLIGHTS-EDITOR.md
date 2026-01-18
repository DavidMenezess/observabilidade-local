# 🎨 Como Remover Highlights Vermelhos/Verdes no Editor

## ❓ Por que aparecem?

Os **destaques vermelhos** (linhas removidas/modificadas) e **verdes** (linhas adicionadas) aparecem quando o editor detecta diferenças entre:
- Versão atual do arquivo
- Última versão salva ou última commitada no Git

## ✅ Como Remover

### Método 1: Salvar o Arquivo (Mais Simples)

```bash
# No VS Code/Cursor: Ctrl+S (Windows/Linux) ou Cmd+S (Mac)
# Ou clique no disco 💾 na parte superior
```

Isso sincroniza o estado do arquivo e remove highlights temporários.

### Método 2: Commit no Git (Se as mudanças são desejadas)

Se você quer manter as mudanças e elas aparecem porque ainda não foram commitadas:

```bash
# Adicionar arquivo ao stage
git add docker-compose.yml

# Fazer commit
git commit -m "Atualizar docker-compose.yml"

# Os highlights desaparecerão após o commit
```

### Método 3: Descartar Mudanças (Se não quiser as mudanças)

Se você não quer as mudanças mostradas:

```bash
# Reverter para última versão commitada
git checkout -- docker-compose.yml
```

### Método 4: Fechar e Reabrir o Arquivo

Às vezes o editor fica "preso" mostrando diffs:
- Feche o arquivo (Ctrl+W)
- Reabra o arquivo

### Método 5: Desabilitar Destaques no Editor

No **VS Code/Cursor**:
1. Abra Settings (Ctrl+,)
2. Procure por: `git.decorations.enabled`
3. Desmarque se quiser desabilitar completamente

Ou procure por: `diffEditor` para configurações de diff

## 🔍 Verificar Status Atual

Para ver se há mudanças pendentes:

```bash
git status docker-compose.yml
```

Se mostrar "nothing to commit", os highlights são apenas do editor (mudanças não salvas ou histórico local).

## 💡 Dica

A maneira mais rápida: **pressione Ctrl+S** para salvar o arquivo!
