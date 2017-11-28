---
UID: NF.video.VideoPortLockPages
title: VideoPortLockPages
author: windows-driver-content
description: The VideoPortLockPages function is obsolete in Windows 2000 and later. Use VideoPortLockBuffer in place of this function.VideoPortLockPages locks the specified virtual memory and possibly performs part or all of a DMA transfer.
old-location: display\videoportlockpages.htm
old-project: display
ms.assetid: f5e06ff3-98ba-4443-8ea6-c32b063cd478
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortLockPages
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortLockPages
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
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortLockPages function



## -description
<p>The <b>VideoPortLockPages</b> function is <b>obsolete</b> in Windows 2000 and later. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff570326">VideoPortLockBuffer</a> in place of this function.</p>
<p><b>VideoPortLockPages</b> locks the specified virtual memory and possibly performs part or all of a DMA transfer.</p>


## -syntax

````
BOOLEAN VideoPortLockPages(
  _In_    PVOID                 HwDeviceExtension,
  _Inout_ PVIDEO_REQUEST_PACKET pVrp,
  _In_    PEVENT                pUEvent,
  _In_    PEVENT                pDisplayEvent,
  _In_    DMA_FLAGS             DmaFlags
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>pVrp</i> [in, out]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a> structure. The miniport driver must have set <b>InputBuffer</b> and <b>InputBufferLength</b> to contain the virtual address and the size in bytes, respectively, of the memory to be locked for the transfer. This memory was allocated by the display driver and passed to the miniport driver through an IOCTL. The video port returns a pointer to and the size in bytes of the scatter/gather list in <b>OutputBuffer</b> and <b>OutputBufferLength</b>, respectively.</p>
</dd>

### -param <i>pUEvent</i> [in]

<dd>
<p>Pointer to a mapped user event that is to be set by the miniport driver, or <b>NULL</b>. The user event was mapped by the display driver and passed to the miniport driver through an IOCTL.</p>
</dd>

### -param <i>pDisplayEvent</i> [in]

<dd>
<p>Pointer to an event that is to be set by the miniport driver, or <b>NULL</b>. This event was created by and received from the display driver through an IOCTL.</p>
</dd>

### -param <i>DmaFlags</i> [in]

<dd>
<p>Specifies the action to be performed. This parameter must be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>VideoPortDmaInitOnly</b></p>
</td>
<td>
<p><b>VideoPortLockPages</b> locks the requested memory.</p>
</td>
</tr>
<tr>
<td>
<p><b>VideoPortKeepPagesLocked</b></p>
</td>
<td>
<p><b>VideoPortLockPages</b> takes no action.</p>
</td>
</tr>
<tr>
<td>
<p><b>VideoPortUnlockAfterDma</b></p>
</td>
<td>
<p><b>VideoPortLockPages</b> takes no action.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>VideoPortLockPages</b> returns <b>TRUE</b> upon successful completion of the action requested of it. It returns <b>FALSE</b> if the <i>DmaFlags</i> parameter is not equal to <b>VideoPortDmaInitOnly</b>.</p>

## -remarks
<p>See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.</p>

<p><b>VideoPortLockPages</b> cannot be called from an ISR or DPC.</p>

<p>See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.</p>

<p><b>VideoPortLockPages</b> cannot be called from an ISR or DPC.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570326">VideoPortLockBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortLockPages function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
