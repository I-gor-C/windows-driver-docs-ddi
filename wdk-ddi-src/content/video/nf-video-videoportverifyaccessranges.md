---
UID: NF.video.VideoPortVerifyAccessRanges
title: VideoPortVerifyAccessRanges function
author: windows-driver-content
description: The VideoPortVerifyAccessRanges function checks the registry for whether another driver has already claimed ownership of the specified bus-relative access ranges and any other hardware resources specified in the VIDEO_PORT_CONFIG_INFO structure.
old-location: display\videoportverifyaccessranges.htm
old-project: display
ms.assetid: 067ecebb-e63c-4161-9e8f-3746ecad3259
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: VideoPortVerifyAccessRanges
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
req.alt-api: VideoPortVerifyAccessRanges
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

# VideoPortVerifyAccessRanges function



## -description
The <b>VideoPortVerifyAccessRanges</b> function checks the registry for whether another driver has already claimed ownership of the specified bus-relative access ranges and any other hardware resources specified in the <a href="display.video_port_config_info">VIDEO_PORT_CONFIG_INFO</a> structure. If not, this function claims the given resources for the caller.


## -syntax

````
VP_STATUS VideoPortVerifyAccessRanges(
           PVOID               HwDeviceExtension,
           ULONG               NumAccessRanges,
  _In_opt_ PVIDEO_ACCESS_RANGE AccessRanges
);
````


## -parameters

### -param HwDeviceExtension 

Pointer to the miniport driver's device extension.

### -param NumAccessRanges 

Specifies the number of elements in the <i>AccessRanges</i> array, or zero.

### -param AccessRanges [in, optional]

Pointer to the miniport driver's access ranges array, or <b>NULL</b>. Each <a href="display.video_access_range">VIDEO_ACCESS_RANGE</a>-type element in this array specifies a bus-relative range of device memory, I/O ports, or register addresses for the adapter.

## -returns
<b>VideoPortVerifyAccessRanges</b> returns one of the following values:
<dl>
<dt><b>ERROR_INVALID_PARAMETER</b></dt>
</dl>An error occurred or a conflict was found; that is, another driver has already claimed one or more of the given hardware resources for its device.
<dl>
<dt><b>NO_ERROR</b></dt>
</dl>The given <i>AccessRanges</i> are valid and have been claimed for use by the caller.

 

## -remarks
Every video miniport driver either must call <b>VideoPortVerifyAccessRanges</b>, or use access ranges returned by <a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a> before attempting to access a video adapter during the driver (and system) initialization process.

<b>VideoPortVerifyAccessRanges</b> can be called only by a miniport driver's <a href="..\video\nc-video-pvideo_hw_find_adapter.md">HwVidFindAdapter</a> function.

Every video miniport driver must define the bus-relative access ranges for its device, either as statically allocated memory in the driver's header file or code or on the stack. Most miniport drivers set up their video access ranges on the stack, except for those that use PC standard address ranges for video memory, such as VGA-compatible SVGA miniport drivers.

The <i>HwVidFindAdapter</i> function should try to obtain bus-relative access range information by calling <a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a>, or by checking the registry through calls to <a href="display.videoportgetdevicedata">VideoPortGetDeviceData</a> or <a href="display.videoportgetregistryparameters">VideoPortGetRegistryParameters</a>. If <a href="..\video\nc-video-pvideo_hw_find_adapter.md">HwVidFindAdapter</a> cannot get this information, the miniport driver should have a set of bus-relative default values for access ranges.

If a miniport driver's access ranges are externally configurable, the installation program sets up access ranges for the adapter in the registry. Such a miniport driver's <i>HwVidFindAdapter</i> function can call <b>VideoPortGetRegistryParameters</b> with a miniport driver-supplied <a href="..\video\nc-video-pminiport_get_registry_routine.md">HwVidQueryNamedValueCallback</a> function that processes information retrieved from the registry.


<a href="..\video\nc-video-pvideo_hw_find_adapter.md">HwVidFindAdapter</a> must not pass any access range addresses to <a href="display.videoportgetdevicebase">VideoPortGetDeviceBase</a> unless it calls <b>VideoPortVerifyAccessRanges</b> or <a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a> first and the respective function returns NO_ERROR.

<b>VideoPortVerifyAccessRanges</b> can be called again if the initial <i>AccessRanges</i> specification or value in the <a href="display.video_port_config_info">VIDEO_PORT_CONFIG_INFO</a>, such as an interrupt vector, causes it to return an ERROR_<i>XXX</i> indicating that another driver has already claimed the resource(s).

If <b>VideoPortVerifyAccessRanges</b> returns NO_ERROR, a subsequent call for the same adapter overwrites the miniport driver's claim on resources for that adapter in the registry.

Note that a miniport driver cannot communicate with its video adapter, except by using mapped addresses returned by <a href="display.videoportgetdevicebase">VideoPortGetDeviceBase</a> with the <b>VideoPortRead/Write</b><i>Xxx</i> functions.

If the <a href="..\video\nc-video-pvideo_hw_find_adapter.md">HwVidFindAdapter</a> function claims bus-relative access ranges and possibly other hardware resources for an adapter but then determines that it does not support the adapter, the miniport driver must relinquish its claims on hardware resources in the registry by calling <b>VideoPortVerifyAccessRanges</b> or <a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a> with <i>NumAccessRanges</i> set to zero and <i>AccessRanges</i> set to <b>NULL</b>.

To relinquish claims on a subset of claimed access ranges that the miniport driver is no longer using, do the following:

Modify the <i>AccessRanges</i> specification for the adapter so that each element describing a range to be released still has <b>RangeStart</b> set to the bus-relative base of a claimed range, but <b>RangeLength</b> reset to zero.

Call <b>VideoPortVerifyAccessRanges</b> with this modified <i>AccessRanges</i> array.

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
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pvideo_hw_find_adapter.md">HwVidFindAdapter</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport_query_device_routine.md">HwVidQueryDeviceCallback</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport_get_registry_routine.md">HwVidQueryNamedValueCallback</a>
</dt>
<dt>
<a href="display.video_access_range">VIDEO_ACCESS_RANGE</a>
</dt>
<dt>
<a href="display.video_port_config_info">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="display.videoportgetaccessranges">VideoPortGetAccessRanges</a>
</dt>
<dt>
<a href="display.videoportgetdevicebase">VideoPortGetDeviceBase</a>
</dt>
<dt>
<a href="display.videoportgetdevicedata">VideoPortGetDeviceData</a>
</dt>
<dt>
<a href="display.videoportgetregistryparameters">VideoPortGetRegistryParameters</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortVerifyAccessRanges function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
