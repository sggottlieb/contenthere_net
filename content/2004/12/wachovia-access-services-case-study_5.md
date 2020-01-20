Title: Wachovia &quot;Content Access Services&quot; Case Study
Date: 2004-12-28T16:58:00.002Z
Modified: 2015-01-06T11:32:13.218Z
Category: misc
Tags: architecture
Slug: 2004/12/wachovia-access-services-case-study_5
Authors: Seth Gottlieb

[This](http://www.gilbane.com/case_studies/wachovia_case_study.html) case study by Gilbane's Content Technology Works (CTW), other than being an advertisement for IBM, shows a successful execution of a content integration strategy. The client is Wachovia, a very large financial services company (4th in the US), that grew out of acquisitions and, consequently, had several document repositories based on different technologies: IBM ImagePlus, FileNet, and Mobius. Libraries of digitized forms and documents are a huge deal in financial services companies because they need to keep every interaction with their customers at hand for customer service and regulatory reasons. As an aside, I once had a client that knew they had to do something major with imaging when the weight of their paper archives started to bow the floors and break the windows of their building.  
  

In order to integrate the business operations of the merged companies, Wachovia employees needed to work with information about their customers from multiple sources. Projects requests started surfacing about building desktop applications that integrated customer information from multiple departments. Rather than trying to migrate all the content over into one system, Wachovia started building a common content access layer with adaptors for different document management systems. The core technology they used was IBM's DB2 Information Integrator Content Edition which already came with a FileNet adaptor. Wachovia also built new adaptors for ImagePlus and Mobius and then added their own XML-based API to insulate Wachovia's client applications from the Information Integrator API.  
  

From reading the case study a couple of really good decisions stand out.  
  

*   Rather than adopt a strategy of migrating all content into a single system such as FileNet, Wachovia chose an integration approach where heterogeneous systems could coexist. This makes sense for several reasons:  
      
    
    
    *   __It is cheaper.__ Migrating terrabytes of content from one format to another has a huge up front cost.  
          
        
    *   __It leverages existing investments.__ Not just licensing but also customization, integration and training.  
          
        
    *   __It is lower risk.__ Wachovia does not have to bet the business on one technology. There is so much volatility in the marketplace that no one knows what is going to be a market leader and what will fall behind.  
          
        
    *   __It allows best of breed selection.__ Different groups may have different needs that are best satisfied with different technologies.  
          
        
    
    
      
      
    
*   Rather than have their client applications access the Information Aggregator API directly, Wachovia added an abstraction layer. This will enable Wachovia to more easily swap out Information Aggregator if a better technology comes along.  
      
    

  
  
In all, I think this is an excellent approach to the vision of "Enterprise Content Management." It is practical, cost effective and reduces dependency on a single provider.  
  
