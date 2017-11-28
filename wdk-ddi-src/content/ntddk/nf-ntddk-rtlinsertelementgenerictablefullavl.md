---
UID: NF.ntddk.RtlInsertElementGenericTableFullAvl
title: RtlInsertElementGenericTableFullAvl
author: windows-driver-content
description: The RtlInsertElementGenericTableFullAvl routine adds a new entry to a generic table.
old-location: ifsk\rtlinsertelementgenerictablefullavl.htm
old-project: ifsk
ms.assetid: c7d346ab-6990-4636-bafd-2e448a937f3b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlInsertElementGenericTableFullAvl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlInsertElementGenericTableFullAvl
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
req.irql: < DISPATCH_LEVEL (see Remarks section)
req.iface: 
---

# RtlInsertElementGenericTableFullAvl function



## -description
<p>The <b>RtlInsertElementGenericTableFullAvl</b> routine adds a new entry to a generic table. </p>


## -syntax

````
PVOID RtlInsertElementGenericTableFullAvl(
  _In_      PRTL_AVL_TABLE      Table,
  _In_      PVOID               Buffer,
  _In_      CLONG               BufferSize,
  _Out_opt_ PBOOLEAN            NewElement,
  _In_      PVOID               NodeOrParent,
  _In_      TABLE_SEARCH_RESULT SearchResult
);
````


## -parameters
<dl>

### -param <i>Table</i> [in]

<dd>
<p>Pointer to a generic Adelson-Velsky/Landis (AVL) table (<a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a>) that was initialized by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A caller-allocated buffer that contains the user data to copy into the new element. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>. </p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Size in bytes of data in <i>Buffer.</i></p>
</dd>

### -param <i>NewElement</i> [out, optional]

<dd>
<p>On output, a value of <b>TRUE</b> means the insertion of the new element in the generic table was successful. A value of <b>FALSE</b> means the insertion failed.</p>
</dd>

### -param <i>NodeOrParent</i> [in]

<dd>
<p>The search result of a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553092">RtlLookupElementGenericTableFullAvl</a>. This value indicates to the <b>RtlInsertElementGenericTableFullAvl</b> routine whether the tree is currently empty, or if not empty, whether to insert the new entry to the left or the right of the parent entry. The <i>SearchResult</i> parameter can have any of the following values:</p>
<p></p>
<dl>

### -param <a id="TableEmptyTree"></a><a id="tableemptytree"></a><a id="TABLEEMPTYTREE"></a><b>TableEmptyTree</b>

<dd>
<p>The tree was empty. The contents of <i>NodeOrParent</i> has <i>not</i> been altered.</p>
</dd>

### -param <a id="TableFoundNode"></a><a id="tablefoundnode"></a><a id="TABLEFOUNDNODE"></a><b>TableFoundNode</b>

<dd>
<p>The <b>RtlInsertElementGenericTableFullAvl</b> routine found a table entry whose key matches the data in <i>Buffer</i>. <i>NodeOrParent</i> contains a pointer to the matched entry.</p>
</dd>

### -param <a id="TableInsertAsLeft"></a><a id="tableinsertasleft"></a><a id="TABLEINSERTASLEFT"></a><b>TableInsertAsLeft</b>

<dd>
<p>The <b>RtlInsertElementGenericTableFullAvl</b> routine did <i>not</i> find a table entry whose key matches the data in <i>Buffer</i>. If the entry that <b>RtlInsertElementGenericTableFullAvl</b> searched for were in the table, it would be the left child of the entry that <i>NodeOrParent</i> points to.</p>
</dd>

### -param <a id="TableInsertAsRight"></a><a id="tableinsertasright"></a><a id="TABLEINSERTASRIGHT"></a><b>TableInsertAsRight</b>

<dd>
<p>The <b>RtlInsertElementGenericTableFullAvl</b> routine did <i>not</i> find a table entry whose key matches the data in <i>Buffer</i>. If the entry that <b>RtlInsertElementGenericTableFullAvl</b> searched for were in the table, it would be the right child of the entry that <i>NodeOrParent</i> points to.</p>
</dd>
</dl>
</dd>

### -param <i>SearchResult</i> [in]

<dd>
<p>A pointer to a table entry. If the <b>RtlInsertElementGenericTableFullAvl</b> routine matches an entry, <i>NodeOrParent</i> points to the matched entry. If the <b>RtlInsertElementGenericTableFullAvl</b> routine fails to find a match, <i>NodeOrParent</i> points to the entry that would be the parent of the entry that <b>RtlInsertElementGenericTableFullAvl</b> routine was searching for.</p>
</dd>
</dl>

## -returns
<p><b>RtlInsertElementGenericTableFullAvl</b> returns a pointer to the user data for the newly inserted entry, or the user data for a matching entry that is already in the generic table. If no matching entry is found, but <b>RtlInsertElementGenericTableFullAvl</b> cannot insert the new entry (for example, because the <i>AllocateRoutine</i> fails), <b>RtlInsertElementGenericTableFullAvl</b> returns <b>NULL</b>. </p>

## -remarks
<p>To insert an entry, <b>RtlInsertElementGenericTableFullAvl</b> calls the <i>CompareRoutine</i> and <i>AllocateRoutine</i> that were registered when the generic table was initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>. After inserting the new entry, <b>RtlInsertElementGenericTableFullAvl</b> rebalances the AVL link tree.</p>

