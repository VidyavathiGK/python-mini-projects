from collections import Counter


class ElectionSystem:
    def __init__(self, candidates: list[str]):
        self.candidates = set(candidates)
        self.voted_ids: set[str] = set()
        self.ballots: Counter = Counter()

    def cast_vote(self, voter_id: str, candidate: str) -> None:
        if voter_id in self.voted_ids:
            raise PermissionError(f"Voter '{voter_id}' has already voted.")
        if candidate not in self.candidates:
            raise ValueError(f"Invalid candidate: '{candidate}'.")

        self.voted_ids.add(voter_id)
        self.ballots[candidate] += 1

    def get_results(self) -> list[tuple[str, int]]:
        return sorted(
            [(c, self.ballots[c]) for c in self.candidates],
            key=lambda item: (-item[1], item[0]),
        )


if __name__ == "__main__":
    election = ElectionSystem(["Alice", "Bob", "Charlie"])
    election.cast_vote("V001", "Alice")
    election.cast_vote("V002", "Bob")
    election.cast_vote("V003", "Alice")
    print("Election Results:", election.get_results())
