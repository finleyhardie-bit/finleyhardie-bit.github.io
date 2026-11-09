"""Builds the static portfolio site. Run: python3 build.py"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
GH = "https://github.com/finleyhardie-bit"
LINKEDIN = "https://www.linkedin.com/in/finleyhardie"
EMAIL = "finleyhardie@gmail.com"

PAGES = [
    ("index.html", "Home"),
    ("projects.html", "Projects"),
    ("experience.html", "Experience"),
    ("skills.html", "Skills"),
    ("education.html", "Education"),
    ("beyond.html", "Beyond work"),
]


def shell(fname, title, desc, body):
    nav = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{label}</a>'
        for f, label in PAGES
    )
    full_title = "Finley Hardie | Business Analytics" if fname == "index.html" else f"{title} | Finley Hardie"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://finleyhardie-bit.github.io/">
<meta property="og:image" content="https://finleyhardie-bit.github.io/img/social-preview.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Public+Sans:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23172A3A'/%3E%3Ctext x='32' y='43' font-family='Arial' font-weight='700' font-size='30' text-anchor='middle' fill='%23fff'%3EFH%3C/text%3E%3C/svg%3E">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
<a class="brand" href="index.html">Finley Hardie</a>
<nav class="nav" aria-label="Main">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="wrap">
<div><h2>Let's talk</h2><p>Denver, CO and New Orleans, LA. English and French.</p></div>
<ul>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><a href="{LINKEDIN}">LinkedIn</a></li>
<li><a href="{GH}">GitHub</a></li>
</ul>
</div></footer>
</body>
</html>
"""


def fig(src, alt, cap):
    return f'<figure><img src="img/{src}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>'


# ---------------------------------------------------------------- HOME
home = f"""
<section class="hero"><div class="wrap">
<div>
<h1 class="statement">I turn messy data from many sources into numbers people can trust and act on.</h1>
<p class="intro">I'm a Business Analytics student at the University of Denver's Daniels College of Business, minoring in French. I work in asset management for an affordable-housing developer, where I build budgets, dashboards and portfolio trackers for LIHTC properties. I grew up across Europe and I'm a native French speaker.</p>
<div class="seeking"><strong>What's next</strong>I graduate in May 2027 and join Smith &amp; Henzy full time that July. I'm always happy to connect with people working in analytics, real estate finance and affordable housing.</div>
<div class="cta">
<a class="btn primary" href="projects.html">See my projects</a>
<a class="btn" href="mailto:{EMAIL}">Email me</a>
<a class="btn" href="{LINKEDIN}">LinkedIn</a>
</div>
</div>
<div class="portrait"><img src="img/finley-hardie.jpg" alt="Portrait of Finley Hardie" width="540" height="725"></div>
</div></section>

<section class="places" aria-labelledby="places-h"><div class="wrap">
<h2 id="places-h">Places I've called home</h2>
<ul><li>New Orleans</li><li>Denver</li><li>France</li><li>Austria</li><li>Malta</li><li>Finland</li></ul>
</div></section>

<section class="section"><div class="wrap">
<div class="highlights">
<div><h3>Real portfolio work</h3><p>At Smith &amp; Henzy I turned financials from about 9 property-manager formats into one budget-vs-actual dashboard covering 21 affordable-housing properties. <a href="experience.html">Read more</a></p></div>
<div><h3>End to end on data</h3><p>I've designed a normalized SQL Server database, built a C# desktop app with reports on top of it, and compared four machine-learning models in R. <a href="skills.html">See my skills</a></p></div>
<div><h3>Leader and bilingual</h3><p>I'm Executive Chair of New Member Education for a 120+ member chapter, a certified soccer referee, and fluent in French. <a href="beyond.html">Beyond work</a></p></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Selected work</h2><a href="projects.html">All projects</a></div>
<div class="tiles">
<a class="tile" href="projects.html#loan-default">
<img src="img/loan-rf-importance.jpg" alt="Variable importance chart from a random forest model" loading="lazy">
<div class="body"><h3>Predicting loan default risk</h3><p>Compared four classifiers on 3,357 loan applications and showed why the most accurate-looking model was the wrong one to deploy.</p><p class="tools">R, tidymodels, Quarto</p></div></a>
<a class="tile" href="projects.html#premierstats">
<img src="img/premierstats-report.jpg" alt="PremierStats desktop app showing a player stats report" loading="lazy">
<div class="body"><h3>PremierStats database and app</h3><p>An 8-table SQL Server database of Premier League stats, with a C# desktop app for searching, editing and reporting.</p><p class="tools">SQL Server, T-SQL, C#</p></div></a>
<a class="tile" href="projects.html#ecommerce">
<img src="img/ecom-customer-clusters.jpg" alt="Scatter plot of customer clusters by recency and spend" loading="lazy">
<div class="body"><h3>E-commerce analytics</h3><p>Segmented 1,000+ customers with k-means and modeled monthly revenue to find the store's peak and slow seasons.</p><p class="tools">R, ggplot2, k-means</p></div></a>
</div>
</div></section>
"""

