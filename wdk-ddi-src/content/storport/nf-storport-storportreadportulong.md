---
UID: NF.storport.StorPortReadPortUlong
title: StorPortReadPortUlong
author: windows-driver-content
description: The StorPortReadPortUlong routine reads a value from a specified port address.
old-location: storage\storportreadportulong.htm
old-project: storage
ms.assetid: b04ef64a-cf1f-4de5-acb3-e57687f64719
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortReadPortUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortReadPortUlong
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortReadPortUlong function



## -description
<p>The <b>StorPortReadPortUlong</b> routine reads a value from a specified port address. </p>


## -syntax

````
STORPORT_API ULONG StorPortReadPortUlong(
  _In_ PVOID  HwDeviceExtension,
  _In_ PULONG Port
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the hardware device extension.</p>
</dd>

### -param <i>Port</i> [in]

<dd>
<p>Pointer to the address from which to read. </p>
</dd>
</dl>

## -returns
<p><b>StorPortReadPortUlong</b> returns a data item of length <b>sizeof</b>(ULONG).</p>

## -remarks
<p>For more information, see the <a href="..\srb\nf-srb-scsiportreadportulong.md">ScsiPortReadPortUlong</a> routine. For a buffered version of this routine see <a href="..\storport\nf-storport-storportreadportbufferulong.md">StorPortReadPortBufferUlong</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\nf-srb-scsiportreadportbufferulong.md">ScsiPortReadPortBufferUlong</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportreadportulong.md">StorPortReadPortUlong</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortReadPortUlong routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
