from agents.transcriber import TranscriberAgent
from agents.summarizer import SummarizerAgent
from agents.compliance import ComplianceAgent
from agents.terraform import TerraformAgent
from agents.vault import VaultAgent
from agents.broadcaster import BroadcasterAgent
from datastore import DataStore

class Orchestrator:
    def __init__(self):
        self.transcriber = TranscriberAgent()
        self.summarizer = SummarizerAgent()
        self.compliance = ComplianceAgent()
        self.terraform = TerraformAgent()
        self.vault = VaultAgent()
        self.broadcaster = BroadcasterAgent()
        self.db = DataStore()

    def run(self, audio_input):
        transcript_data = self.transcriber.process({"audio": audio_input})
        summary_data = self.summarizer.process(transcript_data)
        self.db.save("summary", summary_data)

        compliance_data = self.compliance.process({"flags": summary_data.get("compliance_flags")})
        self.db.save("compliance", compliance_data)

        if summary_data.get("actions"):
            infra_result = self.terraform.process({"actions": summary_data["actions"]})
            self.db.save("infra", infra_result)

            vault_result = self.vault.process({"actions": summary_data["actions"]})
            self.db.save("vault", vault_result)

        broadcast_data = self.broadcaster.process(summary_data)
        self.db.save("broadcast", broadcast_data)

        return {
            "transcript": transcript_data,
            "summary": summary_data,
            "compliance": compliance_data,
            "infra": self.db.get("infra"),
            "vault": self.db.get("vault"),
            "broadcast": broadcast_data
        }