# Shire of Chittering -- Solution Report

## 1. Executive Summary

## 2. Overview

> In response to the Shire of Chittering, our team has been tasked with developing an application that will act as centralized platform for the residents within the Chittering Region. As discussed with CEO Malinda Prinsloo, there is a need for more effective announcements to residents about upcoming events, a more cost effective solution for sending important alerts and a need for making payments to the Shire for Services and Rates more accessible to all residents.
>
> This is the third year that North Metropolitan TAFE has partnered with The Shire of Chittering, As a result of this our team will be working with existing code bases, and prior implementations for features such as, FDR display board, notification system (firebase), etc...

## 3. Business Requirements

- ### 3.1. High Level Objectives / Use-Cases

    > After our first meeting with Shire CEO -- Melinda Prinsloo & Emergency Service Coordinator -- Jodie Connell, several crucial elements emerged that are fundamental for the final application.
    >
    >
    > >_[Note: the following objectives will be referred to throughout the document:]_
    > >
    >
    > #### _A._ **Rate Payment System** --
    >
    >
    >     This objective is the most crucial, Melinda Prinsloo has highlighted the need to provide functionality that allows residents in the Chittering Region to view and make payments on their annual property rates from within the application.
    >
    > #### _B._ **Events & Community News** --
    >
    >     Previously, residents in the region have spoken about how they weren't aware of events being held in the townsite of Bindoon. Despite many different approaches to uplift announcements there is still a need to maximise the outreach of news and events. As discussed in our meeting with the Shire on the 28ᵗʰ March 2024, Melinda mentioned that they require a central hub for the local community to receive news about upcoming events. This will help to provide an equal opportunity for those who live more remote than others, to be able to hear announcements on events and information.
    >
    > #### _C._ **Emergency Alerts & Broadcasts** --
    >
    >     Emergency Service Coordinator, Jodie Connell has expressed the importance of getting bushfire information and alerts out to the community in a timely efficient manner. With the vast rural area being abound by natural bushland, bushfires happen frequently throughout the bushfire season. In response to harsh conditions (such as high UV forecasts), the Shire will impose Harvest-Ban and / or Total-Fire-Ban days under the instruction from the Department of Fire and Emergency Services (DFES). 
    >
    >       ɪ. We have been tasked with creating a way to broadcast alerts whenever restrictions are in effect to users who are subscribed to the service. There is an importance to develop a creative solution for alerts to reach those in mobile "black-spot" areas as it is critical information that can carry offenses if not obeyed.
    >
    >      ɪɪ. The final application also needs to display the current Fire Danger Rating (FDR) system for the Swan Inland North section. !!TODO: mention previous group progress!!
    >
    >     ɪɪɪ. Depending on the time constraints in the projects developmental stage, the Shire has also expressed an interest to have a display showing active bushfire alerts affecting the area and essential information for new residents regarding their responsibility and requirements in maintaining fire breaks for key inspections dates.

