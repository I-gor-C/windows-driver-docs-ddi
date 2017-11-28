---
UID: NF.storport.StorPortGetActiveGroupCount
title: StorPortGetActiveGroupCount
author: windows-driver-content
description: The StorPortGetActiveGroupCount routine returns the number of processor groups that are present in the system.
old-location: storage\storportgetactivegroupcount.htm
old-project: storage
ms.assetid: 640dd836-a5f9-4a88-b2a3-038a66a50868
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetActiveGroupCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetActiveGroupCount
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

# StorPortGetActiveGroupCount function



## -description
<p>The <b>StorPortGetActiveGroupCount</b> routine returns the number of processor groups that are present in the system.</p>


## -syntax

````
ULONG StorPortGetActiveGroupCount(
  _In_  PVOID   HwDeviceExtension,
  _Out_ PUSHORT NumberGroups
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>NumberGroups</i> [out]

<dd>
<p>A pointer to a variable that holds the number of groups.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortGetActiveGroupCount</b> routine returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The operation was successful.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454266">StorPortIrql</a>
</td>
</tr>
</table>