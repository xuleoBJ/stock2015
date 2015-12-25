from ConfigParser import SafeConfigParser
import ConfigParser
import codecs  

config = ConfigParser.ConfigParser()
cfgfile='config.ini'
#config.read('config.ini')
config.readfp(codecs.open(cfgfile, "r", "utf-8-sig"))

stockIDMarketList=config.get("stock","stockIDMarket").split(',')
stockIDList=config.get("stock","stockIDList").split(',')

patternRecDateListSH=[]
patternRecDateListSZ=[]
patternRecDateListCYB=[]

def updatePetternRectDateList():
    config.set("patternRecDate", "SH",",".join(patternRecDateListSH))
    config.set("patternRecDate", "SZ",",".join(patternRecDateListSZ))
    config.set("patternRecDate", "CYB",",".join(patternRecDateListCYB))
    updateConfig()

def creatConfig():
    config = SafeConfigParser()
    config.read('config.ini')
    config.add_section('stock')
    config.set('stock', 'stockID', '999999')

    config.add_section('GDP')
    config.set('GDP', '2013', '53.8')
    config.set('GDP', '2014', '53.8')

    config.add_section('patternRecDate')
    config.set('patternRecDate', 'SH', '')
    config.set('patternRecDate', 'SZ', '')
    config.set('patternRecDate', 'CYB', '')

    config.add_section('softInfor')
    config.set('softInfor', 'installdate', '20150816')

    config.add_section('proxy')
    config.set('proxy', 'enable', '0')
    config.set('proxy', 'host', '10.22.96.29')
    config.set('proxy', 'port', '8080')
    config.set('proxy', 'username', '')
    config.set('proxy', 'password', '')

    with open('config.ini', 'w') as f:
        config.write(f)

def updateConfig():
    with open('config.ini', 'w') as f:
        config.write(f)

if __name__=="__main__":
    pass
