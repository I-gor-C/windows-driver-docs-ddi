---
UID: NF.wdm.RtlSecureZeroMemory
title: RtlSecureZeroMemory
author: windows-driver-content
description: The RtlSecureZeroMemory routine fills a block of memory with zeros in a way that is guaranteed to be secure.
old-location: kernel\rtlsecurezeromemory.htm
old-project: kernel
ms.assetid: b7a9beaf-5eca-4fb0-af63-06c002297085
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlSecureZeroMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows. (Because the routine is declared inline, the body of the routine can be included in earlier versions of the operating system.)
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlSecureZeroMemory
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level (See Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# RtlSecureZeroMemory function



## -description
<p>The <b>RtlSecureZeroMemory</b> routine fills a block of memory with zeros in a way that is guaranteed to be secure.</p>


## -syntax

````
PVOID RtlSecureZeroMemory(
  _Out_ PVOID  ptr,
  _In_  SIZE_T cnt
);
````


## -parameters
<dl>

### -param ptr [out]

<dd>
<p>Pointer to the memory buffer to be filled with zeros.</p>
</dd>

### -param cnt [in]

<dd>
<p>Specifies the number of bytes to be filled with zeros.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The effect of <b>RtlSecureZeroMemory</b> is identical to that of <a href="..\wdm\nf-wdm-rtlzeromemory.md">RtlZeroMemory</a>, except that it is guaranteed to zero the memory location, even if it is not subsequently written to. (The compiler can optimize away a call to <b>RtlZeroMemory</b>, if it determines that the caller does not access that memory range again.)</p>

<p>Use <b>RtlSecureZeroMemory</b> to guarantee that sensitive information has been zeroed out. For example, suppose that a function uses a local array variable to store password information. Once the function exits, the password information can remain in the same memory location unless zeroed out by <b>RtlSecureZeroMemory</b>.</p>

<p><b>RtlSecureZeroMemory</b> is slower than <b>RtlZeroMemory</b>; therefore, if security is not an issue, use <b>RtlZeroMemory</b> instead.</p>

<p>Callers of <b>RtlSecureZeroMemory</b> can be running at any IRQL if the <i>ptr</i> block is in nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2003 and later versions of Windows. (Because the routine is declared inline, the body of the routine can be included in earlier versions of the operating system.) </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlfillmemory.md">RtlFillMemory</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlzeromemory.md">RtlZeroMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlSecureZeroMemory routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
