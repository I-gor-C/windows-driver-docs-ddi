---
UID: NS.MFAPI.TAGCAPTUREDMETADATAEXPOSURECOMPENSATION
title: tagCapturedMetadataExposureCompensation
author: windows-driver-content
description: This structure contains blob information for the EV compensation feedback for the photo captured.
old-location: stream\capturedmetadataexposurecompensation.htm
old-project: stream
ms.assetid: B7C32495-F9A1-4206-81D2-DCA247F83901
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: tagCapturedMetadataExposureCompensation, CapturedMetadataExposureCompensation
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
---

# tagCapturedMetadataExposureCompensation structure



## -description
This structure contains blob information for the EV compensation feedback for the photo captured.



## -syntax

````
typedef struct tagCapturedMetadataExposureCompensation {
  UINT64 Flags;
  INT32  Value;
} CapturedMetadataExposureCompensation;
````


## -struct-fields

### -field Flags

A KSCAMERA_EXTENDEDPROP_EVCOMP_XXX step flag.


### -field Value

The EV compensation value in units of the step specified.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>