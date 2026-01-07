import sqlite3
import pandas as pd


conn = sqlite3.connect("chinook.db")


customers = pd.read_sql("SELECT * FROM Customer", conn)
invoices = pd.read_sql("SELECT * FROM Invoice", conn)
invoice_lines = pd.read_sql("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)

# =========================
# Customer Purchases Analysis
# =========================


invoice_data = invoices.merge(invoice_lines, on="InvoiceId")


total_spent = (
    invoice_data
    .groupby("CustomerId")["UnitPrice"]
    .sum()
    .reset_index(name="TotalSpent")
)


total_spent = total_spent.merge(
    customers[["CustomerId", "FirstName", "LastName"]],
    on="CustomerId"
)


top_5_customers = (
    total_spent
    .sort_values("TotalSpent", ascending=False)
    .head(5)
)

print("=== TOP 5 CUSTOMERS BY TOTAL SPENDING ===")
print(top_5_customers[["CustomerId", "FirstName", "LastName", "TotalSpent"]])

# =========================
# Album vs Individual Track Purchases
# =========================

purchase_tracks = invoice_data.merge(tracks, on="TrackId")


album_track_counts = (
    tracks
    .groupby("AlbumId")
    .size()
    .reset_index(name="TotalTracksInAlbum")
)

customer_album_tracks = (
    purchase_tracks
    .groupby(["CustomerId", "AlbumId"])
    .size()
    .reset_index(name="TracksPurchased")
)

customer_album_tracks = customer_album_tracks.merge(
    album_track_counts,
    on="AlbumId"
)


customer_album_tracks["FullAlbum"] = (
    customer_album_tracks["TracksPurchased"]
    == customer_album_tracks["TotalTracksInAlbum"]
)


customer_preference = (
    customer_album_tracks
    .groupby("CustomerId")["FullAlbum"]
    .any()
    .reset_index()
)

customer_preference["Preference"] = customer_preference["FullAlbum"].map(
    {True: "Full Albums", False: "Individual Tracks"}
)


preference_summary = (
    customer_preference["Preference"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index()
)

preference_summary.columns = ["PurchaseType", "Percentage"]

print("\n=== CUSTOMER PURCHASE PREFERENCE (%) ===")
print(preference_summary)


conn.close()
