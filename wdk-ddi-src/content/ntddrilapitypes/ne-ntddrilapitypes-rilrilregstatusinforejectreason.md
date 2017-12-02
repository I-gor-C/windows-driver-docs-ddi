---
UID: NE.ntddrilapitypes.RILRILREGSTATUSINFOREJECTREASON
title: RILRILREGSTATUSINFOREJECTREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrilregstatusinforejectreason.htm
old-project: netvista
ms.assetid: 17aad504-4223-4764-8a24-536a81807650
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
req.alt-api: RILRILREGSTATUSINFOREJECTREASON
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

# RILRILREGSTATUSINFOREJECTREASON enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILRILREGSTATUSINFOREJECTREASON { 
  RIL_REGREJECTREASON_IMSIUNK_HLR,
  RIL_REGREJECTREASON_ILLEGAL_MS,
  RIL_REGREJECTREASON_IMSIUNK_VLR,
  RIL_REGREJECTREASON_IMSI_NOTACCEPTED,
  RIL_REGREJECTREASON_ILLEGAL_ME,
  RIL_REGREJECTREASON_PLMN_NOTALLOWED,
  RIL_REGREJECTREASON_LOCAREA_NOTALLOWED,
  RIL_REGREJECTREASON_ROAMING_NOTALLOWED,
  RIL_REGREJECTREASON_NOSUITABLECELL,
  RIL_REGREJECTREASON_NETWORKFAILURE,
  RIL_REGREJECTREASON_MACFAILURE,
  RIL_REGREJECTREASON_SYNCHFAILURE,
  RIL_REGREJECTREASON_CONGESTION,
  RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED,
  RIL_REGREJECTREASON_CSG_NOTAUTHORIZED,
  RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED,
  RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED,
  RIL_REGREJECTREASON_SVCOPT_OUTOFORDER
} RILRILREGSTATUSINFOREJECTREASON;
````


## -enum-fields
<dl>

### -field RIL_REGREJECTREASON_IMSIUNK_HLR

<dd></dd>

### -field RIL_REGREJECTREASON_ILLEGAL_MS

<dd></dd>

### -field RIL_REGREJECTREASON_IMSIUNK_VLR

<dd></dd>

### -field RIL_REGREJECTREASON_IMSI_NOTACCEPTED

<dd></dd>

### -field RIL_REGREJECTREASON_ILLEGAL_ME

<dd></dd>

### -field RIL_REGREJECTREASON_PLMN_NOTALLOWED

<dd></dd>

### -field RIL_REGREJECTREASON_LOCAREA_NOTALLOWED

<dd></dd>

### -field RIL_REGREJECTREASON_ROAMING_NOTALLOWED

<dd></dd>

### -field RIL_REGREJECTREASON_NOSUITABLECELL

<dd></dd>

### -field RIL_REGREJECTREASON_NETWORKFAILURE

<dd></dd>

### -field RIL_REGREJECTREASON_MACFAILURE

<dd></dd>

### -field RIL_REGREJECTREASON_SYNCHFAILURE

<dd></dd>

### -field RIL_REGREJECTREASON_CONGESTION

<dd></dd>

### -field RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED

<dd></dd>

### -field RIL_REGREJECTREASON_CSG_NOTAUTHORIZED

<dd></dd>

### -field RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED

<dd></dd>

### -field RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED

<dd></dd>

### -field RIL_REGREJECTREASON_SVCOPT_OUTOFORDER

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