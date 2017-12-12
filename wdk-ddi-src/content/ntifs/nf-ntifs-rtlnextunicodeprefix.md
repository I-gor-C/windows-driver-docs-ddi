---
UID: NF.ntifs.RtlNextUnicodePrefix
title: RtlNextUnicodePrefix function
author: windows-driver-content
description: The RtlNextUnicodePrefix routine is used to enumerate the elements in a Unicode prefix table.
old-location: ifsk\rtlnextunicodeprefix.htm
old-project: ifsk
ms.assetid: c4f43f4c-a598-4bda-9325-21440f56ab17
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlNextUnicodePrefix
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
req.alt-api: RtlNextUnicodePrefix
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
---

# RtlNextUnicodePrefix function



## -description
The <b>RtlNextUnicodePrefix</b> routine is used to enumerate the elements in a Unicode prefix table. 



## -syntax

````
PUNICODE_PREFIX_TABLE_ENTRY RtlNextUnicodePrefix(
  _In_ PUNICODE_PREFIX_TABLE PrefixTable,
  _In_ BOOLEAN               Restart
);
````


## -parameters

### -param PrefixTable [in]

Pointer to the prefix table. The table must have been initialized by calling <a href="ifsk.rtlinitializeunicodeprefix">RtlInitializeUnicodePrefix</a>.


### -param Restart [in]

Set to <b>TRUE</b> if the enumeration is to start at the first element in the table. Set to <b>FALSE</b> if resuming the enumeration from a previous call.

To enumerate all elements in the table, use <b>RtlNextUnicodePrefix</b> as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>for (p = RtlNextUnicodePrefix ( Table, TRUE );
     p != NULL;
     p = RtlNextUnicodePrefix ( Table, FALSE )) {
        // Process the element pointed to by p
}</pre>
</td>
</tr>
</table></span></div>

## -returns
<b>RtlNextUnicodePrefix</b> returns a pointer to the next element, if one exists. If there are no more elements in the table, <b>RtlNextUnicodePrefix</b> returns <b>NULL</b>. 


## -remarks
File systems must call <a href="ifsk.rtlinitializeunicodeprefix">RtlInitializeUnicodePrefix</a> to initialize the prefix table before using any other <b>Rtl..UnicodePrefix</b> routines on it. The initialized prefix table structure should be considered opaque.

Callers of the <b>Rtl..UnicodePrefix</b> routines are responsible for synchronizing access to the prefix table. A fast mutex is the most efficient synchronization mechanism to use for this purpose. 

For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows XP

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2003

</td>
</tr>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.rtlfindunicodeprefix">RtlFindUnicodePrefix</a>
</dt>
<dt>
<a href="ifsk.rtlinitializeunicodeprefix">RtlInitializeUnicodePrefix</a>
</dt>
<dt>
<a href="ifsk.rtlinsertunicodeprefix">RtlInsertUnicodePrefix</a>
</dt>
<dt>
<a href="ifsk.rtlremoveunicodeprefix">RtlRemoveUnicodePrefix</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlNextUnicodePrefix routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

