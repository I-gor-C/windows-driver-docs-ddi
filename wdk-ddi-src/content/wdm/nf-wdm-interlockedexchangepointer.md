---
UID: NF.wdm.InterlockedExchangePointer
title: InterlockedExchangePointer
author: windows-driver-content
description: The InterlockedExchangePointer routine performs an atomic operation that sets a pointer to a new value.
old-location: kernel\interlockedexchangepointer.htm
old-project: kernel
ms.assetid: 8c39a62d-0c05-4d26-b104-90c436e821cb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: InterlockedExchangePointer
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
req.alt-api: InterlockedExchangePointer
req.alt-loc: wdm.h
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

# InterlockedExchangePointer function



## -description
<p>The <b>InterlockedExchangePointer</b> routine performs an atomic operation that sets a pointer to a new value.</p>


## -syntax

````
PVOID InterlockedExchangePointer(
  _Inout_  PVOID volatile *Target,
  _In_opt_ PVOID          Value
);
````


## -parameters
<dl>

### -param <i>Target</i> [in, out]

<dd>
<p>A pointer to a PVOID value. The routine sets (*<i>Target</i>) to <i>Value</i>.</p>
</dd>

### -param <i>Value</i> [in, optional]

<dd>
<p>Specifies the PVOID value to set (*<i>Target</i>) to.</p>
</dd>
</dl>

## -returns
<p><b>InterlockedExchangePointer</b> returns the original value of the pointer at *<i>Target</i> (that is, the value of this pointer at entry to the routine).</p>

## -remarks
<p><b>InterlockedExchangePointer</b> provides a fast, atomic way to synchronize updating a pointer variable that is shared by multiple threads.</p>

<p><b>InterlockedExchangePointer</b> is designed for speed and, typically, is implemented inline by a compiler. <b>InterlockedExchangePointer</b> is atomic only with respect to other <b>Interlocked<i>Xxx</i></b> calls. It does not use a spin lock and can be safely used on pageable data. </p>

<p>The <i>Target</i> parameter should be aligned on either a 32-bit or 64-bit boundary, depending on the system type, for better performance.</p>

<p>A call to <b>InterlockedExchangePointer</b> is atomic only with respect to other <b>Interlocked<i>Xxx</i></b> calls.</p>

<p>Interlocked operations cannot be used on non-cached memory. </p>

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
<a href="..\wdm\nf-wdm-interlockedcompareexchange.md">InterlockedCompareExchange</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-interlockedcompareexchangepointer.md">InterlockedCompareExchangePointer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-interlockedexchange.md">InterlockedExchange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20InterlockedExchangePointer routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
