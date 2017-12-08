---
UID: NS.hbapiwmi._MS_SMHBA_PORTLUN
title: MS_SMHBA_PORTLUN
author: windows-driver-content
description: The MS_SMHBA_PORTLUN structure reports target LUN information that is associated with a port.
old-location: storage\ms_smhba_portlun.htm
old-project: storage
ms.assetid: cf62685f-7b4d-4671-a755-d59a593bf5d6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MS_SMHBA_PORTLUN, MS_SMHBA_PORTLUN, *PMS_SMHBA_PORTLUN
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
req.alt-api: MS_SMHBA_PORTLUN
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

# MS_SMHBA_PORTLUN structure



## -description
<p>The MS_SMHBA_PORTLUN structure reports target LUN information that is associated with a port.</p>


## -syntax

````
typedef struct _MS_SMHBA_PORTLUN {
  UCHAR     PortWWN[8];
  UCHAR     domainPortWWN[8];
  ULONGLONG TargetLun;
} MS_SMHBA_PORTLUN, *PMS_SMHBA_PORTLUN;
````


## -struct-fields
<dl>

### -field PortWWN

<dd>
<p>The worldwide name of the local port whose events the WMI client will receive.</p>
</dd>

### -field domainPortWWN

<dd>
<p>A worldwide name that specifies the SAS domain worldwide name of the local port.</p>
</dd>

### -field TargetLun

<dd>
<p>The target LUN number.</p>
</dd>
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
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>