- ### 3.2. Relation to Strategic Plan
  
  As per the Shire of Chittering's Strategic plan, they have developed the following five strategic objectives that stem from their core community aspirations: &#160;&#187;&#160;&#160;<small>[<u>see below</u>: <a href="#figure-D"><u><b><i>figure</b></u>&#8202;<b>ᴰ</b></i></a>]</small>

  ---

    <table>
    <tr>
      <th></th>
      <th width="30%">Stategic Objectives</th>
    </tr>
    <tc><td width="25%">
    <table width="100%" id="figure-D">
    <tr><th column=""><i><h4 align="right"><u>Figure:&#8202;</u>[<small>D</small>]&nbsp;&nbsp;&nbsp;&nbsp;</h4></i></th>
    <tr>
      <td><image src="https://github.com/Nathan-Bransby-NMT/Dual-Diploma-2024/blob/main/Semester-1/Innovation-Project/Client-Project/SoC_StrategicObjectives.png?raw=true" alt="Shire of Chittering's Strategic Objective figure [2023 - 2027]."></image>
      </td>
    </tr>
    <tr>
      <td>
      <sub><u><b>Reference</u></b>:<br>
      <span style="padding-left: 20px">
      •&#8239;<i><a href="">Shire of Chittering Coorporate Business Plan</i> [2022 - 2027]</a><br>
      <span style="padding-left:30px">
      ⁍ <small><strong>Community Desired Outcomes</strong> 
      ‖ Page&#8202;26 </small>
      </sub>
      </td>
    </tr>
  </table>
    </td></tc>
    <tc><td width="40%">
    <table padding-left="20px">
      <tr>
        <td><b>𝚜<small>.1</small></b></td>
        <td><u><i>A connected safe & healthy community.</i></u></td>
      </tr>
      <tr>
        <td><b>𝚜<small>.2</small></b></td>
        <td><u><i>Sustainable living in a protected environment.</i></u></td>
      </tr>
      <tr>
        <td><b>𝚜<small>.3</small></b></td>
        <td><u><i>Improving infrastructure while retaining the rural amenity.</i></u></td>
      </tr>
      <tr>
        <td><b>𝚜<small>.4</small></b></td>
        <td><u><i>Support new and local business, with a focus on agriculture and tourism.</i></u></td>
      </tr>
      <tr>
        <td><b>𝚜<small>.5</small></b></td>
        <td><u><i>An engaged community with accountable and efficient governance.</i></u></td>
      </tr>
    </table></td></tc>
    </table>
    </p>

    ---

    >   _3.2.A._ **Rate Payment System** --
    <i><small>( see <b><a href="#a-rate-payment-system-–">appendix – A</a></b> )</small></i>
    >    - Reduces paper waste as residents will be able to opt out of future paper rate notices.<sup>[<b>s.2</b>]</sup>
    >    ...
    >
    > _3.2.B._ **Events & Community News** -- 
    <i><small>( see <b><a href="#b-events--community-news-–">appendix – B</a></b> )</small></i>
    >
    >    - encourages members in satellite areas to connect and engage with community events<sup>[<b>s.1</b>]</sup>
    >    - The Shire have listed having "An active and supportive community" Objective [𝚜¹⋅¹] . The Strategic Objective table within importance of Objective 1.1 [𝚜¹⋅¹] under  within the Community Aspiration Strategic Community Plan, highlights the some of the key services & businesses as usual programs/events that contributes in bringing the community together. found in the most recent Shire of Chittering's 'Corporate Business Plan¹'.
    > - **Note** -- _Further information about [𝚜₁.₁] such as the events outlined can also be found in the 2023 - 2024 Budget Project Highlights Plan / Rates Brochure⁽²⁾._
    > - <table><tr><th>#</th><th>References</th><th></th></tr><tr><sup><td><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027"><sup>[1]</sup></a></td><td><sup><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027">Shire of Chittering Coorporate Business Plan 2022 - 2027</a></td><td><sup><small><b>Strategic Objective 1.1</b></small><br><i>page.</i><small> 27</small></sup></td></sup></tr><tr><sup><td><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027"><sup>[2]</sup></a></td><td><sup><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027">2023 - 2024 Budget Project Highlights / Rates Brochure</a></td><td><sup><small><b>Strategic Objective 1.1</b></small><br><i>page.</i><small> 3</small></sup></td></sup></tr></table>
    >
    > _3.2.C._ **Emergency Alerts & Broadcasts** -- 
    <i><small>( see <b><a href="#c-emergency-alerts--broadcasts-–">appendix–C</a></b> )</small></i>
    >
    >    - As highlighted in the Chittering Corporate Business Plan⁽¹⁾, a constant global threat that the Shire faces is the potential disaster of bushfires. An objective of the Shire is to implement planning measures and further development to minimise the impact of this threat.
    >
    >      This aligns with the <u>_Shire of Chittering's strategic objective 2 -- Sustainable living in a protected environment._</u><sup>[<b>s.2</b>]</sup>
    >
    > - <table><tr><th>#</th><th>References</th><th></th></tr><tr><sup><td><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027"><sup>[1]</sup></a></td><td><sup><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027">Shire of Chittering Coorporate Business Plan 2022 - 2027</a></td><td><sup><small><b>Global Threats</b></small><br><i>page.</i><small> 6</small></sup></td></sup></tr></table>
    >

