---
UID: NS.hbapiwmi._SM_GetPersistentBinding_IN
title: SM_GetPersistentBinding_IN
author: windows-driver-content
description: The SM_GetPersistentBinding_IN structure is used to provide input parameters to the SM_GetPersistentBinding method.
old-location: storage\sm_getpersistentbinding_in.htm
old-project: storage
ms.assetid: 6c716394-1e82-40d2-befc-50a0ea88f750
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_GetPersistentBinding_IN, SM_GetPersistentBinding_IN, *PSM_GetPersistentBinding_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_GetPersistentBinding_IN
req.alt-loc: hbapiwmi.h
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

# SM_GetPersistentBinding_IN structure



## -description
<p>The SM_GetPersistentBinding_IN structure is used to provide input parameters to the SM_GetPersistentBinding method.</p>


## -syntax

````
typedef struct _SM_GetPersistentBinding_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DomainPortWWN[8];
  ULONG InEntryCount;
} SM_GetPersistentBinding_IN, *PSM_GetPersistentBinding_IN;
````


## -struct-fields
<dl>

### -field <b>HbaPortWWN</b>

<dd>
<p>The worldwide name (WWN) of the local port whose events the WMI client will receive.</p>
</dd>

### -field <b>DomainPortWWN</b>

<dd>
<p>A worldwide name (WWN) that specifies the SAS domain worldwide name of the local port.</p>
</dd>

### -field <b>InEntryCount</b>

<dd>
<p>The number of persistent bindings that are associated with the HBA.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_GetPersistentBinding_IN structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_TargetInformationMethods WMI class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>