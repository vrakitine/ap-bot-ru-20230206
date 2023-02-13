from VaScript import getVaScript
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from TableClasses import Base, VaTrace

def setup(va):

    ### The VAOP variables setting

    va.defineVariable('The sequential number of the v-agent jump...p10', 0)
    va.defineVariable('The max number of the v-agent jump. It is for prevent looping...p11', 1000)
    va.defineVariable('The default locale language code...p12_0', 'en-US')
    va.defineVariable('The locale language code...p12_1', 'en-US')
    va.defineVariable('VA script...va_script', getVaScript()) #14
    va.defineVariable('The previous Action...previous action', 'Unknown') #15
    va.defineVariable('The current Action...current action', 'Action_000') #16
    va.defineVariable('Direction...direction', 'Direction_10') #17

    ### The DB setting


    hostname = 'localhost'
    database = 'postgres'
    username = 'postgres'
    pwd = 'Postg!2408'
    port_id = 5432

    url_object = URL.create(
        "postgresql",
        username=username,
        password=pwd,  # plain (unescaped) text
        host=hostname,
        database=database,
    )

    engine = create_engine(url_object, echo = False)

    # Флаг echo включает ведение лога через стандартный модуль logging Питона.
    # Когда он включен, мы увидим все созданные нами SQL-запросы. 
    session = sessionmaker(bind=engine)
    s = session()

    va.defineVariable('session...s', session())