# ---------------------------------------------------------------- PROJECTS
def case(id_, title, meta, tags, problem, role, challenges, artifacts, impact, figs_html, links):
    tag_html = "".join(f"<li>{t}</li>" for t in tags)
    links_html = "".join(f'<a href="{u}">{t}</a>' for t, u in links)
    return f"""
<article class="case" id="{id_}"><div class="wrap">
<header class="case-head"><h2>{title}</h2><p class="meta">{meta}</p><ul class="tags">{tag_html}</ul></header>
<div class="case-grid">
<dl>
<dt>The business problem</dt><dd>{problem}</dd>
<dt>What I did</dt><dd>{role}</dd>
<dt>Challenges</dt><dd>{challenges}</dd>
<dt>What I built</dt><dd>{artifacts}</dd>
<dt>Business value</dt><dd>{impact}</dd>
</dl>
<div>{figs_html}<div class="links">{links_html}</div></div>
</div>
</div></article>"""


projects_list = [
    ("loan-default", "Loan default risk"),
    ("ecommerce", "E-commerce analytics"),
    ("premierstats", "PremierStats database and app"),
    ("variance", "Variance analysis"),
    ("crocs", "Crocs 10-K analysis"),
    ("nba", "NBA player performance"),
    ("time-series", "Teaching time series"),
]
idx = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in projects_list)

