#!/usr/bin/env python3
"""
🚀 AFFORDABLE MS OFFICE TRAINING - From Ksh 2,999
Professional Microsoft Office Certification • WhatsApp-First Enrollment
YAHOO EMAIL VERSION - OPTIMIZED WITH RECONNECTION
"""

import smtplib
import time
import os
import sys
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from colorama import init, Fore

init(autoreset=True)

# ========== CONFIGURATION ==========
SENDER_EMAIL = "fawcetteugene@yahoo.com"
APP_PASSWORD = ""  # Yahoo App Password
WHATSAPP_NUMBER = "+254794689731"

# Yahoo SMTP Settings
YAHOO_SMTP_SERVER = "smtp.mail.yahoo.com"
YAHOO_SMTP_PORT = 587

# AFFORDABLE MS Office Training Packages - UPDATED WITH KENYAN PRICING
PACKAGES = {
    "excel_basic": {
        "name": "EXCEL ESSENTIALS",
        "price": "Ksh 2,999",
        "duration": "2 Weeks",
        "delivery": "Certificate in 14 Days",
        "features": [
            "Basic Formulas & Functions",
            "Data Entry & Formatting",
            "Simple Charts & Graphs",
            "Budget & Expense Tracking",
            "Basic Data Analysis",
            "Free Templates"
        ],
        "color": "#1D6F42",  # Excel green
        "icon": "📊"
    },
    "word_basic": {
        "name": "WORD FOR BEGINNERS",
        "price": "Ksh 2,999",
        "duration": "10 Days",
        "delivery": "Certificate in 10 Days",
        "features": [
            "Document Creation & Formatting",
            "Letter & CV Writing",
            "Basic Mail Merge",
            "Report & Assignment Formatting",
            "Spelling & Grammar Tools",
            "Free CV Templates"
        ],
        "color": "#2B579A",  # Word blue
        "icon": "📝"
    },
    "powerpoint_basic": {
        "name": "POWERPOINT BASICS",
        "price": "Ksh 2,999",
        "duration": "10 Days",
        "delivery": "Certificate in 10 Days",
        "features": [
            "Basic Presentation Creation",
            "Slide Design & Layouts",
            "Simple Animations",
            "Photo & Text Slides",
            "Business & School Presentations",
            "Free Presentation Templates"
        ],
        "color": "#D24726",  # PowerPoint orange
        "icon": "📽️"
    },
    "office_bundle": {
        "name": "3-IN-1 OFFICE BUNDLE",
        "price": "Ksh 6,999",
        "duration": "4 Weeks",
        "delivery": "Complete Certification",
        "features": [
            "Excel, Word & PowerPoint Basics",
            "Office Integration Skills",
            "Real Project Portfolio",
            "Email & PDF Skills",
            "Job Search Preparation",
            "FREE Job Placement Support"
        ],
        "color": "#737373",  # Office gray
        "icon": "🏢"
    },
    "excel_advanced": {
        "name": "EXCEL ADVANCED",
        "price": "Ksh 4,999",
        "duration": "3 Weeks",
        "delivery": "Advanced Certificate",
        "features": [
            "Advanced Formulas & Functions",
            "PivotTables & Data Analysis",
            "Dashboard Creation",
            "Business Reports Automation",
            "Data Visualization",
            "FREE Practice Datasets"
        ],
        "color": "#0B5E20",  # Darker green
        "icon": "📈"
    }
}

# Target Audience for MS Office Training
TARGET_AUDIENCES = [
    {"icon": "👨‍🎓", "name": "College Students", "benefit": "Assignments & research projects"},
    {"icon": "👩‍💼", "name": "Job Seekers", "benefit": "CV enhancement & job applications"},
    {"icon": "👨‍💻", "name": "Freelancers", "benefit": "Client document services"},
    {"icon": "👩‍🏫", "name": "Teachers", "benefit": "Teaching materials & reports"},
    {"icon": "👨‍🌾", "name": "Small Business Owners", "benefit": "Business records & invoices"},
    {"icon": "👩‍⚕️", "name": "Healthcare Workers", "benefit": "Patient records & reports"}
]

# Success Stories - Updated for affordability
SUCCESS_STORIES = [
    {
        "name": "Nairobi Student",
        "result": "Got internship with skills",
        "quote": "Excel skills helped me create better reports for my internship application!",
        "avatar": "🎓"
    },
    {
        "name": "Mombasa Job Seeker",
        "result": "Landed office job",
        "quote": "Word formatting skills made my CV stand out from 200+ applicants",
        "avatar": "💼"
    },
    {
        "name": "Kisumu Business Owner",
        "result": "Organized business records",
        "quote": "Now I track my sales and expenses efficiently with Excel",
        "avatar": "📊"
    }
]

# Kenyan Market Stats for MS Office Skills
MARKET_STATS = [
    {"value": "92%", "label": "of Office Jobs Need MS Office", "icon": "💼"},
    {"value": "60%", "label": "Increase in Job Interviews", "icon": "📈"},
    {"value": "3x", "label": "Better Job Opportunities", "icon": "💰"}
]
# ===================================

def print_banner():
    """Display professional banner"""
    print(f"{Fore.CYAN}{'='*80}")
    print(f"{Fore.YELLOW}🚀 AFFORDABLE MS OFFICE TRAINING FOR KENYANS")
    print(f"{Fore.CYAN}{'='*80}")
    print(f"{Fore.WHITE}WhatsApp-First Enrollment • From Ksh 2,999 • Evening & Weekend Classes")
    print(f"{Fore.WHITE}📧 Using: Yahoo Business Email • ⏰ Timing: 5s between emails, 4min break + reconnect after 10")
    print(f"{Fore.WHITE}💰 Packages: From {PACKAGES['excel_basic']['price']} to {PACKAGES['office_bundle']['price']}")
    print(f"{Fore.CYAN}{'='*80}")

def load_emails(limit=100):
    """Load emails from file with validation"""
    if not os.path.exists('emails.txt'):
        print(f"{Fore.RED}❌ 'emails.txt' not found!")
        print(f"{Fore.YELLOW}💡 Creating sample emails.txt with 5 test emails...")
        sample_emails = [
            "test1@example.com",
            "test2@example.com",
            "test3@example.com",
            "test4@example.com",
            "test5@example.com"
        ]
        with open('emails.txt', 'w') as f:
            f.write('\n'.join(sample_emails))
        print(f"{Fore.GREEN}✅ Created emails.txt with {len(sample_emails)} test emails")
        return sample_emails[:limit]
    
    with open('emails.txt', 'r') as f:
        emails = []
        for line in f:
            email = line.strip()
            if email and '@' in email and '.' in email:
                emails.append(email)
    
    print(f"{Fore.GREEN}✅ Loaded {len(emails)} valid email addresses")
    return emails[:limit]

