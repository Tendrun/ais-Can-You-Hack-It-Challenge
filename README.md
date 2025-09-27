
# ais-Can-You-Hack-It-Challenge

Collection of small hands-on security puzzles and exercises.  
Categories include client-side protections, exploitation, input validation, networking, programming, reverse engineering, and steganography.

## Goal
Practice common offensive and defensive security techniques. Each folder contains one or more challenges and solution notes or example code. Use this repository as a learning playground or for CTF-style training.

## Repository structure
```
.
├─ Client-side Protections/     # DOM/JS challenges and bypasses
├─ Exploitation/               # Memory, shellcode, exploit examples
├─ Input Validation/           # Injection, XSS, SQLi style tasks
├─ Networking/                 # Protocol, traffic, and sniffing puzzles
├─ Programming/                # Secure coding and crypto puzzles
├─ Reverse Engineering/        # Binary analysis, cracking, disassembly
├─ Steganography/              # Hidden-data and image/audio puzzles
├─ .gitattributes
└─ .idea/                      # IDE config (can be ignored)
```

## How to use
1. Clone:
   ```bash
   git clone https://github.com/Tendrun/ais-Can-You-Hack-It-Challenge.git
   cd ais-Can-You-Hack-It-Challenge
   ```
2. Inspect folders for README or challenge files.
3. Follow per-challenge instructions. Typical patterns:
   - Python scripts: `python3 challenge.py` or open in an editor.
   - Binaries: run inside a contained environment (VM or container). Do not run unknown binaries on host.
   - Web challenges: open local HTML/JS files in browser or start small HTTP server:
     ```bash
     python3 -m http.server 8000
     ```
   - Packet captures: open in Wireshark.
4. Use common tooling: `gdb`, `radare2`, `ghidra`, `strings`, `binwalk`, `exiftool`, `steghide`, `python3`, `openssl`, `curl`, `nc`, `nmap`.

## Safety and environment
- Run untrusted binaries and scripts in isolated VMs or containers.
- Do not expose your host network services.
- Use snapshots and revert after experiments.

## Contributing
- Add a short README for each challenge describing objective, files, and expected flag format (e.g. `FLAG{...}`).
- Include solution notes in a `SOLUTION.md` or `solutions/` folder and mark spoilers.
- Keep challenges self-contained and include any test inputs.

## Example README for a single challenge
```
# Baby's First RE
Files:
- baby_first_re (binary)
- hints.txt

Objective:
Reverse the binary to extract the flag.

Run:
strings baby_first_re | grep FLAG
# or use gdb/ghidra for static analysis

Solution:
See SOLUTION.md
```

## License
Add a license file. If you want permissive reuse use MIT:
```
MIT License
```

---
