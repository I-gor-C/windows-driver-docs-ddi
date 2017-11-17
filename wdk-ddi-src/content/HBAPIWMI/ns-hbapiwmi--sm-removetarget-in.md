---
UID: NS.hbapiwmi._SM_RemoveTarget_IN
title: SM_RemoveTarget_IN
author: windows-driver-content
description: The SM_RemoveTarget_IN structure is used to provide input parameters to the SM_RemoveTarget WMI method.
old-location: storage\sm_removetarget_in.htm
ms.assetid: a32e2442-a6a8-4c1a-ab70-40fdb525bafb
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
req.alt-api: SM_RemoveTarget_IN
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
ms.keywords: SM_RemoveTarget_IN, SM_RemoveTarget_IN, *PSM_RemoveTarget_IN
req.iface: 
---

# SM_RemoveTarget_IN structure



## -description
<p>The SM_RemoveTarget_IN structure is used to provide input parameters to the SM_RemoveTarget WMI method.</p>


## -syntax

````
typedef struct _SM_RemoveTarget_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DiscoveredPortWWN[8];
  UCHAR DomainPortWWN[8];
  ULONG AllTargets;
} SM_RemoveTarget_IN, *PSM_RemoveTarget_IN;
````


## -struct-fields
<dl>

### -field <b>HbaPortWWN</b>

<dd>
<p>A worldwide name (WWN) that indicates the local port that should be removed from the list of ports whose events are reported to the WMI client.</p>
</dd>

### -field <b>DiscoveredPortWWN</b>

<dd>
<p>A worldwide name (WWN) that indicates the port that was discovered remotely. Remove this port from the list of ports whose events are reported to the WMI client.</p>
</dd>

### -field <b>DomainPortWWN</b>

<dd>
<p>A worldwide name (WWN) that specifies the SAS domain worldwide name of the local port.</p>
</dd>

### -field <b>AllTargets</b>

<dd>
<p>The scope of the target events that stop reporting. If this member is zero, the WMI provider client stops reporting events that are associated with the port that is indicated by DiscoveredPortWWN. If this member is nonzero, the WMI provider stops reporting events that are associated with any target.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_RemoveTarget_IN structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_EventControl WMI class.</p>

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