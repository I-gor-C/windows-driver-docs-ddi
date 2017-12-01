---
UID: NS.rilapitypes.RILOPENUICCLOGICALCHANNELPARAMS
title: RILOPENUICCLOGICALCHANNELPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilopenuicclogicalchannelparams_2.htm
old-project: netvista
ms.assetid: 067d33bf-33d5-49b7-9923-8c893d0b9184
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILOPENUICCLOGICALCHANNELPARAMS, RILOPENUICCLOGICALCHANNELPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILOPENUICCLOGICALCHANNELPARAMS
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILOPENUICCLOGICALCHANNELPARAMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILOPENUICCLOGICALCHANNELPARAMS {
  DWORD                  dwSlotIndex;
  DWORD                  dwChannelGroup;
  DWORD                  dwAppIdLength;
  BYTE [MAXLENGTH_APPID] bAppId;
  DWORD                  dwSelectP2Arg;
} RILOPENUICCLOGICALCHANNELPARAMS, RILOPENUICCLOGICALCHANNELPARAMS;
````


## -struct-fields
<dl>

### -field <b>dwSlotIndex</b>

<dd></dd>

### -field <b>dwChannelGroup</b>

<dd></dd>

### -field <b>dwAppIdLength</b>

<dd></dd>

### -field <b>bAppId</b>

<dd></dd>

### -field <b>dwSelectP2Arg</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>