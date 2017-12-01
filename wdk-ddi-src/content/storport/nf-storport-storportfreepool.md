---
UID: NF.storport.StorPortFreePool
title: StorPortFreePool
author: windows-driver-content
description: The StorPortFreePool routine frees a block of memory that was previously allocated by a call to the StorPortAllocatePool routine.
old-location: storage\storportfreepool.htm
old-project: storage
ms.assetid: e5886fa3-dc37-4764-9304-3609a4ced0ad
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortFreePool
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
req.alt-api: StorPortFreePool
req.alt-loc: storport.h
req.ddi-compliance: StorPortAllocatePool2, StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortFreePool function



## -description
<p>The <b>StorPortFreePool</b> routine frees a block of memory that was previously allocated by a call to the <a href="..\storport\nf-storport-storportallocatepool.md">StorPortAllocatePool</a> routine.</p>


## -syntax

````
ULONG StorPortFreePool(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID BufferPointer
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>BufferPointer</i> [in]

<dd>
<p>A pointer to the block of memory to free. This must be a pointer that was returned by a previous call to the <a href="..\storport\nf-storport-storportallocatepool.md">StorPortAllocatePool</a> routine.</p>
</dd>
</dl>

## -returns
<p>StorPortFreePool returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the routine freed the memory block successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer to the memory block to be freed is <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The call was made at an invalid IRQL.</p>

<p> </p>

## -remarks


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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_storportallocatepool2">StorPortAllocatePool2</a>, <a href="devtest.storport_storportirql">StorPortIrql</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\nf-storport-storportallocatepool.md">StorPortAllocatePool</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortFreePool routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
