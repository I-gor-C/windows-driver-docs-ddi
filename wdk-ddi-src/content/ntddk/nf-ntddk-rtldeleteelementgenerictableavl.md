---
UID: NF.ntddk.RtlDeleteElementGenericTableAvl
title: RtlDeleteElementGenericTableAvl
author: windows-driver-content
description: The RtlDeleteElementGenericTableAvl routine deletes an element from a generic table.
old-location: ifsk\rtldeleteelementgenerictableavl.htm
old-project: ifsk
ms.assetid: 700412A3-5905-4401-BA65-C2DE1613398D
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlDeleteElementGenericTableAvl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDeleteElementGenericTableAvl
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
req.iface: 
---

# RtlDeleteElementGenericTableAvl function



## -description
<p>The <b>RtlDeleteElementGenericTableAvl</b> routine deletes an element from a generic table. </p>


## -syntax

````
BOOLEAN RtlDeleteElementGenericTableAvl(
  _In_ PRTL_AVL_TABLE Table,
  _In_ PVOID          Buffer
);
````


## -parameters
<dl>

### -param <i>Table</i> [in]

<dd>
<p>A pointer to the generic table (<a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a>). The table must have been initialized by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to a caller-allocated buffer containing a value that uniquely identifies the element to be deleted.</p>
</dd>
</dl>

## -returns
<p><b>RtlDeleteElementGenericTableAvl</b> returns <b>TRUE</b> if the element was successfully deleted, <b>FALSE</b> otherwise.</p>

## -remarks
<p><b>RtlDeleteElementGenericTableAvl</b> calls the <i>CompareRoutine</i> and <i>FreeRoutine</i> that were registered in the call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>. </p>

<p>By default, the operating system uses splay trees to implement generic tables, but the <b>RtlDeleteElementGenericTableAvl</b> routine only works with Adelson-Velsky/Landis (AVL) trees. To configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:</p>

<p>#define RTL_USE_AVL_TABLES 0</p>

<p>If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. For example, use the <b>RtlDeleteElementGenericTableAvl</b> routine instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552209">RtlDeleteElementGenericTable</a>. In the call to <b>RtlDeleteElementGenericTableAvl</b>, the caller must pass a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a> table structure rather than <a href="https://msdn.microsoft.com/library/windows/hardware/ff553345">RTL_GENERIC_TABLE</a>.</p>

<p>Callers of the <i>Rtl..GenericTableAvl</i> routines are responsible for exclusively synchronizing access to the generic table. An exclusive fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlDeleteElementGenericTableAvl</b> must be running at IRQL &lt; DISPATCH_LEVEL if either of the following conditions holds:</p>

<p>The caller-allocated memory at <i>Table</i> or at <i>Buffer</i> is pageable.</p>

<p>The caller-supplied <i>CompareRoutine</i> or <i>FreeRoutine</i> contains pageable code. </p>

<p><b>RtlDeleteElementGenericTableAvl</b> calls the <i>CompareRoutine</i> and <i>FreeRoutine</i> that were registered in the call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>. </p>

<p>By default, the operating system uses splay trees to implement generic tables, but the <b>RtlDeleteElementGenericTableAvl</b> routine only works with Adelson-Velsky/Landis (AVL) trees. To configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:</p>

<p>#define RTL_USE_AVL_TABLES 0</p>

<p>If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. For example, use the <b>RtlDeleteElementGenericTableAvl</b> routine instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552209">RtlDeleteElementGenericTable</a>. In the call to <b>RtlDeleteElementGenericTableAvl</b>, the caller must pass a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a> table structure rather than <a href="https://msdn.microsoft.com/library/windows/hardware/ff553345">RTL_GENERIC_TABLE</a>.</p>

<p>Callers of the <i>Rtl..GenericTableAvl</i> routines are responsible for exclusively synchronizing access to the generic table. An exclusive fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlDeleteElementGenericTableAvl</b> must be running at IRQL &lt; DISPATCH_LEVEL if either of the following conditions holds:</p>

<p>The caller-allocated memory at <i>Table</i> or at <i>Buffer</i> is pageable.</p>

<p>The caller-supplied <i>CompareRoutine</i> or <i>FreeRoutine</i> contains pageable code. </p>

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
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406468">RtlInsertElementGenericTableAvl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDeleteElementGenericTableAvl routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
