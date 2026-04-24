# Streaming Rack System

Source artifact: [ONL Streaming Rack Config Summary](../archive/onl-streaming-rack-config-summary.md)

Primary Drive source: [ONL Streaming Rack Config](https://docs.google.com/spreadsheets/d/1JMGN4qKNcqnHObP7pVOS4Mo8iycP0nlGi-JmXWpFFs4)

Repo snapshot: [ONL-Streaming-Rack-Config.xlsx](../archive/ONL-Streaming-Rack-Config.xlsx)

## Purpose

This document is the current repo-level source of truth for the online campus streaming rack topology.

It translates the archived workbook into a readable operational reference for setup, troubleshooting, and future documentation work.

## System scope

The rack system includes:

- switching and routing
- recording and playback
- graphics and audio workstations
- signal conversion
- audio monitoring
- networked control devices
- physical rack placement

## Core devices

### Switching and routing

- `ATEM 2 M/E Constellation Switcher`
- `Smart Videohub 12x12`

### Recording and playback

- `HyperDeck Studio HD Plus`
- `HyperDeck Studio HD Mini`
- `Resi Decoder D2201`
- `Grass Valley iDDR T2`

### Production computers

- `ONL Graphics (Mac Studio 2023)`
- `ONL Audio (Mac Mini 2018)`

### Signal conversion and transport

- `MiniConverter Audio to SDI 4K`
- `MiniConverter SDI to Audio 4K`
- `MiniConverter Optical Fiber`
- `MiniConverter SDI to HDMI #1`
- `MiniConverter SDI to HDMI #2`
- `Micro Converter SDI to HDMI 3G`
- `Decimator MD-HX`
- `Ultra Studio Recorder 3G`
- `Thunderbolt 3 to Thunderbolt 2 Adapter (A1790)`
- `Thunderbolt 2 Dock (OWCTB2DOCK12T1)`
- `HDMI Converter`

### Audio and monitoring

- `ZED-14 Sound Board`
- `Dynasty ProdAudio PMC-2`
- `Yamaha Monitor Speaker (Left)`
- `Yamaha Monitor Speaker (Right)`
- `Dell Ultrasharp U2424H` monitors for graphics, audio, stage display, multiview, and Resi
- `Samsung 50" Crystal UHD` lounge display

## Critical signal paths

### ONL program output

The workbook shows this as the main ONL output chain:

1. `ZED-14 Sound Board` `MAIN OUT 1/2` goes to `MiniConverter Audio to SDI 4K` `Channel 1/2`.
2. `ATEM 2 M/E Constellation Switcher` `SDI Out 4` goes to `MiniConverter Audio to SDI 4K` `SDI In`.
3. `MiniConverter Audio to SDI 4K` `SDI Out` goes to `Smart Videohub 12x12` `SDI In 1`.

This produces the embedded ONL output used downstream by the router.

### ONL recording path

- `Smart Videohub 12x12` `SDI Out 2` feeds `HyperDeck Studio HD Mini` for ONL recording.

### ROC path

- `Data Center` `Fiber Out` feeds `MiniConverter Optical Fiber` `Fiber In`.
- `MiniConverter Optical Fiber` `SDI Out` feeds `Smart Videohub 12x12` `SDI In 2`.
- `Smart Videohub 12x12` `SDI Out 3` feeds `HyperDeck Studio HD Plus` for ROC recording.
- `Smart Videohub 12x12` `SDI Out 1` returns ONL back through `MiniConverter Optical Fiber` toward the data center.

### Audience input path

- `ONL Graphics (Mac Studio 2023)` `TB4 Port 1`
- `Thunderbolt 3 to Thunderbolt 2 Adapter (A1790)`
- `Thunderbolt 2 Dock (OWCTB2DOCK12T1)` `HDMI Out`
- `Decimator MD-HX` `HDMI In`
- `Decimator MD-HX` `SDI Out`
- `ATEM 2 M/E Constellation Switcher` `SDI In 06`

The workbook notes this as the audience input from the Mac to the switcher.

### Program loopback to graphics

- `ATEM 2 M/E Constellation Switcher` `SDI Out 5`
- `Ultra Studio Recorder 3G` `SDI In`
- `Ultra Studio Recorder 3G` `T3 Out`
- `ONL Graphics (Mac Studio 2023)` `TB4 Port 4`

The workbook notes this as `M/E1 Program Loopback to Mac`.

### Audio monitoring path

- `ZED-14 Sound Board` `AUX3/4 Out` feeds `Dynasty ProdAudio PMC-2`
- `Dynasty ProdAudio PMC-2` `XLR Out L/R` feeds the two Yamaha monitor speakers
- `ZED-14 Sound Board` `PHONES` feeds local audio headphones

### De-embedded audio return

- `ATEM 2 M/E Constellation Switcher` `SDI Out 6` feeds `MiniConverter SDI to Audio 4K`
- `MiniConverter SDI to Audio 4K` `CH 1/2 Analog` feeds `ZED-14 Sound Board` `LINE 5/6`

## Videohub map

### Inputs

- `1`: `ME1`
- `2`: `ROC IN`
- `3`: `MV1`
- `4`: `MV2`
- `5`: `RESI IN`

### Outputs and expected sources

- `1`: `ONL Out` from `ME1`
- `2`: `HD 2` from `ME1`
- `3`: `HD 1` from `ROC IN`
- `4`: `Lounge HDMI 1` from `ME1`
- `5`: `Lounge HDMI 2` from `MV2`
- `6`: `Switch In 10` from `ME1`
- `7`: `Multiview Console` from `MV1`
- `8`: `Switch In 11` from `RESI IN`

Ports `9` through `12` are not labeled in the workbook and should be verified onsite before they are treated as available.

## Networked devices

The workbook includes the following device addressing notes:

- `ATEM 2 M/E Constellation Switcher`: `10.20.193.137`
- `Smart Videohub 12x12`: `10.20.193.111`
- `HyperDeck Studio HD Mini`: `10.20.193.113`
- `HyperDeck Studio HD Plus`: `10.20.193.141`
- `Resi Decoder`: `10.20.193.133`
- `ONL Audio (Mac Mini 2018)`: `10.20.193.100`
- `ONL Graphics (Mac Studio 2023)`: `10.20.193.129`

Workbook note:

- both HyperDeck devices include notes that older static IPs were replaced and the devices are now using DHCP

These values should be verified before they are used as current network truth.

## Physical rack positions

The workbook identifies these major rack locations:

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
- `3`: `MFA208 AUDAC`
- `2`: `AUDAC SMQ500`

## Known questions and cleanup targets

- The workbook flags `MV 1` and `MV 2` with `YES?` for audio embedding. Treat multiview audio as unconfirmed until tested.
- The `ONL Audio (Mac Mini 2018)` backup-drive note says `TB4 Port ?`; document the exact port naming after onsite verification.
- Several power adapters are identified only by voltage and barrel style. Labeling them physically would reduce troubleshooting risk.
- The workbook is strong on topology but does not yet document startup order, shutdown order, or failure recovery.

## Documentation next steps

1. Confirm current device addresses and note which are static versus DHCP reservations.
2. Add a normal-state startup and shutdown checklist for the rack.
3. Capture expected ATEM input labels and switcher scene assumptions.
4. Add a fault-isolation guide for fiber, audio embedding, HyperDeck recording, and audience-input issues.
5. Split this page later if individual systems need their own deeper docs.
