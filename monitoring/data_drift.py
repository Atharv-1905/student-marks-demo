
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference = pd.DataFrame({
    "marks": [65, 70, 72, 75, 78, 80, 82, 85, 88, 90]
})

current = pd.DataFrame({
    "marks": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
})

report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data=reference,
    current_data=current
)

result.save_html("monitoring/reports/drift_report.html")

print("Data drift monitoring completed.")
print("Report saved to monitoring/reports/drift_report.html")
