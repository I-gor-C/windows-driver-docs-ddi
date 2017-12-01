---
UID: NF.wdm.KeStallExecutionProcessor
title: KeStallExecutionProcessor
author: windows-driver-content
description: The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval.
old-location: kernel\kestallexecutionprocessor.htm
old-project: kernel
ms.assetid: 9f03af94-0a29-42f4-84f1-09d8d1c97dd6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeStallExecutionProcessor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeStallExecutionProcessor
req.alt-loc: Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: Hal.dll
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# KeStallExecutionProcessor function



## -description
<p>The <b>KeStallExecutionProcessor</b> routine stalls the caller on the current processor for a specified time interval.</p>


## -syntax

````
 VOID KeStallExecutionProcessor(
  _In_ ULONG MicroSeconds
);
````


## -parameters
<dl>

### -param <i>MicroSeconds</i> [in]

<dd>
<p>Specifies the number of microseconds to stall.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>KeStallExecutionProcessor</b> is a processor-dependent routine that busy-waits for at least the specified number of microseconds, but not significantly longer.</p>

<p>This routine is for use by device drivers and other software that must wait for an interval of less than a clock tick but more than for a few instructions. If you use this routine you must minimize the stall interval, typically to less than 50 microseconds. If a driver must wait for a longer interval, you should use a different <a href="https://msdn.microsoft.com/dfee2240-44df-43bc-8804-271203480664">synchronization technique</a>.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hal.dll</dt>
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
<a href="..\wdm\nf-wdm-kedelayexecutionthread.md">KeDelayExecutionThread</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitformultipleobjects.md">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeStallExecutionProcessor routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
