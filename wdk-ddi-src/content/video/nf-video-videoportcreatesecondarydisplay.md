---
UID: NF.video.VideoPortCreateSecondaryDisplay
title: VideoPortCreateSecondaryDisplay
author: windows-driver-content
description: The VideoPortCreateSecondaryDisplay function enables dual-view support by creating a secondary device object for the given device.
old-location: display\videoportcreatesecondarydisplay.htm
old-project: display
ms.assetid: 49dc9ed8-a506-475e-910f-5dce2ad9b168
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortCreateSecondaryDisplay
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
req.alt-api: VideoPortCreateSecondaryDisplay
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
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortCreateSecondaryDisplay function



## -description
<p>The <b>VideoPortCreateSecondaryDisplay</b> function enables dual-view support by creating a secondary device object for the given device.</p>


## -syntax

````
VP_STATUS VideoPortCreateSecondaryDisplay(
  _In_    PVOID HwDeviceExtension,
  _Inout_ PVOID *SecondaryDeviceExtension,
  _In_    ULONG ulFlag
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension. This is the hardware extension for the device that wants to create additional display device objects.</p>
</dd>

### -param <i>SecondaryDeviceExtension</i> [in, out]

<dd>
<p>Pointer to the location in which to store the hardware device extension for the secondary display device.</p>
</dd>

### -param <i>ulFlag</i> [in]

<dd>
<p>Is a set of attributes for the secondary display device. This parameter is restricted to the following value:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_DUALVIEW_REMOVABLE</p>
</td>
<td>
<p>The secondary view can be removed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>VideoPortCreateSecondaryDisplay</b> returns NO_ERROR if the secondary display device was successfully created. Otherwise, this function returns an error code. </p>

## -remarks
<p>In Windows XP and later, a removable logical device will never become the <a href="wdkgloss.p#wdkgloss.primary_display#wdkgloss.primary_display"><i>primary display</i></a>.</p>

<p>Note that on some editions of Windows XP, <b>VideoPortCreateSecondaryDisplay</b> can deliberately fail to enable Dualview. In such cases, the display driver should remain in SingleView mode.</p>

<p>When the video minport driver calls <b>VideoPortCreateSecondaryDisplay</b>, the value of the <i>ulFlags</i> parameter must be equal to VIDEO_DUALVIEW_REMOVABLE, which is defined in <i>ntddvdeo.h</i>.</p>

<p>The flags VIDEO_DUALVIEW_PRIMARY and VIDEO_DUALVIEW_SECONDARY, which are defined in <i>ntddvdeo.h</i>, are for internal use only. The video miniport driver must never set these flags. </p>

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
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
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