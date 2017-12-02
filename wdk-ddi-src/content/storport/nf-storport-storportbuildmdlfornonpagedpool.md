---
UID: NF.storport.StorPortBuildMdlForNonPagedPool
title: StorPortBuildMdlForNonPagedPool
author: windows-driver-content
description: The StorPortBuildMdlForNonPagedPool routine updates the MDL to describe the associated non-paged memory.
old-location: storage\storportbuildmdlfornonpagedpool.htm
old-project: storage
ms.assetid: f22dbf1e-4b40-4294-bca5-3011f0a97644
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortBuildMdlForNonPagedPool
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
req.alt-api: StorPortBuildMdlForNonPagedPool
req.alt-loc: storport.h
req.ddi-compliance: StorPortIrql
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

# StorPortBuildMdlForNonPagedPool function



## -description
<p>The <b>StorPortBuildMdlForNonPagedPool</b> routine updates the MDL to describe the associated non-paged memory.</p>


## -syntax

````
ULONG StorPortBuildMdlForNonPagedPool(
  _In_    PVOID HwDeviceExtension,
  _Inout_ PVOID Mdl
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param Mdl [in, out]

<dd>
<p>A pointer to the MDL that specifies the memory buffer.</p>
</dd>
</dl>

## -returns
<p>StorPortBuildMdlForNonPagedPool returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the MDL was updated successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer to the MDL is <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The call was made at an invalid IRQL. </p>

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
<a href="devtest.storport_storportirql">StorPortIrql</a>
</td>
</tr>
</table>