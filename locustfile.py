import random
from locust import HttpUser, task, between
from core.search_client import SearchGateway
from utils.data_provider import load_search_payloads

class SearchBehaviorUser(HttpUser):

    wait_time = between(1, 4)

    def on_start(self):
        self.gateway = SearchGateway(self.client)
        self.search_cases = load_search_payloads("resources/search_payloads.json")

    @task
    def execute_search_flow(self):
        case = random.choice(self.search_cases)
        query = case["query"]
        expected_status = case["expected_status"]

        with self.gateway.search_by_keyword(query) as response:

            if response.status_code != expected_status:
                response.failure(
                    f"Unexpected status for '{query}': {response.status_code}"
                )
                return

            if response.elapsed.total_seconds() > 2:
                response.failure(
                    f"SLA exceeded for '{query}': {response.elapsed.total_seconds()}s"
                )
                return

            response.success()