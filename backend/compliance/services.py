from datetime import date, timedelta


def calculate_employee_compliance(employee):
    checks = []

    if not employee.is_sponsored:
        return {
            "score": 100,
            "completed": 0,
            "total": 0,
            "checks": [],
            "status": "not_applicable"
        }
    
    checks.extend([
        {
            "key": "visa_type_present",
            "label": "Visa type recorded",
            "complete": bool(employee.visa_type),
            "severity": "high",
        },
        {
            "key": "visa_expiry_date_present",
            "label": "Visa expiry date recorded",
            "complete": employee.visa_expiry_date is not None,
            "severity": "high",
        },
        {
            "key": "right_to_work_check_date_present",
            "label": "Right-to-work check date recorded",
            "complete": employee.right_to_work_check_date is not None,
            "severity": "high",
        },
        {
            "key": "cos_number_present",
            "label": "Certificate of Sponsorship number recorded",
            "complete": bool(employee.cos_number),
            "severity": "high",
        },
        {
            "key": "soc_code_present",
            "label": "SOC code recorded",
            "complete": bool(employee.soc_code),
            "severity": "medium",
        },
        {
            "key": "job_title_present",
            "label": "Job title recorded",
            "complete": bool(employee.job_title),
            "severity": "medium",
        },
        {
            "key": "work_location_present",
            "label": "Work location recorded",
            "complete": bool(employee.work_location),
            "severity": "medium",
        },
        {
            "key": "salary_present",
            "label": "Salary recorded",
            "complete": employee.salary is not None,
            "severity": "high",
        },
        {
            "key": "weekly_hours_present",
            "label": "Weekly working hours recorded",
            "complete": employee.weekly_hours is not None,
            "severity": "medium",
        },
    ])

    if employee.visa_expiry_date:
        checks.append({
            "key": "visa_not_expiring_within_90_days",
            "label": "Visa is not expiring within 90 days",
            "complete": employee.visa_expiry_date > date.today() + timedelta(days=90),
            "severity": "high",
        })
    
    total = len(checks)
    completed = sum(1 for check in checks if check["complete"])
    score = round((completed / total * 100)) if total else 100

    if score == 100:
        status = "compliant"
    elif score >= 70:
        status = "needs_attention"
    else:
        status = "high_risk"
    
    return {
        "score": score,
        "completed": completed,
        "total": total,
        "checks": checks,
        "status": status
    }
