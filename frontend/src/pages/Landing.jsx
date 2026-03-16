import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Sparkles, LayoutDashboard, Zap, Presentation, Wand2, ChevronRight, ChevronLeft, Github, Star, Rocket, Layers, Play, X } from 'lucide-react';
import { Button } from '@/components/ui/button';

export default function Landing() {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);
  const [currentPdfIndex, setCurrentPdfIndex] = useState(0);
  const [isVideoModalOpen, setIsVideoModalOpen] = useState(false);
  const [pdfError, setPdfError] = useState(false);

  // Sample PDFs – ensure these files exist in your public folder
  const samplePdfs = ['/demo.pdf', '/demo1.pdf', '/demo2.pdf', '/demo3.pdf'];

  const nextPdf = (e) => {
    e.stopPropagation();
    setCurrentPdfIndex((prev) => (prev + 1) % samplePdfs.length);
    setPdfError(false); // reset error on change
  };

  const prevPdf = (e) => {
    e.stopPropagation();
    setCurrentPdfIndex((prev) => (prev - 1 + samplePdfs.length) % samplePdfs.length);
    setPdfError(false);
  };

  // Reset error when index changes (handled inside setters above)
  useEffect(() => {
    setPdfError(false);
  }, [currentPdfIndex]);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    
    <div className="min-h-screen bg-[#0a0a0a] relative overflow-x-hidden text-foreground selection:bg-primary/30">

      {/* ========== BACKGROUND VIDEO ========== */}
      <div className="fixed inset-0 z-0 bg-black">
        <video
          autoPlay
          loop
          muted
          playsInline
          className="w-full h-full object-cover opacity-30 mix-blend-screen scale-105" // reduced opacity for less blur
        >
          <source src="https://assets.mixkit.co/videos/preview/mixkit-abstract-liquids-flowing-in-purple-hues-14421-large.mp4" type="video/mp4" />
        </video>
        {/* Reduced overlay opacity for cleaner look */}
        <div className="absolute inset-0 bg-black/40 backdrop-blur-[1px]"></div>
        <div className="absolute inset-0 bg-gradient-to-b from-black/20 via-transparent to-[#0a0a0a] pointer-events-none"></div>
        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-10 mix-blend-overlay pointer-events-none"></div>
      </div>

      {/* ========== NAVIGATION ========== */}
      <nav className={`fixed top-0 inset-x-0 z-50 transition-all duration-500 border-b ${scrolled ? 'bg-black/60 backdrop-blur-xl border-white/10 shadow-[0_4px_30px_rgba(0,0,0,0.1)] py-4' : 'bg-transparent border-transparent py-6'}`}>
        <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
          <div className="flex items-center gap-3 cursor-pointer group" onClick={() => navigate('/')}>
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary to-[hsl(var(--generating))] p-[1px] group-hover:shadow-[0_0_30px_rgba(99,102,241,0.6)] transition-all duration-500">
              <div className="w-full h-full bg-black/90 backdrop-blur-md rounded-[11px] flex items-center justify-center relative overflow-hidden">
                <div className="absolute inset-0 bg-gradient-to-br from-primary/30 to-transparent"></div>
                <Sparkles className="w-5 h-5 text-primary" />
              </div>
            </div>
            <span className="font-bold text-2xl tracking-tighter font-manrope text-white">Slide Ginie</span>
          </div>

          <div className="flex items-center gap-6">
            <a href="https://github.com/sprakhar778/SlideGenie" target="_blank" rel="noreferrer" className="text-white/60 hover:text-white transition-colors hidden sm:flex items-center gap-2 text-sm font-medium">
              <Github className="w-4 h-4" />
              Star on GitHub
            </a>
            <Button
              onClick={() => navigate('/dashboard')}
              className="bg-white hover:bg-white/90 text-black font-semibold rounded-full px-6 transition-all duration-300 shadow-[0_0_20px_rgba(255,255,255,0.2)] hover:shadow-[0_0_30px_rgba(255,255,255,0.4)]"
            >
              Go to App
            </Button>
          </div>
        </div>
      </nav>

      {/* ========== HERO SECTION ========== */}
      <main className="relative z-10 pt-32 lg:pt-48 pb-20">
        <div className="max-w-[1000px] mx-auto px-6 text-center">

          {/* Glowing badge */}
          <div className="inline-flex items-center justify-center mb-10 animate-fade-in-up">
            <div className="relative group cursor-default">
              <div className="absolute -inset-0.5 bg-gradient-to-r from-primary to-[hsl(var(--generating))] rounded-full blur opacity-40 group-hover:opacity-75 transition duration-1000 group-hover:duration-200"></div>
              <div className="relative flex items-center gap-2 px-4 py-1.5 rounded-full bg-black border border-white/10 text-sm font-medium text-white/80">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
                </span>
                Introducing Slide Ginie AI Engine
              </div>
            </div>
          </div>

          <h1 className="text-5xl sm:text-7xl lg:text-8xl xl:text-[7.5rem] font-black tracking-tighter font-manrope leading-[1.05] mb-8 animate-fade-in-up text-white" style={{ animationDelay: '100ms' }}>
            Presentations.<br className="hidden md:block" />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-zinc-300 via-white to-zinc-400">Created by </span>
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary via-[hsl(var(--generating))] to-primary animate-shimmer bg-[length:200%_auto]">Magic.</span>
          </h1>

          <p className="max-w-3xl mx-auto text-xl sm:text-2xl text-zinc-400 mb-12 leading-relaxed animate-fade-in-up font-medium" style={{ animationDelay: '200ms' }}>
            Stop fighting with layout tools and theme templates. Simply describe what you need, and watch our AI instantly generate a stunning, fully-formatted slide deck.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-6 animate-fade-in-up" style={{ animationDelay: '300ms' }}>
            <Button
              size="lg"
              onClick={() => navigate('/dashboard')}
              className="w-full sm:w-auto bg-white hover:bg-zinc-200 text-black font-bold text-lg px-8 h-16 rounded-full transition-all duration-300 hover:scale-105 shadow-[0_0_40px_rgba(255,255,255,0.3)] group"
            >
              Start Generating for Free
              <ChevronRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
            </Button>
            <Button
              size="lg"
              variant="outline"
              onClick={() => navigate('/dashboard')}
              className="w-full sm:w-auto h-16 px-8 text-lg rounded-full border-white/20 text-white bg-white/5 hover:bg-white/10 backdrop-blur-md transition-colors"
            >
              Open Dashboard
            </Button>
          </div>
        </div>

        {/* Hero Mockup with video */}
        <div className="max-w-6xl mx-auto px-6 mt-24 relative animate-fade-in-up" style={{ animationDelay: '500ms' }}>
          <div className="relative rounded-2xl overflow-hidden p-[1px] group">
            <div className="absolute inset-0 bg-gradient-to-b from-white/30 via-white/5 to-transparent rounded-2xl"></div>

            <div
              className="relative bg-black rounded-2xl overflow-hidden shadow-[0_20px_80px_-15px_rgba(0,0,0,1)] border border-white/10 flex items-center justify-center aspect-[16/9] cursor-pointer group/video"
              onClick={() => setIsVideoModalOpen(true)}
            >
              <video
                autoPlay
                loop
                muted
                playsInline
                className="w-full h-full object-cover opacity-90 transition-all duration-1000 group-hover/video:scale-[1.02] group-hover/video:opacity-50"
              >
                <source src="/demo.webm" type="video/webm" />
              </video>

              {/* Lighter overlay for cleaner look */}
              <div className="absolute inset-0 bg-gradient-to-t from-black/30 via-black/20 to-transparent"></div>

              {/* Play button overlay */}
              <div className="absolute inset-0 flex items-center justify-center z-20 pointer-events-none opacity-0 group-hover/video:opacity-100 transition-opacity duration-500">
                <div className="w-20 h-20 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center shadow-2xl">
                  <Play className="w-8 h-8 text-white ml-2" fill="currentColor" />
                </div>
              </div>

              {/* Floating UI element */}
              <div className="absolute bottom-12 left-12 p-6 rounded-2xl bg-black/60 backdrop-blur-xl border border-white/20 shadow-2xl flex items-center gap-6 animate-float group-hover/video:opacity-0 transition-opacity duration-500 z-10">
                <div className="relative w-14 h-10 rounded-full bg-gradient-to-br from-primary to-[hsl(var(--generating))] p-[1px]">
                  <div className="w-full h-full bg-black rounded-full flex items-center justify-center">
                    <Zap className="w-6 h-6 text-primary animate-pulse" />
                  </div>
                </div>
                <div>
                  <div className="text-xl font-bold text-white mb-1">Deck Generated</div>
                  <div className="text-sm font-medium text-zinc-400 flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
                    Ready for export securely
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* ========== SOCIAL PROOF ========== */}
      <section className="relative z-10 py-16 bg-gradient-to-b from-transparent to-black/50">
        <div className="max-w-7xl mx-auto px-6 flex flex-col items-center">
          <p className="text-sm font-bold text-zinc-500 uppercase tracking-[0.2em] mb-8">Powering presentations for</p>
          <div className="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-40 grayscale hover:grayscale-0 transition-all duration-700">
            <div className="flex items-center gap-3 font-manrope font-black text-2xl"><div className="w-8 h-8 bg-white rounded-sm"></div> ACME</div>
            <div className="flex items-center gap-3 font-manrope font-black text-2xl"><div className="w-8 h-8 rounded-full border-4 border-white"></div> GLOBEX</div>
            <div className="flex items-center gap-3 font-manrope font-black text-2xl"><Layers className="w-8 h-8" /> APEX</div>
            <div className="flex items-center gap-3 font-manrope font-black text-2xl"><div className="w-8 h-8 bg-white rotate-45"></div> SOYLENT</div>
          </div>
        </div>
      </section>

      {/* ========== BENTO GRID FEATURES ========== */}
      <section className="relative z-10 py-32 bg-[#050505]">
        <div className="max-w-7xl mx-auto px-6">
          <div className="mb-20 text-center">
            <h2 className="text-5xl md:text-6xl font-black font-manrope mb-6 text-white tracking-tight">Built for speed.<br />Designed for impact.</h2>
            <p className="text-xl text-zinc-400 max-w-2xl mx-auto font-medium">Stop wasting hours pushing pixels. We handled the design system so you can focus purely on the narrative.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

            {/* Feature 1: Large Span (Contextual Intelligence) */}
            <div className="md:col-span-2 rounded-[2rem] p-10 md:p-14 relative overflow-hidden group bg-gradient-to-br from-zinc-900 to-black border border-white/5 hover:border-white/20 transition-all duration-500">
              <div className="absolute top-0 right-0 w-96 h-96 bg-primary/20 blur-[100px] rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>

              <div className="relative z-10 h-full flex flex-col justify-between">
                <div className="mb-12 max-w-lg">
                  <div className="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 text-white group-hover:bg-primary/20 group-hover:text-primary transition-colors">
                    <Wand2 className="w-7 h-7" />
                  </div>
                  <h3 className="text-4xl font-bold font-manrope mb-4 text-white">Contextual Intelligence</h3>
                  <p className="text-lg text-zinc-400 leading-relaxed">Our AI doesn't just fill templates. It understands the nuance of your prompt, generating structured story arcs, appropriate tone, and visually matching aesthetics.</p>
                </div>

                <div className="relative w-full h-64 rounded-2xl overflow-hidden border border-white/10 mt-auto bg-zinc-950">
                  <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1620121692029-d088224ddc74?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80')] bg-cover opacity-50 mix-blend-screen mix-blend-color-dodge transition-transform duration-1000 group-hover:scale-110"></div>
                </div>
              </div>
            </div>

            {/* Feature 2: Small Box (Zero to Deck) */}
            <div className="rounded-[2rem] p-10 relative overflow-hidden group bg-gradient-to-b from-zinc-900 to-black border border-white/5 hover:border-white/20 transition-all duration-500">
              <div className="absolute bottom-0 left-0 w-64 h-64 bg-[hsl(var(--generating))]/20 blur-[80px] rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>

              <div className="relative z-10 flex flex-col h-full">
                <div className="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 text-white group-hover:bg-[hsl(var(--generating))]/20 group-hover:text-[hsl(var(--generating))] transition-colors">
                  <Zap className="w-7 h-7" />
                </div>
                <h3 className="text-3xl font-bold font-manrope mb-4 text-white">Zero to Deck instantly</h3>
                <p className="text-zinc-400 mb-10 text-lg">Type a prompt. Watch a fully formatted presentation assemble itself.</p>

                <div className="w-full aspect-square rounded-2xl bg-black border border-white/10 flex items-center justify-center relative overflow-hidden mt-auto">
                  <Rocket className="w-20 h-20 text-white/20 group-hover:text-white group-hover:-translate-y-4 group-hover:scale-110 transition-all duration-700 ease-out" />
                </div>
              </div>
            </div>

            {/* Feature 3: Small Box (Export Anywhere) with PDF Carousel */}
            <div className="md:col-span-2 rounded-[2rem] p-10 relative overflow-hidden group bg-gradient-to-b from-zinc-900 to-black border border-white/5 hover:border-white/20 transition-all duration-500">
              <div className="absolute top-0 left-0 w-64 h-64 bg-green-500/10 blur-[80px] rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>

              <div className="relative z-10 flex flex-col h-full">
                <div className="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 text-white group-hover:bg-green-500/20 group-hover:text-green-400 transition-colors">
                  <Presentation className="w-7 h-7" />
                </div>
                <h3 className="text-3xl font-bold font-manrope mb-4 text-white">Export Anywhere</h3>
                <p className="text-zinc-400 mb-10 text-lg">Download high-fidelity PDFs directly to your machine seamlessly.</p>

                {/* PDF Preview Carousel */}
                <div className="w-full aspect-square rounded-2xl bg-black border border-white/10 flex flex-col justify-end p-6 relative mt-auto shadow-lg group-hover:border-green-500/30 transition-colors overflow-hidden">
                  {/* PDF container with navigation */}
                  <div className="absolute inset-x-6 top-6 bottom-14 border border-white/10 rounded-xl overflow-hidden bg-zinc-900 group-hover:border-green-500/50 transition-colors flex flex-col">
                    {/* Header Bar */}
                    <div className="h-8 w-full bg-zinc-950/80 border-b border-white/10 flex items-center px-4 gap-2">
                      <div className="w-2.5 h-2.5 rounded-full bg-red-500/80"></div>
                      <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/80"></div>
                      <div className="w-2.5 h-2.5 rounded-full bg-green-500/80"></div>
                      <span className="ml-auto text-[10px] uppercase font-bold tracking-wider text-zinc-600">Generated_Deck_{currentPdfIndex + 1}.pdf</span>
                    </div>

                 
                    {/* PDF display */}
                    <div className="flex-1 relative bg-black overflow-hidden rounded-b-lg">
                      <object
                        data={`${samplePdfs[currentPdfIndex]}#scrollbar=0&toolbar=0&navpanes=0&view=Fit`}
                        type="application/pdf"
                        className="absolute top-0 left-0 w-[calc(100%+24px)] h-[calc(100%+24px)] max-w-none bg-white"
                        onError={() => setPdfError(true)}
                      >
                        {/* Fallback content if PDF fails */}
                        <div className="w-full h-full flex flex-col items-center justify-center text-zinc-400 text-sm p-4 text-center bg-zinc-100 rounded border border-dashed border-zinc-300">
                          {pdfError ? (
                            <>
                              <Presentation className="w-8 h-8 mb-3 text-zinc-400 mx-auto" />
                              <span className="text-zinc-500 font-medium">Preview unavailable.<br />Click 'Open' below to view.</span>
                            </>
                          ) : (
                            <span className="text-zinc-500 font-medium animate-pulse">Loading Document...</span>
                          )}
                        </div>
                      </object>
                    </div>

                    {/* Carousel Controls Overlay */}
                    <div className="absolute inset-0 flex items-center justify-between opacity-0 group-hover:opacity-100 transition-opacity z-30 px-3 pointer-events-none">
                      <button
                        onClick={prevPdf}
                        className="p-2 rounded-full bg-black/80 hover:bg-black text-white pointer-events-auto backdrop-blur-md border border-white/20 transition-all hover:scale-110 shadow-2xl"
                        aria-label="Previous PDF"
                      >
                        <ChevronLeft className="w-5 h-5" />
                      </button>
                      <button
                        onClick={nextPdf}
                        className="p-2 rounded-full bg-black/80 hover:bg-black text-white pointer-events-auto backdrop-blur-md border border-white/20 transition-all hover:scale-110 shadow-2xl"
                        aria-label="Next PDF"
                      >
                        <ChevronRight className="w-5 h-5" />
                      </button>
                    </div>

                    {/* Open button Override */}
                    <div className="absolute inset-x-0 bottom-6 flex justify-center z-40 pointer-events-none opacity-0 group-hover:opacity-100 transform translate-y-4 group-hover:translate-y-0 transition-all duration-300">
                      <Button
                        variant="secondary"
                        size="sm"
                        className="rounded-full shadow-[0_0_20px_rgba(0,0,0,0.5)] pointer-events-auto bg-black border border-white/10 hover:bg-black text-white font-semibold backdrop-blur-md"
                        onClick={() => window.open(samplePdfs[currentPdfIndex], '_blank')}
                      >
                        Open Full Screen
                      </Button>
                    </div>
                  </div>

                  {/* Progress bar container */}
                  <div className="h-2 w-full bg-zinc-800/50 rounded-full overflow-hidden z-10 relative">
                    <div className="h-full bg-gradient-to-r from-green-500 to-emerald-400 transition-all duration-500 ease-out" style={{ width: `${((currentPdfIndex + 1) / samplePdfs.length) * 100}%` }}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Feature 4: Large Span (Command Center) */}
            <div className="md:col-span-1 rounded-[2rem] p-10 md:p-14 relative overflow-hidden group bg-gradient-to-bl from-zinc-900 to-black border border-white/5 hover:border-white/20 transition-all duration-500">
              <div className="relative z-10 flex flex-col md:flex-row items-center gap-16 h-full">
                <div className="flex-1 max-w-sm">
                  <div className="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 text-white group-hover:bg-white/10 transition-colors">
                    <LayoutDashboard className="w-7 h-7" />
                  </div>
                  <h3 className="text-4xl font-bold font-manrope mb-4 text-white">Command Center</h3>
                  <p className="text-lg text-zinc-400 leading-relaxed">Manage everything in one hyper-optimized workspace. Resume drafts, view history, or spin up new ideas on the fly.</p>
                </div>

              
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ========== MASSIVE CTA ========== */}
      <section className="relative z-10 py-40 bg-black overflow-hidden border-t border-white/5">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[400px] bg-gradient-to-r from-primary to-[hsl(var(--generating))] rounded-full blur-[150px] opacity-20 pointer-events-none"></div>

        <div className="max-w-4xl mx-auto px-6 text-center space-y-10 relative z-10">
          <h2 className="text-6xl md:text-8xl font-black font-manrope text-white tracking-tighter">Ready to build?</h2>
          <p className="text-2xl text-zinc-400 max-w-2xl mx-auto font-medium">Join the next evolution of presentation design. No credit card required.</p>

          <div className="pt-10">
            <Button
              size="lg"
              onClick={() => navigate('/dashboard')}
              className="bg-white text-black hover:bg-zinc-200 font-bold text-2xl px-16 h-20 rounded-full transition-all duration-300 hover:scale-105 shadow-[0_0_60px_rgba(255,255,255,0.4)]"
            >
              Start Using Slide Ginie
            </Button>
          </div>
        </div>
      </section>

      {/* ========== FOOTER ========== */}
      <footer className="relative z-10 py-12 bg-black border-t border-white/10">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="flex items-center gap-3">
            <Sparkles className="w-5 h-5 text-white" />
            <span className="font-bold text-xl font-manrope text-white tracking-tight">Slide Ginie</span>
          </div>
          <p className="text-sm font-medium text-zinc-500">© {new Date().getFullYear()} Slide Ginie AI Engine.</p>
          <div className="flex items-center gap-6 text-zinc-500">
            <a href="#" className="hover:text-white text-sm font-medium transition-colors">Privacy</a>
            <a href="#" className="hover:text-white text-sm font-medium transition-colors">Terms</a>
            <a href="https://github.com/sprakhar778/SlideGenie" target="_blank" rel="noreferrer" className="hover:text-white transition-colors"><Github className="w-5 h-5" /></a>
          </div>
        </div>
      </footer>

      {/* ========== VIDEO MODAL ========== */}
      {isVideoModalOpen && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 sm:p-6 lg:p-12 animate-in fade-in duration-300">
          <button
            onClick={() => setIsVideoModalOpen(false)}
            className="absolute top-6 right-6 p-4 rounded-full bg-white/10 hover:bg-white/20 text-white transition-colors z-[110] focus:outline-none backdrop-blur-md border border-white/10"
          >
            <X className="w-6 h-6" />
          </button>
          <div className="w-full max-w-6xl aspect-[16/9] bg-black rounded-2xl overflow-hidden border border-white/10 shadow-[0_0_100px_rgba(0,0,0,0.8)] relative animate-in zoom-in-95 duration-500">
            <video
              src="/demo.webm"
              autoPlay
              controls
              className="w-full h-full object-contain"
            ></video>
          </div>
        </div>
      )}
    </div>
  );
}