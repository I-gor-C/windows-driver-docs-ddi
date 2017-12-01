---
UID: NC.video.PVIDEO_HW_INITIALIZE
title: PVIDEO_HW_INITIALIZE
author: windows-driver-content
description: HwVidInitialize performs the first initialization of the adapter, after the HAL has given up control of the video hardware to the video port driver.
old-location: display\hwvidinitialize.htm
old-project: display
ms.assetid: 0e43de21-59e5-4368-8ea2-34fa52e99950
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwVidInitialize
req.alt-loc: video.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PVIDEO_HW_INITIALIZE callback



## -description
<p><i>HwVidInitialize</i> performs the first initialization of the adapter, after the HAL has given up control of the video hardware to the video port driver.</p>


## -prototype

````
PVIDEO_HW_INITIALIZE HwVidInitialize;

BOOLEAN HwVidInitialize(
   PVOID HwDeviceExtension
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's per-adapter storage area. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543119">Device Extensions</a>.</p>
</dd>
</dl>

## -returns
<p>If the initialization succeeds, <i>HwVidInitialize</i> returns <b>TRUE</b>.</p>

## -remarks
<p>Every video miniport driver must have a <i>HwVidInitialize</i> function.</p>

<p>The video port driver calls <i>HwVidInitialize</i> in response to an open request by the corresponding display driver. As soon as <i>HwVidInitialize</i> is called, the miniport driver can change the state of the adapter, unlike the miniport driver's <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a> function, which must leave the adapter in VGA mode. On return from <i>HwVidInitialize</i>, the adapter must be initialized to a state equivalent to that set up by the miniport driver's <a href="..\video\nc-video-pvideo-hw-reset-hw.md">HwVidResetHw</a> function. This feature is used by autodetection to get mode information from the miniport driver.</p>

<p>If at all possible, <i>HwVidInitialize</i> should avoid programming the device hardware. The miniport driver will initialize the device later, when it is instructed to switch display modes.</p>

<p><i>HwVidInitialize</i> should be made pageable.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-reset-hw.md">HwVidResetHw</a>
</dt>
<dt>
<a href="display.drvassertmode">DrvAssertMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PVIDEO_HW_INITIALIZE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
