---
UID: NF.storport.StorPortFreeTimer
title: StorPortFreeTimer
author: windows-driver-content
description: Frees a Storport timer context object previously created by the StorPortInitializeTimer routine.
old-location: storage\storportfreetimer.htm
old-project: storage
ms.assetid: AF6B1693-6242-4F09-8226-472E75B809F3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortFreeTimer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortFreeTimer
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortFreeTimer function



## -description
<p>Frees a Storport timer context object previously created by the <a href="..\storport\nf-storport-storportinitializetimer.md">StorPortInitializeTimer</a> routine.</p>


## -syntax

````
ULONG StorPortFreeTimer(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID TimerHandle
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>TimerHandle</i> [in]

<dd>
<p>A pointer to an opaque buffer for the timer context returned by <a href="..\storport\nf-storport-storportinitializetimer.md">StorPortInitializeTimer</a>.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortFreeTimer</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>Current IRQL &gt; DISPATCH_LEVEL.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either <i>HwDeviceExtension</i> or <i>TimerHandle</i> is NULL.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient resources are available to free the timer.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The timer was successfully freed.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The timer is already free.</p>

<p> </p>

## -remarks
<p>Miniports should call <b>StorPortFreeTimer</b> whenever a work item is no longer needed or when the miniport receives a PnP SRB notification  that the adapter is removed.</p>

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
<p>Available in Windows 8 and later versions of Windows.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportinitializetimer.md">StorPortInitializeTimer</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportrequesttimer.md">StorPortRequestTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortFreeTimer routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
