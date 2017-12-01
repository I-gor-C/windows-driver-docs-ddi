---
UID: NF.ntddk.PsAllocSiloContextSlot
title: PsAllocSiloContextSlot
author: windows-driver-content
description: This routine allocates a slot that can be used to insert, retrieve, and delete an object in all silos. .
old-location: kernel\psallocsilocontextslot.htm
old-project: kernel
ms.assetid: 835446D1-EB41-47BC-AA0F-54A9C029EFFE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsAllocSiloContextSlot
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsAllocSiloContextSlot
req.alt-loc: ntddk.h
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
req.iface: 
---

# PsAllocSiloContextSlot function



## -description
<p>This routine allocates a slot that can be used to insert, retrieve, and delete an object in all silos. </p>


## -syntax

````
NTSTATUS PsAllocSiloContextSlot(
  _In_  ULONG_PTR Reserved,
  _Out_ ULONG     *ReturnedContextSlot
);
````


## -parameters
<dl>

### -param <i>Reserved</i> [in]

<dd>
<p>This parameter is reserved for future use and <b>must be set to zero</b>. </p>
<div class="alert"><b>Warning</b>  Setting <i>Reserved</i> to a non-zero value causes the system to execute an <b>ASSERT</b> on a checked build.</div>
<div> </div>
</dd>

### -param <i>ReturnedContextSlot</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the newly allocated slot index. This parameter is required and it cannot be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES </b></dt>
</dl><p>There are no more slots available in the system. This is an error code.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p>

<p> </p>

## -remarks
<p>Use of this API is uncommon because all silo monitors are assigned a storage slot when calling the <a href="..\ntddk\nf-ntddk-psregistersilomonitor.md">PsRegisterSiloMonitor</a> routine.  That slot can be retrieved with the <a href="..\ntddk\nf-ntddk-psgetsilomonitorcontextslot.md">PsGetSiloMonitorContextSlot</a> routine and used by a driver for its context operations.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-psfreesilocontextslot.md">PsFreeSiloContextSlot</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsAllocSiloContextSlot routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
