---
UID: NC.video.PVIDEO_HW_GET_CHILD_DESCRIPTOR
title: PVIDEO_HW_GET_CHILD_DESCRIPTOR
author: windows-driver-content
description: HwVidGetVideoChildDescriptor returns a descriptor, a type, and an identification number for a particular child device of the display adapter.
old-location: display\hwvidgetvideochilddescriptor.htm
old-project: display
ms.assetid: 175030c1-95d9-4a3b-976c-16e04852cb91
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
req.alt-api: HwVidGetVideoChildDescriptor
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

# PVIDEO_HW_GET_CHILD_DESCRIPTOR callback



## -description
<p><i>HwVidGetVideoChildDescriptor</i> returns a descriptor, a type, and an identification number for a particular child device of the display adapter.</p>


## -prototype

````
PVIDEO_HW_GET_CHILD_DESCRIPTOR HwVidGetVideoChildDescriptor;

VP_STATUS HwVidGetVideoChildDescriptor(
  _In_  PVOID                  HwDeviceExtension,
  _In_  PVIDEO_CHILD_ENUM_INFO ChildEnumInfo,
  _Out_ PVIDEO_CHILD_TYPE      VideoChildType,
  _Out_ PUCHAR                 pChildDescriptor,
  _Out_ PULONG                 UId,
  _Out_ PULONG                 pUnused
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's per-adapter storage area. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543119">Device Extensions</a>.</p>
</dd>

### -param <i>ChildEnumInfo</i> [in]

<dd>
<p>Is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570499">VIDEO_CHILD_ENUM_INFO</a> structure that describes the device being enumerated.</p>
</dd>

### -param <i>VideoChildType</i> [out]

<dd>
<p>Pointer to a location in which the miniport driver returns the type of child being enumerated. This member can be one of the following from the VIDEO_CHILD_TYPE enumeration:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>Monitor</b></p>
</td>
<td>
<p>The child device is a monitor.</p>
<p>If the miniport driver detects that the monitor has a DDC2-compliant <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> structure associated with it, the miniport driver should extract the EDID information from the monitor and return it in the buffer to which <i>pChildDescriptor</i> points. The miniport driver can more easily obtain the EDID from the monitor by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff570290">VideoPortDDCMonitorHelper</a>.</p>
<p>If the detected monitor is not DDC2-compliant, the miniport driver should not return anything in <i>pChildDescriptor</i>.</p>
</td>
</tr>
<tr>
<td>
<p><b>NonPrimaryChip</b></p>
</td>
<td>
<p>Is reserved for system use.</p>
</td>
</tr>
<tr>
<td>
<p><b>VideoChip</b></p>
</td>
<td>
<p>The child device is the graphics chip.</p>
<p>The miniport driver should return this type when <i>ChildEnumInfo</i>.<b>ChildIndex</b> is DISPLAY_ADAPTER_HW_ID. The miniport driver should not return anything in <i>pChildDescriptor</i>.</p>
</td>
</tr>
<tr>
<td>
<p><b>Other</b></p>
</td>
<td>
<p>The child device has a separate device driver associated with it.</p>
<p>The miniport driver should return the device's PnP hardware identifier as a Unicode string in the buffer to which <i>pChildDescriptor</i> points. This string must match the <a href="wdkgloss.d#wdkgloss.device_id#wdkgloss.device_id"><i>device ID</i></a> specified in the driver's INF file. It will be used by the operating system as the hardware ID for this device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pChildDescriptor</i> [out]

<dd>
<p>Pointer to a buffer in which the miniport driver can return data that identifies the device. The information returned depends on the child type specified in <i>VideoChildType</i>. The size of this buffer is specified by the video port driver in the <b>ChildDescriptorSize</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570499">VIDEO_CHILD_ENUM_INFO</a>.</p>
</dd>

### -param <i>UId</i> [out]

<dd>
<p>Pointer to the location in which the miniport driver returns a unique 32-bit <a href="wdkgloss.d#wdkgloss.device_id#wdkgloss.device_id"><i>device ID</i></a> for this device. The miniport driver should set <i>UId</i> to be DISPLAY_ADAPTER_HW_ID when the device is the actual display adapter.</p>
</dd>

### -param <i>pUnused</i> [out]

<dd>
<p>Is unused and must be set to zero.</p>
</dd>
</dl>

## -returns
<p><i>HwVidGetVideoChildDescriptor</i> returns one of the following values:</p><dl>
<dt><b>VIDEO_ENUM_INVALID_DEVICE</b></dt>
</dl><p>Call again. The miniport driver could not enumerate the child device identified in <i>ChildEnumInfo</i> but there are more devices to be enumerated. </p><dl>
<dt><b>VIDEO_ENUM_MORE_DEVICES</b></dt>
</dl><p>A new child device is enumerated. The video port will call <i>HwVidGetVideoChildDescriptor</i> again in this case.</p><dl>
<dt><b>VIDEO_ENUM_NO_MORE_DEVICES</b></dt>
</dl><p>The miniport driver could not enumerate the child device identified in <i>ChildEnumInfo</i>. Stop enumeration. There are no more devices to be enumerated. </p>

<p> </p>

## -remarks
<p>By default, <i>HwVidGetVideoChildDescriptor</i> is not called until after the device is started by <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a>. To allow the enumeration of a device's children before the device is started, set the <b>AllowEarlyEnumeration</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a>. When <b>AllowEarlyEnumeration</b> is set, <i>HwVidGetVideoChildDescriptor</i> can be called at any time.</p>

<p><i>HwVidGetVideoChildDescriptor</i> should do the following:</p>

<p>Determine the type of the child device based on the data supplied in <i>ChildEnumInfo</i>, and return this type in <i>VideoChildType</i>.</p>

<p>Fill in the buffer to which <i>pChildDescriptor</i> points with the appropriate data, depending on the value of <i>VideoChildType</i>.</p>

<p>Write a 32-bit value in <i>UId</i> that uniquely identifies the child device being enumerated. The video port driver will pass this handle back to the miniport driver for operations such as power management.</p>

<p><i>HwVidGetVideoChildDescriptor</i> should be made pageable.</p>

<p>By default, <i>HwVidGetVideoChildDescriptor</i> is not called until after the device is started by <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a>. To allow the enumeration of a device's children before the device is started, set the <b>AllowEarlyEnumeration</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a>. When <b>AllowEarlyEnumeration</b> is set, <i>HwVidGetVideoChildDescriptor</i> can be called at any time.</p>

<p><i>HwVidGetVideoChildDescriptor</i> should do the following:</p>

<p>Determine the type of the child device based on the data supplied in <i>ChildEnumInfo</i>, and return this type in <i>VideoChildType</i>.</p>

<p>Fill in the buffer to which <i>pChildDescriptor</i> points with the appropriate data, depending on the value of <i>VideoChildType</i>.</p>

<p>Write a 32-bit value in <i>UId</i> that uniquely identifies the child device being enumerated. The video port driver will pass this handle back to the miniport driver for operations such as power management.</p>

<p><i>HwVidGetVideoChildDescriptor</i> should be made pageable.</p>

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
<a href="..\video\nc-video-pvideo-hw-power-get.md">HwVidGetPowerState</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-power-set.md">HwVidSetPowerState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570499">VIDEO_CHILD_ENUM_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570290">VideoPortDDCMonitorHelper</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570297">VideoPortEnumerateChildren</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PVIDEO_HW_GET_CHILD_DESCRIPTOR callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
