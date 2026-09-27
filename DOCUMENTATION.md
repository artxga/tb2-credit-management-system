# Credit Management System - Documentación del Proyecto

Este proyecto es un **Sistema de Gestión de Créditos** implementado en Python. Está diseñado utilizando principios de Programación Orientada a Objetos (POO), incluyendo abstracción, herencia, encapsulamiento y polimorfismo. El sistema permite gestionar clientes (individuales o corporativos), solicitudes de crédito (personales, vehiculares e hipotecarios) y calcular cronogramas de pago utilizando el método de amortización francesa.

## Estructura del Proyecto

El código fuente está dividido en múltiples módulos, cada uno enfocado en una responsabilidad específica (Single Responsibility Principle):

- `main.py`: Punto de entrada de la aplicación.
- `console_menu.py`: Interfaz de línea de comandos (CLI) para la interacción con el usuario.
- `credit_manager.py`: Controlador principal que gestiona la lógica de negocio, clientes y solicitudes.
- Módulos de Modelos:
  - **Personas y Clientes**: `person.py`, `customer.py`, `individual_customer.py`, `corporate_customer.py`, `analyst.py`.
  - **Créditos**: `credit_application.py`, `personal_credit.py`, `vehicle_credit.py`, `mortgage_credit.py`.
  - **Pagos**: `payment_schedule.py`, `installment.py`.
- **Excepciones**: `invalid_data_exception.py`.

---

## Diagrama de Clases (Arquitectura Conceptual)

### 1. Jerarquía de Personas y Clientes
El sistema define una base abstracta para entidades que interactúan con el banco.

- **`Person` (Clase Abstracta)**: Define las propiedades básicas (`person_id`, `name`, `email`, `phone`).
  - **`Analyst`**: Hereda de `Person`. Representa a un empleado del banco encargado de evaluar créditos (incluye `employee_code` y `approval_limit`).
  - **`Customer`**: Hereda de `Person`. Representa a un cliente del banco. Añade `monthly_income` y `credit_history`. Valida que el ingreso no sea negativo.
    - **`IndividualCustomer`**: Hereda de `Customer`. Representa a una persona natural (añade `dni` y `workplace`). Valida que el DNI tenga 8 caracteres.
    - **`CorporateCustomer`**: Hereda de `Customer`. Representa a una entidad corporativa (añade `ruc`, `company_name`, `years_in_operation`). Valida que el RUC tenga 11 caracteres.

### 2. Jerarquía de Solicitudes de Crédito
Las solicitudes de crédito manejan su propio riesgo a través de polimorfismo.

- **`CreditApplication` (Clase Abstracta)**: Contiene la información general de una solicitud (`application_id`, `customer`, `amount`, `months`, `tea`, `status`, `schedule`). Contiene el método abstracto `evaluate_risk()`.
  - **`PersonalCredit`**: Préstamo personal. 
    - *Regla de Aprobación*: El ingreso mensual del cliente debe ser $\ge 2000$ y la cuota estimada debe ser menor al $40\%$ de sus ingresos mensuales.
  - **`VehicleCredit`**: Préstamo vehicular.
    - *Regla de Aprobación*: La cuota inicial (`down_payment`) debe ser al menos el $20\%$ del valor del vehículo, y el monto del préstamo no debe superar la diferencia.
  - **`MortgageCredit`**: Préstamo hipotecario.
    - *Regla de Aprobación*: El plazo máximo es de 300 meses y el monto del préstamo no puede exceder el $90\%$ del valor de la propiedad.

### 3. Sistema de Pagos y Amortización
- **`PaymentSchedule`**: Gestiona el cronograma de pagos. Implementa el **Sistema de Amortización Francés** (cuotas fijas). Convierte la Tasa Efectiva Anual (TEA) a Tasa Efectiva Mensual (TEM) para los cálculos.
- **`Installment`**: Representa una cuota mensual individual. Contiene número de cuota, capital (principal), interés, seguro, monto total a pagar y saldo restante.

### 4. Gestión y Control
- **`CreditManager`**: Mantiene en memoria las listas de clientes (`_customers`) y solicitudes de crédito (`_applications`). Expone métodos para agregar clientes, agregar solicitudes, evaluar solicitudes por ID y listar solicitudes según su estado.
- **`ConsoleMenu`**: Provee el menú de consola que permite al usuario registrar datos de prueba, crear aplicaciones de crédito, evaluarlas y listar las aplicaciones aprobadas.

---

## Flujo de Trabajo y Cálculos Financieros

### Sistema de Amortización Francesa
El método `calculate_amortization` dentro de `PaymentSchedule` aplica la siguiente lógica matemática:

1. **Conversión de Tasa**:
   $\text{TEM} = (1 + \text{TEA})^{(1/12)} - 1$

2. **Cálculo de Cuota Fija** (Fórmula de Anualidad):
   $C = M \times \frac{\text{TEM} \times (1 + \text{TEM})^n}{(1 + \text{TEM})^n - 1}$
   *(Donde $C$ es la cuota fija, $M$ es el monto del préstamo y $n$ es el número de meses)*.

3. **Desglose Mensual**:
   - $\text{Interés Mensual} = \text{Saldo Anterior} \times \text{TEM}$
   - $\text{Capital (Amortización)} = \text{Cuota Fija} - \text{Interés Mensual}$
   - $\text{Nuevo Saldo} = \text{Saldo Anterior} - \text{Capital}$

### Estados de una Solicitud
Una solicitud de crédito (`CreditApplication`) transita por los siguientes estados (`status`):
- `PENDING`: Estado inicial al crear la solicitud.
- `APPROVED`: Asignado si el método `evaluate_risk()` (específico de cada tipo de crédito) retorna verdadero. En este estado, se genera el cronograma de pagos.
- `REJECTED`: Asignado si la evaluación de riesgo falla.

## Excepciones y Validación de Datos
El sistema utiliza una excepción personalizada llamada **`InvalidDataException`** para encapsular errores de lógica de negocio y validación, como:
- Ingresos mensuales negativos.
- DNI con longitud distinta de 8 caracteres.
- RUC con longitud distinta de 11 caracteres.
- Monto o meses de crédito menores o iguales a cero.

## Ejecución del Sistema
Para iniciar la aplicación interactiva, se debe ejecutar el archivo principal:
```bash
python main.py
```

El menú provee las siguientes opciones interactivas:
1. **Register Test Customer**: Instancia y guarda un `IndividualCustomer` de prueba.
2. **Create Personal Credit App**: Toma el primer cliente registrado y le crea una solicitud de `PersonalCredit`.
3. **Evaluate Application**: Solicita un ID de aplicación (ej. `APP-100`) y evalúa sus reglas de riesgo. Si es aprobada, genera su cronograma.
4. **List Approved Applications**: Lista el resumen y los cronogramas de pagos de las solicitudes que tienen estado `APPROVED`.
5. **Exit**: Termina la ejecución.
