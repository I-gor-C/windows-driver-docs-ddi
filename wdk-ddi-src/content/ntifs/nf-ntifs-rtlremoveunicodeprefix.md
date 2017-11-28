---
UID: NF.ntifs.RtlRemoveUnicodePrefix
title: RtlRemoveUnicodePrefix
author: windows-driver-content
description: The RtlRemoveUnicodePrefix routine removes an element from a prefix table.
old-location: ifsk\rtlremoveunicodeprefix.htm
old-project: ifsk
ms.assetid: b2f996b1-0c1a-4ad5-a4c4-5d84ca94c5a1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlRemoveUnicodePrefix
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Windows XP
req.target-min-winversvr: Windows Server 2003
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlRemoveUnicodePrefix
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
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# RtlRemoveUnicodePrefix function



## -description
<p>The <b>RtlRemoveUnicodePrefix</b> routine removes an element from a prefix table. </p>


## -syntax

````
VOID RtlRemoveUnicodePrefix(
  _In_ PUNICODE_PREFIX_TABLE       PrefixTable,
  _In_ PUNICODE_PREFIX_TABLE_ENTRY PrefixTableEntry
);
````


## -parameters
<dl>

### -param <i>PrefixTable</i> [in]

<dd>
<p>Pointer to the prefix table. The table must have been initialized by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553015">RtlInitializeUnicodePrefix</a>.</p>
</dd>

### -param <i>PrefixTableEntry</i> [in]

<dd>
<p>Pointer to the prefix table element to be deleted. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>File systems must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553015">RtlInitializeUnicodePrefix</a> to initialize the prefix table before using any other <b>Rtl..UnicodePrefix</b> routines on it. The initialized prefix table structure should be considered opaque.</p>

<p>Callers of the <b>Rtl..UnicodePrefix</b> routines are responsible for synchronizing access to the prefix table. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

<p>File systems must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553015">RtlInitializeUnicodePrefix</a> to initialize the prefix table before using any other <b>Rtl..UnicodePrefix</b> routines on it. The initialized prefix table structure should be considered opaque.</p>

<p>Callers of the <b>Rtl..UnicodePrefix</b> routines are responsible for synchronizing access to the prefix table. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows XP</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2003</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552272">RtlFindUnicodePrefix</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553015">RtlInitializeUnicodePrefix</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553038">RtlInsertUnicodePrefix</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553123">RtlNextUnicodePrefix</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlRemoveUnicodePrefix routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