<p>When a new entry is inserted into the table, its data is copied from <i>Buffer</i> into the new entry. Thus the pointer returned by <b>RtlInsertElementGenericTableFullAvl</b> is never equal to <i>Buffer</i>. </p>

<p>If the caller's <i>CompareRoutine</i> returns <b>GenericEqual</b>, the data at <i>Buffer</i> is assumed to duplicate the data for an existing entry in the generic table. In this case, <b>RtlInsertElementGenericTableFullAvl</b> does not add the new entry (and thus does not call the <i>AllocateRoutine</i>), because a generic table cannot have duplicate entries.</p>

<p>If a matching entry already exists in the generic table, <b>RtlInsertElementGenericTableFullAvl</b> returns a pointer to the existing entry's data and sets <i>NewElement</i> to <b>FALSE</b>. </p>

<p>If there is no matching entry in the table already,<b>RtlInsertElementGenericTableFullAvl</b> routine allocates sufficient space for the user data of new entry (<i>BufferSize</i>) plus the links associated with the new entry. Thus the total number of bytes will be at least <i>BufferSize</i> + <b>sizeof</b>(BALANCED_LINKS). Caller should not use the first <b>sizeof</b>(BALANCED_LINKS) bytes of the memory that the <i>AllocateRoutine</i>allocates.</p>

<p>Callers of the<i>Rtl..GenericTableAvl</i> routines are responsible for exclusively synchronizing access to the generic table. An exclusive fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>By default, the operating system uses splay trees to implement generic tables, but the <b>RtlInsertElementGenericTableFullAvl</b> routine only works with Adelson-Velsky/Landis (AVL) trees. To configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:</p>

<p>#define RTL_USE_AVL_TABLES 0</p>

<p>If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. For example, use the <b>RtlInsertElementGenericTableFullAvl</b> routine instead of <b>RtlInsertElementGenericTableFull</b>. In the call to <b>RtlInsertElementGenericTableFullAvl</b>, the caller must pass a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a> table structure rather than <a href="https://msdn.microsoft.com/library/windows/hardware/ff553345">RTL_GENERIC_TABLE</a>.</p>

<p>Callers of <b>RtlInsertElementGenericTableFullAvl</b> must be running at IRQL &lt; DISPATCH_LEVEL if either of the following conditions holds:</p>

<p>The caller-allocated memory at <i>Table</i> or at <i>Buffer</i> is pageable.</p>

<p>The caller-supplied <i>CompareRoutine</i> or <i>AllocateRoutine</i> contains pageable code. </p>

<p>To insert an entry, <b>RtlInsertElementGenericTableFullAvl</b> calls the <i>CompareRoutine</i> and <i>AllocateRoutine</i> that were registered when the generic table was initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>. After inserting the new entry, <b>RtlInsertElementGenericTableFullAvl</b> rebalances the AVL link tree.</p>

<p>When a new entry is inserted into the table, its data is copied from <i>Buffer</i> into the new entry. Thus the pointer returned by <b>RtlInsertElementGenericTableFullAvl</b> is never equal to <i>Buffer</i>. </p>

<p>If the caller's <i>CompareRoutine</i> returns <b>GenericEqual</b>, the data at <i>Buffer</i> is assumed to duplicate the data for an existing entry in the generic table. In this case, <b>RtlInsertElementGenericTableFullAvl</b> does not add the new entry (and thus does not call the <i>AllocateRoutine</i>), because a generic table cannot have duplicate entries.</p>

<p>If a matching entry already exists in the generic table, <b>RtlInsertElementGenericTableFullAvl</b> returns a pointer to the existing entry's data and sets <i>NewElement</i> to <b>FALSE</b>. </p>

<p>If there is no matching entry in the table already,<b>RtlInsertElementGenericTableFullAvl</b> routine allocates sufficient space for the user data of new entry (<i>BufferSize</i>) plus the links associated with the new entry. Thus the total number of bytes will be at least <i>BufferSize</i> + <b>sizeof</b>(BALANCED_LINKS). Caller should not use the first <b>sizeof</b>(BALANCED_LINKS) bytes of the memory that the <i>AllocateRoutine</i>allocates.</p>

<p>Callers of the<i>Rtl..GenericTableAvl</i> routines are responsible for exclusively synchronizing access to the generic table. An exclusive fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>By default, the operating system uses splay trees to implement generic tables, but the <b>RtlInsertElementGenericTableFullAvl</b> routine only works with Adelson-Velsky/Landis (AVL) trees. To configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:</p>

<p>#define RTL_USE_AVL_TABLES 0</p>

<p>If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. For example, use the <b>RtlInsertElementGenericTableFullAvl</b> routine instead of <b>RtlInsertElementGenericTableFull</b>. In the call to <b>RtlInsertElementGenericTableFullAvl</b>, the caller must pass a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a> table structure rather than <a href="https://msdn.microsoft.com/library/windows/hardware/ff553345">RTL_GENERIC_TABLE</a>.</p>

<p>Callers of <b>RtlInsertElementGenericTableFullAvl</b> must be running at IRQL &lt; DISPATCH_LEVEL if either of the following conditions holds:</p>

<p>The caller-allocated memory at <i>Table</i> or at <i>Buffer</i> is pageable.</p>

<p>The caller-supplied <i>CompareRoutine</i> or <i>AllocateRoutine</i> contains pageable code. </p>

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
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
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
<p>&lt; DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552209">RtlDeleteElementGenericTable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552989">RtlInitializeGenericTable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlInsertElementGenericTableFullAvl routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
