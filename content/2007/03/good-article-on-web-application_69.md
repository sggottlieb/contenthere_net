Title: Good Article on Web Application Security Vulnerabilities
Date: 2007-03-25T12:30:00.002Z
Modified: 2015-01-06T11:32:49.734Z
Category: misc
Tags: security
Slug: 2007/03/good-article-on-web-application_69
Authors: Seth Gottlieb

The <span class="blsp-spelling-error" id="SPELLING_ERROR_0">PHP</span> programming language has historically gotten a bad rap in the area of security. While the language itself has had some vulnerabilities, three other aspects have (in my opinion) played a larger role:  

  
 *   <span class="blsp-spelling-error" id="SPELLING_ERROR_1">PHP</span> is an easy language to learn so there are a lot of unsophisticated beginners with no awareness of security holes writing web applications on it.
  
 *   The rise of <span class="blsp-spelling-error" id="SPELLING_ERROR_2">PHP</span> coincided with a rise in community content applications (bulletin boards, blogs, Nukes) where external, untrusted users could insert their own content with potentially malicious payloads.
  
 *   The <span class="blsp-spelling-error" id="SPELLING_ERROR_3">PHP</span> programming community was a little late in adopting web application frameworks. Good frameworks provide the plumbing for a web application and take care of security holes so that the custom code that developers write doesn't have to worry as much about known hacker exploits.
  

  
Two of these three factors are rapidly changing. The <span class="blsp-spelling-error" id="SPELLING_ERROR_4">PHP</span> development community is getting more sophisticated from a technology perspective and frameworks are getting better and are becoming more commonly used.  
  
I am seeing more and more articles concerning security on <span class="blsp-spelling-error" id="SPELLING_ERROR_5">PHP</span> developer websites and magazines. For example, there is a [really good article](http://ez.no/community/articles/dangers_of_csrf_and_xss) on the [None](http://ez.no/) site about Cross Site Request Forgery (<span class="blsp-spelling-error" id="SPELLING_ERROR_7">CSRF</span>) and Cross Site Scripting (<span class="blsp-spelling-error" id="SPELLING_ERROR_8">XSS</span>). It goes over how a hacker can inject malicious code into your site and how to protect yourself against these attacks. Here is a hint... never trust anything that a user enters. For more reading, check out Rob Miller's [None](http://php.robm.me.uk/).  
  
If you have been holding back on using a framework, I would reconsider. Most of the <span class="blsp-spelling-error" id="SPELLING_ERROR_10">PHP</span> frameworks have filter components (The <span class="blsp-spelling-error" id="SPELLING_ERROR_11">Zend</span> Framework has their [None](http://framework.zend.com/manual/en/zend.filter.html). [None](http://ez.no/ezcomponents) has a [User Input component](http://ez.no/doc/components/view/latest/%28file%29/classtrees_UserInput.html)) that disarms potentially hazardous user input. Tapping into the collective intelligence about security can free your own mind to building better, more effective web applications.
