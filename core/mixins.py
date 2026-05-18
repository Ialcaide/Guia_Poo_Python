import json

class PromedioMixin:
    def calculate_average(self, grades: list) -> float:
        if not grades:
            return 0.0
        return round(sum(grades) / len(grades), 2)


class ValidacionMixin:
    def validate_email(self, email: str):
        if "@" not in email or ".com" not in email:
            raise ValueError("Email invalido")

    def validate_age(self, age: int):
        if age < 18:
            raise ValueError("La edad debe ser mayor o igual a 18")


class ExportarMixin:
    def export_json(self, data: dict) -> str:
        return json.dumps(data, indent=2)

    def export_csv(self, data: dict) -> str:
        keys   = ",".join(data.keys())
        values = ",".join(str(v) for v in data.values())
        return f"{keys}\n  {values}"