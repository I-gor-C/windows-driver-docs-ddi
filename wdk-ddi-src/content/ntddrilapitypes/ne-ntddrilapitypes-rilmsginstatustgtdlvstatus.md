---
UID: NE.ntddrilapitypes.RILMSGINSTATUSTGTDLVSTATUS
title: RILMSGINSTATUSTGTDLVSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsginstatustgtdlvstatus.htm
old-project: netvista
ms.assetid: 6e22ae6d-55a2-4aa7-993b-67474acc6f7b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGINSTATUSTGTDLVSTATUS
req.alt-loc: ntddrilapitypes.h
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

# RILMSGINSTATUSTGTDLVSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGINSTATUSTGTDLVSTATUS { 
  RIL_MSGDLVSTATUS_FORWARDEDTOSME,
  RIL_MSGDLVSTATUS_REPLACEDBYSC,
  RIL_MSGDLVSTATUS_CONGESTION_TRYING,
  RIL_MSGDLVSTATUS_SMEBUSY_TRYING,
  RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING,
  RIL_MSGDLVSTATUS_SVCREJECTED_TRYING,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING,
  RIL_MSGDLVSTATUS_SMEERROR_TRYING,
  RIL_MSGDLVSTATUS_CONGESTION,
  RIL_MSGDLVSTATUS_SMEBUSY,
  RIL_MSGDLVSTATUS_SMENOTRESPONDING,
  RIL_MSGDLVSTATUS_SVCREJECTED,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP,
  RIL_MSGDLVSTATUS_SMEERROR,
  RIL_MSGDLVSTATUS_REMOTEPROCERROR,
  RIL_MSGDLVSTATUS_INCOMPATIBLEDEST,
  RIL_MSGDLVSTATUS_CONNECTIONREJECTED,
  RIL_MSGDLVSTATUS_NOTOBTAINABLE,
  RIL_MSGDLVSTATUS_NOINTERNETWORKING,
  RIL_MSGDLVSTATUS_VPEXPIRED,
  RIL_MSGDLVSTATUS_DELETEDBYORIGSME,
  RIL_MSGDLVSTATUS_DELETEDBYSC,
  RIL_MSGDLVSTATUS_NOLONGEREXISTS,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL,
  RIL_MSGDLVSTATUS_RESERVED_COMPLETED,
  RIL_MSGDLVSTATUS_RESERVED_TRYING,
  RIL_MSGDLVSTATUS_RESERVED_ERROR,
  RIL_MSGDLVSTATUS_RESERVED_TMPERROR,
  RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED,
  RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING,
  RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR,
  RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR,
  RIL_MSGDLVSTATUS_MAX
} RILMSGINSTATUSTGTDLVSTATUS;
````


## -enum-fields
<dl>

### -field RIL_MSGDLVSTATUS_FORWARDEDTOSME

<dd></dd>

### -field RIL_MSGDLVSTATUS_REPLACEDBYSC

<dd></dd>

### -field RIL_MSGDLVSTATUS_CONGESTION_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_SMEBUSY_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_SVCREJECTED_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_SMEERROR_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_CONGESTION

<dd></dd>

### -field RIL_MSGDLVSTATUS_SMEBUSY

<dd></dd>

### -field RIL_MSGDLVSTATUS_SMENOTRESPONDING

<dd></dd>

### -field RIL_MSGDLVSTATUS_SVCREJECTED

<dd></dd>

### -field RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP

<dd></dd>

### -field RIL_MSGDLVSTATUS_SMEERROR

<dd></dd>

### -field RIL_MSGDLVSTATUS_REMOTEPROCERROR

<dd></dd>

### -field RIL_MSGDLVSTATUS_INCOMPATIBLEDEST

<dd></dd>

### -field RIL_MSGDLVSTATUS_CONNECTIONREJECTED

<dd></dd>

### -field RIL_MSGDLVSTATUS_NOTOBTAINABLE

<dd></dd>

### -field RIL_MSGDLVSTATUS_NOINTERNETWORKING

<dd></dd>

### -field RIL_MSGDLVSTATUS_VPEXPIRED

<dd></dd>

### -field RIL_MSGDLVSTATUS_DELETEDBYORIGSME

<dd></dd>

### -field RIL_MSGDLVSTATUS_DELETEDBYSC

<dd></dd>

### -field RIL_MSGDLVSTATUS_NOLONGEREXISTS

<dd></dd>

### -field RIL_MSGDLVSTATUS_QUALITYUNAVAIL

<dd></dd>

### -field RIL_MSGDLVSTATUS_RESERVED_COMPLETED

<dd></dd>

### -field RIL_MSGDLVSTATUS_RESERVED_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_RESERVED_ERROR

<dd></dd>

### -field RIL_MSGDLVSTATUS_RESERVED_TMPERROR

<dd></dd>

### -field RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED

<dd></dd>

### -field RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING

<dd></dd>

### -field RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR

<dd></dd>

### -field RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR

<dd></dd>

### -field RIL_MSGDLVSTATUS_MAX

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>