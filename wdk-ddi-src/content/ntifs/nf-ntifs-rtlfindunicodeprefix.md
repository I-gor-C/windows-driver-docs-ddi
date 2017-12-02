---
UID: NF.ntifs.RtlFindUnicodePrefix
title: RtlFindUnicodePrefix
author: windows-driver-content
description: The RtlFindUnicodePrefix routine searches for the best match for a given Unicode file name in a prefix table.
old-location: ifsk\rtlfindunicodeprefix.htm
old-project: ifsk
ms.assetid: 525db78d-b25c-4325-ac71-b992564a19c0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlFindUnicodePrefix
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
req.alt-api: RtlFindUnicodePrefix
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# RtlFindUnicodePrefix function



## -description
<p>The <b>RtlFindUnicodePrefix</b> routine searches for the best match for a given Unicode file name in a prefix table. </p>


## -syntax

````
PUNICODE_PREFIX_TABLE_ENTRY RtlFindUnicodePrefix(
  _In_ PUNICODE_PREFIX_TABLE PrefixTable,
  _In_ PCUNICODE_STRING      FullName,
  _In_ ULONG                 CaseInsensitiveIndex
);
````


## -parameters
<dl>

### -param PrefixTable [in]

<dd>
<p>Pointer to the prefix table. The table must have been initialized by calling <a href="..\ntifs\nf-ntifs-rtlinitializeunicodeprefix.md">RtlInitializeUnicodePrefix</a>.</p>
</dd>

### -param FullName [in]

<dd>
<p>Pointer to a Unicode string containing the full pathname for a file. </p>
</dd>

### -param CaseInsensitiveIndex [in]

<dd>
<p>Position in the file name and prefix strings at which the comparison is to become case-insensitive. The string comparison is case-sensitive for the first <i>CaseInsensitiveIndex</i> characters in each string, case-insensitive for the remainder of the string.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>String comparison is case-insensitive.</p>
</td>
</tr>
<tr>
<td>
<p>1..<i>FullName.Length</i>-1</p>
</td>
<td>
<p>String comparison is case-sensitive for characters at positions 0 through <i>CaseInsensitiveIndex</i>-1, case-insensitive for characters from position <i>CaseInsensitiveIndex</i> to the end of the string.</p>
</td>
</tr>
<tr>
<td>
<p><i>FullName.Length</i></p>
</td>
<td>
<p>String comparison is case-sensitive.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>RtlFindUnicodePrefix</b> returns a pointer to the longest proper prefix found for the given string at <i>FullName</i>. If no matching prefix is found, <b>RtlFindUnicodePrefix</b> returns <b>NULL</b>. </p>

## -remarks
<p>Each prefix entry in the table is a pathname relative to the root directory of a file system volume. To be well-formed, the prefix must begin with a single backslash (\). </p>

<p>When it finds a matching prefix, <b>RtlFindUnicodePrefix</b> rebalances the prefix table's splay tree.</p>

<p>File systems must call <a href="..\ntifs\nf-ntifs-rtlinitializeunicodeprefix.md">RtlInitializeUnicodePrefix</a> to initialize the prefix table before using any other <b>Rtl..UnicodePrefix</b> routines on it. The initialized prefix table structure should be considered opaque.</p>

<p>Callers of the <b>Rtl..UnicodePrefix</b> routines are responsible for synchronizing access to the prefix table. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-rtlinitializeunicodeprefix.md">RtlInitializeUnicodePrefix</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlinsertunicodeprefix.md">RtlInsertUnicodePrefix</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlnextunicodeprefix.md">RtlNextUnicodePrefix</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlremoveunicodeprefix.md">RtlRemoveUnicodePrefix</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlFindUnicodePrefix routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
