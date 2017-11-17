---
UID: NF.ntddk.RtlLookupFirstMatchingElementGenericTableAvl
title: RtlLookupFirstMatchingElementGenericTableAvl
author: windows-driver-content
description: The RtlLookupFirstMatchingElementGenericTableAvl routine finds the left-most element in the tree that matches the indicated data.
old-location: ifsk\rtllookupfirstmatchingelementgenerictableavl.htm
ms.assetid: ff9cea5d-a93f-4d3c-b034-d2bf85484df3
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntddk.h
req.include-header: FltKernel.h, Ntifs.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlLookupFirstMatchingElementGenericTableAvl
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
req.irql: <= APC_LEVEL (see Remarks section)
ms.keywords: RtlLookupFirstMatchingElementGenericTableAvl
req.iface: 
---

# RtlLookupFirstMatchingElementGenericTableAvl function



## -description
<p>The <b>RtlLookupFirstMatchingElementGenericTableAvl</b> routine finds the left-most element in the tree that matches the indicated data.</p>


## -syntax

````
PVOID RtlLookupFirstMatchingElementGenericTableAvl(
  _In_  PRTL_AVL_TABLE Table,
  _In_  PVOID          Buffer,
  _Out_ PVOID          *RestartKey
);
````


## -parameters
<dl>

### -param <i>Table</i> [in]

<dd>
<p>A pointer to the generic Adelson-Velsky/Landis (AVL) table (<a href="https://msdn.microsoft.com/library/windows/hardware/ff553327">RTL_AVL_TABLE</a>).</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A buffer that contains the search data.</p>
</dd>

### -param <i>RestartKey</i> [out]

<dd>
<p>On output, contains a search context to use with an enumeration routine, such as <a href="https://msdn.microsoft.com/library/windows/hardware/hh406462">RtlEnumerateGenericTableWithoutSplayingAvl</a>.</p>
</dd>
</dl>

## -returns
<p>The <b>RtlLookupFirstMatchingElementGenericTableAvl</b>routine returns a pointer to the matched data, or <b>NULL</b> if no match was found.</p>

## -remarks
<p>A tree that implements a generic table might contain several file names that differ only in case. A search algorithm can use this routine to locate the first match, without reference to case, and use an enumeration routine, such as <a href="https://msdn.microsoft.com/library/windows/hardware/hh406462">RtlEnumerateGenericTableWithoutSplayingAvl</a>, to return each subsequent match.</p>

<p>By default, the operating system uses splay trees to implement generic tables, but the <b>RtlLookupFirstMatchingElementGenericTableAvl</b>routine only works with Adelson-Velsky/Landis (AVL) trees. Under some circumstances, operations on a splay tree will make the tree deep and narrow and might even turn it into a straight line. Very deep trees degrade the performance of searches. You can ensure a more balanced, shallower tree implementation of generic tables by using Adelson-Velsky/Landis (AVL) trees. If you want to configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:</p>

<p>#define RTL_USE_AVL_TABLES 0</p>

<p>If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. </p>

<p>Callers of <b>RtlLookupFirstMatchingElementGenericTableAvl</b> must be running at &lt;= APC_LEVEL if either of the following conditions holds:</p>

<p>A tree that implements a generic table might contain several file names that differ only in case. A search algorithm can use this routine to locate the first match, without reference to case, and use an enumeration routine, such as <a href="https://msdn.microsoft.com/library/windows/hardware/hh406462">RtlEnumerateGenericTableWithoutSplayingAvl</a>, to return each subsequent match.</p>

<p>By default, the operating system uses splay trees to implement generic tables, but the <b>RtlLookupFirstMatchingElementGenericTableAvl</b>routine only works with Adelson-Velsky/Landis (AVL) trees. Under some circumstances, operations on a splay tree will make the tree deep and narrow and might even turn it into a straight line. Very deep trees degrade the performance of searches. You can ensure a more balanced, shallower tree implementation of generic tables by using Adelson-Velsky/Landis (AVL) trees. If you want to configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:</p>

<p>#define RTL_USE_AVL_TABLES 0</p>

<p>If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. </p>

<p>Callers of <b>RtlLookupFirstMatchingElementGenericTableAvl</b> must be running at &lt;= APC_LEVEL if either of the following conditions holds:</p>

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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include FltKernel.h, Ntifs.h, or Ntddk.h)</dt>
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
<p>&lt;= APC_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406462">RtlEnumerateGenericTableWithoutSplayingAvl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlLookupFirstMatchingElementGenericTableAvl routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
