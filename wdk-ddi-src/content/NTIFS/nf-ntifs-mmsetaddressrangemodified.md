---
UID: NF.ntifs.MmSetAddressRangeModified
title: MmSetAddressRangeModified
author: windows-driver-content
description: The MmSetAddressRangeModified routine marks currently valid pages in the specified range of the system cache as modified.
old-location: ifsk\mmsetaddressrangemodified.htm
ms.assetid: c903485f-205e-4679-99a7-2a644731fa77
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmSetAddressRangeModified
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
req.irql: See Remarks section
ms.keywords: MmSetAddressRangeModified
req.iface: 
---

# MmSetAddressRangeModified function



## -description
<p>The <b>MmSetAddressRangeModified</b> routine marks currently valid pages in the specified range of the system cache as modified.</p>


## -syntax

````
BOOLEAN MmSetAddressRangeModified(
  _In_ PVOID  Address,
  _In_ SIZE_T Length
);
````


## -parameters
<dl>

### -param <i>Address</i> [in]

<dd>
<p>Address of the start of the range.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Length of the range in bytes.</p>
</dd>
</dl>

## -returns
<p><b>MmSetAddressRangeModified</b> returns <b>TRUE</b> if it marked at least one page in the range as modified, <b>FALSE</b> otherwise.</p>

## -remarks
<p>The entire range specified by <i>Address</i> and <i>Length</i> must reside within the system cache.</p>

<p>For more information about memory management, see <a href="https://msdn.microsoft.com/e030a37c-26ab-4177-9980-4336928975e1">Memory Management</a>. </p>

<p>Callers of <b>MmSetAddressRangeModified</b> must be running at IRQL &lt; DISPATCH_LEVEL for pageable addresses, and IRQL &lt;= DISPATCH_LEVEL for nonpageable addresses.</p>

<p>The entire range specified by <i>Address</i> and <i>Length</i> must reside within the system cache.</p>

<p>For more information about memory management, see <a href="https://msdn.microsoft.com/e030a37c-26ab-4177-9980-4336928975e1">Memory Management</a>. </p>

<p>Callers of <b>MmSetAddressRangeModified</b> must be running at IRQL &lt; DISPATCH_LEVEL for pageable addresses, and IRQL &lt;= DISPATCH_LEVEL for nonpageable addresses.</p>

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
<p>See Remarks section</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539145">CcIsThereDirtyData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MmSetAddressRangeModified routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
