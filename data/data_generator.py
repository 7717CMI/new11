import pandas as pd
import random
import numpy as np

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define data pools
companies = [
    ("Coca-Cola Bottling Company UNITED", "Major independent Coca-Cola bottler handling beverage production, sales, marketing & distribution", "Food & Beverage"),
    ("PepsiCo, Inc.", "Leading U.S. food & beverage company with global brands; large U.S. footprint in manufacturing", "Food & Beverage / CPG"),
    ("Halliburton Company", "U.S. oilfield services & technology leader serving upstream energy operators", "Energy / Oil & Gas Services"),
    ("Kennametal Inc.", "U.S. manufacturer of tooling and industrial materials; operates smart factories", "Industrial Manufacturing"),
    ("Procter & Gamble", "Consumer goods corporation with global brands in beauty, healthcare, and household products", "Consumer Goods / CPG"),
    ("Johnson & Johnson", "Pharmaceutical and consumer healthcare company with medical devices division", "Healthcare / Pharmaceuticals"),
    ("Walmart Inc.", "Multinational retail corporation operating hypermarkets and grocery stores", "Retail / E-commerce"),
    ("Ford Motor Company", "Automotive manufacturer with global manufacturing and distribution", "Automotive / Manufacturing"),
    ("Delta Air Lines", "Major U.S. airline with global operations and extensive IT infrastructure", "Airlines / Transportation"),
    ("Bank of America", "Multinational investment bank and financial services company", "Financial Services / Banking"),
    ("Caterpillar Inc.", "Manufacturer of construction and mining equipment, engines, and turbines", "Heavy Equipment / Manufacturing"),
    ("General Electric", "Multinational conglomerate with aviation, healthcare, and power divisions", "Industrial Conglomerate"),
    ("3M Company", "Diversified technology company manufacturing industrial, safety and consumer products", "Industrial / Technology"),
    ("Honeywell International", "Technology and manufacturing company serving aerospace, building, and materials", "Aerospace / Technology"),
    ("Deere & Company", "Agricultural, construction, and forestry machinery manufacturer", "Agriculture / Manufacturing"),
    ("Lockheed Martin", "Aerospace, defense, security, and advanced technologies company", "Aerospace / Defense"),
    ("Starbucks Corporation", "Coffeehouse chain with global presence and digital transformation initiatives", "Food & Beverage / Retail"),
    ("CVS Health", "Healthcare company with retail pharmacy and healthcare services", "Healthcare / Retail"),
    ("Target Corporation", "General merchandise retailer with extensive supply chain operations", "Retail"),
    ("American Airlines Group", "Major U.S. airline with global operations", "Airlines / Transportation"),
    ("Chevron Corporation", "Integrated energy company in oil, gas, and renewable energy", "Energy / Oil & Gas"),
    ("Boeing Company", "Aerospace company manufacturing commercial airplanes and defense systems", "Aerospace / Defense"),
    ("Nike Inc.", "Athletic footwear and apparel company with global manufacturing", "Retail / Consumer Goods"),
    ("Goldman Sachs", "Investment banking and financial services company", "Financial Services / Investment Banking"),
    ("Pfizer Inc.", "Pharmaceutical corporation with research, development, and manufacturing", "Pharmaceuticals / Healthcare"),
    ("Cisco Systems", "Technology company specializing in networking hardware and software", "Technology / Networking"),
    ("Intel Corporation", "Semiconductor chip manufacturer with global operations", "Technology / Semiconductors"),
    ("Verizon Communications", "Telecommunications company providing wireless and wireline services", "Telecommunications"),
    ("Marriott International", "Hospitality company operating hotels and resorts worldwide", "Hospitality / Travel"),
    ("FedEx Corporation", "Logistics and transportation company with global delivery network", "Logistics / Transportation"),
]

