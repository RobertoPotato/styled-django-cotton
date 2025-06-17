# Using DaisyUI and Tailwind CSS

[Official DaisyUI Django Install Guide](https://daisyui.com/docs/install/django/)

## 1. Install Tailwind Executable

Download the Tailwind CSS binary for your OS:

```bash
curl -sLo myapp/static/css/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
```

## 2. Make the File Executable (Linux/macOS)

```bash
chmod +x myapp/static/css/tailwindcss
```

## 3. Get the DaisyUI Bundled JS Files

```bash
curl -sLo static/css/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js
curl -sLo static/css/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js
```

## 4. Create `input.css` in the CSS Directory

Add the following content to `input.css`:

```css
@import "tailwindcss" source(none);
@plugin "./daisyui.js";
@source "../../templates";
```

---

### Icons

Icons are from [Heroicons Solid](https://heroicons.com/solid).