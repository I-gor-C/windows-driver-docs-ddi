---
UID: NF.wdm.KeMemoryBarrier~r3
title: KeMemoryBarrier
author: windows-driver-content
description: The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations.
old-location: kernel\kememorybarrier.htm
old-project: kernel
ms.assetid: e6ffb893-a79f-4cc0-9052-667b835f4ad3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeMemoryBarrier
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeMemoryBarrier
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

# KeMemoryBarrier function



## -description
<p>The <b>KeMemoryBarrier</b> routine creates a barrier at its position in the code—across which the compiler and the processor cannot move any operations.</p>


## -syntax

````
VOID KeMemoryBarrier(void);
````


## -parameters


## -returns
<p>None</p>

<p>None</p>

<p>None</p>

## -remarks
<p>The <b>KeMemoryBarrier</b> routine inserts a memory barrier into your code. This barrier guarantees that every operation that appears in the source code before the call to <b>KeMemoryBarrier</b> will complete before any operation that appears after the call.</p>

<p>The implementation of the <b>KeMemoryBarrier</b> routine depends on the processor architecture. For example, for an x86 processor, the Wdm.h header file defines <b>KeMemoryBarrier</b> to be the following inline function:</p>

<p>In this definition, the braces that follow the <b>__asm</b> keyword contain inline assembly code. The compiler optimizer cannot move an instruction from a position before the inline assembly code to a position after the inline assembly code, and vice versa. In addition, the <b>xchg</b> instruction implicitly includes the <b>lock</b> prefix, which forces the processor hardware to complete the memory operations for all instructions that precede the <b>xchg</b> instruction before it initiates memory operations for instructions that follow the <b>xchg</b> instruction.</p>

<p><b>KeMemoryBarrier</b> prevents both the compiler and the processor from moving operations across the barrier. To prevent only the compiler from moving operations, call <a href="kernel.kememorybarrierwithoutfence">KeMemoryBarrierWithoutFence</a>. </p>

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
<a href="kernel.kememorybarrierwithoutfence">KeMemoryBarrierWithoutFence</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeMemoryBarrier routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
