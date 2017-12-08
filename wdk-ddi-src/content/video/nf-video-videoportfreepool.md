---
UID: NF.video.VideoPortFreePool
title: VideoPortFreePool function
author: windows-driver-content
description: The VideoPortFreePool function deallocates a block of pool memory previously allocated by VideoPortAllocatePool.
old-location: display\videoportfreepool.htm
old-project: display
ms.assetid: 84e4f178-87d3-4f40-b4fc-7959818305fd
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: VideoPortFreePool
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortFreePool
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
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# VideoPortFreePool function



## -description
The <b>VideoPortFreePool</b> function deallocates a block of pool memory previously allocated by <a href="display.videoportallocatepool">VideoPortAllocatePool</a>.


## -syntax

````
VOID VideoPortFreePool(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID Ptr
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the miniport driver's device extension.

### -param Ptr [in]

Pointer to the first byte of the memory to be freed.

## -returns
None

## -remarks
<b>VideoPortFreePool</b> is intended to replace <b>VideoPortReleaseBuffer</b>, which is obsolete.

Callers of <b>VideoPortFreePool</b> must be running at IRQL &lt;= DISPATCH_LEVEL. A caller at DISPATCH_LEVEL must have specified a <b>VpNonPaged </b><i>XxxPoolType</i> when the memory was allocated. Otherwise, the caller must be running at IRQL &lt; DISPATCH_LEVEL.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows XP and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
See Remarks section.
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.videoportallocatepool">VideoPortAllocatePool</a>
</dt>
<dt>
<a href="display.videoportallocatecommonbuffer">VideoPortAllocateCommonBuffer</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortFreePool function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
