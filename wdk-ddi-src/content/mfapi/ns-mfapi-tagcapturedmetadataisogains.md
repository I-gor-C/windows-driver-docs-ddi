---
UID: NS.mfapi.tagCapturedMetadataISOGains
title: tagCapturedMetadataISOGains
author: windows-driver-content
description: The CapturedMetadataISOGains structure describes the blob format for MF_CAPTURE_METADATA_ISO_GAINS.
old-location: stream\capturedmetadataisogains.htm
old-project: stream
ms.assetid: 6B87BDFB-EAD5-496D-BE6A-9AE709119515
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagCapturedMetadataISOGains, CapturedMetadataISOGains
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CapturedMetadataISOGains
req.alt-loc: mfapi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# tagCapturedMetadataISOGains structure



## -description
<p>The CapturedMetadataISOGains structure describes the blob format for <b>MF_CAPTURE_METADATA_ISO_GAINS</b>.</p>


## -syntax

````
typedef struct tagCapturedMetadataISOGains {
  FLOAT AnalogGain;
  FLOAT DigitalGain;
} CapturedMetadataISOGains;
````


## -struct-fields
<dl>

### -field <b>AnalogGain</b>

<dd></dd>

### -field <b>DigitalGain</b>

<dd></dd>
</dl>

## -remarks
<p>The <b>CapturedMetadataISOGains</b> structure only describes the blob format for the <b>MF_CAPTURE_METADATA_ISO_GAINS</b> attribute.  The metadata item structure for ISO gains (<a href="https://msdn.microsoft.com/library/windows/hardware/dn925184">KSCAMERA_METADATA_ITEMHEADER</a> + ISO gains metadata payload) is up to driver and must be 8-byte aligned.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>