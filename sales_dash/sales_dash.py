import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import os

# ----- Load data -----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "sales_data.csv")

df = pd.read_csv(file_path)
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.strftime("%b")

# ----- Inisialisasi app -----
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])
app.title = "E-Commerce Dashboard"

# ----- Navbar (Filter Button di KIRI) -----
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(dbc.Button("⚙️ Filter", id="open-filter", color="light", outline=True, className="me-3")),
            dbc.Col(html.Img(src="https://cdn-icons-png.flaticon.com/512/2331/2331970.png", height="40px")),
            dbc.Col(dbc.NavbarBrand("E-Commerce Sales Dashboard", className="ms-2 fw-bold text-white")),
        ], align="center", className="g-0"),
    ]),
    color="primary",
    dark=True,
    className="shadow-sm mb-4"
)

# ----- Offcanvas Sidebar -----
offcanvas = dbc.Offcanvas(
    [
        html.H5("⚙️ Filter Data", className="text-primary fw-bold"),
        html.Hr(),

        html.Label("📅 Pilih Tahun:", className="fw-bold"),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": str(y), "value": y} for y in sorted(df["Year"].unique())],
            value=df["Year"].max(),
            clearable=False,
            className="mb-3"
        ),

        html.Label("🏷️ Pilih Kategori:", className="fw-bold"),
        dcc.Dropdown(
            id="category-dropdown",
            options=[{"label": c, "value": c} for c in sorted(df["Category"].unique())],
            value=None,
            multi=True,
            placeholder="Semua Kategori",
            className="mb-3"
        ),

        html.Label("🗓️ Pilih Rentang Tanggal:", className="fw-bold"),
        dcc.DatePickerRange(
            id="date-range",
            start_date=df["Date"].min(),
            end_date=df["Date"].max(),
            display_format="YYYY-MM-DD",
            className="mb-3"
        ),

        html.Div("© 2025 - Dashboard Sales", className="text-muted small mt-5")
    ],
    id="offcanvas",
    title="Filter Penjualan",
    is_open=False,
    placement="start",
    style={"width": "300px"}
)

# ----- KPI Cards -----
def kpi_card(title, id_value, color="primary"):
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="text-muted"),
            html.H4(id=id_value, className=f"text-{color} fw-bold")
        ]),
        className=f"shadow-sm border-start border-3 border-{color} mb-4"
    )

# ----- Layout utama -----
content = dbc.Container([
    dbc.Row([
        dbc.Col(kpi_card("💰 Total Penjualan", "kpi-sales", "success"), md=3),
        dbc.Col(kpi_card("📦 Total Transaksi", "kpi-orders", "info"), md=3),
        dbc.Col(kpi_card("🛍️ Rata-rata Penjualan", "kpi-average", "warning"), md=3),
        dbc.Col(kpi_card("🏆 Kategori Terlaris", "kpi-topcat", "danger"), md=3),
    ], className="mb-4"),

    # Grafik 1 & 2
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("📈 Tren Penjualan Bulanan", className="fw-bold text-primary"),
                dbc.CardBody([dcc.Graph(id="sales-trend")])
            ], className="shadow-sm mb-4 rounded-3")
        ], md=6),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("📊 Penjualan per Kategori", className="fw-bold text-primary"),
                dbc.CardBody([dcc.Graph(id="category-chart")])
            ], className="shadow-sm mb-4 rounded-3")
        ], md=6)
    ]),

    # Grafik 3 & 4
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("📉 Rata-rata Penjualan Harian", className="fw-bold text-primary"),
                dbc.CardBody([dcc.Graph(id="daily-avg-chart")])
            ], className="shadow-sm mb-4 rounded-3")
        ], md=8),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🥧 Proporsi Penjualan per Kategori", className="fw-bold text-primary"),
                dbc.CardBody([dcc.Graph(id="pie-chart")])
            ], className="shadow-sm mb-4 rounded-3")
        ], md=4),
    ])
], fluid=True)

# ----- Layout Gabungan -----
app.layout = html.Div([navbar, offcanvas, content])

# ----- Callback: Toggle Sidebar -----
@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-filter", "n_clicks"),
    State("offcanvas", "is_open"),
)
def toggle_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open

# ----- Callback Utama -----
@app.callback(
    [
        Output("sales-trend", "figure"),
        Output("category-chart", "figure"),
        Output("daily-avg-chart", "figure"),
        Output("pie-chart", "figure"),
        Output("kpi-sales", "children"),
        Output("kpi-orders", "children"),
        Output("kpi-average", "children"),
        Output("kpi-topcat", "children")
    ],
    [
        Input("year-dropdown", "value"),
        Input("category-dropdown", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date")
    ]
)
def update_dashboard(selected_year, selected_category, start_date, end_date):
    dff = df[(df["Year"] == selected_year) & (df["Date"].between(start_date, end_date))]
    if selected_category:
        dff = dff[dff["Category"].isin(selected_category)]

    # KPI
    total_sales = dff["Sales"].sum()
    total_orders = len(dff)
    avg_sales = dff["Sales"].mean()
    top_cat = dff.groupby("Category")["Sales"].sum().idxmax() if not dff.empty else "-"

    kpi_sales = f"Rp {total_sales:,.0f}".replace(",", ".")
    kpi_orders = f"{total_orders:,}".replace(",", ".")
    kpi_avg = f"Rp {avg_sales:,.0f}".replace(",", ".")
    kpi_topcat = top_cat

    # Grafik 1: Tren Bulanan
    monthly = dff.groupby("Month", as_index=False)["Sales"].sum()
    monthly["Month"] = pd.Categorical(monthly["Month"],
                                      categories=["Jan","Feb","Mar","Apr","May","Jun",
                                                  "Jul","Aug","Sep","Oct","Nov","Dec"],
                                      ordered=True)
    fig_trend = px.line(monthly, x="Month", y="Sales", markers=True, title="Tren Penjualan Bulanan")
    fig_trend.update_layout(template="plotly_white")

    # Grafik 2: Bar per Kategori
    cat_sales = dff.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
    fig_cat = px.bar(cat_sales, x="Category", y="Sales", color="Category", title="Penjualan per Kategori")
    fig_cat.update_layout(template="plotly_white")

    # Grafik 3: Rata-rata Harian
    daily_avg = dff.groupby("Date", as_index=False)["Sales"].mean()
    fig_daily = px.line(daily_avg, x="Date", y="Sales", markers=False, title="Rata-rata Penjualan Harian")
    fig_daily.update_layout(template="plotly_white")

    # Grafik 4: Pie Chart Proporsi
    if not cat_sales.empty:
        fig_pie = px.pie(cat_sales, names="Category", values="Sales",
                         title="Proporsi Penjualan per Kategori",
                         hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    else:
        fig_pie = px.pie(title="Tidak ada data untuk periode ini")

    fig_pie.update_layout(template="plotly_white")

    return fig_trend, fig_cat, fig_daily, fig_pie, kpi_sales, kpi_orders, kpi_avg, kpi_topcat


# ----- Main -----
if __name__ == "__main__":
    app.run(port=8050, debug=True)