projects = f"""
<section class="page-intro"><div class="wrap">
<h1>Projects</h1>
<p class="lede">Coursework and professional projects, newest first. Each one covers the business problem, my part in it, what got in the way, and what it was worth. My work at Smith &amp; Henzy is on the <a href="experience.html">Experience</a> page.</p>
<ul class="project-index">{idx}</ul>
</div></section>
""" + case(
    "loan-default",
    "Predicting loan default risk",
    "INFO 3200, Spring 2026. Individual case study for a fictional lender, Rocky Mountain Lending Co.",
    ["R", "tidymodels", "Logistic regression", "Decision trees", "Random forest", "Quarto"],
    "A lender wants to approve good borrowers and catch risky ones before they default. About 27.5% of the 3,357 complete applications were bad risks, so a model that simply approves everyone is already 72.5% accurate. Any real model has to beat that.",
    "<ul><li>Explored income, prior defaults and debt-to-income ratio against risk.</li><li>Trained a baseline, a decision tree, logistic regression and two random forests on an 80/20 split, then compared accuracy, sensitivity and specificity.</li><li>Ran a second set of regression models to predict loan size.</li><li>Wrote underwriting recommendations and dug into the applicants the best model got wrong.</li></ul>",
    "The random forests looked best on training data (96%+ accuracy) but fell to about 73% on new data, a textbook case of overfitting. Every model still missed about 70% of bad-risk applicants, so I had to argue that accuracy alone was the wrong yardstick.",
    "A full Quarto report with code, charts, summary tables and variable-importance plots from two models.",
    "Logistic regression generalized best (<span class=\"result\">74.3% test accuracy</span>, with only a 1.7-point train/test gap). Prior default history was the strongest signal across every model, which became my first recommendation: treat a prior default as a near-disqualifying flag and add income tiers and a debt-to-income cap to underwriting.",
    '<div class="figs">' + fig("loan-rf-importance.jpg", "Bar chart of variable importance in the random forest, led by prior default", "Prior default and income lead the random forest's variable importance.") + fig("loan-prior-default.jpg", "Stacked bar chart showing much higher bad-risk share for applicants with a prior default", "Applicants with a prior default are far more likely to be bad risks.") + "</div>",
    [("Read the full report", "reports/loan-default-risk.html"), ("View the code", f"{GH}/r-data-visualization/tree/main/case-study-2-loan-default")],
) + case(
    "ecommerce",
    "E-commerce analytics: from data to decisions",
    "INFO 3200, Spring 2026. Individual case study on a fictional online retailer.",
    ["R", "dplyr", "ggplot2", "k-means clustering", "Linear regression", "Quarto dashboard"],
    "An online store selling across ten categories had three years of transactions (2022 to 2024) and 1,000+ customers, but no clear view of which products, channels and customers made it money, or when sales peak.",
    "<ul><li>Joined the transaction, customer and product tables and charted revenue by category, by month and by marketing channel.</li><li>Grouped customers with k-means on recency, frequency and spend, using an elbow plot to choose the number of clusters.</li><li>Fit a trend-plus-season regression on monthly revenue.</li><li>Built a Quarto dashboard to summarize it all.</li></ul>",
    "The product and transaction tables shared column names (category and cost), so a naive join would have duplicated columns. I chose the join keys and columns on purpose. Picking k for clustering was a judgment call that I backed with the elbow plot.",
    "An analysis report with code and charts, plus a one-page Quarto dashboard.",
    "Electronics drove about $1.3M, the most of any category. The model put July <span class=\"result\">about $44.9K above</span> January and February about $34.3K below it, which helps plan inventory and promotions around the season. The top customer cluster (about 8 orders and $11K spend each) is the group to protect with loyalty offers.",
    '<div class="figs">' + fig("ecom-customer-clusters.jpg", "Scatter plot of three customer clusters by recency and total spend", "Three customer segments from k-means clustering.") + '<div class="figs two">' + fig("ecom-revenue-by-category.jpg", "Bar chart of total revenue by product category", "Revenue by category.") + fig("ecom-forecast-fit.jpg", "Line chart comparing actual and fitted monthly revenue", "Actual vs. fitted monthly revenue.") + "</div></div>",
    [("Read the report", "reports/ecommerce-analytics.html"), ("View the code", f"{GH}/r-data-visualization/tree/main/case-study-1-ecommerce")],
) + case(
    "premierstats",
    "PremierStats: a Premier League database and desktop app",
    "INFO 3140 (Winter 2026), rebuilt and extended in INFO 3240 (Spring 2026). Individual project for a fictional sports analytics firm.",
    ["SQL Server", "T-SQL", "C# / WinForms", "RDLC reports", "ER modeling", "3NF"],
    "Scouts, coaches and analysts need to compare players across all 20 clubs, but the stats that matter differ by position: save percentage only makes sense for goalkeepers, take-ons for wingers. They need one trusted source they can search and report from without writing SQL.",
    "<ul><li>First version (INFO 3140): designed a 6-table schema in SQLite (one team table plus five position tables), proved third normal form and wrote analytical queries.</li><li>Second version (INFO 3240): rebuilt it in SQL Server as 8 tables, adding referees and matches, with primary and foreign keys and CHECK constraints for the business rules.</li><li>Added a view of top performers, a player-rating function and a stored procedure for adding players.</li><li>Built a C# desktop app with 7 screens (player grid, search, team roster, players by position, a striker add/edit/delete form) and 2 printable reports.</li></ul>",
    "Keeping one player from appearing in two position tables, and keeping stats in valid ranges (0 to 38 appearances, unique league positions), meant enforcing the rules in the database, not only in the app. Wiring report filters to the database through a reusable helper class took several iterations.",
    "Build scripts, an ER diagram, the C# app source and a recorded demo.",
    "A non-technical user can look up any player, filter by team or position and print a report. Every number on screen comes from one constrained database, so the reports always agree with each other. The project shows the whole path from a data model to a tool someone can use.",
    '<div class="figs">' + fig("premierstats-report.jpg", "PremierStats Player Stats Report window listing players, goals and assists", "The Player Stats Report, filterable by team.") + '<div class="figs two">' + fig("premierstats-striker-detail.jpg", "Striker Detail form with add, save and delete buttons", "Add, edit and delete form with a calculated player rating.") + fig("premierstats-erd.jpg", "Entity relationship diagram of the PremierStats database", "The 8-table SQL Server design.") + "</div></div>",
    [("View the SQL and C# code", f"{GH}/sql-databases/tree/main/premierstats")],
) + case(
    "variance",
    "Variance analysis for a furniture maker",
    "Managerial Accounting, Spring 2026. Team project: a board presentation for a fictional company, PineCraft Furniture Co.",
    ["Excel", "Flexible budgets", "Variance analysis", "Executive presentation"],
    "PineCraft planned to sell 950 custom oak tables but made and sold 1,000. Comparing actual costs to the original plan mixed up two different effects: selling more units, and paying more or less per unit. The board needed to know which one was really driving results.",
    "<ul><li>I built the Excel model: I rebuilt the budget at the actual volume using standard costs (a flexible budget) and calculated all 8 variances</li><li>Our team explained each one to the board in plain terms, with a plan for how management should respond.</li></ul>",
    "Favorable and unfavorable effects cancelled each other out at the top line. The extra volume hid a $50K price cut and higher labor costs, so we had to make the offsetting effects visible.",
    "An Excel variance model and a board-ready slide deck.",
    "The board could see the real story: volume and lower overhead spending helped, while the price cut and labor overruns hurt. That tells management which levers to pull. It's the same budget-vs-actual thinking I now use on affordable-housing properties.",
    fig("pinecraft-variances.jpg", "Horizontal bar chart of eight variances, favorable in green and unfavorable in red", "The 8 variances from our analysis, charted for this page."),
    [("View the model and slides", f"{GH}/excel-financial-analysis/tree/main/pinecraft-variance-analysis")],
) + case(
    "crocs",
    "Crocs 10-K comparative analysis",
    "ACTG 2200 Introduction to Financial Reporting, Winter 2026. Individual project.",
    ["Financial statements", "Ratio analysis", "Excel", "SEC filings"],
    "Investors and analysts read a 10-K to judge whether a company is getting healthier or weaker. The assignment was to read Crocs' FY2023 and FY2024 filings and explain how the business changed.",
    "Walked through every 10-K section, then calculated year-over-year trends, margins, liquidity and profitability ratios, and earnings per share from the reported statements.",
    "Translating dense filings into a few numbers that tell a clear story, and explaining what drove each change rather than just reporting it.",
    "A written analysis with supporting ratio calculations.",
    "Showed a sharp jump in reported EPS, from <span class=\"result\">$8.82 to $16.00</span>, and explained the margin trends behind it. This is the same skill I use to read property financial statements at work.",
    "",
    [("Read the analysis", f"{GH}/excel-financial-analysis/blob/main/crocs-10k-analysis/crocs-10k-analysis.pdf")],
) + case(
    "nba",
    "NBA player performance analysis",
    "INFO 3100 Automating Business Processes with Python, Winter 2026. Individual project.",
    ["Python", "pandas", "Jupyter", "Correlation", "Group comparisons"],
    "Teams and fantasy players want to know what actually drives scoring. Using 50 players from the 2023–24 season, I asked three questions: does position change points per game, do more minutes mean more points, and do Eastern and Western Conference players differ in assists?",
    "Merged player and stats tables in pandas, cleaned them, and answered each question with group summaries, crosstabs and a Pearson correlation.",
    "Keeping the analysis honest with a small sample. I reported what the data showed, including the question where the answer was no difference.",
    "A Jupyter notebook with the full analysis.",
    "Point guards scored the most (18.8 points per game on average); minutes and points were strongly related (r = 0.64); and conference made essentially no difference to assists (4.29 vs. 4.28).",
    "",
    [("View the notebook", f"{GH}/python-data-analysis/blob/main/nba-player-performance/nba-player-performance-analysis.ipynb")],
) + case(
    "time-series",
    "Teaching time series to the class",
    "INFO 3200, Spring 2026. Class presentation with Jack Callahan.",
    ["R", "Time series", "Quarto / Reveal.js", "Presenting"],
    "Our classmates needed a working understanding of time series before the next unit: what makes it different from regular data, and how to split a series into trend, seasonality and noise.",
    "We co-built and presented an interactive slide deck using the AirPassengers dataset, covering decomposition, stationarity and forecasting basics, with speaker notes and everyday examples.",
    "Explaining statistics to peers without losing them. We tied each idea to something familiar, like tracking a Venmo balance or Spotify streams.",
    "A Quarto slide deck with live R charts.",
    "The class left able to read a decomposition chart and say why stationarity matters, which set up the forecasting work that followed.",
    "",
    [("View the slides", "reports/time-series-presentation.html")],
)

