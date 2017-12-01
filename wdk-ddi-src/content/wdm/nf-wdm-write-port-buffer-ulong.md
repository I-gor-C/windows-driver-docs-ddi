---
UID: NF.wdm.WRITE_PORT_BUFFER_ULONG
title: WRITE_PORT_BUFFER_ULONG
author: windows-driver-content
description: The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address.
old-location: kernel\write_port_buffer_ulong.htm
old-project: kernel
ms.assetid: 6f786456-344a-4fc3-bc13-8d4253f4039a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WRITE_PORT_BUFFER_ULONG
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
req.alt-api: WRITE_PORT_BUFFER_ULONG
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

# WRITE_PORT_BUFFER_ULONG function



## -description
<p>The <b>WRITE_PORT_BUFFER_ULONG</b> routine writes a number of ULONG values from a buffer to the specified port address.</p>


## -syntax

````
 VOID WRITE_PORT_BUFFER_ULONG(
  _In_ PULONG Port,
  _In_ PULONG Buffer,
  _In_ ULONG  Count
);
````


## -parameters
<dl>

### -param <i>Port</i> [in]

<dd>
<p>Pointer to the port, which must be a mapped memory range in I/O space.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Pointer to a buffer from which an array of ULONG values is to be written.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of ULONG values to be written to the port. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The size of the buffer must be large enough to contain at least the specified number of ULONG values.</p>

<p>Callers of <b>WRITE_PORT_BUFFER_ULONG</b> can be running at any IRQL, assuming the <i>Buffer</i> is resident and the <i>Port</i> is resident, mapped device memory.</p>

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