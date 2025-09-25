(function () {
  const copyClass = 'copy-button';

  function getCode(container) {
    const cmContent = container.querySelector('.cm-content');
    if (cmContent) {
      return Array.from(cmContent.querySelectorAll('.cm-line'))
        .map((line) => line.textContent)
        .join('\n');
    }
    if (container.tagName === 'PRE') {
      return container.innerText;
    }
    const pre = container.querySelector('pre');
    if (pre) {
      return pre.innerText;
    }
    const code = container.querySelector('code');
    if (code) {
      return code.innerText;
    }
    return container.innerText;
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
    const container = button.closest('[data-copy-target]');
    if (!container) {
      return;
    }
    const code = getCode(container).trimEnd();
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

  function ensurePosition(container) {
    const style = window.getComputedStyle(container);
    if (!style || style.position === 'static') {
      container.style.position = 'relative';
    }
  }

  function injectButton(container) {
    if (!container || container.dataset.copyDecorated === 'true') {
      return;
    }
    container.dataset.copyDecorated = 'true';
    container.setAttribute('data-copy-target', '');
    container.classList.add('has-copy-button');
    ensurePosition(container);

    const button = document.createElement('button');
    button.type = 'button';
    button.className = copyClass;
    button.setAttribute('data-copy-button', '');
    button.setAttribute('aria-label', 'Copy code to clipboard');
    button.textContent = 'Copy';
    button.addEventListener('click', handleCopy);
    container.appendChild(button);
  }

  function decorateCodeCells() {
    document.querySelectorAll('.jp-InputArea').forEach((area) => {
      const editor = area.querySelector('.jp-InputArea-editor');
      if (editor) {
        injectButton(editor);
      }
    });
  }

  function decorateMarkdownBlocks() {
    document.querySelectorAll('.jp-RenderedMarkdown').forEach((markdown) => {
      markdown.querySelectorAll('div.highlight').forEach((block) => {
        injectButton(block);
      });

      markdown.querySelectorAll('pre').forEach((pre) => {
        if (pre.closest('div.highlight')) {
          return;
        }
        if (pre.dataset.copyWrapped === 'true') {
          return;
        }
        pre.dataset.copyWrapped = 'true';
        const wrapper = document.createElement('div');
        wrapper.className = 'copy-markdown-block';
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        injectButton(wrapper);
      });
    });
  }

  function decorateAll() {
    decorateCodeCells();
    decorateMarkdownBlocks();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', decorateAll);
  } else {
    decorateAll();
  }
})();
