---
UID: NF.strmini.StreamClassReadWriteConfig
title: StreamClassReadWriteConfig
author: windows-driver-content
description: The StreamClassReadWriteConfig routine reads or writes configuration data for the minidriver's parent bus driver.
old-location: stream\streamclassreadwriteconfig.htm
old-project: stream
ms.assetid: ae8c1478-b429-4af1-a36d-96145696a990
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: StreamClassReadWriteConfig
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassReadWriteConfig
req.alt-loc: Stream.lib,Stream.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Stream.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassReadWriteConfig function



## -description
<p>The <b>StreamClassReadWriteConfig</b> routine reads or writes configuration data for the minidriver's parent bus driver.</p>


## -syntax

````
BOOLEAN StreamClassReadWriteConfig(
  _In_    PVOID   HwDeviceExtension,
  _In_    BOOLEAN Read,
  _Inout_ PVOID   Buffer,
  _In_    ULONG   Offset,
  _In_    ULONG   Length
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the minidriver's device extension. The minidriver specifies the size of this buffer in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>. The class driver then passes pointers to the buffer in the <b>HwDeviceExtension</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559706">HW_TIME_CONTEXT</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -param <i>Read</i> [in]

<dd>
<p>Specifies whether to read or write the configuration information. A value of <b>TRUE</b> indicates that a read is requested. A value of <b>FALSE</b> indicates that a write should be performed.</p>
</dd>

### -param <i>Buffer</i> [in, out]

<dd>
<p>Points to the buffer to use to read/write the configuration information.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the offset within the configuration information to begin the read/write operation.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the length of the data to read or write.</p>
</dd>
</dl>

## -returns
<p>Returns <b>TRUE</b> on success, <b>FALSE</b> on failure.</p>

## -remarks
<p>This routine reads or writes configuration information for the minidriver's parent bus driver. For example, for a PCI device, <b>StreamClassReadWriteConfig</b> reads or writes PCI configuration information.</p>

<p>This routine can only be called at PASSIVE_LEVEL.</p>

<p>This routine reads or writes configuration information for the minidriver's parent bus driver. For example, for a PCI device, <b>StreamClassReadWriteConfig</b> reads or writes PCI configuration information.</p>

<p>This routine can only be called at PASSIVE_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>