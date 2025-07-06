# Curl V2

*Converted from PDF on 2025-07-06 10:42:33*


## Page 1

cURL Command Learning Game – Design and
### Implementation
### Overview
We propose an interactive cURL learning game with a rich GUI that allows users to practice real cURL
commands in a fun, competitive environment. The game is structured as a series of “missions” or
scenarios where the user must figure out and run the appropriate cURL command to solve each
challenge. It integrates a set of built-in cURL command scenarios (provided via JSON) and allows users
to modify commands or even add new ones for practice. The interface provides immediate feedback by
actually executing cURL commands on the system, so users can learn from real outputs and errors,
improving their understanding of cURL usage and troubleshooting. Key Features:
- Rich GUI: A high-quality graphical interface (not using Tkinter) with a cyber-themed design,
custom fonts, colors, and an engaging UX/UI. The interface includes text areas for scenario
descriptions, command output console, and interactive input, all styled for a “hacker” feel (dark background, colored text, etc.).
- Real cURL Execution: The game runs actual cURL commands on the user's system (via the
system curl binary) so that the outputs and errors are authentic. This teaches users how each
command behaves in reality and how to interpret and fix errors.
- Scenario-Based Learning: Each level presents a scenario/problem (e.g. bypassing a firewall,
exploiting a vulnerability, performing a specific file transfer) that can be solved with a particular
cURL command. The user can experiment with commands, see outputs, and iteratively arrive at a solution.
- Guidance and Hints: For each scenario, the game can provide hints or the full solution
command if the user gets stuck. After revealing the solution, a detailed explanation of the
command is shown (from the JSON data) to breakdown how it works and what each part does.
- Progress & Scoring: The game tracks which missions were solved (and whether hints were used)
and awards points accordingly. This adds a competitive element – users are encouraged to solve
missions without hints to maximize score. At the end, a summary score is displayed (e.g. X out of Y missions solved without help).
- Extensibility: The set of missions is loaded from an external JSON file (provided). This JSON
contains the command data, descriptions, explanations, etc. Developers or users can easily add
or modify missions by editing this file, without changing code. The game reads the JSON at
startup to populate the missions. (It’s also possible to extend the game with additional files or categories as needed.)
- Cross-Platform & Apple M1 Support: The project is implemented in Python using PySide6 (Qt
for Python) for the GUI. PySide6/Qt6 supports Apple Silicon (M1) natively, ensuring the game
runs smoothly on an M1 Mac. (No Tkinter is used, as requested.) The only requirements are
Python 3 and the PySide6 library, plus curl installed (macOS has curl pre-installed).
- Modern Tech Stack: Using Qt for the GUI provides a polished look-and-feel and the ability to
style the application extensively with style sheets, custom fonts, and images. The interface is
responsive and can be resized. We leverage Qt’s QProcess to run cURL asynchronously, 1

## Page 2

preventing UI freezes and allowing real-time output capture (so the user can see the command output as it arrives). Game Flow and Mechanics
- When the game starts, the user is presented with the first mission scenario. This includes a
short narrative or problem description (for example, “During a penetration test, you encounter a
target behind Cloudflare WAF. Find a way to access the target’s admin panel by bypassing
Cloudflare.”). The category of the task (e.g. Security, DevOps, Networking) may also be shown for context.
- The user has an input field where they can type a cURL command they think will solve the
mission. They must include the curl command and any options/parameters. (The interface will
remind the user to begin with "curl".) They can run the command by clicking the “Run” button (or pressing Enter).
- Real Output: When the user runs a command, the game executes it using the system’s cURL.
The output (STDOUT and STDERR) is captured and shown in a console area in the GUI. This area
is styled like a terminal: dark background, monospaced font. Normal output text appears in one
color (e.g. green), and error messages in another (e.g. red), so the user can easily distinguish
them. If the command returns HTTP headers or data, they will see it; if it produces an error (e.g.
certificate error, connection timeout, 404 response, etc.), they will see the actual cURL error
message. This immediate feedback helps them learn to interpret and debug cURL
responses. For example, a missing -k on a self-signed certificate site will result in a TLS error –
the user can spot this and realize they need the -k option.
- Iteration: The user can adjust their command and run again as many times as needed. The
output console clears for each new run to avoid confusion, but the user’s last command remains
in the input field for editing. This encourages trial-and-error learning: if their first attempt fails or
returns unexpected output, they can tweak the options.
- Hint/Solution: If the user is stuck, they can click “Hint” to get a clue. The hint is typically a subtle
nudge extracted from the mission’s description (for instance, it might say “Try bypassing DNS –
perhaps by resolving the domain to an IP manually.”). The hint text comes from the JSON
“description” field (which summarises the technique in Hebrew, in our provided data). It’s
displayed either in the scenario panel or as a popup, in a distinct style (e.g. italicized or different
color) to denote a hint. Using a hint might reduce the points for that mission.
- If the user still cannot find the solution, they can click “Show Solution”. This will reveal the
recommended cURL command (the exact command from the JSON data) to solve the scenario.
The solution can be displayed in the input field (so they can run it immediately) and also shown
as text for copying. When the solution is revealed, the explanation for that command (from the
JSON “explanation” field) is also displayed in detail – this explains each option and part of the
command so the user can learn how it works. For example, it will clarify why --resolve was
used, or what -H "User-Agent: ..." does, etc. The explanation text is shown in a dedicated
panel below the scenario description, with clear formatting (perhaps with bullet points or new
lines for different parts, as provided in the data).
- After viewing the solution and explanation, the user can click “Next” to move to the next
mission. If the user actually solved the mission without revealing the full solution, the game can
automatically mark it as solved and enable the Next button as well. (In that case, the explanation
is still available via a “Explain” button or automatically shown, so they can confirm their solution and learn any nuances.)
- Scoring: The game maintains a score or performance metric. For instance, each mission solved
without using the “Show Solution” yields 1 point. Using a hint might still allow a point, but using
the full solution yields 0 points for that mission. At the end of all missions, the game shows the 2

## Page 3

