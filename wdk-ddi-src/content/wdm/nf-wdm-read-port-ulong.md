---
UID: NF.wdm.READ_PORT_ULONG
title: READ_PORT_ULONG
author: windows-driver-content
description: The READ_PORT_ULONG routine reads a ULONG value from the specified port address.
old-location: kernel\read_port_ulong.htm
old-project: kernel
ms.assetid: 8a2f4429-b805-4a36-afdf-8b9c9a886951
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: READ_PORT_ULONG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: READ_PORT_ULONG
req.alt-loc: Hal.lib,Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: 
req.irql: Any level (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# READ_PORT_ULONG function



## -description
<p>The <b>READ_PORT_ULONG</b> routine reads a ULONG value from the specified port address.</p>


## -syntax

````
ULONG READ_PORT_ULONG(
  _In_ PULONG Port
);
````


## -parameters
<dl>

### -param <i>Port</i> [in]

<dd>
<p>Specifies the port address, which must be a mapped range in I/O space. </p>
</dd>
</dl>

## -returns
<p><b>READ_PORT_ULONG</b> returns the ULONG value that is read from the specified port address.</p>

## -remarks
<p>Callers of <b>READ_PORT_ULONG</b> can be running at any IRQL, assuming the <i>Port</i> is resident, mapped device memory.</p>

<p>Callers of <b>READ_PORT_ULONG</b> can be running at any IRQL, assuming the <i>Port</i> is resident, mapped device memory.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>