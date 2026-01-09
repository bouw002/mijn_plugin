# Mijn Test Plugin (HACS test plugin)

Eenvoudige test frontend plugin / Lovelace custom card bedoeld om te gebruiken met HACS.

## Inhoud
- `mijn-plugin.js` — de frontend plugin / custom card
- `hacs.json` — HACS metadata

## Installatie via HACS (voor gebruikers)
1. Voeg deze repository toe als een Custom Repository in HACS:
   - HACS -> Integraties / Frontend -> Repositories -> Voeg repository toe
   - Type: `plugin`
2. Installeer de plugin via HACS.
3. Voeg de resource toe in Lovelace (Settings -> Resources) met:

```yaml
url: /hacsfiles/mijn_plugin/mijn-plugin.js
type: module
```

(Het pad `/hacsfiles/<owner>_<repo>/...` kan variëren afhankelijk van HACS; na installatie toont HACS de juiste resource-URL.)

4. Gebruik de kaart in Lovelace (voorbeeld):

```yaml
type: custom:mijn-test-plugin
entity: sensor.example  # optioneel, toont state als opgegeven
```

## Ontwikkelen / lokaal testen
- Je kunt de `mijn-plugin.js` direct als module laden in je Lovelace resources tijdens ontwikkeling.
- Debugging: open de browser console; de kaart logt geen foutmeldingen door eenvoudige implementatie.

## Aanpassen / aanbevelingen
- Voeg een `package.json` en buildstap toe als je ES6-modules / bundlers gebruikt.
- Voeg versiebeheer in `hacs.json` of gebruik releases wanneer je deze plugin publiceert.
- Voeg preview-afbeelding en uitgebreidere README met screenshots toe voor publicatie in HACS.

## License
Kies een license en voeg `LICENSE` file toe (bijv. MIT).
