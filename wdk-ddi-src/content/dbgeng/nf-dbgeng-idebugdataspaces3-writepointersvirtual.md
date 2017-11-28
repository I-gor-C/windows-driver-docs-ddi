---
UID: NF.dbgeng.IDebugDataSpaces3.WritePointersVirtual
title: IDebugDataSpaces3::WritePointersVirtual
author: windows-driver-content
description: The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space.
old-location: debugger\writepointersvirtual.htm
old-project: debugger
ms.assetid: b6bde54b-262a-4431-8f85-63f9c66463c4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces3, WritePointersVirtual, IDebugDataSpaces3::WritePointersVirtual
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.WritePointersVirtual,IDebugDataSpaces2.WritePointersVirtual,IDebugDataSpaces3.WritePointersVirtual,IDebugDataSpaces4.WritePointersVirtual
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugDataSpaces3
---

# IDebugDataSpaces3::WritePointersVirtual method



## -description
<p>The <b>WritePointersVirtual</b> method is a convenience method for writing pointers to the target's virtual address space.</p>


## -syntax

````
HRESULT WritePointersVirtual(
  [in] ULONG    Count,
  [in] ULONG64  Offset,
  [in] PULONG64 Ptrs
);
````


## -parameters
<dl>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of pointers to write.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space at which to start writing the pointers.</p>
</dd>

### -param <i>Ptrs</i> [in]

<dd>
<p>Specifies the array of pointers to write.  The number of elements in this array is <i>Count</i>.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>All the pointers in <i>Ptrs</i>  were written to the target's memory.</p>

<p> </p>

## -remarks
<p>If the target uses 32-bit pointers, this method casts the specified  64-bit values into 32-bit pointers.  Then it writes these pointers to the target's memory.</p>

<p>If the target uses 32-bit pointers, this method casts the specified  64-bit values into 32-bit pointers.  Then it writes these pointers to the target's memory.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550528">IDebugDataSpaces</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550537">IDebugDataSpaces3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550546">IDebugDataSpaces4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561468">WriteVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554323">ReadPointersVirtual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces::WritePointersVirtual method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
