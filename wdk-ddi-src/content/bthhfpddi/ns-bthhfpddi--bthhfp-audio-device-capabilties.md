---
UID: NS.bthhfpddi._BTHHFP_AUDIO_DEVICE_CAPABILTIES
title: BTHHFP_AUDIO_DEVICE_CAPABILTIES
author: windows-driver-content
description: The BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure describes the capabilities of a Bluetooth HFP device, including the version and whether it supports 16 kHz sampling.
old-location: audio\bthhfp_audio_device_capabilties.htm
old-project: audio
ms.assetid: 56c2bbb9-8fcd-43d4-9202-c8925575e44d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BTHHFP_AUDIO_DEVICE_CAPABILTIES, BTHHFP_AUDIO_DEVICE_CAPABILTIES, *PBTHHFP_AUDIO_DEVICE_CAPABILTIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTHHFP_AUDIO_DEVICE_CAPABILTIES
req.alt-loc: bthhfpddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# BTHHFP_AUDIO_DEVICE_CAPABILTIES structure



## -description
<p>The <b>BTHHFP_AUDIO_DEVICE_CAPABILTIES</b> data structure describes the capabilities of a Bluetooth HFP device, including the version and whether it supports 16 kHz sampling.</p>


## -syntax

````
typedef struct _BTHHFP_AUDIO_DEVICE_CAPABILTIES {
  DWORD Version;
  BOOL  Supports16kHzSampling;
} BTHHFP_AUDIO_DEVICE_CAPABILTIES, BTHHFP_AUDIO_DEVICE_CAPABILTIES;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the device.</p>
</dd>

### -field <b>Supports16kHzSampling</b>

<dd>
<p>Whether the device supports 16 kHz sampling.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthhfpddi.h</dt>
</dl>
</td>
</tr>
</table>