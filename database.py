import sqlite3
import threading

db = None
db_lock = threading.Lock()

def get_cursor():
    local_thread = threading.current_thread()
    if not hasattr(local_thread, "db"):
        local_thread.db = sqlite3.connect("main.db")
    if not hasattr(local_thread, "cur"):
        local_thread.cur = local_thread.db.cursor()
    return local_thread.db, local_thread.cur

def get_connection():
    return sqlite3.connect("main.db")

def execute_sql(sql, params=None):
    with db_lock:
        db, cur = get_cursor()
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        return cur.fetchall()

db, cur = get_cursor()

cur.execute("PRAGMA journal_mode=WAL")

cur.executescript(
    """
-- Configurações gerais do bot --
CREATE TABLE IF NOT EXISTS bot_config(
    lara_name TEXT DEFAULT 'use automatico',                 
    lara_key TEXT DEFAULT 'use automatico',                                      
    main_img TEXT DEFAULT 'nadaquiiii',  
    support_user TEXT DEFAULT '@teslaofc',                               
    channel_user TEXT DEFAULT '@teslaofc',                                    
    is_on INTEGER DEFAULT 1,                                                
    gate_chk TEXT DEFAULT '@teslaofc',                                            
    gate_chk_publico TEXT DEFAULT '@teslaofc',                                            
    gate_exchange TEXT DEFAULT '@teslaofc',                                       
    pay_auto TEXT DEFAULT 'mercado pago',                                            
    random_pix TEXT,                                                            
    random_pix_pb TEXT,                                                         
    time_exchange INTEGER DEFAULT 10,                                            
    exchange_is INTEGER DEFAULT 1,                                              
    db_version INTEGER DEFAULT 9                                                
);

INSERT OR IGNORE INTO bot_config(ROWID) values(0);

CREATE TABLE IF NOT EXISTS bonus_users(
    porcentagem TEXT,
    Id_login TEXT
);

CREATE TABLE IF NOT EXISTS preco(
    Preco_login TEXT,
    Nome_login TEXT,
    Id_login TEXT
);

CREATE TABLE IF NOT EXISTS config_adm(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    free_chk TEXT,
    admin_id TEXT
);

CREATE TABLE IF NOT EXISTS grupos_free(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_grupo TEXT
);

CREATE TABLE IF NOT EXISTS cartoes_testados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cartao TEXT NOT NULL,
    id_testou INTEGER NOT NULL,
    data_teste DATE DEFAULT (date('now')),
    ban_users TEXT,
    dies_testadas TEXT,
    lives_testadas TEXT,
    status TEXT
);

-- Db principal de cartões --
CREATE TABLE IF NOT EXISTS docscnh(
    tipo TEXT NOT NULL,
    email TEXT NOT NULL,                                                      
    senha TEXT NOT NULL,
    idlogin INTEGER PRIMARY KEY,
    cidade TEXT NOT NULL,                                                    
    added_date TEXT DEFAULT (datetime('now','localtime')),                  
    pending INTEGER DEFAULT 0,                                              
    cpf TEXT NOT NULL DEFAULT '',                                                       
    owner INTEGER NOT NULL                                                     
);

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY NOT NULL,                                     
    username TEXT,                                                       
    premium TEXT,
    premium_creditos INTEGER DEFAULT 0,                                   
    name_user TEXT,                                                      
    balance NUMERIC NOT NULL DEFAULT 0,                                  
    balance_diamonds NUMERIC NOT NULL DEFAULT 0,                         
    agreed_tos INTEGER NOT NULL DEFAULT 0,                               
    last_bought TEXT,                                                    
    is_action_pending INTEGER DEFAULT 0,                                
    is_blacklisted INTEGER NOT NULL DEFAULT 0,                           
    refer INTEGER,                                                       
    cpf TEXT,                                                            
    name TEXT,                                                           
    email TEXT                                                           
);

CREATE TABLE IF NOT EXISTS gifts(
    token TEXT PRIMARY KEY NOT NULL,                                    
    value INTEGER NOT NULL                                              
);

CREATE TABLE IF NOT EXISTS tokens(
    type_token TEXT PRIMARY KEY NOT NULL,                              
    client_id TEXT,                                                    
    client_secret TEXT,                                                
    name_cert_pem TEXT,                                                
    name_cert_key TEXT,                                                
    bearer_tk TEXT                                                     
);

-- Table para fazer o relatorio de vendas de entrada de saldo diario. --
CREATE TABLE IF NOT EXISTS sold_balance(
    type TEXT NOT NULL,                                                
    value INTEGER NOT NULL,                                            
    owner INTEGER NOT NULL,                                           
    quantity INTEGER NOT NULL DEFAULT 1,                               
    add_balance_date TEXT DEFAULT (datetime('now','localtime'))       
);

-- tabela para configurar bonus e preços e etc. --
CREATE TABLE IF NOT EXISTS values_config(
    transaction_type TEXT NOT NULL,                                   
    min_value INTEGER NOT NULL,                                       
    bonus_value INTEGER NOT NULL                                      
);
"""
)

database_version = execute_sql("SELECT db_version FROM bot_config")[0][0]

if database_version == 0:
    execute_sql(
        """
    ALTER TABLE bot_config ADD COLUMN gate_chk TEXT DEFAULT 'w4rlock';
    ALTER TABLE bot_config ADD COLUMN gate_exchange TEXT DEFAULT 'w4rlock';
        """
    )

    database_version += 1

if database_version == 1:
    execute_sql(
        """
    ALTER TABLE bot_config ADD COLUMN time_exchange INTEGER DEFAULT 5;
        """
    )
    database_version += 1

if database_version == 2:
    execute_sql(
        """
    ALTER TABLE bot_config ADD COLUMN exchange_is INTEGER DEFAULT 1;
        """
    )
    database_version += 1

if database_version == 3:
    execute_sql(
        """
    ALTER TABLE users ADD COLUMN is_action_pending INTEGER DEFAULT 0;
        """
    )
    database_version += 1


if database_version == 4:
    execute_sql(
        """
    ALTER TABLE bot_config ADD COLUMN pay_auto TEXT DEFAULT 'mercado pago';
    ALTER TABLE bot_config ADD COLUMN random_pix TEXT;
        """
    )
    database_version += 1

if database_version == 5:
    execute_sql(
        """
    ALTER TABLE tokens ADD COLUMN name_cert_pem TEXT NOT NULL;
    ALTER TABLE tokens ADD COLUMN name_cert_key TEXT NOT NULL;
        """
    )
    database_version += 1

if database_version == 6:
    execute_sql(
        """
    ALTER TABLE tokens ADD COLUMN bearer_tk TEXT DEFAULT 'None';
    ALTER TABLE bot_config ADD COLUMN random_pix_pb TEXT;
        """
    )
    database_version += 1

if database_version == 7:
    execute_sql(
        """
    ALTER TABLE docscnh ADD COLUMN cpf TEXT;
    ALTER TABLE docscnh ADD COLUMN name TEXT;
        """
    )
    database_version += 1

if database_version == 8:
    execute_sql(
        """
    ALTER TABLE sold_balance ADD COLUMN quantity INTEGER NOT NULL DEFAULT 1;
        """
    )
    database_version += 1


execute_sql("UPDATE bot_config SET db_version = ?", (database_version,))

execute_sql("UPDATE users SET is_action_pending = 0")

execute_sql("UPDATE docscnh SET pending = 0")

save = lambda: db.commit()
