---
UID: NS.ndis._PD_BUFFER_8021Q_INFO
title: PD_BUFFER_8021Q_INFO
author: windows-driver-content
description: This structure contains the IEEE 802.1Q information.
old-location: netvista\pd_buffer_8021q_info.htm
old-project: netvista
ms.assetid: B5B2051E-C62F-4E3D-9C52-DE46145A2C24
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PD_BUFFER_8021Q_INFO, PD_BUFFER_8021Q_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PD_BUFFER_8021Q_INFO
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# PD_BUFFER_8021Q_INFO structure



## -description
<p>This structure contains the IEEE 802.1Q information.</p>


## -syntax

````
typedef struct _PD_BUFFER_8021Q_INFO {
  UINT16 UserPriority  :3;
  UINT16 CanonicalFormatId  :1;
  UINT16 VlanId  :12;
} PD_BUFFER_8021Q_INFO, *PPD_BUFFER_8021Q_INFO;
````


## -struct-fields
<dl>

### -field <b>UserPriority</b>

<dd>
<p>The user priority.</p>
</dd>

### -field <b>CanonicalFormatId</b>

<dd>
<p>The canonical format ID.</p>
</dd>

### -field <b>VlanId</b>

<dd>
<p>The virtual LAN ID.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>