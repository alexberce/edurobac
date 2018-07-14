# -*- coding: utf-8 -*-
import scrapy


class BacalaureatEduScapper(scrapy.Spider):
    name = 'eduscrapper'
    start_urls = ['http://bacalaureat.edu.ro/Pages/TaraRezultAlfa.aspx']

    def parse(self, response):
        for nume in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(2)'):
            yield {'Nume': nume.css('::text').extract_first()}

        for pozitieJudet in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(3)'):
            yield {'pozitieJudet': pozitieJudet.css('::text').extract_first()}

        for pozitieTara in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(4)'):
            yield {'pozitieTara': pozitieTara.css('::text').extract_first()}

        for unitateInvatamant in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(5)'):
            yield {'unitateInvatamant': unitateInvatamant.css('::text').extract_first()}

        for judet in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(6)'):
            yield {'judet': judet.css('::text').extract_first()}

        for promotieAnterioara in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(7)'):
            yield {'promotieAnterioara': promotieAnterioara.css('::text').extract_first()}

        for formaInvatamant in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(8)'):
            yield {'formaInvatamant': formaInvatamant.css('::text').extract_first()}

        for specializare in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(9)'):
            yield {'specializare': specializare.css('::text').extract_first()}

        for limbaRomanaCompetente in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(10)'):
            yield {'limbaRomanaCompetente': limbaRomanaCompetente.css('::text').extract_first()}

        for limbaRomanaScris in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(11)'):
            yield {'limbaRomanaScris': limbaRomanaScris.css('::text').extract_first()}

        for limbaRomanaContestatie in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(12)'):
            yield {'limbaRomanaContestatie': xlimbaRomanaContestatie.css('::text').extract_first()}

        for limbaRomanaNotaFinala in response.css('#ContentPlaceHolderBody_FinalDiv .mainTable tbody tr:nth-child(2n+1) .tdBac:nth-child(13)'):
            yield {'limbaRomanaNotaFinala': limbaRomanaNotaFinala.css('::text').extract_first()}

        for next_page in response.css('#ContentPlaceHolderBody_ImageButtonDR1'):
            yield response.follow(next_page, self.parse)
