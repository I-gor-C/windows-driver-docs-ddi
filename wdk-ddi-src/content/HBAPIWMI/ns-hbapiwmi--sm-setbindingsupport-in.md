---
UID: NS.hbapiwmi._SM_SetBindingSupport_IN
title: SM_SetBindingSupport_IN
author: windows-driver-content
description: The SM_SetBindingSupport_IN structure is used to provide input parameters to the SM_SetBindingSupport method.
old-location: storage\sm_setbindingsupport_in.htm
ms.assetid: 7bcee845-9b3f-4ad7-843f-1f4cd74ee1be
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_SetBindingSupport_IN
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
ms.keywords: SM_SetBindingSupport_IN, SM_SetBindingSupport_IN, *PSM_SetBindingSupport_IN
req.iface: 
---

# SM_SetBindingSupport_IN structure



## -description
<p>The SM_SetBindingSupport_IN structure is used to provide input parameters to the SM_SetBindingSupport method.</p>


## -syntax

````
typedef struct _SM_SetBindingSupport_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DomainPortWWN[8];
  ULONG Flags;
} SM_SetBindingSupport_IN, *PSM_SetBindingSupport_IN;
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

### -field <b>Flags</b>

<dd>
<p>The HBA_BIND_CAPABILITY binding capabilities.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_SetBindingSupport_IN structure in <i>Hbapiwmi.h</i> when it compiles the MS_SMHBA_BindingEntry WMI class.</p>

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