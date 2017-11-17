---
UID: NF.video.VideoPortFreeCommonBuffer
title: VideoPortFreeCommonBuffer
author: windows-driver-content
description: The VideoPortFreeCommonBuffer function is obsolete and is supported only for backward compatibility with existing drivers.
old-location: display\videoportfreecommonbuffer.htm
ms.assetid: 8725868e-00bc-45fe-ab9d-c192abd1a059
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
req.alt-api: VideoPortFreeCommonBuffer
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
req.irql: PASSIVE_LEVEL
ms.keywords: VideoPortFreeCommonBuffer
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortFreeCommonBuffer function



## -description
<p>The <b>VideoPortFreeCommonBuffer</b> function is <b>obsolete</b> and is supported only for backward compatibility with existing drivers. In its place, driver writers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff570355">VideoPortReleaseCommonBuffer</a>.</p>
<p><b>VideoPortFreeCommonBuffer</b> deallocates system memory that was allocated by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570308">VideoPortGetCommonBuffer</a>.</p>


## -syntax

````
VOID VideoPortFreeCommonBuffer(
  _In_ PVOID            HwDeviceExtension,
  _In_ ULONG            Length,
  _In_ PVOID            VirtualAddress,
  _In_ PHYSICAL_ADDRESS LogicalAddress,
  _In_ BOOLEAN          CacheEnabled
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the number of bytes of memory to be freed.</p>
</dd>

### -param <i>VirtualAddress</i> [in]

<dd>
<p>Pointer to the corresponding virtual address of the allocated memory range.</p>
</dd>

### -param <i>LogicalAddress</i> [in]

<dd>
<p>Specifies the logical address of the buffer to be freed.</p>
</dd>

### -param <i>CacheEnabled</i> [in]

<dd>
<p>Indicates whether the allocated memory is cached.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Except for <a href="https://msdn.microsoft.com/c8329d26-fb6f-46f1-aacd-ba78ee4ea5d5">VideoPortGetCommonBuffer's </a><i>Alignment</i> parameter, all of the parameters used in a call to <b>VideoPortFreeCommonBuffer</b> must have the same values as those used in the previous call to <b>VideoPortGetCommonBuffer</b>.</p>

<p>Except for <a href="https://msdn.microsoft.com/c8329d26-fb6f-46f1-aacd-ba78ee4ea5d5">VideoPortGetCommonBuffer's </a><i>Alignment</i> parameter, all of the parameters used in a call to <b>VideoPortFreeCommonBuffer</b> must have the same values as those used in the previous call to <b>VideoPortGetCommonBuffer</b>.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570355">VideoPortReleaseCommonBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570308">VideoPortGetCommonBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortFreeCommonBuffer function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
