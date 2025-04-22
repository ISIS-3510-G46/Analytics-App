import os
from dotenv import load_dotenv
from supabase import create_client as create_session

def init_supabase():
    """Initialize and return the Supabase (postgreSQL) client."""
    load_dotenv()
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("No URL or KEY provided for supabase")
    
    return create_session(url, key)

def fetch_posts():
    """Fetch all posts from the Post table."""
    supabase = init_supabase()
    response = supabase.table("Post").select("*").execute()
    
    if response.data:
        return response.data
    else:
        raise Exception
    

def fetch_favorites():
    """Fetch all favorites from favorites tables"""
    supabase = init_supabase()
    favorites = supabase.table("favorites").select("*").execute()
    events = supabase.table("favorite_events").select("*").execute()
    
    if favorites.data:
        return favorites.data, events.data
    else:
        raise Exception
    


