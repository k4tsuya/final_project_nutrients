# <img src="https://raw.githubusercontent.com/user-attachments/assets/dd3a5fdf-3d44-469b-9a99-4c07d3b07044" width="32" height="32" alt="logo"> BITAMINES
### *Nutrient intelligence, simplified.*
> Track over 147 nutrients, optimize your meals, and build smarter dietary habits with data-driven insights.

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)   
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)   
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)   
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)   
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)   
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)   
[![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)

</div>

---

### ✨ Key Features

| Feature                 | Description                                                                                             | Status      |
| ----------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| 🧬 **Deep Nutrient Insights** | Access data on 147+ essential nutrients, compare foods with our powerful engine, and see bioavailability estimates. | ✅ Complete |
| 📊 **Personalized Tracking**  | Log meals in under 30 seconds, get dynamic daily targets based on your goals, and receive smart deficiency alerts. | ✅ Complete |
| ⚡ **Smart Pattern Analysis**  | Discover insights from your meal timing, find nutrient synergies, and generate automated health reports.        | 🚧 In Progress |
| 🍏 **Recipe Optimizer**      | Automatically adjust recipes to meet your specific nutrient targets without sacrificing taste.                | 📅 Planned   |

---

### 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/bitamines.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
4.  Open your browser to `http://127.0.0.1:8000` and start your journey to smarter eating!

---

<p align="center">
  Made with ❤️ by the Bitamines Team
</p>

---

### 🌱 Your Daily Nutrition at a Glance

This chart provides a real-time overview of your macronutrient balance. It animates on load to draw your attention to the data that matters most.





<!-- SELF-ANIMATING SVG PIE CHART - Placed at the very end for maximum compatibility -->
<svg width="100%" height="320" viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
    <!-- Chart Title -->
    <text x="400" y="30" font-family="'Segoe UI', sans-serif" font-size="24" font-weight="600" text-anchor="middle" fill="#333">Macronutrient Distribution</text>

    <!-- Chart Circle Group -->
    <g transform="translate(200, 170) rotate(-90)">
        <!-- Segments -->
        <circle r="90" cx="0" cy="0" fill="transparent" stroke="#D1E4C9" stroke-width="60"/>
        
        <!-- Segment 1: Protein (25%) -->
        <circle r="90" cx="0" cy="0" fill="transparent" stroke="#8DBC7F" stroke-width="60" stroke-dasharray="141.3 424.1">
            <animate attributeName="stroke-dashoffset" from="565.4" to="0" dur="1.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" />
        </circle>
        
        <!-- Segment 2: Vitamins (45%) - Rotated by 25% -->
        <circle r="90" cx="0" cy="0" fill="transparent" stroke="#6E8B3D" stroke-width="60" stroke-dasharray="254.4 311" transform="rotate(90)">
             <animate attributeName="stroke-dashoffset" from="565.4" to="0" dur="1.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" begin="0.2s"/>
        </circle>
        
        <!-- Segment 3: Minerals (30%) - Rotated by 70% (25+45) -->
        <circle r="90" cx="0" cy="0" fill="transparent" stroke="#A2C47E" stroke-width="60" stroke-dasharray="169.6 395.8" transform="rotate(252)">
            <animate attributeName="stroke-dashoffset" from="565.4" to="0" dur="1.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" begin="0.4s"/>
        </circle>
    </g>

    <!-- Legend -->
    <g transform="translate(450, 100)" font-family="'Segoe UI', sans-serif" font-size="16">
        <!-- Protein -->
        <rect x="0" y="0" width="16" height="16" fill="#8DBC7F" rx="4"/>
        <text x="25" y="13" fill="#555">Protein (25%)</text>
        
        <!-- Vitamins -->
        <rect x="0" y="40" width="16" height="16" fill="#6E8B3D" rx="4"/>
        <text x="25" y="53" fill="#555">Vitamins (45%)</text>
        
        <!-- Minerals -->
        <rect x="0" y="80" width="16" height="16" fill="#A2C47E" rx="4"/>
        <text x="25" y="93" fill="#555">Minerals (30%)</text>

        <!-- Interactive Hint -->
        <text x="0" y="140" font-size="14" fill="#777" font-style="italic">Hover over segments for details in the app!</text>
    </g>
</svg>










