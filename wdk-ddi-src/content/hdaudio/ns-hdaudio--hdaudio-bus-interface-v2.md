---
UID: NS.hdaudio._HDAUDIO_BUS_INTERFACE_V2
title: HDAUDIO_BUS_INTERFACE_V2
author: windows-driver-content
description: The HDAUDIO_BUS_INTERFACE_V2 structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE_V2 version of the HD Audio DDI.
old-location: audio\hdaudio_bus_interface_v2.htm
old-project: audio
ms.assetid: 7d639909-dc56-4ec5-b596-bfbbf262a3d9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HDAUDIO_BUS_INTERFACE_V2, HDAUDIO_BUS_INTERFACE_V2, *PHDAUDIO_BUS_INTERFACE_V2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HDAUDIO_BUS_INTERFACE_V2
req.alt-loc: hdaudio.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL.
req.iface: 
---

# HDAUDIO_BUS_INTERFACE_V2 structure



## -description
<p>The HDAUDIO_BUS_INTERFACE_V2 structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE_V2 version of the HD Audio DDI. The interface represented by this structure provides all the functionality of <a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface.md">HDAUDIO_BUS_INTERFACE</a> and can also support flexible DMA-driven event notification.</p>


## -syntax

````
typedef struct _HDAUDIO_BUS_INTERFACE_V2 {
  USHORT                                 Size;
  USHORT                                 Version;
  PVOID                                  Context;
  PINTERFACE_REFERENCE                   InterfaceReference;
  PINTERFACE_DEREFERENCE                 InterfaceDereference;
  PTRANSFER_CODEC_VERBS                  TransferCodecVerbs;
  PALLOCATE_CAPTURE_DMA_ENGINE           AllocateCaptureDmaEngine;
  PALLOCATE_RENDER_DMA_ENGINE            AllocateRenderDmaEngine;
  PCHANGE_BANDWIDTH_ALLOCATION           ChangeBandwidthAllocation;
  PALLOCATE_DMA_BUFFER                   AllocateDmaBuffer;
  PFREE_DMA_BUFFER                       FreeDmaBuffer;
  PFREE_DMA_ENGINE                       FreeDmaEngine;
  PSET_DMA_ENGINE_STATE                  SetDmaEngineState;
  PGET_WALL_CLOCK_REGISTER               GetWallClockRegister;
  PGET_LINK_POSITION_REGISTER            GetLinkPositionRegister;
  PREGISTER_EVENT_CALLBACK               RegisterEventCallback;
  PUNREGISTER_EVENT_CALLBACK             UnregisterEventCallback;
  PGET_DEVICE_INFORMATION                GetDeviceInformation;
  PGET_RESOURCE_INFORMATION              GetResourceInformation;
  PALLOCATE_DMA_BUFFER_WITH_NOTIFICATION AllocateDmaBufferWithNotification;
  PFREE_DMA_BUFFER_WITH_NOTIFICATION     FreeDmaBufferWithNotification;
  PREGISTER_NOTIFICATION_EVENT           RegisterNotificationEvent;
  PUNREGISTER_NOTIFICATION_EVENT         UnregisterNotificationEvent;
} HDAUDIO_BUS_INTERFACE_V2, *PHDAUDIO_BUS_INTERFACE_V2;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of the HDAUDIO_BUS_INTERFACE_V2 structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the baseline HD Audio DDI.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to interface-specific context information.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>A pointer to a driver-supplied routine that increments the reference count for the interface.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>A pointer to a driver-supplied routine that decrements the reference count for the interface.</p>
</dd>

### -field <b>TransferCodecVerbs</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-ptransfer-codec-verbs.md">TransferCodecVerbs</a> routine.</p>
</dd>

### -field <b>AllocateCaptureDmaEngine</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a> routine.</p>
</dd>

### -field <b>AllocateRenderDmaEngine</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a> routine.</p>
</dd>

### -field <b>ChangeBandwidthAllocation</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pchange-bandwidth-allocation.md">ChangeBandwidthAllocation</a> routine.</p>
</dd>

### -field <b>AllocateDmaBuffer</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer.md">AllocateDmaBuffer</a> routine.</p>
</dd>

### -field <b>FreeDmaBuffer</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer.md">FreeDmaBuffer</a> routine.</p>
</dd>

### -field <b>FreeDmaEngine</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pfree-dma-engine.md">FreeDmaEngine</a> routine.</p>
</dd>

### -field <b>SetDmaEngineState</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pset-dma-engine-state.md">SetDmaEngineState</a> routine.</p>
</dd>

### -field <b>GetWallClockRegister</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pget-wall-clock-register.md">GetWallClockRegister</a> routine.</p>
</dd>

### -field <b>GetLinkPositionRegister</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pget-link-position-register.md">GetLinkPositionRegister</a> routine.</p>
</dd>

### -field <b>RegisterEventCallback</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pregister-event-callback.md">RegisterEventCallback</a> routine.</p>
</dd>

### -field <b>UnregisterEventCallback</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-punregister-event-callback.md">UnregisterEventCallback</a> routine.</p>
</dd>

### -field <b>GetDeviceInformation</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pget-device-information.md">GetDeviceInformation</a> routine.</p>
</dd>

### -field <b>GetResourceInformation</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pget-resource-information.md">GetResourceInformation</a> routine.</p>
</dd>

### -field <b>AllocateDmaBufferWithNotification</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer-with-notification.md">AllocateDmaBufferWithNotification</a> routine.</p>
</dd>

### -field <b>FreeDmaBufferWithNotification</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer-with-notification.md">FreeDmaBufferWithNotification</a> routine.</p>
</dd>

### -field <b>RegisterNotificationEvent</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-pregister-notification-event.md">RegisterNotificationEvent</a> routine.</p>
</dd>

### -field <b>UnregisterNotificationEvent</b>

<dd>
<p>A function pointer to the <a href="..\hdaudio\nc-hdaudio-punregister-notification-event.md">UnregisterNotificationEvent</a> routine.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> IOCTL uses this structure to provide interface information to a client that is querying the HD Audio bus driver for the HD Audio DDI.</p>

<p>The names and definitions of the first five members of the <b>HDAUDIO_BUS_INTERFACE_V2</b> structure (Size, Version, Context, InterfaceReference, and InterfaceDereference) are the same as in the <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure. The remaining members are specific to the baseline HD Audio DDI and specify function pointers to the routines in the DDI. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hdaudio.h (include Hdaudio.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer.md">AllocateDmaBuffer</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer-with-notification.md">AllocateDmaBufferWithNotification</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pchange-bandwidth-allocation.md">ChangeBandwidthAllocation</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer.md">FreeDmaBuffer</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer-with-notification.md">FreeDmaBufferWithNotification</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pfree-dma-engine.md">FreeDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pget-device-information.md">GetDeviceInformation</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pget-link-position-register.md">GetLinkPositionRegister</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pget-resource-information.md">GetResourceInformation</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pget-wall-clock-register.md">GetWallClockRegister</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pregister-event-callback.md">RegisterEventCallback</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pregister-notification-event.md">RegisterNotificationEvent</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pset-dma-engine-state.md">SetDmaEngineState</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-ptransfer-codec-verbs.md">TransferCodecVerbs</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-punregister-event-callback.md">UnregisterEventCallback</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-punregister-notification-event.md">UnregisterNotificationEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20HDAUDIO_BUS_INTERFACE_V2 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
