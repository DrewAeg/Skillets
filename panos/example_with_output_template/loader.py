#!/usr/bin/env python3

from skilletlib import SkilletLoader

sl = SkilletLoader('.')

skillet = sl.get_skillet_with_name('panos_cli_example')

context = dict()
context['cli_command'] = 'show system info'
context['username'] = 'admin'
context['password'] = 'NOPE'
context['ip_address'] = 'NOPE'

output = skillet.execute(context)

print(output.get('output_template', 'n/a'))

