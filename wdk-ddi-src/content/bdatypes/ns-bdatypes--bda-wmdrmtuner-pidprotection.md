---
UID: NS.bdatypes._BDA_WMDRMTUNER_PIDPROTECTION
title: BDA_WMDRMTUNER_PIDPROTECTION
author: windows-driver-content
description: .
old-location: stream\bda_wmdrmtuner_pidprotection.htm
old-project: stream
ms.assetid: EA2590B0-7EF0-4E5E-A270-A13047BE0F2C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_WMDRMTUNER_PIDPROTECTION, BDA_WMDRMTUNER_PIDPROTECTION, *PBDA_WMDRMTUNER_PIDPROTECTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_WMDRMTUNER_PIDPROTECTION
req.alt-loc: Bdatypes.h
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

# BDA_WMDRMTUNER_PIDPROTECTION structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_WMDRMTUNER_PIDPROTECTION {
  PBDARESULT lResult;
  GUID       uuidKeyID;
} BDA_WMDRMTUNER_PIDPROTECTION, *PBDA_WMDRMTUNER_PIDPROTECTION;
````


## -struct-fields
<dl>

### -field lResult

<dd></dd>

### -field uuidKeyID

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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>