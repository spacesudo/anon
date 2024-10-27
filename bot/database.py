import sqlite3
from datetime import datetime


class User:
    
    def __init__(self, dbname = "users.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)


    def setup(self):
        statement1 = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, chatid INTEGER UNIQUE, mnemonics TEXT UNIQUE, wallet TEXT UNIQUE, slippage FLOAT DEFAULT 0.2 )"
        self.conn.execute(statement1)
        self.conn.commit()


    def add_user(self, username_, mnemonics, wallet):
        statement = "INSERT OR IGNORE INTO users (chatid, mnemonics, wallet) VALUES (?, ?, ?)"
        args = (username_, mnemonics, wallet)
        self.conn.execute(statement, args)
        self.conn.commit()
    

    def update_slippage(self, amount, userid):
        statement = "UPDATE users SET slippage = ? WHERE chatid = ?"
        args = (amount, userid)
        self.conn.execute(statement, args)
        self.conn.commit()
    
    
    def update_wallet(self, wallet, userid):
        statement = "UPDATE users SET wallet = ? WHERE chatid = ?"
        args = (wallet, userid)
        self.conn.execute(statement, args)
        self.conn.commit()
        
        
    def update_mnemonics(self, amount, userid):
        statement = "UPDATE users SET mnemonics = ? WHERE chatid = ?"
        args = (amount, userid)
        self.conn.execute(statement, args)
        self.conn.commit()
        
        
        
    def get_slippage(self, owner):
        statement = "SELECT slippage FROM users WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    def get_wallet(self, owner):
        statement = "SELECT wallet FROM users WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    
    def get_mnemonics(self, owner):
        statement = "SELECT mnemonics FROM users WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None


    def get_users(self):
        statement = "SELECT chatid FROM users"
        return [x[0] for x in self.conn.execute(statement)]
    
    
class Withdraw:
    
    def __init__(self, dbname="withdraw.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        statement1 = """CREATE TABLE IF NOT EXISTS referrals (
                            id INTEGER PRIMARY KEY,
                            chatid INTEGER UNIQUE,
                            txid TEXT DEFAULT 'YES',
                            amount FLOAT DEFAULT 0.0
                        )"""
        self.conn.execute(statement1)
        self.conn.commit()

    def add_user(self, chatid):
        statement = "INSERT OR IGNORE INTO referrals (chatid) VALUES (?)"
        args = (chatid,)
        self.conn.execute(statement, args)
        self.conn.commit()

    def update_txid(self, txid, userid):
        statement = "UPDATE referrals SET txid = ? WHERE chatid = ?"
        args = (txid, userid)
        self.conn.execute(statement, args)
        self.conn.commit()

    def get_txid(self, userid):
        statement = "SELECT txid FROM referrals WHERE chatid = ?"
        args = (userid,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def update_amount(self, amount, userid):
        statement = "UPDATE referrals SET amount = ? WHERE chatid = ?"
        args = (amount, userid)
        self.conn.execute(statement, args)
        self.conn.commit()

    def get_amount(self, userid):
        statement = "SELECT amount FROM referrals WHERE chatid = ?"
        args = (userid,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def del_user(self, userid):
        statement = "DELETE FROM referrals WHERE chatid = ?"
        args = (userid,)
        self.conn.execute(statement, args)
        self.conn.commit()


class Referrals:
    
    def __init__(self, dbname = "referrals.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)


    def setup(self):
        statement1 = """CREATE TABLE IF NOT EXISTS referrals (id INTEGER PRIMARY KEY, chatid INTEGER UNIQUE,
                            wallet TEXT UNIQUE, referrer INTEGER , referrals INTEGER DEFAULT 0,
                            referrals_vol FLOAT DEFAULT 0.0, trading_vol FLOAT DEFAULT 0.0 )"""
                            
        self.conn.execute(statement1)
        self.conn.commit()


    def add_user(self, username_, wallet, referrer):
        statement = "INSERT OR IGNORE INTO referrals (chatid, wallet, referrer) VALUES (?, ?, ?)"
        args = (username_, wallet,referrer)
        self.conn.execute(statement, args)
        self.conn.commit()
        
        
    def update_referrals(self, amount, userid):
        statement = "UPDATE referrals SET referrals = ? WHERE chatid = ?"
        args = (amount, userid)
        self.conn.execute(statement, args)
        self.conn.commit()
        
        
        
    def get_referrals(self, owner):
        statement = "SELECT referrals FROM referrals WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    
    def update_referrals_vol(self, amount, userid):
        statement = "UPDATE referrals SET referrals_vol = ? WHERE chatid = ?"
        args = (amount, userid)
        self.conn.execute(statement, args)
        self.conn.commit()
        
        
        
    def get_referrals_vol(self, owner):
        statement = "SELECT referrals_vol FROM referrals WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    def update_trading_vol(self, amount, userid):
        statement = "UPDATE referrals SET trading_vol = ? WHERE chatid = ?"
        args = (amount, userid)
        self.conn.execute(statement, args)
        self.conn.commit()
        
        
        
    def get_trading_vol(self, owner):
        statement = "SELECT trading_vol FROM referrals WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    def get_referrer(self, owner):
        statement = "SELECT referrer FROM referrals WHERE chatid = ?"
        args = (owner,)
        cursor = self.conn.execute(statement, args)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    def get_users(self):
        statement = "SELECT chatid, wallet, referrer, referrals, referrals_vol, trading_vol FROM referrals"
        return [x for x in self.conn.execute(statement)]
    
    

class Bets:
    def __init__(self, dbname="bets.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        statement = """
        CREATE TABLE IF NOT EXISTS bets (
            owner TEXT, 
            selection TEXT,
            bet_time TEXT,
            result TEXT DEFAULT NULL
        )
        """
        self.conn.execute(statement)
        self.conn.commit()

    def add(self, owner, selection):
        try:
            bet_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time
            statement = """
            INSERT INTO bets (owner, selection, bet_time, result) 
            VALUES (?, ?, ?, ?)
            """
            args = (owner, selection, bet_time, None)  # result defaults to NULL
            self.conn.execute(statement, args)
            self.conn.commit()
        except Exception as e:
            return e

    def get_last_selection(self, owner):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT selection FROM bets WHERE owner = ? ORDER BY ROWID DESC LIMIT 1
            """, (owner,))
            last_selection = cursor.fetchone()
            return last_selection[0] if last_selection else None
        except Exception as e:
            return e

    def update_selection(self, owner, selection):
        try:
            statement = """
            UPDATE bets 
            SET selection=? 
            WHERE owner=?
            """
            args = (selection, owner)
            self.conn.execute(statement, args)
            self.conn.commit()
            return "Selection updated successfully"
        except Exception as e:
            return e

    def update_result(self, owner, result):
        try:
            statement = """
            UPDATE bets 
            SET result=? 
            WHERE owner=?
            """
            args = (result, owner)
            self.conn.execute(statement, args)
            self.conn.commit()
            return "Result updated successfully"
        except Exception as e:
            return e

    def get_all(self, owner):
        statement = """
        SELECT owner, selection, bet_time, result 
        FROM bets 
        WHERE owner = ?
        """
        args = (owner,)
        return [x for x in self.conn.execute(statement, args)]