---
UID: NF.wdfhwaccess.WDF_WRITE_REGISTER_BUFFER_ULONG
title: WDF_WRITE_REGISTER_BUFFER_ULONG
author: windows-driver-content
description: The WDF_WRITE_REGISTER_BUFFER_ULONG function writes a number of ULONG values from a buffer to the specified register.
old-location: wdf\wdf_write_register_buffer_ulong.htm
ms.assetid: D52888A2-4CC1-4C5A-890E-5585424339E0
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfhwaccess.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WDF_WRITE_REGISTER_BUFFER_ULONG
req.alt-loc: Wdfhwaccess.h
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
ms.keywords: WDF_WRITE_REGISTER_BUFFER_ULONG
req.iface: 
req.product: Windows 10 or later.
---

# WDF_WRITE_REGISTER_BUFFER_ULONG function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WDF_WRITE_REGISTER_BUFFER_ULONG</b> function writes a number of ULONG values from a buffer to the specified register.</p>


## -syntax

````
void WDF_WRITE_REGISTER_BUFFER_ULONG(
  _In_ WDFDEVICE Device,
  _In_ PULONG    Register,
  _In_ PULONG    Buffer,
  _In_ ULONG     Count 
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Register</i> [in]

<dd>
<p>A pointer to the register, which must be a mapped range in memory space.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to a buffer from which an array of ULONG values is to be written.</p>
</dd>

### -param <i>Count </i> [in]

<dd>
<p>Specifies the number of ULONG values to write to the register.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The size of the buffer must be large enough to contain at least the specified number of bytes.</p>

<p>The size of the buffer must be large enough to contain at least the specified number of bytes.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfhwaccess.h</dt>
</dl>
</td>
</tr>
</table>