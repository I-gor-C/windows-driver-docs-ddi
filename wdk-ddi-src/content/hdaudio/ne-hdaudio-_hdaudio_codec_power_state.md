---
UID: NE:hdaudio._HDAUDIO_CODEC_POWER_STATE
title: "_HDAUDIO_CODEC_POWER_STATE"
author: windows-driver-content
description: The HDAUDIO_CODEC_POWER_STATE enumeration defines constants that specify the different power states that HD Audio codecs can support. All states are from DEVICE_POWER_STATE except PowerCodecD3Cold.
old-location: audio\hdaudio_codec_power_state.htm
old-project: audio
ms.assetid: 4C002B40-AD27-4FE2-B07F-5E9715E6CF1F
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PHDAUDIO_CODEC_POWER_STATE, HDAUDIO_CODEC_POWER_STATE, HDAUDIO_CODEC_POWER_STATE enumeration [Audio Devices], PHDAUDIO_CODEC_POWER_STATE, PHDAUDIO_CODEC_POWER_STATE enumeration pointer [Audio Devices], PowerCodecD0, PowerCodecD1, PowerCodecD2, PowerCodecD3, PowerCodecD3Cold, PowerCodecMaximum, PowerCodecUnspecified, _HDAUDIO_CODEC_POWER_STATE, audio.hdaudio_codec_power_state, hdaudio/HDAUDIO_CODEC_POWER_STATE, hdaudio/PHDAUDIO_CODEC_POWER_STATE, hdaudio/PowerCodecD0, hdaudio/PowerCodecD1, hdaudio/PowerCodecD2, hdaudio/PowerCodecD3, hdaudio/PowerCodecD3Cold, hdaudio/PowerCodecMaximum, hdaudio/PowerCodecUnspecified"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: hdaudio.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Hdaudio.h
api_name:
-	HDAUDIO_CODEC_POWER_STATE
product: Windows
targetos: Windows
req.typenames: HDAUDIO_CODEC_POWER_STATE, *PHDAUDIO_CODEC_POWER_STATE
---

# _HDAUDIO_CODEC_POWER_STATE Enumeration
The <b>HDAUDIO_CODEC_POWER_STATE</b> enumeration defines constants that specify the different power states that HD Audio codecs can support.  All states
are from <a href="..\wudfddi\ne-wudfddi-_device_power_state.md">DEVICE_POWER_STATE</a> except PowerCodecD3Cold.

## Syntax
````
typedef enum _HDAUDIO_CODEC_POWER_STATE { 
  PowerCodecUnspecified   = 0,
  PowerCodecD0,
  PowerCodecD1,
  PowerCodecD2,
  PowerCodecD3,
  PowerCodecD3Cold,
  PowerCodecMaximum
} HDAUDIO_CODEC_POWER_STATE, *PHDAUDIO_CODEC_POWER_STATE;
````

## Constants

<table>
            
                <tr>
                    <td>PowerCodecD0</td>
                    <td>Power state D0</td>
                </tr>
            
                <tr>
                    <td>PowerCodecD1</td>
                    <td>Power state D1</td>
                </tr>
            
                <tr>
                    <td>PowerCodecD2</td>
                    <td>Power state D2</td>
                </tr>
            
                <tr>
                    <td>PowerCodecD3</td>
                    <td>Power state D3</td>
                </tr>
            
                <tr>
                    <td>PowerCodecD3Cold</td>
                    <td>Power state D3 Cold</td>
                </tr>
            
                <tr>
                    <td>PowerCodecMaximum</td>
                    <td>Power state Maximum</td>
                </tr>
            
                <tr>
                    <td>PowerCodecUnspecified</td>
                    <td>An unspecified power state.</td>
                </tr>
</table>

## Remarks

For more information about power states, see <a href="..\wudfddi\ne-wudfddi-_device_power_state.md">DEVICE_POWER_STATE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hdaudio.h |