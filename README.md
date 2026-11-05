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
1. Vistoria de entrada — Essa fissura já estava aqui? (**imagem ilustrativa fotográfica gerada para a campanha**; capa e quadros 0,8 s, 3,3 s e 6,2 s conferidos; programado para 16/11/2026)
2. Vistoria de saída — Devolver as chaves encerra tudo?
3. Laudo fotográfico — Só descrever basta?
4. Apoio às imobiliárias — Muitas vistorias. Pouco tempo?
5. Vistoria profissional — Vistoria não é só olhar.

## Restrições de publicação
- Revisar ortografia e legibilidade mobile.
- Verificar no Cloudflare status HTTP 200, Content-Type correto e integridade dos MP4.
- Nunca publicar automaticamente sem verificar arquivo, identidade visual, legenda e se o Reel já foi publicado.
- **Os agendamentos antigos baseados no acervo Lovable foram desativados.** Um calendário único programa Reels 02, 03, 05 e 01 para 07/11, 10/11, 13/11 e 16/11, sempre às 18h30 (Brasília).
- O Reel comercial sobre apoio às imobiliárias já foi publicado em 05/11/2026 com ID `18118115135030841`; evitar duplicação.
- Preservar o site institucional `rrwvistorias.com.br`.

## Verificação operacional (05/11/2026)
- [GitHub Actions: integridade de 5 MP4 e 5 JPG no Cloudflare confirmada](https://github.com/rrwvistoriasimobiliarias-oss/rrw-midia-instagram/actions/runs/42120522198).
- [Reel 01: montagem conferida em três quadros](qa/reel01-revisao.jpg).
- Cache de MP4/JPG controlado por cabeçalhos e URLs versionadas para evitar arquivos antigos.
- A programação exige nova conferência e impede publicações duplicadas.
