---
UID: NE.ntddrilapitypes.RILPERSOFEATURE
title: RILPERSOFEATURE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersofeature.htm
old-project: netvista
ms.assetid: e212ab20-e9b4-4ccc-b0db-a82ca5b59573
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
req.alt-api: RILPERSOFEATURE
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

# RILPERSOFEATURE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILPERSOFEATURE { 
  RIL_PERSOFEATURE_3GPP_NET,
  RIL_PERSOFEATURE_3GPP_NETSUB,
  RIL_PERSOFEATURE_3GPP_SP,
  RIL_PERSOFEATURE_3GPP_CORP,
  RIL_PERSOFEATURE_3GPP_USIM,
  RIL_PERSOFEATURE_3GPP2_NETTYPE1,
  RIL_PERSOFEATURE_3GPP2_NETTYPE2,
  RIL_PERSOFEATURE_3GPP2_HRPD,
  RIL_PERSOFEATURE_3GPP2_SP,
  RIL_PERSOFEATURE_3GPP2_CORP,
  RIL_PERSOFEATURE_3GPP2_UIM,
  RIL_PERSOFEATURE_ALL
} RILPERSOFEATURE;
````


## -enum-fields
<dl>

### -field RIL_PERSOFEATURE_3GPP_NET

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP_NETSUB

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP_SP

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP_CORP

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP_USIM

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP2_NETTYPE1

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP2_NETTYPE2

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP2_HRPD

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP2_SP

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP2_CORP

<dd></dd>

### -field RIL_PERSOFEATURE_3GPP2_UIM

<dd></dd>

### -field RIL_PERSOFEATURE_ALL

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