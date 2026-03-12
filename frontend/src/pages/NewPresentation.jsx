import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, Sparkles, Loader2, Presentation, Image } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { toast } from 'sonner';
import { createPresentation } from '@/lib/api';

// Unsplash API for cover images
const UNSPLASH_ACCESS_KEY = process.env.REACT_APP_UNSPLASH_ACCESS_KEY;

export const getUnsplashCoverUrl = async (topic) => {
  try {
    const res = await fetch(
      `https://api.unsplash.com/photos/random?query=${encodeURIComponent(topic)}&orientation=landscape&client_id=${UNSPLASH_ACCESS_KEY}`
    );

    const data = await res.json();
    console.log(data);

    return data?.urls?.regular;
  } catch (error) {
    console.error("Unsplash error:", error);
    return null;
  }
};
export default function NewPresentation() {
  const navigate = useNavigate();
  const [topic, setTopic] = useState('');
  const [content, setContent] = useState('');
  const [creating, setCreating] = useState(false);
  const [previewCover, setPreviewCover] = useState(null);

  useEffect(() => {
    const loadImage = async () => {
      if (!topic.trim()) {
        setPreviewCover(null);
        return;
      }

      const img = await getUnsplashCoverUrl(topic.trim());
      setPreviewCover(img);
    };

    loadImage();
  }, [topic]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!topic.trim()) {
      toast.error('Please enter a topic');
      return;
    }
    if (!content.trim()) {
      toast.error('Please enter content');
      return;
    }

    setCreating(true);
    
    try {
      const result = await createPresentation(topic.trim(), content.trim());
      
      // Generate cover image URL based on topic
      const coverImage = await getUnsplashCoverUrl(topic.trim());
      
      // Save to localStorage
      const stored = localStorage.getItem('slidegenie_presentations');
      const presentations = stored ? JSON.parse(stored) : [];
      
      presentations.unshift({
        id: result.presentation_id,
        topic: topic.trim(),
        createdAt: new Date().toISOString(),
        slideCount: null,
        coverImage: coverImage,
      });
      
      localStorage.setItem('slidegenie_presentations', JSON.stringify(presentations));
      
      toast.success('Presentation created!');
      navigate(`/editor/${result.presentation_id}`);
    } catch (error) {
      console.error('Failed to create:', error);
      toast.error('Failed to create. Is the API running?');
      setCreating(false);
    }
  };

  return (
    <div className="min-h-screen bg-background bg-grid-pattern">
      {/* Header */}
      <header className="border-b border-border glass sticky top-0 z-50">
        <div className="max-w-4xl mx-auto px-6 py-4 flex items-center gap-4">
          <Button variant="ghost" size="icon" onClick={() => navigate('/')}>
            <ArrowLeft className="w-5 h-5" />
          </Button>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-primary/20 flex items-center justify-center">
              <Presentation className="w-5 h-5 text-primary" />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight">New Presentation</h1>
              <p className="text-xs text-muted-foreground uppercase tracking-widest">AI Powered</p>
            </div>
          </div>
        </div>
      </header>

      {/* Main */}
      <main className="max-w-4xl mx-auto px-6 py-12">
        <div className="grid lg:grid-cols-5 gap-8">
          {/* Form */}
          <div className="lg:col-span-3">
            <Card className="border-primary/20">
              <CardHeader>
                <div className="flex items-center gap-2">
                  <Sparkles className="w-5 h-5 text-primary" />
                  <CardTitle>Create Presentation</CardTitle>
                </div>
                <CardDescription>
                  Enter a topic and content. AI will generate slides.
                </CardDescription>
              </CardHeader>
              
              <CardContent>
                <form onSubmit={handleSubmit} className="space-y-6">
                  <div className="space-y-2">
                    <Label htmlFor="topic">Topic</Label>
                    <Input
                      id="topic"
                      data-testid="topic-input"
                      placeholder="Introduction to Machine Learning"
                      value={topic}
                      onChange={(e) => setTopic(e.target.value)}
                      disabled={creating}
                      className="h-12 text-lg"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="content">Content & Notes</Label>
                    <Textarea
                      id="content"
                      data-testid="content-input"
                      placeholder="• Key points to cover&#10;• Main ideas&#10;• Examples and data&#10;&#10;The more detail, the better!"
                      value={content}
                      onChange={(e) => setContent(e.target.value)}
                      disabled={creating}
                      className="min-h-[250px] resize-none"
                    />
                  </div>

                  <div className="flex justify-end gap-4 pt-4">
                    <Button
                      type="button"
                      variant="outline"
                      onClick={() => navigate('/')}
                      disabled={creating}
                    >
                      Cancel
                    </Button>
                    <Button
                      type="submit"
                      data-testid="generate-btn"
                      disabled={creating || !topic.trim() || !content.trim()}
                      className="min-w-[160px] glow-primary"
                    >
                      {creating ? (
                        <>
                          <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                          Creating...
                        </>
                      ) : (
                        <>
                          <Sparkles className="w-4 h-4 mr-2" />
                          Generate
                        </>
                      )}
                    </Button>
                  </div>
                </form>
              </CardContent>
            </Card>
          </div>

          {/* Cover Preview */}
          <div className="lg:col-span-2">
            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-sm flex items-center gap-2">
                  <Image className="w-4 h-4" /> Cover Preview
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="aspect-video rounded-lg overflow-hidden bg-secondary">
                  {previewCover ? (
                    <img
                      src={previewCover}
                      alt="Cover preview"
                      className="w-full h-full object-cover"
                      onError={(e) => {
                        e.target.style.display = 'none';
                      }}
                    />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center">
                      <p className="text-sm text-muted-foreground">
                        Enter a topic to see cover
                      </p>
                    </div>
                  )}
                </div>
                <p className="text-xs text-muted-foreground mt-3 text-center">
                 </p>
              </CardContent>
            </Card>

            {/* Tips */}
            <div className="mt-6 space-y-3">
              {[
                { title: 'Be Specific', desc: 'Detailed topics get better results' },
                { title: 'Add Structure', desc: 'Use bullet points to organize' },
                { title: 'Include Context', desc: 'Mention your audience or goal' },
              ].map((tip, i) => (
                <div key={i} className="p-3 rounded-lg border border-border bg-card/50">
                  <h4 className="text-sm font-medium">{tip.title}</h4>
                  <p className="text-xs text-muted-foreground">{tip.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