- ### 3.3. Current Systems & Infrastructure

  Listed below are the current systems / infrastructure that the shire of Chittering are using to handle the following:

  > _3.3.A._ **Rate Payment System** -- 
    <i><small>( see <b><a href="#a-rate-payment-system-–">appendix – A</a></b> )</small></i>

      There are currently multiple different ways for residents to make Property-Rates payments. The methods of payment include:
        
          I.  BPoint Online Paymentsᴵ (credit-card only) 
             
         II.  Manual BPay (savings, cheque or credit-card) 
              sent to the Biller Code: 55038 along with reference number
        
        III.  Reoccurring BPay (Direct Debit). 
              Information on rates notice.
        
         IV.  Payment via Telephone BPoint (Visa or MasterCard) 
              Number: 1300 276 468
        
          V.  In person payments.
              At the Shire's administration office (during open hours)

         IV.  Payments by; 
                - cash, 
                - cheque, 
                - money order, 
                - EFTPOS, 
                - MasterCard, 
                - Visa.

        IIV.  Mail Cheques to:
              The Shire of Chittering, PO Box 70 Bindoon WA 6502
        
    _ref: [Shire of Chittering's BPoint Page](https://www.bpoint.com.au/payments/chittering)_

  > _3.3.B._ **Events & Community News** -- 
    <i><small>( see <b><a href="#b-events--community-news-–">appendix – B</a></b> )</small></i>

      - Facebook.
      - Website.
      - Fliers & Posters.
      - Electronic Billboards around the town.
      - Word of mouth.
      - Community Notice Letters (postal)
      

  > _3.3.C._ **Emergency Alerts & Broadcasts** -- 
    <i><small>( see <b><a href="#c-emergency-alerts--broadcasts-–">appendix – C</a></b> )</small></i>

      - TIMS - Fire restriction SMS subscription service.

      - Facebook - Posts stating when fire bans & restrictions are coming into affect.

      - Website - About Fire Ratings & displays a FDR for the current day.

      - Emergency WA - External government site that displays FDR for regions as well as any active emergency alerts.

## 4. Gap Analysis / Preliminary Research

  >### 4.A. <u>Solution Gap-Analysis Table</u>
  >
  > <image src="https://github.com/Nathan-Bransby-NMT/Dual-Diploma-2024/blob/main/Semester-1/Innovation-Project/Assessments/AT1/Solution-1-Gap-Analysis.png?raw=true" alt="Solution-1, Gap Analysis"></image>
  > >
  > > _ref:_ [Solution-1-Gap-Analysis.xlsx](https://github.com/Nathan-Bransby-NMT/Dual-Diploma-2024/raw/main/Semester-1/Innovation-Project/Assessments/AT1/Solution-1-Gap-Analysis.xlsx)

  > ### _<u>Figure:</u>_ <b>E</b>
  >
  > #### Telstra Integrated Messaging Service (TIMS) Cost Analysis.
  >
  > - $\large n$ _: Total number of subscribed residents to SMS notifications._ $= 2000 \small ^+/_- $ _residents._
  >
  > - $\large c$ _: Costs_ $= \$1500.00 \small ^+/_-$ _per SMS Broadcast._
  >
  > - $\large f$ _: Frequency of alerts sent --_ _<small>(2024 fire-season to date).</small>_ $= 42.$
  > 
  > - $\small{T}$ _: Total SMS's sent this fire-season_ $:$ $\small{T} = \large{n} \times \large{f} = \small{2000} \times \small{42} = 84000$ $\small{^+/_-}$
  > - $\large{v}$ _: Total Expense on SMS service this year :_ 
  $\large{v} = \large{c} \times \large{f} = \small{\$1500.00} \times 42 = \small{\$63000.00}$ $\small{^+/_-}$ Per Year.

  > ### _<u>Figure:</u>_ **F** <br><br>Payment Gateway's / S.W.O.T Analysis Table
  >
  > - Payment Service / Gateway must meet the [PCI Compliance Checklist](https://business.gov.au/finance/payments-and-invoicing/choose-payment-methods) criteria.
  >
  > > #### Payment Gateway Workflow Model _[<u>figure : **F-I**</u>]_
  > >
  > > <image src="https://github.com/Nathan-Bransby-NMT/Dual-Diploma-2024/blob/main/Semester-1/Innovation-Project/Client-Project/Payment-Gateway-Workflow.png?raw=true" alt="A workflow diagram showing how payment gateways operate."></image>
  > > 
  > > | **<sub>F.I.</sub>** &nbsp;<small><i>[ Reference : [https://squareup.com/au](https://squareup.com/au/en/the-bottom-line/managing-your-finances/payment-gateway) ]</i></small>
  >
  > | _**Service**_ | **Strengths** | **Weaknesses** | **Opportunities** | **Threats** |
  > |---|---|---|---|---|
  > | [**BPoint**](https://www.bpoint.com.au/payments/chittering) _(current system)_ | - Allows Custom JavaScript Alterations | - Relies of redirecting the user to a BPoint payment page (out of application). |  - Allows customisation of the payment API's to meet the users needs. | - Payer must manually enter a reference number, which could be entered incorrectly. |
  > | [**Square**](https://squareup.com/au/en) | - [Customisable APIs & SDKs](https://developer.squareup.com/docs/payments-overview)<br> - Easy useability & setup <br> - Offer multiple eCommerce solutions<br> - Built in 24/7 security with end-to-end encryption. | - Requires the Shire changing current systems.<br>- Requires setting up the system. | - They offer physical [POS Hardware solutions](https://squareup.com/au/en/point-of-sale) that can use the same workflow as the online payment service<br> - Includes analytical tools | - Could create a centralised ecosystem, which can become a financial issue if subscription prices increase.<br>-   |

  > ### City of Swan's Online Rates Portal _(How to Guide)_
  >
  > - #### Relevant Document Content
  >
  >   1. Registering details.
  >      - Customer name & activation-key.
  >      - Create a password.
  >
  >   2. Signing into the portal.
  >  
  >   3. Using the portal.
  >
  >   4. Editing contact details.
  >
  >   5. Viewing rate notices & manage payments.
  >      - Create a direct debit.
  >      - Confirm your direct debit.
  >      - Create a payment arrangement.
  >
  >   6. View Current & Previous notices.
  >
  > > - _ref :_ [online-service-rates-portal.pdf](https://www.swan.wa.gov.au/awcontent/Web/Documents/Annual-Reports/online-services-rates-portal-how-to-guide.pdf)
  >

## 5. Possible Solutions

 ### 5.a. -- Solution #1

    In order to address the requirements being asked by the Shire of Chittering, I propose that we adhere to these following solution that cover the key objectives below:

        - I.   | Rates Payment System
        - II.  | Events & Community News
        - III. | Emergency Alerts & Broadcasts

    > Section I. Rates Payment System:
      
      To implement an effective system that benefits both residents and Shire staff, I propose the implementation of a self 
      service portal that allows residents to: 

          1. Make property rate payments, select appropriate installment period options.
          2. View any outstanding rates for the financial year.
          3. Get notified when rates are issues and/or due.
          4. Change payment details / options.
      
      In order to enhance security when requesting property payments and other sensitive information, I propose the following 
      solutions:

          5. Users can register accounts with a  one time registration process.

          6. Account information will be tied to each property's unique reference number and name of the addressee. 
             - This information can be found on the issued rate notice sent to the resident.
          
          7. Users will create passwords with email verification upon registering their accounts.
             - By implements an email verification, residents can recover accounts if details are lost.

          8. Information on account creation will be encrypted using Industry Best Practices & Standards.
             - This ensures password protection at all levels.

          9. Once user credentials are encrypted they can be stored in either:
             - The currently implemented database (with minimal amendments to the current table)
             - If the need arises, the creation of an separate database can be created after the account setup process.

            **Note**: Alterations WILL NOT impact how any of the current property information is stored and/or 
                      accessed by internal & external systems & practices.
          
    > Section II. Events & Community News:
          
      An additional requirement of the application is the implementation of a community platform, that will improve event & 
      community news announcements to the residents in the shire. As the Shire consists of multiple rural satellite towns,
      hearing the latest news & community information can be difficult for residents. 
      
      Highlighted in the Shires Strategic-Objectives for Connecting Communities, their strategic approach illustrates the 
      importance of supporting community events, social hubs and increasing community volunteering. 
      This demonstrates the importance of establishing an effective community outreach & engagement system, and how it is an 
      essential element to capture in the project. To support this ideology I propose we include the following elements:
           
          1. A togglable system that allows users to opt for notifications about upcoming events.
             - This ensures that residents and store-holders are aware of events as soon as they are announced.

          2. An Export event to calender feature. 
             - This will allow residents to export scheduled events straight from the application into their personal device. 

          3. The possibility of having a contact feature for resident feedback / questions.
             - The feature could include required fields such as contact information for non registered accounts.
             - The send messages will act as an email service for Shire staff as an alternative means of contact.

    > Section III. Emergency Alerts & Broadcasts:

      The Shire of Chittering being a rural area surrounded by natural bushland, means that bushfires are a annual threat to
      the community. Henceforth, addressing bushfire information guarantees that residents are made aware of what to do if a 
      bushfire occurs, as well as convey their responsibility in reducing the risks and support to emergency services during 
      the bushfire season. To administer the following requirements I propose the development of the following areas:
        
        1. A information page and/or links to current sources of information for residents to view what their requirements are.
           - This will aid in the reduction of bushfire threats & encourage resident compliance.
        
        2. Alerts and Highlight sections to notify residents when: 
           - Fire Restrictions come into affect
           - Leading up to Fire-Break compliance inspection dates.

        3. Emergency Service Information.
           - Contacts and Links to DFES
           - DFES, VFES, SES & VFS information (such as websites, contact details and volunteer recruitment dates)

        4. Display the current FDR for the Swan Inland North Area.

      Currently the Shire rely on a Subscription based SMS service (TIMS) to notify subscribed residents when they are required 
      to stop machine related activities during summer. How ever the costs to broadcast alerts are expensive. [see 5.figure: E]
      Another downside the the current broadcast system is that those subscribed will only receive alerts when they come into 
      effect if they are currently with-in mobile signal. The shire has many mobile 'black-spot' areas where there is no mobile 
      signal making it deadly when fire restrictions are put in place. Therefore I also propose the following features:

        5. Display information regarding any active or scheduled bushfire restrictions on the application.

        6. Create a togglable notification system for pre-scheduled fire restrictions.
           - Allow residents to subscribe for push notifications as an alternative to the current TIMS system.
        
        7. A feature that checks for updates whenever users come into mobile signal.
           - Checks for scheduled alerts.
           - Operational for users in 'dead-spot' areas.
           - Removes the current push activation system with one that can be pre scheduled. This revolutionizes the way 
             that users receive scheduled emergency alerts.
        
        8. The feature will operate entire free of charge to both resident & Shire cutting costs dramatically.

 ### 5.b. -- Solution #2

     ...

         - I.   | Rates Payment System
         - II.  | Events & Community News
         - III. | Emergency Alerts & Broadcasts

     > Section I. Rates Payment System:
       
       1. Simple verification method 
          - Only requires property reference number & addressed resident.

       2. Users can make one time payments from the application.

       3. 

     > Section II. Events & Community News:

       1. Hooks posts from the website.
       
       2. 

     > Section III. Emergency Alerts & Broadcasts:
       ...

- ### 6.1. Business Impacts

  #### 6.1.1. **Solution - #1**

    - **S1.A.  Rates Payment System**
        
        1. By implementing a built in rates payment & query system into the application, it will ease staff workload by 
          enabling residents to access rates services without the need of staff. This overall will increase customer support 
          satisfaction, and increase staff productivity.

        2. There will be a requirement to train Shire Staff, and the need to develop Community "How To" support material and/or 
          information sessions.

      ---

    - **S1.B. Events & Community News**

        1. Creating a central hub for community information, will increase attendance of events, better connecting the
           community together.
        
        2. By fostering a platform, a space is created for local advertisement opportunities which overall will boost local
           economy.

        3. By allowing residents to export event schedules from the application, into their personal device calendar encourages
           residents to attend the event as they can be notified prior to an event date.

      ---

    - **S1.C. Emergency Alerts & Broadcasts**

        1. By implementing in-app broadcast alert system, the Shire may be able to phase out of their current Emergency
           Broadcast system that is implemented by Telstra Integrated Messaging System (TIMS).
               
           - <u>TIMS is not a cost effective solution as each broadcast costs upwards of $1500 --- _[see [figure E](#figure-e)]_.</u>

        2. Makes sure that residents are made aware of active restrictions, therefore potentially reducing the number of emergency events creating less business interruptions throughout the year.

  ---

  #### **6.1.2. Solution - #2**
    
    - **S2.A. Rate Payment System**

        ...

    - **S2.B. Events & Community News**

        ...

    - **S2.C. Emergency Alerts & Broadcasts**

        ...

  ---

- ### 6.2. Implementation Constraints

  #### 6.2.1. **Solution - #1**

    - **S1.A.  Rates Payment System**

        1. Accessing existing database and making alterations to help secure / create user accounts.

        2. Residents support of the changing system may need some encouragement as the median age of residents are above the
           age of 40 so their acceptance of a technology based approach may be lower than the latter.
        
        3. Potential time constraints of implementing such a system may impact our ability to deliver all requirements.

      ---

    - **S1.B. Events & Community News**

        1. The ability for local businesses to utilise the platform without engaging the shire may decrease its effectiveness.

        2. Implementing a support enquiry platform may increase the number of emails received by Shire administration staff.
        
        3. Those less likely to adopt a technology based approach may not use the application if the process is too complex.

      ---

    - **S1.C. Emergency Alerts & Broadcasts**

       1. Phasing out of the current TIMS broadcast service will require a timely approach for residents to adopt the new system.

       2. Time constraints may effect our ability to implement the service, given the overall  scope of the project, testing requirements.

       3. Effectiveness of the Emergency Alert broadcasts from within 'black-spot' areas is still unknown.

  #### 6.2.2. **Solution - #2**

    - **S2.A.  Rates Payment System**

        ...

      ---

    - **S2.B. Events & Community News**

        ...

      ---

    - **S2.C. Emergency Alerts & Broadcasts**

        ...

- ### 6.3. Overall Effectiveness

  #### 6.3.1. **Solution - #1**

    - **S1.A.  Rates Payment System**

        * e

      ---

    - **S1.B. Events & Community News**

        ...

      ---

    - **S1.C. Emergency Alerts & Broadcasts**

        ...

  #### 6.3.2. **Solution - #2**

    - **S2.A.  Rates Payment System**

        ...

      ---

    - **S2.B. Events & Community News**

        ...

      ---

    - **S2.C. Emergency Alerts & Broadcasts**

        ...

- ### 6.4. Refection to Industry Standards (Best Practices)

  #### 6.4.1. **Solution - #1**

    - **S1.A.  Rates Payment System**

        ...

      ---

    - **S1.B. Events & Community News**

        ...

      ---

    - **S1.C. Emergency Alerts & Broadcasts**

        ...

  #### 6.4.2. **Solution - #2**

    - **S2.A.  Rates Payment System**

        ...

      ---

    - **S2.B. Events & Community News**

        ...

      ---

    - **S2.C. Emergency Alerts & Broadcasts**

        ...
