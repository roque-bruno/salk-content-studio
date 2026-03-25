-- ============================================================
-- Content Studio v2.0 — Supabase Migration
-- Migração do SQLite para PostgreSQL (Supabase)
-- ============================================================

-- 1. Pieces (Production Board / Kanban)
CREATE TABLE IF NOT EXISTS pieces (
    id TEXT PRIMARY KEY DEFAULT gen_random_uuid()::text,
    title TEXT NOT NULL DEFAULT '',
    brand TEXT NOT NULL DEFAULT 'salk',
    product TEXT DEFAULT '',
    pillar TEXT DEFAULT '',
    platform TEXT DEFAULT '',
    format TEXT DEFAULT '',
    stage TEXT NOT NULL DEFAULT 'briefing',
    assignee TEXT DEFAULT '',
    vdp_path TEXT DEFAULT '',
    copy_text TEXT DEFAULT '',
    claims_used JSONB DEFAULT '[]'::jsonb,
    hashtags JSONB DEFAULT '[]'::jsonb,
    persona_target TEXT DEFAULT '',
    master_id TEXT DEFAULT '',
    is_derivative BOOLEAN DEFAULT false,
    calendar_slot_id TEXT DEFAULT '',
    notes TEXT DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_pieces_stage ON pieces(stage);
CREATE INDEX IF NOT EXISTS idx_pieces_brand ON pieces(brand);
CREATE INDEX IF NOT EXISTS idx_pieces_updated ON pieces(updated_at DESC);

-- 2. Reviews (Lens — Fila de revisão)
CREATE TABLE IF NOT EXISTS reviews (
    id TEXT PRIMARY KEY DEFAULT gen_random_uuid()::text,
    piece_id TEXT DEFAULT '' REFERENCES pieces(id) ON DELETE SET DEFAULT,
    review_type TEXT DEFAULT 'editorial',
    verdict TEXT DEFAULT 'pending',
    comments TEXT DEFAULT '',
    reviewer TEXT DEFAULT '',
    checklist JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_reviews_verdict ON reviews(verdict);
CREATE INDEX IF NOT EXISTS idx_reviews_piece ON reviews(piece_id);

-- 3. Metrics (Pulse — Performance pós-publicação)
CREATE TABLE IF NOT EXISTS metrics (
    id TEXT PRIMARY KEY DEFAULT gen_random_uuid()::text,
    piece_id TEXT DEFAULT '',
    platform TEXT DEFAULT '',
    published_at TIMESTAMPTZ DEFAULT NULL,
    impressions INTEGER DEFAULT 0,
    reach INTEGER DEFAULT 0,
    engagement INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    saves INTEGER DEFAULT 0,
    shares INTEGER DEFAULT 0,
    comments_count INTEGER DEFAULT 0,
    notes TEXT DEFAULT '',
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_metrics_platform ON metrics(platform);
CREATE INDEX IF NOT EXISTS idx_metrics_piece ON metrics(piece_id);
CREATE INDEX IF NOT EXISTS idx_metrics_recorded ON metrics(recorded_at DESC);

-- 4. Calendars (Calendário editorial semanal)
CREATE TABLE IF NOT EXISTS calendars (
    week_id TEXT PRIMARY KEY,
    brand TEXT DEFAULT 'salk',
    year INTEGER DEFAULT 2026,
    status TEXT DEFAULT 'draft',
    slots JSONB DEFAULT '[]'::jsonb,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 5. Row Level Security (RLS)
-- Por enquanto desabilitado — sistema single-tenant (uma gestora)
-- Habilitar quando houver multi-tenant
ALTER TABLE pieces ENABLE ROW LEVEL SECURITY;
ALTER TABLE reviews ENABLE ROW LEVEL SECURITY;
ALTER TABLE metrics ENABLE ROW LEVEL SECURITY;
ALTER TABLE calendars ENABLE ROW LEVEL SECURITY;

-- Política permissiva (service_role key tem acesso total)
CREATE POLICY "Allow all for service role" ON pieces FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all for service role" ON reviews FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all for service role" ON metrics FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all for service role" ON calendars FOR ALL USING (true) WITH CHECK (true);

-- 6. Função de auto-update do updated_at
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER pieces_updated_at
    BEFORE UPDATE ON pieces
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER reviews_updated_at
    BEFORE UPDATE ON reviews
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- 7. View de performance summary (substitui query agregada do Python)
CREATE OR REPLACE VIEW performance_summary AS
SELECT
    platform,
    COUNT(*) as count,
    SUM(impressions) as total_impressions,
    SUM(reach) as total_reach,
    SUM(engagement) as total_engagement,
    SUM(clicks) as total_clicks,
    SUM(saves) as total_saves,
    SUM(shares) as total_shares,
    ROUND(AVG(engagement)::numeric, 2) as avg_engagement
FROM metrics
GROUP BY platform;
