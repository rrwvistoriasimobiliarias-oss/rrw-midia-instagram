# RRW Vistorias Imobiliárias — Biblioteca independente de Reels

**Fluxo oficial:** código-fonte RRW no GitHub → GitHub Actions produz MP4 e JPG → Cloudflare Pages hospeda → Windsor.ai publica apenas após controle editorial.

## Estado da implantação
- Conta Instagram: `@rrwvistoriasimobiliarias`
- Hospedagem pública: `https://rrw-midia-instagram.pages.dev`
- Fonte principal da campanha: `scripts/render_rrw.py`
- Geração automática: `.github/workflows/gerar-reels-rrw.yml`
- Marca: `assets/rrw-logo.png` (extraída uma vez de material oficial para preservação do símbolo; nunca redesenhar)
- Saídas: `instagram/reels/01-vistoria-entrada.mp4` até `05-vistoria-profissional.mp4`, acompanhadas por `.jpg`.

**Não utiliza os MP4 nem as capas anteriores do Lovable para gerar as novas peças.** A antiga sincronização de mídia foi desativada e removida.

## Conteúdo
1. Vistoria de entrada — Essa fissura já estava aqui? (a cena atual é **ilustração**, não fotografia, e precisa de revisão visual antes de publicação)
2. Vistoria de saída — Devolver as chaves encerra tudo?
3. Laudo fotográfico — Só descrever basta?
4. Apoio às imobiliárias — Muitas vistorias. Pouco tempo?
5. Vistoria profissional — Vistoria não é só olhar.

## Restrições de publicação
- Revisar ortografia e legibilidade mobile.
- Verificar no Cloudflare status HTTP 200, Content-Type correto e integridade dos MP4.
- Nunca publicar automaticamente sem verificar arquivo, identidade visual, legenda e se o Reel já foi publicado.
- **Os agendamentos antigos baseados no acervo Lovable foram desativados.**
- O Reel comercial sobre apoio às imobiliárias já foi publicado em 05/11/2026 com ID `18118115135030841`; evitar duplicação.
- Preservar o site institucional `rrwvistorias.com.br`.
