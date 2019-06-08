
import logging
from steamctl.argparser import register_command

_LOG = logging.getLogger(__name__)

def cmd_steamid(args):
    from steam.steamid import SteamID

    if args.s_input.startswith('http'):
        _LOG.debug("Input is URL. Making online request to resolve SteamID")
        s = SteamID.from_url(args.s_input) or SteamID()
    else:
        s = SteamID(args.s_input)

    lines = [
    "SteamID: {s.as_64}",
    "Account ID: {s.as_32}",
    "Type: {s.type} ({stype})",
    "Universe: {s.universe} ({suniverse})",
    "Instance: {s.instance}",
    "Steam2: {s.as_steam2}",
    "Steam2Legacy: {s.as_steam2_zero}",
    "Steam3: {s.as_steam3}",
    ]

    if s.community_url:
        lines += ["Community URL: {s.community_url}"]

    lines += ["Valid: {is_valid}"]

    print("\n".join(lines).format(s=s,
                                  stype=str(s.type),
                                  suniverse=str(s.universe),
                                  is_valid=str(s.is_valid()),
                                  ))

# ARG PARSER

epilog = """\
Example usage:
    {prog} steamid 4

"""


@register_command('steamid', help='Parse SteamID representations', epilog=epilog)
def cmd_parser(cp):
    cp.add_argument('s_input', metavar='<accountid|steamid64|steam2|steam3|url>')
    cp.set_defaults(_cmd_func=cmd_steamid)
