import textwrap

def generate_proposal_idea(project_type, client_name, key_goals):
    """
    Simulates GigPilot AI generating a project proposal idea.
    """
    project_type_lower = project_type.lower()
    
    # --- AI Assistance Simulation ---
    # This section simulates the 'AI' processing input to structure the proposal.
    # In a real GigPilot, this would involve advanced NLP and LLMs.
    # Here, we use simple string matching and formatting to illustrate the concept.
    
    title = f"Öneri Taslağı: {client_name} için {project_type} Projesi"
    
    introduction = textwrap.dedent(f"""
    Sayın {client_name},
    
    Bu taslak, {project_type} projeniz için potansiyel bir yaklaşımı ve ana hatları sunmaktadır.
    Amacımız, hedeflerinize ulaşmanıza yardımcı olacak yenilikçi ve etkili bir çözüm sunmaktır.
    """)

    goals_section = f"\n### 1. Proje Hedefleri\n"
    goals_section += f"- Müşterinin ana hedefleri: {key_goals}\n"
    
    # The 'AI' adapts the goals section based on the project type.
    if "web sitesi" in project_type_lower or "website" in project_type_lower:
        goals_section += "- Modern, kullanıcı dostu ve mobil uyumlu bir arayüz oluşturmak.\n"
        goals_section += "- Marka kimliğini yansıtan estetik bir tasarım sağlamak.\n"
        goals_section += "- Belirtilen temel işlevsellikleri (örneğin, iletişim formu, ürün sergileme) entegre etmek.\n"
    elif "mobil uygulama" in project_type_lower or "mobile app" in project_type_lower:
        goals_section += "- Akıcı bir kullanıcı deneyimi sunan sezgisel bir mobil uygulama geliştirmek.\n"
        goals_section += "- iOS ve Android platformlarında sorunsuz çalışmayı sağlamak.\n"
        goals_section += "- Belirtilen temel mobil özelliklerini (örneğin, bildirimler, konum servisleri) entegre etmek.\n"
    else:
        goals_section += "- Belirtilen proje türüne özgü temel hedeflere ulaşmak.\n"

    scope_section = f"\n### 2. Proje Kapsamı (Önerilen)\n"
    scope_section += f"- Detaylı gereksinim analizi ve planlama.\n"
    scope_section += f"- {project_type} için UI/UX tasarımı ve prototipleme.\n"
    scope_section += f"- Geliştirme ve entegrasyon (belirtilen teknolojilerle).\n"
    scope_section += f"- Test ve kalite güvencesi.\n"
    scope_section += f"- Dağıtım ve lansman desteği.\n"

    next_steps = textwrap.dedent("""
    ### 3. Sonraki Adımlar
    
    Bu taslak, projenin başlangıç noktasıdır. Detaylı bir görüşme ile gereksinimleri daha derinlemesine
    anlayarak size özel, kesin bir teklif hazırlayabiliriz.
    """)

    conclusion = textwrap.dedent("""
    Saygılarımızla,
    [Freelancer Adınız/Şirketiniz]
    """)

    full_proposal = f"{title}\n{'=' * len(title)}\n"
    full_proposal += introduction
    full_proposal += goals_section
    full_proposal += scope_section
    full_proposal += next_steps
    full_proposal += conclusion
    
    return full_proposal

def main():
    print("--------------------------------------------------")
    print("  GigPilot AI Asistanı: Proje Önerisi Taslağı Oluşturucu")
    print("--------------------------------------------------")
    print("Bu araç, freelancer'ların hızlıca proje önerisi taslakları oluşturmasına yardımcı olur.")
    print("Yapay zeka, girdiğiniz bilgilere göre taslağı şekillendirir.")
    print("\nLütfen aşağıdaki bilgileri girin:")

    project_type = input("Proje Türü (örn: Web Sitesi, Mobil Uygulama, Pazarlama Kampanyası): ")
    client_name = input("Müşteri Adı: ")
    key_goals = input("Projenin Temel Hedefleri/İstenen Özellikler (virgülle ayırın): ")

    print("\nGigPilot AI sizin için öneri taslağını hazırlıyor...")
    
    # Call the simulated AI assistant function to generate the proposal draft
    proposal_draft = generate_proposal_idea(project_type, client_name, key_goals)
    
    print("\n" + "="*60)
    print("  Oluşturulan Proje Önerisi Taslağı  ")
    print("="*60)
    print(proposal_draft)
    print("="*60)
    print("\nBu taslak bir başlangıç noktasıdır. Detayları kendi ihtiyaçlarınıza göre düzenleyebilirsiniz.")

if __name__ == "__main__":
    main()
