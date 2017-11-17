---
UID: NS.ntifs._SYSTEM_PROCESS_TRUST_LABEL_ACE
title: SYSTEM_PROCESS_TRUST_LABEL_ACE
author: windows-driver-content
description: Reserved.
old-location: ifsk\system_process_trust_label_ace.htm
ms.assetid: DF334754-8027-418D-B329-877492896B82
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SYSTEM_PROCESS_TRUST_LABEL_ACE
req.alt-loc: Ntifs.h
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
ms.keywords: SYSTEM_PROCESS_TRUST_LABEL_ACE, SYSTEM_PROCESS_TRUST_LABEL_ACE, *PSYSTEM_PROCESS_TRUST_LABEL_ACE
req.iface: 
---

# SYSTEM_PROCESS_TRUST_LABEL_ACE structure



## -description
<p>Reserved.</p>


## -syntax

````
struct SYSTEM_PROCESS_TRUST_LABEL_ACE {
  ACE_HEADER  Header;
  ACCESS_MASK Mask;
  ULONG       SidStart;
};
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd></dd>

### -field <b>Mask</b>

<dd></dd>

### -field <b>SidStart</b>

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
<dt>Ntifs.h</dt>
</dl>
</td>
</tr>
</table>