locations = [
    ("Birmingham, AL", "Southeast U.S."),
    ("Purchase, NY", "Northeast U.S."),
    ("Houston, TX", "South Central U.S."),
    ("Pittsburgh, PA", "Northeast U.S."),
    ("Cincinnati, OH", "Midwest U.S."),
    ("New Brunswick, NJ", "Northeast U.S."),
    ("Bentonville, AR", "South Central U.S."),
    ("Dearborn, MI", "Midwest U.S."),
    ("Atlanta, GA", "Southeast U.S."),
    ("Charlotte, NC", "Southeast U.S."),
    ("Peoria, IL", "Midwest U.S."),
    ("Boston, MA", "Northeast U.S."),
    ("St. Paul, MN", "Midwest U.S."),
    ("Charlotte, NC", "Southeast U.S."),
    ("Moline, IL", "Midwest U.S."),
    ("Bethesda, MD", "Mid-Atlantic U.S."),
    ("Seattle, WA", "Pacific Northwest U.S."),
    ("Woonsocket, RI", "Northeast U.S."),
    ("Minneapolis, MN", "Midwest U.S."),
    ("Fort Worth, TX", "South Central U.S."),
    ("San Ramon, CA", "West Coast U.S."),
    ("Chicago, IL", "Midwest U.S."),
    ("Beaverton, OR", "Pacific Northwest U.S."),
    ("New York, NY", "Northeast U.S."),
    ("New York, NY", "Northeast U.S."),
    ("San Jose, CA", "West Coast U.S."),
    ("Santa Clara, CA", "West Coast U.S."),
    ("New York, NY", "Northeast U.S."),
    ("Bethesda, MD", "Mid-Atlantic U.S."),
    ("Memphis, TN", "South Central U.S."),
]

cloud_platforms = [
    "Microsoft Azure",
    "AWS (Amazon Web Services)",
    "Google Cloud Platform",
    "Multi-cloud (Azure + AWS)",
    "Multi-cloud (AWS + GCP)",
    "Microsoft Azure",
    "AWS (Amazon Web Services)",
]

license_ecosystems = [
    ["Microsoft 365", "SAP HANA", "Power Platform"],
    ["Microsoft 365", "SAP ERP", "Oracle Database"],
    ["Microsoft 365", "SAP S/4HANA"],
    ["Microsoft 365", "Oracle E-Business Suite", "IBM WebSphere"],
    ["Oracle Cloud", "SAP", "Microsoft"],
    ["Microsoft", "SAP", "IBM Mainframe"],
    ["AWS Services", "Microsoft 365", "Oracle"],
    ["Microsoft 365", "SAP", "Oracle Database"],
]

optimization_types = [
    "Both (Cloud FinOps + ELO)",
    "Cloud FinOps",
    "Enterprise License Optimization (ELO)",
    "Both (Cloud FinOps + ELO)",
]

pain_points = [
    "Need for scalable, cost-efficient infrastructure for high-volume SAP and automation at scale",
    "Managing massive data/analytics workloads and modernizing ERP; Need cost control & governance at scale",
    "Data-center exit & application migration at scale - cost, performance, governance, and licensing alignment needs",
    "Modernizing legacy ERP/network; Need agility/visibility for global manufacturing and planning",
    "Multi-cloud cost optimization and license compliance across distributed systems",
    "Managing legacy Oracle licenses while migrating to cloud; compliance and cost visibility gaps",
    "SAP licensing complexity during cloud transformation; need visibility into actual usage vs. entitlements",
    "Rising cloud costs post-migration; lack of granular cost allocation and chargeback mechanisms",
    "Oracle license audit risk; need comprehensive asset management and compliance tracking",
    "Hybrid infrastructure creating licensing grey areas between on-prem perpetual and cloud subscription models",
]

trigger_events = [
    "SAP HANA migration and scale-up on Azure",
    "Strategic Azure partnership to migrate data estate and SAP; Azure ML deployment in U.S. markets",
    "Strategic Azure migration with Accenture/Avanade; cloud-first operating model",
    "SAP-to-Azure migration; adoption of SAP IBP & Azure ML/IoT in smart factories",
    "Multi-cloud expansion for disaster recovery and workload optimization",
    "Oracle license renewal cycle; exploring license buyback and optimization strategies",
    "AWS Enterprise Agreement renewal; negotiating better rates based on commitment",
    "Microsoft EA renewal approaching; opportunity to rightsize M365 and Azure subscriptions",
    "Recent Oracle audit notice triggering compliance review and optimization initiative",
    "SAP S/4HANA migration project kickoff; re-evaluating license requirements",
]

stakeholders_pool = [
    ["CIO", "IT Infrastructure Lead", "Data & Analytics Director", "Finance Transformation Manager"],
    ["CIO", "VP Cloud Platforms", "Head of SAM/Procurement", "Finance IT Director"],
    ["CIO", "VP Digital/IT", "Head of Cloud Transformation", "Global Procurement (IT)"],
    ["CIO", "VP Enterprise Apps", "Head of Manufacturing IT/OT", "SAM Lead"],
    ["CFO", "VP IT Operations", "Enterprise Architect", "Procurement Director"],
]

