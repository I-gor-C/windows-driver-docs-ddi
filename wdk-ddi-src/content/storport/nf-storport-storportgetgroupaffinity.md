---
UID: NF.storport.StorPortGetGroupAffinity
title: StorPortGetGroupAffinity
author: windows-driver-content
description: The StorPortGetGroupAffinity routine constructs a mask of the active processors in a requested group.
old-location: storage\storportgetgroupaffinity.htm
old-project: storage
ms.assetid: eec0c985-fb59-4190-afb8-5eb62ac1edea
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetGroupAffinity
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
req.alt-api: StorPortGetGroupAffinity
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

# StorPortGetGroupAffinity function



## -description
<p>The <b>StorPortGetGroupAffinity</b> routine constructs a mask of the active processors in a requested group.</p>


## -syntax

````
ULONG StorPortGetGroupAffinity(
  _In_  PVOID      HwDeviceExtension,
  _In_  USHORT     GroupNumber,
  _Out_ PKAFFINITY GroupAffinityMask
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>GroupNumber</i> [in]

<dd>
<p>The group from which to return the processor mask.</p>
</dd>

### -param <i>GroupAffinityMask</i> [out]

<dd>
<p>A pointer to a variable that holds the affinity mask of the given group.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortGetGroupAffinity</b> routine returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The operation was successful.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The operation fails with this return value if one or more of the parameters are invalid, for example, if <i>GroupAffinityMask</i> is set to <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The operation fails with this return value if one or more of the parameters are invalid, for example, if <i>GroupNumber</i> is set to a value greater than the active group count.</p>

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