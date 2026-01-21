---
title: "Microblogs"
date: 2026-01-20
url: /micro
---

> 1. 我一直在成长，曾经的稚嫩作为一种真实记录，便留了下来
> 2. 我担心冒犯一些需要更多交流才能理解的读者，也便因此删去了很多

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
    <a href="/twitter/?year=2024" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2024</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Jun 25, 2024 - Nov 5, 2024<br>
            <strong>165 Tweets</strong>
        </div>
    </a>
    <a href="/twitter/?year=2023" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2023</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Jun 25, 2023 - Nov 5, 2023<br>
            <strong>157 Tweets</strong>
        </div>
    </a>
    <a href="/twitter/?year=2022" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2022</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Dec 20, 2022 - Dec 24, 2022<br>
            <strong>6 tweets.</strong>
        </div>
    </a>
    <a href="/twitter/?year=2021" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2021</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Sep 7, 2021 - Dec 30, 2021<br>
            <strong>11 Tweets</strong>
        </div>
    </a>
    <a href="/twitter/?year=2020" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2020</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Jan 2, 2020 - May 10, 2020<br>
            <strong>33 Tweets</strong>
        </div>
    </a>
    <a href="/twitter/?year=2019" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2019</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Apr 1, 2019 - Dec 31, 2019<br>
            <strong>104 Tweets</strong>
        </div>
    </a>
    <a href="/twitter/?year=2018" class="archive-card">
        <div class="archive-icon">
            <svg viewBox="0 0 24 24" width="50" height="50" fill="#1DA1F2"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>
        </div>
        <span class="archive-year">2018</span>
        <span class="archive-link-text">Twitter Archive</span>
        <div class="archive-details">
            Jan 5, 2018 - Dec 17, 2018<br>
            <strong>230 Tweets</strong>
        </div>
    </a>
    <a href="/weibo-albertkui.html" class="archive-card">
        <div class="archive-icon">
            <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 415" fill-rule="evenodd" clip-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2"><g transform="scale(1.45729)"><clipPath id="prefix__a"><path d="M0 0h351.336v284.628H0z"/></clipPath><g clip-path="url(#prefix__a)" fill-rule="nonzero"><path d="M25.84 195.715c0 40.917 53.28 74.078 118.97 74.078 65.691 0 118.971-33.161 118.971-74.078 0-40.918-53.28-74.078-118.971-74.078-65.69 0-118.97 33.16-118.97 74.078" fill="#fff"/><path d="M147.622 263.781c-58.176 5.769-108.401-20.556-112.183-58.71-3.781-38.202 40.336-73.786 98.463-79.556 58.177-5.769 108.402 20.556 112.135 58.71 3.83 38.202-40.287 73.835-98.415 79.556m116.304-126.776c-4.945-1.503-8.338-2.472-5.769-8.969 5.624-14.107 6.206-26.276.097-35.002-11.393-16.29-42.614-15.417-78.392-.437 0 0-11.248 4.897-8.339-3.975 5.478-17.695 4.654-32.482-3.878-41.063-19.392-19.44-71.024.727-115.286 44.99C19.247 125.661 0 160.809 0 191.206c0 58.079 74.514 93.422 147.38 93.422 95.555 0 159.112-55.51 159.112-99.579.049-26.664-22.398-41.79-42.566-48.044" fill="#e6162d"/><path d="M327.387 30.688C304.311 5.09 270.277-4.654 238.862 2.036c-7.272 1.552-11.877 8.727-10.326 15.95 1.551 7.272 8.678 11.878 15.95 10.326 22.349-4.751 46.541 2.182 62.927 20.362 16.387 18.18 20.847 42.954 13.817 64.673-2.278 7.078 1.6 14.641 8.678 16.919 7.078 2.279 14.641-1.599 16.92-8.629v-.049c9.89-30.494 3.636-65.351-19.441-90.9" fill="#f93"/><path d="M291.948 62.685c-11.247-12.459-27.828-17.211-43.099-13.914-6.254 1.309-10.229 7.515-8.92 13.769 1.357 6.253 7.514 10.229 13.72 8.871 7.466-1.599 15.61.728 21.089 6.788a22.126 22.126 0 014.605 21.67c-1.939 6.06 1.358 12.605 7.466 14.593 6.109 1.939 12.605-1.358 14.593-7.466 4.799-14.884 1.793-31.852-9.454-44.311" fill="#f93"/><path d="M150.822 194.648c-2.036 3.491-6.545 5.139-10.035 3.685-3.491-1.406-4.558-5.333-2.57-8.727 2.036-3.393 6.351-5.042 9.793-3.684 3.491 1.26 4.751 5.187 2.812 8.726m-18.568 23.756c-5.624 8.968-17.695 12.895-26.761 8.774-8.92-4.072-11.587-14.495-5.963-23.27 5.575-8.727 17.21-12.605 26.228-8.823 9.114 3.926 12.023 14.253 6.496 23.319m21.138-63.51c-27.683-7.223-58.952 6.594-70.976 30.979-12.265 24.871-.387 52.504 27.537 61.522 28.991 9.356 63.121-4.994 74.999-31.803 11.732-26.277-2.909-53.28-31.56-60.698"/></g></g></svg>
        </div>
        <span class="archive-year">2011</span>
        <span class="archive-link-text">Weibo Archive</span>
        <div class="archive-details">
            2011 - 2025<br>
            <strong>Weibo Posts</strong>
        </div>
    </a>
    <a href="/fanfou/?page=1" class="archive-card">
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
