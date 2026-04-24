# ONL Streaming Rack Config Summary

Archived source file: [ONL-Streaming-Rack-Config.xlsx](ONL-Streaming-Rack-Config.xlsx)

Primary Drive source:

- [ONL Streaming Rack Config](https://docs.google.com/spreadsheets/d/1JMGN4qKNcqnHObP7pVOS4Mo8iycP0nlGi-JmXWpFFs4)

Related Drive exports:

- [ONL Streaming Rack Config.xlsx](https://drive.google.com/file/d/1nmBs53w0qfgtp_mGyT20JPO5HeancJ4L)
- [ONL Streaming Rack Config.xlsx](https://drive.google.com/file/d/1Cg5j7nFk5VwXBcdZ_BSizwSKJhxzXpuP)

Repo note:

- The Google Sheet is the likely living source.
- The archived workbook is a repo snapshot used for this summary and the current streaming rack documentation.

## What this is

This workbook is a detailed source artifact for the online campus streaming rack and adjacent console setup.

It captures five kinds of operational knowledge in one place:

- point-to-point cabling by source device
- point-to-point cabling by destination device
- named device inventory, network notes, and IP addresses
- rack-unit placement for major hardware
- Smart Videohub input and output labeling

It also includes embedded reference pictures for key hardware and port layouts.

## What it tells us about the system

### 1. The rack is a real signal-routing system, not just a gear list

The workbook documents how the online campus moves signal between:

- the ATEM 2 M/E Constellation switcher
- the Smart Videohub 12x12 router
- HyperDeck recorders
- the Resi decoder
- audio embed and de-embed converters
- the ONL Graphics and ONL Audio computers

That makes this spreadsheet more like an infrastructure map than an inventory sheet.

### 2. The ONL program path is intentionally routed through audio embedding and SDI distribution

The clearest output path in the workbook is:

1. `ZED-14 Sound Board` main outs feed `MiniConverter Audio to SDI 4K`.
2. `ATEM 2 M/E Constellation Switcher` `SDI Out 4` feeds that same converter.
3. `MiniConverter Audio to SDI 4K` sends embedded ONL output into `Smart Videohub 12x12` `SDI In 1`.
4. The Videohub then distributes that feed to recording, lounge display, and switcher return destinations.

This is important because it shows the system depends on both switching and audio embedding to create the final ONL output.

### 3. ROC, audience, and monitoring feeds are distinct paths

The workbook shows separate paths for:

- ROC input coming from the data center over fiber into `MiniConverter Optical Fiber`
- audience input coming from the graphics computer through the OWC dock and `Decimator MD-HX`
- multiview and lounge-monitor outputs routed separately through the Videohub

That separation matters for troubleshooting because a failure in one path does not necessarily mean the whole rack is down.

### 4. The graphics machine is the primary control computer

`ONL Graphics (Mac Studio 2023)` appears to own several important roles:

- ProPresenter output on HDMI
- stage display output through the HDMI converter
- audience input path through Thunderbolt and the OWC dock
- program loopback from `Ultra Studio Recorder 3G`
- local control accessories through USB hub and Stream Decks

The `ONL Audio (Mac Mini 2018)` appears to be a secondary production node focused on audio display, control peripherals, and backup storage.

### 5. The sheet preserves practical network knowledge

The workbook includes IP information for several networked devices:

- `ATEM 2 M/E Constellation Switcher`: `10.20.193.137`
- `HyperDeck Studio HD Mini`: `10.20.193.113`
- `HyperDeck Studio HD Plus`: `10.20.193.141`
- `ONL Audio (Mac Mini 2018)`: `10.20.193.100`
- `ONL Graphics (Mac Studio 2023)`: `10.20.193.129`
- `Resi Decoder`: `10.20.193.133`
- `Smart Videohub 12x12`: `10.20.193.111`

It also notes that both HyperDeck devices were moved from older static IPs to DHCP.

### 6. The rack map is good enough to support physical troubleshooting

The worksheet identifies major rack positions, including:

- `36`: `Smart Videohub 12x12`
- `35`: `OWC THUNDERBOLT DOCK`
- `34`: `FURMAN RP-8L`
- `33`: `HyperDeck Studio HD Plus` and `HyperDeck Studio HD Mini`
- `32`: `ATEM 2 M/E Constellation Switcher`
- `30`: `Corning LANscape Fiber Optic Closet Connector Housing`
- `29`: `Grass Valley iDDR T2`
- `24`: `ONL GRAPHICS (Mac Studio 2023)`
- `22`: `ONL AUDIO (Mac Mini 2018)`
- `21`: `Resi Decoder D2201`
- `5`: `Cisco SG112-24`
- `4`: `WattBox IP Power Conditioner`

That makes this artifact useful during onsite troubleshooting when someone needs to find the right device quickly.

## Notable unresolved details in the workbook

- `ATEM` multiview outputs are marked `YES?` for audio with the note: can we find a way to embed sound here?
- `ONL Audio (Mac Mini 2018)` lists `TB4 Port ?` for the LaCie drive, which is likely a documentation shortcut rather than a precise port label.
- Several Videohub ports are unnamed or unused in the current workbook.

These are good candidates for cleanup or on-site verification later.

## How it maps to the current repo

- The preserved source artifact belongs in [Archive Overview](README.md).
- The durable operating knowledge belongs in [Streaming Rack System](../operations/streaming-rack-system.md).
- The broader systems index belongs in [Technical Systems](../operations/technical-systems.md).

## Suggested follow-up work from this artifact

1. Validate whether the listed IP addresses are still current.
2. Confirm whether the HyperDeck DHCP note is still accurate.
3. Add a startup, shutdown, and recovery procedure for the rack.
4. Document the normal Videohub routes as expected states, not only as labels.
5. Add a short troubleshooting guide for audio-embed, fiber, and audience-input failures.

## Bottom line

This workbook is worth preserving because it contains tribal knowledge about the online campus rack that would be hard to reconstruct quickly from memory.

It is one of the strongest source artifacts in the repo so far for turning the streaming environment from personal knowledge into shared documentation.
