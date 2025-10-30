
#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup

def extract_html_data(filepath):
    """Extract title, description, and published date from an HTML file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        title = soup.title.string.strip() if soup.title else os.path.basename(filepath)
        description_tag = soup.find("meta", attrs={"name": "description"})
        description = description_tag["content"].strip() if description_tag else "(No description found)"
        published_tag = soup.find("meta", attrs={"property": "article:published_time"})
        published_date = published_tag["content"].split("T")[0] if published_tag else "(No date)"
        return {"file": filepath, "title": title, "description": description, "date": published_date}
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def build_li(entry):
    """Build one <li> block in the format requested."""
    return f"""
      <li>
        <img src="(PLACEHOLDER)" alt="{entry['title']}">
        <div>
          <time>{entry['date']}</time>
          <h3>{entry['title']}</h3>
          <p>{entry['description']}</p>
          <button onclick="location.href='{entry['file']}'">READ MORE</button>
        </div>
      </li>"""

def main():
    entries = []
    for file in os.listdir(".."):
      filename = os.path.abspath(os.path.join("..",file))
      if filename.lower().endswith(".html") and filename != "summaries.html":
            data = extract_html_data(filename)
            if data:
                entries.append(data)

    list_items = "\n".join(build_li(e) for e in entries)

    html_output = f"""<!DOCTYPE html>
<html lang="en" itemscope itemtype="http://schema.org/Article">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Summary of all available articles.">
  <title>All Posts Summary</title>
  <link rel="stylesheet" href="../style.css">
</head>

<body>
  <header aria-label="Main Navigation">
    <nav>
      <ul>
        <li><a href="https://tracysaundersformayor.com/">Home</a></li>
        <li><a href="../biography.html">Biography</a></li>
        <li><a href="https://www.clover.com/pay-widgets/d817a1d9-bde3-4eb5-bdfb-43f13803ae61">Donate</a></li>
        <li><a href="mailto:volunteer@example.com?subject=Volunteer Inquiry">Volunteer</a></li>
        <li><a href="https://tracysaundersformayor.com/blogs/">Posts</a></li>
        <li><a href="sms:+19126604846?body=Dear Tracy,">Contact Us</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <ul>
{list_items}
    </ul>
  </main>

    <footer aria-label="Footer">
    <section aria-label="Call to Action">
      <a href="mailto:volunteer@example.com?subject=Volunteer%20Inquiry&body=Please%20fill%20out%20these%20fields%20before%20sending...%0A%0AName:%0ANumber:%0ANote:">
        <img src="../volunteer.svg" alt="Volunteer">
      </a>
      <form>
        <label for="name">Name*</label>
        <input id="name" type="text" name="name" required>
        <label for="email">Email*</label>
        <input id="email" type="email" name="email" required>
        <label for="subject">Subject*</label>
        <input id="subject" type="text" name="subject" required>
        <label for="message">Message*</label>
        <textarea id="message" name="message" required></textarea>
        <button type="submit">Submit</button>
      </form>
      <a href="https://www.clover.com/pay-widgets/d817a1d9-bde3-4eb5-bdfb-43f13803ae61">
        <img src="../donate.svg" alt="Donate">
      </a>
    </section>
    <section aria-label="Copyright Information">
      <p>&copy; 2025. All rights reserved.</p>
      <ul aria-label="Social Media Links">
        <li>
          <a href="https://www.instagram.com/tracysaundersformayor?igsh=MWg2a21mZjduM2N5">
            <svg viewBox="0 0 24 24">
              <path
                d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z">
              </path>
            </svg>
          </a>
        </li>
        <li>
          <a href="https://www.tiktok.com/@tracysaundersformayor">
            <svg viewBox="0 0 448 512">
              <path
                d="M448,209.91a210.06,210.06,0,0,1-122.77-39.25V349.38A162.55,162.55,0,1,1,185,188.31V278.2a74.62,74.62,0,1,0,52.23,71.18V0l88,0a121.18,121.18,0,0,0,1.86,22.17h0A122.18,122.18,0,0,0,381,102.39a121.43,121.43,0,0,0,67,20.14Z">
              </path>
            </svg>
          </a>
        </li>
        <li>
          <a href="https://www.facebook.com/share/1WTQAywvsR/?mibextid=wwXIfr">
            <svg viewBox="0 0 24 24">
              <path
                d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z">
              </path>
            </svg>
          </a>
        </li>
      </ul>
    </section>
  </footer>
</body>
</html>
"""

    with open("summaries.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"✅ Created summaries.html with {len(entries)} entries.")

if __name__ == "__main__":
    main()
