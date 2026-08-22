# Structured Output Validation with Pydantic

This example demonstrates enforcing strict JSON schema conformance using Pydantic models with the Google Antigravity SDK.

```python
import asyncio
from typing import List
from pydantic import BaseModel, Field
from google.antigravity import Agent, LocalAgentConfig

class SecurityVulnerability(BaseModel):
    cve_id: str = Field(description="Standard CVE identifier or internal identifier")
    severity: str = Field(description="CRITICAL, HIGH, MEDIUM, or LOW")
    affected_module: str = Field(description="Component path or package name")
    remediation_step: str = Field(description="Concrete resolution action")

class SecurityAuditReport(BaseModel):
    target_repository: str
    risk_score: float = Field(ge=0.0, le=10.0, description="Overall risk rating 0-10")
    findings: List[SecurityVulnerability]

async def main():
    config = LocalAgentConfig(
        system_instructions="You are a strict security vulnerability auditor.",
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Audit the cryptography module and emit structured JSON.",
            output_schema=SecurityAuditReport,
        )

        audit_report: SecurityAuditReport = response.structured_output
        print(f"Audited Target: {audit_report.target_repository}")
        print(f"Risk Score:     {audit_report.risk_score}")
        print(f"Total Findings: {len(audit_report.findings)}")
        for finding in audit_report.findings:
            print(f" - [{finding.severity}] {finding.cve_id} in {finding.affected_module}: {finding.remediation_step}")

if __name__ == "__main__":
    asyncio.run(main())
```
