class MijnTestCard extends HTMLElement {
  setConfig(config) {
    this._config = config || {};
    if (!this.style) this.style = '';
  }

  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: "open" });
    }
    this._render();
  }

  _render() {
    const entityText = this._config.entity ? `Entity: ${this._config.entity}` : "Geen entity ingesteld";
    const style = `
      <style>
        :host { display:block; box-shadow: var(--ha-card-box-shadow, 0 1px 3px rgba(0,0,0,0.2)); padding: 12px; border-radius: 6px; background: var(--card-background-color, white); color: var(--primary-text-color); font-family: Roboto, Helvetica, Arial, sans-serif; }
        h3 { margin: 0 0 8px 0; font-size: 14px; }
        p { margin: 0; font-size: 13px; }
      </style>
    `;
    this.shadowRoot.innerHTML = `${style}
      <div>
        <h3>Mijn Test Plugin</h3>
        <p id="info">${entityText}</p>
      </div>
    `;
  }

  set hass(hass) {
    this._hass = hass;
    if (!this._config || !this._config.entity) return;
    const stateObj = hass.states[this._config.entity];
    const infoEl = this.shadowRoot && this.shadowRoot.getElementById("info");
    if (infoEl) {
      infoEl.textContent = stateObj ? `State: ${stateObj.state}` : `Entity ${this._config.entity} niet gevonden`;
    }
  }
}

if (!customElements.get("mijn-test-plugin")) {
  customElements.define("mijn-test-plugin", MijnTestCard);
}

window.customCards = window.customCards || [];
window.customCards.push({
  type: "mijn-test-plugin",
  name: "Mijn Test Plugin",
  preview: false,
  description: "Eenvoudige test plugin / Lovelace custom card"
});

export default MijnTestCard;
