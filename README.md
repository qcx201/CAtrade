---
title: A prospectus on the Canada-US Trade War
date: 2025-03-24
categories: [economics]
tags: [trade war, Canada]
---

<!-- # A prospectus on the Canada-US Trade War -->

Why did Donald Trump start an unnecessary trade war with Canada? The consensus seems to be for no good reason.

His formal justifications are nebulous, but hover around border security and the US trade deficit with Canada. These reasons, however, are either detached from reality or based on a flawed understanding of how bilateral trade works.

Canada's contribution to US border problem is negligeable. Less than xx% illegal migrants come from Canada, and less than 1% of fentanyl in the US comes from Canada. [SOURCE] Almost a rounding error.

The trade deficit with Canada is dwarfed by those of other US trade partners like China and Germany. [SOURCE]

So why did he really start all this trouble? My favourite pet theory is that he did not like being [cuckolded](https://www.urbandictionary.com/define.php?term=Cuckold) by Justin Trudeau (even though the President has had a [storied history of alleged adulteries](https://www.businessinsider.com/trump-melania-stormy-daniels-affairs-marriages-timeline-2018-3)).

It goes back to a G7 summit in 2019, where a photo of Trudeau kissing First Lady Melania Trump, who was holding the oblivious President's hand, went viral. One French (of course) news outlet reporting on this lead with ["look of lust"](https://www.france24.com/en/20190827-papers-indonesia-names-new-capital-borneo-israel-lebanon-melania-trudeau-g7-photo) in the headline.

<br>
<div style="text-align: center; width: 100%;">
<img src="https://github.com/user-attachments/assets/5d8a43b6-657d-483d-97ab-13966278c6e4" alt="Justin Trudeau and Melania Trump stand next to Donald Trump in Biarritz, France, on 25 August. Photograph: Carlos Barría/Reuters" width="600"/>
</div>
<br>

The first daughter was not spared the Trudeau photo trap either. Following Trudeau's 2017 visit to Washington, one viral tweet wrote, ["Get someone that looks at you the way Ivanka Trump looks at Justin Trudeau,"](https://x.com/Phil_Lewis_/status/831280292379910144?t=EAPxWbPN6pyIdn-oeZOecQ&s=19) accompanying a snapshot of Ivanka Trump gazing at the Prime Minister with a pondering hand on her chin.

<br>
<div style="text-align: center; width: 100%;">
<img src="https://github.com/user-attachments/assets/4b67b532-9ce9-4f73-9ca3-a5631cd5c578" alt="Ivanka Trump and Justin Trudeau at a roundtable discussion at the White House on Monday. Photograph: Saul Loeb/AFP/Getty Images" width="600"/>
</div>
<br>

Say what you will about Justin, but our boy is handsome. And there is definitely animosity there from the big man in DC/Mar-a-Lago.

However ridiculous (and hilarious) these or other reasons for Trump's tariffs are, Canada is now in a trade war against the US, its closest historical trade partner.

Mark Carney, the new Prime Minister replacing Trudeau after the latter's resignation, said after his Liberal Party's election victory that ["Canada will win" the trade war.](https://www.bbc.com/news/articles/c36wkg47z1po.amp) Pierre Poilievre, leader of the main Conservatives opposition, also stated that he [favors a retaliatory response](https://youtube.com/shorts/4ZP7V5cxKPs?si=hMU9ef43AnjcC4nY) to US tariffs. Both major contenders to become the Prime Minister in the coming election this year have stated clear intentions to decouple from the United States in trade relations. [SOURCE]

How might this play out for Canadian industries and workers? Let's first take a look at the current state of affairs between Canada and its main trade partners. Then we'll discuss how the proposed tariffs and counter-tariffs may influence Canada's trade patterns and the effect on jobs, wages, and prices using a simple open economy general equilibrium model.


## Canada's Trade Partners

To understand how Canada's trade balance might evolve under the tariffs, let's first look back at the good old days of 2024, the most recent year before the Trump regime.

In 2024, imports from the US totaled $360 billion, constituting about half of all $744 billion Canadian imports. Canadian imports from the entire [European Economic Area plus UK and Switzerland](https://www.gov.uk/eu-eea) (EEA+ for short; these are pretty much the Western European countries) totaled $103 billion, less than a third of US imports. After the US, China is the next largest single-country import partner to Canada at $88 billion.

<figure>
    <figcaption align="center" style="font-size:16">
        <b>Canada's Top Import Partners (2024)</b>
    </figcaption>
    <img src='https://github.com/JackQCXie/CAtrade/blob/master/figures/03-import_partners.png?raw=true' alt=''/>
    <figcaption align="left">Data source: ISED Canada | Figure by author.</figcaption>
</figure>

About three-quarters of total Canadian exports ($751 billion) went to the US ($569 billion), dwarfing Western Europe's $70 billion. The next largest single-country export partners are China and UK, receiving a little less than $30 billion of Canadian exports in each country.

<figure>
    <figcaption align="center" style="font-size:16">
        <b>Canada's Top Export Partners (2024)</b>
    </figcaption>
        <img src='https://github.com/JackQCXie/CAtrade/blob/master/figures/03-export_partners.png?raw=true' alt=''/>
    <figcaption align="left">Data source: ISED Canada | Figure by author.</figcaption>
</figure>

Looking back over the past 25 years, there is a trend towards diversifying trade away from the US for imports. [EXPAND]

<figure>
    <figcaption align="center" style="font-size:16">
        <b>Shares of Imports to Canadian from Trade Partners</b>
    </figcaption>
        <img src='https://github.com/JackQCXie/CAtrade/blob/master/figures/03-importshare.png?raw=true' alt=''/>
    <figcaption align="left">Data source: ISED Canada | Figure by author.</figcaption>
</figure>

There is also a trend of diversifying from US, but much less pronouced compared to imports. Shares of exports to the US [EXPAND]

<figure>
    <figcaption align="center" style="font-size:16">
        <b>Shares of Exports from Canada to Trade Partners</b>
    </figcaption>
        <img src='https://github.com/JackQCXie/CAtrade/blob/master/figures/03-exportshare.png?raw=true' alt=''/>
    <figcaption align="left">Data source: ISED Canada | Figure by author.</figcaption>
</figure>

It's quite clear that Canada's trade activities are heavily reliant on the US, especially in exports. A lot of Canadian producers will be hit hard by the tariffs, since such policies will limit their access to not only their neighbour but probably the largest single-country consumer market in the world. Not going to lie, the prognostication looks quite grim. But how bad will it be? Well let's see which sectors will be most affected by trade shocks and what the tariffs are.

## Trade Sectors and Tariffs


<!-- 
<style>
figure{text-align: center; max-width: 45%; float:left; margin:0;padding: 1px;}
figure img{width: 100%;}
</style>

<div>
<figure>
    <figcaption align="center"><b>Canada's top 10 import partners (2024)</b></figcaption>
    <img src='https://github.com/JackQCXie/CAtrade/blob/master/figures/03-import_partners.png?raw=true' alt=''/>
</figure>
<figure>
    <figcaption align="center"><b>Canada's top 10 export partners (2024)</b></figcaption>
    <img src='https://github.com/JackQCXie/CAtrade/blob/master/figures/03-export_partners.png?raw=true' alt=''/>
</figure>
</div> -->

<!--
TODO:
* Descriptive figures of balance of payments by industry for Canada and main trade partners
* General equilibrium (SOE) model with tariffs
* DSGE (NOEM) model
-->