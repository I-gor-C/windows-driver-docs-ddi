---
UID: NE.rilapitypes.RILMSGCDMATELESERVICE
title: RILMSGCDMATELESERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmateleservice_2.htm
old-project: netvista
ms.assetid: 35d3e419-ad21-403d-8590-f49cf6fd3b25
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGCDMATELESERVICE
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

# RILMSGCDMATELESERVICE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>