---
UID: NF.storport.StorPortInitializeWorker
title: StorPortInitializeWorker
author: windows-driver-content
description: Creates a new Storport work item that runs in a system worker thread.
old-location: storage\storportinitializeworker.htm
old-project: storage
ms.assetid: 4472A092-B2F4-4220-9685-6BE4FF0A83DB
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortInitializeWorker
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
req.alt-api: StorPortInitializeWorker
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

# StorPortInitializeWorker function



## -description
<p>Creates a new Storport work item that runs in a system worker thread.</p>


## -syntax

````
ULONG StorPortInitializeWorker(
  _In_  PVOID HwDeviceExtension,
  _Out_ PVOID *Worker
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>Worker</i> [out]

<dd>
<p>A pointer to an opaque buffer that holds context information for the work item.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortInitializeWorker</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>Current IRQL &gt; DISPATCH_LEVEL.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either <i>HwDeviceExtension</i> or <i>Worker</i> is NULL.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p> Insufficient resources are available to initialize the work item context.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The work item was successfully initialized.</p>

<p> </p>

## -remarks
<p>The work item context returned in the <i>Worker</i> parameter by <b>StorPortInitializeWorker</b> is used in future calls to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451509">StorPortQueueWorkItem</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh451478">StorPortFreeWorker</a>.</p>

<p>If the miniport uses the work item during IO processing, we recommended that <b>StorPortInitializeWorker</b> be called during the miniport's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> function to ensure that resources are available when needed.</p>

<p>The work item context returned in the <i>Worker</i> parameter by <b>StorPortInitializeWorker</b> is used in future calls to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451509">StorPortQueueWorkItem</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh451478">StorPortFreeWorker</a>.</p>

<p>If the miniport uses the work item during IO processing, we recommended that <b>StorPortInitializeWorker</b> be called during the miniport's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> function to ensure that resources are available when needed.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451478">StorPortFreeWorker</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451509">StorPortQueueWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortInitializeWorker routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
