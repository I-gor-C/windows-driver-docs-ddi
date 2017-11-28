---
UID: NF.wdm.IoGetNextIrpStackLocation
title: IoGetNextIrpStackLocation
author: windows-driver-content
description: The IoGetNextIrpStackLocation routine gives a higher level driver access to the next-lower driver's I/O stack location in an IRP so the caller can set it up for the lower driver.
old-location: kernel\iogetnextirpstacklocation.htm
old-project: kernel
ms.assetid: 44d38686-7a66-4e27-9dc7-9b3b4dbdffd6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoGetNextIrpStackLocation
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
req.alt-api: IoGetNextIrpStackLocation
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

# IoGetNextIrpStackLocation function



## -description
<p>The <b>IoGetNextIrpStackLocation</b> routine gives a higher level driver access to the next-lower driver's I/O stack location in an IRP so the caller can set it up for the lower driver.</p>


## -syntax

````
PIO_STACK_LOCATION IoGetNextIrpStackLocation(
  _In_ PIRP Irp
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>A pointer to the IRP. </p>
</dd>
</dl>

## -returns
<p><b>IoGetNextIrpStackLocation</b> returns a pointer to the next-lower-level driver's <a href="https://msdn.microsoft.com/62c8ee00-c7cb-4aa1-90ab-b8bedbd818ee">I/O stack location</a> in the given IRP.</p>

## -remarks
<p>Each driver that passes IRPs on to lower drivers must set up the stack location for the next lower driver. A driver calls <b>IoGetNextIrpStackLocation</b> to get a pointer to the next-lower driver's I/O stack location.</p>

<p>If a driver is passing the same parameters that it received to the next-lower driver, it should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548387">IoCopyCurrentIrpStackLocationToNext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a> instead of getting a pointer to the next-lower stack location and copying the parameters manually.</p>

<p>The return value is a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551821">I/O Stack Locations</a>.</p>

<p>Each driver that passes IRPs on to lower drivers must set up the stack location for the next lower driver. A driver calls <b>IoGetNextIrpStackLocation</b> to get a pointer to the next-lower driver's I/O stack location.</p>

<p>If a driver is passing the same parameters that it received to the next-lower driver, it should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548387">IoCopyCurrentIrpStackLocationToNext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a> instead of getting a pointer to the next-lower stack location and copying the parameters manually.</p>

<p>The return value is a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551821">I/O Stack Locations</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549174">IoGetCurrentIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548387">IoCopyCurrentIrpStackLocationToNext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550321">IoSetNextIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetNextIrpStackLocation routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
