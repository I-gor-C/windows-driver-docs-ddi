---
UID: NF.video.VideoPortCompareMemory
title: VideoPortCompareMemory
author: windows-driver-content
description: The VideoPortCompareMemory function compares two blocks of system memory, byte-by-byte, and returns the number of compared bytes that are equivalent.
old-location: display\videoportcomparememory.htm
ms.assetid: 89528b31-4d81-4612-92d7-5f64bdca8108
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortCompareMemory
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: Any level (see Remarks section)
ms.keywords: VideoPortCompareMemory
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortCompareMemory function



## -description
<p>The <b>VideoPortCompareMemory</b> function compares two blocks of system memory, byte-by-byte, and returns the number of compared bytes that are equivalent.</p>


## -syntax

````
ULONG VideoPortCompareMemory(
   PVOID  Source1,
   PVOID  Source2,
   SIZE_T Length
);
````


## -parameters
<dl>

### -param <i>Source1</i> 

<dd>
<p>Pointer to the first block of memory to compare.</p>
</dd>

### -param <i>Source2</i> 

<dd>
<p>Pointer to the second block of memory to compare.</p>
</dd>

### -param <i>Length</i> 

<dd>
<p>Specifies the number of bytes to be compared.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortCompareMemory</b> returns the number of bytes that are equivalent. If both blocks are equivalent, it returns the <i>Length</i> parameter.</p>

## -remarks
<p>The values in the <i>Source1</i> and <i>Source2</i> parameters must be in a mapped logical range returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a> and/or a <a href="wdkgloss.s#wdkgloss.system_space#wdkgloss.system_space"><i>system space</i></a> RAM address, such as an address on the stack.</p>

<p>Callers of <b>VideoPortCompareMemory</b> can be running at any IRQL if both blocks of memory are resident.</p>

<p>The values in the <i>Source1</i> and <i>Source2</i> parameters must be in a mapped logical range returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a> and/or a <a href="wdkgloss.s#wdkgloss.system_space#wdkgloss.system_space"><i>system space</i></a> RAM address, such as an address on the stack.</p>

<p>Callers of <b>VideoPortCompareMemory</b> can be running at any IRQL if both blocks of memory are resident.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570332">VideoPortMoveMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570360">VideoPortScanRom</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570492">VideoPortZeroDeviceMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570493">VideoPortZeroMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortCompareMemory function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
