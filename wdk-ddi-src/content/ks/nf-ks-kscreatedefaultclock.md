---
UID: NF.ks.KsCreateDefaultClock
title: KsCreateDefaultClock
author: windows-driver-content
description: Given an IRP_MJ_CREATE request, the KsCreateDefaultClock function creates a default clock that uses the system clock as a time base and associates the IoGetCurrentIrpStackLocation(Irp)-&gt;FileObject with the clock using an internal dispatch table (KSDISPATCH_TABLE). Does not complete the IRP or set the status in the IRP.The KsCreateDefaultClock function can only be called at PASSIVE_LEVEL.
old-location: stream\kscreatedefaultclock.htm
ms.assetid: 38ac85bc-9ace-4e70-a886-92e18afb32db
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCreateDefaultClock
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
ms.keywords: KsCreateDefaultClock
req.iface: 
---

# KsCreateDefaultClock function



## -description
<p>Given an IRP_MJ_CREATE request, the <b>KsCreateDefaultClock</b> function creates a default clock that uses the system clock as a time base and associates the IoGetCurrentIrpStackLocation(Irp)-&gt;FileObject with the clock using an internal dispatch table (KSDISPATCH_TABLE).  Does not complete the IRP or set the status in the IRP.</p>
<p>The <b>KsCreateDefaultClock</b> function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
NTSTATUS KsCreateDefaultClock(
  _In_ PIRP            Irp,
  _In_ PKSDEFAULTCLOCK DefaultClock
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP with the clock-create request being handled.</p>
</dd>

### -param <i>DefaultClock</i> [in]

<dd>
<p>Specifies an initialize default clock structure that is shared among any instance of the default clock for the parent.</p>
</dd>
</dl>

## -returns
<p>The <b>KsCreateDefaultClock</b> function returns STATUS_SUCCESS if successful, or an error if unsuccessful.</p>

## -remarks
<p>The clock can be created after using <b>KsAllocateDefaultClock</b> to create and initialize the internal structures for a default clock instance. After initialization, many file objects can be created against the same underlying default clock instance.</p>

<p>The clock can be created after using <b>KsAllocateDefaultClock</b> to create and initialize the internal structures for a default clock instance. After initialization, many file objects can be created against the same underlying default clock instance.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560952">KsAllocateDefaultClock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsCreateDefaultClock function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
