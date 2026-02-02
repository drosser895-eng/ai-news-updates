#!/usr/bin/env python3
"""
AI News Updates Generator
Automatically generates content about the latest AI developments
"""

import os
import random
from datetime import datetime
from pathlib import Path

# AI topics and categories
AI_CATEGORIES = [
    "Machine Learning Breakthroughs",
    "AI Ethics & Governance", 
    "Generative AI Advances",
    "Robotics & Automation",
    "AI in Healthcare",
    "AI in Finance",
    "AI Research",
    "AI Hardware",
    "AI Policy & Regulation",
    "AI Startups & Funding"
]

def generate_ai_news_content():
    """Generate a sample AI news article"""
    titles = [
        "New Transformer Architecture Promises 40% Efficiency Gains",
        "Major AI Safety Initiative Launched by Leading Tech Companies",
        "Breakthrough in Multimodal AI Understanding Announced",
        "Regulatory Framework for AI Deployments Released",
        "Open Source AI Model Achieves State-of-the-Art Results",
        "AI Hardware Company Reports Record Performance",
        "Ethical Guidelines for Generative AI Applications Published",
        "AI Startup Secures $50M in Series A Funding",
        "New Research Paper Addresses AI Bias in Healthcare",
        "Industry Leaders Unveil New AI Safety Protocol"
    ]
    
    lead_paragraphs = [
        "In a significant development for the artificial intelligence community, researchers have announced a breakthrough that could reshape how we approach machine learning models.",
        "The announcement comes as part of a broader initiative to advance responsible AI development and deployment across multiple industries.",
        "This advancement represents a major milestone in the field of artificial intelligence, with potential applications spanning numerous sectors.",
        "The findings were published in a peer-reviewed paper and have already garnered significant attention from the research community.",
        "Industry experts are calling this development a game-changer for how organizations approach AI implementation."
    ]
    
    body_content = [
        "The technical details reveal significant improvements in computational efficiency while maintaining high performance standards.",
        "Early implementations have shown promising results across various benchmarks and real-world applications.",
        "The methodology introduces novel approaches to training and optimization that could influence future AI development.",
        "Researchers believe this advancement could accelerate the deployment of AI in previously challenging domains.",
        "The open-source nature of the research is expected to foster further innovation and collaboration in the field."
    ]
    
    conclusion = [
        "This development represents another step forward in the rapid evolution of artificial intelligence technologies.",
        "The implications for industry and society are still being assessed as the research community continues to explore applications.",
        "As the field continues to mature, such advances highlight the importance of continued investment in AI research.",
        "The pace of innovation in AI continues to accelerate, bringing both opportunities and challenges."
    ]
    
    title = random.choice(titles)
    lead = random.choice(lead_paragraphs)
    body = " ".join(random.sample(body_content, 3))
    concl = random.choice(conclusion)
    
    content = f"""<article class="ai-news-item">
    <h2>{title}</h2>
    <div class="date">{datetime.now().strftime('%Y-%m-%d')}</div>
    <p class="lead">{lead}</p>
    <p>{body}</p>
    <p>{concl}</p>
</article>
"""
    return title, content

def create_category_pages(output_dir):
    """Create category pages for different AI topics"""
    os.makedirs(os.path.join(output_dir, "category"), exist_ok=True)
    
    for category in AI_CATEGORIES:
        category_slug = category.lower().replace(" ", "-").replace("&", "and")
        category_path = os.path.join(output_dir, "category", f"{category_slug}.html")
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{category} - AI News Updates</title>
    <base href="/ai-news-updates/">
    <link rel="stylesheet" href="css/style.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-AINEWS123"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-AINEWS123');
    </script>
</head>
<body>
    <header>
        <div class="container">
            <h1>AI News Updates</h1>
            <p>Tracking the latest developments in Artificial Intelligence</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="./">Home</a></li>
                {"".join([f'<li><a href="category/{cat.lower().replace(" ", "-").replace("&", "and")}.html">{cat}</a></li>' for cat in AI_CATEGORIES[:5]])}
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h2>{category}</h2>
            <div class="posts-list">
                <!-- Generated AI news articles will appear here -->
            </div>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 AI News Updates. All rights reserved.</p>
            <p><a href="privacy-policy/">Privacy Policy</a> | <a href="terms/">Terms of Service</a></p>
        </div>
    </footer>
</body>
</html>"""
        
        with open(category_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

def generate_site():
    """Generate the complete AI news site"""
    output_dir = "_build"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "js"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)
    
    # Create CSS
    css_content = """/* AI News Updates - Clean Professional Design */
:root {
  --primary: #2563eb;
  --secondary: #1e40af;
  --accent: #0ea5e9;
  --background: #f8fafc;
  --surface: #ffffff;
  --text: #1e293b;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --radius: 8px;
  --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: var(--text);
  background-color: var(--background);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

header {
  background: var(--primary);
  color: white;
  padding: 1.5rem 0;
  box-shadow: var(--shadow);
}

header h1 {
  font-size: 2rem;
  margin: 0;
}

header p {
  margin: 0.25rem 0 0 0;
  opacity: 0.9;
}

nav {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 1rem 0;
}

nav ul {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  list-style: none;
}

nav a {
  color: var(--text);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: var(--radius);
  transition: background 0.2s;
}

nav a:hover {
  background: var(--background);
}

main {
  padding: 2rem 0;
}

.hero {
  text-align: center;
  margin-bottom: 2rem;
}

.hero h2 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

.latest-posts {
  margin-top: 2rem;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.ai-news-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
}

.ai-news-item h2 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: var(--primary);
}