def remove_sent_email(email):
    """Remove sent email from list and log it"""
    try:
        with open('emails.txt', 'r') as f:
            emails = [line.strip() for line in f if line.strip()]
        
        if email in emails:
            emails.remove(email)
            with open('emails.txt', 'w') as f:
                f.write('\n'.join(emails))
            
            # Log sent email
            with open('sent_emails.log', 'a') as log_file:
                log_file.write(f"{datetime.now()}: {email}\n")
                
    except Exception as e:
        print(f"{Fore.YELLOW}⚠️ Note: Could not update emails.txt: {e}")

def create_html_email():
    """Create high-conversion HTML email for AFFORDABLE MS Office Training"""
    whatsapp_msg = f"Hi%2C%20I%20saw%20your%20affordable%20MS%20Office%20training%20from%20Ksh%202%2C999.%20Please%20share%20more%20information."
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={whatsapp_msg}"
    
    # Random success story
    story = random.choice(SUCCESS_STORIES)
    
    # Today + 5 days for limited offer (extended for affordability)
    offer_expiry = (datetime.now() + timedelta(days=5)).strftime("%B %d")
    
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affordable MS Office Training | From Ksh 2,999 | WhatsApp {WHATSAPP_NUMBER}</title>
    <style>
        :root {{
            --primary: #2B579A;
            --secondary: #1D6F42;
            --accent: #D24726;
            --dark: #1e293b;
            --light: #f8fafc;
            --whatsapp: #25D366;
            --whatsapp-dark: #128C7E;
            --affordable: #FF6B35;
        }}
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: var(--dark);
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .email-container {{
            max-width: 650px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }}
        
        /* Header */
        .header {{
            background: linear-gradient(135deg, #FF6B35 0%, #2B579A 100%);
            color: white;
            padding: 50px 30px;
            text-align: center;
            position: relative;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path fill="rgba(255,255,255,0.1)" d="M30,30 Q50,10 70,30 T90,30 Q70,50 90,70 T90,90 Q70,70 50,90 T30,90 Q10,70 30,50 T10,30 Q30,10 30,30Z"/></svg>');
            background-size: 60px;
            opacity: 0.1;
        }}
        
        .header h1 {{
            font-family: 'Poppins', sans-serif;
            font-size: 36px;
            font-weight: 800;
            margin-bottom: 15px;
            line-height: 1.2;
            position: relative;
            z-index: 1;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .header-tagline {{
            font-size: 18px;
            opacity: 0.95;
            margin-bottom: 25px;
            font-weight: 400;
            position: relative;
            z-index: 1;
        }}
        
        .affordable-badge {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 16px;
            margin: 15px 0;
            position: relative;
            z-index: 1;
            animation: pulse 2s infinite;
        }}
        
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        
        /* Price Comparison */
        .price-comparison {{
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            padding: 30px;
            margin: 20px;
            border-radius: 15px;
            border: 2px dashed #f59e0b;
            text-align: center;
        }}
        
        .price-comparison h3 {{
            font-family: 'Poppins', sans-serif;
            color: #92400e;
            margin-bottom: 15px;
            font-size: 22px;
        }}
        
        .price-grid {{
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            gap: 20px;
            align-items: center;
            max-width: 400px;
            margin: 0 auto;
        }}
        
        .old-price {{
            text-align: right;
            color: #64748b;
        }}
        
        .old-price span {{
            text-decoration: line-through;
            font-size: 20px;
            font-weight: 600;
        }}
        
        .vs {{
            font-size: 24px;
            font-weight: 800;
            color: #d97706;
        }}
        
        .new-price {{
            text-align: left;
            color: var(--affordable);
        }}
        
        .new-price span {{
            font-size: 28px;
            font-weight: 800;
        }}
        
        .savings {{
            grid-column: 1 / -1;
            background: var(--affordable);
            color: white;
            padding: 10px;
            border-radius: 10px;
            font-weight: 700;
            margin-top: 10px;
        }}
        
        /* Stats Section */
        .stats-section {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            padding: 40px 30px;
            background: white;
        }}
        
        .stat-card {{
            background: #f8fafc;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid #e2e8f0;
            transition: all 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
            border-color: var(--affordable);
            box-shadow: 0 10px 25px rgba(255, 107, 53, 0.1);
        }}
        
        .stat-icon {{
            font-size: 32px;
            margin-bottom: 15px;
            display: block;
        }}
        
        .stat-number {{
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            font-weight: 800;
            color: var(--affordable);
            margin-bottom: 8px;
            line-height: 1;
        }}
        
        .stat-label {{
            color: #64748b;
            font-size: 14px;
            font-weight: 500;
            line-height: 1.4;
        }}
        
        /* Main CTA Button */
        .main-cta {{
            padding: 50px 30px;
            text-align: center;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-bottom: 3px solid var(--affordable);
        }}
        
        .cta-button {{
            display: inline-flex;
            align-items: center;
            gap: 15px;
            background: var(--whatsapp);
            color: white;
            padding: 22px 45px;
            border-radius: 50px;
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            text-decoration: none;
            font-size: 20px;
            margin: 15px 0;
            transition: all 0.3s ease;
            box-shadow: 0 15px 30px rgba(37, 211, 102, 0.3);
            border: 3px solid rgba(255, 255, 255, 0.3);
            animation: ctaPulse 2s infinite;
        }}
        
        @keyframes ctaPulse {{
            0% {{ box-shadow: 0 15px 30px rgba(37, 211, 102, 0.3); }}
            50% {{ box-shadow: 0 15px 40px rgba(37, 211, 102, 0.5); }}
            100% {{ box-shadow: 0 15px 30px rgba(37, 211, 102, 0.3); }}
        }}
        
        .cta-button:hover {{
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 25px 50px rgba(37, 211, 102, 0.4);
            background: var(--whatsapp-dark);
        }}
        
        .cta-subtitle {{
            color: #64748b;
            font-size: 16px;
            margin-top: 20px;
            margin-bottom: 10px;
            font-weight: 500;
        }}
        
        /* Payment Options */
        .payment-options {{
            background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
            padding: 30px;
            margin: 20px;
            border-radius: 15px;
            border: 2px solid #22c55e;
            text-align: center;
        }}
        
        .payment-options h3 {{
            font-family: 'Poppins', sans-serif;
            color: #166534;
            margin-bottom: 15px;
            font-size: 22px;
        }}
        
        .payment-methods {{
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 20px;
        }}
        
        .payment-method {{
            background: white;
            padding: 15px 25px;
            border-radius: 10px;
            border: 2px solid #86efac;
            font-weight: 600;
            color: #166534;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        /* Target Audience Grid */
        .audience-section {{
            padding: 50px 30px;
            background: white;
        }}
        
        .section-title {{
            text-align: center;
            margin-bottom: 30px;
        }}
        
        .section-title h2 {{
            font-family: 'Poppins', sans-serif;
            font-size: 28px;
            font-weight: 700;
            color: var(--dark);
            margin-bottom: 10px;
            position: relative;
            display: inline-block;
        }}
        
        .section-title h2::after {{
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, var(--affordable), var(--primary));
            border-radius: 2px;
        }}
        
        .section-title p {{
            color: #64748b;
            font-size: 16px;
            margin-top: 20px;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .audience-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        
        .audience-card {{
            background: #f8fafc;
            padding: 25px;
            border-radius: 15px;
            border: 2px solid #e2e8f0;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .audience-card:hover {{
            border-color: var(--affordable);
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255, 107, 53, 0.1);
        }}
        
        .audience-icon {{
            font-size: 40px;
            margin-bottom: 15px;
            display: block;
        }}
        
        .audience-card h3 {{
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: var(--dark);
            margin-bottom: 8px;
        }}
        
        .audience-card p {{
            color: #64748b;
            font-size: 14px;
            line-height: 1.5;
        }}
        
        /* Packages */
        .packages-section {{
            padding: 50px 30px;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        }}
        
        .packages-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}
        
        .package-card {{
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border: 2px solid transparent;
            position: relative;
        }}
        
        .package-card:hover {{
            transform: translateY(-8px);
            border-color: var(--affordable);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.12);
        }}
        
        .package-popular {{
            position: absolute;
            top: 20px;
            right: -30px;
            background: var(--affordable);
            color: white;
            padding: 8px 40px;
            font-size: 12px;
            font-weight: 700;
            transform: rotate(45deg);
            z-index: 1;
        }}
        
        .package-header {{
            padding: 30px 25px;
            color: white;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .package-header::after {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        }}
        
        .package-icon {{
            font-size: 40px;
            margin-bottom: 15px;
            display: block;
            position: relative;
            z-index: 1;
        }}
        
        .package-name {{
            font-family: 'Poppins', sans-serif;
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }}
        
        .package-price {{
            font-size: 32px;
            font-weight: 800;
            margin: 15px 0;
            position: relative;
            z-index: 1;
            letter-spacing: -1px;
        }}
        
        .package-duration {{
            font-size: 14px;
            opacity: 0.9;
            font-weight: 500;
            background: rgba(255,255,255,0.2);
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            position: relative;
            z-index: 1;
        }}
        
        .package-features {{
            padding: 25px;
        }}
        
        .feature-item {{
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            padding: 12px;
            background: #f8fafc;
            border-radius: 10px;
            transition: all 0.2s ease;
        }}
        
        .feature-item:hover {{
            background: #e2e8f0;
            transform: translateX(5px);
        }}
        
        .feature-check {{
            width: 22px;
            height: 22px;
            background: var(--affordable);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            margin-right: 12px;
            flex-shrink: 0;
            font-size: 12px;
            font-weight: bold;
        }}
        
        /* Offer Banner */
        .offer-banner {{
            background: linear-gradient(90deg, #FF6B35, #2B579A);
            color: white;
            padding: 25px;
            text-align: center;
            margin: 40px 30px;
            border-radius: 15px;
            animation: pulse 2s infinite;
            box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
            position: relative;
            overflow: hidden;
        }}
        
        .offer-banner::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 20px 20px;
            opacity: 0.2;
        }}
        
        .offer-banner h3 {{
            font-family: 'Poppins', sans-serif;
            font-size: 24px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            position: relative;
            z-index: 1;
        }}
        
        .offer-banner p {{
            font-size: 16px;
            opacity: 0.95;
            position: relative;
            z-index: 1;
        }}
        
        /* Testimonials */
        .testimonials-section {{
            padding: 50px 30px;
            background: white;
        }}
        
        .testimonial-card {{
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            padding: 40px;
            border-radius: 20px;
            border: 2px solid #bae6fd;
            position: relative;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .testimonial-card::before {{
            content: '"';
            position: absolute;
            top: 20px;
            left: 30px;
            font-size: 80px;
            font-family: 'Poppins', sans-serif;
            color: var(--affordable);
            opacity: 0.1;
            line-height: 1;
        }}
        
        .testimonial-text {{
            font-size: 18px;
            line-height: 1.6;
            color: var(--dark);
            margin-bottom: 30px;
            position: relative;
            z-index: 1;
            font-style: italic;
        }}
        
        .testimonial-author {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        
        .author-avatar {{
            width: 50px;
            height: 50px;
            background: var(--affordable);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 24px;
            flex-shrink: 0;
        }}
        
        .author-info h4 {{
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: var(--dark);
            margin-bottom: 5px;
        }}
        
        .author-info p {{
            color: var(--secondary);
            font-size: 14px;
            font-weight: 500;
        }}
        
        /* WhatsApp CTA Section */
        .whatsapp-section {{
            padding: 60px 30px;
            background: linear-gradient(135deg, var(--secondary) 0%, var(--affordable) 100%);
            color: white;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .whatsapp-section::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 30px 30px;
            opacity: 0.1;
        }}
        
        .whatsapp-title {{
            font-family: 'Poppins', sans-serif;
            font-size: 36px;
            font-weight: 800;
            margin-bottom: 20px;
            position: relative;
            z-index: 1;
        }}
        
        .whatsapp-subtitle {{
            font-size: 18px;
            opacity: 0.9;
            margin-bottom: 30px;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
            position: relative;
            z-index: 1;
        }}
        
        .whatsapp-button {{
            display: inline-flex;
            align-items: center;
            gap: 15px;
            background: white;
            color: var(--affordable);
            padding: 22px 45px;
            border-radius: 50px;
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            text-decoration: none;
            font-size: 20px;
            margin: 20px 0;
            transition: all 0.3s ease;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            position: relative;
            z-index: 1;
            animation: ctaPulse 2s infinite;
        }}
        
        .whatsapp-button:hover {{
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3);
            background: #f8fafc;
        }}
        
        .whatsapp-benefits {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 40px 0;
            position: relative;
            z-index: 1;
        }}
        
        .benefit-item {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .benefit-item:hover {{
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-5px);
        }}
        
        .benefit-icon {{
            font-size: 32px;
            margin-bottom: 15px;
            display: block;
        }}
        
        .benefit-text {{
            font-size: 16px;
            font-weight: 500;
        }}
        
        .whatsapp-number-box {{
            margin-top: 40px;
            padding: 25px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            display: inline-block;
            position: relative;
            z-index: 1;
        }}
        
        .whatsapp-number-label {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 10px;
            display: block;
        }}
        
        .whatsapp-number {{
            font-size: 28px;
            font-weight: 800;
            color: white;
            text-decoration: none;
            display: block;
            margin-bottom: 10px;
        }}
        
        .whatsapp-number-note {{
            font-size: 14px;
            opacity: 0.8;
        }}
        
        /* Footer */
        .footer {{
            background: var(--dark);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }}
        
        .footer-logo {{
            font-family: 'Poppins', sans-serif;
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}
        
        .footer-tagline {{
            color: #94a3b8;
            margin-bottom: 30px;
            line-height: 1.6;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
            font-size: 16px;
        }}
        
        .copyright {{
            font-size: 14px;
            color: #64748b;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            line-height: 1.5;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 28px;
            }}
            
            .header-tagline {{
                font-size: 16px;
            }}
            
            .whatsapp-title {{
                font-size: 28px;
            }}
            
            .whatsapp-subtitle {{
                font-size: 16px;
            }}
            
            .audience-grid,
            .packages-grid {{
                grid-template-columns: 1fr;
            }}
            
            .stats-section {{
                grid-template-columns: 1fr 1fr;
            }}
            
            .cta-button,
            .whatsapp-button {{
                padding: 18px 35px;
                font-size: 18px;
            }}
            
            .whatsapp-benefits {{
                grid-template-columns: 1fr;
            }}
            
            .price-grid {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
            
            .old-price, .new-price {{
                text-align: center;
            }}
            
            .vs {{
                display: none;
            }}
        }}
        
        @media (max-width: 480px) {{
            .header,
            .stats-section,
            .main-cta,
            .audience-section,
            .packages-section,
            .testimonials-section,
            .whatsapp-section,
            .footer {{
                padding: 30px 20px;
            }}
            
            .offer-banner,
            .payment-options,
            .price-comparison {{
                margin: 30px 20px;
                padding: 20px;
            }}
            
            .stats-section {{
                grid-template-columns: 1fr;
            }}
            
            .package-price {{
                font-size: 28px;
            }}
            
            .whatsapp-number {{
                font-size: 22px;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="header">
            <h1>AFFORDABLE MS OFFICE TRAINING 🇰🇪</h1>
            <div class="header-tagline">
                From Ksh 2,999 • WhatsApp Enrollment • Certificate in 10-14 Days
            </div>
            <div class="affordable-badge">
                ⚡ Most Affordable in Kenya • M-Pesa Payment • Free Templates
            </div>
        </div>
        
        <!-- Price Comparison -->
        <div class="price-comparison">
            <h3>💰 COMPARE & SAVE 60%+</h3>
            <div class="price-grid">
                <div class="old-price">
                    <div>Others Charge:</div>
                    <span>Ksh 8,999+</span>
                </div>
                <div class="vs">VS</div>
                <div class="new-price">
                    <div>Our Price:</div>
                    <span>Ksh 2,999</span>
                </div>
                <div class="savings">
                    You Save: Ksh 6,000+ (60%+ Savings)!
                </div>
            </div>
        </div>
        
        <!-- Stats -->
        <div class="stats-section">
            {"".join([f"""
            <div class="stat-card">
                <div class="stat-icon">{stat['icon']}</div>
                <div class="stat-number">{stat['value']}</div>
                <div class="stat-label">{stat['label']}</div>
            </div>
            """ for stat in MARKET_STATS])}
        </div>
        
        <!-- Main CTA -->
        <div class="main-cta">
            <a href="{whatsapp_url}" class="cta-button" target="_blank">
                <span>💬</span>
                <span>WHATSAPP FOR 50% DISCOUNT</span>
                <span>→</span>
            </a>
            <div class="cta-subtitle">
                Fast response (typically 10 minutes) • M-Pesa Payment • Installments Available
            </div>
        </div>
        
        <!-- Payment Options -->
        <div class="payment-options">
            <h3>💳 FLEXIBLE PAYMENT OPTIONS</h3>
            <p>Choose what works for you:</p>
            <div class="payment-methods">
                <div class="payment-method">
                    <span>📱</span>
                    <span>Full M-Pesa Payment</span>
                </div>
                <div class="payment-method">
                    <span>💰</span>
                    <span>50% Deposit, 50% Later</span>
                </div>
                <div class="payment-method">
                    <span>📅</span>
                    <span>Weekly Installments</span>
                </div>
            </div>
        </div>
        
        <!-- Limited Offer Banner -->
        <div class="offer-banner">
            <h3>🎁 SUPER AFFORDABLE OFFER</h3>
            <p>First 100 students get: 50% OFF + FREE Practice Materials + Certificate Fee Included<br>
            Offer ends: {offer_expiry} • WhatsApp us now to claim!</p>
        </div>
        
        <!-- Target Audiences -->
        <div class="audience-section">
            <div class="section-title">
                <h2>Perfect for Every Kenyan</h2>
                <p>Designed for students, job seekers, and working professionals</p>
            </div>
            
            <div class="audience-grid">
                {"".join([f"""
                <div class="audience-card">
                    <div class="audience-icon">{audience['icon']}</div>
                    <h3>{audience['name']}</h3>
                    <p>{audience['benefit']}</p>
                </div>
                """ for audience in TARGET_AUDIENCES])}
            </div>
        </div>
        
        <!-- Packages -->
        <div class="packages-section">
            <div class="section-title">
                <h2>AFFORDABLE MS OFFICE PACKAGES</h2>
                <p>Quality training at prices every Kenyan can afford</p>
            </div>
            
            <div class="packages-grid">
                {"".join([f"""
                <div class="package-card">
                    {"<div class='package-popular'>MOST POPULAR</div>" if pkg_key == "excel_basic" else ""}
                    {"<div class='package-popular'>BEST VALUE</div>" if pkg_key == "office_bundle" else ""}
                    <div class="package-header" style="background: {pkg['color']};">
                        <span class="package-icon">{pkg['icon']}</span>
                        <div class="package-name">{pkg['name']}</div>
                        <div class="package-price">{pkg['price']}</div>
                        <div class="package-duration">{pkg['duration']} • {pkg['delivery']}</div>
                    </div>
                    <div class="package-features">
                        {"".join([f"""
                        <div class="feature-item">
                            <div class="feature-check">✓</div>
                            <div>{feature}</div>
                        </div>
                        """ for feature in pkg['features']])}
                    </div>
                </div>
                """ for pkg_key, pkg in PACKAGES.items()])}
            </div>
        </div>
        
        <!-- Testimonials -->
        <div class="testimonials-section">
            <div class="section-title">
                <h2>Success Stories from Kenyans</h2>
                <p>Real results from people who started with basic skills</p>
            </div>
            
            <div class="testimonial-card">
                <div class="testimonial-text">
                    {story['quote']}
                </div>
                <div class="testimonial-author">
                    <div class="author-avatar">{story['avatar']}</div>
                    <div class="author-info">
                        <h4>{story['name']}</h4>
                        <p>{story['result']}</p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- WhatsApp Section -->
        <div class="whatsapp-section">
            <h2 class="whatsapp-title">READY TO LEARN AT AFFORDABLE PRICES?</h2>
            <div class="whatsapp-subtitle">
                Chat directly with our training team on WhatsApp. Get course details, payment plans, and start learning.
            </div>
            
            <a href="{whatsapp_url}" class="whatsapp-button" target="_blank">
                <span>📱</span>
                <span>CLICK TO CHAT ON WHATSAPP NOW</span>
                <span>💬</span>
            </a>
            
            <div class="whatsapp-benefits">
                <div class="benefit-item">
                    <div class="benefit-icon">⚡</div>
                    <div class="benefit-text">Fast Response (Typically 10 minutes)</div>
                </div>
                <div class="benefit-item">
                    <div class="benefit-icon">🎯</div>
                    <div class="benefit-text">50% Discount for First 100</div>
                </div>
                <div class="benefit-item">
                    <div class="benefit-icon">🇰🇪</div>
                    <div class="benefit-text">Kenyan Trainers Understanding Local Needs</div>
                </div>
            </div>
            
            <div class="whatsapp-number-box">
                <div class="whatsapp-number-label">WHATSAPP TRAINING SUPPORT</div>
                <a href="https://wa.me/{WHATSAPP_NUMBER}" class="whatsapp-number" target="_blank">{WHATSAPP_NUMBER}</a>
                <div class="whatsapp-number-note">Tap number to save contact • Click to chat directly</div>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <div class="footer-logo">
                <span>🎓</span>
                <span>Affordable MS Office Training</span>
            </div>
            
            <div class="footer-tagline">
                Making quality Microsoft Office training accessible and affordable for every Kenyan.
            </div>
            
            <div class="copyright">
                © {datetime.now().year} Affordable MS Office Training Center<br>
                Professional Skills • Affordable Prices • WhatsApp: {WHATSAPP_NUMBER}<br>
                Serving: Students • Job Seekers • Working Professionals • Business Owners
            </div>
        </div>
    </div>
</body>
</html>"""

def create_text_email():
    """Create high-conversion text version for AFFORDABLE MS Office Training"""
    whatsapp_msg = f"Hi%2C%20I%20saw%20your%20affordable%20MS%20Office%20training%20from%20Ksh%202%2C999.%20Please%20share%20more%20information."
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={whatsapp_msg}"
    
    return f"""AFFORDABLE MS OFFICE TRAINING 🇰🇪
==========================================

🎓 PROFESSIONAL MS OFFICE SKILLS - FROM KSH 2,999 ONLY!

💰 COMPARE & SAVE 60%+:
Others Charge: Ksh 8,999+
Our Price: Ksh 2,999
YOU SAVE: Ksh 6,000+ (60%+ Savings!)

📊 WHY MS OFFICE SKILLS MATTER:
• 92% of Office Jobs Need MS Office Skills
• 60% Increase in Job Interview Chances  
• 3x Better Job Opportunities with MS Office Skills

🎯 PERFECT FOR EVERY KENYAN:
• College Students: Assignments & research projects
• Job Seekers: CV enhancement & job applications
• Freelancers: Client document services
• Teachers: Teaching materials & reports
• Small Business Owners: Business records & invoices
• Healthcare Workers: Patient records & reports

💰 AFFORDABLE MS OFFICE PACKAGES:

📊 EXCEL ESSENTIALS - Ksh 2,999 (MOST POPULAR)
2 Weeks • Certificate in 14 Days
✓ Basic Formulas & Functions
✓ Data Entry & Formatting
✓ Simple Charts & Graphs
✓ Budget & Expense Tracking
✓ Basic Data Analysis
✓ Free Templates

📝 WORD FOR BEGINNERS - Ksh 2,999
10 Days • Certificate in 10 Days
✓ Document Creation & Formatting
✓ Letter & CV Writing
✓ Basic Mail Merge
✓ Report & Assignment Formatting
✓ Spelling & Grammar Tools
✓ Free CV Templates

📽️ POWERPOINT BASICS - Ksh 2,999
10 Days • Certificate in 10 Days
✓ Basic Presentation Creation
✓ Slide Design & Layouts
✓ Simple Animations
✓ Photo & Text Slides
✓ Business & School Presentations
✓ Free Presentation Templates

🏢 3-IN-1 OFFICE BUNDLE - Ksh 6,999 (BEST VALUE)
4 Weeks • Complete Certification
✓ Excel, Word & PowerPoint Basics
✓ Office Integration Skills
✓ Real Project Portfolio
✓ Email & PDF Skills
✓ Job Search Preparation
✓ FREE Job Placement Support

📈 EXCEL ADVANCED - Ksh 4,999
3 Weeks • Advanced Certificate
✓ Advanced Formulas & Functions
✓ PivotTables & Data Analysis
✓ Dashboard Creation
✓ Business Reports Automation
✓ Data Visualization
✓ FREE Practice Datasets

📈 SUCCESS STORY:
"Excel skills helped me create better reports for my internship application! 
I got selected over 50 other applicants because of my skills."
— Nairobi Student

🎁 SUPER AFFORDABLE OFFER:
First 100 students get:
• 50% DISCOUNT on any package
• FREE Practice Materials
• Certificate Fee INCLUDED
• FREE Templates & Resources
• Offer ends in 5 days

💳 FLEXIBLE PAYMENT OPTIONS:
1. Full M-Pesa Payment
2. 50% Deposit, 50% Later
3. Weekly Installments Available
4. Group Discounts (2+ people)

📱 GET CERTIFIED IN 3 SIMPLE STEPS:
1. WhatsApp us at {WHATSAPP_NUMBER} for FREE consultation
2. Choose your affordable MS Office package
3. Start learning immediately (Evening & Weekend classes)

💬 WHY WHATSAPP FOR AFFORDABLE TRAINING:
• Fast response (typically 10 minutes)
• Direct communication with trainers
• Easy payment via M-Pesa
• Flexible installment plans
• Schedule that fits your time

👉 CLICK TO CHAT NOW: {whatsapp_url}

✅ WHAT YOU GET (ALL PACKAGES):
• Professional MS Office certificate
• Hands-on practical exercises
• Downloadable templates
• Free practice materials
• Email support
• Certificate of completion
• Evening & weekend class options

⚡ Most Affordable in Kenya • M-Pesa Payment • Free Templates • Installments Available

==========================================
Affordable MS Office Training Center • WhatsApp: {WHATSAPP_NUMBER}
© {datetime.now().year} • Quality Training at Affordable Prices
Serving: Students • Job Seekers • Working Professionals • Business Owners"""

def send_campaign():
    """Send high-conversion AFFORDABLE MS Office training campaign"""
    emails = load_emails(100)
    
    if not emails:
        print(f"{Fore.RED}❌ No valid emails found in 'emails.txt'!")
        return
    
    print_banner()
    print(f"\n{Fore.YELLOW}🚀 AFFORDABLE MS OFFICE TRAINING CAMPAIGN:")
    print(f"{Fore.CYAN}{'='*80}")
    print(f"{Fore.WHITE}Theme:           {Fore.GREEN}Affordable MS Office Training for Kenyans")
    print(f"{Fore.WHITE}Primary CTA:     {Fore.YELLOW}WhatsApp for 50% Discount")
    print(f"{Fore.WHITE}Packages:        {Fore.YELLOW}{PACKAGES['excel_basic']['price']} • {PACKAGES['word_basic']['price']} • {PACKAGES['powerpoint_basic']['price']} • {PACKAGES['office_bundle']['price']}")
    print(f"{Fore.WHITE}Offer:           {Fore.GREEN}50% OFF + Free Materials (First 100 students)")
    print(f"{Fore.WHITE}WhatsApp:        {Fore.CYAN}{WHATSAPP_NUMBER}")
    print(f"{Fore.WHITE}Recipients:      {Fore.YELLOW}{len(emails)}")
    print(f"{Fore.WHITE}Timing:          {Fore.GREEN}5s between emails • 4min break + reconnect after 10 emails")
    print(f"{Fore.CYAN}{'='*80}")
    
    # High-conversion subject lines
    subjects = [
        f"🎓 MS Office Training | From Ksh 2,999 Only | 50% OFF WhatsApp {WHATSAPP_NUMBER}",
        f"Affordable Computer Skills | MS Office from Ksh 2,999 | Get Certificate",
        f"🚀 Learn MS Office Today | Most Affordable in Kenya | Ksh 2,999"
    ]
    
    print(f"\n{Fore.YELLOW}📝 SELECT SUBJECT LINE:")
    for i, subj in enumerate(subjects, 1):
        print(f"{Fore.CYAN}{i}. {Fore.WHITE}{subj}")
    
    choice = input(f"\n{Fore.GREEN}Choose option (1-3) [1]: ").strip()
    subject = subjects[0]
    if choice in ['1', '2', '3']:
        subject = subjects[int(choice)-1]
    
    print(f"\n{Fore.YELLOW}✅ Selected: {Fore.CYAN}{subject}")
    
    confirm = input(f"\n{Fore.GREEN}Send campaign to {len(emails)} recipients? (y/N): ").lower()
    if confirm != 'y':
        print(f"{Fore.YELLOW}Cancelled")
        return
    
    success = 0
    failed = 0
    
    print(f"\n{Fore.YELLOW}⏳ Starting campaign in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"{Fore.CYAN}Starting in {i} seconds...{' ' * 20}", end='\r')
        time.sleep(1)
    print(f"{Fore.GREEN}✅ Starting campaign!{' ' * 30}")
    
    print(f"\n{Fore.YELLOW}📤 SENDING AFFORDABLE TRAINING CAMPAIGN...")
    print(f"{Fore.CYAN}{'='*80}")
    
    # Initialize connection
    server = None
    
    for i, recipient in enumerate(emails, 1):
        try:
            # Reconnect after every 10 emails
            if (i - 1) % 10 == 0 or server is None:
                # Close existing connection if any
                if server is not None:
                    try:
                        server.quit()
                    except:
                        pass
                
                # Wait 4 minutes if not first batch
                if i > 1:
                    print(f"\n{Fore.YELLOW}⏳ Sent {i-1} emails. Waiting 4 minutes, then reconnecting...")
                    for minute in range(4, 0, -1):
                        for second in range(60, 0, -1):
                            print(f"{Fore.CYAN}Reconnecting in {minute:02d}:{second:02d}...{' ' * 20}", end='\r')
                            time.sleep(1)
                    print(f"{Fore.GREEN}✅ Reconnecting to Yahoo SMTP...{' ' * 30}")
                
                # Connect to Yahoo SMTP
                try:
                    print(f"{Fore.BLUE}🔗 Connecting to Yahoo SMTP server...")
                    server = smtplib.SMTP(YAHOO_SMTP_SERVER, YAHOO_SMTP_PORT)
                    server.starttls()
                    server.login(SENDER_EMAIL, APP_PASSWORD.replace(" ", ""))
                    print(f"{Fore.GREEN}✅ Connected to Yahoo successfully")
                except Exception as e:
                    print(f"{Fore.RED}❌ Connection failed: {e}")
                    print(f"{Fore.YELLOW}💡 Yahoo SMTP Troubleshooting:")
                    print(f"{Fore.YELLOW}  1. Ensure 'Less Secure Apps' is enabled")
                    print(f"{Fore.YELLOW}  2. Verify App Password is correct (no spaces)")
                    print(f"{Fore.YELLOW}  3. Check internet connection")
                    return
            
            # Create email
            msg = MIMEMultipart('alternative')
            msg['From'] = f"Affordable MS Office Training <{SENDER_EMAIL}>"
            msg['To'] = recipient
            msg['Subject'] = subject
            msg['Reply-To'] = SENDER_EMAIL
            msg['X-Priority'] = '1'
            msg['X-MSMail-Priority'] = 'High'
            msg['Importance'] = 'high'
            
            # Add text and HTML versions
            text_part = MIMEText(create_text_email(), 'plain')
            html_part = MIMEText(create_html_email(), 'html')
            
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Send email
            server.send_message(msg)
            remove_sent_email(recipient)
            
            progress = (i / len(emails)) * 100
            bar_length = 40
            filled = int(bar_length * progress / 100)
            bar = f"{Fore.GREEN}█" * filled + f"{Fore.CYAN}░" * (bar_length - filled)
            
            print(f"{Fore.GREEN}[{i:03d}/{len(emails):03d}] ✓ {recipient[:30]:<30} {bar} {progress:.1f}%")
            success += 1
            
            # Wait 5 seconds before next email
            if i < len(emails):
                time.sleep(5)  # 5 second wait
                
        except Exception as e:
            print(f"{Fore.RED}[{i:03d}] ✗ {recipient[:30]:<30} Failed: {str(e)[:50]}...")
            failed += 1
            
            # Wait 5 seconds on error
            if i < len(emails):
                time.sleep(5)  # 5 second wait on error
    
    # Close final connection
    if server is not None:
        try:
            server.quit()
        except:
            pass
    
    # Results
    print(f"\n{Fore.CYAN}{'='*80}")
    print(f"{Fore.GREEN}✅ AFFORDABLE MS OFFICE TRAINING CAMPAIGN COMPLETED!")
    print(f"{Fore.CYAN}{'='*80}")
    print(f"{Fore.WHITE}Successfully sent: {Fore.GREEN}{success}")
    print(f"{Fore.WHITE}Failed:            {Fore.RED}{failed}")
    print(f"{Fore.WHITE}Total recipients:  {Fore.YELLOW}{len(emails)}")
    print(f"{Fore.WHITE}Success rate:      {Fore.GREEN}{(success/len(emails)*100):.1f}%")
    print(f"{Fore.WHITE}Sending speed:     {Fore.CYAN}5 seconds between emails")
    print(f"{Fore.WHITE}Reconnection:      {Fore.GREEN}4 minutes + reconnect after every 10 emails")
    print(f"{Fore.CYAN}{'='*80}")
    
    if success > 0:
        # Project conversions - Higher for affordable pricing
        expected_responses = int(success * 0.25)  # 25% response rate for affordable training
        expected_students = int(expected_responses * 0.45)  # 45% enrollment rate
        
        # Distribution based on package preferences
        excel_students = int(expected_students * 0.35)  # 35% choose Excel Essentials
        word_students = int(expected_students * 0.25)  # 25% choose Word Basics
        powerpoint_students = int(expected_students * 0.15)  # 15% choose PowerPoint Basics
        bundle_students = int(expected_students * 0.20)  # 20% choose 3-in-1 Bundle
        advanced_students = int(expected_students * 0.05)  # 5% choose Excel Advanced
        
        excel_rev = excel_students * 2999
        word_rev = word_students * 2999
        powerpoint_rev = powerpoint_students * 2999
        bundle_rev = bundle_students * 6999
        advanced_rev = advanced_students * 4999
        total_rev = excel_rev + word_rev + powerpoint_rev + bundle_rev + advanced_rev
        
        print(f"\n{Fore.MAGENTA}💰 AFFORDABLE TRAINING REVENUE PROJECTION:")
        print(f"{Fore.CYAN}{'-'*80}")
        print(f"{Fore.WHITE}Expected WhatsApp inquiries: {Fore.GREEN}{expected_responses}")
        print(f"{Fore.WHITE}Expected enrolled students:  {Fore.YELLOW}{expected_students}")
        print(f"{Fore.WHITE}Excel Essentials students:  {Fore.GREEN}{excel_students} × Ksh 2,999 = Ksh {excel_rev:,}")
        print(f"{Fore.WHITE}Word Basics students:       {Fore.CYAN}{word_students} × Ksh 2,999 = Ksh {word_rev:,}")
        print(f"{Fore.WHITE}PowerPoint Basics students: {Fore.YELLOW}{powerpoint_students} × Ksh 2,999 = Ksh {powerpoint_rev:,}")
        print(f"{Fore.WHITE}3-in-1 Bundle students:     {Fore.MAGENTA}{bundle_students} × Ksh 6,999 = Ksh {bundle_rev:,}")
        print(f"{Fore.WHITE}Excel Advanced students:    {Fore.GREEN}{advanced_students} × Ksh 4,999 = Ksh {advanced_rev:,}")
        print(f"{Fore.CYAN}{'-'*80}")
        print(f"{Fore.WHITE}Total Potential Revenue:     {Fore.GREEN}Ksh {total_rev:,}")
        
        # Additional services revenue (materials, certificates)
        addon_rev = expected_students * 500  # Additional affordable materials
        total_with_addons = total_rev + addon_rev
        
        print(f"{Fore.WHITE}Additional materials:        {Fore.YELLOW}Ksh {addon_rev:,}")
        print(f"{Fore.CYAN}{'-'*80}")
        print(f"{Fore.WHITE}TOTAL POTENTIAL:            {Fore.GREEN}Ksh {total_with_addons:,}")
        print(f"{Fore.CYAN}{'='*80}")
    
    # Save campaign report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"affordable_ms_office_campaign_{timestamp}.txt"
    
    with open(report_file, 'w') as f:
        f.write(f"🎓 Affordable MS Office Training Campaign Report - {datetime.now()}\n")
        f.write("="*60 + "\n")
        f.write(f"Subject: {subject}\n")
        f.write(f"Recipients: {len(emails)}\n")
        f.write(f"Successful: {success}\n")
        f.write(f"Failed: {failed}\n")
        f.write(f"Success Rate: {(success/len(emails)*100):.1f}%\n")
        f.write(f"WhatsApp Number: {WHATSAPP_NUMBER}\n")
        f.write(f"Packages: {PACKAGES['excel_basic']['price']} • {PACKAGES['word_basic']['price']} • {PACKAGES['powerpoint_basic']['price']} • {PACKAGES['office_bundle']['price']}\n")
        f.write(f"Offer: 50% OFF + Free Materials (First 100 students)\n")
        f.write(f"Sending Speed: 5 seconds between emails\n")
        f.write(f"Reconnection: 4 minutes + reconnect after every 10 emails\n")
        f.write(f"\n📊 Affordable Training Features:\n")
        f.write("- 5 Affordable MS Office packages from Ksh 2,999\n")
        f.write("- Professional certification\n")
        f.write("- Evening & weekend classes\n")
        f.write("- Flexible M-Pesa payment plans\n")
        f.write("- Free templates & materials\n")
        f.write("- Kenyan trainers\n")
    
    print(f"\n{Fore.GREEN}📄 Campaign report saved: {report_file}")
    
    print(f"\n{Fore.GREEN}🎯 IMMEDIATE ACTIONS FOR AFFORDABLE TRAINING CONVERSION:")
    print(f"{Fore.WHITE}1. 📱 Keep WhatsApp active 7AM-10PM for student inquiries")
    print(f"{Fore.WHITE}2. ⚡ Respond within 10 minutes for best enrollment")
    print(f"{Fore.WHITE}3. 💰 Highlight the 60%+ savings compared to competitors")
    print(f"{Fore.WHITE}4. 📱 Share M-Pesa payment details immediately")
    print(f"{Fore.WHITE}5. 🎓 Send free sample lessons to interested students")
    print(f"{Fore.WHITE}6. 👥 Offer group discounts for 2+ students")
    print(f"{Fore.WHITE}7. 📅 Schedule flexible class times for students")

def main():
    """Main menu - Optimized for AFFORDABLE MS Office Training"""
    while True:
        print_banner()
        
        print(f"\n{Fore.YELLOW}🚀 AFFORDABLE MS OFFICE TRAINING MENU:")
        print(f"{Fore.CYAN}1. {Fore.WHITE}Send Affordable Training Campaign")
        print(f"{Fore.CYAN}2. {Fore.WHITE}Preview Training Email Design")
        print(f"{Fore.CYAN}3. {Fore.WHITE}Manage Contact List")
        print(f"{Fore.CYAN}4. {Fore.WHITE}Test Yahoo Connection")
        print(f"{Fore.CYAN}5. {Fore.WHITE}View Campaign Statistics")
        print(f"{Fore.CYAN}6. {Fore.WHITE}View Package Details")
        print(f"{Fore.CYAN}7. {Fore.WHITE}Exit Program")
        
        choice = input(f"\n{Fore.GREEN}Select option (1-7): ").strip()
        
        if choice == "1":
            send_campaign()
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        elif choice == "2":
            html = create_html_email()
            filename = f"affordable_ms_office_preview_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
            with open(filename, 'w') as f:
                f.write(html)
            print(f"\n{Fore.GREEN}✅ Affordable training preview saved: '{filename}'")
            print(f"{Fore.YELLOW}💡 Open in browser - 5 packages from Ksh 2,999")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        elif choice == "3":
            emails = load_emails(100)
            print(f"\n{Fore.CYAN}📊 CONTACT LIST MANAGEMENT: {len(emails)} addresses")
            if emails:
                print(f"{Fore.YELLOW}First 15 contacts:")
                for i, email in enumerate(emails[:15], 1):
                    print(f"{Fore.WHITE}{i:2d}. {email}")
                if len(emails) > 15:
                    print(f"{Fore.YELLOW}... and {len(emails)-15} more")
                
                print(f"\n{Fore.CYAN}Options:")
                print(f"{Fore.WHITE}1. Remove duplicates")
                print(f"{Fore.WHITE}2. Export contacts")
                print(f"{Fore.WHITE}3. Back to menu")
                
                sub_choice = input(f"\n{Fore.GREEN}Select: ").strip()
                if sub_choice == "1":
                    unique_emails = list(set(emails))
                    with open('emails.txt', 'w') as f:
                        f.write('\n'.join(unique_emails))
                    print(f"{Fore.GREEN}✅ Removed duplicates. Now {len(unique_emails)} unique contacts.")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        elif choice == "4":
            print(f"\n{Fore.YELLOW}🔧 TESTING YAHOO CONNECTION...")
            try:
                server = smtplib.SMTP(YAHOO_SMTP_SERVER, YAHOO_SMTP_PORT)
                server.starttls()
                server.login(SENDER_EMAIL, APP_PASSWORD.replace(" ", ""))
                server.quit()
                print(f"{Fore.GREEN}✅ Connection successful!")
                
                # Test content creation
                print(f"{Fore.YELLOW}📧 Testing email content...")
                print(f"{Fore.GREEN}✅ HTML email: {len(create_html_email())} characters")
                print(f"{Fore.GREEN}✅ Text email: {len(create_text_email())} characters")
                
            except Exception as e:
                print(f"{Fore.RED}❌ Failed: {e}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        elif choice == "5":
            print(f"\n{Fore.YELLOW}📈 CAMPAIGN STATISTICS:")
            print(f"{Fore.CYAN}{'='*80}")
            print(f"{Fore.WHITE}Primary Contact:   {Fore.GREEN}WhatsApp: {WHATSAPP_NUMBER}")
            print(f"{Fore.WHITE}Training Packages: {Fore.YELLOW}{PACKAGES['excel_basic']['price']} • {PACKAGES['word_basic']['price']} • {PACKAGES['powerpoint_basic']['price']} • {PACKAGES['office_bundle']['price']}")
            print(f"{Fore.WHITE}Special Offer:     {Fore.GREEN}50% OFF + Free Materials (First 100 students)")
            print(f"{Fore.WHITE}Sending Speed:     {Fore.CYAN}5 seconds between emails")
            print(f"{Fore.WHITE}Reconnection:      {Fore.GREEN}4 minutes + reconnect after 10 emails")
            
            if os.path.exists('sent_emails.log'):
                with open('sent_emails.log', 'r') as f:
                    sent_count = len(f.readlines())
                print(f"{Fore.WHITE}Total sent:        {Fore.GREEN}{sent_count}")
            
            print(f"{Fore.CYAN}{'='*80}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        elif choice == "6":
            print(f"\n{Fore.YELLOW}💰 AFFORDABLE MS OFFICE PACKAGE DETAILS:")
            print(f"{Fore.CYAN}{'='*80}")
            for pkg_key, pkg in PACKAGES.items():
                print(f"\n{Fore.GREEN}{pkg['icon']} {pkg['name']} - {pkg['price']}")
                print(f"{Fore.YELLOW}{pkg['duration']} • {pkg['delivery']}")
                for feature in pkg['features']:
                    print(f"  ✓ {feature}")
            print(f"\n{Fore.MAGENTA}🎯 INCLUDED IN ALL AFFORDABLE PACKAGES:")
            print(f"{Fore.WHITE}• Professional MS Office certificate")
            print(f"{Fore.WHITE}• Hands-on practical exercises")
            print(f"{Fore.WHITE}• Downloadable templates & resources")
            print(f"{Fore.WHITE}• Free practice materials")
            print(f"{Fore.WHITE}• Email support")
            print(f"{Fore.WHITE}• Certificate of completion")
            print(f"{Fore.WHITE}• Evening & weekend class options")
            print(f"{Fore.WHITE}• Flexible M-Pesa payment plans")
            print(f"{Fore.WHITE}• Group discounts available")
            print(f"{Fore.CYAN}{'='*80}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        elif choice == "7":
            print(f"\n{Fore.CYAN}👋 Thank you for using Affordable MS Office Training!")
            print(f"{Fore.GREEN}📱 WhatsApp Training: {WHATSAPP_NUMBER}")
            print(f"{Fore.YELLOW}🎓 Chat with us for affordable MS Office skills from Ksh 2,999!")
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}❌ Invalid option. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠ Program interrupted")
        print(f"{Fore.GREEN}WhatsApp: {WHATSAPP_NUMBER}")
        print(f"{Fore.YELLOW}Affordable MS Office training from {PACKAGES['excel_basic']['price']}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}")
