# Shire of Chittering -- Solution Report

## 1. Executive Summary

## 2. Overview

> In response to the Shire of Chittering, our team has been tasked with developing an application that will act as centralized platform for the residents within the Chittering Region. As discussed with CEO Malinda Prinsloo, there is a need for more effective announcements to residents about upcoming events, a more cost effective solution for sending important alerts and a need for making payments to the Shire for Services and Rates more accessible to all residents.


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
    >
    >     ...
    >
    > _3.2.B._ **Events & Community News** -- 
    <i><small>( see <b><a href="#b-events--community-news-–">appendix – B</a></b> )</small></i>
    >
    >     Within the Shires 'Strategic Community Plan', they introduce their strategic objective for 

    _[Disregard below...]_
    >     The Shire have listed having "An active and supportive community" Objective [𝚜¹⋅¹] . The Strategic Objective table within importance of Objective 1.1 [𝚜¹⋅¹] under  within the Community Aspiration Strategic Community Plan, highlights the some of the key services & businesses as usual programs/events that contributes in bringing the community together. found in the most recent Shire of Chittering's 'Corporate Business Plan¹'.
    >
    >     Further information about [𝚜₁.₁] such as the events outlined can also be found in the 2023 - 2024 Budget Project Highlights Plan / Rates Brochure⁽²⁾.
    > - <table><tr><th>#</th><th>References</th><th></th></tr><tr><sup><td><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027"><sup>[1]</sup></a></td><td><sup><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027">Shire of Chittering Coorporate Business Plan 2022 - 2027</a></td><td><sup><small><b>Strategic Objective 1.1</b></small><br><i>page.</i><small> 27</small></sup></td></sup></tr><tr><sup><td><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027"><sup>[2]</sup></a></td><td><sup><a href="https://www.chittering.wa.gov.au/documents/584/corporate-business-plan-2023-2027">2023 - 2024 Budget Project Highlights / Rates Brochure</a></td><td><sup><small><b>Strategic Objective 1.1</b></small><br><i>page.</i><small> 3</small></sup></td></sup></tr></table>
    >
    > _3.2.C._ **Emergency Alerts & Broadcasts** -- 
    <i><small>( see <b><a href="#c-emergency-alerts--broadcasts-–">appendix–C</a></b> )</small></i>
    >
    >       As highlighted in the Chittering Corporate Business Plan⁽¹⁾, a constant global threat that the Shire faces is the potential disaster of bushfires. An objective of the Shire is to implement planning measures and further development to minimise the impact of this threat.
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
        
    [https://www.bpoint.com.au/payments/chittering]

  > _3.3.B._ **Events & Community News** -- 
    <i><small>( see <b><a href="#b-events--community-news-–">appendix – B</a></b> )</small></i>

      ...

  > _3.3.C._ **Emergency Alerts & Broadcasts** -- 
    <i><small>( see <b><a href="#c-emergency-alerts--broadcasts-–">appendix – C</a></b> )</small></i>

      ...

## 4. Gap Analysis

  >### 4.𝚜1. _(Solution-1)_
  >
  > <table>
  >   <tr><th>Objectives</th><th>Current-State</th><th>Desired-State</th><th>Gaps</th><th>Action to Bridge the Gaps</th></tr>
  >   <tr><td><i>[𝚜1.1]</i><br><b>Query Payment Information</b></td><td>Unable to check current payment information<br><i>(i.e., remaining rates, etc.)</i></td><td>Allow residents to check their own balances</td><td><table><tr><td>No self service<sup>[i]</sup></td></tr><tr><td><br>Requesting Information Requires Staff assistance<sup>[ii]</sup></td></tr><tr><td>Can only make request during the opening hours at the shire<sup>[iii]</sup></td></tr><tr><td>Difficult to do if you don't live near Bindoon.<sup>[iv]</sup></td></tr></table></td><td><table><tr><td>Implement a Secure Sign in system, allowing self service payment queries.<sup>[i]</sup></td></tr><tr><td>Connect application queries to Rates & Payment database to query based of account info.<sup>[ii]</sup></td></tr><tr><td>Implement a 24/7 access system, without needing shire assistance.<sup>[iii]</sup></td></tr><tr><td><br>No need to go in person.<sup>[iv]</sup></td></tr></table></td></tr>
  >   <tr>
  >    <td><i>[𝚜1.2]</i><br><b>Increase Community Awareness</b></td><td><table><tr><td>Some residents are unaware of events happening in and around Chittering.<sup>[v]</sup></td></tr><tr><td>Events are advertised on social media sites.<sup>[vi]</sup></td></tr></table></td><td><table><tr><td>All Residents that want to be made aware of events are made aware.<sup>[v]</sup></td></tr><tr><td>No social media required to engage with comminity.<sup>[vi]</sup></td></tr></table></td><td><table><tr><td>Event announcements & Community News reaches all residents.<sup>[v]</sup></td></tr><tr><td>Not all residents have social media.<sup>[vi]</sup></td></tr></table></td><td><table><tr><td>Create an notification system.<sup>[v]</sup></td></tr><tr><td>Create a central News & Announce Portal without the need of social media.<sup>[vi]</sub></td></tr></table></td>
  >   </tr>
  >   <tr>
  >    <td><i>[𝚜1.3]<i><br><b>Increase Bush-Fire Danger Awareness & Compliance</b></td><td><table><tr><td>FDR information is only available via Emergency WA or the Shire of Chittering's Website<sup>[vii]</sup></td></tr><tr><td>Residents with property have to seek fire-break compliance dates<sup>[viii]</sup></td></tr></table></td><td><table><tr><td>Make it more accessible for residents personal devices.<sup>[vii]</sup></td></tr><tr><td>Residents no longer require to seek compliance dates.<sup>[viii]</sup></td></tr></table></td><td>Currently requires frequent monitoring by residents.</td><td><table><tr><td>Display Current FDR for Swan Inland North<sup>[vii]</sup></td></tr><tr><td>Enable automatic push notifications when FDR is high and/or Fire Restrictions are in-place.<sup>[viii]</sup></td></tr></table></td>
  >   </tr>
  >   <tr>
  >    <td><i>[𝚜1.4]</i><br><b>Broadcast Bushfire Alerts & Fire Restrictions</b></td>
  >    <td><table><tr><td>Bushfire Restrictions & Alerts via SMS subscriptions, require mobile signal at the time of the issued alert.<sup>[ix]</sup></td></tr><tr><td>Currently paying for each broadcasted SMS through <b><i>Telstra Integrated Messaging Service</i></b> - (<b>TIMS</b>)<sup>[x]</sup></td></tr></table></td>
  >    <td><table><tr><td>Increase the reliability of the alert system ensuring that all residents are aware of active alerts.</td></tr><tr><td>Reduce the costs of using sending emergency SMS alerts to residents.</td></tr></table></td>
  >    <td><table><tr><td>Residents in "black-spot" areas may not receive alerts at the time they go into affect.<sup>[ix]</sup></td></tr><tr><td>TIMS is expensive for each alert sent.<sup>[x]<br><i>[see <a href="#figure-e">Fig: E</a>]</i></sup></td></tr></table></td>
  >    <td><table><tr><td></td></tr><tr><td></td></tr></table></td>
  >   </tr>
  > </table>

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
  > - $\large{v}$ _: Total Expense on SMS service this year :_ $\large{v} = \large{c} \times \large{f} = \small{\$1500.00} \times 42 = \small{\$63000.00}$ $\small{^+/_-}$ 

  >
  > |Objectives|Current-State|Desired-State|Gaps|Action to bridge the gaps|
  > |---------:|:------------|:------------|:---|-------------------------|
  > | _<small>[<b>A</b></small> - 𝚜1.1.<small>]</small>_<br>**Residents Query<br>Payement Progress** | Residents Are required to track their own progress, or must call the shire. | Residents can query their progress without contacting the shire. | <li>Self service requests.</li> | Create an effective system that allows residents to check their own rates information. |
  > |_[**B** - 𝚜1.2.]_<br>**Increased Community Awareness**| Some residents are not aware of events happening in and around Bindoon. | All residents are aware of things happening in the community. | <li>Residents that prefer not to use facebook may not hear about events.</li> | Broadcast Event Annou |
  > ||||||
  > | **Rates Payment<br> System** |  |  |  |  |
  > | **Events <br>& Community<br>News** |  |  |  |  |
  > | **Emergency Alerts <br>& Broadcast** |  |  |  |  |

  >### 4.𝚜2. _(Solution-2)_
  >
  > |Objectives|Current-State|Desired-State|Gaps|Action to bridge the gaps|
  > |---------:|:------------|:------------|:---|-------------------------|
  > | **Rates Payment<br> System** | Payment options for property rates can be done via BPoint on the Shire of Chittering's Website, Cheque, BPay (single or reoccurring) telephone, or in person.  | Be able to view Property Rate information, make payments and queries with ease. |  |  |
  > | **Events <br>& Community<br>News** | Community outreach is lacking for residents that don't live within the town of Bindoon. Those residents are only made aware of events if they follow the Shire on social media or use the website. | Increase resident connectivity and involvement from those living in the broader "Satelite Community" beyond the town of Bindoon. |  |
  > | **Emergency Alerts <br>& Broadcast** | Emergency Broadcasted SMS messages are costing the Shire upward of $63,000.00 a year. The service is affected to those who are in "black-spot" mobile areas. | Get emergency bushfire alerts to all affected residents whilst dropping the overall costs to the Shire. |  | - Implement a bushfire togglable service on the application that gives residents the option to subscribe to alerts that may affect them (Harvest bans), whilst providing a non-surpressable alert system for emergency broadcasts and total fire bans.<br><br>- By implementing a calendar system for recieving pre-schedualed alerts like total fire bans, it can allow for a timed alert to be scheduled as soon as residents come into signal so the alert comes through regardless of their signal as it comes into effect.  |

## 5. Preliminary Research

## 6. Possible Solutions


- ### 6.1. Business Impacts

  #### 6.1.1. **Solution - #1**

    - **S1.A.  Rate Payment System**

          ...

    - **S1.B. Events & Community News**

          ...

    - **S1.C. Emergency Alerts & Broadcasts**

          ...

  #### **Solution - #2**
    
    - **S2.A. Rate Payment System**

          ...

    - **S2.B. Events & Community News**

          ...

    - **S2.C. Emergency Alerts & Broadcasts**

          ...

- ### 6.2. Implementation Constraints

  #### **Solution: 1**

      ...

  #### **Solution: 2**

      ...

- ### 6.3. Overall Effectiveness

  #### **Solution: 1**

      ...

  #### **Solution: 2**

      ...

- ### 6.4. Refection to Industry Standards (Best Practices)

  #### **Solution: 1**

      ...

  #### **Solution: 2**

      ...