# ---------------------------------------------------------------- EXPERIENCE
experience = f"""
<section class="page-intro"><div class="wrap">
<h1>Experience</h1>
<p class="lede">What I've worked on, the tools I used and what came of it. I've kept the numbers but left out anything confidential (no property, client or partner names).</p>
</div></section>

<section class="section" style="padding-top:8px"><div class="wrap">

<div class="entry">
<div class="when"><strong>July 2026 to present</strong>Part-time during the school year. Joining full time in July 2027.</div>
<div>
<h3>Asset Management &amp; Development Intern</h3>
<p class="org">Smith &amp; Henzy, affordable-housing development and finance (LIHTC)</p>
<p>I support the asset management and development teams on a portfolio of low-income housing tax credit (LIHTC) properties: performance reporting, next-year budgets, the monthly portfolio tracker, construction draws and compliance. I use AI tools heavily for the build work. I set the methodology and rules, direct the work and check every output before it goes to my supervisors.</p>

<p class="sub">Budget vs. actual dashboard (my own initiative)</p>
<ul>
<li><strong>Problem:</strong> leadership had no single view of how properties were doing against budget, and the financials arrived in about 9 different property-manager formats.</li>
<li><strong>What I did:</strong> normalized six months of budget-vs-actual data for 21 properties into one dataset with 5 standard metrics (income, expenses, NOI, vacancy, expense ratio). I built a one-file dashboard in R and Quarto with automatic red, yellow and green flags.</li>
<li><strong>Challenge:</strong> 7 properties paid some costs, like insurance or taxes, through escrow on one side of the report only. I set a rule to drop a mismatched category from both sides and footnote it, so no property is ever compared on mismatched totals. Some reports were scanned images that needed OCR.</li>
<li><strong>Result:</strong> flagged 7 properties for follow-up. New months can be added without touching the dashboard code.</li>
</ul>
<figure style="margin:18px 0 8px;max-width:760px"><img src="img/bva-dashboard-illustration.jpg" alt="Illustration of a budget-vs-actual dashboard with twelve property cards flagged review, watch or on track" loading="lazy"><figcaption>What the dashboard looks like, rebuilt with invented properties and numbers. The real one uses confidential data.</figcaption></figure>

<p class="sub">Next-year operating budgets</p>
<ul>
<li>Prepared 2027 operating budgets for 16 properties from trailing-12-month actuals, using a written rule set so every property is budgeted the same way. For example, vacancy is a flat 5%, utilities rise 3% unless a known rate exists, and management fees come from the actual contract.</li>
<li>Caught problems that would have skewed budgets: partial-year data labeled as a full year, outdated embedded tabs, and debt on the balance sheet that never showed on the income statement. A line-by-line audit after one rebuild caught a stale value that a formula check had missed.</li>
</ul>

<p class="sub">Monthly portfolio tracker</p>
<ul>
<li>Each month about 30 properties' financials go into one tracker. I documented where each of its ~28 columns comes from for each of the 6 main report formats, and added tie-out checks (income and net cash flow must match the statements).</li>
<li>Found and fixed a formula error that added up a monthly <em>balance</em> instead of averaging it, overstating delinquent rent across the portfolio. I then built a delinquency tab that finds each property's latest month and highlights rising or falling balances.</li>
</ul>

<p class="sub">Compliance and one-off analysis</p>
<ul>
<li>Read the recorded regulatory agreements for 3 newly acquired LIHTC communities (310 units) to find 7 required resident-service categories and how often each is required. I caught that the property manager's notes, which said there was no requirement, were wrong. I then lined up local nonprofit and public providers.</li>
<li>Reviewed 57 vendor invoices against the payables tracker and caught 13 already entered, a possible duplicate charge, and a vendor change of payment account that could have misrouted a payment.</li>
<li>Built a side-by-side pro forma comparison for the firm's principals. The first draft was called "impossible to read," so I rebuilt it with clear labels, simple formatting and notes on a separate tab, and it was approved on the second pass.</li>
</ul>
<ul class="pill-row"><li>Excel</li><li>R</li><li>Quarto</li><li>Python</li><li>OCR</li><li>AI agents</li><li>LIHTC</li><li>Budgeting</li><li>Variance analysis</li></ul>
</div>
</div>

<div class="entry">
<div class="when"><strong>2025 to present</strong>University of Denver</div>
<div>
<h3>Executive Chair of New Member Education</h3>
<p class="org">Sigma Chi Fraternity</p>
<ul>
<li>Elected to the executive board of a chapter with 120+ members.</li>
<li>Design and run the onboarding program for each incoming new member class.</li>
<li>Work with the executive board on planning, budgeting and day-to-day operations.</li>
</ul>
<ul class="pill-row"><li>Leadership</li><li>Program design</li><li>Budgeting</li></ul>
</div>
</div>

<div class="entry">
<div class="when"><strong>2024 to 2025</strong>Denver, CO</div>
<div>
<h3>Kitchen Steward</h3>
<p class="org">College Fresh</p>
<ul>
<li>Kept a high-volume campus kitchen running on schedule, working as part of a fast-moving team while carrying a full course load.</li>
</ul>
<ul class="pill-row"><li>Reliability</li><li>Teamwork</li><li>Time management</li></ul>
</div>
</div>

</div></section>
"""

