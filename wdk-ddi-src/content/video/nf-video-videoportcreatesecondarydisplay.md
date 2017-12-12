---
UID: NF.video.VideoPortCreateSecondaryDisplay
title: VideoPortCreateSecondaryDisplay function
author: windows-driver-content
description: The VideoPortCreateSecondaryDisplay function enables dual-view support by creating a secondary device object for the given device.
old-location: display\videoportcreatesecondarydisplay.htm
old-project: display
ms.assetid: 49dc9ed8-a506-475e-910f-5dce2ad9b168
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
req.product: Windows 10 or later.
---

# VideoPortCreateSecondaryDisplay function



## -description
The <b>VideoPortCreateSecondaryDisplay</b> function enables dual-view support by creating a secondary device object for the given device.



## -syntax

````
VP_STATUS VideoPortCreateSecondaryDisplay(
  _In_    PVOID HwDeviceExtension,
  _Inout_ PVOID *SecondaryDeviceExtension,
  _In_    ULONG ulFlag
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the miniport driver's device extension. This is the hardware extension for the device that wants to create additional display device objects.


### -param SecondaryDeviceExtension [in, out]

Pointer to the location in which to store the hardware device extension for the secondary display device.


### -param ulFlag [in]

Is a set of attributes for the secondary display device. This parameter is restricted to the following value:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
VIDEO_DUALVIEW_REMOVABLE

</td>
<td>
The secondary view can be removed.

</td>
</tr>
</table>
 


## -returns
<b>VideoPortCreateSecondaryDisplay</b> returns NO_ERROR if the secondary display device was successfully created. Otherwise, this function returns an error code. 


## -remarks
In Windows XP and later, a removable logical device will never become the <a href="wdkgloss.p#wdkgloss.primary_display#wdkgloss.primary_display"><i>primary display</i></a>.

Note that on some editions of Windows XP, <b>VideoPortCreateSecondaryDisplay</b> can deliberately fail to enable Dualview. In such cases, the display driver should remain in SingleView mode.

When the video minport driver calls <b>VideoPortCreateSecondaryDisplay</b>, the value of the <i>ulFlags</i> parameter must be equal to VIDEO_DUALVIEW_REMOVABLE, which is defined in <i>ntddvdeo.h</i>.

The flags VIDEO_DUALVIEW_PRIMARY and VIDEO_DUALVIEW_SECONDARY, which are defined in <i>ntddvdeo.h</i>, are for internal use only. The video miniport driver must never set these flags. 


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
PASSIVE_LEVEL

</td>
</tr>
</table>