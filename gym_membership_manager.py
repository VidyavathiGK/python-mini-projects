from datetime import date, timedelta


class Member:
    def __init__(self, member_id: str, name: str, plan: str, duration_days: int):
        self.member_id = member_id
        self.name = name
        self.plan = plan
        self.start_date = date.today()
        self.expiry_date = self.start_date + timedelta(days=duration_days)
        self.attendance_log: list[str] = []

    def is_active(self, check_date: date | None = None) -> bool:
        target = check_date or date.today()
        return target <= self.expiry_date

    def renew(self, extra_days: int) -> None:
        base = max(date.today(), self.expiry_date)
        self.expiry_date = base + timedelta(days=extra_days)


class GymManager:
    PLANS = {"monthly": 30, "quarterly": 90, "annual": 365}

    def __init__(self):
        self.members: dict[str, Member] = {}

    def register_member(self, member_id: str, name: str, plan: str) -> Member:
        plan_key = plan.lower().strip()
        if plan_key not in self.PLANS:
            raise ValueError(f"Unknown plan '{plan}'. Choose from {list(self.PLANS.keys())}.")
        member = Member(member_id, name, plan_key, self.PLANS[plan_key])
        self.members[member_id] = member
        return member

    def check_in(self, member_id: str) -> str:
        member = self.members.get(member_id)
        if not member:
            return "Member not found."
        if not member.is_active():
            return f"Access denied for {member.name}: Membership expired on {member.expiry_date}."
        today_str = date.today().isoformat()
        member.attendance_log.append(today_str)
        return f"Welcome {member.name}! Checked in on {today_str} (Valid until {member.expiry_date})."


if __name__ == "__main__":
    gym = GymManager()
    gym.register_member("M101", "Ananya", "quarterly")
    print(gym.check_in("M101"))
