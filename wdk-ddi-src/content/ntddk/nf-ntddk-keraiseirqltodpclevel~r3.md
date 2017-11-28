---
UID: NF.ntddk.KeRaiseIrqlToDpcLevel~r3
title: KeRaiseIrqlToDpcLevel
author: windows-driver-content
description: The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor.
old-location: kernel\keraiseirqltodpclevel.htm
old-project: kernel
ms.assetid: ac82e003-ec05-4b8b-a4fb-64498fb17f9b
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeRaiseIrqlToDpcLevel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRaiseIrqlToDpcLevel
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
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
---

# KeRaiseIrqlToDpcLevel function



## -description
<p>The <b>KeRaiseIrqlToDpcLevel</b> routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor.</p>


## -syntax

````
KIRQL KeRaiseIrqlToDpcLevel(void);
````


## -parameters


## -returns
<p><b>KeRaiseIrqlToDpcLevel</b> returns the IRQL at which the call occurred.</p>

<p><b>KeRaiseIrqlToDpcLevel</b> returns the IRQL at which the call occurred.</p>

<p><b>KeRaiseIrqlToDpcLevel</b> returns the IRQL at which the call occurred.</p>

## -remarks
<p>Any caller of <b>KeRaiseIrqlToDpcLevel</b> should save the returned IRQL value. Every such caller must restore the original IRQL as quickly as possible by passing this returned IRQL in a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552968">KeLowerIrql</a>.</p>

<p>Callers of <b>KeRaiseIrqlToDpcLevel</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, a call to this routine causes a bug check.</p>

<p>Any caller of <b>KeRaiseIrqlToDpcLevel</b> should save the returned IRQL value. Every such caller must restore the original IRQL as quickly as possible by passing this returned IRQL in a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552968">KeLowerIrql</a>.</p>

<p>Callers of <b>KeRaiseIrqlToDpcLevel</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, a call to this routine causes a bug check.</p>

<p>Any caller of <b>KeRaiseIrqlToDpcLevel</b> should save the returned IRQL value. Every such caller must restore the original IRQL as quickly as possible by passing this returned IRQL in a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552968">KeLowerIrql</a>.</p>

<p>Callers of <b>KeRaiseIrqlToDpcLevel</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, a call to this routine causes a bug check.</p>

<p>Any caller of <b>KeRaiseIrqlToDpcLevel</b> should save the returned IRQL value. Every such caller must restore the original IRQL as quickly as possible by passing this returned IRQL in a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552968">KeLowerIrql</a>.</p>

<p>Callers of <b>KeRaiseIrqlToDpcLevel</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, a call to this routine causes a bug check.</p>

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552054">KeGetCurrentIrql</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRaiseIrqlToDpcLevel routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
