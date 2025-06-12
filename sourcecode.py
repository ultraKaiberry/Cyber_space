
import sys

...

def update_trace(amount=10):
    global trace_level
    trace_level += amount
    if trace_level >= 100:
        log.append("[red]>>> TRACE COMPLETE. CONNECTION TERMINATED.[/red]")
        console.print(display_log())
        sleep(2)
        sys.exit()
from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from random import choice, randint
from time import sleep

console = Console()
fig = Figlet(font='slant')
colors = ['bright_magenta', 'cyan', 'bright_green', 'bright_yellow']
log = []
trace_level = 0  
def glitch_text(text):
    t = Text()
    for c in text:
        t.append(c, style=choice(colors))
    return t

def draw_banner(word="cyber space"):
    console.print(glitch_text(fig.renderText(word)))

def display_log():
    text = Text()
    for line in log[-10:]: 
        text.append(line + '\n', style=choice(colors))
    return Panel(text, border_style=choice(colors), title="[cyan]SYS-LOG")

def typewriter(text, delay=0.01):
    result = Text()
    for char in text:
        result.append(char, style=choice(colors))
        console.print(result, end='\r')
        sleep(delay)
        result = Text()
    console.print(glitch_text(text))

def update_trace(amount=10):
    global trace_level
    trace_level += amount
    if trace_level >= 100:
        log.append("[red]>>> TRACE COMPLETE. CONNECTION TERMINATED.[/red]")
        console.print(display_log())
        sleep(2)
        exit()
    else:
        bar = "▓" * (trace_level // 10) + "░" * (10 - trace_level // 10)
        log.append(f"[yellow]SECURITY TRACE:[/] {bar} {trace_level}%")

def handle_command(cmd):
    cmd = cmd.lower()

    if "connect" in cmd:
        log.append(">> LINK ESTABLISHED : DRONE NODE 11")
        update_trace(5)
    elif "override" in cmd:
        log.append(">> BYPASSING BIOMETRIC LOCK... SUCCESS")
        update_trace(15)
    elif "inject" in cmd:
        log.append(">> PAYLOAD TRANSFERRED - SIGNAL LOST")
        update_trace(20)
    elif "help" in cmd:
        help_text = Text.from_markup(
            "[cyan bold]>> CYBER SPACE OPERATIONS MANUAL <<[/cyan bold]\n\n"
            "[bright_green]connect[/bright_green]   → Establish link to drone or terminal node\n"
            "[bright_green]override[/bright_green]  → Bypass biometric or firewall security locks\n"
            "[bright_green]inject[/bright_green]    → Send malicious payload (use with caution)\n"
            "[bright_green]scan[/bright_green]      → Analyze enemy chip data and implant details\n"
            "[bright_green]exit / quit[/bright_green] → Disconnect from Neon Terminal\n"
            "\n[yellow]Trace Level rises with every unauthorized action.[/yellow]\n"
            "[red]When trace hits 100%, connection is forcefully severed.[/red]\n"
            "\n[bright_magenta]Tip:[/bright_magenta] Upgrade your stealth modules and scan for weak points.\n"
        )
        log.append(help_text.plain)
    elif "scan" in cmd:
        names = ["XEN-42", "MIRA-99", "GHOST-EYE"]
        roles = ["CyberOps", "Sniper Unit", "Drone Swarm Controller"]
        implants = ["Neural Fork", "Thermal Lens", "Cortex Sync"]
        firewall = f"Level {randint(1, 5)}"

        profile = Text.from_markup(
            f"[bright_cyan]BIO CHIP ID:[/]  {choice(names)}\n"
            f"[bright_green]ROLE:[/] {choice(roles)}\n"
            f"[bright_yellow]IMPLANTS:[/] {choice(implants)}\n"
            f"[red]FIREWALL:[/] Active - {firewall}"
        )
        log.append(profile.plain)
        update_trace(10)
    else:
        log.append(">> UNKNOWN COMMAND")
        update_trace(5)

def shell():
    draw_banner()
    while True:
        console.print(display_log())
        console.print("[bold cyan]λ[/bold cyan] ", end="")
        cmd = input()
        if cmd.strip().lower() in ["exit", "quit"]:
            break
        log.append(f"λ {cmd}")
        handle_command(cmd)

if __name__ == "__main__":
    shell()
    
    