# ---------------------------------------------------------------- SKILLS
skills = f"""
<section class="page-intro"><div class="wrap">
<h1>Skills</h1>
<p class="lede">What I can do, and where I've actually done it.</p>
</div></section>

<section class="section" style="padding-top:8px"><div class="wrap">
<h2 style="margin-bottom:24px">Technical skills</h2>
<div class="skill-groups">

<div class="skill-group">
<h3>Statistics and machine learning</h3>
<p>I use these to explain why something happened and to predict what comes next.</p>
<ul class="skill-list">
<li><strong>R with tidymodels</strong><span>Logistic regression, decision trees, random forests, k-nearest neighbors, naive Bayes and ROC curves. Used in <a href="projects.html#loan-default">loan default risk</a>.</span></li>
<li><strong>Customer segmentation</strong><span>k-means clustering with an elbow plot to choose the number of segments. Used in <a href="projects.html#ecommerce">e-commerce analytics</a>.</span></li>
<li><strong>Regression and time series</strong><span>Trend and seasonality models, and decomposing a series into trend, seasonality and noise. I <a href="projects.html#time-series">taught this</a> to my class.</span></li>
</ul>
</div>

<div class="skill-group">
<h3>Databases and SQL</h3>
<p>I can take a business process from a diagram to a working database.</p>
<ul class="skill-list">
<li><strong>SQL Server and T-SQL</strong><span>Tables, keys, constraints, views, functions and stored procedures. Used in <a href="projects.html#premierstats">PremierStats</a>.</span></li>
<li><strong>Data modeling</strong><span>ER diagrams, normalization to third normal form, and star schemas for data warehousing.</span></li>
<li><strong>SQLite</strong><span>Querying with joins, subqueries and aggregates across several practice databases.</span></li>
</ul>
</div>

<div class="skill-group">
<h3>Excel and finance</h3>
<p>Excel is my daily tool at work, from budgets to portfolio trackers.</p>
<ul class="skill-list">
<li><strong>Modeling and auditing</strong><span>Budgets built from trailing-12 actuals, INDEX/COUNT lookups, conditional formatting, and tracing and fixing formula errors. See <a href="experience.html">Experience</a>.</span></li>
<li><strong>Financial analysis</strong><span>10-K reading, ratio analysis, flexible budgets and variance analysis. See <a href="projects.html#variance">variance analysis</a> and <a href="projects.html#crocs">Crocs</a>.</span></li>
</ul>
</div>

<div class="skill-group">
<h3>Programming and reporting</h3>
<p>I build tools and reports other people can use.</p>
<ul class="skill-list">
<li><strong>Python and pandas</strong><span>Merging, cleaning, group summaries and pivot tables. Used in <a href="projects.html#nba">NBA analysis</a> and for reading PDF reports at work.</span></li>
<li><strong>C# and WinForms</strong><span>A desktop app with data-bound screens and printable reports on top of SQL Server.</span></li>
<li><strong>Quarto and ggplot2</strong><span>Reports, dashboards and slide decks that combine code, charts and writing.</span></li>
<li><strong>AI-assisted analysis</strong><span>Directing an AI agent on real business files under strict data rules, and checking its work before anything goes out.</span></li>
</ul>
</div>

</div>
</div></section>

<section class="section"><div class="wrap">
<h2 style="margin-bottom:24px">How I work</h2>
<div class="soft">
<div><h3>I check before I hand off</h3><p>I tie totals back to the source, audit line by line after a rebuild, and never overwrite an original file. A wrong number in a budget costs more than a slow one.</p></div>
<div><h3>I make messy data usable</h3><p>Nine report formats, scanned PDFs, missing months: I write down the rules for handling each case so the next person, or the next month, gets the same answer.</p></div>
<div><h3>I take feedback and fix it fast</h3><p>When a principal called a draft "impossible to read," I rebuilt it and it was approved on the second pass.</p></div>
<div><h3>I respect people's time</h3><p>I batch my questions into one clear list instead of sending ten emails, and I flag big swings early instead of guessing.</p></div>
<div><h3>I lead and teach</h3><p>I run onboarding for a 120+ member organization and have presented technical topics to my class.</p></div>
<div><h3>I work across cultures</h3><p>Native French speaker raised across Europe. I'm comfortable with clients and teammates from different backgrounds.</p></div>
</div>
</div></section>
"""

