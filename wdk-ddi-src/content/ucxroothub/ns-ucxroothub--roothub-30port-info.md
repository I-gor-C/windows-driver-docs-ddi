---
UID: NS.ucxroothub._ROOTHUB_30PORT_INFO
title: ROOTHUB_30PORT_INFO
author: windows-driver-content
description: Provides information about a USB 3.0 root hub port. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_30PORT_INFO callback function.
old-location: buses\_roothub_30port_info.htm
old-project: usbref
ms.assetid: 5C39C0EB-AC7F-44E5-95EB-9F067DBE0801
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ROOTHUB_30PORT_INFO, ROOTHUB_30PORT_INFO, *PROOTHUB_30PORT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ROOTHUB_30PORT_INFO
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ROOTHUB_30PORT_INFO structure



## -description
<p>Provides information about a USB 3.0 root hub port. This structure is passed by UCX in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187835">EVT_UCX_ROOTHUB_GET_30PORT_INFO</a> callback function.</p>


## -syntax

````
typedef struct _ROOTHUB_30PORT_INFO {
  USHORT   PortNumber;
  UCHAR    MinorRevision;
  UCHAR    HubDepth;
  TRISTATE Removable;
  TRISTATE DebugCapable;
} ROOTHUB_30PORT_INFO, *P_ROOTHUB_30PORT_INFO;
````


## -struct-fields
<dl>

### -field <b>PortNumber</b>

<dd>
<p>The USB 3.0 port number connected to the root hub.</p>
</dd>

### -field <b>MinorRevision</b>

<dd>
<p>Revision number.</p>
</dd>

### -field <b>HubDepth</b>

<dd>
<p>The hub depth limit.</p>
</dd>

### -field <b>Removable</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187907">TRISTATE</a> value that indicates if the port is removable. </p>
</dd>

### -field <b>DebugCapable</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187907">TRISTATE</a> value that indicates if the port is debug capable. </p>
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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>