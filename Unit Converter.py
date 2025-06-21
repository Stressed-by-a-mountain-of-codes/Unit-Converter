class UnitConverter:
    def __init__(self):
        self.length = {
            'm': 1.0,
            'km': 1000.0,
            'mile': 1609.34,
            'ft': 0.3048
        }
        self.weight = {
            'g': 1.0,
            'kg': 1000.0,
            'lb': 453.592,
            'oz': 28.3495
        }
        self.time = {
            's': 1.0,
            'min': 60.0,
            'h': 3600.0,
            'day': 86400.0
        }

    def convert(self, value, from_unit, to_unit):
        category = None
        for unit_map in (self.length, self.weight, self.time):
            if from_unit in unit_map and to_unit in unit_map:
                category = unit_map
                break
        if not category:
            raise ValueError('Incompatible units')
        return value * category[from_unit] / category[to_unit]

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'C':
            return value * 9 / 5 + 32 if to_unit == 'F' else value + 273.15
        if from_unit == 'F':
            return (value - 32) * 5 / 9 if to_unit == 'C' else (value - 32) * 5 / 9 + 273.15
        if from_unit == 'K':
            return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9 / 5 + 32
        raise ValueError('Invalid temperature units')


if __name__ == '__main__':
    uc = UnitConverter()
    mode = input('Mode (length/weight/time/temp): ').strip().lower()
    if mode == 'temp':
        val = float(input('Value: '))
        from_u = input('From (C/F/K): ').strip().upper()
        to_u = input('To (C/F/K): ').strip().upper()
        result = uc.convert_temperature(val, from_u, to_u)
    else:
        val = float(input('Value: '))
        from_u = input('From unit: ').strip().lower()
        to_u = input('To unit: ').strip().lower()
        result = uc.convert(val, from_u, to_u)
    print(f'Result: {result}')
