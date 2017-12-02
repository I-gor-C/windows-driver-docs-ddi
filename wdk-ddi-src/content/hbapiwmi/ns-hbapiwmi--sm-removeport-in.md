---
UID: NS.hbapiwmi._SM_RemovePort_IN
title: SM_RemovePort_IN
author: windows-driver-content
description: The SM_RemovePort_IN structure is used to provide input parameters to the SM_RemovePort WMI method.
old-location: storage\sm_removeport_in.htm
old-project: storage
ms.assetid: b8eb6321-928f-4366-9553-c75900fa1ac6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_RemovePort_IN, SM_RemovePort_IN, *PSM_RemovePort_IN
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
req.alt-api: SM_RemovePort_IN
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

# SM_RemovePort_IN structure



## -description
<p>The SM_RemovePort_IN structure is used to provide input parameters to the SM_RemovePort WMI method.</p>


## -syntax

````
typedef struct _SM_RemovePort_IN {
  UCHAR PortWWN[8];
  ULONG EventType;
} SM_RemovePort_IN, *PSM_RemovePort_IN;
````


## -struct-fields
<dl>

### -field PortWWN

<dd>
<p>A worldwide name (WWN) that indicates the port that should be removed from the list of ports whose events are reported to the WMI client.</p>
</dd>

### -field EventType

<dd>
<p>An event type value.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_RemovePort_IN structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_EventControl WMI class.</p>

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