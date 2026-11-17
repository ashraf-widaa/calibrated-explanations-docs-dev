/* Candidate-local RTD integration. Public event contract:
   https://docs.readthedocs.com/platform/stable/addons.html#custom-event-integration */
(() => {
  "use strict";

  let config;

  function mountVersionPicker() {
    const sidebar = document.querySelector(".sidebar-scroll");
    const active = config?.versions?.active;
    const current = config?.versions?.current;
    if (!sidebar || !Array.isArray(active) || !current?.slug) return;

    const filename = (
      document.querySelector('meta[name="readthedocs-resolver-filename"]')?.content || ""
    ).replace(/^\/+/, "");
    const versions = active.filter((version) => version.built !== false);
    if (!versions.some((version) => version.slug === current.slug)) {
      versions.unshift(current);
    }

    const picker = document.createElement("div");
    picker.className = "ce-rtd-version-picker";
    const label = document.createElement("label");
    label.htmlFor = "ce-rtd-version";
    label.textContent = "Documentation version";
    const select = document.createElement("select");
    select.id = "ce-rtd-version";
    let hasCurrent = false;

    for (const version of versions) {
      try {
        const root = new URL(version.urls.documentation);
        if (!["https:", "http:"].includes(root.protocol)) continue;
        const option = document.createElement("option");
        option.value = new URL(filename, root).href;
        option.textContent = version.verbose_name || version.slug;
        option.selected = version.slug === current.slug;
        if (option.selected) hasCurrent = true;
        select.append(option);
      } catch {
        // Leave invalid entries out; never hide the fallback without a current version.
      }
    }
    if (!hasCurrent) return;

    select.addEventListener("change", () => window.location.assign(select.value));
    picker.append(label, select);
    const previous = document.querySelector(".ce-rtd-version-picker");
    if (previous) previous.replaceWith(picker);
    else sidebar.prepend(picker);
    document.body.classList.add("ce-rtd-versions-ready");
  }

  document.addEventListener("readthedocs-addons-data-ready", (event) => {
    config = event.detail.data();
    mountVersionPicker();
  });
  document.addEventListener("DOMContentLoaded", mountVersionPicker);
})();