decision_makers = [
    "CIO",
    "VP Cloud Platforms",
    "VP Digital",
    "VP Enterprise Applications",
    "CTO",
    "VP IT Operations",
    "Chief Technology Officer",
    "VP Infrastructure",
]

phone_prefixes = ["+1 (205)", "+1 (914)", "+1 (713)", "+1 (412)", "+1 (513)", "+1 (732)", "+1 (479)", "+1 (313)"]

def generate_customer_data(num_customers=30):
    """Generate synthetic customer intelligence data"""
    data = []

    for i in range(num_customers):
        company, overview, industry = companies[i % len(companies)]
        hq_city, region = locations[i % len(locations)]

        # Generate varied product offerings based on industry
        if "Food & Beverage" in industry or "CPG" in industry:
            product = "Manufacturing, distribution, supply chain management, retail execution, data & analytics"
        elif "Energy" in industry or "Oil & Gas" in industry:
            product = "Oilfield services, digital operations, subsurface software, enterprise applications"
        elif "Manufacturing" in industry:
            product = "Manufacturing operations, smart factory systems, supply chain, ERP systems"
        elif "Healthcare" in industry or "Pharmaceuticals" in industry:
            product = "Healthcare services, pharmaceutical R&D, medical devices, patient systems"
        elif "Retail" in industry:
            product = "Retail operations, e-commerce, supply chain, point-of-sale systems, analytics"
        elif "Financial" in industry or "Banking" in industry:
            product = "Financial services, trading platforms, risk management, customer banking systems"
        elif "Technology" in industry:
            product = "Product development, cloud services, R&D systems, enterprise platforms"
        elif "Aerospace" in industry or "Defense" in industry:
            product = "Aerospace systems, defense programs, manufacturing, supply chain"
        else:
            product = "Enterprise operations, digital transformation, IT infrastructure, analytics"

        cloud = random.choice(cloud_platforms)
        licenses = random.choice(license_ecosystems)
        opt_type = random.choice(optimization_types)

        # Generate optimization potential based on type
        if "Both" in opt_type:
            cloud_opt = random.randint(15, 28)
            elo_opt = random.randint(10, 20)
        elif "Cloud" in opt_type:
            cloud_opt = random.randint(18, 30)
            elo_opt = 0
        else:
            cloud_opt = 0
            elo_opt = random.randint(12, 22)

        pain = random.choice(pain_points)
        trigger = random.choice(trigger_events)
        stakeholders = random.choice(stakeholders_pool)
        decision_maker = random.choice(decision_makers)

        phone = f"{random.choice(phone_prefixes)} {random.randint(100, 999)}-{random.randint(1000, 9999)}"
        fax = f"{random.choice(phone_prefixes)} {random.randint(100, 999)}-{random.randint(1000, 9999)}"

        # Generate quantitative metrics
        # Annual IT spend based on company size
        annual_it_spend_m = random.randint(50, 500)  # Million USD

        # Current cloud spend (% of IT spend)
        cloud_spend_pct = random.uniform(0.15, 0.45)  # 15-45% of IT spend
        current_cloud_spend_m = round(annual_it_spend_m * cloud_spend_pct, 2)

        # Potential cloud savings
        potential_cloud_savings_m = round(current_cloud_spend_m * (cloud_opt / 100), 2)

        # License spend
        license_spend_m = round(annual_it_spend_m * random.uniform(0.20, 0.40), 2)  # 20-40% on licenses
        potential_license_savings_m = round(license_spend_m * (elo_opt / 100), 2)

        # Total potential savings
        total_potential_savings_m = round(potential_cloud_savings_m + potential_license_savings_m, 2)

        # Number of employees and IT team size
        num_employees = random.randint(5000, 150000)
        it_team_size = int(num_employees * random.uniform(0.02, 0.05))  # 2-5% of workforce

        # Infrastructure metrics
        num_vms = random.randint(500, 5000)
        num_servers_physical = random.randint(50, 800)
        num_databases = random.randint(20, 300)
        num_applications = random.randint(100, 1500)

        # License counts
        ms_licenses = random.randint(5000, num_employees)
        sap_licenses = random.randint(100, int(num_employees * 0.3))
        oracle_licenses = random.randint(50, int(num_employees * 0.2))

        # Cloud resource metrics
        if "Azure" in cloud:
            azure_vms = random.randint(200, 2000)
            azure_storage_tb = random.randint(50, 500)
            azure_monthly_spend_k = round(current_cloud_spend_m * 1000 / 12, 1)
        else:
            azure_vms = 0
            azure_storage_tb = 0
            azure_monthly_spend_k = 0

        if "AWS" in cloud:
            aws_ec2_instances = random.randint(200, 2000)
            aws_s3_storage_tb = random.randint(50, 500)
            aws_monthly_spend_k = round(current_cloud_spend_m * 1000 / 12, 1)
        else:
            aws_ec2_instances = 0
            aws_s3_storage_tb = 0
            aws_monthly_spend_k = 0

        if "GCP" in cloud:
            gcp_vms = random.randint(100, 1000)
            gcp_storage_tb = random.randint(30, 300)
            gcp_monthly_spend_k = round(current_cloud_spend_m * 1000 / 12, 1)
        else:
            gcp_vms = 0
            gcp_storage_tb = 0
            gcp_monthly_spend_k = 0

        # ROI metrics
        implementation_cost_k = random.randint(50, 300)  # Thousand USD
        monthly_savings_k = round(total_potential_savings_m * 1000 / 12, 1)
        roi_months = round(implementation_cost_k / monthly_savings_k, 1) if monthly_savings_k > 0 else 0

        # Engagement metrics
        last_contact_days = random.randint(1, 180)
        engagement_score = random.randint(1, 10)

        data.append({
            "Sr_No": i + 1,
            "Customer_Name": company,
            "Overview": overview,
            "Geographical_Presence": f"HQ: {hq_city}; operates across {region}",
            "Product_Offering": product,
            "Industry_Vertical": industry,
            "Cloud_Platforms": cloud,
            "License_Ecosystem": ", ".join(licenses),
            "Optimization_Type": opt_type,
            "Pain_Points": pain,
            "Trigger_Event": trigger,
            "Key_Stakeholders": ", ".join(stakeholders),
            "Cloud_Optimization_Potential": cloud_opt,
            "ELO_Optimization_Potential": elo_opt,
            "Total_Optimization_Potential": cloud_opt + elo_opt,
            "Decision_Maker": decision_maker,
            "Phone": phone,
            "Fax": fax,
            "Email": f"contact@{company.lower().replace(' ', '').replace(',', '').replace('.', '')[:20]}.com",
            "Website": f"www.{company.lower().replace(' ', '').replace(',', '').replace('.', '')[:20]}.com",

            # Quantitative Financial Metrics (in Millions USD)
            "Annual_IT_Spend_M": annual_it_spend_m,
            "Current_Cloud_Spend_M": current_cloud_spend_m,
            "Current_License_Spend_M": license_spend_m,
            "Potential_Cloud_Savings_M": potential_cloud_savings_m,
            "Potential_License_Savings_M": potential_license_savings_m,
            "Total_Potential_Savings_M": total_potential_savings_m,

            # Organization Metrics
            "Number_of_Employees": num_employees,
            "IT_Team_Size": it_team_size,

            # Infrastructure Metrics
            "Number_of_VMs": num_vms,
            "Physical_Servers": num_servers_physical,
            "Number_of_Databases": num_databases,
            "Number_of_Applications": num_applications,

            # License Counts
            "Microsoft_Licenses": ms_licenses,
            "SAP_Licenses": sap_licenses,
            "Oracle_Licenses": oracle_licenses,

            # Cloud Resource Metrics
            "Azure_VMs": azure_vms,
            "Azure_Storage_TB": azure_storage_tb,
            "Azure_Monthly_Spend_K": azure_monthly_spend_k,
            "AWS_EC2_Instances": aws_ec2_instances,
            "AWS_S3_Storage_TB": aws_s3_storage_tb,
            "AWS_Monthly_Spend_K": aws_monthly_spend_k,
            "GCP_VMs": gcp_vms,
            "GCP_Storage_TB": gcp_storage_tb,
            "GCP_Monthly_Spend_K": gcp_monthly_spend_k,

            # ROI Metrics (in Thousands USD)
            "Implementation_Cost_K": implementation_cost_k,
            "Monthly_Savings_K": monthly_savings_k,
            "ROI_Payback_Months": roi_months,

            # Engagement Metrics
            "Last_Contact_Days_Ago": last_contact_days,
            "Engagement_Score": engagement_score
        })

    return pd.DataFrame(data)

if __name__ == "__main__":
    # Generate data
    df = generate_customer_data(30)

    # Save to CSV
    df.to_csv("customers.csv", index=False)
    print(f"Generated {len(df)} customer records and saved to customers.csv")
    print(f"\nSample data:\n{df.head()}")
