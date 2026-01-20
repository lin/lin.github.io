---
title: "Microblogs"
date: 2026-01-20
url: /micro
---

<style>
.archive-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    align-items: center;
    margin: 3rem auto;
    max-width: 800px;
    padding: 0 1rem;
}

.archive-card {
    display: grid;
    grid-template-columns: auto 1fr auto;
    align-items: center;
    gap: 0.5rem 1.5rem;
    background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
    border: 1px solid #e1e8ed;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    width: 100%;
    text-decoration: none !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
}

.archive-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 15px -3px rgba(0, 133, 255, 0.2), 0 4px 6px -2px rgba(0, 133, 255, 0.1);
    border-color: #0085ff;
}

.archive-icon {
    grid-row: 1 / 3;
    grid-column: 1;
    font-size: 3rem;
    margin-bottom: 0;
    margin-right: 0.5rem;
    color: #0085ff;
    display: flex;
    align-items: center;
    justify-content: center;
}

.archive-year {
    grid-column: 2;
    grid-row: 1;
    font-size: 1.5rem;
    font-weight: 800;
    color: #111;
    margin: 0;
    text-align: left;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.2;
}

.archive-link-text {
    grid-column: 2;
    grid-row: 2;
    font-size: 0.9rem;
    color: #666;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0;
    text-align: left;
}

.archive-details {
    grid-column: 3;
    grid-row: 1 / 3;
    font-size: 0.85rem;
    color: #888;
    margin: 0;
    text-align: right;
    line-height: 1.4;
    border-top: none;
    border-left: 1px solid rgba(0,0,0,0.1);
    padding-top: 0;
    padding-left: 1.5rem;
    width: auto;
    min-width: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Mobile Responsive */
@media (max-width: 600px) {
    .archive-card {
        display: flex;
        flex-direction: column;
        text-align: center;
        padding: 1.5rem;
        gap: 0.5rem;
    }
    .archive-icon { margin-right: 0; margin-bottom: 1rem; }
    .archive-year { text-align: center; margin-bottom: 0.25rem; }
    .archive-link-text { text-align: center; margin-bottom: 1rem; }
    .archive-details {
        border-left: none;
        border-top: 1px solid rgba(0,0,0,0.1);
        padding-left: 0;
        padding-top: 1rem;
        text-align: center;
        width: 100%;
        min-width: 0;
    }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    .archive-card {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        border-color: #4a5568;
    }
    .archive-year {
        color: #f7fafc;
    }
    .archive-link-text {
        color: #a0aec0;
    }
    .archive-details {
        color: #a0aec0;
        border-color: rgba(255,255,255,0.1);
    }
}
</style>

<div class="archive-container">
    <a href="/bsky2026/timeline/with_replies/1.html" class="archive-card">
        <div class="archive-icon"><svg fill="none" viewBox="0 0 64 57" width="50" style="width: 50px; height: 44.53px;"><path fill="#0F73FF" d="M13.873 3.805C21.21 9.332 29.103 20.537 32 26.55v15.882c0-.338-.13.044-.41.867-1.512 4.456-7.418 21.847-20.923 7.944-7.111-7.32-3.819-14.64 9.125-16.85-7.405 1.264-15.73-.825-18.014-9.015C1.12 23.022 0 8.51 0 6.55 0-3.268 8.579-.182 13.873 3.805ZM50.127 3.805C42.79 9.332 34.897 20.537 32 26.55v15.882c0-.338.13.044.41.867 1.512 4.456 7.418 21.847 20.923 7.944 7.111-7.32 3.819-14.64-9.125-16.85 7.405 1.264 15.73-.825 18.014-9.015C62.88 23.022 64 8.51 64 6.55c0-9.818-8.578-6.732-13.873-2.745Z"></path></svg></div>
        <span class="archive-year">2026</span>
        <span class="archive-link-text">Bluesky Archive</span>
        <div class="archive-details">
            Nov 22, 2025 - Jan 19, 2026<br>
            <strong>791 posts</strong>
        </div>
    </a>
    <a href="/bsky2025/timeline/with_replies/1.html" class="archive-card">
        <div class="archive-icon"><svg fill="none" viewBox="0 0 64 57" width="50" style="width: 50px; height: 44.53px;"><path fill="#0F73FF" d="M13.873 3.805C21.21 9.332 29.103 20.537 32 26.55v15.882c0-.338-.13.044-.41.867-1.512 4.456-7.418 21.847-20.923 7.944-7.111-7.32-3.819-14.64 9.125-16.85-7.405 1.264-15.73-.825-18.014-9.015C1.12 23.022 0 8.51 0 6.55 0-3.268 8.579-.182 13.873 3.805ZM50.127 3.805C42.79 9.332 34.897 20.537 32 26.55v15.882c0-.338.13.044.41.867 1.512 4.456 7.418 21.847 20.923 7.944 7.111-7.32 3.819-14.64-9.125-16.85 7.405 1.264 15.73-.825 18.014-9.015C62.88 23.022 64 8.51 64 6.55c0-9.818-8.578-6.732-13.873-2.745Z"></path></svg></div>
        <span class="archive-year">2025</span>
        <span class="archive-link-text">Bluesky Archive</span>
        <div class="archive-details">
            Nov 14, 2025 - Nov 22, 2025<br>
            <strong>4,479 posts</strong>
        </div>
    </a>
    <a href="/fanfou/index.html" class="archive-card">
        <div class="archive-icon">
            <svg width="50" height="50" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <rect width="100" height="100" rx="10" fill="#03CCFF"/>
                <text x="50" y="72" font-size="60" text-anchor="middle" fill="white" font-family="sans-serif" font-weight="bold">饭</text>
            </svg>
        </div>
        <span class="archive-year">2009</span>
        <span class="archive-link-text">Fanfou Archive</span>
        <div class="archive-details"> Feb 11, 2009 - Jul 05, 2009<br>
            <strong>129 posts</strong>
        </div>
    </a>
</div>
