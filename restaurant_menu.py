import streamlit as st
import time
import json

# Page configuration with custom styling
st.set_page_config(
    page_title="Brew & Bite Café - Premium Dining Experience",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with Modern Design
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Header */
    .main-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 1.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Category Cards */
    .category-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
        cursor: pointer;
        text-align: center;
    }
    
    .category-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 1);
    }
    
    .category-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .category-description {
        color: #666;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    
    /* Menu Item Cards */
    .menu-item {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
        overflow: hidden;
    }
    
    .menu-item:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    .item-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 15px;
        margin-bottom: 1rem;
    }
    
    .item-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .item-price {
        font-size: 1.25rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 1rem;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
    
    /* Cart Sidebar */
    .cart-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        position: sticky;
        top: 2rem;
    }
    
    .cart-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .cart-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .cart-total {
        font-size: 1.5rem;
        font-weight: 700;
        color: #667eea;
        text-align: center;
        margin: 1.5rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-radius: 15px;
    }
    
    /* Floating Cart */
    .floating-cart {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        z-index: 9999;
        font-weight: 600;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(20px);
    }
    
    .floating-cart:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* Success Messages */
    .success-message {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 4px 16px rgba(76, 175, 80, 0.3);
    }
    
    /* Navigation */
    .nav-button {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .nav-button:hover {
        background: rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.5);
    }
    
    /* Form Inputs */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #eee;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Number Input */
    .stNumberInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #eee;
        padding: 0.75rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .category-card {
            padding: 1.5rem;
        }
        
        .menu-item {
            padding: 1rem;
        }
        
        .floating-cart {
            bottom: 1rem;
            right: 1rem;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Menu Data with descriptions
category_data = {
    "Starters": {
        "image": "https://c.ndtvimg.com/2023-08/sfc3gcoo_chicken-snack_625x300_21_August_23.jpg?im=FaceCrop,algorithm=dnn,width=1200,height=675",
        "description": "Delightful appetizers to start your culinary journey",
        "emoji": "🥗"
    },
    "Main Course": {
        "image": "https://cbx-prod.b-cdn.net/COLOURBOX60103276.jpg?width=800&height=800&quality=70",
        "description": "Hearty and satisfying dishes that define our cuisine",
        "emoji": "🍽️"
    },
    "Smoothies": {
        "image": "https://thumbs.dreamstime.com/b/colorful-smoothies-glass-jars-fresh-fruit-black-surface-colorful-smoothies-glass-jars-fresh-fruit-black-339067901.jpg",
        "description": "Fresh and healthy blended beverages",
        "emoji": "🥤"
    },
    "Desserts": {
        "image": "https://cdn.hswstatic.com/gif/desserts-update.jpg",
        "description": "Sweet endings to perfect your dining experience",
        "emoji": "🍰"
    }
}

# Enhanced menu with detailed descriptions
menu = {
    "Starters": [
        {"name": "Veg Spring Roll", "price": 120, "image": "https://www.womansworld.com/wp-content/uploads/2023/09/airfryer13.jpg", "description": "Crispy golden rolls filled with fresh vegetables"},
        {"name": "French Fries", "price": 100, "image": "https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw3a257599/images/recipe-Images/french-fries-airfryer-recipe.jpg?sw=1200&sh=1200&sm=fit", "description": "Perfectly seasoned golden potato fries"},
        {"name": "Paneer Tikka", "price": 150, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/03/paneer-tikka-1.jpg", "description": "Marinated cottage cheese grilled to perfection"},
        {"name": "Chicken Lollipop", "price": 160, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/07/chicken-lollipop.jpg", "description": "Succulent chicken drumettes with spicy coating"},
        {"name": "Hara Bhara Kebab", "price": 130, "image": "https://www.cookingcarnival.com/wp-content/uploads/2020/07/Hara-Bhara-Kabab-1.jpg", "description": "Healthy green vegetable patties with aromatic spices"},
        {"name": "Cheese Balls", "price": 140, "image": "https://www.cookclickndevour.com/wp-content/uploads/2017/06/cheese-balls-recipe-2.jpg", "description": "Crispy exterior with molten cheese center"},
        {"name": "Corn Cheese Nuggets", "price": 120, "image": "https://i.ytimg.com/vi/YcB3T6T-0ks/maxresdefault.jpg", "description": "Sweet corn and cheese in crispy coating"},
        {"name": "Onion Rings", "price": 90, "image": "https://www.cookingclassy.com/wp-content/uploads/2022/05/onion-rings-10.jpg", "description": "Beer-battered onion rings with tangy dip"},
        {"name": "Garlic Bread", "price": 110, "image": "https://www.simplyrecipes.com/thmb/dNHsQZbo1eWWCeaLFiitBIr8Eaw=/2000x1333/filters:fill(auto,1)/Simply-Recipes-Garlic-Bread-LEAD-04-4a403d4687da4384b1c1774f9919b6b3.jpg", "description": "Herb-infused bread with garlic butter"},
        {"name": "Stuffed Mushrooms", "price": 150, "image": "https://www.loveandlemons.com/wp-content/uploads/2020/12/stuffed-mushrooms-580x629.jpg", "description": "Button mushrooms stuffed with savory filling"},
    ],
    "Main Course": [
        {"name": "Paneer Butter Masala", "price": 220, "image": "https://www.ruchiskitchen.com/wp-content/uploads/2020/12/Paneer-butter-masala-recipe-3-500x500.jpg", "description": "Rich and creamy tomato-based curry with cottage cheese"},
        {"name": "Chicken Biryani", "price": 250, "image": "https://j6e2i8c9.delivery.rocketcdn.me/wp-content/uploads/2020/09/Chicken-Biryani-Recipe-01-1.jpg", "description": "Aromatic basmati rice layered with spiced chicken"},
        {"name": "Dal Makhani", "price": 200, "image": "https://www.whiskaffair.com/wp-content/uploads/2020/07/Dal-Makhani-2-3.jpg", "description": "Slow-cooked black lentils in rich creamy sauce"},
        {"name": "Butter Naan", "price": 40, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/07/butter-naan-recipe-1.jpg", "description": "Soft leavened bread brushed with butter"},
        {"name": "Jeera Rice", "price": 90, "image": "https://www.whiskaffair.com/wp-content/uploads/2020/08/Jeera-Rice-2-3.jpg", "description": "Fragrant basmati rice tempered with cumin"},
        {"name": "Shahi Paneer", "price": 230, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/shahi-paneer-1.jpg", "description": "Royal cottage cheese curry in cashew-based gravy"},
        {"name": "Veg Pulao", "price": 150, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/05/vegetable-pulao-recipe.jpg", "description": "Aromatic rice cooked with mixed vegetables"},
        {"name": "Kadai Chicken", "price": 240, "image": "https://www.cubesnjuliennes.com/wp-content/uploads/2020/12/Kadai-Chicken-Recipe.jpg", "description": "Spicy chicken cooked in traditional iron wok"},
        {"name": "Chole Bhature", "price": 180, "image": "https://www.cookwithmanali.com/wp-content/uploads/2020/05/Chole-Bhature.jpg", "description": "Spiced chickpeas with fluffy fried bread"},
        {"name": "Egg Curry", "price": 190, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/03/egg-curry-recipe.jpg", "description": "Hard-boiled eggs in spiced onion-tomato gravy"},
    ],
    "Smoothies": [
        {"name": "Mango Smoothie", "price": 80, "image": "https://vaya.in/recipes/wp-content/uploads/2017/09/Mango-Smoothie_1-1.jpg", "description": "Tropical mango blended with creamy yogurt"},
        {"name": "Dark Chocolate Iced Coffee", "price": 90, "image": "https://lorcoffee.com/cdn/shop/articles/Dark-Chocolate-Ice-Coffee-with-Provocateur-exc.jpg", "description": "Rich coffee with dark chocolate and ice"},
        {"name": "Strawberry Banana", "price": 85, "image": "https://cdn.loveandlemons.com/wp-content/uploads/2021/07/strawberry-banana-smoothie-580x869.jpg", "description": "Classic combination of sweet berries and banana"},
        {"name": "Blueberry Oat", "price": 95, "image": "https://www.wellplated.com/wp-content/uploads/2021/06/Blueberry-Oat-Smoothie.jpg", "description": "Antioxidant-rich blueberries with hearty oats"},
        {"name": "Avocado Green", "price": 100, "image": "https://cdn.loveandlemons.com/wp-content/uploads/2021/07/green-smoothie-580x869.jpg", "description": "Creamy avocado with fresh greens and fruits"},
        {"name": "Pineapple Mint", "price": 80, "image": "https://www.runningtothekitchen.com/wp-content/uploads/2020/07/pineapple-mint-smoothie-480x480.jpg", "description": "Refreshing tropical pineapple with cool mint"},
        {"name": "Peach Yogurt", "price": 85, "image": "https://www.acouplecooks.com/wp-content/uploads/2021/06/Peach-Smoothie-010.jpg", "description": "Sweet peaches blended with Greek yogurt"},
        {"name": "Chocolate Banana", "price": 90, "image": "https://www.wellplated.com/wp-content/uploads/2021/06/Chocolate-Banana-Smoothie.jpg", "description": "Decadent chocolate with ripe banana"},
        {"name": "Coconut Mango", "price": 95, "image": "https://www.gimmesomeoven.com/wp-content/uploads/2015/07/Coconut-Mango-Smoothie.jpg", "description": "Tropical fusion of coconut and mango"},
        {"name": "Mixed Berry", "price": 100, "image": "https://www.acouplecooks.com/wp-content/uploads/2021/01/Berry-Smoothie-015.jpg", "description": "Antioxidant powerhouse of mixed berries"},
    ],
    "Desserts": [
        {"name": "Chocolate Brownie", "price": 150, "image": "https://www.spendwithpennies.com/wp-content/uploads/2016/09/Hot-Fudge-Slow-Cooker-Brownies-21.jpg", "description": "Fudgy chocolate brownie with warm center"},
        {"name": "Trifle", "price": 60, "image": "https://media.restless.co.uk/uploads/2021/05/trifle.jpg", "description": "Layered dessert with cake, custard, and fruits"},
        {"name": "Gulab Jamun", "price": 70, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/gulab-jamun-recipe-1.jpg", "description": "Soft milk dumplings in rose-flavored syrup"},
        {"name": "Rasmalai", "price": 90, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/07/rasmalai.jpg", "description": "Cottage cheese dumplings in cardamom milk"},
        {"name": "Cheesecake", "price": 120, "image": "https://sallysbakingaddiction.com/wp-content/uploads/2018/05/classic-cheesecake.jpg", "description": "Creamy New York style cheesecake"},
        {"name": "Cupcake", "price": 60, "image": "https://www.cookingclassy.com/wp-content/uploads/2020/06/vanilla-cupcakes-6.jpg", "description": "Fluffy vanilla cupcake with buttercream"},
        {"name": "Ice Cream Sundae", "price": 90, "image": "https://www.simplyrecipes.com/thmb/zGJh8Xc3ZUGSPBD8IDvddE3EGpg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Ice-Cream-Sundae-LEAD-05-96ce9146e3d94ef6a9d2468f071c5d3b.jpg", "description": "Classic ice cream with toppings and sauces"},
        {"name": "Choco Lava Cake", "price": 100, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/molten-lava-cake-1.jpg", "description": "Warm chocolate cake with molten center"},
        {"name": "Fruit Custard", "price": 70, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/fruit-custard-recipe-1.jpg", "description": "Creamy custard with fresh seasonal fruits"},
        {"name": "Kheer", "price": 80, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/rice-kheer-recipe-1.jpg", "description": "Traditional rice pudding with nuts and cardamom"},
    ]
}

# Initialize session state with enhanced defaults
default_states = {
    "page": "home",
    "cart": [],
    "customer_info": {"name": "", "mobile": "", "email": ""},
    "last_added_item": None,
    "last_added_qty": 0,
    "just_added": False,
    "selected_category": None,
    "order_placed": False,
    "show_item_details": None,
    "order_type": "Dine In"
}

for key, default in default_states.items():
    if key not in st.session_state:
        st.session_state[key] = default

def display_header():
    """Display the main header with branding"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🍽️ Brew & Bite Café</h1>
        <p class="subtitle">Premium Dining Experience Since 2020</p>
    </div>
    """, unsafe_allow_html=True)

def display_home_page():
    """Enhanced home page with hero section"""
    display_header()
    
    st.markdown("""
    <div class="hero-section">
        <h2 class="hero-title">Welcome to Culinary Excellence</h2>
        <p class="hero-subtitle">Where every dish tells a story of passion, flavor, and tradition</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero image with proper aspect ratio
    st.image(
        "https://www.cafeflorista.com/_next/image?url=%2Fimages%2Fcafe%2FIMG-20240922-WA0015.jpg&w=640&q=75",
        use_container_width=True,
        caption="Experience the finest culinary journey"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🍽️ Explore Our Menu", use_container_width=True):
            st.session_state.page = "menu"
            st.session_state.selected_category = None
            st.rerun()

def display_category_selection():
    """Enhanced category selection with better layout"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">📋 Choose Your Category</h1>
        <p class="subtitle">Select from our carefully curated menu sections</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create 2x2 grid for categories
    col1, col2 = st.columns(2)
    categories = list(category_data.keys())
    
    for i, category in enumerate(categories):
        data = category_data[category]
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="category-card">
                <h3 class="category-title">{data['emoji']} {category}</h3>
                <p class="category-description">{data['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.image(data['image'], use_container_width=True)
            
            if st.button(f"View {category}", key=f"cat_{category}", use_container_width=True):
                st.session_state.selected_category = category
                st.rerun()

def display_cart_summary():
    """Enhanced cart display in sidebar"""
    with st.sidebar:
        st.markdown("""
        <div class="cart-container">
            <h2 class="cart-title">🛒 Your Order</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Group cart items
        grouped_cart = {}
        for item in st.session_state.cart:
            key = item["name"]
            if key in grouped_cart:
                grouped_cart[key]["qty"] += item["qty"]
            else:
                grouped_cart[key] = item.copy()
        
        total = 0
        if grouped_cart:
            for name, item in grouped_cart.items():
                item_total = item["price"] * item["qty"]
                total += item_total
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{item['name']}**  \n{item['qty']} × ₹{item['price']} = ₹{item_total}")
                with col2:
                    if st.button("🗑️", key=f"remove_{item['name']}", help="Remove item"):
                        st.session_state.cart = [i for i in st.session_state.cart if i["name"] != item["name"]]
                        st.rerun()
                st.markdown("---")
            
            st.markdown(f"""
            <div class="cart-total">
                Total: ₹{total}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Your cart is empty")
        
        # Customer information
        st.markdown("### 👤 Customer Details")
        st.session_state.customer_info["name"] = st.text_input(
            "Full Name *", 
            value=st.session_state.customer_info["name"],
            placeholder="Enter your full name"
        )
        st.session_state.customer_info["mobile"] = st.text_input(
            "Mobile Number *", 
            value=st.session_state.customer_info["mobile"],
            placeholder="Enter your mobile number"
        )
        st.session_state.customer_info["email"] = st.text_input(
            "Email (Optional)", 
            value=st.session_state.customer_info["email"],
            placeholder="Enter your email"
        )
        
        # Order type selection
        st.session_state.order_type = st.selectbox(
            "Order Type",
            ["Dine In", "Takeaway", "Delivery"]
        )
        
        # Checkout button
        if st.button("🧾 Proceed to Checkout", use_container_width=True):
            if not st.session_state.customer_info["name"] or not st.session_state.customer_info["mobile"]:
                st.error("Please fill in your name and mobile number.")
            elif not grouped_cart:
                st.warning("Your cart is empty.")
            else:
                st.session_state.page = "checkout"
                st.rerun()

def display_menu_items(category):
    """Enhanced menu item display with better layout"""
    st.markdown(f"""
    <div class="main-header">
        <h1 class="main-title">{category_data[category]['emoji']} {category}</h1>
        <p class="subtitle">{category_data[category]['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Categories", key="back_to_categories"):
        st.session_state.selected_category = None
        st.rerun()
    
    # Display items in a responsive grid
    items = menu[category]
    
    # Create columns based on screen size
    cols = st.columns(2)
    
    for i, item in enumerate(items):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="menu-item">
                <img src="{item['image']}" class="item-image" alt="{item['name']}">
                <h3 class="item-name">{item['name']}</h3>
                <p class="item-price">₹{item['price']}</p>
                <p style="color: #666; margin-bottom: 1rem;">{item.get('description', 'Delicious and freshly prepared')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Quantity selector
            qty_key = f"qty_{item['name']}_{category}"
            qty = st.number_input(
                "Quantity", 
                min_value=1, 
                max_value=10, 
                step=1,
                key=f"qty_input_{qty_key}",
                value=1
            )
            
            # Add to cart button
            if st.button(f"Add to Cart", key=f"add_{item['name']}_{category}", use_container_width=True):
                cart_item = {**item, "qty": qty}
                st.session_state.cart.append(cart_item)
                st.session_state.last_added_item = item['name']
                st.session_state.last_added_qty = qty
                st.session_state.just_added = True
                st.rerun()
            
            # Success message
            if (st.session_state.last_added_item == item['name'] and 
                st.session_state.just_added):
                st.markdown(f"""
                <div class="success-message">
                    ✅ Added {st.session_state.last_added_qty} × {item['name']} to cart
                </div>
                """, unsafe_allow_html=True)
                st.session_state.just_added = False

def display_floating_cart():
    """Display floating cart widget"""
    grouped_cart = {}
    for item in st.session_state.cart:
        key = item["name"]
        if key in grouped_cart:
            grouped_cart[key]["qty"] += item["qty"]
        else:
            grouped_cart[key] = item.copy()
    
    total_items = sum(item["qty"] for item in grouped_cart.values())
    total_price = sum(item["qty"] * item["price"] for item in grouped_cart.values())
    
    if total_items > 0:
        st.markdown(f"""
        <div class="floating-cart" onclick="document.getElementById('floating_checkout_btn').click();">
            🛒 {total_items} item(s) | ₹{total_price}
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button for navigation
        if st.button("Go to Checkout", key="floating_checkout_btn", type="primary"):
            st.session_state.page = "checkout"
            st.rerun()

def display_checkout():
    """Enhanced checkout page"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🧾 Order Summary</h1>
        <p class="subtitle">Review your order before confirmation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Customer details
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👤 Customer Information")
        st.write(f"**Name:** {st.session_state.customer_info['name']}")
        st.write(f"**Mobile:** {st.session_state.customer_info['mobile']}")
        if st.session_state.customer_info['email']:
            st.write(f"**Email:** {st.session_state.customer_info['email']}")
        st.write(f"**Order Type:** {st.session_state.order_type}")
    
    with col2:
        st.markdown("### 📅 Order Details")
        import datetime
        st.write(f"**Date:** {datetime.datetime.now().strftime('%d %B %Y')}")
        st.write(f"**Time:** {datetime.datetime.now().strftime('%I:%M %p')}")
    
    st.markdown("---")
    
    # Order items
    st.markdown("### 🍽️ Items Ordered")
    
    grouped_cart = {}
    for item in st.session_state.cart:
        key = item["name"]
        if key in grouped_cart:
            grouped_cart[key]["qty"] += item["qty"]
        else:
            grouped_cart[key] = item.copy()
    
    total = 0
    for name, item in grouped_cart.items():
        subtotal = item["price"] * item["qty"]
        total += subtotal
        
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"**{item['name']}**")
        with col2:
            st.write(f"₹{item['price']}")
        with col3:
            st.write(f"× {item['qty']}")
        with col4:
            st.write(f"₹{subtotal}")
    
    st.markdown("---")
    
    # Total calculation
    tax = total * 0.18  # 18% GST
    grand_total = total + tax
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Subtotal:**")
        st.write("**Tax (18% GST):**")
        st.write("**Grand Total:**")
    with col2:
        st.write(f"₹{total:.2f}")
        st.write(f"₹{tax:.2f}")
        st.write(f"**₹{grand_total:.2f}**")
    
    st.markdown("---")
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("← Modify Cart", use_container_width=True):
            st.session_state.page = "menu"
            st.rerun()
    
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    
    with col3:
        if st.button("✅ Confirm Order", use_container_width=True):
            # Simulate order processing
            with st.spinner("Processing your order..."):
                time.sleep(2)
            
            st.markdown("""
            <div class="success-message">
                🎉 Order placed successfully!<br>
                Order ID: #BB{}<br>
                Estimated time: 25-30 minutes
            </div>
            """.format(str(int(time.time()))[-6:]), unsafe_allow_html=True)
            
            # Clear cart and redirect
            time.sleep(3)
            st.session_state.cart.clear()
            st.session_state.page = "home"
            st.session_state.selected_category = None
            st.session_state.order_placed = True
            st.rerun()

# Main application flow
def main():
    if st.session_state.page == "home":
        display_home_page()
    
    elif st.session_state.page == "menu":
        display_cart_summary()
        
        if st.session_state.selected_category is None:
            display_category_selection()
        else:
            display_menu_items(st.session_state.selected_category)
            display_floating_cart()
        
        # Navigation
        st.markdown("---")
        if st.button("🏠 Back to Home", key="home_nav"):
            st.session_state.page = "home"
            st.rerun()
    
    elif st.session_state.page == "checkout":
        display_checkout()

if __name__ == "__main__":
    main()