# PrismTEC
PrismTEC: The Prism Threat Enrichment and Correlation engine ingests alerts, normalizes it into a standardized format, enriches any IOCs with threat intelligence, calculates risk and confidence scores, and exports the enriched IOC information as formatted JSON generalized to support platform-ambiguity.

---

## Operational Layers

**Layer 1: Data Ingestion and Normalization**
- Ingest bulk or isolated threat data (from "predictable structured data")
  - Supported formats:
    - `Splunk`, `XSOAR`
- Reformat ingested data to PrismTEC JSON-Struct



---

## Sources for Threat Intelligence Enrichment

| ***Intelligence Focus Area*** | ***Source*** |
| --- | --- |
| **IPv4 Address** | `AbuseIPDB`, `VirusTotal` |
| **Domain** | `VirusTotal`, `Whois` |

---
