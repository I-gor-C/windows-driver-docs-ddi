---
UID: NF.video.VideoPortUnlockPages
title: VideoPortUnlockPages function
author: windows-driver-content
description: The VideoPortUnlockPages function is obsolete in Windows 2000 and later. Use VideoPortUnlockBuffer in place of this function.VideoPortUnlockPages releases memory used for packet-based DMA.
old-location: display\videoportunlockpages.htm
old-project: display
ms.assetid: c233d4e1-285c-4f74-bb37-808cf855b19c
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: VideoPortUnlockPages
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
req.alt-api: VideoPortUnlockPages
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
req.product: Windows 10 or later.
---

# VideoPortUnlockPages function



## -description
The <b>VideoPortUnlockPages</b> function is <b>obsolete</b> in Windows 2000 and later. Use <a href="display.videoportunlockbuffer">VideoPortUnlockBuffer</a> in place of this function.

<b>VideoPortUnlockPages</b> releases memory used for packet-based DMA.



## -syntax

````
BOOLEAN VideoPortUnlockPages(
   PVOID hwDeviceExtension,
   PDMA  pDma
);
````


## -parameters

### -param hwDeviceExtension 

Pointer to the miniport driver's device extension.


### -param pDma 

Specifies a non-<b>NULL</b> DMA handle. 


## -returns
<b>VideoPortUnlockPages</b> always returns <b>TRUE</b>.


## -remarks
See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.

This function can be called only within the context of a DMA IOCTL. It cannot be called from an ISR or DPC.


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
Available in Windows 2000 and later versions of the Windows operating systems.

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
</table>

## -see-also
<dl>
<dt>
<a href="display.videoportunlockbuffer">VideoPortUnlockBuffer</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortUnlockPages function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

