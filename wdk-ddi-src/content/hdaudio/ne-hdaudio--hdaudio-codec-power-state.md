---
UID: NE.hdaudio._HDAUDIO_CODEC_POWER_STATE
title: HDAUDIO_CODEC_POWER_STATE
author: windows-driver-content
description: The HDAUDIO_CODEC_POWER_STATE enumeration defines constants that specify the different power states that HD Audio codecs can support. All states are from DEVICE_POWER_STATE except PowerCodecD3Cold.
old-location: audio\hdaudio_codec_power_state.htm
old-project: audio
ms.assetid: 4C002B40-AD27-4FE2-B07F-5E9715E6CF1F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
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
req.alt-api: HDAUDIO_CODEC_POWER_STATE
req.alt-loc: Hdaudio.h
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
req.iface: 
---

# HDAUDIO_CODEC_POWER_STATE enumeration



## -description
<p>The <b>HDAUDIO_CODEC_POWER_STATE</b> enumeration defines constants that specify the different power states that HD Audio codecs can support.  All states
are from <a href="..\wudfddi\ne-wudfddi--device-power-state.md">DEVICE_POWER_STATE</a> except PowerCodecD3Cold.
</p>


## -syntax

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


## -enum-fields
<dl>

### -field PowerCodecUnspecified 

<dd>
<p>An unspecified power state.</p>
</dd>

### -field PowerCodecD0

<dd>
<p>Power state D0</p>
</dd>

### -field PowerCodecD1

<dd>
<p>Power state D1</p>
</dd>

### -field PowerCodecD2

<dd>
<p>Power state D2</p>
</dd>

### -field PowerCodecD3

<dd>
<p>Power state D3</p>
</dd>

### -field PowerCodecD3Cold

<dd>
<p>Power state D3 Cold</p>
</dd>

### -field PowerCodecMaximum

<dd>
<p>Power state Maximum</p>
</dd>
</dl>

## -remarks
<p>For more information about power states, see <a href="..\wudfddi\ne-wudfddi--device-power-state.md">DEVICE_POWER_STATE</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hdaudio.h</dt>
</dl>
</td>
</tr>
</table>