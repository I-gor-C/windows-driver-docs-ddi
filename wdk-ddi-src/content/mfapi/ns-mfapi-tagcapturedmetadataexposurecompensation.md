---
UID: NS.mfapi.tagCapturedMetadataExposureCompensation
title: tagCapturedMetadataExposureCompensation
author: windows-driver-content
description: This structure contains blob information for the EV compensation feedback for the photo captured.
old-location: stream\capturedmetadataexposurecompensation.htm
ms.assetid: B7C32495-F9A1-4206-81D2-DCA247F83901
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
req.alt-api: CapturedMetadataExposureCompensation
req.alt-loc: Mfapi.h
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
ms.keywords: tagCapturedMetadataExposureCompensation, CapturedMetadataExposureCompensation
req.iface: 
---

# tagCapturedMetadataExposureCompensation structure



## -description
<p>This structure contains blob information for the EV compensation feedback for the photo captured.</p>


## -syntax

````
typedef struct tagCapturedMetadataExposureCompensation {
  UINT64 Flags;
  INT32  Value;
} CapturedMetadataExposureCompensation;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>A KSCAMERA_EXTENDEDPROP_EVCOMP_XXX step flag.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The EV compensation value in units of the step specified.</p>
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
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>