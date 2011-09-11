#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re
 
class CurrencyConverter:
    
    def setFromCurrency(self, currency):
        self.fcurrency = currency

    def setToCurrency(self, currency):
        self.tcurrency = currency

    def getFromCurrency(self):
        return self.fcurrency

    def getToCurrency(self):
        return self.tcurrency

    def convert(self, amount):
        currencyline = urllib2.urlopen('http://www.google.com/ig/calculator?hl=en&q=' + self.fcurrency + '%3D%3F' + self.tcurrency).read()
        #print currencyline
        result = re.search(".*rhs: \"(\d\.\d*)", currencyline)
        #result1 = re.search(".*rhs: \"(\d\.\d*)", currencyline)
        #print result1                   
                           
        if result:
            return float(result.group(1))*amount
  
    def print_currency_list(self):
        clist = []
        clist.append("United Arab Emirates Dirham (AED)")
        clist.append("Netherlands Antillean Guilder (ANG)")
        clist.append("Argentine Peso (ARS)")
        clist.append("Australian Dollar (AUD)")
        clist.append("Bangladeshi Taka (BDT)")
        clist.append("Bulgarian Lev (BGN)")
        clist.append("Bahraini Dinar (BHD)")
        clist.append("Brunei Dollar (BND)")
        clist.append("Bolivian Boliviano (BOB)")
        clist.append("Brazilian Real (BRL)")
        clist.append("Botswanan Pula (BWP)")
        clist.append("Canadian Dollar (CAD)")
        clist.append("Swiss Franc (CHF)")
        clist.append("Chilean Peso (CLP)")
        clist.append("Chinese Yuan (CNY)")
        clist.append("Colombian Peso (COP)")
        clist.append("Costa Rican Col√≥n (CRC)")
        clist.append("Czech Republic Koruna (CZK)")
        clist.append("Danish Krone (DKK)")
        clist.append("Dominican Peso (DOP)")
        clist.append("Algerian Dinar (DZD)")
        clist.append("Estonian Kroon (EEK)")
        clist.append("Egyptian Pound (EGP)")
        clist.append("Euro (EUR)")
        clist.append("Fijian Dollar (FJD)")
        clist.append("British Pound Sterling (GBP)")
        clist.append("Hong Kong Dollar (HKD)")
        clist.append("Honduran Lempira (HNL)")
        clist.append("Croatian Kuna (HRK)")
        clist.append("Hungarian Forint (HUF)")
        clist.append("Indonesian Rupiah (IDR)")
        clist.append("Israeli New Sheqel (ILS)")
        clist.append("Indian Rupee (INR)")
        clist.append("Jamaican Dollar (JMD)")
        clist.append("Jordanian Dinar (JOD)")
        clist.append("Japanese Yen (JPY)")
        clist.append("Kenyan Shilling (KES)")
        clist.append("South Korean Won (KRW)")
        clist.append("Kuwaiti Dinar (KWD)")
        clist.append("Cayman Islands Dollar (KYD)")
        clist.append("Kazakhstani Tenge (KZT)")
        clist.append("Lebanese Pound (LBP)")
        clist.append("Sri Lankan Rupee (LKR)")
        clist.append("Lithuanian Litas (LTL)")
        clist.append("Latvian Lats (LVL)")
        clist.append("Moroccan Dirham (MAD)")
        clist.append("Moldovan Leu (MDL)")
        clist.append("Macedonian Denar (MKD)")
        clist.append("Mauritian Rupee (MUR)")
        clist.append("Maldivian Rufiyaa (MVR)")
        clist.append("Mexican Peso (MXN)")
        clist.append("Malaysian Ringgit (MYR)")
        clist.append("Namibian Dollar (NAD)")
        clist.append("Nigerian Naira (NGN)")
        clist.append("Nicaraguan C√≥rdoba (NIO)")
        clist.append("Norwegian Krone (NOK)")
        clist.append("Nepalese Rupee (NPR)")
        clist.append("New Zealand Dollar (NZD)")
        clist.append("Omani Rial (OMR)")
        clist.append("Peruvian Nuevo Sol (PEN)")
        clist.append("Papua New Guinean Kina (PGK)")
        clist.append("Philippine Peso (PHP)")
        clist.append("Pakistani Rupee (PKR)")
        clist.append("Polish Zloty (PLN)")
        clist.append("Paraguayan Guarani (PYG)")
        clist.append("Qatari Rial (QAR)")
        clist.append("Romanian Leu (RON)")
        clist.append("Serbian Dinar (RSD)")
        clist.append("Russian Ruble (RUB)")
        clist.append("Saudi Riyal (SAR)")
        clist.append("Seychellois Rupee (SCR)")
        clist.append("Swedish Krona (SEK)")
        clist.append("Singapore Dollar (SGD)")
        clist.append("Slovak Koruna (SKK)")
        clist.append("Sierra Leonean Leone (SLL)")
        clist.append("Salvadoran Col√≥n (SVC)")
        clist.append("Thai Baht (THB)")
        clist.append("Tunisian Dinar (TND)")
        clist.append("Turkish Lira (TRY)")
        clist.append("Trinidad and Tobago Dollar (TTD)")
        clist.append("New Taiwan Dollar (TWD)")
        clist.append("Tanzanian Shilling (TZS)")
        clist.append("Ukrainian Hryvnia (UAH)")
        clist.append("Ugandan Shilling (UGX)")
        clist.append("US Dollar (USD)")
        clist.append("Uruguayan Peso (UYU)")
        clist.append("Uzbekistan Som (UZS)")
        clist.append("Venezuelan Bol√≠var (VEF)")
        clist.append("Vietnamese Dong (VND)")
        clist.append("CFA Franc(XOF)")
        clist.append("Yemeni Rial (YER)")
        clist.append("South African Rand (ZAR)")
        clist.append("Zambian Kwacha (ZMK)")

        for currency in clist:
          print currency

        return clist #if do you want to use externally
