import { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  ArrowLeft,
  ArrowRight,
  Palette,
  Database,
  LayoutTemplate,
  Play,
  Check,
  Loader2,
  AlertCircle,
  RefreshCw,
  Edit3,
  Save,
  ChevronLeft,
  ChevronRight,
  Presentation,
  Code,
  Eye,
  Copy,
  CheckCheck,
  MessageSquare,
  Sparkles,
  Download,
  Wand2,
} from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Textarea } from '@/components/ui/textarea';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { toast } from 'sonner';
import {
  getPresentation,
  getTheme,
  updateTheme,
  getSlidesData,
  updateSlideData,
  getLayouts,
  regenerateSlideLayout,
  streamSlides,
  regenerateSlideCode,
  getApiUrl,
  downloadPresentationPDF,
} from '@/lib/api';

import { THEMES_DATA } from '@/data';
const STAGES = [
  { id: 'theme', label: 'Theme', icon: Palette },
  { id: 'data', label: 'Content', icon: Database },
  { id: 'layout', label: 'Layout', icon: LayoutTemplate },
  { id: 'preview', label: 'Preview', icon: Play },
];

export default function Editor() {
  const { id } = useParams();
  const navigate = useNavigate();
  
  const [stage, setStage] = useState(0);
  const [status, setStatus] = useState({ theme: 'pending', data: 'pending', layout: 'pending', preview: 'pending' });
  const [presentation, setPresentation] = useState(null);
  const [theme, setTheme] = useState('');
  const [themeName, setThemeName] = useState('');
  const [editTheme, setEditTheme] = useState('');
  const [slides, setSlides] = useState([]);
  const [codes, setCodes] = useState({});
  const [activeSlide, setActiveSlide] = useState(0);
  const [loading, setLoading] = useState(true);
  const [working, setWorking] = useState(false);
  const [view, setView] = useState('preview');
  const [copied, setCopied] = useState(false);
  const [downloading, setDownloading] = useState(false);
  
  // Dialogs
  const [editOpen, setEditOpen] = useState(false);
  const [editIdx, setEditIdx] = useState(null);
  const [editContent, setEditContent] = useState('');
  const [editDesc, setEditDesc] = useState('');
  const [saving, setSaving] = useState(false);
  
  const [regenOpen, setRegenOpen] = useState(false);
  const [regenIdx, setRegenIdx] = useState(null);
  const [regenText, setRegenText] = useState('');
  const [regenerating, setRegenerating] = useState(false);

  useEffect(() => { loadData(); }, [id]);

  // Keyboard navigation for slides
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (stage === 3 && !editOpen && !regenOpen) {
        if (e.key === 'ArrowLeft' && activeSlide > 0) {
          e.preventDefault();
          setActiveSlide(p => p - 1);
        } else if (e.key === 'ArrowRight' && activeSlide < slides.length - 1) {
          e.preventDefault();
          setActiveSlide(p => p + 1);
        }
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [stage, activeSlide, slides.length, editOpen, regenOpen]);

  const loadData = async () => {
    try {
      const data = await getPresentation(id);
      setPresentation(data);
      const s = data.state || {};
      if (s.theme_info) { setTheme(s.theme_info); setEditTheme(s.theme_info); setThemeName(s.theme_name || ''); setStatus(p => ({ ...p, theme: 'success' })); }
      if (s.slides_data?.length) {
        setSlides(s.slides_data);
        setStatus(p => ({ ...p, data: 'success', layout: 'success' }));
        const c = {};
        s.slides_data.forEach((sl, i) => { if (sl.slide_code) c[i] = sl.slide_code; });
        if (Object.keys(c).length) { setCodes(c); setStatus(p => ({ ...p, preview: 'success' })); setStage(3); }
      }
    } catch (e) { toast.error('Failed to load'); }
    setLoading(false);
  };

  const runStage = async () => {
    setWorking(true);
    const stageId = STAGES[stage].id;
    setStatus(p => ({ ...p, [stageId]: 'generating' }));
    
    try {
      if (stageId === 'theme') {
        const r = await getTheme(id);
        setTheme(r.theme_info || ''); setEditTheme(r.theme_info || ''); setThemeName(r.theme_name || '');
      } else if (stageId === 'data') {
        const r = await getSlidesData(id);
        setSlides(r.slides_data || []);
      } else if (stageId === 'layout') {
        const r = await getLayouts(id);
        setSlides(r.slides_data || []);
      } else if (stageId === 'preview') {
        setCodes({});
        await streamSlides(id,
          (c) => { if (c.token) setCodes(p => ({ ...p, [c.slide_index]: (p[c.slide_index] || '') + c.token })); },
          () => { setStatus(p => ({ ...p, preview: 'success' })); setWorking(false); toast.success('Done!'); },
          () => { setStatus(p => ({ ...p, preview: 'error' })); setWorking(false); toast.error('Failed'); }
        );
        return;
      }
      setStatus(p => ({ ...p, [stageId]: 'success' }));
      toast.success('Done!');
    } catch (e) {
      setStatus(p => ({ ...p, [stageId]: 'error' }));
      toast.error('Failed');
    }
    setWorking(false);
  };

  const saveThemeChanges = async () => {
    setWorking(true);
    try { await updateTheme(id, editTheme); setTheme(editTheme); toast.success('Saved!'); }
    catch { toast.error('Failed'); }
    setWorking(false);
  };

  const openEdit = (i) => { setEditIdx(i); setEditContent(slides[i]?.content || ''); setEditDesc(slides[i]?.description || ''); setEditOpen(true); };
  
  const saveEdit = async () => {
    setSaving(true);
    try {
      await updateSlideData(id, editIdx, editContent, editDesc);
      setSlides(p => p.map((s, i) => i === editIdx ? { ...s, content: editContent, description: editDesc } : s));
      toast.success('Saved!'); setEditOpen(false);
    } catch { toast.error('Failed'); }
    setSaving(false);
  };

  const regenLayout = async (i) => {
    try { const r = await regenerateSlideLayout(id, i); setSlides(p => p.map((s, j) => j === i ? { ...s, layout: r.layout } : s)); toast.success(r.layout); }
    catch { toast.error('Failed'); }
  };

  const openRegen = (i) => { setRegenIdx(i); setRegenText(''); setRegenOpen(true); };
  
  const doRegen = async () => {
    if (!regenText.trim()) return;
    setRegenerating(true);
    setCodes(p => ({ ...p, [regenIdx]: '' }));
    await regenerateSlideCode(id, regenIdx, regenText,
      (c) => { if (c.token) setCodes(p => ({ ...p, [c.slide_index]: (p[c.slide_index] || '') + c.token })); },
      () => { setRegenerating(false); setRegenOpen(false); toast.success('Done!'); },
      () => { setRegenerating(false); toast.error('Failed'); }
    );
  };

  const copyCode = () => {
    const code = codes[activeSlide] || '';
    const ta = document.createElement('textarea');
    ta.value = code;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    setCopied(true);
    toast.success('Copied!');
    setTimeout(() => setCopied(false), 2000);
  };

  const downloadPDF = async () => {
    setDownloading(true);
    toast.info('Generating PDF...');
    
    try {
      const response = await downloadPresentationPDF(id);
      
      // Create download link
      const blob = response.data;
      const blobUrl = URL.createObjectURL(blob);
      
      // Create safe filename
      let filename = 'presentation';
      if (presentation?.state?.topic) {
        const safeTopic = presentation.state.topic.replace(/[^a-zA-Z0-9\s-]/g, '').replace(/\s+/g, '_');
        filename = `presentation_${safeTopic}`;
      } else {
        filename = `presentation_${id}`;
      }
      filename += '.pdf';
      
      // Create and trigger download
      const link = document.createElement('a');
      link.href = blobUrl;
      link.download = filename;
      link.style.display = 'none';
      document.body.appendChild(link);
      link.click();
      
      // Cleanup
      setTimeout(() => {
        if (document.body.contains(link)) {
          document.body.removeChild(link);
        }
        URL.revokeObjectURL(blobUrl);
      }, 1000);
      
      toast.success(`PDF downloaded: ${filename}`);
    } catch (error) {
      console.error('PDF download error:', error);
      
      // Handle specific error cases
      if (error.response) {
        const status = error.response.status;
        if (status === 404) {
          toast.error('PDF download endpoint not found. This feature may not be implemented on the server yet.');
        } else if (status === 405) {
          toast.error('PDF download is not available yet. This feature is still being developed.');
        } else if (status >= 500) {
          toast.error('Server error while generating PDF. Please try again later.');
        } else {
          toast.error(`Download failed: ${error.response.data?.error || 'Unknown error'}`);
        }
      } else if (error.code === 'NETWORK_ERROR' || error.message.includes('Network')) {
        toast.error('Network error. Please check your connection and try again.');
      } else {
        toast.error(`Download failed: ${error.message}`);
      }
    } finally {
      setDownloading(false);
    }
  };

  const canNext = () => status[STAGES[stage].id] === 'success';

  if (loading) return (
    <div className="h-screen bg-background flex items-center justify-center">
      <Loader2 className="w-10 h-10 animate-spin text-primary" />
    </div>
  );

  return (
    <div className="h-screen flex flex-col bg-[#0a0a0b] overflow-hidden">
      {/* Header */}
      <header className="h-14 px-4 flex items-center justify-between border-b border-zinc-800 bg-zinc-900/80 backdrop-blur shrink-0">
        <div className="flex items-center gap-3">
          <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => navigate('/')}>
            <ArrowLeft className="w-4 h-4" />
          </Button>
          <Presentation className="w-5 h-5 text-indigo-500" />
          <span className="font-medium text-sm truncate max-w-[180px]">{presentation?.state?.topic || 'Untitled'}</span>
        </div>

        <div className="flex items-center gap-1 bg-zinc-800/50 rounded-lg p-1">
          {STAGES.map((s, i) => {
            const Icon = s.icon;
            const st = status[s.id];
            const active = i === stage;
            const canClick = st === 'success' || i <= stage;
            return (
              <button
                key={s.id}
                onClick={() => canClick && setStage(i)}
                disabled={!canClick}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition-all ${
                  active ? 'bg-indigo-600 text-white' :
                  st === 'success' ? 'text-emerald-400 hover:bg-zinc-700 cursor-pointer' :
                  i < stage ? 'text-zinc-400 hover:bg-zinc-700 cursor-pointer' :
                  'text-zinc-500 cursor-not-allowed'
                }`}
              >
                {st === 'generating' ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> :
                 st === 'success' ? <Check className="w-3.5 h-3.5" /> : <Icon className="w-3.5 h-3.5" />}
                <span className="hidden sm:inline">{s.label}</span>
              </button>
            );
          })}
        </div>

        <div className="flex items-center gap-2">
          {status.preview === 'success' && (
            <Button variant="outline" size="sm" className="h-8 text-xs border-zinc-700 hover:bg-zinc-800" onClick={downloadPDF} disabled={downloading}>
              {downloading ? <Loader2 className="w-3.5 h-3.5 animate-spin mr-1.5" /> : <Download className="w-3.5 h-3.5 mr-1.5" />}
              PDF
            </Button>
          )}
        </div>
      </header>

      {/* Content */}
      <div className="flex-1 overflow-hidden">
        {/* Theme Stage */}
        {stage === 0 && (
          <div className="h-full flex flex-col lg:flex-row items-center justify-center p-6 gap-6 overflow-y-auto">
            <div className="w-full max-w-5xl space-y-6">
              <div className="text-center space-y-2">
                <div className="w-16 h-16 rounded-2xl bg-indigo-600/20 flex items-center justify-center mx-auto">
                  <Palette className="w-8 h-8 text-indigo-500" />
                </div>
                <h2 className="text-2xl font-bold">Presentation Theme</h2>
                <p className="text-zinc-500">Define colors, fonts, and visual style</p>
              </div>
              
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <Card className="bg-zinc-900/50 border-zinc-800 flex flex-col">
                  <CardContent className="p-6 space-y-4 flex-1 flex flex-col">
                    <Textarea
                      value={editTheme}
                      onChange={(e) => setEditTheme(e.target.value)}
                      placeholder="Modern dark theme with indigo accents, Inter font, clean minimal design..."
                      className="flex-1 min-h-[400px] bg-zinc-800/50 border-zinc-700 text-sm resize-none"
                    />
                    <div className="flex gap-3">
                      <Button onClick={runStage} disabled={working} className="bg-indigo-600 hover:bg-indigo-700">
                        {working ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Wand2 className="w-4 h-4 mr-2" />}
                        Generate Theme
                      </Button>
                      {editTheme && editTheme !== theme && (
                        <Button variant="outline" onClick={saveThemeChanges} disabled={working} className="border-zinc-700">
                          <Save className="w-4 h-4 mr-2" /> Save
                        </Button>
                      )}
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-zinc-900/50 border-zinc-800 flex flex-col shadow-xl overflow-hidden">
                  <div className="px-6 py-4 border-b border-zinc-800 flex items-center justify-between bg-zinc-900">
                    <div className="flex items-center gap-2">
                      <Eye className="w-4 h-4 text-zinc-400" />
                      <span className="text-sm font-medium text-zinc-300">Theme Preview</span>
                    </div>
                    {themeName && (
                      <span className="text-xs px-2 py-1 rounded-md bg-zinc-800 text-zinc-400">
                        {themeName}
                      </span>
                    )}
                  </div>
                  <CardContent className="p-6 flex-1 flex bg-zinc-950/50 min-h-[400px]">
                    <div 
                      className="w-full h-full flex flex-col items-center justify-center"
                      dangerouslySetInnerHTML={{ 
                        __html: THEMES_DATA[themeName] || THEMES_DATA['Dummy Preview'] 
                      }} 
                    />
                  </CardContent>
                </Card>
              </div>

              <div className="flex justify-between pt-4">
                <div />
                <Button onClick={() => canNext() && setStage(1)} disabled={!canNext()} className="bg-indigo-600 hover:bg-indigo-700">
                  Continue <ArrowRight className="w-4 h-4 ml-2" />
                </Button>
              </div>
            </div>
          </div>
        )}

        {/* Data Stage */}
        {stage === 1 && (
          <div className="h-full flex flex-col p-6">
            <div className="text-center space-y-2 mb-6">
              <div className="w-14 h-14 rounded-2xl bg-indigo-600/20 flex items-center justify-center mx-auto">
                <Database className="w-7 h-7 text-indigo-500" />
              </div>
              <h2 className="text-xl font-bold">Slide Content</h2>
              <p className="text-zinc-500 text-sm">Generate and edit content for each slide</p>
            </div>

            <div className="flex justify-center mb-6">
              <Button onClick={runStage} disabled={working} className="bg-indigo-600 hover:bg-indigo-700">
                {working ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Wand2 className="w-4 h-4 mr-2" />}
                Generate Content
              </Button>
            </div>

            <div className="flex-1 overflow-auto">
              <div className="max-w-5xl mx-auto grid gap-4">
                {slides.map((sl, i) => (
                  <Card key={i} className="bg-zinc-900/50 border-zinc-800 hover:border-zinc-700 transition-colors min-h-[140px]">
                    <CardContent className="p-6 flex items-start gap-6">
                      <div className="w-12 h-12 rounded-lg bg-indigo-600/20 flex items-center justify-center shrink-0">
                        <span className="text-indigo-400 font-bold text-lg">{i + 1}</span>
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-2 mb-2">
                          {sl.slide_type && <span className="text-xs px-2.5 py-1 rounded bg-zinc-800 text-zinc-400 font-medium">{sl.slide_type}</span>}
                        </div>
                        <p className="text-base text-zinc-300 line-clamp-4 leading-relaxed">{sl.content || 'No content'}</p>
                      </div>
                      <Button variant="ghost" size="icon" className="h-10 w-10 shrink-0" onClick={() => openEdit(i)}>
                        <Edit3 className="w-5 h-5" />
                      </Button>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>

            <div className="flex justify-between pt-6 border-t border-zinc-800 mt-6">
              <Button variant="outline" onClick={() => setStage(0)} className="border-zinc-700">
                <ArrowLeft className="w-4 h-4 mr-2" /> Back
              </Button>
              <Button onClick={() => canNext() && setStage(2)} disabled={!canNext()} className="bg-indigo-600 hover:bg-indigo-700">
                Continue <ArrowRight className="w-4 h-4 ml-2" />
              </Button>
            </div>
          </div>
        )}

        {/* Layout Stage */}
        {stage === 2 && (
          <div className="h-full flex flex-col p-6">
            <div className="text-center space-y-2 mb-6">
              <div className="w-14 h-14 rounded-2xl bg-indigo-600/20 flex items-center justify-center mx-auto">
                <LayoutTemplate className="w-7 h-7 text-indigo-500" />
              </div>
              <h2 className="text-xl font-bold">Slide Layouts</h2>
              <p className="text-zinc-500 text-sm">Assign visual layouts to each slide</p>
            </div>

            <div className="flex justify-center mb-6">
              <Button onClick={runStage} disabled={working} className="bg-indigo-600 hover:bg-indigo-700">
                {working ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Wand2 className="w-4 h-4 mr-2" />}
                Assign Layouts
              </Button>
            </div>

            <div className="flex-1 overflow-auto">
              <div className="max-w-3xl mx-auto grid gap-3">
                {slides.map((sl, i) => (
                  <Card key={i} className="bg-zinc-900/50 border-zinc-800 hover:border-zinc-700 transition-colors">
                    <CardContent className="p-4 flex items-center justify-between">
                      <div className="flex items-center gap-4">
                        <div className="w-10 h-10 rounded-lg bg-indigo-600/20 flex items-center justify-center">
                          <span className="text-indigo-400 font-bold text-sm">{i + 1}</span>
                        </div>
                        <div>
                          <p className="text-sm text-zinc-300 truncate max-w-[300px]">{sl.content?.substring(0, 50)}...</p>
                          <span className="text-xs px-2 py-0.5 rounded bg-emerald-600/20 text-emerald-400 inline-block mt-1">
                            {sl.layout || 'No layout'}
                          </span>
                        </div>
                      </div>
                      <Button variant="outline" size="sm" className="border-zinc-700 h-8" onClick={() => regenLayout(i)}>
                        <RefreshCw className="w-3.5 h-3.5 mr-1.5" /> Regenerate
                      </Button>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>

            <div className="flex justify-between pt-6 border-t border-zinc-800 mt-6">
              <Button variant="outline" onClick={() => setStage(1)} className="border-zinc-700">
                <ArrowLeft className="w-4 h-4 mr-2" /> Back
              </Button>
              <Button onClick={() => canNext() && setStage(3)} disabled={!canNext()} className="bg-indigo-600 hover:bg-indigo-700">
                Continue <ArrowRight className="w-4 h-4 ml-2" />
              </Button>
            </div>
          </div>
        )}

        {/* Preview Stage */}
        {stage === 3 && (
          <div className="h-full flex flex-col">
            {/* Preview Controls */}
            <div className="h-12 px-4 flex items-center justify-between border-b border-zinc-800 shrink-0">
              <div className="flex items-center gap-3">
                <Button variant="ghost" size="sm" className="h-8 text-xs" onClick={() => setStage(2)}>
                  <ArrowLeft className="w-3.5 h-3.5 mr-1.5" /> Back
                </Button>
                {!Object.keys(codes).length && (
                  <Button size="sm" className="h-8 text-xs bg-indigo-600 hover:bg-indigo-700" onClick={runStage} disabled={working}>
                    {working ? <Loader2 className="w-3.5 h-3.5 mr-1.5 animate-spin" /> : <Play className="w-3.5 h-3.5 mr-1.5" />}
                    Generate Slides
                  </Button>
                )}
              </div>

              {slides.length > 0 && (
                <div className="flex items-center gap-2">
                  <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => setActiveSlide(p => Math.max(0, p - 1))} disabled={activeSlide === 0}>
                    <ChevronLeft className="w-5 h-5" />
                  </Button>
                  <span className="text-sm font-medium min-w-[60px] text-center text-zinc-400">
                    {activeSlide + 1} / {slides.length}
                  </span>
                  <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => setActiveSlide(p => Math.min(slides.length - 1, p + 1))} disabled={activeSlide === slides.length - 1}>
                    <ChevronRight className="w-5 h-5" />
                  </Button>
                </div>
              )}

              <div className="flex items-center gap-2">
                {codes[activeSlide] && (
                  <>
                    <Button variant="ghost" size="sm" className="h-8 text-xs" onClick={() => openRegen(activeSlide)}>
                      <MessageSquare className="w-3.5 h-3.5 mr-1.5" /> Edit with AI
                    </Button>
                    <Button variant="ghost" size="sm" className="h-8 text-xs" onClick={copyCode}>
                      {copied ? <CheckCheck className="w-3.5 h-3.5 mr-1.5" /> : <Copy className="w-3.5 h-3.5 mr-1.5" />}
                      {copied ? 'Copied!' : 'Copy'}
                    </Button>
                  </>
                )}
                <div className="flex bg-zinc-800 rounded-md p-0.5">
                  <button
                    onClick={() => setView('preview')}
                    className={`px-3 py-1 rounded text-xs font-medium transition-colors ${view === 'preview' ? 'bg-indigo-600 text-white' : 'text-zinc-400 hover:text-white'}`}
                  >
                    <Eye className="w-3.5 h-3.5 inline mr-1" /> Preview
                  </button>
                  <button
                    onClick={() => setView('code')}
                    className={`px-3 py-1 rounded text-xs font-medium transition-colors ${view === 'code' ? 'bg-indigo-600 text-white' : 'text-zinc-400 hover:text-white'}`}
                  >
                    <Code className="w-3.5 h-3.5 inline mr-1" /> Code
                  </button>
                </div>
              </div>
            </div>

            {/* Slide View - Fixed size, no scroll */}
            <div className="flex-1 flex items-center justify-center p-4 bg-zinc-950 min-h-0">
              <div 
                className="rounded-lg overflow-hidden shadow-2xl shadow-black/50 bg-black"
                style={{ 
                  width: '100%',
                  maxWidth: 'calc((100vh - 180px) * 16 / 9)',
                  aspectRatio: '16/9'
                }}
              >
                {view === 'preview' ? (
                  codes[activeSlide] ? (
                    <iframe 
                      srcDoc={
                        (codes[activeSlide] || '') + 
                        `<style>
                          body, html { margin: 0 !important; padding: 0 !important; overflow: hidden !important; width: 100%; height: 100%; display: block !important; }
                          .slide-container { position: absolute !important; top: 0 !important; left: 0 !important; margin: 0 !important; transform-origin: top left !important; }
                        </style>
                        <script>
                          function fit() {
                            const slide = document.querySelector('.slide-container');
                            if (slide) {
                              slide.style.transform = 'scale(' + (window.innerWidth / 1280) + ')';
                            }
                          }
                          window.addEventListener('resize', fit);
                          new MutationObserver(fit).observe(document.documentElement, { childList: true, subtree: true });
                          fit();
                        </script>`
                      } 
                      className="w-full h-full border-0 block" 
                      style={{ backgroundColor: 'black' }}
                      sandbox="allow-scripts" 
                    />
                  ) : working ? (
                    <div className="w-full h-full flex items-center justify-center bg-zinc-900">
                      <div className="text-center">
                        <Loader2 className="w-10 h-10 animate-spin text-indigo-500 mx-auto mb-3" />
                        <p className="text-zinc-500 text-sm">Generating slide {activeSlide + 1}...</p>
                      </div>
                    </div>
                  ) : (
                    <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-zinc-900 to-zinc-950">
                      <div className="text-center">
                        <Play className="w-16 h-16 text-zinc-700 mx-auto mb-4" />
                        <p className="text-zinc-600">Click "Generate Slides"</p>
                      </div>
                    </div>
                  )
                ) : (
                  <div className="w-full h-full bg-[#1e1e1e] p-4 overflow-auto">
                    <pre className="text-xs font-mono text-emerald-400 whitespace-pre-wrap leading-relaxed">
                      {codes[activeSlide] || '<!-- No code yet -->'}
                    </pre>
                  </div>
                )}
              </div>
            </div>

            {/* Thumbnails - Horizontal scroll */}
            {slides.length > 0 && (
              <div className="h-20 px-4 py-2 border-t  border-zinc-800 bg-zinc-900/80 shrink-0 overflow-hidden">
                <div className="flex gap-2 h-full overflow-x-auto scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent pb-1">
                  {slides.map((_, i) => (
                    <button
                      key={i}
                      onClick={() => setActiveSlide(i)}
                      className={`h-full aspect-video rounded overflow-hidden border-2 transition-all shrink-0 ${
                        activeSlide === i ? 'border-indigo-500 ring-1 ring-indigo-500/50 scale-105' : 'border-zinc-700 hover:border-zinc-500 opacity-70 hover:opacity-100'
                      }`}
                    >
                      {codes[i] ? (
                        <iframe 
                          srcDoc={
                            (codes[i] || '') +
                            `<style>
                              html, body {
                                margin:0 !important;
                                padding:0 !important;
                                overflow:hidden !important;
                                width:1280px !important;
                                height:720px !important;
                                display:block !important;
                                background:white;
                              }
                        
                              body{
                                transform:none !important;
                                display:block !important;
                              }
                        
                              .slide-container{
                                position:absolute !important;
                                top:0 !important;
                                left:0 !important;
                              }
                            </style>`
                          }
                          className="w-full h-full border-0 pointer-events-none" 
                          style={{ 
                            transform: 'scale(0.08)', 
                            transformOrigin: 'top left', 
                            width: '1250%', 
                            height: '1250%',
                            backgroundColor: 'black'
                          }} 
                        />
                      ) : (
                        <div className="w-full h-full flex items-center justify-center bg-zinc-800 text-zinc-500 text-xs font-bold">
                          {i + 1}
                        </div>
                      )}
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Edit Dialog */}
      <Dialog open={editOpen} onOpenChange={setEditOpen}>
        <DialogContent className="bg-zinc-900 border-zinc-800">
          <DialogHeader>
            <DialogTitle>Edit Slide {editIdx !== null ? editIdx + 1 : ''}</DialogTitle>
          </DialogHeader>
          <div className="space-y-4 py-4">
            <div className="space-y-2">
              <Label className="text-zinc-400">Content</Label>
              <Textarea value={editContent} onChange={(e) => setEditContent(e.target.value)} className="min-h-[120px] bg-zinc-800 border-zinc-700" />
            </div>
            <div className="space-y-2">
              <Label className="text-zinc-400">Visual Description</Label>
              <Input value={editDesc} onChange={(e) => setEditDesc(e.target.value)} className="bg-zinc-800 border-zinc-700" />
            </div>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setEditOpen(false)} className="border-zinc-700">Cancel</Button>
            <Button onClick={saveEdit} disabled={saving} className="bg-indigo-600 hover:bg-indigo-700">
              {saving ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Save className="w-4 h-4 mr-2" />} Save
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* Regen Dialog */}
      <Dialog open={regenOpen} onOpenChange={setRegenOpen}>
        <DialogContent className="bg-zinc-900 border-zinc-800">
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-indigo-500" /> Edit with AI
            </DialogTitle>
            <DialogDescription className="text-zinc-500">Describe the changes you want</DialogDescription>
          </DialogHeader>
          <Textarea
            value={regenText}
            onChange={(e) => setRegenText(e.target.value)}
            placeholder="Make the background darker, larger text, add animation..."
            className="min-h-[100px] bg-zinc-800 border-zinc-700"
          />
          <DialogFooter>
            <Button variant="outline" onClick={() => setRegenOpen(false)} disabled={regenerating} className="border-zinc-700">Cancel</Button>
            <Button onClick={doRegen} disabled={regenerating || !regenText.trim()} className="bg-indigo-600 hover:bg-indigo-700">
              {regenerating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Sparkles className="w-4 h-4 mr-2" />} Regenerate
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}
