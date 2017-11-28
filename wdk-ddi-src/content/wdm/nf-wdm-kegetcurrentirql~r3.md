---
UID: NF.wdm.KeGetCurrentIrql~r3
title: KeGetCurrentIrql
author: windows-driver-content
description: The KeGetCurrentIrql routine returns the current IRQL.
old-location: kernel\kegetcurrentirql.htm
old-project: kernel
ms.assetid: 63c33017-d827-4a8f-bb6f-fd13a2528e0c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeGetCurrentIrql
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
req.alt-api: KeGetCurrentIrql
req.alt-loc: Hal.lib,Hal.dll
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# KeGetCurrentIrql function



## -description
<p>The <b>KeGetCurrentIrql</b> routine returns the current IRQL.</p>


## -syntax

````
 KIRQL KeGetCurrentIrql(void);
````


## -parameters


## -returns
<p><b>KeGetCurrentIrql</b> returns the current IRQL.</p>

<p><b>KeGetCurrentIrql</b> returns the current IRQL.</p>

<p><b>KeGetCurrentIrql</b> returns the current IRQL.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551921">KeAcquireSpinLockAtDpcLevel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552968">KeLowerIrql</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553079">KeRaiseIrql</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeGetCurrentIrql routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
