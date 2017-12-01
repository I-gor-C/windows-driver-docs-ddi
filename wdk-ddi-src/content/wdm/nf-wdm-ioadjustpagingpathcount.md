---
UID: NF.wdm.IoAdjustPagingPathCount
title: IoAdjustPagingPathCount
author: windows-driver-content
description: The IoAdjustPagingPathCount routine increments or decrements a caller-supplied page-file counter as an atomic operation.
old-location: kernel\ioadjustpagingpathcount.htm
old-project: kernel
ms.assetid: be353d10-1d8a-4fea-a415-e1729184e451
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoAdjustPagingPathCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoAdjustPagingPathCount
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# IoAdjustPagingPathCount function



## -description
<p>The <b>IoAdjustPagingPathCount</b> routine increments or decrements a caller-supplied page-file counter as an atomic operation.</p>


## -syntax

````
VOID IoAdjustPagingPathCount(
  _In_ PLONG   Count,
  _In_ BOOLEAN Increment
);
````


## -parameters
<dl>

### -param <i>Count</i> [in]

<dd>
<p>Pointer to a caller-supplied variable that contains a counter. A driver typically stores a page-file counter in the device extension for the device.</p>
</dd>

### -param <i>Increment</i> [in]

<dd>
<p>Specifies whether the counter is to be incremented or decremented. A value of <b>TRUE</b> specifies an increment operation.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This routine is useful for maintaining a count of paging files on a device. The operating system notifies a driver that a paging file has been created on, or removed from, one of the driver's devices by sending an IRP. The IRP has the major code <a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a> and the minor code <a href="https://msdn.microsoft.com/library/windows/hardware/ff550841">IRP_MN_DEVICE_USAGE_NOTIFICATION</a>.</p>

<p>This routine can be used for other counters, such as counters for hibernation files or crash-dump files.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550841">IRP_MN_DEVICE_USAGE_NOTIFICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoAdjustPagingPathCount routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
