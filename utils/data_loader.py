import os
import zipfile
import requests
import pandas as pd

# Lokasi folder data
base_path = "data"

# --- Fungsi untuk download file dari Google Drive ---
def download_file_from_google_drive(file_url, save_path):
    if not os.path.exists(save_path):
        print("Downloading dataset from Google Drive...")
        response = requests.get(file_url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Download complete.")

# --- Fungsi untuk ekstrak zip ---
def extract_zip(zip_path, extract_to):
    if not os.path.exists(extract_to):
        print("Extracting dataset...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("Extraction complete.")

# --- Setup data ---
def setup_data():
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
        # Ganti dengan link file Google Drive kamu
        zip_url = "https://drive.google.com/uc?export=download&id=1_3FfjZFp9o_6VyMxgmKm0QIsN0351RvC"
        zip_path = "data.zip"
        download_file_from_google_drive(zip_url, zip_path)
        extract_zip(zip_path, base_path)

def load_all_data(base_path="data"):
    setup_data()
    customers = pd.read_csv(os.path.join(base_path, 'customers_dataset.csv'))
    geolocation = pd.read_csv(os.path.join(base_path, 'geolocation_dataset.csv'))
    leads_qualified = pd.read_csv(os.path.join(base_path, 'marketing_qualified_leads_dataset.csv'))
    leads_closed = pd.read_csv(os.path.join(base_path, 'closed_deals_dataset.csv'))  
    order_items = pd.read_csv(os.path.join(base_path, 'order_items_dataset.csv'))
    order_payments = pd.read_csv(os.path.join(base_path, 'order_payments_dataset.csv'))
    order_reviews = pd.read_csv(os.path.join(base_path, 'order_reviews_dataset.csv'))
    orders = pd.read_csv(os.path.join(base_path, 'orders_dataset.csv'))
    product_cat = pd.read_csv(os.path.join(base_path, 'product_category_name_translation.csv'))
    products = pd.read_csv(os.path.join(base_path, 'products_dataset.csv'))
    sellers = pd.read_csv(os.path.join(base_path, 'sellers_dataset.csv'))

    return {
        "orders": orders,
        "order_items": order_items,
        "order_payments": order_payments,
        "order_reviews": order_reviews,
        "products": products,
        "product_cat": product_cat,
        "customers": customers,
        "sellers": sellers,
        "geolocation": geolocation,
        "leads_qualified": leads_qualified,
        "leads_closed": leads_closed,
    }