.date {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.lead {
  font-weight: 500;
  margin-bottom: 0.75rem;
}

.post-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
}

.post-card h3 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.post-card .date {
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.category-tag {
  display: inline-block;
  background: rgba(37, 99, 235, 0.1);
  color: var(--primary);
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  margin-bottom: 0.75rem;
}

footer {
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: 2rem 0;
  margin-top: 3rem;
}

footer p {
  text-align: center;
  margin: 0.25rem 0;
}

footer a {
  color: var(--primary);
  text-decoration: none;
}

footer a:hover {
  text-decoration: underline;
}

/* Responsive design */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
  
  header h1 {
    font-size: 1.5rem;
  }
  
  nav ul {
    justify-content: left;
  }
  
  .post-grid {
    grid-template-columns: 1fr;
  }
}
"""
    
    # Process all HTML files to ensure proper base tag placement
    def add_base_tags_to_html_files():
        import os
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Ensure base tag is properly placed after other head elements but before relative links
                    if "<base href=" not in content:
                        # Insert base tag after meta tags but before CSS links
                        content = content.replace(
                            '</head>', 
                            '    <base href="/ai-news-updates/" />\n</head>', 
                            1
                        )
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
    
    with open(os.path.join(output_dir, "css", "style.css"), 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    # Create JavaScript
    js_content = """
// Simple analytics and interactive features
document.addEventListener('DOMContentLoaded', function() {
    // Track page views
    if (typeof gtag !== 'undefined') {
        gtag('event', 'page_view', {
            page_title: document.title,
            page_location: window.location.href
        });
    }
    
    // Add any interactive features here
});
"""
    
    with open(os.path.join(output_dir, "js", "main.js"), 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    # Create category pages
    create_category_pages(output_dir)
    
    # Generate index page with latest news
    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News Updates - Latest Developments in Artificial Intelligence</title>
    <meta name="description" content="Stay updated with the latest news, breakthroughs, and advancements in artificial intelligence.">
    <link rel="stylesheet" href="css/style.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-AINEWS123"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-AINEWS123');
    </script>
</head>
<body>
    <header>
        <div class="container">
            <h1>AI News Updates</h1>
            <p>Tracking the latest developments in Artificial Intelligence</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="./">Home</a></li>
                {"".join([f'<li><a href="category/{cat.lower().replace(" ", "-").replace("&", "and")}.html">{cat}</a></li>' for cat in AI_CATEGORIES[:7]])}
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <section class="hero">
                <h2>Latest AI Developments</h2>
                <p>Stay informed about the most important updates in artificial intelligence, machine learning, and related fields.</p>
            </section>
            
            <section class="latest-posts">
                <h2>Recent News</h2>
                <div class="post-grid">
                    {"".join([f'''
                    <div class="post-card">
                        <div class="category-tag">{random.choice(AI_CATEGORIES)}</div>
                        <h3><a href="posts/{title.lower().replace(" ", "-").replace(",", "").replace("!", "").replace("?", "")}/index.html">{title}</a></h3>
                        <div class="date">{datetime.now().strftime('%Y-%m-%d')}</div>
                        <p>{random.choice(["Breakthrough in AI research announced", "Major funding round for AI startup", "New ethical guidelines released", "Technical advancement reported"])}...</p>
                    </div>''' for title, _ in [generate_ai_news_content() for _ in range(6)]])}
                </div>
            </section>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 AI News Updates. All rights reserved.</p>
            <p><a href="privacy-policy/">Privacy Policy</a> | <a href="terms/">Terms of Service</a></p>
        </div>
    </footer>
    
    <script src="js/main.js"></script>
</body>
</html>"""
    
    with open(os.path.join(output_dir, "index.html"), 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    # Apply base tags to all HTML files after creation
    add_base_tags_to_html_files()
    
    # Create additional pages
    privacy_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - AI News Updates</title>
    <base href="/ai-news-updates/">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>AI News Updates</h1>
            <p>Tracking the latest developments in Artificial Intelligence</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="../">Home</a></li>
                <li><a href="../about/">About</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h2>Privacy Policy</h2>
            <p>We respect your privacy and are committed to protecting your personal data.</p>
            <!-- Privacy policy content would go here -->
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 AI News Updates. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    
    os.makedirs(os.path.join(output_dir, "privacy-policy"), exist_ok=True)
    with open(os.path.join(output_dir, "privacy-policy", "index.html"), 'w', encoding='utf-8') as f:
        f.write(privacy_content)
    
    # Create sitemap
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://drosser895-eng.github.io/ai-news-updates/</loc>
      <lastmod>2026-02-02</lastmod>
      <changefreq>daily</changefreq>
      <priority>1.0</priority>
   </url>
   <url>
      <loc>https://drosser895-eng.github.io/ai-news-updates/category/machine-learning-breakthroughs.html</loc>
      <lastmod>2026-02-02</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
   </url>
   <url>
      <loc>https://drosser895-eng.github.io/ai-news-updates/category/ai-ethics-&amp;-governance.html</loc>
      <lastmod>2026-02-02</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
   </url>
</urlset>"""
    
    with open(os.path.join(output_dir, "sitemap.xml"), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    # Create robots.txt
    robots_content = """User-agent: *
Allow: /
Sitemap: https://drosser895-eng.github.io/ai-news-updates/sitemap.xml"""
    
    with open(os.path.join(output_dir, "robots.txt"), 'w', encoding='utf-8') as f:
        f.write(robots_content)
    
    print("AI News Updates site generated successfully!")
    print(f"Files created in {output_dir}/ directory")

if __name__ == "__main__":
    generate_site()