# ---------------------------------------------------------------- EDUCATION
def course(name, code, what, learned):
    return f'<div class="course"><h3>{name}</h3><p class="code">{code}</p><p>{what}</p><p class="learned">{learned}</p></div>'

education = """
<section class="page-intro"><div class="wrap">
<h1>Education</h1>
<p class="lede">Key courses and what I took away from each one.</p>
</div></section>

<section class="section" style="padding-top:8px"><div class="wrap">
<div class="entry">
<div class="when"><strong>Expected May 2027</strong>Denver, CO</div>
<div>
<h3>University of Denver, Daniels College of Business</h3>
<p class="org">Bachelor of Science in Business Analytics. Minor in French and Francophone Studies.</p>
</div>
</div>
</div></section>

<section class="section"><div class="wrap">
<h2 style="margin-bottom:24px">Analytics and information systems</h2>
<div class="courses">
""" + course("Statistical learning and visualization in R", "INFO 3200", "Built classification and regression models in R and judged them on data they hadn't seen. Created dashboards and reports in Quarto.", "Logistic regression, trees, random forests, kNN, naive Bayes, k-means, ROC, time series, ggplot2") \
+ course("Database programming", "INFO 3240", "Designed and built a SQL Server database, then wrote a C# app with reports on top of it.", "T-SQL, constraints, views, functions, stored procedures, C#, WinForms") \
+ course("Database management", "INFO 3140", "Learned to design relational databases from business rules and query them.", "ER diagrams, normalization to 3NF, SQL joins and subqueries") \
+ course("Automating business processes with Python", "INFO 3100", "Used Python to clean, combine and summarize business data and automate repetitive work.", "pandas, functions, loops, pivot tables") \
+ course('Data warehousing and business intelligence <span class="status">In progress</span>', "INFO 3300", "Designing a dimensional data mart for a retail client, from requirements to ETL.", "Star schemas, slowly changing dimensions, ETL") \
+ course('Project management and simulation <span class="status">In progress</span>', "INFO 3340", "Managing a simulated team project with real cost, schedule and risk constraints.", "Monte Carlo simulation, cost baselines, earned value, NPV") \
+ course('Analytics careers <span class="status">In progress</span>', "INFO 3700", "Building a professional brand and job-search materials for analytics roles, including this site.", "Personal branding, resumes, interviewing") \
+ """
</div>
</div></section>

<section class="section"><div class="wrap">
<h2 style="margin-bottom:24px">Business, finance and communication</h2>
<div class="courses">
""" + course("Introduction to financial reporting", "ACTG 2200", "Read real 10-K filings and analyzed a public company's performance over two years.", "Financial statements, ratios, EPS, SEC filings") \
+ course("Managerial accounting", "Accounting II", "Used costs and budgets to support management decisions and presented findings to a mock board.", "Flexible budgets, variance analysis, break-even, Tableau") \
+ course("Business communications", "Daniels College of Business", "Practiced professional writing and presenting, including managerial reports and an informational interview.", "Business writing, presentations, professional email") \
+ course("French and Francophone studies", "Minor", "Upper-level writing and literature courses taught in French.", "Advanced French writing, Francophone literature") \
+ """
</div>
</div></section>
"""