total score (e.g. “You solved 20/25 missions without full help”). This adds a competitive/replay
element – users can try again to solve more missions without hints to improve their score.
- Free Play: In addition to guided missions, the interface effectively functions as a cURL
playground. The user can type any cURL command into the input and run it, even if it’s not
specifically part of the current mission. This is useful if they want to experiment beyond the
scenarios (e.g. test a random API or URL). The output console will show the result. This free-form
usage is always available, though the game will still be focused on the current mission. (If the
user does something unrelated, it won’t count towards mission progress, but it’s allowed.)
- Safety & Actual Execution: Since real curl commands are executed, the game should caution
users not to misuse it (e.g. not to attack unauthorized targets). The provided scenarios largely
use either safe example domains or demonstrate concepts. We ensure the commands target
either public test services (like httpbin.org , badssl.com , etc.) or non-routable example
addresses, to avoid any harmful effects. For example:
- We use self-signed.badssl.com for testing a self-signed certificate scenario (this is a safe site provided by BadSSL).
- We might use httpbin.org for testing HTTP Basic or Digest auth endpoints, so that the user can actually see a success response.
- For scenarios that involve potentially malicious actions (like exploiting Shellshock or uploading a
web shell), we simulate or explain rather than actually attack a live target. (The game might not
actually execute the dangerous exploit against any real server, but the command can be shown
and explained. If the user tries to run it, it will likely fail harmlessly or time out, which is fine as a learning point.)
- Some placeholder values (like <target.com> or <origin_ip> ) are used in the JSON. The
game’s scenario descriptions will clarify these (e.g. “target.com” is a hypothetical victim domain).
If possible, we substitute them with safe example values (like example.com or a reserved IP
like 203.0.113.10 ) so that if the user runs the command, it won’t accidentally hit a real server
or will just time out. This way, the user can still see how cURL behaves (e.g. it might show a DNS resolution or connection attempt).
- Feedback and Errors: Part of learning is seeing error messages. Our game preserves all cURL
feedback. For instance, if a user forgets to include -L on a URL that redirects, they’ll see a “301
Moved Permanently” response with no final content. The game’s scenario can hint them to try -
L , or they might deduce it themselves. Another example: not using -k with an insecure site
will show an SSL error from cURL. Users will learn to recognize these and fix their commands. We
ensure the console shows these errors in a readable way (colored differently, and we do not suppress them).
- Cancel/Timeout: If a command is taking too long (e.g. waiting on a response that isn't coming),
the user can cancel it. The UI might repurpose the Run button as “Stop” while running, or
provide a separate “Cancel” button, which will terminate the cURL process. We also set
reasonable timeouts in certain scenarios (some commands in our missions explicitly use
--max-time or --connect-timeout to demonstrate those flags). For general use, the user
can always stop a hung request instead of freezing the game. The game itself remains
responsive due to asynchronous process execution.
### User Interface Design
Overall Look: The GUI has a dark, cyber-security themed design. The background is black or deep
gray. Text is displayed in bright, contrasting colors (greens, whites, oranges) reminiscent of terminal and
hacker aesthetics. We use a monospaced font for console output (and possibly for input) to resemble a
terminal. Other text (scenario descriptions, explanations) can use a clean sans-serif font or also
monospaced for consistency. Key is that everything is easily readable and the layout is clear. 3

## Page 4

```
Layout:
```
- The window is divided into sections for Scenario Description, Console Output, User Input, and
control Buttons. - Scenario Description Panel: At the top, we display the current mission’s description.
This includes the scenario narrative (and possibly the mission title/category). This text can be in Hebrew
```
(as provided) and possibly some English technical terms. We ensure Hebrew text is properly supported
```
```
(right-to-left alignment for that panel if needed). The text is likely multi-line. This panel might also later
```
show the hint and the explanation text. We can either use separate text areas or dynamically update the
```
content: - Initially, it shows the Scenario narrative (e.g. “תא ףוקעל חילצמ קדוב ,תורידח תקידבב
```
Cloudflare...”). This sets the stage for what needs to be done, without immediately giving away the exact
command. - If the user requests a hint, we can append or show the Hint text (a shorter description of the
approach). This is taken from the “description” field of JSON, which in our data is also in Hebrew and gives a
one-liner about what the command does. We might display this in italic or another color to differentiate it as a
hint. - After solving (or if the user clicks “Show Solution”), we display the Explanation text in this area (or in a
toggled sub-panel). The explanation from JSON can be several sentences, often including technical detail and
examples. We format it neatly (line breaks, maybe bullet points if needed as in the original text). This thorough
explanation appears once the user has seen the solution, ensuring they learn from it. - Console Output Panel:
In the middle, a large scrollable text area shows the output from cURL. It is initialized empty for each mission
run. This area has black background and uses a neon-green text (for standard output) on black to simulate a
terminal. Error messages (from cURL’s stderr) are captured and shown in e.g. red text. We might prefix error
lines with something like “Error:” or an icon, or simply color them. This differentiation helps users notice
issues. The output panel is read-only. - Input Field: At the bottom (above the control buttons), there is a text
input field where the user types their cURL command. This could be a single-line input (QLineEdit) so that
pressing Enter triggers the run. The input field might be pre-populated with the word curl (since every
command starts with it) to remind users, or at least have a placeholder text “Enter cURL command...”. We
allow the input to be fairly long (some commands are long), and it will scroll horizontally if needed. The font
can be monospaced here as well and maybe colored differently (e.g. light green text on black background
inside the input field for consistency). We ensure that this field accepts text in English and symbols easily (for
flags, URLs, etc.). (For convenience, we could also allow pasting a command.) - Buttons: Below the input (or
next to it) we have control buttons: - Run: Executes the command typed in the input. If a command is currently
running, this button might turn into “Stop” to allow cancellation. We give it a distinct color (maybe bright
green) to indicate action. - Hint: Provides a hint for the current mission. Possibly this button becomes disabled
or changes to “Hint used” after clicking. The hint will then display in the scenario panel. - Show Solution:
Reveals the correct command and explanation. Using this forfeits the point for this mission (we can warn “Are
you sure?”). Once clicked, the solution command is shown (for example, automatically inserted into the input
field or displayed above output) and the detailed explanation text is shown. This also effectively marks the
mission as completed (with help). - Next →: Moves to the next mission. This is enabled only after the current
mission is completed (either solved or solution revealed). If the user solved it without revealing solution, the
game can auto-enable Next and perhaps highlight “Success!” somewhere. If they haven’t solved it yet, Next
may remain disabled to encourage them to try or use the solution. (We might also have a ← Prev button to go
back to earlier missions for review; this could always be enabled for already unlocked missions.) - Score
```
Display: We can have a small area or status bar that shows the current progress, e.g. “Mission 3 of 30 – Score:
```
2” indicating they solved 2 without help so far. This updates as they progress. At game end, we might show a
dialog with the final score or simply include it in the UI. - Styling/Graphics: We use Qt Style Sheets to customize
the look: - Set the main window background to a dark color. - Use a custom font for a “cyber” look. For
example, a monospaced font like Consolas, Courier, or Monaco for the console and input. For headings or
scenario text, maybe use a bold variant or a sci-fi style font if available (ensuring Hebrew characters are still
supported – likely stick to a standard font that supports Hebrew). - Color scheme: bright green (#00FF00) for
normal output text, bright red (#FF5555) for errors, cyan or orange for scenario descriptions or hints, white
for explanation text, etc. We will ensure contrast for readability. - Button styling: perhaps use neon-glow
effects on hover, etc., to fit the theme. Qt allows styling buttons with CSS (e.g. green text, black background,
bright border). - Possibly include a faint background image or watermark (like a circuit board or binary code 4

## Page 5

motif) with low opacity, to enhance the cyber feel without distracting from text. (This is optional; we can
achieve a lot with just colors and fonts.) - Sound/animation (optional): We could play a subtle “console beep”
sound on errors or a “success” sound when a mission is solved, for feedback. Also, transitions like fading in the
explanation text or blinking cursor in the console can add to the effect. Qt can handle these with animations,
but given scope we focus on static UI with perhaps a typewriter-like text reveal for output (not too slow
though). In the current implementation, we primarily ensure everything is snappy and visually appealing,
leaving heavy animations as future enhancements. - Responsiveness: The window can be resized. The text
areas will expand accordingly (we use layout managers). This ensures if a command output is very long or
user wants a bigger console view, they can enlarge the window. Scroll bars on the console appear if needed
when output is long. (For example, verbose output with -v might produce many lines – the user can scroll
back to review them.) - Localization:* Our mission content is in Hebrew (with technical terms in English).
The UI labels (buttons, score text) we can provide in English or Hebrew as needed. Since the user
provided Hebrew content, likely the interface should support it. We will align Hebrew text to the right in
the scenario panel for natural reading. (The rest of the UI like "Run", "Hint" can be in English or could be
translated to Hebrew if desired for consistency. In this implementation, we'll use English UI labels for simplicity, but this can be adapted.)
### Implementation Details
Technology Choice: We use Python 3 with PySide6 (Qt6) for the GUI and overall logic. This choice
meets the requirements: - It avoids Tkinter (which was explicitly disallowed) and provides a modern GUI
framework that can achieve the desired high-end look and feel. - PySide6 (Qt 6) has support for Apple
M1 Macs (Qt6 is natively compatible with Apple Silicon【7†】), and is cross-platform (works on
Windows/Linux as well). The user on an M1 should be able to install PySide6 via pip without issue. - Qt's
signal-slot and QProcess framework allow us to run external processes (like curl ) asynchronously
and capture their output easily, which is perfect for this use case. - The rich widgets of Qt (QTextEdit,
QLineEdit, QLabel, QPushButton, etc.) and style sheets let us craft the custom UI appearance.
Running cURL Commands: - We rely on the system’s curl program to execute commands. The code
uses Qt’s QProcess to spawn a curl process with the arguments the user provided. We split the
input by spaces respecting quotes (to handle multi-word arguments properly). Alternatively, we may
pass the whole string to a shell, but it's safer to parse arguments or use QProcess argument list to
avoid shell injection issues. - QProcess is started with curl as the program and the list of
arguments (excluding the leading "curl" if the user typed it, because we can launch the program
directly). - We connect signals: - readyReadStandardOutput and readyReadStandardError to
capture output continuously. We append the output to the console text widget as it comes in, applying
coloring for stdout vs stderr. - finished signal to know when the command completes (to re-enable
the Run button or update mission status). - We also handle process termination on user cancel: calling
process.kill() if the user clicks Stop. - To ensure no blocking, the UI thread never waits for the
process; all updates happen via the signals mentioned. - Note: We ensure the curl output is
displayed raw. We do not post-process it except for coloring. This means if a user runs a command that
outputs binary or a lot of data, it might not be pretty (e.g., downloading a binary file will produce
gibberish in console). However, our mission scenarios avoid such cases (or use -I or similar to not
dump binary). For general use, the user can see headers or partial content as needed. We might
intercept and truncate very large outputs for performance, but typically cURL won’t output huge data
unless intentionally downloading a big file. Also, cURL’s progress meter is disabled in some cases: we
will likely invoke curl with the -s (silent) flag automatically unless verbose mode is requested, to
avoid the interactive progress bar messing up the console output. (When the user uses -v , we don’t
force silent, so they see the verbose output. For other commands, we add --no-progress-meter to
avoid the bouncing progress bar output. This detail will be handled in the code for cleanliness of 5

## Page 6

output.) - We have to parse the user’s input command string. We support the user including the curl
at start or not. For instance, if they type curl -I https://example.com , our code can detect the
first token “curl” is the program and skip it (since we launch our own process). If they omit it (just -I
```
https://... ), we can still run curl with those arguments. We will handle both cases so the user
```
isn’t confused by needing to type "curl" twice (once as concept and once because the game expects it).
In the UI, though, we’ll encourage including it for clarity, but it’s optional in implementation. - Security:
The game will execute whatever command is given in the input. While this gives users freedom, it also
means a user could potentially use the game to run arbitrary curl commands (including ones that might
be harmful or target any site). We assume the user will use this responsibly (and it’s similar to just
opening a terminal and running curl themselves). Our game doesn’t elevate any privileges or hide
what’s happening – it’s simply a guided wrapper around curl. In the README we will caution users
accordingly. Additionally, since this is a local educational tool, it’s not exposed to remote input.
JSON Data Integration: - The provided JSON (see scenario_data.json below) contains an array of
scenario objects, each with fields: command , description , explanation , category ,
scenario . We include this file with the project. - On launch, the game reads scenario_data.json
```
(using Python’s json module) to load all missions. This makes it easy to maintain or expand missions.
```
The game then populates an internal list of missions (each could be a dictionary or a small custom class
for convenience). - We use the data as follows: - scenario field: used as the main scenario narrative
shown initially (Hebrew text describing a real-world situation). - description field: used as the hint
```
(one-liner of what the command does, essentially giving away the approach if the user chooses to see
```
it). - command field: the actual solution command string. This is revealed when needed and used for
verification. - explanation field: shown after solution to teach the details. - category field: We can
display this as a label (e.g. "Category: Security") to let the user know the topic area of the mission. It
might also influence text color or icon (maybe a tiny icon for security vs devops, etc., if we wanted to
distinguish). - The game does not automatically run all these commands on load or anything; it only
runs what the user inputs. So having potentially dangerous commands in the JSON is not an issue as
long as the user doesn’t execute them against a real target. They serve as reference/solution. - The JSON
being external means users can add their own scenarios. For example, to add a new challenge, they can
append an object in scenario_data.json with their custom command , description , etc. The
game will load it next time and include it in the missions list. This fulfills the requirement of user-
extendable commands. - We ensure to document in the README how to add missions via the JSON file.
File Structure: - main.py – Main execution script. This contains the GUI setup code, event handlers,
and game logic (loading JSON, managing scenarios, running processes). You run this file to start the
game. - scenario_data.json – Scenario data file. Contains the array of missions (the provided
JSON content, including all required commands and their info). This is loaded by main.py . We keep it
separate for easy editing. - README.md – Instructions on how to install and run the game, and how to
adapt it (e.g. installing PySide6 on M1, ensuring curl is available, how to add scenarios, etc.). - (No
additional files are strictly required beyond these three, to stay within the 3-4 file limit. If needed, we
might include an icon or a CSS file, but we can also embed styling in the code. For now, we keep it minimal.)
Now, let's present the code for the main components and the JSON data as they would be implemented: 6

## Page 7

```
File: scenario_data.json
```
First, the JSON data file including all the provided commands and details (plus any minor adjustments
for proper JSON format). This includes the scenarios given in the prompt and can be extended as
needed. We preserve the content and structure, so the game can parse and display everything correctly: [ {
```
"command":"curl -k --resolve <target.com>:443:<origin_ip> https:// <target.com>/path",
```
```
"description":"תא ףקוע Cloudflare הדוקפה .הנגהה ירוחאמ רוקמה תרשל הרישי השיג ידי-לע
```
ה תבותכל תורישי תרבחתמ-IP ה תפיקע ךות ,רוקמה תרש לש-DNS לש Cloudflare תרתוכה תגצהו Host
ןוניסש ילב ,ןגומה תרשהמ תורישי הבוגת לבקל ןתינ ךכ .ירוקמה רתאה לש Cloudflare ונתוא םוסחי.", "explanation":
```
"-k רושיא תואיגשמ םלעתמ SSL (ה רושיא יכ שרדנ-SSL ןיימודל םאות וניא ירוקמה תרשה לש); --
```
resolve ל הרומ-curl ל ןיימודה םש תא רותפל-IP םוקמב ןותנה DNS; <target.com>:
443:<origin_ip> – לש טמרופ --resolve: ל טרופהו ןיימודה תא דימצמ-IP יוצרה; URL ה-https
ירוקמה ןיימודה םשב שמתשמ (תרתוכ תחילש רשפאמ Host המיאתמ).", "category":"עדימ תחטבא",
```
"scenario":"תא ףוקעל חילצמ קדוב ,תורידח תקידבב Cloudflare לש ירוקמה תרשל תורישי תונפלו
```
target.com השלוח לצנל ידכ (ל תשגל לשמל-/admin ירוקמה תרשב ףושחש). םיצור רשאכ ישומיש הז
תנגה קודבל WAF ל הרישי הינפה – ןנעב-IP ןגמה אלל עיגפ ימינפה תרשה םא תפשוח." }, {
```
"command":"curl -H \"User-Agent: () { :; }; echo; /usr/bin/id\" http:/// cgi-bin/status",
```
```
"description":"תצרפ תא לצנמ Shellshock תרתוכ ךרד שאבב User-Agent הדוקפה .תינודז
```
תרשל תחלוש HTTP תרתוכ User-Agent הדוקפ עצבמש ןעטמ הליכמה (id) תקדוב ךכבו ,עיגפה תרשה לע תצרפל שיגר תרשה םא Shellshock.",
```
"explanation":"-H \"User-Agent: …\" תרתוכ רידגמ HTTP תרדגומ תרתוכה ןאכ .תמאתומ
```
טמרופה תא לצנמש דחוימ ךרעל Shellshock (היצקנופ Bash תרתוכ ףוגב); אוה … ;{ ;: } () טמרופה
ה-signature לש Shellshock ל הדוקפ הסינכמה-execution; /usr/bin/id עצובתש הדוקפה איה
```
(ךילהתה תצרה רזוי תוהז תגצה) עיגפ אוה םא תרשה לע.", "category":"עדימ תחטבא",
```
```
"scenario":"ב ושמתשה תורידח יקדוב ,2014 רבמבונב-curl תורתוכ םע Shellshock קודבל ידכ
```
םיתרש CGI טפירקסל וז תרתוכ תחילש ,לשמל .םיעיגפ CGI ומכ /cgi-bin/status – ריזחמ תרשה םא
הדוקפה לש טלפ id, ל ףושח אוהש ןמיס-Shellshock השלוחה תא לצנל ךישמהל ןתינו." }, {
```
"command":"curl -H \"X-Forwarded-For: 127.0.0.1\" -H \"Host:
```
```
<internal.site>\" http://<backend_ip>/secure",
```
```
"description":"תרתוכ ףויז X-Forwarded-For תבותכ יפל ןוניס ינונגנמ ףוקעל ידכ IP. הדוקפה
```
ל תורישי השקב תחלוש-IP תרתוכ םע ימינפ תרש לש Host תגצה ךות ,רתאה לש X-Forwarded-For =
127.0.0.1. התוא םוסחל אלו הנמיהמ תימוקמ תבותכמ העיגמ השקבהש בושחל יושע תרשה ךכ .",
```
"explanation":"-H \"X-Forwarded-For: 127.0.0.1\" ה תבותכש תרשל ןייצמ-IP תירוקמה
```
איה חוקלה לש localhost (וז תרתוכ לע ךמוס תרשהש הרקמב) ; -H \"Host: <internal.site>\"
שקובמה ןיימודה תא רידגמ (ל תורישי תכלוה השקבה יכ ץוחנ-IP); URL םע <backend_ip> תורישי הנופ ףקועה דעיה תרשל DNS/proxy.", "category":"עדימ תחטבא", 7

## Page 8

```
"scenario":"בש ףשח החטבא רקחמ-Yelp תחילש י"\ע םיימינפ םיפדל תשגל היה ןתינ X-
```
Forwarded-For: 127.0.0.1, ושמתשה םיפקות ,לעופב .השיג תמיסחל חוקלה תבותכ לע ךמס םושייה יכ
ב-curl ה תא רובעל ידכ וז הרוצב-WAF תנגה וא IP לולסמל תשגלו /secure תימוקמ השיגל קר דעוימש ." }, {
```
"command":"curl -v -X PUT -d '<?php system($_GET[\"cmd\"]); ?>' http:/// shell.php", "description":
```
```
"ץבוק הלעמ Web Shell תשקב תועצמאב תרשל PUT. תשקב תחלוש הדוקפה HTTP PUT ליכמה ףוג םע
```
דוק PHP ינודז (Web shell), ץבוק רוציל הנווכב shell.php רשפאמ תרשה םא .דעיה תרשב PUT
```
(ב לשמל-WebDAV היוגש הרוצת וא), תרשה לע הצרה ץבוק רוצית הדוקפה.",
```
```
"explanation":"-X PUT ל השקבה תטיש תא רידגמ-HTTP PUT (באשמ תאלעה); -d '<?php
```
… ?>' דוק רבעומ ןאכ .רצווייש ץבוקה ןכות תא ריבעמ PHP תכרעמ תודוקפ ץירמש רצק (system) רטמרפמ
cmd; -v טרופמ טלפ גיצמ (headers, תרש תבוגת) המסחנ וא החילצה האלעהה םא אדוול ידכ.", "category":"עדימ תחטבא",
```
"scenario":"תרש םא ,הרידח תוקידבב web תטיש רשפאמ PUT (וא תואלעה תייקית לשמל WebDAV
```
ב םישמתשמ םירדוח ,(ןגומ אל-curl תריציל Shell: ץבוק םילעמ PHP םע backdoor. לע ,המגודל
תרצוי הדוקפה ,העיגפ היצקילפא shell.php, ןפדפדה ךרד תודוקפ עצבל ףקותל רשפאמש (URL ומכ shell.php?cmd=whoami)." }, {
```
"command":"curl -X POST -F 'file=@/path/to/file.zip' -F 'user=admin' https:///upload",
```
```
"description":"ספוטב ץבוק תאלעה עצבמ HTTP (multipart/form-data). תחלוש הדוקפה
```
תשקב POST ףוריצל ץבוק :ספוט תודש םע (file=@…) ילאוטסקט הדשו (user=admin). Curl לפטמ
ספוטש ומכ ץבוקה תא רגשמו טרפיטלומ טמרופב הזיראב HTML השוע היה.",
```
"explanation":"-F 'file=@/path/to/file.zip' םשב ץבוק ףרצמ file.zip ספוט הדשב
```
ארקנה \"file\" (Curl תשקבב ותוא ףרצמו ץבוקה ןכות תא ארוק multipart); -F 'user=admin'
םשב ליגר טסקט הדש ףיסומ user ךרעה םע \"admin\"; -X POST תשקב ןייצמ POST (לש הרקמב -F, Curl ב שמתשי אליממ-POST multipart).", "category":"חותיפ",
```
"scenario":"חתפמ DevOps קשממ תועצמאב תרשל היצרוגיפנוק ןויכרא הלעמ HTTP. קשממ םוקמב
```
GUI, תדוקפ ץירמ אוה curl ךרד יוביג יצבוק לבקל היונבה לוהינ תכרעמב ,המגודל .ץבוקה תא חולשל ידכ
תא הלעמ הדוקפה ,ספוט file.zip ךילהת לש היצמוטוא רשפאמו ןמז ךסוח הז .ןפדפד ילב םיאתמה הדשב האלעה." }, {
```
"command":"curl -T backup.sql ftp://ftp.example.com/backups/ -u user:pass",
```
```
"description":"תרשל ץבוק הלעמ FTP. ץבוקה תא הריבעמ הדוקפה backup.sql היירפסל /
```
backups/ תרשב FTP תדוקפ תועצמאב PUT תינבומ. Curl ל רבחתי-ftp.example.com םירושיאה םע
ל יטמוטוא םיצבק רוגיש רשפאמ רבדה .דעיל ץבוקה ןכות תא ריבעיו-FTP יוביג יכילהתמ קלחכ.",
```
"explanation":"-T backup.sql ל ןייצמ-curl תולעהל (\"transfer/upload\") ץבוקה תא
```
ימוקמה backup.sql ה ;תרשה לא-URL ftp://…/backups/ םייתסמ אוהש ללגבו ,היקית ליבש ללוכ
תרשב ץבוקה םשכ םג שמשי ימוקמה ץבוקה םש ,שאלסב; -u user:pass רוביחל המסיסו שמתשמ םש קפסמ ה-FTP (ל יסיסב תומיא-FTP).", "category":"DevOps",
```
"scenario":"יוביג תרשל םינותנ ידסמ הלעמ הליל יוביג ךילהת FTP. ב שמתשמ טפירקס-curl ידכ
```
ל רבחתהל-ftp.example.com תא םישלו backup.sql תייקיתב backups. תורדגהב CI/CD, וז הדוקפ
חוקלב ךרוצ אלל ,קחורמ תרשל ץבוקה תא תיטמוטוא הריבעמו יוביג תריצי רחאל הצר FTP יביטקארטניא." }, 8

## Page 9

```
{
```
```
"command":"curl --socks5-hostname localhost:9050 http:// checkip.amazonaws.com",
```
```
"description":"תשר ךרד השקבה תא בתנמ Tor יסקורפב שומיש ידי-לע SOCKS5 הדוקפה .ימוקמ
```
ךרד הרובעתה תא ריבעת sock5://localhost:9050 (תאיצי Tor תלבוקמה), תאצוי השקבהש ךכ
תבותכמ IP לש תימינונא Tor . ל אתליאשה-checkip.amazonaws.com תינוציחה תבותכה תא גיצת,
תאיצי לש תבותכ תויהל הרומאש Tor שמתשמה לש אלו.",
```
"explanation":"--socks5-hostname localhost:9050 ל הרומ-curl יסקורפ ךרד רבחתהל
```
SOCKS5 9050 טרופ לע טסוה-לאקולב לעופה (Tor daemon). תורשפאה hostname ןורתפש ךכל תמרוג
ה-DNS יסקורפה דצב עצבתי (תפילד ענומ DNS); ה-URL (http://checkip.amazonaws.com) אוה
ה תבותכ תא ריזחמש תוריש-IP ךרד האיצי תקידבל שמשמ ןאכ – ךלש Tor.", "category":"עדימ תחטבא",
```
"scenario":"תדוקפ ץירמ אוה .תימינונא ולש הרובעתהש אדוול הצור תויטרפ רקוח curl ךרד Tor
```
ה תא קדובו-IP תשר לש תבותכ הארמ האצותה . ינוציחה Tor רשאמש המ ,תיתימאה ותבותכ תא אלו
ךרד האיציה – הנידמ ינגומ םירתא תקירסב םג ישומיש הז .תימינונא הבתונ ןכא השקבהש Tor השיג תרשפאמ רוקמה תרתסה ךות." }, {
```
"command":"curl -x http://proxy.corp:8080 -U user:pwd https:// www.example.com",
```
```
"description":"יסקורפ ךרד השקב חלוש HTTP ל הרומ הדוקפה .ינוגרא-curl יסקורפל רבחתהל
```
proxy.corp:8080 תשקב וכרד עצבלו GET ל-https://www.example.com. השקבה תא לבקי יסקורפה
יסקורפל יסיסב רושיא םג תללוכ הדוקפה .דעיה לא האלה התוא ריבעיו (user:pwd) שרוד יסקורפהש הרקמל היצקיטנתוא.",
```
"explanation":"-x http://proxy.corp:8080 לוקוטורפ ללוכ) יסקורפה תבותכ תא רידגמ
```
http, טרופו חראמ םש); -U user:pwd תורשפא) יסקורפה לומ תומיא רובע המסיסו שמתשמ םש קפסמ
לש תרצוקמ --proxy-user); ה דעי-URL (https) ליגרכ ןיוצמ – curl רוביח םיקי TLS יסקורפה ךרד
```
('CONNECT') ל עיגהל ידכ-www.example.com.", "category":"DevOps",
```
```
"scenario":"ךרד רובעל תבייח תינוציחה הרובעתה לכ םיבר םינוגראב Proxy. הרבחב חתפמ ,המגודל
```
ב שמתשמ-curl םע -x קודבל ידכ תורבחתה ינותנו API לא תחלשנ השקבה .ינוציח proxy.corp:8080,
ב שמתשהל ןתינ ךכ .טנרטניאל השקבה תא איצומו ותוא תמאמש-curl לבקל ילבמ תינוגרא שא תמוח ירוחאמ המיסח תאיגש." }, {
```
"command":"curl --resolve example.net:443:203.0.113.10 https://example.net/ path",
```
```
"description":"תשקב עצבמ HTTPS ל-example.net ןורתפ םע ךא DNS תידועיי תבותכל ינדי.
```
תמושר הסינכמ הדוקפה DNS תימוקמ: example.net עצבל םוקמב ,443 טרופב 203.0.113.10-ל רתפי
תתליאש DNS תונשל ילב (תוקידב תרש לשמל) יוצרה ןיימודה םש תחת םיוסמ תרשל תונפל ןתינ ךכ .הליגר DNS ילבולג.",
```
"explanation":"--resolve example.net:443:203.0.113.10 ה ךרעל ףיסומ-DNS ימינפה
```
לש curl םשה תא example.net ה םע-IP שכ .טרופהו ןותנה-curl לע גלדי אוה ,השקבה תא עצבי DNS
תחלוש ןיידע המצע השקבה .וזה תבותכב שמתשיו ינוציח Host: example.net, וליאכ גהנתי דעי תרשהש ךכ ןוכנה ןיימודה םשב וילא ונפ.", "category":"DevOps",
```
"scenario":"תסרגל תונפל הצור אוה :האלעה-םורט תוקידב רידגמ סדנהמ staging רתאה לש
```
example.net ב הצרש-IP תועצמאב .דחוימ --resolve תא הנפמ אוה curl תחת 203.0.113.10 לא
םשה example.net. תומושר תונשל ילב ,וילא בתונמ רבכ ןיימודה וליאכ שדחה תרשה תא קודבל ןתינ ךכ DNS
תקידב תעב ליעומ ילכ הז .תויתימא Load Balancer םיתרש רבעמ וא שדח." 9

## Page 10

```
}, {
```
```
"command":"curl -I https://www.example.com",
```
```
"description":"תשקב חלוש HEAD (דבלב תורתוכ תלבק) ל-HTTPS://www.example.com.
```
תורתוכה תא קר תרשהמ תשקבמ הדוקפה HTTP לע עדימ לבקל ןתינ ךכ .ףוגה ןכות אלל ,ישארה באשמה לש
תרשה (בצמ HTTP, וכו ןכות ךרוא ,ןכות גוס ,תרש גוס’) דומעה לכ תא דירוהל ילבמ ,תוריהמב.",
```
"explanation":"-I (וא --head) ל השקבה תא הנשמ-HEAD, תורתוכ קר ריזחי תרשה רמולכ HTTP
```
ןכות ףוג אלו. Curl תורתוכה תא גיצמ (HTTP/2 200 OK, Content-Type, וכו’) לע תורישי
ה-stdout. תדותמב ךרוצ ןיאש בל ומיש -X הז הרקמב תשרופמ, -I ךכל גאוד.", "category":"עדימ תחטבא",
```
"scenario":"ףושחל היושע הדוקפה ,לשמל .תורתוכב ילמינימ עדימ ףשוח תרשהש תמאמ החטבא קדוב
```
תרתוכ ‘Server: Apache/2.4.7’ וא ‘X-Powered-By: PHP/5.4’. לולעש תואסרג ההזמ עדימ הז
ב שומישה .םיפקותל עייסל-curl -I דעצכ םירתא רפסמ רובע רהמ הבושתה תורתוכ תא רוקסל רשפאמ ןוקר." }, {
```
"command":"curl -v https://api.example.com/health",
```
```
"description":"תרזעב .תואיגש יופינ יכרצל טרופמ טלפ םע השקב ץירמ -v, curl יבלש לכ תא גיצמ
```
ןורתפ :לוקוטורפהו רוביחה DNS, רוביח TCP, TLS handshake, תולבקתמש תורתוכהו תורתוכה תחילשו
ל תרבחתמ הדוקפה .הרזח-api.example.com ירוחאמ שחרתמ המ קוידב תוארל םיחתפמל תרשפאמו םיעלקה.",
```
"explanation":"-v (verbose) ל םרוג-curl תוליחתמש תורוש :ךילהתה לע טרופמ עדימ סיפדהל
```
תכרעמ יעוריא תוארמ *-ב (ומכ 'Connecting', 'TLS handshake' וכו’); תורתוכ תוגציימ > תורוש
השקבה תא תוארל ןתינ ךכ .השקבב תוחלשנש תורתוכ ןה < תורושו ,תרשהמ ולבקתהש (Host, User-
Agent תרשה תבושת תאו (’וכו (HTTP/1.1 200 OK, תורתוכ).", "category":"חותיפ",
```
"scenario":"ןמזב Debug ץירמ חתפמ ,תוריש לש curl -v אל תורישה תואירב המל ןיבהל ידכ
```
ב עקתנ אוהש הארמ טרופמה טלפה .הניקת-TLS handshake 500 ריזחמ וא ,היוגש הדועת ללגב Internal
Server Error המגודל .תרתוכב האיגש תעדוה םע, -v תאיגש ףשוח SSL ומכ) תינדי expired
certificate) תרחאש curl תיללכ האיגש תעדוהכ גיצמ היה." }, {
```
"command":"curl -D resp_headers.txt -o /dev/null http://example.com/ index.html",
```
```
"description":"תשקב עצבמ GET ץבוקל הבושתה תורתוכ תרימש ךות ,הבוגתה ףוג תא קיתשמו.
```
לשב ךא ,באשמה תא דירות הדוקפה -o /dev/null ה ןכות-HTML ה תורתוכ לכ .קרזנ-HTTP ולבקתהש
ץבוקב ורמשיי resp_headers.txt רתוי רחואמ חותינל.",
```
"explanation":"-D resp_headers.txt ל הרומ-curl ןותנה ץבוקל הבוגתה תורתוכ תא םושרל.
```
המ הרוש לכ-status line םש עיפות תורתוכה ףוס דעו; -o /dev/null חפל הבוגתה ףוג תא בותכל רמוא
```
(ותוא רומשל אל רמולכ), אלל ;תורתוכב קר דקמתמ עוציבהש ךכ -s, curl תומדקתה תא גיצי ןיידע
```
ףיסוהל ןתינ לבא ,הדרוהה -s םיצור םא האלמ הקתשהל.", "category":"הקיטילנא",
```
"scenario":"תוארל ידכ ,המגודל) תורתוכב ריזחמ תרשה המ קדוב טסילנא cookie Set-Cookie,
```
תורתוכ וא Cache-Control). ץירמ אוה curl םע -D ץבוקה תא קרוס זאו ,ץבוקב תורתוכה תא סופתל ידכ.
חלש תרשה םא קדוב ,לשמל HSTS (Strict-Transport-Security) הרסח החטבא תרתוכ שי םא וא.
ץירהל לוכי טפירקס :היצמוטואב םג ישומיש הז curl -D תורתוכב תוזורחמ שפחלו." }, {
```
"command":"curl -c session.txt -d 'username=admin&password=P@ssw0rd' https://app.example.com/login", 10
```

## Page 11

```
"description":
```
```
"תורבחתה תשקב חלוש (POST) ה תא רמושו היצקילפאל-Cookie םש הריבעמ הדוקפה .ץבוקל לבקתהש
```
ב המסיסו שמתשמ-POST, ל הרומו ,תורבחתה ספוט השועש יפכ-curl תויגועה לכ תא םושרל (Set-
Cookie) ץבוקל הבוגתב תועיגמש session.txt. תחכוהל ךשמהב וללה תויגועב שמתשהל ןתינ ךכ תורבחתה.",
```
"explanation":"-d 'username=…&password=…' דודיקב) ספוט ינותנ חלוש application/x-
```
www-form-urlencoded) תשקבב POST – תורבחתהה ירושיא ןאכ; -c session.txt (וא --cookie-
jar) הבוגתב רידגמ תרשהש תויגועה תא ףסוא (לשמל Session ID) תרשהש םעפ לכב .ץבוקל ןתוא בתוכו
חלוש Set-Cookie, curl (’וכו הגופת ךיראת ,ביתנ ,ןיימוד ,היגוע םש) ץבוקב המיאתמ הרוש םושרי.", "category":"חותיפ",
```
"scenario":"תוקידבב API, ב שמתשמ חתפמ-curl עצבל ידכ login תחילש רחאל .ןפדפד אלל
```
ריזחמ תרשה ,םיטרפה SessionID ו ,היגועב-curl וז היגועב שמתשהל ןתינ רתוי רחואמ .ץבוקב התוא רמוש
אורקל ידכ APIs ל האירק לשמל ,תורבחתה םיבייחמש-/user/profile םע session.txt. רשפאמ הז
תויגועב רזוח שומישו תחא םעפ תורבחתה לש םיטפירקס ישיחרת." }, {
```
"command":"curl -b session.txt https://app.example.com/dashboard",
```
```
"description":"תויגועה ץבוק תא תנעוט הדוקפה .תורומש תויגוע תועצמאב ןגומ באשמל שגינ
```
session.txt תשקב תעצבמו GET דרובשדה תבותכל. Curl תויטנוולרה תויגועה לכ תא תיטמוטוא חלשי
תורבחתה עציב רבכש ןפדפד המדמ ךכו ,השקבב.",
```
"explanation":"-b session.txt (וא --cookie) ץבוקה ךותמ תויגועה לכ תא ןעוט
```
session.txt ךרוצה יפל השקבב ןתוא חלושו (ה לש ביתנ/םוחתל תומאותש תויגוע-URL וללכיי). ללוכ הז
תייגוע תא לשמל session תשקב םה הדוקפה יקלח ראש .תורבחתהב הלבקתהש GET ל תיטרדנטס-URL.", "category":"חותיפ",
```
"scenario":"השע םדוק טפירקס :תורבחתה ירחא היצמוטוא טירסת login תעכ .תויגוע רמשו
```
תועצמאב curl -b ל שגינ אוה/app.example.com/dashboard, תא תויגועב האור תרשהו SessionID
בוש רבחתהל ךרוצ אלל שמתשמ לש ימינפ ףד תאירק המיגדמ וז המגוד .שקובמה ףדה תא ריזחמו ףקתה (Single Sign-On טפירקסה ךותב)." }, {
```
"command":"curl -u apiuser:secret https://api.example.com/v1/data",
```
```
"description":"תשקב עצבמ HTTP תומיא םע Basic. תאירק תחלוש הדוקפה GET ל-API איהשכ
```
תללוכ Authentication יסיסב (Basic Auth) תרתוכב Authorization. המסיס:שמתשמה גוז
יסיסב תומיא עצבל ידכ תרשל חלשנו 64סיסבב תיטמוטוא דדוקמ.", "explanation":
```
"-u apiuser:secret יסיסב תומיאב שומישל המסיסו שמתשמ םש ןייצמ (Basic) תרשה לומ. Curl
```
תרתוכל הז ךרע ךופהי Authorization: Basic <credentials> יטמוטוא ןפואב (apiuser:secret
-> YXBpdXNlcjpzZWNyZXQ= ה ,ךכל רבעמ .(64סיסבב-URL תבותכ אוה API אלל ;הליגר -X, היהת וז תאירק GET.", "category":"חותיפ",
```
"scenario":"תומיא שרוד ימינפ תוריש HTTP Basic. לשמל, API ארוק חתפמ .המסיסב ןגומה ןשי
```
תועצמאב םינותנל curl םע -u. 200 ריזחמ תרשה OK ה םא קר-Credentials הז הרקמב .םינוכנ,
```
apiuser:secret ל השיג רשפאמ-https://api.example.com/v1/data ינוגרא עדימ לשמל ריזחמש.
```
ל םירשקתמש םיטפירקסב ישומיש-API אלל אמסיסב ןגומ OAuth." }, {
```
"command":"curl -H 'Authorization: Bearer $TOKEN' -H 'Content-Type:
```
application/json' -d '{\"action\":\"restart\"}' -X POST https:// api.example.com/servers/123",
```
"description":"תאירק חלוש API ןקוט םע תחטבואמ OAuth (Bearer). תעצבמ הדוקפה POST 11
```

## Page 12

לוהינ ביתנל (/servers/123) ינותנ הריבעמו JSON, תרתוכ ללוכ Authorization ןומיסא םע Bearer
המסיס/שמתשמ םשב ךרוצ אלל ןקוטה יפל היצקילפא/שמתשמה תא תרשה ההזמ ךכ .האשרה קפסמה.",
```
"explanation":"-H 'Authorization: Bearer $TOKEN' תרתוכ ףיסומ Authorization םע
```
ןקוט Bearer קפוסש (הנתשמה $TOKEN תזורחמ ליכמ JWT המוד וא); -H 'Content-Type:
application/json' טמרופב אוה חלשנה ףוגהש רידגמ JSON; -d '{\"action\":\"restart\"}'
םינותנ ףוג קפסמ JSON (םע טקייבוא ןאכ action:\"restart\"); -X POST תטיש תא רידגמ HTTP ל-POST תורישל הדוקפה תחילשל.", "category":"חותיפ",
```
"scenario":"תקפסמה ןנעב תכרעמ API (םיתרש תלעפה ,המגודל) תשרוד OAuth Bearer
```
token. טפירקס DevOps ליעפמ curl שארמ לביקש ןקוטה םע (מ ילוא-idP). תחילש ,לשמל POST ל-/
servers/123 םע Authorization: Bearer abc123… תא קודבי תרשה .123 רפסמ תרש לחתאת
תומיאתמה תואשרהה לעב ןקוטה םא (שדחמ הלעפה) הלועפה תא עצביו ןקוטה תופקת." }, {
```
"command":"curl --ntlm -u 'DOMAIN\\User:Passw0rd' http:// internal.win.local/data",
```
```
"description":"תומיא םע השקב עצבמ NTLM (Windows Integrated Authentication).
```
לוקוטורפ תא הסנת הדוקפה NTLM, תוביבסב ץופנה Windows, שמתשמה תא תמאל ידכ DOMAIN\\User
ה תרש לומ-IIS ימינפה internal.win.local. Curl תרשה לומ ןתמו אשמ עצבי (Challenge/
Response) לוקוטורפה תרגסמב יטמוטוא ןפואב.",
```
"explanation":"--ntlm תומיאה ןונגנמ תא ליעפמ NTLM השקבב; -u 'DOMAIN\
```
\User:Passw0rd' שמתשמ םש קפסמ (םע domain) ה רובע המסיסו-NTLM. ןייצמ \\\\ ריבחת
תשר םוחת/ןיימוד Windows. Curl תבוגת רוציל םהב שמתשי NTLM המיאתמ (Type1/Type3
messages) ה ךלהמב-HandShake. ה-URL תבותכ אוה HTTP ימינפ תוריש לש הליגר.", "category":"חותיפ", "scenario":
```
"יתרש ,תינוגרא תשר ךותב IIS וא SMB ב םינגומ-NTLM/Integrated Auth. ףולשל ךירצ חתפמ ,המגודל
```
מ עדימ-SharePoint ב שמתשמ אוה .ימינפ-curl םע --ntlm ו-Credentials לש Windows, ךכבו
ףדה תא לבקלו תמאל חילצמ http://internal.win.local/data תורבחתה בייחמש Windows. הז
תיטמוטוא המישמ רובע תודבכ תוירפס וא ןפדפדב שומיש ךסוח." }, {
```
"command":"curl --digest -u admin:admin http://camera.local/protected/ config.xml",
```
```
"description":"תומיא םע השקב חלוש Digest (HTTP Digest Authentication). הדוקפה
```
ןתמו אשמ להנמו ,(תשר תמלצמב תורדגה ץבוק חיננ) המסיסב תנגומה תבותכל הנופ Digest. חלשי תרשה
רגתא (nonce וכו’), ו-curl תבוגת בשחי MD5 םוקמב ,וקפוסש המסיס/שמתשמה םש ךותמ המיאתמ יולגב םתוא חולשל.",
```
"explanation":"--digest תומיאה ןונגנמ תא ליעפמ HTTP Digest השקבה רובע; -u
```
```
admin:admin ה יבושיחל םישורדה (המסיסו םש) שמתשמה ירושיא תא קפסמ-Digest (םיחלשנ אל םה
```
ה בושיחל םישמשמ אלא ,תורישי-hash תרשה רגתא יפל). Curl לש הבוגת/רגתאה יבלשב תיטמוטוא לפטי
Digest (ו 401 דוק-Authorization header ינש).", "category":"עדימ תחטבא",
```
"scenario":"תמלצמ IP קר העיצמ הנשי HTTP Digest Auth תשר רקוח .הלש לוהינה קשממל
```
ב שמתשמ-curl םע --digest תא ףולשל ידכ config.xml המסיס ןיזהל םוקמב .חטבואמה קשממהמ
זאו ,רגתא תלבקמ ,השקב הליחת תחלוש הדוקפה ,ןפדפדב curl תרתוכ םע בישמ Authorization
Digest םירישכממ תורדגה יוביגל םיטפירקסב םג ישומיש רבדה .החלצהב ץבוקה רזחומ ףוסבל .המיאתמ םיקחורמ." }, { 12

## Page 13

```
"command":"curl -C - -O https://releases.example.com/app.tar.gz",
```
```
"description":"תקתונמ הדרוה שדחמ (Resumable Download). ץבוק תדרוה ךישמת הדוקפה
```
app.tar.gz תימוקמ םייק רבכ ונממ קלח םא הנורחאה הריצעה תדוקנמ. -O ירוקמה ץבוקה םש תא רמוש.
curl תשקב חלשיו ודרוה רבכ םיתב המכ קודבי HTTP Range רתיה תא קר דירוהל ידכ תיטמוטוא.",
```
"explanation":"-C - (וא --continue-at -) ל רמוא-curl הנורחאה תיבהמ ךישמהל תוסנל
```
אוה ,תימוקמ םייק אל ץבוקה םא .תרשהמ רתונה ןכותה תא שקביו םייקה ץבוקה לדוג תא קודבי אוה .הדרוהש
דיימ םייתסי אוה ,דרי רבכ לכה םא ;הלחתההמ דירוי. -O (וא --remote-name) םשב הדרוהה תא רמוש ירוקמה (app.tar.gz) תרשבש יפכ.", "category":"DevOps",
```
"scenario":"ב שמתשמ תוכרעמ להנמ ,העטקנ לודג ץבוק תדרוה רשאכ-curl -C - דירוהל אל ידכ
```
1 היצקילפא לש הסרג תדרוה ,המגודל .הלחתהמGB 300 ירחא הלפנMB – תצרה curl םע בוש -C - םורגת
תשקבל HTTP םע \"Range: bytes=300000000-\" םייוביגב ןמזו ספ בחור ךסוח הז .הרתיה קר ודרוי ךכו םילודג םיצבק תוצפהו." }, {
```
"command":"curl --limit-rate 500k -o output.mp4 https://media.example.com/ file.mp4",
```
```
"description":"500 לש לבגומ בצקב ץבוק דירומKB תא תרמוש הדוקפה .היינשל output.mp4, ךא
```
מ תענומ-curl הדרוה רשפאמ הז .הרבעהה תוריהמ תלבגה ידי-לע ןימזה ספה בחור אולמ תא ךורצל
\"גניפיירקסב תישונא תוגהנתהל תוזחתהל וא תשרה לע סימעהל אל ידכ לשמל – רתוי "\הנותמ.",
```
"explanation":"--limit-rate 500k ןייצל ןתינ .היינש/טייבוליק 500-ל הדרוהה בצק תא ליבגמ
```
כ תודיחי-k, m וכו’. Curl אל תעצוממה תוריהמהש אדוול ידכ ירוזחמ ןפואב רוצעי זאו ,םינותנ טעמ ריבעי
לובגה תא רובעת. -o output.mp4 טלפל םוקמב ןותנה ץבוקה םש תחת דרונה ןכותה תא רומשל הרומ יטרדנטס.", "category":"הקירס/DevOps",
```
"scenario":"אוה .ידמ הריהמ הדרוה ידי-לע בל תמושת ךושמל הצור וניא רקוסה ,םינותנ ףוסיא טפירקסב
```
ב שמתשמ--limit-rate תלבגומ ההובג היצולוזרב ןוטרס תדרוה ,לשמל ."\יטיא"\ שלוגל תוזחתהל ידכ
500-לKB/s בצק תלבגמ ,יוביג יכילהתב ,ףסונב .תינוגראה תשרב םירחא םישמתשמ תייווחב עוגפל אל ידכ
יוביג ךילהת – םיווק תקינח תענומ nightly ספ בחור ריאשהל ידכ לבגומ בצקב ןנעב תרשהמ םיצבק דירומ תיקסעה תוליעפל." }, {
```
"command":"curl --connect-timeout 5 --max-time 10 https:// api.slowserver.com/data",
```
```
"description":"תשקב עצבמ HTTP רצונ אל םא רוביח לשכ עבקת הדוקפה .הנתמה ינמז תלבגה םע
```
עקתיי אל טירסתהש חיטבמ רבדה . תוינש 10-מ רתוי תכשמנ איה םא ןיטולחל השקבה תא שוטנתו ,תוינש 5 ךות
ידמ תיטיא הבוגת וא ןימז אל תרש לש הרקמב ןמז ךרואל.",
```
"explanation":"--connect-timeout 5 רוביחל הנתמהל (תוינשב) ילמיסקמ ןמז עבוק TCP
```
לבקתה אל תוינש 5 ךותב םא .תרשל ינושאר SYN-ACK רוביח רצונו, curl (28) האיגש ריזחיו קיספי. --
max-time 10 10 רחאל .הלבק ,החילש ,רוביח ללוכ – תוינש 10-ל השקבה לש ללוכה עוציבה ןמז תא ליבגמ
השקבה תלחתה עגרמ תוינש, curl תאיגש םע רוביחה תא רוגסי Timeout. יתלב היילת םיענומ םילגדה ינש תלבגומ.", "category":"DevOps", "scenario":
```
"ב שמתשמ רטנמ טפירקס :תוריש תואירב תקידב-curl ל-API תוריש םא ,לשמל .חצנל ןיתמהל אלש רדגומו
```
down, connect-timeout=5 רבחתמ תורישה םא םג .המלש הקד הכחת אלו רהמ לשכית הקידבהש חיטבמ
```
(עוקת) ביגמ אל ךא, max-time=10 לבקמ טפירקסה הז הרקמב .הנתמהה תא עטקי exit code 28
```
ןמזב תולקת יוהיזו רוטינל בושח הז .ןימז אל/יטיא תורישהש ןמסמו." }, { 13

## Page 14

```
"command":"curl -f -s http://web.example.com/endpoint -o result.json",
```
```
"description":"תאיגש לש הרקמב טקשב לשכנו "\טקש בצמ"\ב השקב ץירמ HTTP. הסנמ הדוקפה
```
תא דירוהל endpoint ץבוקב האצותה תא רומשלו result.json, םע ךא -f ל םורגת איה-exit code םא
האיגש סוטטס ריזחמ תרשה (4XX/5XX). -s ספדוי אל האיגש הרקמבש ךכ ,ךילהת טלפ קיתשמ HTML ףד לש חוודי האיציה דוק קר אלא האיגש.",
```
"explanation":"-f (וא --fail) ל הרומ-curl ידוקל סחייתהל אל HTTP 400 החלצהכ הלעמו.
```
האיגש דוק ריזחיו הבוגתה ףוג תא סיפדי אל אוה ,תאז םוקמב (exit status >0). םא ,רמולכ endpoint
ץבוקה ,500 וא 404 ריזחמ result.json ו רצוויי אל-curl תרתסומ האיגש תעדוה םע רוזחי. -s
```
(silent) טקשב דובעל ידכ ,האיגשה תועדוהו תומדקתהה ספ תא לרטנמ; -o ץבוקל טלפה תא רמוש, החלצה לש הרקמב (HTTP 200-399).", "category":"חותיפ",
```
```
"scenario":"טירסת CI 200-ל הפצמ תוריש-ורקימ ןיקתמש OK מ-endpoint םישמתשמ .תואירב
```
ב-curl -f לשמל .האיגש ףד וא 500 לבקתה םא תיטמוטוא לשכיי בלשהש ידכ: result.json ליכהל רומא
JSON. 503 רזח תאז םוקמב םא Service Unavailable, curl -f האיגש ריזחמ (Exit 22) ילב
טולפל HTML ץבוקה ןכות חותינ לע ףידע הז .הלשכנ הקידבהש עדוי טפירקסה ךכו ,הקוזחת ףד לש." }, {
```
"command":"curl --trace trace.log --trace-time https://example.com/api",
```
```
"description":"רוגיש עצבמ HTTP ץבוקל תרושקתה לכ לש תטרופמ הבקע םושיר ךות trace.log,
```
ב דעתת הדוקפה .ןמז תומתוח םע-log אירק טמרופב ,ףוג ינותנו תורתוכ ללוכ ,םילבקמו םיחלושש תיב לכ
```
(hex/ASCII) בלש לכב תויהשהו הרובעתה לש קימעמ חותינ רשפאמ הז .בלש לכל םינמז םע דחי.",
```
```
"explanation":"--trace trace.log בצמ ליעפמ debug ובש אלמ curl םינותנה לכ תא בתוכ
```
ה .(תכרעמ יעוריא ןכו) ץבוקל םילבקתמהו םיחלשנה-log לולכי headers, גוציי וליפאו ,העדוה ןכות
דרפנב >>ו <<כ םינמוסמ ,ןכותה לש ילמיצד-הסקה. --trace-time ידכ םושיר תרוש לכל ןמז תמתוח ףיסומ
מ הנושב .(תויהשה לש םיגאב רותיאל ליעומ) םינמז דודמל- -v, קר אלו תועדוהה יפוג םג םימשרנ ןאכ תורתוכ.", "category":"הקיטילנא",
```
"scenario":"תשקב :הנידע היעב קדוב לוקוטורפ חתפמ API ץירמ אוה .עצמאב תקרפתמש curl םע --
```
trace ץבוקב .חלשנ המו תרשה בישה תיב הזיאב קוידב תוארל ידכ trace.log חלש תרשהש אצומ אוה
header ןכותש וא יופצ אל JSON המגודל .םימיוסמ םיתב ירחא םגפנ, trace מ ימואתפ רבעמ הארה-TLS
Application Data תרזעב :םיעוציב חותינל םג שמשמ הז ילכ .הלקתה תא ריבסהש המ ,רוביח תריגסל
timestamps ךרא ןמז המכ תוארל ןתינ DNS, TLS handshake וכו’.", }, {
```
"command":"curl --http3 https://www.cloudflare.com/cdn-cgi/trace",
```
```
"description":"תשקב עצבמ HTTP/3 (יבג לע QUIC) תא החירכמ הדוקפה .ןותנ רתאל curl
```
לוקוטורפב שמתשהל HTTP/3 ב םוקמב-HTTP/2 היינפ תעצובמ ןאכ .הכימתל ףופכב ,1.1 וא
ל-cloudflare.com רובע script לש trace, תרושקתש אדוול תנמ-לע HTTP/3 תרשה םא .תלעופ
לע ץורת השקבה ,םיכמות חוקלהו UDP/QUIC םוקמב TCP.",
```
"explanation":"--http3 ל הרומ-curl ב תורישי רבחתהל תוסנל-HTTP/3. Curl שמתשי
```
לוקוטורפב QUIC (UDP) ב ועצבתי הבוגתהו השקבה – חילצה םאו ,רוביחה תחיתפל-HTTP/3. אל תרשה םא
תושדח תואסרגב ,ךמות curl ל לופיל תוסנל יושע-HTTP/2 (ב םישמתשמ םא אלא--http3-only). ה-URL
אוה HTTPS יכ שרדנ – ליגר HTTP/3 לעמ קר םייק TLS.", "category":"חותיפ",
```
"scenario":"תרשש קדוב תשר סדנהמ Cloudflare ב ןכות שיגמ ןכא ולש-HTTP/3. תועצמאב curl
```
--http3 לש הקידבה תוריש תבותכל הנופ אוה Cloudflare (cdn-cgi/trace) ללוכ עדימ הריזחמש
תזורחמה \"http=http/3\" ןכא רוביחה רשאכ http/3. טניילקה תביבסבש תתמאמ הדוקפה (curl +
תוירפס QUIC) ל לפונ היהו הדימב .הליעפ הכימתה – תרשבו-HTTP/2, הכימתב היעב שיש עדוי היה סדנהמה ב-HTTP/3." }, 14

## Page 15

```
{
```
```
"command":"curl --tlsv1.0 -Iv https://old.example.com/",
```
```
"description":"תסרג םע רבחתהל הסנמ TLS תשקב עצבת הדוקפה .רוחאל הכימת קודבל ידכ תנשוימ
```
HEAD (-I) טרופמ טלפ םע (-v), ה תסרג תא ליבגת ךא-TLS רתוי ךמות אל תרשה םא .1.0-ל תילמיסקמה
ב-TLS1.0 (החטבא תוביסמ), ב הארנ ,רשפאמ ןכ אוה םא .לשכיי רוביחה-log רוביח TLS הסרגב חלצומ 1.0.",
```
"explanation":"--tlsv1.0 ל הרומ-curl ב רתויה לכל שמתשהל-TLS 1.0 (ל לוקש- --tls-max
```
1.0) תוסנל אלו TLS1.2/1.3. דיה תציחל תעב ,ךכמ האצותכ TLS, curl טלפב גיצי (-v) תסרג תא
קליסש שדח תרש םע .הרחבנש לוקוטורפה TLS1.0, תאיגש לבקנ SSL Handshake (failure). -I ו--
verbose תורתוכהו רוביחה ךילהת תא תוארל קר אלא ןכותה תא דירוהל אלש ידכ םילולכ.", "category":"עדימ תחטבא",
```
"scenario":"תרשש אדוומ תומיאת קדוב legacy שרוד ןיידע TLS1.0 ץירמ אוה .םינשי תוחוקל רובע
```
curl --tlsv1.0 םא ,לשמל .חילצמ רוביחה םא ןנובתמו curl אל תרשהש ןמיס הז ,רבחתהל חילצמ
תאיגש םע לשכנ רוביחה םא ,תאז תמועל .הפרות תדוקנ תילאיצנטופ - תנשוימ הנפצה תיבשה \"Protocol
version\", קר רשפאמ הארנכ תרשה TLS קודבל הריהמ הקינכט וז .תיתחטבא הניחבמ יוצר הזו ינרדומ תורדגה SSL םידבכ הקירס ילכ אלל." }, {
```
"command":"curl --ciphers 'AES128-SHA256' https://secure.example.com/",
```
```
"description":"תשקב עצבמ TLS רבחתהל הסנמ הדוקפה .םיוסמ ןפוצ טס ץוליא ךות
```
ל-secure.example.com ל םינפצה תלבגה ךות-AES128-SHA256 דבלב (ןפוצ TLS רדגומ) קודבל ידכ
שמ םא .הזה ןפוצה תא בייחמ וא ךמות תרשה םאจบั TLS תרשהש ןכתיי ,לשכנ םא ;ןימז ןפוצהש ןמיס ,חילצמ הז ןפוצ לבקמ אל.",
```
"explanation":"--ciphers 'AES128-SHA256' רוביחל תרתומה םינפצה תמישר תא ןייצמ TLS.
```
יפיצפס ןפוצ רחבנ ןאכ (ךותמ המגודל suite לש TLS1.2). Curl ל ריבעי-TLS handshake תמישר
ידכ םיקיספב תדרפומ המישר ןייצל ןתינ .תוחדיהל יושע רוביחה ,רחא ןפוצ בייחמ תרשה םא .תמצמוצמ םינפצ
רוביח טושפ איה הדוקפה ראש .תויורשפא רפסמ לולכל HTTPS עיפוי ,םאות אל ןפוצה םא יכ םא) ליגר error רוביחה ןמזב).", "category":"עדימ תחטבא",
```
"scenario":"אדוול הצור ןוגרא ,לשמל .םיוסמ קזח וא שלח ןפוצב ךמות תרש םאה קדוב החטבא קדוב
```
ץירמ החמומה .ןשוימ ןפוצ םירשפאמ םניא םהיתרשש curl םע --ciphers לשמל) שלח ןפוצ לש 'RC4-
MD5'): םע הקידב ,ונלש הרקמב .ןוקית בייחמה רבד – ותוא רשפאמ ןיידע תרשה ,חילצמ רוביחה םא
AES128-SHA256 ןפוצב ךמות תרשהש החיכומ AES 128bit םע SHA-256. תורדגה ןוחבל הריהמ ךרד וז תקירס ילכ ילב ןפוצ SSL םיידועיי." }, {
```
"command":"curl -w 'Connect: %{time_connect}s, TTFB: %{time_starttransfer}
```
s, Total: %{time_total}s\\n' -o /dev/null -s https://www.example.com/",
```
"description":"ןמזהו ,ןושאר תיב תלבקל ןמז ,רוביח ןמז :םיירקיע םיעוציב ינמז דדומו השקב עצבמ
```
ףד תא הדירומ המצע הדוקפה .ללוכה example.com תרוש אוה הצוחה ספדומש המ לכו ,ןכותה תא תקרוז ךא
ינותנ לבקל ןתינ ךכ .םידדמנה םינותנה םע הקיטסיטטס Latency ו-TTFB תאוושהל לשמל ,תולקב םיעוציב.",
```
"explanation":"-w '…%{time_connect}…%{time_starttransfer}…%{time_total}…'
```
ב שומיש אוה--write-out: curl תוקיטסיטטסה ךותמ םישקובמה םיכרעה תא השקבה םויסב סיפדמ
ןמזה ינתשמ תא בלשמה טסקט טלפמט רדגוה ןאכ .תורבטצמה: time_connect – בלש ףוס דע ךשמ TCP
handshake; time_starttransfer – ןכותה לש ןושארה טייבה תלבקל דע ןמז (TTFB);
time_total – הדרוהה םויס דע ללוכ ןמז. \\n הרוש רבעמ ףיסומ ףוסב. -o /dev/null תספדה ענומ
```
(הדידמל עירפי אלש ידכ) ןכותה; -s םידדמה תרוש תא קר ליכי טלפהש ידכ ,תומדקתה ספו תורתוכ קיתשמ.", "category":"הקיטילנא", "scenario": 15
```

## Page 16

```
"טפירקס בתוכ אוה ,םידבכ הדידמ ילכב שמתשהל םוקמב .םירתא ינש ןיב האוושה תוקידב ץירמ םיעוציב סדנהמ
```
תועצמאבש curl -w רובע ,לשמל .הבוגתה ינמז תא ףלוש www.example.com תויהל יושע טלפה
\"Connect: 0.032s, TTFB: 0.120s, Total: 0.350s\". םיסנכנו ןמז ךרואל םיפסאנ הלא םינותנ
תשרב תויעב וא הניעטה תוריהמב םייוניש רחא לק בקעמל םיכוז ךכ – תוחודל." }, {
```
"command":"curl -Z https://files.example.com/1.iso -o 1.iso https:// files.example.com/2.iso -o 2.iso",
```
```
"description":"ליבקמב םיבורמ םיצבק דירומ (Parallel transfers) הדוקפה .דחא רוביחב
```
לש תושקבה-יוביר תלוכי תא לצנת curl (7.66.0 הסרג זאמ) לכ .רוטב אלו תינמז-וב םיצבק ינש שקבל ידכ
ידועייה םשב רמשי ץבוק (1.iso, 2.iso) רפסמ תדרוה ץיאמ רבדה .רשפאה תדימב רוביחה ףותיש ךות
הכומנ הייהשהו הובג ספה בחור רשאכ דחוימב ,םיטקייבוא.",
```
"explanation":"-Z (וא --parallel) תיליבקמ הדרוה בצמ ליעפמ - curl תושקבה תא רגשי
```
ל-URLלכל .תחא תחא םוקמב דחי םינותנה םי URL רומש -o םיאתמ ץבוק םש (ל ךייש-URL וינפלש). Curl
ךרוצה יפל (םי)רוביח חתפי (HTTP/2 וא HTTP/3 דיחי ץורעב בוביר םירשפאמ). לדחמ תרירבכ curl ליבגי
ומייסי תורחאש ןיתמי הזל רבעמו ,ליבקמב תודרוה 50-ל (םע ןווכל ןתינ --parallel-max).", "category":"DevOps",
```
"scenario":"להנמ ,רוטב תאז תושעל םוקמב .רהמ םילודג םי’גמיא המכ דירוהל ךירצ ,הצפה שיחרתב
```
ב שמתשמ תכרעמ-curl -Z יצבק 2 דירוהל ידכ ISO םימייתסמו דחי םימדקתמ םהינשש האור אוה .ליבקמב
םיעלקה ירוחאמ .(קיפסמ ספ בחור ןתניהב) דחא-דחא רשאמ רתוי םדקומ, curl ב שמתשה ילוא-HTTP/2
multiplexing - ותוא לע תוצר תודרוהה יתש TLS connection, ךסוח םג ךכו Handshake הז .ףסונ
ןימז ספה בחור לבא ההובג היהשהה הבש הביבסב דחוימב ליעי." }, {
```
"command":"curl -z local.backup -o local.backup https://mirror.example.com/ backup.tar.gz",
```
```
"description":"תא תשקבמ הדוקפה .הנורחאה םעפה זאמ ןכדוע אוה םא קר ץבוק דירומ
```
backup.tar.gz יאנת הפיסומ ךא ,תרשהמ If-Modified-Since לש ןכדועמה ןמזה לע ססובמה יטמוטוא
ימוקמה ץבוקה ‘local.backup’. תמייק השדח הסרגש ריזחמ תרשה םא (HTTP 200), דרוי ץבוקה
הנתשה אל םא ;ןשיה תא ףילחמו (HTTP 304), curl רבד דירוי אל.",
```
"explanation":"-z local.backup (וא --time-cond) ל םרוג-curl יונישה ינמז תא קודבל
```
```
(timestamp) ימוקמה ץבוקה לש local.backup. תרתוכ תרשל חלוש אוה If-Modified-Since םע
```
304 ריזחי תרשה ,זאמ הנוש אל תרשב ץבוקה םא .ץבוקה לש ןוכדעה ךיראת Not Modified ו-curl קיספי
הליגר הדרוה עצבתת ,השדח הסרג שי םא .דירוהל ילב. -o local.backup הרימשל ץבוקה םש תא ןייצמ –
ךרוצה הרקמב קר ןשיה תא ףילחהל ידכ םש ותואב םישמתשמ ונא.", "category":"DevOps",
```
"scenario":"ה יתרשב רתוי תינכדע הסרג שי םא קר יוביג ץבוק דירומ ימוי יוביג טפירקס-Mirror.
```
הדוקפה curl -z םיוסמ םויבש חיננ .תורתוימ תודרוה עונמל ידכ ימוקמה יוביגה לש ןמזה תמתוחב תשמתשמ
הנתשה אל ץבוקה – curl 100 בוש דירוי אלו 304 לבקיGB השכ ,רחא םויב .אוושל-Mirror תא ןכדעי
backup.tar.gz, curl 200 יפל תאז ההזי OK ספ בחורו ןמז ךסוח הז .ןשיה תא ףילחמו דרוי שדחה יוביגהו יתועמשמ ןפואב." }, {
```
"command":"curl -O \"https://site.example.com/images/pic[1-5].jpg\"",
```
```
"description":"בולג תינבת תועצמאב ,בקוע ןפואב םירפסוממש םיצבק תרדס דירומ (ןויפיכ URL).
```
תושקב ףצרל םיעבורמה םיירגוסה תא תיטמוטוא םגרתת הדוקפה: pic1.jpg, pic2.jpg, … pic5.jpg,
ירוקמה םשב תחא לכ רומשתו (-O). האלול אלל םיצבק לש העודי הצובק תחא תבב דירוהל ןתינ ךכ תינוציח.",
```
"explanation":"\"pic[1-5].jpg\" ה ריבחתב-URL בולג תינבת אוהbing: curl התוא ביחרמ
```
םיירגוס םע הפיצר אל המישר ןייצל םג ןתינ .5 דע 1-מ רפסמ לכל הדרוה עצבי אוה .תודרפנ תובותכ שמחל 16

## Page 17

םילסלוסמ (לשמל {file1,file2}). -O (–remote-name) יפכ ירוקמה ומשב רמשיי ץבוק לכש חיטבמ
בש-URL (pic1.jpg וכו’). ב םישמתשמ ,יובכ גניבולג םיצור םא :הרעה -g, ןווכמ שומיש הז ןאכ לבא.", "category":"חותיפ",
```
"scenario":"ולש רתאהמ תורפסוממ תונומת דירוהל הצור םלצ (pic1.jpg דע pic5.jpg). םוקמב
```
האלול וא תודוקפ 5 ליעפהל shell, לש בולגב שמתשמ אוה curl. השימח תרציימ ליעל הדוקפה GET ףצרב
ש הלוסנוקב תוארל ןתינ .יטמוטוא-curl תדרוה :לשמל םינותנל ישומיש םג הז .דרפנב הנומת לכל השקב רצוי
ידומע report_01.csv, report_02.csv תחא תינבתב ’וכו." }, {
```
"command":"curl -I https://old.example.com --next -I https:// new.example.com",
```
```
"description":"ב תשמתשמ הדוקפה .תחא הדוקפב ףצרב תודרפנ תושקב יתש חלוש--next ידכ
```
תשקב םיעצבמ םדוק :תויורשפא לש םיטס ןיב דירפהל HEAD ל-old.example.com, תשקב םיעצבמ זאו
HEAD ל תדרפנ-new.example.com, ךרוצה יפל דרפנ וא דחא רוביחב ןהיתש. Curl תא הארי --next
תורדגה לחתאיו (ומכ -I) היינשה השקבה ינפל.",
```
"explanation":"--next תדוקפב דחוימ דירפמ אוה curl השדח השקב"\ ליחתהל רשפאמה\"
```
ה ינפל .הדוקפ תרוש התואב--next, תורשפא שי ,ןאכ -I לע הלחה old.example.com. רחאל --next,
בוש רדגומו תספאתמ תורדגהה -I, זאו URL יתש םיחלוש ונא ךכ .ינש HEAD back-to-back. Curl לוכי
לכל דרפנ רוביח חותפל (לכל URL םע host שדח רוביח חתפיי הארנכ הנוש). יפל דרפנב ספדות הבושת לכ רדס.", "category":"DevOps",
```
"scenario":"תורתוכ תוושהל ןיינועמ סדנהמ HTTP הדוקפב שמתשמ אוה .תוריהמב שדחל ןשי תרש ןיב
```
םע הדיחי --next: ה תא הליחת הגיצמ הבוגתה-Headers מ-old.example.com לש ולא תא ןכמ רחאלו
new.example.com. ה תסרג שדחה תרשבש לשמל תוארל רשפא-Server החטבא תורתוכ שיש וא הנוש
ב שומיש .תופסונ--next ל אורקל םוקמב :םיטפירקסב חונ-curl תולועפ ףצר תעצבמ תחא האירק ,םיימעפ
```
(ידי-לע תימינפ לפוטמ ךא ,רושרשל המודב curl)." }, {
```
```
"command":"curl smtp://mail.example.com --mail-from user@example.com --
```
mail-rcpt admin@corp.com -T email.txt -u \"user@example.com:Pa$$w0rd\"",
```
"description":"לוקוטורפ ךרד ל"\אוד חלוש SMTP תועצמאב curl. ב תחתפנ הדוקפה-URL
```
```
smtp:// ץבוק ךותמ העדוהה ףוג תא הלעמו ,ליימה ןעמנו חלוש הרידגמ ,ראודה תרש לש email.txt.
```
Curl לוקוטורפ תא עצבי SMTP (EHLO, AUTH, MAIL FROM, RCPT TO, DATA) םירטמרפה סיסב-לע ונקפיסש.",
```
"explanation":"smtp://mail.example.com ל הרומ-curl תרשל רבחתהל SMTP (לדחמ תרירב
```
587 וא 25 טרופ TLS םא smtp://). --mail-from user@example.com חלושה תבותכ תא רידגמ
envelope ליימה לש; --mail-rcpt admin@corp.com המכ םע םינעמנ רפסמ רשפא) ןעמנ ןייצמ --
mail-rcpt); -T email.txt תורתוכ ללוכ) ליימה תעדוה ףוגכ חולשלו ץבוקה ןכות תא תחקל רמוא MIME
ליכי ץבוקהש יאדכש); -u \"user:Pa$$w0rd\" ירושיא קפסמ SMTP (ראודה ןובשחל תורבחתה) םא
שרוד תרשה AUTH LOGIN/PLAIN. Curl עצבי AUTH החילשה רחאל .וללה המסיס/שמתשמה םש םע, 250-ב ביגי תרשה OK חילצה םא.", "category":"חותיפ",
```
"scenario":"ב שמתשהל םוקמב .בו’ג םויסב ליימב תחלשנ תיטמוטוא הארתה-sendmail, טפירקס
```
ב שמתשמ-curl תרש ךרד ליימ חולשל ידכ SMTP ץבוקה .הרבחה לש email.txt ןכותו אשונ תא ליכמ
טמרופב העדוהה RFC822. curl ל רבחתמ-mail.example.com, םע תמאמ user@example.com,
ל ליימה תא חלושו-admin@corp.com . המ ל"\אוד חולשל ןתינ ךכ-Shell חווידל ישומיש ,הדיחי הדוקפב םייטמוטוא םיכילהתמ תואצות." }, {
```
"command":"curl -X OPTIONS -i https://api.example.com/v2/", 17
```

## Page 18

```
"description":"תוטיש וליא קדוב HTTP תשקב תועצמאב םיוסמ באשמ ידי-לע תוכמתנ OPTIONS.
```
תשקב תחלוש הדוקפה OPTIONS ביתנל /v2/ ה לש-API, תשקבמו (-i) הבוגתה תורתוכ תא םג לולכל
תרתוכלו 204/200 סוטטס םע תונעל יופצ תרשה .טלפב Allow תורתומה תודותמה תא תטרפמש (GET, POST, באשמה רובע (’דכו.",
```
"explanation":"-X OPTIONS תטיש תא עבוק HTTP ל-OPTIONS, תליאשל תשמשמה
```
תרתוכב הל בישהל לוכי תרשהש תיטרדנטס השקב וז .תרשב תודותמ/תולוכי Allow: …; -i (וא --include)
ל הרומ-curl ףוג קר אלו הבוגתה תורתוכ תא םג גיצהל (OPTIONS תורתוכ קר ,ללכ ףוג ריזחי אל בורל).
לשמל גיצי טלפה ‘Allow: GET,POST,OPTIONS’ תולועפ וליא ןיבהל רשפאמש המ ,תורתוכה ןיב תוכמתנ.", "category":"עדימ תחטבא",
```
"scenario":"קדוב API ב שמתשמ-OPTIONS תויופצ אל תודותמ רשפאמ אל תרשהש אדוול ידכ.
```
תלעפה ,לשמל OPTIONS לע /v2/ ריזחהל היושע ‘Allow: GET,HEAD,OPTIONS’ םג עיפומ היה םאו
‘PUT’ וא ‘DELETE’ הרוצת תקידבב ,ןכ ומכ .תלבגומ תויהל הכירצ ילואש תורשפא לע דמלמ היה הז,
ש םיאדוומ-OPTIONS שיגר עדימ ףשוח אל. Curl המכ לע תוריהמב וז הקידב עצבל רשפאמ endpoints תקירסמ קלחכ ,ףצרב Best Practices." }, {
```
"command":"curl -k -v -X TRACE https://www.example.com/",
```
```
"description":"תטיש תא רשפאמ תרש םא קדוב HTTP TRACE (ןוכיס הווהמ םיתיעלש XST).
```
תשקב תחלוש הדוקפה TRACE (חלשש המ תא חוקלל ריזחהל הרומאש) ל-https://www.example.com,
הדועת תואיגשמ תומלעתה ךות (-k) תטרופמ הספדהו (-v). 200 ריזחמ תרשה םא OK תא ףקשמה ףוג םע
ש ןמיס ,השקבה-TRACE ומכ תורתוכ ףולדל לולעש המ ,קלוד Cookie.",
```
"explanation":"-X TRACE ל הדותמה תא הנשמ-TRACE, ףוגב הריזחמש תיטסונגאיד הדותמ איהש
```
תרשה לביקש השקבה ןכות תא. -v הבושתהו השקבה תורתוכ תא תוארל ידכ ללכנ. -k קדבנ תובורק םיתיעל יכ
ה טלפב .תימצע הדועת םע טסט תרש לע-verbose, םא TRACE וארי ,רשפואמ Response ףוג םע echo
405 לבקתי הארנכ ,לטובמ אוה םא .(ונחלשש תורתוכה ,לשמל) השקבה תורתוכ לש Method Not Allowed המוד וא.", "category":"עדימ תחטבא",
```
"scenario":"תרש םאה ןחוב טסילנא web קילדמ TRACE, תפקתמ רשפאל לולעש המ XSS ךרד
```
reflection לש cookies (Cross-Site Tracing). תועצמאב curl חלוש אוה TRACE; םא ,לשמל
תרתוכה תא הבושתב האור ‘Cookie: session=abc’ התוא ריזחה תרשהש ןמיס – חוקלה דצב חלשהש
רמולכ ,ףוגב TRACE תובכל ץילמהל ידכ דעותמ הז עדימ .ליעפ TRACE. ןפדפד ילכב שומישל טושפ ףילחת הז, םיתרש רפסמ לע תיטפירקס הקידב רשפאמו." }, {
```
"command":"curl -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\" -e
```
\"https://google.com\" https://target.com/page",
```
"description":"תרדגה ידי-לע תמא ןפדפדל תיביטקא הרוצב זחתמ User-Agent םיירלופופ ררפרו.
```
ל השקב תחלוש הדוקפה-target.com/page םע User-Agent לש Chrome לע Windows תרתוכ םעו
Referer לע העיבצמה Google. ףוקעל יושע הז :הלא םינייפאמ םע תושקבל הנוש םיסחייתמ םיבר םירתא
תא תוננסמש תויסיסב תומיסח User-Agent ‘curl’ רחא ףדמ העגה תושרוד וא.",
```
"explanation":"-A/--user-agent תזורחמ ןייצל רשפאמ User-Agent םימש ונא ןאכ .תמאתומ
```
ןפדפד לש יוהיז Chrome/Windows הליגר השילגכ תואריהל ידכ. -e/--referer תרתוכ תא עבוק
ה-Referer םא ,לשמל ךכ .לגוג לש ףדמ ונעגהש המדמה target.com ידי-לע תינפוה םא קר ןכות גיצמ
Google (הרישי השיג עונמל ידכ), ה ראש .יאנתב דומעת וז השקב-URL ליגר דעי אוה.", "category":"הקירס",
```
"scenario":"ב-web scraping, רידגמ רקוסה ,תומיסח עונמל ידכ User-Agent ץופנ ןפדפד לש,
```
םוסחל םילולע םירתא תרחא UA רתא ,לשמל .טפירקס לש target.com אל התאש ההזמ םא ןכות גיצמ אל
םע – ןפדפד -A כ-Dummy Chrome, שופיח עונממ היהת הינפההש שרוד רתאה ,ףסונב .החילצמ השקבה
םע – תימניח הייפצל -e Google, curl חלוש Referer טפירקסל רשפאמ הזה בולישה .הקידבה תא רבועש 18

## Page 19

םיטושפ הנגה ינונגנמ לומ רתוי "\ישונא"\ תואריהל." }, {
```
"command":"curl --cert client.crt --key client.key --cacert CA.pem https:// secure.api/test",
```
```
"description":"תשקב עצבמ HTTPS חוקל תומיא םע (Mutual TLS). תרשל הגיצמ הדוקפה
```
ידי-לע המותח חוקל תדועת CA.pem, ידדצ-וד חוקל יוהיז שרודש חטבואמ ביתנל השיג תרשפאמו. Curl
יטרפה חתפמב שמתשמ (client.key) הדועתו (client.crt) רוביח רוציל ידכ TLS לומ תמואמ ה-API.",
```
"explanation":"--cert client.crt טמרופ) חוקלה תדועת ץבוק תא ןייצמ PEM, םג לולכל לוכי
```
קפוסמ םא יטרפה חתפמה תא); --key client.key םא שרדנ) הדועתל םאותה יטרפה חתפמה תא קפסמ
ותוא הליכמ אל הדועתה); --cacert CA.pem תדועת רידגמ CA תדועת תומיא תעב ךומסל הילעש תירוביצ
עצובמ ךכ .(ףסונב וא ,לדחמה תרירב תונח םוקמב) תרשה TLS חוקלה תדועת תא קדוב תרשה :ידדצ-וד
```
(י"\ע האצוהש CA.pem), ותוא לומ תרשה תדועת תא קדוב חוקלהו CA.pem וא CA רחא.", "category":"עדימ תחטבא", "scenario":
```
```
"יקשממ API םישרוד םיתיעל םיימינפ Mutual TLS – תוחוקלל קר השיג תרשפאמש תיאקנב תכרעמ ,לשמל
```
ב שמתשמ היצרגטניא חתפמ .תילטיגיד הדועת םע-curl םע --cert/--key קשממל האירק קודבל ידכ test.
םג ללוכ אוה --cacert ה י"\ע םותח אוה יכ תרשה תא תמאל ידכ-CA החילצמ השקבה .ןוגראה לש (200 OK)
הדועתה םא קר client.crt אלל ןויסנ .תומיאתמ תואשרה תלעבו ,הגפ אלו הפקת --cert תאיגש בינמ היה 403, תשיג המיגדמ וז הדוקפ ןכלו mTLS." }, {
```
"command":"curl --dns-servers 8.8.8.8,8.8.4.4 https://check.example/dns- test",
```
```
"description":"יתרשב שמתשמ DNS עוציבל לדחמה תרירב םוקמב םימאתומ Resolving םש לש
```
ה תתליאש תא עצבת הדוקפה .ןיימודה-DNS רובע check.example 8.8.4.4-ו 8.8.8.8 םיתרשה ךרד
```
(Google DNS), ה םוקמב-DNS ףוקעל וא םיינוציח םירבלוזרב שרפתמ םש ךיא קודבל רשפאמ הז .ימוקמה DNS ימינפ.",
```
```
"explanation":"--dns-servers 8.8.8.8,8.8.4.4 ה יתרש תמישר תא עבוק-DNS שמתשיש
```
םהב curl שומישל קיספב תודרפומ תובותכה ינש .הלעפהה תכרעמל תונפל םוקמב ,תומש רותפל ידכ
כ-Primary ו-Secondary. תיטרדנטס איה השקבה ראש – curl יresolve תא check.example ךרד 8.8.8.8 (8.8.4.4 הסני ךירצ םאו).", "category":"הקיטילנא", "scenario":
```
"תמושרש דשוח תשר סדנהמ DNS ב שמתשמ אוה .תנכדועמ אל תינוציח-curl םע DNS תוארל ידכ לגוג לש
```
תימינפה תשרב ,לשמל .םחתמה םש םגרתמ ןאל check.example םע ךא ,תרחא תבותכל עיבצמ --dns-
servers 8.8.8.8 תקידבב ישומיש םג הז .הנשי תבותכל רתפמ ןיידע טנרטניאהש םיאור CDN: לואשל רשפא
יתרש DNS תונוש תונידמב (םא curl םש ץר) תבשומ תבותכ וזיא תוארל ידכ." }, {
```
"command":"curl --interface eth0 https://ipinfo.io/json",
```
```
"description":"יפיצפס תשר קשממ ךרד השקבה תא חלוש (eth0). יסיטרכ רפסמ שי הנוכמל םא
```
תובותכ וא תשר IP, מ אצת השקבהש אדוול רשפא-interface ב שמתשת הדוקפה .ןותנ-eth0 רוקמכ,
תורישל הנפתו ipinfo הזיאל קודבל ןתינ ךכ .תיארנה תירוביצה תבותכה המ ררבל ידכ IP רשוקמ eth0 םא לשמל ,םג שי, eth1.",
```
"explanation":"--interface eth0 לע הפוכ curl ומשש תשרה קשממב שמתשהל eth0 עוציבל
```
ה-TCP connect (ידי לע SO_BINDTODEVICE תכרעמב). תבותכ ןייצל םג ןתינ IP םא .קשממ םש םוקמב
eth0 רסח וא רדגומ אל, curl האיגש ריזחי. URL ה-https םע בולישב .קשממ ותוא ךרד רבחתי
ipinfo.io (ריזחמש JSON םע IP), תא תגציימש תירוביצה תבותכה תא תוארל רשפא eth0 (לשמל 19

## Page 20

םירוביח המכ םע תרש לש הרקמב).", "category":"תשר",
```
"scenario":"תבותכמ תואצוי םיוסמ דעיל תושקבש אדוול הצר תובותכ-הבורמ תרש םע תוכרעמ להנמ
```
ה-IP תועצמאב .הנוכנה curl --interface םע תרש ,המגודל .שרופמב רוחבל לוכי אוה eth0 ו-eth1 –
ץירמ אוה curl --interface eth1 ifconfig.co תבותכ האורו A, םע זאו eth0 תבותכ האורו B. הז
תא םיסנמ טושפ – לעופ ןכא (תירלולס תשרל חיננ) דרפנ קשממש אדוול :יוביג תקידבב םג רזוע curl וכרד הבושת םילבקמ םא םיאורו." }, {
```
"command":"curl --compressed -o page.html https://www.example.com/",
```
```
"description":"יטמוטוא ןפואב תרשהמ הסוחד הבוגת לבקל ידכ ,הסיחדב הכימת םע השקב חלוש.
```
תרתוכ הפיסומ הדוקפה Accept-Encoding המיאתמ (gzip, deflate, br). ןכות חלוש תרשה םא
סוחד, curl ףדב ןכותה תא רומשיו הסיחדה תא קרפי page.html. תא תוארל רשפאמו ספ בחור ךסוח הז תידיימ אירקה ןכותה.",
```
"explanation":"--compressed הסיחדה תכימת תא תיטמוטוא ליעפמ. curl חלשי Accept-
```
```
Encoding: deflate, gzip, br (ךמות חוקלהש היצניבמוק וא), חולשל יושע תרשהו Content-
```
```
Encoding:gzip וכו’. Curl ןכות תא ארקי gzip ל הביתכה ינפל ותוא חפניו-output. ץבוקב ךכ
```
page.html םילבקמ HTML הז לגד אלל .חנעופמ, curl חלוש היה תרשה םאו ,הסיחד שקבי אל gzip לכב
תאז – curl (אירק אל) אוהש ומכ ותוא רמוש היה.", "category":"חותיפ",
```
"scenario":"םע .דבכ רתא דומע תקדוב תחתפמ --compressed, סחוד תרשה יכ רתוי הריהמ הדרוהה
```
~70% ןכותהמ. Curl ב גיצמ-header Content-Encoding: gzip תא רמוש לבא page.html רבכ
חנעופמ (ה תא אורקלו טסקטב ץבוקה תא חותפל הלוכי איה-HTML דימ). ירקמב םג ישומיש הז API
םיריזחמש JSON תפסוה – סוחד --compressed ל תרמוא-curl חתפמהש םוקמב ,חונעפה םע דדומתהל ץירהל ךרטצי gunzip תינדי." }, {
```
"command":"curl -s https://api.example.com/data | jq '.items[] | .name'",
```
```
"description":"תא בלשמ curl דוביע ילכ םע JSON (jq) הדוקפה .תורישי טלפה תא חתנל ידכ
```
ל אתליאש הצירמ-API הבוגתה תא הריבעמו (טמרופבש JSON) ל-jq, ןאכ – םיכרע תמישר הכותמ איצומש,
ךרעמב םיטירפה לכ תומש items. םיינדי םייניב יבלש אלל םינותנ דוביע רשפאמ רוניצב שומישה.",
```
"explanation":"-s (silent) לע curl וא תומדקתה יספ אלל הבוגתה ףוג תא קר ריאשמ header
```
```
(ב םישמתשמ אל ונחנא יכ-i ןאכ), ש חיטבמש המ-jq לבקי JSON ה ;ןיקת-pipe | לש טלפה תא חלוש
```
curl ל-jq. רטליפה jq '.items[] | .name' ךרעמב טירפ לכ רובע :ושוריפ items, הדשה תא טלפ
name. לשמל ךכ JSON ומכ { items:[ {name:\"A\"}, {name:\"B\" ] } סיפדהל םורגי A זאו B תודרפנ תורושב.", "category":"הקיטילנא",
```
"scenario":"מ םירצומ תמישר ךשומ םינותנ טסילנא-API. ץירמ אוה ,חותפל זאו ץבוקל רומשל םוקמב
```
curl | jq ה ,המגודל .תחא הדוקפב-API טקייבוא ריזחמ JSON םע .לודג jq, תא קר וכותמ דדובמ אוה
ףיסוהל םג רשפא :ןמז ךסוח הז .םירצומה תומש תמישר לש יקנ טלפ לבקמ אוה .תומשה | wc -l לשמל
בוליש .םיטירפה רפסמ תא רופסל curl+jq םינותנמ קלח רבעמ רשפאמו ,םיטפירקסב המצוע-תבר תינבת אוה חותינל םייח." }, {
```
"command":"curl -X POST -H 'Content-Type: application/json' -d
```
@payload.json https://api.example.com/create",
```
"description":"תאירק חלוש POST ףוג םע JSON ץבוקה ןכות תא ןעטת הדוקפה .ץבוקמ ארקנה
```
payload.json יפוג רובע חונ הז .הדוקפה תרושב םינותנה תא ןייצל םוקמב ,השקבה ףוגכ ותוא חולשלו
טקייבוא ומכ ,םינבומ וא םילודג השקב JSON בכרומ. Content-Type כ רדגומ-application/json ידכ םאתהב שרפל עדי תרשהש.", 20

## Page 21

```
"explanation":"-d @payload.json ל רמוא-curl ץבוקה ןכות תא אורקל local םשב
```
payload.json ודילקהל ילבמ לודג טסקט לולכל רשפאמ @ ןמיסה .השקבה לש םינותנה ףוגכ ותוא םישלו
תינדי. -H 'Content-Type: application/json' טמרופב אוה חלשנה ףוגהש רידגמ JSON; -X POST
ל הטישה תא עבוק-POST (ב שומיש ,השעמל-d ל לדחמ תרירבכ איבמ רבכ-POST, תא ריהבמ שרופמ ןויצ לבא הנווכה).", "category":"חותיפ", "scenario":
```
"ב שומיש תעב-API אוה טלקה םיתיעל ,םיבאשמ תריציל JSON םינותנ אורקל ךירצ חתפמ ,המגודל .לודג
```
ב ותוא רמוש אוה .תרחא תינכותב רצונש ץבוקמ-payload.json ץירמו curl -d @payload.json.
ץבוקב בותכ אוהש יפכ קוידב ףוגה תא לבקמ תרשה (טקייבוא ,המגודל JSON םיבורמ תודש םע). ענומ הז
םיבכרומ םינותנ ינבמ תחילש לע לקמו הדוקפה תרושב טוטיצ/החירב לש תואיגש." }, {
```
"command":"curl -m 5 'http://vuln.example/search?q=1%20AND%20SLEEP(10)'",
```
```
"description":"תועיגפ קדוב SQL Injection תבכעמ התליאש תקרזה ידי-לע ןמז תססובמ רוויע.
```
רטמרפ הפיסומ הדוקפה q םע payload ל םרוגש-SLEEP(10) תמייק תועיגפה םא תרשב. –max-time 5
```
(רוציק -m) תוינש 10 בכעל הסנמ תרשה םאש ךכ ,תוינש 5-ל הנתמהה תא ליבגמ, curl הבוגתה תא עטקי
```
בוכיעל המרגו הצרוה התליאשהש קיסהל ןתינ ךכמ .התמלשה ינפל.",
```
"explanation":"-m 5 (וא --max-time 5) התליאשה .תללוכה השקבל תוינש 5 לש יברימ ןמז עבוק
```
```
'1 AND SLEEP(10)' ךרעה תא ללוכו עיגפ רתאה םא .םינותנה סיסבב תוינש 10 לש בוכיעל םורגל תדעוימ
```
ב תורישי-SQL, ךא .הנעמ ינפל תוינש 10~ בכעתי ףדה curl רוביחה תא רוגסי אוהש ךכ ,5-מ רתוי הכחי אל
```
(Timeout). םא ,ןכל curl תאיגש ריזחמ Timeout הדוקפ ץירהל הסינ תרשהש ןמיס ,תוינש 5 רחאל
```
תוינש 5-מ רתוי הכראש (רמולכ SLEEP(10) עצוב הארנכ). האצות ריזחמ וא ליגרכ רהמ בישמ תרשה םא
ה .(עיגפ אל) היהשהה העצוב אלש הארנכ ,תידיימ-URL םיחוור רובע %20 ללוכ (URL-encoded).", "category":"עדימ תחטבא",
```
"scenario":"ב שמתשמ תורידח קדוב-curl תקידב עצבל ידכ Blind SQLi: ףיסומ אוה payload
```
םע SLEEP(10) הדשל query. םע –max-time=5, ש האור אוה-curl ב תוינש 5 רחאל אצי-TIMEOUT –
תוינש 5-מ רתוי הכראש הדוקפ ץירהל הסינ תרשהש זמרמש המ (רמולכ SLEEP(10) עצוב הארנכ). וז
הדשהש הקזח היצקידניא q ל עיגפ-SQL Injection. םא ,תאז תמועל curl 5-מ תוחפ ךות הבושת ריזחה
ש דיעמ הז ,האיגש וא הבוגתה ,תוינש-SLEEP הליעי הקינכט יהוז .תקרזומ אל התליאשהש ןכתייו עצוב אל רותיאל SQLi ןמז ילדבה תרזעב." }, {
```
"command":"curl -G 'https://maps.googleapis.com/maps/api/geocode/json' --
```
data-urlencode 'address=1600 Amphitheatre Parkway, Mountain View, CA' --data- urlencode 'key=YOUR_API_KEY'",
```
"description":"תשקב חלוש GET תנפצהב חונ שומיש ךות ,םידחוימ םיוות םיללוכה םירטמרפ םע
```
URL. ל הנופ הדוקפה-Geocoding API לש Google דדוקל םוקמב .םיקיספו םיחוור תללוכש תבותכ םע
תינדי, –data-urlencode הנפצהב לפטמ. -G ל םרוג-curl ל הלאה םירטמרפה תא ףרצל-URL תתליאשכ GET.",
```
"explanation":"-G (וא --get) ל רמוא-curl תועצמאב) םיקפוסמה םינותנל סחייתהל --data-
```
urlencode וא -d) ירטמרפכ Query string, ל םתוא ףיסוהלו-URL ינש שי ןאכ .השקבה ףוגב םוקמב
םירטמרפ: address ו-key. --data-urlencode 'address=…' תיטמוטוא ןיפצמ ,תבותכה תא חקול
%2-כ םיקיספ ,%20-כ םיחוורC ל ףיסומו ,'וכו-URL כ-...?
```
address=1600%20Amphitheatre%20Parkway…; רטמרפ key=YOUR_API_KEY שיש הרקמב ןפצומ םג
```
```
(חתפמ לש הרקמב וסנכוי '=' וא '+' ילוא ,המגודל) םידחוימ םיוות. Curl הש אדווי-URL יקוח יפוסה ןפצומו.", "category":"חותיפ",
```
```
"scenario":"ביכרהל םוקמב URL ב שמתשמ חתפמ ,תינדי-curl --data-urlencode אורקל ידכ
```
API 1600' תבותכה ,לשמל .בכרומ טלק םע Amphitheatre Parkway, Mountain View, CA' 21

## Page 22

ב תורישי םישל הסנמ היה םא – םיקיספו םיחוור הליכמ-URL האיגשל םרוגש המ ,ןיפצהל חכוש היהש ןכתיי. --
data-urlencode לבקמ אוה .ורובע תאז השוע JSON המ תוטנידרואוק םע-API לש Google החלצהב,
תושקב חולשל תפדעומ ךרד יהוז .ריבחת תואיגש אלל GET רחאמ ,םידחוימ םיוות/םיחוור םיללוכ םירטמרפ םע דודיק תויועט תענומ איהו." }, {
```
"command":"curl 'ldap://ldap.example.com/ou=users,dc=example,dc=com?cn?sub?
```
```
(uid=jdoe)' -u 'cn=Manager,dc=example,dc=com:ldapPass'", "description":
```
```
"ב שופיח עצבמ-LDAP תועצמאב curl חוקלכ LDAP. תתליאש תחלוש הדוקפה LDAP Directory
```
תא תשקבמה attribute=cn (Common Name) תחת תו/הסינכ לש ou=users,dn=example,dn=com
ןוניס ךות uid=jdoe, םע scope=sub (ץע-תת). תומיאב תרבחתמ םג איה Bind להנמ שמתשמכ.
םישקובמה םיכרעה םע טלפב רזחות (האצמנ םא) האצותה.",
```
"explanation":"URL טמרופב ldap://…??? יפל רדגומ RFC. ןאכ: base DN =
```
```
ou=users,dc=example,dc=com; attrs = cn (רוזחי אלמ םש קר); scope = sub (סיסבב שפחל
```
ץעה-תת לכו); filter = (uid=jdoe) שמתשמ םש םע טקייבוא אצומ jdoe. -u
```
'cn=Manager,dc=example,dc=com:ldapPass' קפסמ DN ךרוצל שמתשמ לש Bind (טושפ תומיא)
```
+ המסיס (ldapPass). ךרע ריזחי תרשה ,המאתה שיו םיפקת לוהינה ירושיא םא CN שמתשמה לש jdoe.
המכ שי םא, curl םע המושר לכ גיצי 'DN:' לש תודגואמ תורושו attribute: value. (וז הדוקפ רשפאמ תרשהש החינמ LDAP queries).", "category":"עדימ תחטבא",
```
"scenario":"ב שמתשמ תוכרעמ להנמ-curl תרש לואשל ידכ LDAP ןיקתהל םוקמב ינוגרא
```
ldapsearch. ומכ והשמ ריזחת ליעל הדוקפה .שמתשמ לש ןובשח יטרפ קדוב אוה: 'DN:
```
uid=jdoe,ou=users,dc=example,dc=com' זאו 'cn: John Doe'. תועצמאב ךכ curl לוכי אוה
```
ה ךירדממ םינותנ איצוהל טפירקסב-LDAP (םש היה :ליימ תבותכ ףולשל לשמל attr=mail). תלוכי יהוז
לש העודי תוחפ curl ו טפירקס יכרצל הליעי ךא-DIY רוטינב LDAP." }, {
```
"command":"curl --unix-socket /var/run/docker.sock http://localhost/ containers/json",
```
```
"description":"תאירק עצבמ API לומ Docker daemon ךרד ימוקמ Unix Domain Socket
```
רוביח םוקמב TCP. ל חלשת הדוקפה-socket ץבוקה /var/run/docker.sock תשקב HTTP GET
רובע /containers/json – קשממל האירק איהש Docker REST צלListing Containers.
Docker תרושקתל ןיזאמ HTTP ה ךרד-socket, ו-curl ותועצמאב תורישי ותיא רשקתל לוכי.",
```
"explanation":"--unix-socket /var/run/docker.sock ל הרומ-curl ץבוק תא חותפל
```
ה .ליגר תשר רוביח חותפל םוקמב סקינוי טקוסה-URL ומכ הארנ ןיידע HTTP םע localhost, םש לבא
תייצולוזרב שמשמ תמאב אל חראמה DNS תרוש רובע קר אוה – רוביחב וא Host. curl טקוסה ביתנל רבחי
רבדיו HTTP. עצבי אוה ,ןאכ GET /containers/json. 'http://localhost/…' יכ עיפוהל בייח
curl טמרופ שרוד URL, לעופב ךא localhost דעיכ שמשמ טקוסה – רתפנ אל. Docker daemon לבקי
ריזחיו טקוסה ךרד השקבה תא JSON טלפב תוארל רשפא .םירנייטנוקה תמישר לש list יטקייבוא לש container (ID, image וכו’).", "category":"DevOps",
```
"scenario":"תנוכמב Linux, ליעפמ להנמ curl לומ תורישי Docker אלל עדימ לבקל ידכ docker
```
CLI. טמרופב ,םיצרש םירנייטנוקה תמישר תא ריזחת ל"\נה הדוקפה JSON. םיטפירקסב ,לשמל ,ישומיש הז
תדוקפמ תורישי םינימז אלש םיטרופמ םינותנ גישהל םיצורש docker ךרד השענ הז לכו רחאמ ,ףסונב .הליגר
ץבוקה /var/run/docker.sock, חותפל ךרוצ ןיא Docker ל-TCP – החטבא ילוקישמ. Curl םע --
unix-socket ךרד םיפושחה םירחא םיימוקמ םיתורישל השיג םג רשפאמ socket (ומכ Docker,
Kubernetes API ב-unix-socket, Caddy, וכו’)." }, { 22

## Page 23

```
"command":"curl telnet://mail.example.com:25 --max-time 5",
```
```
"description":"תרשל רוביח חתופ SMTP תועצמאב ,הכרבה רנאב תא סופתל ידכ 25 טרופב curl
```
םוקמב telnet. ל תמרוג הדוקפה-curl רוביח עצבל TCP ל-mail.example.com:25 (SMTP), ןיתמהל
ה תרש םא .תוינש 5 ירחא םייסל זאו ,םינותנל טעמ-SMTP 220"\ לשמל) רנאב תרוש חלשי אוה ,ליעפ
mail.example.com ESMTP Postfix…\") התוא גיצת הדוקפהו.",
```
"explanation":"telnet://mail.example.com:25 ל ןייצמ-curl לוקוטורפב שמתשהל
```
```
'telnet' 25 טרופב תרשל רבחתהל ידכ. Curl רבחי השעמל TCP חלשי אל לבא ,תרשהמ טלקל הכחיו
```
תרש .(החילשל םינותנ ונקפיס אל יכ) רבד םוש SMTP טסקט רנאב חלוש רוביח תעב דימ כ"\דב. Curl גיצי
לע ותוא STDOUT. --max-time 5 שרוד תרשה םא עקתיהל אל ידכ ,הרקמ לכב תוינש 5 ירחא קתננש אדוומ
ןיאש ןוויכ .םולכ חלוש אלו טלק user input (ל דוגינב-telnet יביטקארטניא), לע קר םיכמתסמ ונחנא החיתפ רנאב חולשל תרשה לש המזויה.", "category":"עדימ תחטבא",
```
"scenario":"ילכ Banner Grabbing: תרשב הצר ראוד תנכות הזיא קדוב החמומ
```
mail.example.com. תדוקפב שמתשהל םוקמב telnet, ב שמתשמ אוה-curl (לכב טעמכ ןימזש
220' ומכ רנאב חלוש תרשה .רוביח חותפל ידכ (תכרעמ mail.example.com ESMTP Postfix 2.10' –
curl אוה תרשהש האור החמומה .רגוסו הרושה תא סיפדמ Postfix v2.10. ב שומישה-curl
```
telnet:// תנקתה אלל הפולחכ רכומ telnet, םיתרש תמישר קורסל ידכ םיטפירקסב ותוא בלשל ןתינו הנכות תואסרג שפחלו." }, {
```
```
"command":"curl -H 'Accept: application/json' -H 'Accept-Language: en-US' https://site.example/data",
```
```
"description":"ןכות לבקל הרטמב ,הפשו טמרופ תופדעה תועבוקש תורתוכ םע השקב חלוש JSON
```
ןכות תרשהמ תשקבמ הדוקפה .תילגנאב JSON (םוקמב HTML) תועצמאב Accept, שמתשמהש הריהצמו
תועצמאב תילגנא ףידעמ Accept-Language. טמרופב הבוגת ריזחי אוה ,ךכל ןנכותמ תרשה םא JSON םיאתמה ימואלניב.",
```
"explanation":"-H 'Accept: application/json' תרתוכ ףיסומ HTTP תרשל העידומש
```
כ ןכותה תא לבקל ףידענש-JSON. הברה APIs וריזחי םירתא וא JSON םוקמב ,תחכונ וזה תרתוכה רשאכ
HTML. -H 'Accept-Language: en-US' םירתא לש הרקמב .(תיאקירמא) תילגנאה הפשב ןכות שקבמ
ןכות קיפהל תרשה תא תונווכמ דחי תורתוכה יתש .ןימז םא תילגנאב טסקט ריזחהל יושע תרשה ,םיינושל-בר
לשמל :םאות API טמרופו תילגנא רחבי אוה – תומגרותמ האיגש תועדוה ריזחמש JSON. ה ראש-URL אלל יוניש.", "category":"חותיפ",
```
"scenario":"חוקל חתפמ-API ריזחמ םימעפל תורישהש ןיחבמ HTML ףד לשמל) האיגש תועדוה םע
```
שקובמ אל םא (יללכ האיגש JSON תלבק חיטבהל ידכ .שרופמב JSON, תרתוכ תא ףיסומ אוה Accept
עבוק אוה ,חותינ ךרוצל תילגנאב םינותנ לבקל ידכ ,ןכ ומכ .ויתושקבב Accept-Language=en. המגודל,
ילב האירק Accept ףד לשמל הריזחמ התייה HTML, טקייבוא לביק אוה ,הנוכנה תרתוכה םע ךא JSON רדוסמ
ןכותב ךמות תוריש םא תוארל רשפא – תוקידבב םג תוישומיש ולא תורתוכ .םינותנה לש JSON, וזיאב ןכ םאו םאתהב השקבה תא תונשלו ,לדחמ תרירב הפש." }, {
```
"command":"curl -L -o final_page.html http://short.url/abc123",
```
```
"description":"תוינפה ירחא תיטמוטוא בקוע (Redirects) הדוקפה .יפוסה ןכותה תא רמושו
```
תשקבמ URL הארנכ ריזחמש Redirect (ןוגכ short.url הכורא תבותכל הינפה השועש), ל תודוהו- -L,
curl רמשנ יפוסה ןכותה .יפוסה דעיל העגהל דע האבה הינפהה תא עצבי אלא רוצעי אל
כ-final_page.html. הינפה תוארשרש ירחא בוקעל ינדי ךרוצ ילבמ האצותה תלבקתמ ךכ.",
```
"explanation":"-L (וא --location) ל רמוא-curl: 3 דוק לבקתמ םאXX תרתוכו Location,
```
עצב GET ל יטמוטוא-URL שדחה. curl םע דדומתהל ידכ ,לדחמ תרירבכ םימעפ 50 דע תינרזוח תאז השעי
תובורמ תוינפה וא תוארשרש. -o final_page.html אלל .ץבוקב ןורחאה דעיה לש ןכותה תא רמוש -L,
curl תרתוכה תא קר סיפדמ ,הינפהה רחאל רצועו בקוע אל לדחמ תרירבכ 'Location' םע .לביקש -L, 23

## Page 24

רוציק לש הרקמב המגודל URL, האלמה תבותכהמ ןכותה תא איבי אוה.", "category":"חותיפ",
```
"scenario":"קדוב QA ליעפמ אוה .ןוכנה ףדל ליבומ רצק רושיקש תמאמ curl -L רושיקה לע
```
ילב .רצוקמה -L 301' לשמל לבקמ היה Moved Permanently Location: https://
long.example.com/article', םע ךא -L, curl תיטמוטוא עצבמ GET אוה םויסב .השדחה תבותכל
המכ הנפמש תבותכמ ץבוק תדרוה – םיטפירקסב םג ליעומ הז .ותוא רמושו רמאמה לש יתימאה ןכותה תא לבקמ
םימעפ (לשמל from http ל-https) תעדוה םע עצמאב רוצעל םוקמב ,קלח עצבתת Location דבלב." }, {
```
"command":"curl -k https://self-signed.badssl.com/",
```
```
"description":"ה תומיא לע גוליד ךות ןימא אל/ימצע רושיא םע תרשל השקב עצבמ-SSL. הדוקפה
```
תמיתחב הניאש הדועת גיצמש רתאל הנופ CA רדגוהש ןוויכמו ,רכומ -k (insecure) curl קספיי אל
ןיא םהב םירקמב וא ,םותח אל רושיא םע ןחבמ תרש לע תוריש וא ןכות קודבל ןתינ ךכ .הדועת תומיא תאיגשב
```
(תוימינפ תוקידב לשמל) תרשה תוהז תא אדוול ךרוצ.", "explanation":
```
```
"-k (וא --insecure) תא החנמ curl תדועת תומיא תואיגשמ םלעתהל SSL/TLS. םא ,ללכ ךרדב
```
לומ תתמואמ תויהל הלוכי אל הדועתה CA ןימא (Self-signed ףקות גפ וא), curl עצבי אלו האיגש ריזחי
םע .השקבה תא -k, curl ןכוסמ הזש ןייצל בושח .הרהזא אלל התיא ןפצומ רוביח רוצייו הדועת לכ לבקי
ןוכיסל ףשוח הז יכ תינרצי הביבסב MitM, רתאה ,ןאכ .תוקידבב ישומיש לבא self-signed.badssl.com
ונממ ןכות איצוהל חילצת הדוקפהו ,תימצע הדועת גיצמכ עודי.", "category":"חותיפ",
```
"scenario":"תוביבס תוקידבב QA, תוריש חיננ .תויתימא תודועת םישכור דימת אל םיחתפמ API םע
```
ילב :תימצע הדועת -k, תואירק curl םע תולשכנ ויה 'SSL certificate problem'. םע -k, חתפמ
תלעפה ,המגודב .תודועתב לפטל ילב תורישה תא קודבל לוכי curl לע self-signed.badssl.com ילב -k
םע ךא ,תלשכנ התייה -k רושיאה ףד רזחות (הארמש 'self signed certificate' טלפכ). הז
תובוגת לש הריהמ הקידב רשפאמ HTTPS רדגומ אלשכ םג CA תכרעמב." }, {
```
"command":"curl -r 0-99999 -o snippet.bin https://largefile.example.com/ video.mp4",
```
```
"description":"תא קר תשקבמ הדוקפה .ולוכ תא םוקמב לודג ץבוקמ (םיתב חווט) קלח דירומ
```
100,000 לש םינושארה םיתבה video.mp4 (99999 דע 0 תיבמ) תרתוכ תועצמאב Range . םא ,תרשה
ב ךמות-Range, תבושת ריזחי Partial Content (206) חלפ ותוא םע קר. Curl הזה גלפה תא רומשי
ב-snippet.bin. ולוכ תא דירוהל ילב לודג ץבוק לש הקידב וא תיקלח הייפצל ישומיש הז.",
```
"explanation":"-r 0-99999 טייב דעו (הלחתה) 0 טייבב ליחתמ :הדרוהל םיטייב חווט רידגמ
```
99,999 100 רמולכ .ללוכKB םינושאר. Curl תרתוכ חלשי \"Range: bytes=0-99999\" השקבב.
ריזחי אוה ,רשפאמ תרשה םא Content-Range: bytes 0-99999/total שקובמה ךרואב ףוגו. -o
snippet.bin ןייצל םג ןתינ .הז םשב ץבוקל עטקמה תא בותכי -r 100000- דע 100000 תיבמ לחה ץוליחל
ץבוקה לכ תא חלשיו םלעתי אוה ,םיחווטב ךמות אל תרשה םא .םירחא םיחווט וא ,ףוס (Curl םלעתי זא
100 רחאל ראשהמKB) ןיקת אל חווטה םא 416 ריזחי וא.", "category":"הקיטילנא",
```
"scenario":"ץבוק לש תרתוכה טמרופ תא קודבל הצור ואדיו סדנהמ MP4 דירומ אוה .ולוכ תא דירוהל ילב
```
100 תא קרKB םע םינושארה curl -r. ץבוק snippet.bin תא ליכמ header + ואדיווה תליחת,
הדרוה תויקלח אדוול םיצור םימעפל ,תרש תוקידבב ,המודב .תוניקת םיקדובש םילכ ץירהל ידכ םיקיפסמש –
תועצמאב -r תיקלח הדרוה תומדל רשפא (קודבל ידכ לשמל resume ןכות רציימה תוריש וא streaming).
ךרוצל םוצע םינותנ רוקממ עטק ךושמל ידכ הזב שמתשהל יושע חתפמ ,ןכ ומכ preview ריהמ." } ] 24

## Page 25

```
(The JSON above is included as-is in the project. Note that <target.com> or <origin_ip> are
```
placeholders; the game will explain them, and the user is not expected to literally run those exact strings
unless they replace them with real values. Also, special characters and quotes are properly escaped in the JSON so it can be parsed.) File: main.py
Now, the main Python script for the game. This script will create the GUI, handle user interactions, and
coordinate the game logic described. It uses PySide6 for the UI components and QProcess for running
cURL. Comments are included to explain key parts of the implementation: importsys,json
fromPySide6.QtWidgetsimportQApplication,QWidget,QVBoxLayout,QHBoxLayout, QLabel,QTextEdit,QLineEdit,QPushButton
fromPySide6.QtGuiimportQFont,QTextCursor,QColor fromPySide6.QtCoreimportQt,QProcess # Load scenarios from JSON file try:
withopen("scenario_data.json","r",encoding="utf-8")asf: scenarios=json.load(f) exceptExceptionase:
print("Error loading scenario_data.json:",e) sys.exit(1) # Prepare an application instance app=QApplication(sys.argv)
# Set application font or style (global font for all widgets for consistency if desired)
app.setApplicationName("cURL Learning Game")
# Optionally, set a custom font globally
# e.g., app.setFont(QFont("Consolas", 10)) # Main window setup window=QWidget()
window.setWindowTitle("cURL Command Learning Game")
window.resize(900,600) # decent default size main_layout=QVBoxLayout(window) main_layout.setSpacing(8)
main_layout.setContentsMargins(10,10,10,10) window.setLayout(main_layout)
# Scenario text display (including description, hints, explanation) scenario_text=QTextEdit() scenario_text.setReadOnly(True)
scenario_text.setWordWrapMode(QTextEdit.WordWrap) # allow multiline wrapping # Set scenario text font and color 25

## Page 26

```
scenario_font=QFont("Arial",10) # or another font that supports Hebrew scenario_text.setFont(scenario_font)
```
scenario_text.setStyleSheet("QTextEdit { background-color: #000000; color: #FFA500; }")
# (Using orange (#FFA500) for scenario text by default, can adjust) main_layout.addWidget(scenario_text) # Console output display output_text=QTextEdit() output_text.setReadOnly(True)
output_text.setWordWrapMode(QTextEdit.NoWrap) # preserve output formatting, no wrapping
# Set console font and initial color (we will color output programmatically too) console_font=QFont("Courier New",10)
console_font.setStyleHint(QFont.Monospace) output_text.setFont(console_font)
output_text.setStyleSheet("QTextEdit { background-color: #000000; color: #00FF00; }") main_layout.addWidget(output_text)
# Horizontal layout for input and buttons input_layout=QHBoxLayout() main_layout.addLayout(input_layout) # Input field for cURL command input_field=QLineEdit()
input_field.setPlaceholderText("Type a curl command...") # Monospace font for input as well input_field.setFont(console_font)
input_field.setStyleSheet("QLineEdit { background-color: #111111; color: #00FF00; }") input_layout.addWidget(input_field) # Buttons run_button=QPushButton("Run") hint_button=QPushButton("Hint")
```
solution_button=QPushButton("Show Solution") next_button=QPushButton("Next →") prev_button=QPushButton("← Prev") # Disable some initially hint_button.setEnabled(True) solution_button.setEnabled(True) prev_button.setEnabled(False) next_button.setEnabled(False)
```
# Style the buttons (give them a flat dark look with colored text perhaps) button_style=
```
"QPushButton { background-color: #222; color: #0f0; border: 1px solid #0f0;
```
```
padding: 5px 10px; } QPushButton:disabled { color: #555; border: 1px solid #555; }" 26
```

## Page 27

run_button.setStyleSheet(button_style) hint_button.setStyleSheet(button_style)
solution_button.setStyleSheet(button_style) prev_button.setStyleSheet(button_style) next_button.setStyleSheet(button_style) input_layout.addWidget(run_button) input_layout.addWidget(hint_button) input_layout.addWidget(solution_button) input_layout.addWidget(next_button)
# We will add prev_button to navigate back, though optional in UI flow input_layout.addWidget(prev_button)
# We add Prev at the end for now (it's appended after Next in layout).
# Alternatively, place Prev and Next together separate from Run/Hint/ Solution. # Create a QProcess for running curl process=QProcess()
# We will configure and start this process when needed. # Game state variables current_index=0 total_missions=len(scenarios)
# Track solved status: 0 = not solved, 1 = solved without solution, -1 = solved with solution solved_status=[0]*total_missions
# (Using -1 for solved with help and 1 for solved solo; unsolved 0.) # Function to load a scenario by index defload_scenario(index): globalcurrent_index current_index=index scenario=scenarios[index] # Display scenario narrative scenario_text.clear()
scenario_text.setAlignment(Qt.RightToLeftifscenario["scenario"]and
ord(scenario["scenario"][0])>1279elseQt.AlignLeft)
# The above alignment check: if first char seems Hebrew (Hebrew Unicode range starts ~1488), align right.
# This is a simple heuristic to handle RTL text.
scenario_text.setHtml(f"<span style='font-weight:bold;
```
color:#FFFFFF;'>Mission {index+1}/{total_missions} - {scenario.get('category', '')}</span><br/>"+ f"{scenario['scenario']}")
```
# We display category and scenario description. Category could be in Hebrew or English.
# We made category bold white for emphasis, scenario text in default color (orange). # Reset buttons for this mission 27

## Page 28

hint_button.setEnabled(True) solution_button.setEnabled(True)
next_button.setEnabled(False) # lock next until solved
prev_button.setEnabled(index>0) # prev enabled if not first # Clear any lingering output and input output_text.clear() input_field.clear()
# If there's context needed (like placeholder values), we might mention it in the scenario text or hint.
# The scenario text provided usually contains all info.
# Stop any running process (if user skipped while running) ifprocess.state()!=QProcess.NotRunning: process.kill() # Load first scenario initially iftotal_missions>0: load_scenario(0) else:
scenario_text.setText("No scenarios loaded.") run_button.setEnabled(False) hint_button.setEnabled(False) solution_button.setEnabled(False) next_button.setEnabled(False) prev_button.setEnabled(False) # Run command action defrun_command():
# If a process is already running, interpret this as a cancel/stop action ifprocess.state()!=QProcess.NotRunning: process.kill() run_button.setText("Run") return cmd_text=input_field.text().strip() ifnotcmd_text: return # nothing to run # Ensure the command starts with 'curl' ifcmd_text.startswith("curl"):
# Remove the leading 'curl' for execution because we'll call curl directly cmd_text=cmd_text[len("curl"):].strip() # Prepare process output_text.clear() # Set running state UI feedback run_button.setText("Stop")
run_button.setStyleSheet("QPushButton { background-color: #400; color:
#f44; }") # turn button red to indicate stop
output_text.setPlainText("Running: curl "+cmd_text+"\n") # Show the command being run
# Split the command text into arguments respecting quotes
# We'll do a simple split by spaces for now, but to be robust we can use shlex.split 28

## Page 29

importshlex try: args=shlex.split(cmd_text) exceptExceptionase:
output_text.append(f"[Parsing error] {e}") run_button.setText("Run") run_button.setStyleSheet(button_style) return
# Configure process to capture stdout and stderr process.setProgram("curl") process.setArguments(args)
process.setProcessChannelMode(QProcess.MergedChannels)
# or SeparateChannels to color differently
# (We'll use separate channels to color output vs error)
process.setProcessChannelMode(QProcess.SeparateChannels) process.start()
# If failed to start (e.g., curl not found): ifnotprocess.waitForStarted(100):
output_text.append("[Failed to start curl process]") run_button.setText("Run") run_button.setStyleSheet(button_style) return
# Connect run button to run_command function run_button.clicked.connect(run_command) # Hint button action defshow_hint(): scenario=scenarios[current_index]
```
hint_text=scenario.get("description","") ifhint_text: # Append hint text to scenario_text
```
scenario_text.append(f"\n<span style='color:#AAAAFF; font-style: italic;'>Hint: {hint_text}</span>")
hint_button.setEnabled(False) # one hint per mission (to avoid spamming or multiple identical hints)
# We don't penalize or mark as solved yet; just assist. hint_button.clicked.connect(show_hint) # Solution button action defshow_solution(): scenario=scenarios[current_index] sol_cmd=scenario.get("command","") ifsol_cmd: # Display the solution and explanation
scenario_text.append(f"\n<span style='color:#00FF00;'>Solution: <code>{sol_cmd}</code></span>")
# Insert the solution command into input for convenience input_field.setText(sol_cmd) 29

## Page 30

```
exp_text=scenario.get("explanation","") ifexp_text:
```
scenario_text.append(f"\n<span style='color:#FFFFFF;'>Explanation:</span> {exp_text}") solution_button.setEnabled(False)
hint_button.setEnabled(False) # once solution is shown, hint is moot
# Mark mission as solved with help (-1 score) solved_status[current_index]=-1 # Enable Next to allow proceeding next_button.setEnabled(True)
solution_button.clicked.connect(show_solution) # Next button action defnext_mission(): ifcurrent_index<total_missions-1: load_scenario(current_index+1)
next_button.clicked.connect(next_mission)
# Prev button action (if user wants to go back to review) defprev_mission(): ifcurrent_index>0: load_scenario(current_index-1)
prev_button.clicked.connect(prev_mission) # Process output handling defon_stdout_ready():
```
data=process.readAllStandardOutput().data().decode(errors='ignore') ifdata:
```
# Append standard output in green (already green by default style) output_text.moveCursor(QTextCursor.End) output_text.insertPlainText(data) output_text.moveCursor(QTextCursor.End) defon_stderr_ready():
```
data=process.readAllStandardError().data().decode(errors='ignore') ifdata: # Append error output in red output_text.moveCursor(QTextCursor.End)
```
# Use HTML insertion for red text to differentiate
output_text.insertHtml(f"<span style='color:#FF4444;'>{data}</span>") output_text.moveCursor(QTextCursor.End)
defon_process_finished(exitCode,exitStatus): # Reset run button appearance run_button.setText("Run") run_button.setStyleSheet(button_style)
# If process finished successfully (exitCode 0) and user did not use Show 30

## Page 31

Solution, mark solved if not already
```
ifexitStatus==QProcess.NormalExitandexitCode==0: ifsolved_status[current_index]==0:
```
# If solution was not revealed and not solved yet
# We can attempt to verify if their command matches the expected
solution to count as solved without help. user_cmd=input_field.text().strip()
```
correct_cmd=scenarios[current_index].get("command","").strip()
```
```
ifuser_cmdandcorrect_cmdanduser_cmd==correct_cmd: solved_status[current_index]=1 # Indicate success to user
```
output_text.append("\n[✓ Mission accomplished without help!]") else:
# Even if not exact match, the user might have solved it in an alternative way.
# For simplicity, we mark as solved as well if exitCode 0, because presumably they achieved the goal. solved_status[current_index]=1
output_text.append("\n[✓ Command executed (assuming mission solved).]")
# Enable Next now that a command ran to completion (for flexibility, we
could require match, but let's allow progress) next_button.setEnabled(True) else:
# Non-zero exit code or killed: this might indicate an error or the command didn't achieve the goal.
# We leave solved_status as-is (likely 0 unless user gave up). ifexitStatus==QProcess.NormalExit:
output_text.append(f"\n[ curl exited with code {exitCode}]") ✗ else:
output_text.append("\n[ Command terminated]") ✗
# If this was the last mission and finished, we could show final score.
# If last mission solved or revealed, display final score summary in scenario_text or a popup ifcurrent_index==total_missions-1:
```
solved_count=sum(1forsinsolved_statusifs==1) total=total_missions
```
scenario_text.append(f"\n<b>Game Completed!</b> You solved {solved_count}
out of {total} missions without using the full solution.") # We mark completion with a summary.
process.readyReadStandardOutput.connect(on_stdout_ready)
process.readyReadStandardError.connect(on_stderr_ready)
process.finished.connect(on_process_finished)
# Enable pressing Enter in input_field to trigger Run defhandle_return(): run_button.click()
input_field.returnPressed.connect(handle_return) 31

## Page 32

# Show the main window window.show() app.exec() Explanation of main.py :
- We set up the PySide6 application and main window with a vertical layout of three main parts:
scenario_text (top), output_text (middle), and a horizontal layout for input and buttons (bottom).
- scenario_text is a non-editable QTextEdit where scenario descriptions, hints, and
explanations will be displayed. We detect if the text begins with a Hebrew character to set right-
to-left alignment (so Hebrew text is properly aligned to the right). We use HTML formatting to
style the text (for example, making the mission title bold and white, coloring hints differently).
- output_text is the console output area, also a QTextEdit (read-only). We set a monospaced
font and initially color text green globally. We actually use insertHtml for error messages in red when needed.
- The input is a QLineEdit with a monospaced font and green text on black background. Pressing
Enter triggers the same action as clicking "Run".
- We create buttons for Run, Hint, Solution, Next, Prev, and style them via CSS for the neon look.
The "Next" and "Prev" handle navigation between missions.
- We use a QProcess object ( process ) to run curl. It is configured to capture stdout and stderr separately.
- load_scenario(index) is a function to populate the UI with the scenario at the given index:
it updates the scenario_text with the mission description and category, resets the output and
input, and updates button states (disabling Next until solved, etc.).
- We initially load the first scenario (index 0).
- Run Command logic ( run_command ): When Run is clicked, if a process is already running, we
interpret it as a cancel (kill the process and reset the button). Otherwise, we retrieve the text
from the input, strip any leading "curl" (so users can include it or not), use shlex.split to
parse it into arguments, and start the QProcess with program "curl" and those arguments. We
temporarily change the Run button text to "Stop" and color to red, and display "Running: curl
```
[args]" in the output area. If curl fails to start (e.g. not found), we show an error. • We connect QProcess signals:
```
- readyReadStandardOutput -> on_stdout_ready : Reads and decodes any stdout from curl
and appends it to output_text. Since we set the widget's default color to green, it will appear in green.
- readyReadStandardError -> on_stderr_ready : Reads stderr and appends it in red. We do
this by wrapping the stderr text in an HTML span with red color and inserting into the QTextEdit.
```
(QTextEdit supports mixing rich text via insertHtml.)
```
- finished -> on_process_finished : When curl finishes (or is killed), we reset the Run
button to "Run" (and green color). Then we analyze the result:
◦ If curl exited normally with code 0, we consider that the user’s command achieved its
objective (at least it ran successfully). If the mission wasn’t already marked solved
```
(solved_status still 0), we then check if the command exactly matches the expected
```
solution string. If yes, mark as solved without help (score +1). If not exactly but still exit 0,
it might mean they solved it in an alternative way or partially; we still mark solved (to
allow progress) but it's up to interpretation. We append a success marker ( [✓ Mission accomplished] ) to output. 32

## Page 33

◦ If curl had a non-zero exit code (or was terminated), we consider the mission not solved
yet. We append a failure marker ( [ ...] ) to hint that the attempt didn't fully succeed. ✗
The user can try again or use hint/solution. (We do not automatically disable Next
because they might still choose to skip or reveal solution.)
◦ We also handle if it was the last mission – we then display a final summary (count how many solved without help).
- The finished handler also enables the Next button if the process succeeded (exit 0) to allow
moving on. (We also enable Next when they click "Show Solution", since that is another way to complete the mission.)
- Hint button: Appends the hint (description text from JSON) to the scenario_text in a different
color and italic style, and disables itself.
- Show Solution button: Inserts the solution command and explanation into the scenario_text
```
(solution in green, explanation in white). It also puts the solution into the input field so the user
```
can run it immediately to see output if they want. It then marks the mission as solved with help (solved_status = -1) and enables Next.
- Next/Prev buttons: Call load_scenario for the next or previous index, respectively,
preserving any progress. Prev allows reviewing past missions (we keep their solved_status and
maybe one could attempt again, though in this code we don’t reset solved_status on going back).
- We also update the scenario_text to show mission number and category at the top for context.
- Scoring: We maintain solved_status list. We increment a count in the end for those with
value 1 (solved without help). This is displayed in the final message. Optionally, we could also
show partial scores live, but we kept it to final summary to keep interface clean.
- The code comments indicate where further polish can be added (like verifying alternative correct
commands, etc.). As is, it gives the basic functionality required. File: README.md
Finally, an organized README to guide the user to install and run the game on their machine, including
any adaptation needed for M1 Macs and usage instructions: # cURL Learning Game - README ## Introduction
This is an interactive learning game for the `curl` command. It presents a
series of scenarios where `curl` can be used in various advanced ways
```
(security testing, API usage, networking tricks, etc.). The user can practice
```
writing `curl` commands, see real output/errors, and learn from hints or
solutions. It's both educational and fun, with a "cyber" themed interface.
This README will help you set up and run the game on your computer. ## Requirements -**Python 3.7+** installed.
-**PySide6** library (Qt for Python) installed.
-The system `curl` command should be available in your PATH. (On macOS and
Linux, curl is usually pre-installed. On Windows, you may need to install
curl or use Git Bash/WSL where curl is available.)
-The game is tested on macOS (including Apple M1), and should also run on
Linux or Windows (though the scenarios assume Unix-like paths and behaviors 33

## Page 34

in some cases).
**Note for Apple M1 (Apple Silicon) users:** PySide6 (Qt6) supports M1
natively. You can install PySide6 via pip (see below). If you encounter
issues installing, make sure you're using a Python build that runs natively on M1 (or use Rosetta as a fallback). ## Installation
1.**Install Python 3** if not already installed. On macOS, you can use
Homebrew (`brew install python3`) or download from Python.org.
2.**Create a virtual environment (optional but recommended):** ```bash python3-mvenvvenv
sourcevenv/bin/activate # on Windows: venv\Scripts\activate ``` 3.**Install required packages:** ```bash pipinstallPySide6 ```
This will install PySide6 which includes the Qt libraries.
*If the above fails on M1 Mac:* Ensure pip is updated (`pip install --
upgrade pip`) and try again. If you still have trouble, you can try `pip
install PyQt6` as an alternative (the code should work with minimal changes
for PyQt6 as well, just replace the imports).
## 4. No other dependencies are needed; we use the system's `curl`.
5.**Download the game code**: Make sure you have `main.py` and
`scenario_data.json` in the same directory. (If you've copied this from a
single file, split the JSON out into its own file named exactly `scenario_data.json`.)
6.**Verify `curl` availability:** Open a terminal and run `curl --version`.
If it prints version info, you're good. If not, install curl (on macOS it
should be present; on Windows, either install curl or run the game in an
environment where curl exists, like Git Bash or Windows 10's built-in curl in Command Prompt). ## Running the Game
Activate your Python environment (if you made one) and run: ```bash python main.py
This will launch the GUI window for the cURL learning game.
On first launch, the window will show the first mission scenario. You might see something like (if you read Hebrew): 34

## Page 35

עדימ תחטבא - 1/30 המישמ [Scenario description in Hebrew...]
The interface is dark-themed with green text on black, etc.
Basic usage: - Read the scenario description at the top. It explains the situation and what you need to
achieve with curl. - In the bottom text field, type a curl command that you think will solve the mission.
You can include all usual curl options. For example, if the mission is about making a HEAD request, you
might type curl -I https://example.com . - Press Enter or click Run to execute. The output (or
error) will appear in the middle console area. - Analyze the output. If it's not what you expect (maybe an
error or incomplete result), adjust your command and run again. - If you're stuck, click Hint. A hint will
appear in the scenario description area (usually giving you a clue like which curl option or approach to
consider). - If you still need help, click Show Solution. This will display the recommended solution
command and an explanation of it. The solution command will also be loaded into the input field; you
can run it to see it in action. - Once you've solved the mission (either by finding the right command or by
viewing the solution), the Next → button will be enabled. Click it to move to the next mission. - You can
use ← Prev to go back to previous missions (for review or retry), although your score won't change for
already solved missions. - Continue through all missions. At the end, you'll see a summary of how many you solved without using the solution.
During execution: - The Run button turns into Stop while a command is running. If a command is
hanging (e.g., waiting too long), you can click Stop to terminate it. - Some missions deliberately involve
timeouts or long waits (to illustrate --max-time or similar). In those cases, even if you don't stop, the
curl will stop by itself after the timeout. Just be patient or adjust your command/timeouts if
experimenting. - The output console will color errors in red. For instance, if you see something like "curl:
```
(6) Could not resolve host: ..." in red, that means DNS resolution failed – perhaps you need to adjust the
```
command or ensure you're online. - The program adds no artificial output except messages in brackets
```
[...] indicating if a mission was counted as solved. All other output is directly from curl. So you can trust it as real behavior. Adapting/Customizing
```
- Adding Missions: You can add your own scenarios to scenario_data.json . Follow the same
```
structure: each entry is a JSON object with "command" , "description" , "explanation" ,
```
```
"category" , and "scenario" . Make sure to respect JSON syntax (comma between objects,
```
quotes around strings, etc.). After editing, save the file and restart the game. Your new missions
will appear (most likely at the end of the list if you appended).
- Language: The provided missions are in Hebrew (with some technical terms in English). If you
prefer to translate or add English scenarios, you can do so in the JSON. The interface itself can be
easily translated (just change the button text labels in main.py to Hebrew or any language).
- UI Themes: The colors and fonts are set in main.py via stylesheets. Feel free to tweak these.
For example, to use a different font, change the QFont in the code. To adjust colors, edit the
color codes in the styleSheet strings. You can also enhance the UI (since it's Python/Qt) by adding
images or sounds. For instance, you could add a background image by setting a stylesheet on the window or scenario_text with
background-image: url("path/to/image.png"); .
- Running on Windows: PySide6 works on Windows as well. The main difference is ensuring
curl is accessible. Windows 10 and above include a curl.exe in C:\Windows\System32 .
If for some reason it's not found, you might need to add that path to your PATH environment 35

## Page 36

variable or use the full path in the code (you could modify process.setProgram("curl") to
process.setProgram("curl.exe") or the exact path). Another adaptation might be needed
for the shlex.split usage if Windows paths with backslashes are present (shlex should handle quotes properly, though).
- Apple M1 specifics: If using a Python environment under Rosetta (x86 emulation), PySide6
might have installed an x86 build of Qt. It's generally fine, but for best performance use a native
arm64 Python environment. The game itself doesn't do heavy computations, so either way
should be smooth. No further changes are needed for M1.
- Performance: The game is lightweight. Each mission's curl command runs as a separate
process. We don't expect high CPU/GPU usage. The JSON loading is trivial. The UI should handle
dozens of missions without issue. If you add a very large number of missions, consider adding a
menu to jump to a mission or categorize them.
### Troubleshooting
- If the game window appears but is blank or not interactive, make sure you have loaded the JSON
correctly and that Python didn't output an error in the console. Run python main.py from a terminal to see any error messages.
- If clicking Run does nothing: check that curl is in PATH. For debugging, you can add a print in
run_command to print shlex.split result to see if the command is parsed incorrectly.
- If the GUI elements look too small or text is cut off, you can resize the window or adjust the font
sizes in the code. We set default size to 900x600, but on very high DPI screens you might want to maximize it.
- If PySide6 is not installing on your platform, you can try PyQt6 as an alternative. The code
differences are minor (mostly import statements). In main.py , replace from
PySide6.QtWidgets with from PyQt6.QtWidgets (and similarly for QtGui, QtCore). Also
use app.exec() vs app.exec() if needed (PyQt uses exec by returning an int; PySide allows both).
- Make sure scenario_data.json is in the same directory you run main.py from, or else provide the correct path. Credits and License
This game concept and content was tailored from a list of advanced curl command examples. Many
thanks to those examples (some inspired by real-world cases like Cloudflare WAF bypass, Shellshock
exploit, etc.). The JSON scenario content is in Hebrew to cater to Hebrew-speaking security
professionals, but it can be translated for wider use.
Feel free to modify and distribute this game for educational purposes. (No specific license was provided
in the prompt, but you may treat this as open-source, CC-BY or similar, given it's an educational tool.)
Enjoy learning cURL, and happy hacking! ```
### Conclusion
With the files above, you have a complete solution for a cURL learning game that meets all the specified requirements:
- It uses a modern GUI (Qt via PySide6) with a cyber-themed design (dark mode, custom colors/
fonts) – far more polished than a basic Tkinter interface. 36
|  | curl |
| --- | --- |
| shlex.split |  |

| PySide6.QtWidgets |  |
| --- | --- |
|  | app.exec() |


## Page 37

- It incorporates the provided JSON of cURL commands (and you can add more) to create interactive missions.
- It allows actual execution of cURL commands on the user’s machine, letting them see real
outputs and errors, which is crucial for learning debugging skills.
- The game flow encourages users to try, fail, learn from hints, and eventually see the correct
solution with explanation – reinforcing memory of the commands and their purpose.
- The project is contained in a minimal number of files (main.py, scenario_data.json, README, plus
the ability to expand if needed) for ease of deployment.
- Compatibility with M1 Macs and other platforms is ensured by using Python and Qt (which are cross-platform and have ARM support).
By engaging with this game, users will learn to remember cURL commands and understand the
context and errors associated with each. The competitive element (scoring and progression) and the
creative cyber atmosphere make it a standout educational tool for 2025. 37