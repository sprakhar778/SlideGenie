import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Plus, Trash2, Presentation, Clock, AlertCircle, Loader2, Settings, X, Check } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from '@/components/ui/alert-dialog';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { toast } from 'sonner';
import { deletePresentation, healthCheck, getApiUrl, setApiUrl } from '@/lib/api';

export default function Dashboard() {
  const navigate = useNavigate();
  const [presentations, setPresentations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [apiStatus, setApiStatus] = useState('checking');
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [selectedPresentation, setSelectedPresentation] = useState(null);
  const [deleting, setDeleting] = useState(false);
  
  
  // Settings state
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [apiUrlInput, setApiUrlInput] = useState("http://localhost:8000");
  const [testingConnection, setTestingConnection] = useState(false);

  useEffect(() => {
    checkApiHealth();
    loadPresentations();
  }, []);

  const checkApiHealth = async () => {
    setApiStatus('checking');
    try {
      const result = await healthCheck();
      setApiStatus(result.status === 'ok' ? 'connected' : 'error');
    } catch {
      setApiStatus('error');
    }
  };

  const loadPresentations = async () => {
    setLoading(true);
    const stored = localStorage.getItem('slidegenie_presentations');
    if (stored) {
      setPresentations(JSON.parse(stored));
    }
    setLoading(false);
  };

  const handleDelete = async () => {
    if (!selectedPresentation) return;
    
    setDeleting(true);
    try {
      await deletePresentation(selectedPresentation.id);
      
      const updated = presentations.filter(p => p.id !== selectedPresentation.id);
      setPresentations(updated);
      localStorage.setItem('slidegenie_presentations', JSON.stringify(updated));
      
      toast.success('Presentation deleted');
    } catch (error) {
      // Still remove from UI
      const updated = presentations.filter(p => p.id !== selectedPresentation.id);
      setPresentations(updated);
      localStorage.setItem('slidegenie_presentations', JSON.stringify(updated));
      toast.success('Presentation removed');
    } finally {
      setDeleting(false);
      setDeleteDialogOpen(false);
      setSelectedPresentation(null);
    }
  };

  const openPresentation = (presentation) => {
    navigate(`/editor/${presentation.id}`);
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const diff = now - date;
    
    if (diff < 60000) return 'Just now';
    if (diff < 3600000) return `${Math.floor(diff / 60000)}m ago`;
    if (diff < 86400000) return `${Math.floor(diff / 3600000)}h ago`;
    if (diff < 604800000) return `${Math.floor(diff / 86400000)}d ago`;
    
    return date.toLocaleDateString();
  };

  const handleSaveApiUrl = () => {
    const url = apiUrlInput.trim().replace(/\/$/, ''); // Remove trailing slash
    setApiUrl(url);
    setSettingsOpen(false);
    toast.success('API URL updated');
    checkApiHealth();
  };

  const handleTestConnection = async () => {
    setTestingConnection(true);
    const url = apiUrlInput.trim().replace(/\/$/, '');
    
    try {
      const response = await fetch(`${url}/health`, {
        headers: {
          'ngrok-skip-browser-warning': 'true',
        },
      });
      if (response.ok) {
        const data = await response.json();
        if (data.status === 'ok') {
          toast.success('Connection successful!');
        } else {
          toast.success('Connected but status unclear');
        }
      } else {
        toast.error(`Connection failed: HTTP ${response.status}`);
      }
    } catch (error) {
      toast.error(`Connection failed: ${error.message}`);
    } finally {
      setTestingConnection(false);
    }
  };

  return (
    <div className="min-h-screen bg-background bg-grid-pattern">
      {/* Header */}
      <header className="border-b border-border glass sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-primary/20 flex items-center justify-center">
              <Presentation className="w-5 h-5 text-primary" />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight font-[Manrope]">SlideGenie</h1>
              <p className="text-xs text-muted-foreground uppercase tracking-widest">
                AI Presentation Studio
              </p>
            </div>
          </div>
          
          <div className="flex items-center gap-4">
            {/* API Status */}
            <button
              onClick={() => setSettingsOpen(true)}
              className="flex items-center gap-2 text-sm hover:bg-secondary/50 px-3 py-1.5 rounded-lg transition-colors"
              data-testid="api-status-btn"
            >
              <div className={`status-dot ${apiStatus === 'connected' ? 'success' : apiStatus === 'error' ? 'error' : 'generating'}`} />
              <span className="text-muted-foreground">
                {apiStatus === 'connected' ? 'API Connected' : apiStatus === 'error' ? 'API Offline' : 'Checking...'}
              </span>
              <Settings className="w-4 h-4 text-muted-foreground" />
            </button>
            
            <Button
              data-testid="create-presentation-btn"
              onClick={() => navigate('/new')}
              className="glow-primary"
            >
              <Plus className="w-4 h-4 mr-2" />
              New Presentation
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-12">
        {/* Section Header */}
        <div className="mb-8">
          <h2 className="text-3xl font-semibold tracking-tight mb-2">Your Presentations</h2>
          <p className="text-muted-foreground">
            {presentations.length} presentation{presentations.length !== 1 ? 's' : ''} in your workspace
          </p>
        </div>

        {/* Loading State */}
        {loading ? (
          <div className="flex items-center justify-center py-24">
            <Loader2 className="w-8 h-8 animate-spin text-primary" />
          </div>
        ) : presentations.length === 0 ? (
          /* Empty State */
          <Card className="border-dashed">
            <CardContent className="py-16 text-center">
              <div className="w-16 h-16 rounded-2xl bg-primary/10 flex items-center justify-center mx-auto mb-6">
                <Presentation className="w-8 h-8 text-primary" />
              </div>
              <h3 className="text-xl font-semibold mb-2">No presentations yet</h3>
              <p className="text-muted-foreground mb-6 max-w-md mx-auto">
                Create your first AI-powered presentation and watch the magic happen.
              </p>
              <Button
                data-testid="empty-create-btn"
                onClick={() => navigate('/new')}
                className="glow-primary"
              >
                <Plus className="w-4 h-4 mr-2" />
                Create Presentation
              </Button>
            </CardContent>
          </Card>
        ) : (
          /* Presentations Grid */
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {presentations.map((presentation) => (
              <Card
                key={presentation.id}
                data-testid={`presentation-card-${presentation.id}`}
                className="group relative overflow-hidden cursor-pointer transition-all duration-300 hover:border-primary/50 hover:shadow-lg hover:shadow-primary/10"
                onClick={() => openPresentation(presentation)}
              >
                {/* Cover Image */}
                <div className="aspect-video overflow-hidden bg-secondary">
                  {presentation.coverImage ? (
                    <img
                      src={presentation.coverImage}
                      alt={presentation.topic}
                      className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                    />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-primary/20 to-secondary">
                      <Presentation className="w-12 h-12 text-muted-foreground/50" />
                    </div>
                  )}
                </div>

                <CardContent className="p-4">
                  <h3 className="font-semibold text-lg mb-2 line-clamp-2 group-hover:text-primary transition-colors">
                    {presentation.topic}
                  </h3>
                  
                  <div className="flex items-center justify-between text-sm text-muted-foreground">
                    <div className="flex items-center gap-1">
                      <Clock className="w-3.5 h-3.5" />
                      <span>{formatDate(presentation.createdAt)}</span>
                    </div>
                    <span>{presentation.slideCount || '?'} slides</span>
                  </div>
                </CardContent>

                {/* Delete Button */}
                <button
                  data-testid={`delete-btn-${presentation.id}`}
                  className="absolute top-3 right-3 w-8 h-8 rounded-lg bg-destructive/80 backdrop-blur-sm flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity hover:bg-destructive"
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedPresentation(presentation);
                    setDeleteDialogOpen(true);
                  }}
                >
                  <Trash2 className="w-4 h-4 text-destructive-foreground" />
                </button>
              </Card>
            ))}
          </div>
        )}

        {/* API Warning */}
        {apiStatus === 'error' && (
          <div className="mt-8 p-4 rounded-xl border border-warning/30 bg-warning/10 flex items-start gap-3">
            <AlertCircle className="w-5 h-5 text-warning mt-0.5" />
            <div>
              <h4 className="font-medium text-warning">SlideGenie API Offline</h4>
              <p className="text-sm text-muted-foreground mt-1">
                Cannot connect to your API. Click the settings icon above to configure your API URL. Make sure CORS is enabled on your server.
              </p>
            </div>
          </div>
        )}
      </main>

      {/* Delete Confirmation Dialog */}
      <AlertDialog open={deleteDialogOpen} onOpenChange={setDeleteDialogOpen}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Delete Presentation?</AlertDialogTitle>
            <AlertDialogDescription>
              This will permanently delete &quot;{selectedPresentation?.topic}&quot;. This action cannot be undone.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel data-testid="cancel-delete-btn">Cancel</AlertDialogCancel>
            <AlertDialogAction
              data-testid="confirm-delete-btn"
              onClick={handleDelete}
              className="bg-destructive text-destructive-foreground hover:bg-destructive/90"
              disabled={deleting}
            >
              {deleting ? (
                <>
                  <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                  Deleting...
                </>
              ) : (
                'Delete'
              )}
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>

      {/* Settings Dialog */}
      <Dialog open={settingsOpen} onOpenChange={setSettingsOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>API Configuration</DialogTitle>
            <DialogDescription>
              Configure the URL of your SlideGenie API server. Make sure CORS is enabled.
            </DialogDescription>
          </DialogHeader>
         
          <div className="space-y-4 py-4">
            <div className="space-y-2">
              <Label htmlFor="api-url">API URL</Label>
              <Input
                id="api-url"
                data-testid="api-url-input"
                value={apiUrlInput}
                onChange={(e) => setApiUrlInput(e.target.value)}
                placeholder="http://localhost:8000 or https://your-ngrok-url.ngrok.io"
                
              />
              <p className="text-xs text-muted-foreground">
                Enter your SlideGenie API URL. Use ngrok if running locally.
              </p>
            </div>

            <div className="p-3 rounded-lg bg-secondary/50 text-sm space-y-2">
              <p className="font-medium">CORS Setup Required</p>
              <p className="text-muted-foreground text-xs">
                Your API must allow requests from: <code className="bg-background px-1 rounded">https://presentation-craft-5.preview.com</code>
              </p>
            </div>
          </div>

          <DialogFooter className="gap-2">
            <Button
              variant="outline"
              onClick={handleTestConnection}
              disabled={testingConnection}
              data-testid="test-connection-btn"
            >
              {testingConnection ? (
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
              ) : (
                <Check className="w-4 h-4 mr-2" />
              )}
              Test Connection
            </Button>
            <Button onClick={handleSaveApiUrl} data-testid="save-api-url-btn">
              Save
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}
