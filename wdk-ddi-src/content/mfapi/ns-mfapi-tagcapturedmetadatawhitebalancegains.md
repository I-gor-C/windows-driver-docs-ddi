---
UID: NS.mfapi.tagCapturedMetadataWhiteBalanceGains
title: tagCapturedMetadataWhiteBalanceGains
author: windows-driver-content
description: This structure describes the blob format for the MF_CAPTURE_METADATA_WHITEBALANCE_GAINS attribute.
old-location: stream\capturedmetadatawhitebalancegains.htm
ms.assetid: 1F844204-0709-4203-80C5-C90949F96159
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CapturedMetadataWhiteBalanceGains
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
ms.keywords: tagCapturedMetadataWhiteBalanceGains, CapturedMetadataWhiteBalanceGains
req.iface: 
---

# tagCapturedMetadataWhiteBalanceGains structure



## -description
<p>This structure describes the blob format for the <b>MF_CAPTURE_METADATA_WHITEBALANCE_GAINS</b> attribute.  </p>


## -syntax

````
typedef struct tagCapturedMetadataWhiteBalanceGains {
  FLOAT R;
  FLOAT G;
  FLOAT B;
} CapturedMetadataWhiteBalanceGains;
````


## -struct-fields
<dl>

### -field <b>R</b>

<dd>
<p>The  <b>R</b> value of the blob.</p>
</dd>

### -field <b>G</b>

<dd>
<p>The  <b>G</b> value of the blob.</p>
</dd>

### -field <b>B</b>

<dd>
<p>The  <b>B</b> value of the blob.</p>
</dd>
</dl>

## -remarks
<p>The <b>MF_CAPTURE_METADATA_WHITEBALANCE_GAINS</b> attribute contains the white balance gains applied to R, G, B by the sensor or ISP when the preview frame was captured. This is a unitless.</p>

<p>The <b>CapturedMetadataWhiteBalanceGains</b> structure only describes the blob format for the <b>MF_CAPTURE_METADATA_WHITEBALANCE_GAINS</b> attribute.  The metadata item structure for white balance gains (<a href="https://msdn.microsoft.com/library/windows/hardware/dn925184">KSCAMERA_METADATA_ITEMHEADER</a> + white balance gains metadata payload) is up to driver and must be 8-byte aligned.</p>

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