import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_TIMELINE_DIR = (
    Path(__file__).resolve().parents[1] / "static" / "bsky2026" / "timeline" / "posts"
)
DEFAULT_ARCHIVE_DIR = DEFAULT_TIMELINE_DIR.parents[1]
DEFAULT_CSV_PATH = DEFAULT_ARCHIVE_DIR / "timeline-post-counts-by-day.csv"
DEFAULT_STATS_PATH = DEFAULT_ARCHIVE_DIR / "stats.html"


class FeedPostDateParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.feed_post_dates = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return

        attributes = dict(attrs)
        classes = attributes.get("class", "").split()
        aria_label = attributes.get("aria-label")

        if "FeedPost__date" not in classes or not aria_label:
            return

        date_text = aria_label.split(" at ", 1)[0].strip()
        parsed_date = datetime.strptime(date_text, "%B %d, %Y").date()
        self.feed_post_dates.append(parsed_date.isoformat())


def iter_html_files(folder: Path):
    return sorted(path for path in folder.iterdir() if path.suffix == ".html" and path.is_file())


def count_posts_by_day(folder: Path):
    counter = Counter()
    html_files = iter_html_files(folder)

    for html_file in html_files:
        parser = FeedPostDateParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        counter.update(parser.feed_post_dates)

    return counter, html_files


def build_rows(counts, year=None):
    return [
        {"date": day, "count": count}
        for day, count in sorted(counts.items())
        if year is None or day.startswith(f"{year}-")
    ]


def parse_target(value):
    if value is None:
        return DEFAULT_TIMELINE_DIR, None

    if value.isdigit() and len(value) == 4:
        return DEFAULT_TIMELINE_DIR, int(value)

    return Path(value).expanduser().resolve(), None


def resolve_output_path(output_value, default_path: Path, year, suffix):
    if output_value:
        return Path(output_value).expanduser().resolve()

    if year is None:
        return default_path

    return default_path.with_name(f"{default_path.stem}-{year}{suffix}")


def write_csv(rows, output_path: Path):
    output_path.write_text("", encoding="utf-8")
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["date", "count"])
        writer.writeheader()
        writer.writerows(rows)


def render_stats_html(rows, csv_path: Path, year=None):
    data_json = json.dumps(rows, ensure_ascii=False)
    max_count = max((row["count"] for row in rows), default=0)
    total_posts = sum(row["count"] for row in rows)
    date_range = (
        f"{rows[0]['date']} → {rows[-1]['date']}"
        if rows
        else "No timeline post data found"
    )
    csv_href = csv_path.name
    title_suffix = f" ({year})" if year is not None else ""
    subtitle = (
        f"Daily counts of root timeline posts extracted from the timeline HTML pages for {year}. "
        "Use this page to see how posting frequency changes over time."
        if year is not None
        else "Daily counts of root timeline posts extracted from the timeline HTML pages. Use this page to see how posting frequency changes over time."
    )

    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>@fastcalm.bsky.social timeline stats{title_suffix}</title>
  <link rel="stylesheet" href="assets/style.css">
  <style>
    body {{
      background: #0f172a;
      color: #e2e8f0;
    }}
    .StatsPage {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 24px 16px 64px;
    }}
    .StatsHero {{
      display: grid;
      gap: 16px;
      margin-top: 24px;
    }}
    .StatsTitle {{
      font-size: 2rem;
      font-weight: 700;
      line-height: 1.1;
    }}
    .StatsSubtitle {{
      color: #cbd5e1;
      max-width: 70ch;
    }}
    .StatsGrid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }}
    .StatsCard, .ChartCard, .TableCard {{
      background: rgba(15, 23, 42, 0.72);
      border: 1px solid rgba(148, 163, 184, 0.25);
      border-radius: 16px;
      box-shadow: 0 12px 30px rgba(15, 23, 42, 0.25);
    }}
    .StatsCard {{
      padding: 18px 20px;
    }}
    .StatsLabel {{
      color: #94a3b8;
      font-size: 0.95rem;
      margin-bottom: 8px;
    }}
    .StatsValue {{
      font-size: 1.8rem;
      font-weight: 700;
    }}
    .ChartCard, .TableCard {{
      padding: 20px;
      margin-top: 20px;
    }}
    .SectionTitle {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 16px;
    }}
    .ChartWrap {{
      width: 100%;
      overflow-x: auto;
    }}
    #chart {{
      width: 100%;
      min-height: 360px;
      display: block;
    }}
    .AxisText {{
      fill: #94a3b8;
      font-size: 12px;
    }}
    .GridLine {{
      stroke: rgba(148, 163, 184, 0.16);
      stroke-width: 1;
    }}
    .TrendLine {{
      fill: none;
      stroke: #38bdf8;
      stroke-width: 3;
      stroke-linecap: round;
      stroke-linejoin: round;
    }}
    .Point {{
      fill: #f8fafc;
      stroke: #38bdf8;
      stroke-width: 2;
    }}
    .Point--weekday {{
      fill: #f59e0b;
      stroke: #fbbf24;
    }}
    .ChartLegend {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      margin: 0 0 12px;
      color: #cbd5e1;
      font-size: 0.92rem;
    }}
    .LegendItem {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .LegendDot {{
      width: 10px;
      height: 10px;
      border-radius: 999px;
      background: #f8fafc;
      border: 2px solid #38bdf8;
    }}
    .LegendDot--weekday {{
      background: #f59e0b;
      border-color: #fbbf24;
    }}
    .Tooltip {{
      position: fixed;
      pointer-events: none;
      background: rgba(15, 23, 42, 0.96);
      color: #f8fafc;
      border: 1px solid rgba(148, 163, 184, 0.35);
      border-radius: 10px;
      padding: 8px 10px;
      font-size: 0.9rem;
      transform: translate(12px, 12px);
      opacity: 0;
      transition: opacity 120ms ease;
      z-index: 10;
      white-space: nowrap;
    }}
    .LinkRow {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 8px;
    }}
    .StatsLink {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 10px 14px;
      border-radius: 999px;
      background: #2563eb;
      color: #eff6ff;
      font-weight: 600;
    }}
    .StatsLink--secondary {{
      background: rgba(148, 163, 184, 0.16);
      color: #e2e8f0;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
    }}
    th, td {{
      text-align: left;
      padding: 10px 12px;
      border-bottom: 1px solid rgba(148, 163, 184, 0.12);
    }}
    th {{
      color: #94a3b8;
      font-weight: 600;
    }}
    tbody tr:hover {{
      background: rgba(148, 163, 184, 0.06);
    }}
    @media (max-width: 640px) {{
      .StatsTitle {{
        font-size: 1.6rem;
      }}
      .ChartCard, .TableCard, .StatsCard {{
        padding: 16px;
      }}
    }}
  </style>
