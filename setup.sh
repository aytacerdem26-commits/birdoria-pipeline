#!/usr/bin/env bash
set -euo pipefail

# Birdoria Production Pipeline — Yeni Makine Kurulumu
# Kullanım: git clone <repo> ~/zenn && cd ~/zenn && ./setup.sh

echo "=== Birdoria Pipeline Setup ==="

# 1. Homebrew bağımlılıkları
echo "[1/6] Sistem araçları kuruluyor..."
if ! command -v brew &>/dev/null; then
  echo "Homebrew yok. Kur: https://brew.sh"
  exit 1
fi
brew install --quiet ffmpeg yt-dlp python3 2>/dev/null || true

# 2. Python venv + bağımlılıklar
echo "[2/6] Python venv kuruluyor..."
python3 -m venv .venv
source .venv/bin/activate
pip install --quiet groq numba 2>/dev/null || true

# 3. Claude Code global dizinleri
echo "[3/6] Claude Code dizinleri hazırlanıyor..."
mkdir -p ~/.claude/skills
mkdir -p ~/.claude/hookify-rules
mkdir -p ~/.config/birdoria
mkdir -p ~/.config/watch

# Global CLAUDE.md (varsa dokunma)
if [ ! -f ~/.claude/CLAUDE.md ]; then
  cp claude-global/CLAUDE.md ~/.claude/CLAUDE.md
  echo "  ~/.claude/CLAUDE.md kopyalandı"
else
  echo "  ~/.claude/CLAUDE.md zaten var — atlandı (elle birleştir)"
fi

# 4. Memory dosyaları
echo "[4/6] Memory dosyaları kuruluyor..."
MEMORY_DIR="$HOME/.claude/projects/-Users-$(whoami)-zenn/memory"
mkdir -p "$MEMORY_DIR"
if [ -d "claude-memory" ]; then
  cp -n claude-memory/*.md "$MEMORY_DIR/" 2>/dev/null || true
  echo "  Memory dosyaları kopyalandı: $MEMORY_DIR"
else
  echo "  claude-memory/ klasörü yok — atlandı"
fi

# 5. Hookify kuralları
echo "[5/6] Hookify kuralları kuruluyor..."
if [ -d "claude-hookify" ]; then
  cp claude-hookify/*.md ~/.claude/hookify-rules/ 2>/dev/null || true
  # Symlink'leri oluştur
  for f in ~/.claude/hookify-rules/*.md; do
    base=$(basename "$f")
    ln -sf "$f" ".claude/$base" 2>/dev/null || true
  done
  echo "  Hookify kuralları bağlandı"
else
  echo "  claude-hookify/ klasörü yok — atlandı"
fi

# 6. API key'ler (elle girilecek)
echo "[6/6] API key kontrolü..."
if [ ! -f ~/.config/birdoria/.env ]; then
  echo "  ~/.config/birdoria/.env EKSIK — elle oluştur:"
  echo "    echo 'GENAIPRO_API_KEY=sk_gap_...' > ~/.config/birdoria/.env"
fi
if [ ! -f ~/.config/watch/.env ]; then
  echo "  ~/.config/watch/.env EKSIK — elle oluştur:"
  echo "    echo 'GROQ_API_KEY=gsk_...' > ~/.config/watch/.env"
fi

echo ""
echo "=== Kurulum tamamlandı ==="
echo ""
echo "Manuel adımlar:"
echo "  1. API key'leri gir (yukarıdaki .env dosyaları)"
echo "  2. Claude Code'da MCP connector'ları authorize et:"
echo "     - vidIQ: claude.ai > Settings > Connectors"
echo "     - Nim: claude.ai > Settings > Connectors (OAuth)"
echo "     - Chrome: Chrome extension kur + Claude Code'a bağla"
echo "  3. Claude Code skills plugin olarak kurulu gelecek (aynı hesap)"
echo "     Elle kurulu skill varsa: claude install <skill-url>"
echo ""
echo "Test: cd ~/zenn && claude"
