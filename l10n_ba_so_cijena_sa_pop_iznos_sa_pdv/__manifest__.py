{
    "name": "Prodajna narudžba (SO), prikaz dodatnih kolona",
    "summary": 'Cijena sa Popustom, Cijena sa PDV, Iznos sa PDV',
    "description": """
Dodatne kolone:
- Cijena sa popustom (ako je popust <> 0%)
- Cijena sa PDV (sa uračunatim popustom)
- Iznos sa PDV
""",
    "version": "16.0.2.0.7",
    "author": "bring.out doo Sarajevo",
    "website": "https://www.bring.out.ba",
    "category": "Localization",
    "depends": [ "l10n_bs", "order_line_sequences", "l10n_ba_sifra_in_documents"],
    "data": [
        "views/sale_order_document_view.xml",
    ],
    "installable": True,
}
