# AccessLearn

An open-source assistive learning platform designed to make standard educational materials accessible for blind, low-vision, and deaf students.

## The Problem
Millions of visually and hearing-impaired students—particularly in developing and underserved regions—lack access to localized, adaptive study tools. Most mainstream EdTech platforms are built for sighted and hearing users first, leaving students with disabilities behind due to high licensing costs for specialized software and a lack of localized content.

## What We Are Building
AccessLearn is a modular, open-source toolkit that bridges this gap by converting standard curricula into accessible, interactive formats:

* **Voice-First Navigation & Screen-Reader Optimization:** Clean, distraction-free interfaces strictly compliant with WCAG 2.1 AA/AAA standards, allowing blind students to navigate lessons independently using audio cues and keyboard shortcuts.
* **Automated Visual Descriptions:** Tools that generate clear, context-aware text and audio descriptions for educational diagrams, charts, and images.
* **Smart Transcription & Structured Captions:** Real-time captioning and simplified text summaries for video and audio lectures, helping deaf and hard-of-hearing learners follow along effortlessly.
* **Lightweight & Localizable:** Built to run smoothly on low-bandwidth connections and easily adaptable to local languages.

## Tech Stack & Architecture
* **Frontend:** React.js, Next.js, Tailwind CSS (built with semantic HTML5 and ARIA attributes for seamless screen-reader compatibility).
* **Backend:** Python, FastAPI (high-performance asynchronous API for media, audio, and text processing).
* **AI & Accessibility Engine:** 
  * Large Language Models (Claude API) for curriculum simplification, structured note generation, and context-aware visual descriptions.
  * Speech-to-Text (Whisper) & Web Speech API for real-time transcription and voice-guided navigation.
* **Database & Storage:** PostgreSQL, Redis (for caching processed audio/text modules).

## Getting Started (Local Development)

```bash
# Clone the repository
git clone [https://github.com/your-username/access-learn.git](https://github.com/your-username/access-learn.git)

# Navigate to the project directory
cd access-learn

# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend && npm install