</head>
<body>
  <div class="Root">
    <div class="Page StatsPage">
      <div class="PageHeader">
        <a href="index.html" class="Link">Home</a>
        <a href="timeline/posts/1.html" class="Link">Timeline</a>
        <a href="search.html" class="Link">Search</a>
        <a href="stats.html" class="Link">Stats</a>
      </div>
      <div class="StatsHero">
        <h1 class="StatsTitle">@fastcalm.bsky.social timeline stats{title_suffix}</h1>
        <p class="StatsSubtitle">{subtitle}</p>
        <div class="LinkRow">
          <a href="{csv_href}" class="StatsLink">Download CSV</a>
          <a href="timeline/posts/1.html" class="StatsLink StatsLink--secondary">Back to timeline</a>
        </div>
      </div>
      <div class="StatsGrid">
        <div class="StatsCard">
          <div class="StatsLabel">Days with posts</div>
          <div class="StatsValue">{len(rows)}</div>
        </div>
        <div class="StatsCard">
          <div class="StatsLabel">Total posts</div>
          <div class="StatsValue">{total_posts}</div>
        </div>
        <div class="StatsCard">
          <div class="StatsLabel">Peak daily posts</div>
          <div class="StatsValue">{max_count}</div>
        </div>
        <div class="StatsCard">
          <div class="StatsLabel">Date range</div>
          <div class="StatsValue" style="font-size: 1rem;">{date_range}</div>
        </div>
      </div>
      <div class="ChartCard">
        <div class="SectionTitle">Posts per day</div>
        <div class="ChartLegend">
          <span class="LegendItem"><span class="LegendDot LegendDot--weekday"></span>Weekday</span>
          <span class="LegendItem"><span class="LegendDot"></span>Weekend</span>
        </div>
        <div class="ChartWrap">
          <svg id="chart" viewBox="0 0 1100 420" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Timeline posts per day chart"></svg>
        </div>
      </div>
      <div class="TableCard">
        <div class="SectionTitle">Daily counts</div>
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Posts</th>
            </tr>
          </thead>
          <tbody id="stats-table-body"></tbody>
        </table>
      </div>
    </div>
  </div>
  <div id="tooltip" class="Tooltip"></div>
  <script>
    const data = {data_json};
    const svg = document.getElementById("chart");
    const tableBody = document.getElementById("stats-table-body");
    const tooltip = document.getElementById("tooltip");
    const width = 1100;
    const height = 420;
    const margin = {{ top: 24, right: 24, bottom: 56, left: 56 }};
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;
    const maxCount = Math.max(...data.map((item) => item.count), 1);
    const xStep = data.length > 1 ? innerWidth / (data.length - 1) : innerWidth / 2;

    const yScale = (value) => margin.top + innerHeight - (value / maxCount) * innerHeight;
    const xScale = (index) => margin.left + (data.length > 1 ? index * xStep : innerWidth / 2);

    const yTicks = new Set([0, Math.ceil(maxCount / 4), Math.ceil(maxCount / 2), Math.ceil(maxCount * 3 / 4), maxCount]);
    const tickValues = [...yTicks].sort((a, b) => a - b);
    const isWeekday = (dateString) => {{
      const day = new Date(`${{dateString}}T00:00:00`).getDay();
      return day >= 1 && day <= 5;
    }};

    const linePath = data
      .map((item, index) => `${{ index === 0 ? "M" : "L" }} ${{xScale(index).toFixed(2)}} ${{yScale(item.count).toFixed(2)}}`)
      .join(" ");

    const labelInterval = Math.max(Math.floor(data.length / 6), 1);
    const xLabelIndexes = data
      .map((_, index) => index)
      .filter((index) => index === 0 || (index !== data.length - 1 && index % labelInterval === 0));

    svg.innerHTML = `
      ${{tickValues.map((tick) => `
        <g>
          <line class="GridLine" x1="${{margin.left}}" y1="${{yScale(tick)}}" x2="${{width - margin.right}}" y2="${{yScale(tick)}}"></line>
          <text class="AxisText" x="${{margin.left - 12}}" y="${{yScale(tick) + 4}}" text-anchor="end">${{tick}}</text>
        </g>
      `).join("")}}
      <line class="GridLine" x1="${{margin.left}}" y1="${{margin.top + innerHeight}}" x2="${{width - margin.right}}" y2="${{margin.top + innerHeight}}"></line>
      <path class="TrendLine" d="${{linePath}}"></path>
      ${{data.map((item, index) => `
        <circle
          class="Point${{isWeekday(item.date) ? " Point--weekday" : ""}}"
          cx="${{xScale(index)}}"
          cy="${{yScale(item.count)}}"
          r="4"
          data-date="${{item.date}}"
          data-count="${{item.count}}"
        ></circle>
      `).join("")}}
      ${{xLabelIndexes.map((originalIndex) => {{
        const item = data[originalIndex];
        return `
          <text class="AxisText" x="${{xScale(originalIndex)}}" y="${{height - 18}}" text-anchor="${{originalIndex === 0 ? "start" : "middle"}}">${{item.date}}</text>
        `;
      }}).join("")}}
    `;

    data.forEach((item) => {{
      const row = document.createElement("tr");
      row.innerHTML = `<td>${{item.date}}</td><td>${{item.count}}</td>`;
      tableBody.appendChild(row);
    }});

    svg.querySelectorAll(".Point").forEach((point) => {{
      point.addEventListener("mouseenter", () => {{
        tooltip.style.opacity = "1";
        tooltip.textContent = `${{point.dataset.date}}: ${{point.dataset.count}} posts`;
      }});
      point.addEventListener("mousemove", (event) => {{
        tooltip.style.left = `${{event.clientX}}px`;
        tooltip.style.top = `${{event.clientY}}px`;
      }});
      point.addEventListener("mouseleave", () => {{
        tooltip.style.opacity = "0";
      }});
    }});
  </script>
