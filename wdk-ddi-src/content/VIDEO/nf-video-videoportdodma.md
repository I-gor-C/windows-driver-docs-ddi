---
UID: NF.video.VideoPortDoDma
title: VideoPortDoDma
author: windows-driver-content
description: The VideoPortDoDma function is obsolete in Windows 2000 and later. VideoPortDoDma causes the miniport driver's HwVidStartDma function to be called.
old-location: display\videoportdodma.htm
ms.assetid: a827df55-ff88-439a-8d56-fba8212105a6
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
req.alt-api: VideoPortDoDma
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
req.irql: 
ms.keywords: VideoPortDoDma
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortDoDma function



## -description
<p>The <b>VideoPortDoDma</b> function is <b>obsolete</b> in Windows 2000 and later. </p>
<p><b>VideoPortDoDma</b> causes the miniport driver's <i>HwVidStartDma</i> function to be called.</p>


## -syntax

````
PDMA VideoPortDoDma(
  _In_ PVOID     HwDeviceExtension,
  _In_ PDMA      pDma,
  _In_ DMA_FLAGS DmaFlags
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>pDma</i> [in]

<dd>
<p>Specifies a non-<b>NULL</b> DMA handle. This handle was obtained from a prior call to <b>VideoPortDoDma</b> or from the <b>OutputBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a> returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff570327">VideoPortLockPages</a>.</p>
</dd>

### -param <i>DmaFlags</i> [in]

<dd>
<p>Specifies the action to be performed. This member can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>VideoPortKeepPagesLockedVideoPortDmaInitOnly</b></p>
</td>
<td>
<p>If possible, the video port driver should keep the memory locked for subsequent DMA operation(s).</p>
</td>
</tr>
<tr>
<td>
<p><b>VideoPortUnlockAfterDma</b></p>
</td>
<td>
<p>The video port driver should unlock the memory after the DMA operation is performed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>VideoPortDoDma</b> always returns <b>NULL</b>.</p>

## -remarks
<p>See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.</p>

<p>See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570327">VideoPortLockPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortDoDma function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
