---
UID: NS.mfapi.tagCapturedMetadataWhiteBalanceGains
title: tagCapturedMetadataWhiteBalanceGains
author: windows-driver-content
description: This structure describes the blob format for the MF_CAPTURE_METADATA_WHITEBALANCE_GAINS attribute.
old-location: stream\capturedmetadatawhitebalancegains.htm
old-project: stream
ms.assetid: 1F844204-0709-4203-80C5-C90949F96159
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagCapturedMetadataWhiteBalanceGains, CapturedMetadataWhiteBalanceGains
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

### -field R

<dd>
<p>The  <b>R</b> value of the blob.</p>
</dd>

### -field G

<dd>
<p>The  <b>G</b> value of the blob.</p>
</dd>

### -field B

<dd>
<p>The  <b>B</b> value of the blob.</p>
</dd>
</dl>

## -remarks
<p>The <b>MF_CAPTURE_METADATA_WHITEBALANCE_GAINS</b> attribute contains the white balance gains applied to R, G, B by the sensor or ISP when the preview frame was captured. This is a unitless.</p>

<p>The <b>CapturedMetadataWhiteBalanceGains</b> structure only describes the blob format for the <b>MF_CAPTURE_METADATA_WHITEBALANCE_GAINS</b> attribute.  The metadata item structure for white balance gains (<a href="stream.kscamera_metadata_itemheader">KSCAMERA_METADATA_ITEMHEADER</a> + white balance gains metadata payload) is up to driver and must be 8-byte aligned.</p>

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