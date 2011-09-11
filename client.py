#!/usr/bin/python
#-*- coding:utf-8 -*-#
import sys
from optparse import OptionParser
from currencyconverter import CurrencyConverter

parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog 0.1")

parser.disable_interspersed_args()
parser.add_option('--from', '-f', dest='cfrom', type="string", help="Select the original currency")
parser.add_option('--to', '-t', dest='cto', type="string", help="Select the currency to be converted")
parser.add_option('--amount', '-a', dest='amount', type="float", help="The amount to be converted")
parser.add_option('-l', dest='list', action='store_true', help="List currency list")
(opts, remainder) = parser.parse_args()

if opts.list:
  print 'Supported currency conversions:'  
  result = CurrencyConverter()
  result.print_currency_list()
  sys.exit(-1)

if opts.cfrom is None:
  print 'Missing argument'
  sys.exit(-1)

if opts.cto is None:
  print 'Missing argument'
  sys.exit(-1)

if opts.amount is None:
  print 'Missing argument'
  sys.exit(-1)
  

result = CurrencyConverter()
result.setFromCurrency(opts.cfrom)
result.setToCurrency(opts.cto)

print str(opts.amount) + ' ' + result.getFromCurrency() + ' = '  + str(result.convert(opts.amount)) + ' '  + result.getToCurrency()
