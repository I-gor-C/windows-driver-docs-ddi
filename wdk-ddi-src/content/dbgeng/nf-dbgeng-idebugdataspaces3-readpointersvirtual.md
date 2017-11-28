---
UID: NF.dbgeng.IDebugDataSpaces3.ReadPointersVirtual
title: IDebugDataSpaces3::ReadPointersVirtual
author: windows-driver-content
description: The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space.
old-location: debugger\readpointersvirtual.htm
old-project: debugger
ms.assetid: 003fd20c-12d6-40b0-8e43-a7d730199846
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces3, ReadPointersVirtual, IDebugDataSpaces3::ReadPointersVirtual
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
req.alt-api: IDebugDataSpaces.ReadPointersVirtual,IDebugDataSpaces2.ReadPointersVirtual,IDebugDataSpaces3.ReadPointersVirtual,IDebugDataSpaces4.ReadPointersVirtual
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

# IDebugDataSpaces3::ReadPointersVirtual method



## -description
<p>The <b>ReadPointersVirtual</b> method is a convenience method for reading pointers from the target's virtual address space.</p>


## -syntax

````
HRESULT ReadPointersVirtual(
  [in]  ULONG    Count,
  [in]  ULONG64  Offset,
  [out] PULONG64 Ptrs
);
````


## -parameters
<dl>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of pointers to read.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space to start reading the pointers.</p>
</dd>

### -param <i>Ptrs</i> [out]

<dd>
<p>Specifies the array to store the pointers.  The number of elements this array holds is <i>Count</i>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>All the pointers were read from the target's memory and stored in <i>Ptrs</i>.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method reads from the memory from the target's virtual address space.  The memory is then treated as a list of pointers.  Any 32-bit pointers are then sign-extended to  64-bit values.</p>

<p>This method reads from the memory from the target's virtual address space.  The memory is then treated as a list of pointers.  Any 32-bit pointers are then sign-extended to  64-bit values.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554359">ReadVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561451">WritePointersVirtual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces::ReadPointersVirtual method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
