---
UID: NF.ks.KsAcquireResetValue
title: KsAcquireResetValue
author: windows-driver-content
description: The KsAcquireResetValue function retrieves the current reset state from an IOCTL_KS_RESET_STATE IRP.
old-location: stream\ksacquireresetvalue.htm
old-project: stream
ms.assetid: 80a990e3-3637-4837-8800-42d5848e01cf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsAcquireResetValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsAcquireResetValue
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsAcquireResetValue function



## -description
<p>The <b>KsAcquireResetValue </b>function retrieves the current reset state from an IOCTL_KS_RESET_STATE IRP.</p>


## -syntax

````
NTSTATUS KsAcquireResetValue(
  _In_  PIRP    Irp,
  _Out_ KSRESET *ResetValue
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Points to the IRP from which to retrieve the reset state.</p>
</dd>

### -param <i>ResetValue</i> [out]

<dd>
<p>Points to a caller-allocated buffer, that on successful completion contains the reset value (KSRESET_BEGIN, KSRESET_END) associated with the IRP.</p>
</dd>
</dl>

## -returns
<p>The <b>KsAcquireResetValue </b>function returns STATUS_SUCCESS if the reset value was obtained.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>