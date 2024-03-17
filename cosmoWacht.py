########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
import datetime

from checks import PostgreSQL, MeiliSearch, Homer, Zitadel, Ertie

########################################################################################################################
# DEFINITIONS ##########################################################################################################
########################################################################################################################
servicesToCheck = [Ertie, Homer, Zitadel, PostgreSQL, MeiliSearch]
title = 'CosmoWacht'
header = 'Global Status'


########################################################################################################################
# METHODS ##############################################################################################################
########################################################################################################################
def main() -> int:
    try:
        # check services
        checks = [x.isHealthy() for x in servicesToCheck]
        nUnhealthyServices = len([x for x in checks if x.get('isHealthy') is False])
    except Exception as e:
        print(f'Unable to get global health status! Error Message: {e}')
        exit(1)

    for check in checks:
        print(check)

    with open("index.html", "w", encoding='utf-8') as html:
        # HTML definitions
        html.write('<!DOCTYPE html><html lang="en">')
        html.write('\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, '
                   'initial-scale=1, shrink-to-fit=no">')
        html.write(f'\n\t<title>{title}</title>')

        # CSS
        html.write('\n\t<style>')
        html.write('\n\t\tbody {font-family: Segoe UI, Roboto, Helvetica, Cantarell, sans-serif; '
                   'background-color: #3B4252; color: #D8DEE9}')
        html.write('\n\t\th1 { margin-top: 30px; }')
        html.write('\n\t\tul { padding: 0px; }')
        html.write('\n\t\tli { list-style: none; margin-bottom: 2px; padding: 5px; border-bottom: 1px solid #D8DEE9; }')
        html.write('\n\t\t\t.container { max-width: 600px; width: 100%; margin: 15px auto; }')
        html.write('\n\t\t\t.panel { text-align: center; padding: 10px; border: 0px; border-radius: 5px; }')
        html.write('\n\t\t\t.failed-bg  { color: #ECEFF4; background-color: #BF616A; }')
        html.write('\n\t\t\t.success-bg { color: #ECEFF4; background-color: #A3BE8C; }')
        html.write('\n\t\t\t.failed  { color: #BF616A; }')
        html.write('\n\t\t\t.success { color: #A3BE8C; }')
        html.write('\n\t\t\t.small { font-size: 80%; }')
        html.write('\n\t\t\t.status { float: right; }')
        html.write('\n\t</style>\n</head>')
        html.write('\n<body>')
        html.write("\n\t<div class='container'>")

        # global status
        html.write(f'\n\t\t<h1>{header}</h1>')
        if nUnhealthyServices == 0:
            html.write(f"\n\t\t<ul><li class='panel success-bg'>All Systems Operational</li></ul>")
        else:
            html.write(f"\n\t\t<ul><li class='panel failed-bg'>Outages: {nUnhealthyServices}</li></ul>")

        # services
        html.write(f'\n\t\t<h1>Services</h1>')
        html.write('\n\t\t<ul>')
        for check in checks:
            if check.get('isHealthy') is True:
                # success
                html.write(f"\n\t\t\t<li>{check.get('serviceName')}"
                           f"<span class='status success'>Operational</span></li>")
            else:
                html.write(f"\n\t\t\t<li>{check.get('serviceName')} "
                           f"<span class='small failed'>{check.get('message')}</span>"
                           f"<span class='status failed'>Disrupted</span></li>")
        html.write(f'\n\t\t<ul>')

        # last check
        html.write(f'\n\t\t<p class=small>Last Check: {datetime.datetime.now().replace(microsecond=0)}</p>')

        # incidents

        # close html tags
        html.write(f'\n\t</div>\n</body>\n</html>')

    return 0


if __name__ == '__main__':
    exit(main())
