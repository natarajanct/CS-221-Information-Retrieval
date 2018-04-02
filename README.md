CS 221 - Information Retrieval - Winter 2018

Project 1 - Text Processing Functions

word_frequencies.py - Has a method/function that reads in a text file and returns a list of the tokens in that file. (Independent of Capitalization). Has a method/function that counts the number of occurrences of each word in the token list and also has a method that prints out the word frequency counts onto the screen and the print out is ordered by decreasing frequency.

intersection_of_two_files.py - The program takes two text files as arguments and outputs the number of tokens they have in common.

reducing_two_word_frequency_counts.py - The program takes two word-frequency maps (given in two separate input text files) and creates an output word-frequency count file where the counts are added. The input and output files are of the form “word, count”, one of these per line. (Assumption - the input files are ordered alphabetically).

Project 2 – The Spacetime Crawler (Crawling ICS domain of UCI for building a search engine)

Team - Natarajan chidhambharam, Adithya Srinivasan, Utkarsha Ganla
 
The crawler is stand alone, but shares data with the rest of the crawlers in the class. Each crawler has 
their own frontier in a server in ICS department of UCI, and can manage this frontier. The frontier does a lot of the heavy 
work. The crawler will be given 1 URL at a time and should proceed to download and process it. 
 
Step 1 Getting the project - git clone https://github.com/Mondego/spacetime‐crawler 
 
Step 2 Installing the dependencies - pip install spacetime
 
Step 3 Writing the required classes, functions, and parameters 

function extract_next_links (applications/search/crawler_frame.py) - This function extracts links from the content of a downloaded webpage. 
Input:  raw_content_obj 
Output: list of URLs in string form with each URL should in their absolute form. 

Each object contains information that can be used to make an informed decision for link 
extraction. The detailed description of each field is given below: 
- url: The source link given by the frontier. 
- content: The raw_content that was downloaded by the crawler client using the given 
URL. 
- error_message: The HTTP error message/ custom error message in case of failure. 
- headers: The HTTP response headers returned on download. 
- http_code: The HTTP response code sent by the server on download. 
- is_redirected: Boolean that declares if there were redirects when downloading this URL. (True if the URL was redirected, False if not) 
- final_url: In case of redirects (i.e. is_redirected = True), the final URL where the resource was found. If there were no redirects, this URL is left as None. 
 
function is_valid (applications/search/crawler_frame.py) - This function returns True or False based on whether a URL is valid and must be downloaded or not. 
Input: URL is the URL of a web page in string form 
Output: True if URL is valid, False if the URL otherwise. Robot rules and duplication rules are checked separately and should not be checked here. This is a place to 
1. filter out crawler traps (e.g. the ICS calendar) 
2. double check that the URL is valid and in absolute form. Returning False on a URL does not let that URL to enter your 
frontier. 
 
Step 4 - Analytics 
Along with crawling the web pages, the crawler keeps track of some information, and writes out 
to a file at the end. Specifically, it : 
1. Keeps track of all the subdomains that it visited, and counts how many different URLs it has 
processed from each of those subdomains 
2. Counts how many invalid links it received from the frontier, if any 
3. Finds the page with the most out links (of all pages given to your crawler) 

Project 3 - Search Engine
