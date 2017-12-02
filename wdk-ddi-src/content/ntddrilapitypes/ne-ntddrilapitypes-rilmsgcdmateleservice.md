---
UID: NE.ntddrilapitypes.RILMSGCDMATELESERVICE
title: RILMSGCDMATELESERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmateleservice.htm
old-project: netvista
ms.assetid: 01c45c31-2cae-4f9f-a3dc-4a164a3df670
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
req.alt-api: RILMSGCDMATELESERVICE
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

# RILMSGCDMATELESERVICE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGCDMATELESERVICE { 
  RIL_MSGTELESERVICE_MESSAGING_OLD,
  RIL_MSGTELESERVICE_VOICEMAIL_OLD,
  RIL_MSGTELESERVICE_WAP_OLD,
  RIL_MSGTELESERVICE_BROADCAST_OLD,
  RIL_MSGTELESERVICE_SELFREG_OLD,
  RIL_MSGTELESERVICE_PAGING,
  RIL_MSGTELESERVICE_MESSAGING,
  RIL_MSGTELESERVICE_WEMT,
  RIL_MSGTELESERVICE_VOICEMAIL_VMN_95,
  RIL_MSGTELESERVICE_VOICEMAIL_MWI,
  RIL_MSGTELESERVICE_WAP,
  RIL_MSGTELESERVICE_WAP_CT_MMS,
  RIL_MSGTELESERVICE_WAP_CT_OMA,
  RIL_MSGTELESERVICE_BROADCAST,
  RIL_MSGTELESERVICE_SELFREG
} RILMSGCDMATELESERVICE;
````


## -enum-fields
<dl>

### -field RIL_MSGTELESERVICE_MESSAGING_OLD

<dd></dd>

### -field RIL_MSGTELESERVICE_VOICEMAIL_OLD

<dd></dd>

### -field RIL_MSGTELESERVICE_WAP_OLD

<dd></dd>

### -field RIL_MSGTELESERVICE_BROADCAST_OLD

<dd></dd>

### -field RIL_MSGTELESERVICE_SELFREG_OLD

<dd></dd>

### -field RIL_MSGTELESERVICE_PAGING

<dd></dd>

### -field RIL_MSGTELESERVICE_MESSAGING

<dd></dd>

### -field RIL_MSGTELESERVICE_WEMT

<dd></dd>

### -field RIL_MSGTELESERVICE_VOICEMAIL_VMN_95

<dd></dd>

### -field RIL_MSGTELESERVICE_VOICEMAIL_MWI

<dd></dd>

### -field RIL_MSGTELESERVICE_WAP

<dd></dd>

### -field RIL_MSGTELESERVICE_WAP_CT_MMS

<dd></dd>

### -field RIL_MSGTELESERVICE_WAP_CT_OMA

<dd></dd>

### -field RIL_MSGTELESERVICE_BROADCAST

<dd></dd>

### -field RIL_MSGTELESERVICE_SELFREG

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