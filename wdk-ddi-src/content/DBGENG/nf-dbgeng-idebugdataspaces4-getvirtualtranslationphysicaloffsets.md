---
UID: NF.dbgeng.IDebugDataSpaces4.GetVirtualTranslationPhysicalOffsets
title: IDebugDataSpaces4::GetVirtualTranslationPhysicalOffsets
author: windows-driver-content
description: The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy.
old-location: debugger\getvirtualtranslationphysicaloffsets.htm
ms.assetid: 40438ee7-2e58-4048-8739-75f21179c22c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces2.GetVirtualTranslationPhysicalOffsets,IDebugDataSpaces3.GetVirtualTranslationPhysicalOffsets,IDebugDataSpaces4.GetVirtualTranslationPhysicalOffsets
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
ms.keywords: IDebugDataSpaces4, GetVirtualTranslationPhysicalOffsets, IDebugDataSpaces4::GetVirtualTranslationPhysicalOffsets
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::GetVirtualTranslationPhysicalOffsets method



## -description
<p>The <b>GetVirtualTranslationPhysicalOffsets</b> method returns the physical addresses of the system paging structures at different levels of the paging hierarchy.</p>


## -syntax

````
HRESULT GetVirtualTranslationPhysicalOffsets(
  [in]            ULONG64  Virtual,
  [out, optional] PULONG64 Offsets,
  [in]            ULONG    OffsetsSize,
  [out, optional] PULONG   Levels
);
````


## -parameters
<dl>

### -param <i>Virtual</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space to translate.</p>
</dd>

### -param <i>Offsets</i> [out, optional]

<dd>
<p>Receives the physical addresses for the system paging structures.  If it is set to <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>OffsetsSize</i> [in]

<dd>
<p>Specifies the number of elements the array <i>Offsets</i> holds.  This is the maximum number of addresses that will be returned.</p>
</dd>

### -param <i>Levels</i> [out, optional]

<dd>
<p>Receives the number of levels in the paging hierarchy for the specified address.  If this is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>HRESULT_FROM_NT(STATUS_NO_PAGEFILE)</b></dt>
</dl><p>No physical page containing the specified address could be found.</p>

<p> </p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>Translating a virtual address to a physical address requires Windows  to walk down the paging hierarchy.  At each level it reads paging information from physical memory.  This method returns the offsets for these physical pages.  The number of levels in the paging hierarchy may be different for different addresses.</p>

<p>The address at the last level of the hierarchy is the physical address corresponding to the specified virtual address.  This is what <a href="https://msdn.microsoft.com/library/windows/hardware/ff560335">VirtualToPhysical</a> would return.</p>

<p>For details on how virtual addresses are translated into physical addresses, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>This method is only available in kernel-mode debugging.</p>

<p>Translating a virtual address to a physical address requires Windows  to walk down the paging hierarchy.  At each level it reads paging information from physical memory.  This method returns the offsets for these physical pages.  The number of levels in the paging hierarchy may be different for different addresses.</p>

<p>The address at the last level of the hierarchy is the physical address corresponding to the specified virtual address.  This is what <a href="https://msdn.microsoft.com/library/windows/hardware/ff560335">VirtualToPhysical</a> would return.</p>

<p>For details on how virtual addresses are translated into physical addresses, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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