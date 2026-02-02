
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
