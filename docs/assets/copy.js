(function () {
  const copyClass = 'copy-button';

  function getCode(area) {
    const cmContent = area.querySelector('.cm-content');
    if (cmContent) {
      return Array.from(cmContent.querySelectorAll('.cm-line'))
        .map((line) => line.textContent)
        .join('\n');
    }
    const pre = area.querySelector('pre');
    if (pre) {
      return pre.innerText;
    }
    return area.innerText;
  }

  function fallbackCopy(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.opacity = '0';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
    } catch (err) {
      console.warn('Copy failed', err);
    }
    document.body.removeChild(textArea);
  }

  function showStatus(button, message) {
    const original = button.dataset.originalLabel || button.textContent;
    if (!button.dataset.originalLabel) {
      button.dataset.originalLabel = original;
    }
    button.classList.add('is-copied');
    button.textContent = message;
    button.setAttribute('aria-live', 'polite');
    setTimeout(() => {
      button.classList.remove('is-copied');
      button.textContent = original;
      button.removeAttribute('aria-live');
    }, 1800);
  }

  async function handleCopy(event) {
    const button = event.currentTarget;
    const area = button.closest('.jp-InputArea');
    if (!area) {
      return;
    }
    const code = getCode(area).trimEnd();
    if (!code) {
      showStatus(button, 'Empty');
      return;
    }
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(code);
      } else {
        fallbackCopy(code);
      }
      showStatus(button, 'Copied!');
    } catch (error) {
      console.warn('Clipboard error', error);
      fallbackCopy(code);
      showStatus(button, 'Copied');
    }
  }

  function injectButton(area) {
    const editor = area.querySelector('.jp-InputArea-editor');
    if (!editor) {
      return;
    }
    if (area.dataset.copyDecorated === 'true') {
      return;
    }
    area.dataset.copyDecorated = 'true';
    const button = document.createElement('button');
    button.type = 'button';
    button.className = copyClass;
    button.setAttribute('data-copy-button', '');
    button.setAttribute('aria-label', 'Copy code to clipboard');
    button.textContent = 'Copy';
    button.addEventListener('click', handleCopy);
    editor.appendChild(button);
  }

  function decorateAll() {
    document.querySelectorAll('.jp-InputArea').forEach((area) => {
      area.style.position = area.style.position || 'relative';
      injectButton(area);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', decorateAll);
  } else {
    decorateAll();
  }
})();
