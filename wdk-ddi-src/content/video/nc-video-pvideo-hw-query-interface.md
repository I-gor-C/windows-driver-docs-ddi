---
UID: NC.video.PVIDEO_HW_QUERY_INTERFACE
title: PVIDEO_HW_QUERY_INTERFACE
author: windows-driver-content
description: HwVidQueryInterface returns a miniport driver-implemented functional interface that a child device can call.
old-location: display\hwvidqueryinterface.htm
old-project: display
ms.assetid: f16a7fa3-3471-4ccb-b1b4-982d33f930d3
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
req.alt-api: HwVidQueryInterface
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

# PVIDEO_HW_QUERY_INTERFACE callback



## -description
<p><i>HwVidQueryInterface</i> returns a miniport driver-implemented functional interface that a child device can call.</p>


## -prototype

````
PVIDEO_HW_QUERY_INTERFACE HwVidQueryInterface;

VP_STATUS HwVidQueryInterface(
   PVOID            HwDeviceExtension,
   PQUERY_INTERFACE QueryInterface
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's per-adapter storage area. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543119">Device Extensions</a>.</p>
</dd>

### -param <i>QueryInterface</i> 

<dd>
<p>Pointer to a <a href="..\video\ns-video--query-interface.md">QUERY_INTERFACE</a> structure in which the miniport driver should return information about the interface it supports.</p>
</dd>
</dl>

## -returns
<p><i>HwVidQueryInterface</i> should return NO_ERROR upon success; otherwise it should return the appropriate error code. For example, a miniport driver should return ERROR_OUTOFMEMORY if it cannot allocate memory to complete the operation.</p>

## -remarks
<p><i>HwVidQueryInterface</i> exposes a communication mechanism between the video miniport driver and the driver of a child device. A miniport driver that exposes such a mechanism should implement this function.</p>

<p>The video port calls <i>HwVidQueryInterface</i> when it receives an IRP_MN_QUERY_INTERFACE request. If the miniport driver fails the call, the video port driver passes the request to the parent of the miniport driver's device.</p>

<p><i>HwVidQueryInterface</i> should fill in the members of the <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure to which <i>QueryInterface</i>-&gt;<b>Interface</b> points as follows:</p>

<p>Set <b>Size</b> to the number of bytes in the INTERFACE structure. This value must not exceed the number of bytes specified by <i>QueryInterface</i>-&gt;<b>Size</b>.</p>

<p>Set <b>Version</b> to the version of the interface being returned by the miniport driver. The miniport driver should best match the version requested by the child driver in <i>QueryInterface</i>-&gt;<b>Version</b>.</p>

<p>Set <b>Context</b> to point to a miniport driver-defined context for the interface. Typically, a miniport driver would set <b>Context</b> to point to the device extension identified by <i>HwDeviceExtension</i>.</p>

<p>Initialize <b>InterfaceReference</b> and <b>InterfaceDereference</b> to point to the miniport driver-implemented reference and dereference routines for this interface.</p>

<p>Initialize all additional interface-specific members to point to the appropriate routines of the interface being exposed.</p>

<p>A miniport driver that returns an interface is responsible for referencing the interface by calling <i>QueryInterface</i>-&gt;<b>Interface.InterfaceReference</b>. The child driver requesting the interface is responsible for dereferencing it when the driver no longer requires the interface by calling <i>QueryInterface</i>-&gt;<b>Interface.InterfaceDereference</b>. If the child driver passes the interface to another component, the child is responsible for taking out another reference, and the other component is responsible for removing the additional reference when it no longer needs access to the interface. Referencing allows a parent to determine when the interface is still required by the child device, and consequently when the parent can free any interface-associated resources.</p>

<p>The driver of a child device can call into the miniport driver through the functions exposed by <i>HwVidQueryInterface</i> at any time without the video port driver's knowledge. Consequently, the miniport driver must synchronize access to itself by acquiring and releasing the video port driver-maintained device lock in all of the functions exposed by <i>HwVidQueryInterface</i>.</p>

<p>A child device is enumerated by <a href="..\video\nc-video-pvideo-hw-get-child-descriptor.md">HwVidGetVideoChildDescriptor</a>.</p>

<p><i>HwVidQueryInterface</i> should be made pageable.</p>

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
<a href="..\video\ns-video--query-interface.md">QUERY_INTERFACE</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-get-child-descriptor.md">HwVidGetVideoChildDescriptor</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportacquiredevicelock.md">VideoPortAcquireDeviceLock</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportreleasedevicelock.md">VideoPortReleaseDeviceLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PVIDEO_HW_QUERY_INTERFACE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
