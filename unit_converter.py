class UnitConverter:
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        # Convert everything to meters first
        to_meters = {
            "m": 1.0,
            "km": 1000.0,
            "cm": 0.01,
            "mm": 0.001,
            "mi": 1609.34,
            "ft": 0.3048,
            "in": 0.0254
        }
        if from_unit not in to_meters or to_unit not in to_meters:
            raise ValueError("Invalid unit type for length.")
        
        meters = value * to_meters[from_unit]
        return meters / to_meters[to_unit]

    @staticmethod
    def convert_weight(value, from_unit, to_unit):
        # Convert everything to grams first
        to_grams = {
            "g": 1.0,
            "kg": 1000.0,
            "mg": 0.001,
            "lb": 453.592,
            "oz": 28.3495
        }
        if from_unit not in to_grams or to_unit not in to_grams:
            raise ValueError("Invalid unit type for weight.")
        
        grams = value * to_grams[from_unit]
        return grams / to_grams[to_unit]


if __name__ == "__main__":
    print("=== Unit Converter ===")
    print("1. Length (options: m, km, cm, mm, mi, ft, in)")
    print("2. Weight (options: g, kg, mg, lb, oz)")
    
    choice = input("Choose category (1 or 2): ").strip()
    try:
        val = float(input("Enter value to convert: "))
        f_unit = input("From unit: ").strip().lower()
        t_unit = input("To unit: ").strip().lower()

        if choice == "1":
            result = UnitConverter.convert_length(val, f_unit, t_unit)
            print(f"\nResult: {val} {f_unit} = {result:.4f} {t_unit}")
        elif choice == "2":
            result = UnitConverter.convert_weight(val, f_unit, t_unit)
            print(f"\nResult: {val} {f_unit} = {result:.4f} {t_unit}")
        else:
            print("Invalid category choice.")
    except ValueError as e:
        print(f"Error: {e}")
