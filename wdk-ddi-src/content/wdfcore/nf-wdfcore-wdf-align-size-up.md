---
UID: NF.wdfcore.WDF_ALIGN_SIZE_UP
title: WDF_ALIGN_SIZE_UP
author: windows-driver-content
description: The WDF_ALIGN_SIZE_UP function returns the next-higher buffer size that is aligned to a specified alignment offset.
old-location: wdf\wdf_align_size_up.htm
old-project: wdf
ms.assetid: 68523004-c9f5-4038-985e-702d929cdf04
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_ALIGN_SIZE_UP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcore.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_ALIGN_SIZE_UP
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: Any IRQL.
req.iface: 
req.product: Windows 10 or later.
---

# WDF_ALIGN_SIZE_UP function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_ALIGN_SIZE_UP</b> function returns the next-higher buffer size that is aligned to a specified alignment offset.</p>


## -syntax

````
size_t WDF_ALIGN_SIZE_UP(
  _In_ size_t Length,
  _In_ size_t AlignTo
);
````


## -parameters
<dl>

### -param <i>Length</i> [in]

<dd>
<p>The length, in bytes, of a <a href="wdf.using_memory_buffers">memory buffer</a>.</p>
</dd>

### -param <i>AlignTo</i> [in]

<dd>
<p>The alignment offset, in bytes. This value must be a power of 2, such as 2, 4, 8, 16, and so on.</p>
</dd>
</dl>

## -returns
<p><b>WDF_ALIGN_SIZE_UP</b> returns the aligned buffer size, in bytes.</p>

## -remarks
<p>Drivers can use <b>WDF_ALIGN_SIZE_UP</b> or <a href="..\wdfcore\nf-wdfcore-wdf-align-size-down.md">WDF_ALIGN_SIZE_DOWN</a> to calculate a buffer size that is aligned to a specified alignment offset. This calculation is useful if your driver must allocate multiple contiguous buffers, if each buffer must begin at an address alignment boundary.</p>

<p>If the value of either input parameter is too large, arithmetic overflow causes <b>WDF_ALIGN_SIZE_UP</b> to return an invalid value that is smaller than <i>Length</i>. Your code should test for this condition.</p>

<p>The following code example receives a buffer size and returns the size (either the current size or the next-higher size) that aligns to a DWORD address boundary.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcore.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any IRQL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfcore\nf-wdfcore-wdf-align-size-down.md">WDF_ALIGN_SIZE_DOWN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_ALIGN_SIZE_UP function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
