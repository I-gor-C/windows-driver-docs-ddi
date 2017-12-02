---
UID: NF.wdm.RtlEqualMemory
title: RtlEqualMemory
author: windows-driver-content
description: The RtlEqualMemory routine compares two blocks of memory to determine whether the specified number of bytes are identical.
old-location: kernel\rtlequalmemory.htm
old-project: kernel
ms.assetid: 43695fa9-32e1-4bd5-b146-88d6d03fe9fb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlEqualMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlEqualMemory
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

# RtlEqualMemory function



## -description
<p>The <b>RtlEqualMemory</b> routine compares two blocks of memory to determine whether the specified number of bytes are identical. </p>


## -syntax

````
LOGICAL RtlEqualMemory(
  _In_ const VOID   *Source1,
  _In_ const VOID   *Source2,
  _In_       SIZE_T Length
);
````


## -parameters
<dl>

### -param Source1 [in]

<dd>
<p>Pointer to a caller-allocated block of memory to compare. </p>
</dd>

### -param Source2 [in]

<dd>
<p>Pointer to a caller-allocated block of memory that is compared to the block of memory to which <i>Source1</i> points. </p>
</dd>

### -param Length [in]

<dd>
<p>Specifies the number of bytes to be compared. </p>
</dd>
</dl>

## -returns
<p><b>RtlEqualMemory</b> returns <b>TRUE</b> if <i>Source1</i> and <i>Source2</i> are equivalent; otherwise, it returns <b>FALSE</b>. </p>

## -remarks
<p><b>RtlEqualMemory</b> begins the comparison with byte zero of each block.</p>

<p>Callers of <b>RtlEqualMemory</b> can be running at any IRQL if both blocks of memory are resident.</p>

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
<p>Available starting with Windows 2000.</p>
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
<a href="..\wdm\nf-wdm-rtlcomparememory.md">RtlCompareMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlEqualMemory routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