</body>
</html>
"""


def write_stats_html(rows, output_path: Path, csv_path: Path, year=None):
    output_path.write_text(render_stats_html(rows, csv_path, year=year), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target",
        nargs="?",
        help="Optional folder path or a 4-digit year like 2026",
    )
    parser.add_argument(
        "--year",
        type=int,
        help="Filter results to a specific year",
    )
    parser.add_argument(
        "--csv-output",
        help="Output CSV path",
    )
    parser.add_argument(
        "--stats-output",
        help="Output HTML stats page path",
    )
    args = parser.parse_args()

    folder, target_year = parse_target(args.target)
    year = args.year if args.year is not None else target_year
    if not folder.is_dir():
        raise SystemExit(f"Folder not found: {folder}")

    counts, html_files = count_posts_by_day(folder)
    rows = build_rows(counts, year=year)
    csv_output = resolve_output_path(args.csv_output, DEFAULT_CSV_PATH, year, ".csv")
    stats_output = resolve_output_path(args.stats_output, DEFAULT_STATS_PATH, year, ".html")
    csv_output.parent.mkdir(parents=True, exist_ok=True)
    stats_output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows, csv_output)
    write_stats_html(rows, stats_output, csv_output, year=year)

    print(f"HTML files processed: {len(html_files)}")
    if year is not None:
        print(f"Year filter: {year}")
    print(f"Total posts found: {sum(row['count'] for row in rows)}")
    print(f"CSV written to: {csv_output}")
    print(f"Stats page written to: {stats_output}")

    for row in rows:
        print(f"{row['date']}: {row['count']}")


if __name__ == "__main__":
    main()
