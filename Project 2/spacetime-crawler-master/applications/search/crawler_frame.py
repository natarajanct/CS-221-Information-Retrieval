import logging
from datamodel.search.UganlaAdithyasNchidham_datamodel import UganlaAdithyasNchidhamLink, OneUganlaAdithyasNchidhamUnProcessedLink, add_server_copy, get_downloaded_content
from spacetime.client.IApplication import IApplication
from spacetime.client.declarations import Producer, GetterSetter, Getter, ServerTriggers
from lxml import html,etree
import re, os
from time import time
from uuid import uuid4

from urlparse import urlparse, parse_qs
from uuid import uuid4

logger = logging.getLogger(__name__)
LOG_HEADER = "[CRAWLER]"

@Producer(UganlaAdithyasNchidhamLink)
@GetterSetter(OneUganlaAdithyasNchidhamUnProcessedLink)
@ServerTriggers(add_server_copy, get_downloaded_content)
class CrawlerFrame(IApplication):

    def __init__(self, frame):
        self.starttime = time()
        self.app_id = "UganlaAdithyasNchidham"
        self.frame = frame


    def initialize(self):
    	global countInvalid
        try:
            file = open("AUN_subdomains.txt","r") 
            for line in file: 
                line=line.split(":")
                subdomainDictionary[line[0]]=int(line[1])
        except IOError:
            file = open("AUN_subdomains.txt","w") 
            
        file.close()
        
        
        try:
            file = open("AUN_outlinks.txt","r") 
            for line in file: 
                line=line.split(":")
                linksDictionary[line[0]]=int(line[1])
        except IOError:
            file = open("AUN_outlinks.txt","w") 
        file.close()
        
        try:
            file=open("AUN_stats.txt","r")
            line=file.readline()
            if len(line)>1:
                countInvalid=line.split(":")[1]
            
        except IOError:
            file=open("AUN_stats.txt","w")
            
        file.close()

        self.count = 0
        l = UganlaAdithyasNchidhamLink("http://www.ics.uci.edu/")
        print l.full_url
        self.frame.add(l)

    def update(self):
        unprocessed_links = self.frame.get(OneUganlaAdithyasNchidhamUnProcessedLink)
        if unprocessed_links:
            link = unprocessed_links[0]
            print "Got a link to download:", link.full_url
            downloaded = link.download()
            links = extract_next_links(downloaded)
            for l in links:
                if is_valid(l):
                    self.frame.add(UganlaAdithyasNchidhamLink(l))

    def shutdown(self):
    	 #write analytics to file
        file=open("AUN_subdomains.txt","w")
        for subdomain,count in subdomainDictionary.items():
            file.write(subdomain+":"+str(count)+"\n")
        file.close()
        
        file=open("AUN_outlinks.txt","w")
        for link ,cnt in linksDictionary.items():
            file.write(link+":"+str(cnt)+"\n")
        file.close()
        
        file=open("AUN_stats.txt","w")
        file.write("INVALID LINKS:"+str(countInvalid)+"\n")
        file.write("SUB DOMAIN WITH MAX OUTLINKS:"+str(max(subdomainDictionary.iterkeys(), key=lambda k: subdomainDictionary[k]))+"\n")
        file.write("PAGE WITH MAX OUTLINKS:"+str(max(linksDictionary.iterkeys(), key=lambda k: linksDictionary[k]))+"\n")
        file.close()

        print (
            "Time time spent this session: ",
            time() - self.starttime, " seconds.")

from bs4 import BeautifulSoup
from urllib2 import urlparse as u  
    
def extract_next_links(rawDataObj):
    outputLinks = []
    '''
    rawDataObj is an object of type UrlResponse declared at L20-30
    datamodel/search/server_datamodel.py
    the return of this function should be a list of urls in their absolute form
    Validation of link via is_valid function is done later (see line 42).
    It is not required to remove duplicates that have already been downloaded. 
    The frontier takes care of that.
    
    Suggested library: lxml
    '''
    for link in soup.find_all('a'):
        link=link.get('href')
        if not link or link.startswith("mailto") or len(link)<=1 or link.startswith(".") or "?" in link or '\u' in link or rawDataObj.is_redirected: 
            continue
        
        if(link==currentpage):
            continue
        elif(link[0]=="#"):     #starts with #
            link=currentdomain+link[1:]
        elif (link[0]=='/'):    #starts with /
            link=currentdomain+link
        elif (not (link.startswith("http") or link.startswith("http"))):
            link=currentdomain+'/'+link  # starts with characters other than http/https
            print("******"+link)
        count+=1
        if link and all(ord(char)<128 for char in link):
            outputLinks.append(link)
        
        hname=u.urlparse(rawDataObj.url).hostname
        if ".ics" in hname:
            subdomain=hname[:hname.index(".ics.uci.edu")]
            if subdomain == "www":
                subdomain="ics"
        else:
            subdomain="ics"
            
        #count of links in subdomain
        subdomainDictionary[subdomain]=subdomainDictionary.get(subdomain,0)+1
        
    linksDictionary[rawDataObj.url]=linksDictionary.get(rawDataObj.url,0)+count


    return outputLinks

def is_valid(url):
    '''
    Function returns True or False based on whether the url has to be
    downloaded or not.
    Robot rules and duplication rules are checked separately.
    This is a great place to filter out crawler traps.
    '''
    global countInvalid
    parsed = urlparse(url)
    if re.search("(\d{4})[/.-](\d{2})[/.-](\d{2})", parsed.path):
        print "Date found in link"
        return False
    if "twitter" in url or "facebook" in url or "instagram" in url or "linkedin" in url:
        return False

    if parsed.scheme not in set(["http", "https"]):
        return False
    try:
        isValid = return ".ics.uci.edu" in parsed.hostname \
            and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4"\
            + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
            + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
            + "|thmx|mso|arff|rtf|jar|csv"\
            + "|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())
        if not isValid:
            
            #increment invalid links count
            countInvalid+=1
            
        return isValid


    except TypeError:
        print ("TypeError for ", parsed)
        return False

countInvalid=0
subdomainDictionary={}
linksDictionary={}