# ---------------------------------------------------------------- BEYOND
beyond = """
<section class="page-intro"><div class="wrap">
<h1>Beyond work</h1>
<p class="lede">A few things that don't fit on a resume but say a lot about how I work.</p>
</div></section>

<section class="section" style="padding-top:8px"><div class="wrap">
<div class="beyond">
<div><h3>Growing up across Europe</h3><p>I was raised in Malta, Austria, France and Finland before settling in New Orleans. I'm a native French speaker, and moving that often taught me to walk into a new room, figure out how it works and fit in fast. Clients and teammates from different backgrounds feel familiar to me, not foreign.</p></div>
<div><h3>Soccer: captain and referee</h3><p>I captained my varsity team at Brother Martin High School to a district championship. I'm also a soccer referee with the Louisiana State Referee Committee, which means making fast calls under pressure and explaining them to people who don't want to hear it.</p></div>
<div><h3>Leading new members in Sigma Chi</h3><p>As Executive Chair of New Member Education, I design the program that brings each new class into a chapter of 120+ members. It's part teaching, part planning and part keeping a lot of people on the same page.</p></div>
<div><h3>Premier League stats nerd</h3><p>I follow the Premier League closely as a Manchester United fan, which is partly why my database project tracks every club's players. When a hobby turns into a dataset, I'll take it.</p></div>
<div><h3>Service and discipline</h3><p>I volunteered 100+ hours serving meals to people in need in high school, and spent two years in the NJROTC Naval Development Program, where I picked up habits I still use: show up early, finish what you start.</p></div>
<div><h3>Cooking and skiing</h3><p>Living in Denver means skiing whenever I can. At home I cook; lately that's been steak au poivre and carbonara.</p></div>
</div>
</div></section>
"""

SITE = {
    "index.html": ("Home", "Finley Hardie: Business Analytics student at the University of Denver. SQL, R, Python and Excel projects and affordable-housing asset management experience.", home),
    "projects.html": ("Projects", "Analytics, database and finance projects by Finley Hardie, each with the problem, approach, challenges and business value.", projects),
    "experience.html": ("Experience", "Finley Hardie's work experience in affordable-housing asset management and leadership roles.", experience),
    "skills.html": ("Skills", "Technical and soft skills, with links to where Finley Hardie used each one.", skills),
    "education.html": ("Education", "University of Denver Business Analytics coursework and what Finley Hardie learned in each course.", education),
    "beyond.html": ("Beyond work", "Soccer, leadership, languages and life outside work for Finley Hardie.", beyond),
}

for fname, (title, desc, body) in SITE.items():
    (OUT / fname).write_text(shell(fname, title, desc, body), encoding="utf-8")
(OUT / ".nojekyll").write_text("")
print("built", len(SITE), "pages")
