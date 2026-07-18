import os

def create_banner(output_path, banner_b64, is_light=False):
    # Colors
    bg = "#f8f4ff" if is_light else "#0d0117"
    text = "#1a0a2e" if is_light else "#ffffff"
    text_muted = "#555577" if is_light else "#8888aa"
    card_bg = "rgba(100,50,150,0.08)" if is_light else "rgba(255,255,255,0.05)"
    code_bg = "#f0ecf7" if is_light else "#1e1e3f"
    pink = "#ff6baa" if is_light else "#ff2d7b"
    purple = "#7c3aed" if is_light else "#a855f7"
    glow = "rgba(124, 58, 237, 0.2)" if is_light else "rgba(255, 45, 123, 0.4)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 580" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg}" />
      <stop offset="50%" stop-color="{bg}" />
      <stop offset="100%" stop-color="{"#ebd9ff" if is_light else "#12001a"}" />
    </linearGradient>
    <linearGradient id="accent-grad" x1="0%" y1="0%" x2="200%" y2="0%">
      <stop offset="0%" stop-color="{pink}" />
      <stop offset="25%" stop-color="{purple}" />
      <stop offset="50%" stop-color="{pink}" />
      <animate attributeName="x1" values="0%;-100%" dur="3s" repeatCount="indefinite" />
      <animate attributeName="x2" values="200%;100%" dur="3s" repeatCount="indefinite" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="8" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <clipPath id="hologram-clip">
      <rect x="780" y="0" width="450" height="0">
        <animate attributeName="height" values="0;400" begin="3s" dur="2s" fill="freeze" />
      </rect>
    </clipPath>
    
    <clipPath id="banner-clip">
      <rect width="1280" height="580" rx="16" />
    </clipPath>
  </defs>

  <style>
    @keyframes blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    .cursor {{ animation: blink 0.8s infinite; fill: {pink}; }}
    
    @keyframes type {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    
    @keyframes slideUp {{
      from {{ transform: translateY(20px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}
    
    @keyframes float {{
      0% {{ transform: translateY(0) scale(1); opacity: 0.8; }}
      50% {{ transform: translateY(-20px) scale(1.1); opacity: 0.4; }}
      100% {{ transform: translateY(0) scale(1); opacity: 0.8; }}
    }}
    
    @keyframes pulse {{
      0% {{ opacity: 0.2; transform: scale(1); }}
      50% {{ opacity: 0.5; transform: scale(1.2); }}
      100% {{ opacity: 0.2; transform: scale(1); }}
    }}
    
    .role {{ opacity: 0; }}
    .role-1 {{ animation: roleCycle 12s infinite 4s; }}
    .role-2 {{ animation: roleCycle 12s infinite 8s; }}
    .role-3 {{ animation: roleCycle 12s infinite 12s; }}
    
    @keyframes roleCycle {{
      0%, 25% {{ opacity: 1; transform: translateY(0); }}
      33%, 100% {{ opacity: 0; transform: translateY(-10px); }}
    }}
    
    .pill {{ opacity: 0; transform: scale(0.9); }}
    .about-line {{ opacity: 0; transform: translateX(-20px); }}
    .code-line {{ opacity: 0; }}
    
    @keyframes widthAnim {{
      from {{ width: 0; }}
      to {{ width: 85%; }}
    }}
    
    @keyframes flicker {{
      0%, 100% {{ opacity: 1; }}
      41% {{ opacity: 1; }}
      42% {{ opacity: 0.3; }}
      43% {{ opacity: 1; }}
      45% {{ opacity: 0.2; }}
      46% {{ opacity: 1; }}
    }}
    
    .text-mono {{ font-family: "Consolas", "Courier New", monospace; font-size: 18px; fill: {text}; }}
    .text-body {{ font-family: "Segoe UI", "Helvetica Neue", sans-serif; fill: {text}; }}
    
  </style>

  <rect width="1280" height="580" rx="16" fill="url(#bg-grad)" clip-path="url(#banner-clip)"/>

  <!-- Background Orbs -->
  <circle cx="200" cy="450" r="150" fill="{purple}" opacity="0.1" filter="url(#glow)">
    <animate attributeName="cy" values="450;400;450" dur="8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1000" cy="150" r="200" fill="{pink}" opacity="0.1" filter="url(#glow)">
    <animate attributeName="r" values="200;220;200" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- Content Group -->
  <g transform="translate(60, 60)">
    
    <!-- Terminal Line -->
    <g class="text-mono" font-weight="bold">
      <text x="0" y="20">
        <tspan fill="{pink}">hassan@dev</tspan>
        <tspan fill="{text_muted}">:~$</tspan>
        <tspan fill="{text}"> cat README.md</tspan>
      </text>
      <rect x="250" y="3" width="10" height="20" class="cursor"/>
    </g>

    <!-- Name -->
    <text x="0" y="90" class="text-body" font-size="64" font-weight="800" fill="url(#accent-grad)" letter-spacing="-1">
      Hassan Ali Abrar
      <animate attributeName="opacity" values="0;1" begin="2s" dur="1s" fill="freeze"/>
    </text>

    <!-- Roles -->
    <g class="text-mono" font-size="24" fill="{text_muted}" transform="translate(0, 140)">
      <text x="0" y="0" class="role role-1">>> AI Engineer</text>
      <text x="0" y="0" class="role role-2">>> Full Stack Developer</text>
      <text x="0" y="0" class="role role-3">>> Open Source Contributor</text>
    </g>

    <!-- Quote Box -->
    <g transform="translate(0, 180)">
      <rect x="0" y="0" width="550" height="50" rx="8" fill="{card_bg}" stroke="{purple}" stroke-width="1" opacity="0.5"/>
      <text x="20" y="32" class="text-body" font-size="20" font-style="italic" fill="{text_muted}">
        "Keep learning. Keep building. Keep growing."
      </text>
      <animate attributeName="opacity" values="0;1" begin="5s" dur="0.8s" fill="freeze" />
      <animateTransform attributeName="transform" type="translate" values="0,200; 0,180" begin="5s" dur="0.8s" fill="freeze" />
    </g>

    <!-- Code Editor (Left Side) -->
    <g transform="translate(0, 250)">
      <rect width="600" height="200" rx="10" fill="{code_bg}" stroke="#333" stroke-width="1"/>
      <!-- Mac Buttons -->
      <circle cx="20" cy="20" r="6" fill="#ff5f56"/>
      <circle cx="40" cy="20" r="6" fill="#ffbd2e"/>
      <circle cx="60" cy="20" r="6" fill="#27c93f"/>
      
      <g class="text-mono" font-size="18" transform="translate(20, 50)">
        <text y="0">
          <tspan fill="{pink}">const</tspan> <tspan fill="{text}">buildDreams</tspan> <tspan fill="{text_muted}">=</tspan> <tspan fill="{purple}">()</tspan> <tspan fill="{pink}">=&gt;</tspan> <tspan fill="{text_muted}">{{</tspan>
        </text>
        <text y="25" opacity="0">
          <tspan fill="{text}" dx="20">while(</tspan><tspan fill="{purple}">alive</tspan><tspan fill="{text}">) {{</tspan>
          <animate attributeName="opacity" values="0;1" begin="9.5s" dur="0.1s" fill="freeze"/>
        </text>
        <text y="50" opacity="0">
          <tspan fill="{pink}" dx="40">code</tspan><tspan fill="{text}">(); </tspan><tspan fill="{pink}">learn</tspan><tspan fill="{text}">(); </tspan><tspan fill="{pink}">grow</tspan><tspan fill="{text}">();</tspan>
          <animate attributeName="opacity" values="0;1" begin="10.5s" dur="0.1s" fill="freeze"/>
        </text>
        <text y="75" opacity="0">
          <tspan fill="{text}" dx="20">}}</tspan>
          <animate attributeName="opacity" values="0;1" begin="11s" dur="0.1s" fill="freeze"/>
        </text>
        <text y="100" opacity="0">
          <tspan fill="{text_muted}">  }}</tspan>
          <animate attributeName="opacity" values="0;1" begin="11.5s" dur="0.1s" fill="freeze"/>
        </text>
        <text y="125" opacity="0">
          <tspan fill="{text_muted}">}};</tspan>
          <animate attributeName="opacity" values="0;1" begin="12s" dur="0.1s" fill="freeze"/>
        </text>
      </g>
    </g>

    <!-- About Me -->
    <g transform="translate(0, 470)" class="text-body" font-size="18" fill="{text_muted}">
      <text x="0" y="0">
        <tspan x="0" dy="0" opacity="0">⚡ Turning coffee into intelligent AI solutions.</tspan>
        <tspan x="0" dy="30" opacity="0">🌱 Currently exploring advanced machine learning architectures.</tspan>
        <tspan x="0" dy="30" opacity="0">🎯 Goals: Build impactful tech and automate the boring stuff.</tspan>
        <animate attributeName="opacity" values="0;1" begin="7s" dur="0.5s" fill="freeze"/>
      </text>
    </g>
    
  </g>

  <!-- Right Side - Character, Scanner, Skills -->
  <!-- Image Hologram Clip -->
  <g clip-path="url(#hologram-clip)">
    <!-- Embed the character image (Smaller, not overlapping) -->
    <image x="800" y="10" width="400" height="400" href="data:image/png;base64,{banner_b64}" preserveAspectRatio="xMidYMid meet" />
  </g>
  
  <!-- Scan line leading the reveal -->
  <rect x="800" y="10" width="400" height="3" fill="{pink}" filter="url(#glow)" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="3s" dur="2s" />
    <animate attributeName="y" values="10;410" begin="3s" dur="2s" fill="freeze"/>
  </rect>

  <!-- Skills Under Image -->
  <g transform="translate(730, 420)">
'''
    
    skills = [
        ("Python", "#3776AB", "M19.98 10.87c.05-.73-.24-1.89-1.28-2.67-1.3-.98-3.32-1.35-6.05-1.35H8.7c-2.48 0-4.5 1.76-4.5 3.93v3.93c0 2.17 2.02 3.93 4.5 3.93h1.86v-1.96c0-1.63 1.34-2.95 3-2.95h3.94c1.66 0 3-1.32 3-2.95v-2.36h.05c-.01.16-.07.31-.07.47z M15.15 8.12c.5 0 .9.39.9.88s-.4.88-.9.88-.9-.39-.9-.88.4-.88.9-.88z"),
        ("AI/ML", "#FF6F00", "M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"),
        ("Linux", "#FCC624", "M12 22s-4-1.5-4-5.5V11C8 8.5 9 5 12 5s4 3.5 4 6v5.5c0 4-4 5.5-4 5.5z"),
        ("HTML", "#E34F26", "M1.5 1.5h21l-1.9 21-8.6 2.5-8.6-2.5-1.9-21zm10.5 19.5l6.5-1.9 1.3-14.6H4.2l.4 4.5h11l-.3 3.6-4.8 1.4-4.8-1.4-.2-2.7H3.4l.4 5.9 6.7 1.9h.1z"),
        ("CSS", "#1572B6", "M1.5 1.5h21l-1.9 21-8.6 2.5-8.6-2.5-1.9-21zm10.5 19.5l6.5-1.9 1.3-14.6H4.2l.4 4.5h11l-.3 3.6-4.8 1.4-4.8-1.4-.2-2.7H3.4l.4 5.9 6.7 1.9h.1z"),
        ("JavaScript", "#F7DF1E", "M0 0h24v24H0V0zm22 22H2V2h20v20zM15 11h2c.6 0 1-.4 1-1V8c0-.6-.4-1-1-1h-4v6h3v1h-3v2h4c.6 0 1-.4 1-1v-2c0-.6-.4-1-1-1h-2v-1zM9 11H7v7H5v-9h4c.6 0 1 .4 1 1v1c0 .6-.4 1-1 1z"),
        ("React", "#61DAFB", "M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10zm0-1c-4.97 0-9-4.03-9-9s4.03-9 9-9 9 4.03 9 9-4.03 9-9 9z"),
        ("Node.js", "#339933", "M12 2L2 7v10l10 5 10-5V7l-10-5zm0 18l-8-4V9l8-4 8 4v8l-8 4z"),
        ("SQL", "#4169E1", "M12 2C6.48 2 2 4.24 2 7v10c0 2.76 4.48 5 10 5s10-2.24 10-5V7c0-2.76-4.48-5-10-5zm0 3c4.42 0 8 1.79 8 4s-3.58 4-8 4-8-1.79-8-4 3.58-4 8-4z"),
        ("Docker", "#2496ED", "M2 15s2-1 5 1c3 2 7 2 10-1 3-3 5-1 5-1V9H2v6zM4 3h3v3H4V3zm5 0h3v3H9V3zm5 0h3v3h-3V3z"),
        ("Git", "#F05032", "M21.71 10.29l-9-9c-.39-.39-1.02-.39-1.41 0l-9 9c-.39.39-.39 1.02 0 1.41l9 9c.39.39 1.02.39 1.41 0l9-9c.39-.39.39-1.02 0-1.41zM12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z")
    ]
    x_offset = 0
    y_offset = 0
    delay = 5.5
    for i, (skill, color, path) in enumerate(skills):
        svg += f'''
      <g transform="translate({x_offset}, {y_offset})">
        <rect width="{len(skill)*12 + 40}" height="36" rx="18" fill="{card_bg}" stroke="{color}" stroke-width="1.5" opacity="0.8"/>
        <!-- Basic SVG Icon approach -->
        <svg x="10" y="8" width="20" height="20" viewBox="0 0 24 24" fill="{color}"><path d="{path}"/></svg>
        <text x="35" y="24" class="text-body" font-size="16" fill="{color}">{skill}</text>
        <animate attributeName="opacity" values="0;1" begin="{delay}s" dur="0.3s" fill="freeze"/>
      </g>'''
        x_offset += len(skill)*12 + 50
        if x_offset > 450:
            x_offset = 0
            y_offset += 45
        delay += 0.15
        
    svg += f'''
    </g>
  
  <!-- Continuous Scanner -->
  <rect x="0" y="-10" width="1280" height="4" fill="url(#accent-grad)" filter="url(#glow)" opacity="0.6">
    <animate attributeName="y" values="-10;590" begin="5s" dur="3.5s" repeatCount="indefinite" />
  </rect>

  <!-- Particles and Sparkles Overlay (Subtle) -->
  <g fill="{pink}" opacity="0.5">
    <circle cx="850" cy="200" r="3"><animate attributeName="cy" values="200;150;200" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="1100" cy="600" r="2"><animate attributeName="cy" values="600;550;600" dur="3s" repeatCount="indefinite"/></circle>
    <circle cx="900" cy="500" r="4" fill="{purple}"><animate attributeName="cy" values="500;430;500" dur="5s" repeatCount="indefinite"/></circle>
  </g>
</svg>
'''
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def create_lanyard(output_path, face_b64):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-250 -50 500 600" width="350" height="420">
  <defs>
    <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.15)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0.05)"/>
    </linearGradient>
    <linearGradient id="shine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0)" />
      <stop offset="40%" stop-color="rgba(255,255,255,0)" />
      <stop offset="50%" stop-color="rgba(255,255,255,0.5)" />
      <stop offset="60%" stop-color="rgba(255,255,255,0)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </linearGradient>
    <filter id="glow-badge">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="avatar-clip">
      <circle cx="0" cy="120" r="60"/>
    </clipPath>
  </defs>

  <style>
    @keyframes dropIn {{
      0% {{ transform: translateY(-500px); }}
      60% {{ transform: translateY(20px); }}
      80% {{ transform: translateY(-10px); }}
      100% {{ transform: translateY(0); }}
    }}
    
    @keyframes sway {{
      0% {{ transform: rotate(15deg); }}
      100% {{ transform: rotate(-15deg); }}
    }}
    
    .pendulum {{
      transform-origin: 0px -50px;
      animation: dropIn 1s cubic-bezier(0.25, 1, 0.5, 1) forwards, sway 3s ease-in-out 1s infinite alternate;
    }}
    
    @keyframes shineAnim {{
      0% {{ transform: translateX(-300px) translateY(-300px); }}
      100% {{ transform: translateX(300px) translateY(300px); }}
    }}
    
    .shiner {{
      animation: shineAnim 4s infinite linear;
    }}
    
    .font-sans {{ font-family: "Segoe UI", sans-serif; }}
    .font-mono {{ font-family: "Consolas", monospace; }}
  </style>

  <!-- Group acting as Pendulum -->
  <g class="pendulum">
    
    <!-- Strap -->
    <path d="M -20 -150 L -15 20 L 15 20 L 20 -150" fill="#ff2d7b" opacity="0.9"/>
    
    <!-- Metal Clip -->
    <rect x="-10" y="20" width="20" height="30" rx="4" fill="#888"/>
    <circle cx="0" cy="60" r="8" fill="none" stroke="#aaa" stroke-width="4"/>
    
    <!-- Card Base -->
    <rect x="-110" y="70" width="220" height="340" rx="16" fill="#150a21" stroke="#a855f7" stroke-width="2"/>
    <rect x="-110" y="70" width="220" height="340" rx="16" fill="url(#glass)"/>
    
    <!-- Face Avatar -->
    <circle cx="0" cy="140" r="64" fill="none" stroke="#ff2d7b" stroke-width="4" filter="url(#glow-badge)"/>
    <g clip-path="url(#avatar-clip)" transform="translate(0, 20)">
      <rect x="-60" y="60" width="120" height="120" fill="#222"/>
      <image x="-60" y="60" width="120" height="120" href="data:image/png;base64,{face_b64}" preserveAspectRatio="xMidYMid slice" />
    </g>

    <!-- Text Info -->
    <text x="0" y="250" text-anchor="middle" class="font-sans" font-size="24" font-weight="bold" fill="#fff">Hassan Ali Abrar</text>
    <text x="0" y="280" text-anchor="middle" class="font-sans" font-size="16" fill="#a855f7">AI Engineer</text>
    <text x="0" y="310" text-anchor="middle" class="font-mono" font-size="14" fill="#aaa">@hassan-635</text>
    
    <!-- Fake Barcode -->
    <g transform="translate(-70, 340)" fill="#fff" opacity="0.8">
      <rect x="0" width="4" height="40"/>
      <rect x="8" width="2" height="40"/>
      <rect x="14" width="8" height="40"/>
      <rect x="26" width="2" height="40"/>
      <rect x="32" width="6" height="40"/>
      <rect x="42" width="12" height="40"/>
      <rect x="58" width="4" height="40"/>
      <rect x="66" width="2" height="40"/>
      <rect x="72" width="10" height="40"/>
      <rect x="86" width="4" height="40"/>
      <rect x="94" width="6" height="40"/>
      <rect x="104" width="4" height="40"/>
      <rect x="112" width="2" height="40"/>
      <rect x="118" width="8" height="40"/>
      <rect x="130" width="10" height="40"/>
    </g>
    
    <!-- Shine Overlay (Clipped to card) -->
    <g clip-path="url(#card-clip)">
      <clipPath id="card-clip">
        <rect x="-110" y="70" width="220" height="340" rx="16"/>
      </clipPath>
      <rect x="-220" y="70" width="660" height="660" fill="url(#shine)" class="shiner"/>
    </g>
    
  </g>
</svg>
'''
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Read base64 data
    with open(os.path.join(base_dir, "banner_b64.txt"), "r") as f:
        banner_b64 = f.read().strip()
        
    with open(os.path.join(base_dir, "face_b64.txt"), "r") as f:
        face_b64 = f.read().strip()
        
    print("Generating banner.svg...")
    create_banner(os.path.join(base_dir, "banner.svg"), banner_b64, is_light=False)
    
    print("Generating banner-light.svg...")
    create_banner(os.path.join(base_dir, "banner-light.svg"), banner_b64, is_light=True)
    
    print("Generating lanyard.svg...")
    create_lanyard(os.path.join(base_dir, "lanyard.svg"), face_b64)
    
    print("Done generating SVGs.")
