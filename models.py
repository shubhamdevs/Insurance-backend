from datetime import datetime, timedelta
import random
import string

class PolicyHolder:
    """Model for policy holder data"""
    def __init__(self, policy_id, customer_name, email, phone):
        self.policy_id = policy_id
        self.customer_name = customer_name
        self.email = email
        self.phone = phone
        self.registration_date = datetime.utcnow().isoformat()

class RealTimeData:
    """Generate real-time insurance data"""
    
    @staticmethod
    def get_policy_status(policy_id):
        """Get real-time policy status"""
        statuses = ['Active', 'Pending', 'Suspended', 'Expired']
        status = random.choice(['Active', 'Active', 'Active'])  # 66% chance of Active
        
        return {
            'policy_id': policy_id,
            'status': status,
            'days_remaining': random.randint(30, 365),
            'last_updated': datetime.utcnow().isoformat(),
            'is_active': status == 'Active'
        }
    
    @staticmethod
    def get_claims_balance(policy_id):
        """Get real-time claims information"""
        total_benefits = 500000
        claims_made = random.randint(0, 150000)
        remaining_balance = total_benefits - claims_made
        
        return {
            'policy_id': policy_id,
            'total_benefits': total_benefits,
            'claims_made_ytd': claims_made,
            'remaining_balance': remaining_balance,
            'remaining_percentage': round((remaining_balance / total_benefits) * 100, 2),
            'last_claim_date': (datetime.utcnow() - timedelta(days=random.randint(1, 120))).isoformat(),
            'timestamp': datetime.utcnow().isoformat()
        }
    
    @staticmethod
    def get_premium_info(policy_id):
        """Get real-time premium payment information"""
        premium_amount = random.choice([1200, 1800, 2400, 3000, 3600])
        days_until_due = random.randint(1, 30)
        payment_status = 'Paid' if random.random() > 0.1 else 'Pending'
        
        return {
            'policy_id': policy_id,
            'annual_premium': premium_amount,
            'monthly_premium': round(premium_amount / 12, 2),
            'payment_status': payment_status,
            'days_until_next_payment': days_until_due,
            'next_due_date': (datetime.utcnow() + timedelta(days=days_until_due)).isoformat(),
            'last_payment_date': (datetime.utcnow() - timedelta(days=random.randint(1, 30))).isoformat(),
            'payment_method': random.choice(['Credit Card', 'Bank Transfer', 'Check']),
            'timestamp': datetime.utcnow().isoformat()
        }
    
    @staticmethod
    def get_coverage_details(policy_id):
        """Get real-time coverage details (not in policy document)"""
        return {
            'policy_id': policy_id,
            'coverages': [
                {
                    'type': 'Medical Coverage',
                    'limit': 500000,
                    'used': random.randint(0, 100000),
                    'remaining': 500000 - random.randint(0, 100000),
                    'status': 'Active'
                },
                {
                    'type': 'Accidental Death & Dismemberment',
                    'limit': 250000,
                    'used': 0,
                    'remaining': 250000,
                    'status': 'Active'
                },
                {
                    'type': 'Critical Illness',
                    'limit': 100000,
                    'used': random.randint(0, 50000),
                    'remaining': 100000 - random.randint(0, 50000),
                    'status': 'Active'
                },
                {
                    'type': 'Disability Income',
                    'limit': 5000,
                    'used': 0,
                    'remaining': 5000,
                    'status': 'Active'
                }
            ],
            'timestamp': datetime.utcnow().isoformat()
        }
    
    @staticmethod
    def get_beneficiary_info(policy_id):
        """Get beneficiary information (not in policy document)"""
        beneficiaries = [
            {
                'name': 'Jane Doe',
                'relationship': 'Spouse',
                'percentage': 50,
                'contact': 'jane.doe@email.com'
            },
            {
                'name': 'John Doe Jr.',
                'relationship': 'Child',
                'percentage': 25,
                'contact': 'john.jr@email.com'
            },
            {
                'name': 'Mary Smith',
                'relationship': 'Mother',
                'percentage': 25,
                'contact': 'mary.smith@email.com'
            }
        ]
        
        return {
            'policy_id': policy_id,
            'beneficiary_count': len(beneficiaries),
            'beneficiaries': beneficiaries,
            'timestamp': datetime.utcnow().isoformat()
        }
    
    @staticmethod
    def get_medical_history(policy_id):
        """Get medical history summary (not in policy document)"""
        conditions = ['Diabetes', 'Hypertension', 'Asthma', 'None']
        selected_conditions = random.sample(conditions, random.randint(1, 2))
        
        return {
            'policy_id': policy_id,
            'pre_existing_conditions': selected_conditions if 'None' not in selected_conditions else [],
            'waiting_period_months': 12 if selected_conditions and 'None' not in selected_conditions else 0,
            'waiting_period_end_date': (datetime.utcnow() + timedelta(days=365)).isoformat() if selected_conditions and 'None' not in selected_conditions else None,
            'health_screening_required': 'Yes' if len(selected_conditions) > 1 else 'No',
            'last_health_checkup': (datetime.utcnow() - timedelta(days=random.randint(30, 365))).isoformat(),
            'timestamp': datetime.utcnow().isoformat()
        }
