---
UID: NF.wdm.InterlockedIncrement~r1
title: InterlockedIncrement
author: windows-driver-content
description: The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation.
old-location: kernel\interlockedincrement.htm
old-project: kernel
ms.assetid: e8f4c3c9-c5b7-4fc1-9be3-0254c6cbd6f3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: InterlockedIncrement
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
req.alt-api: InterlockedIncrement
req.alt-loc: OneCoreUAP.lib,OneCoreUAP.dll,API-MS-Win-Core-Interlocked-l1-1-0.dll,API-MS-Win-Core-Interlocked-l1-2-0.dll,KernelBase.dll,MinKernelBase.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: OneCoreUAP.lib on Windows 10
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# InterlockedIncrement function



## -description
<p>The <b>InterlockedIncrement</b> routine increments a caller-supplied variable as an atomic operation. </p>


## -syntax

````
LONG InterlockedIncrement(
  _Inout_ LONG volatile *Addend
);
````


## -parameters
<dl>

### -param <i>Addend</i> [in, out]

<dd>
<p>A pointer to a variable of type LONG. </p>
</dd>
</dl>

## -returns
<p><b>InterlockedIncrement</b> returns the incremented value.</p>

## -remarks
<p><b>InterlockedIncrement</b> should be used instead of <b>ExInterlockedIncrementLong</b> because it is both more efficient and faster. </p>

<p><b>InterlockedIncrement </b>is implemented inline by the compiler when appropriate and possible. It does not require a spin lock and can therefore be safely used on pageable data.</p>

<p><b>InterlockedIncrement</b> is atomic only with respect to other <b>Interlocked<i>Xxx</i></b> calls. </p>

<p>Interlocked operations cannot be used on non-cached memory. </p>

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
<dt>OneCoreUAP.lib on Windows 10</dt>
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
<a href="..\wdm\nf-wdm-interlockeddecrement.md">InterlockedDecrement</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-interlockedexchange.md">InterlockedExchange</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinterlockedaddlargeinteger.md">ExInterlockedAddLargeInteger</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinterlockedaddulong.md">ExInterlockedAddUlong</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20InterlockedIncrement routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
