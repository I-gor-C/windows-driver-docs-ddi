---
UID: NS.1394._IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP
title: IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out a IsochAllocateResources request.
old-location: ieee\irb_req_isoch_allocate_resources_wxp.htm
old-project: IEEE
ms.assetid: 8DE03C05-48A4-4699-8513-F2B596EED37F
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP, IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP
req.alt-loc: 1394.h
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
---

# IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out a IsochAllocateResources request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP {
  ULONG          fulSpeed;
  ULONG          fulFlags;
  ULONG          nChannel;
  ULONG          nMaxBytesPerFrame;
  ULONG          nNumberOfBuffers;
  ULONG          nMaxBufferSize;
  ULONG          nQuadletsToStrip;
  HANDLE         hResource;
  ULARGE_INTEGER ChannelMask;
} IRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP, *PIRB_REQ_ISOCH_ALLOCATE_RESOURCES_WXP;
````


## -struct-fields
<dl>

### -field fulSpeed

<dd>
<p>Specifies the connection speed to use for communication on the channel. The possible speed values are SPEED_FLAGS_xxx, where xxx is the (approximate) transfer rate in megabits per second. Existing hardware supports transfer rates of 100, 200, and 400 Mb/sec.</p>
<table>
<tr>
<th>Transfer Rate</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_100</p>
</td>
<td>
<p>100 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_200</p>
</td>
<td>
<p>200 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_400</p>
</td>
<td>
<p>400 Mb/s</p>
</td>
</tr>
</table>
<p> </p>
<div class="alert"><b>Note</b>  In Windows 7 and later versions of Windows, you can specify new values higher speed and  greater sized payloads. For more information, see <a href="buses.device_driver_interface__ddi__changes_in_windows_7#speed#speed">New Flags for Speed and Payload Size</a> and <a href="buses.device_driver_interface__ddi__changes_in_windows_7#ioctl#ioctl">IEEE 1394 IOCTL Changes</a> in Device Driver Interface (DDI) Changes in Windows 7.</div>
<div> </div>
</dd>

### -field fulFlags

<dd>
<p>Specifies how the bus driver should use any buffers attached to the resource handle. Many of the flags specify how the bus driver should configure the IEEE host controller for DMA from or to attached buffers.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p> RESOURCE_USED_IN_LISTENING </p>
</td>
<td>
<p>Attached buffers are used to read data from an  isochronous channel. Set this if the resource handle will be used in a REQUEST_ISOCH_LISTEN request.</p>
</td>
</tr>
<tr>
<td>
<p>RESOURCE_USED_IN_TALKING </p>
</td>
<td>
<p>Attached buffers are used to write data to an isochronous channel. Set this if the resource handle will be used in a REQUEST_ISOCH_TALK request.</p>
</td>
</tr>
<tr>
<td>
<p>RESOURCE_STRIP_ADDITIONAL_QUADLETS </p>
</td>
<td>
<p>The bus driver configures the host controller to strip  additional quadlets from incoming isochronous packets. The number of quadlets to be stripped is specified in <b>nQuadletsToStrip</b>.</p>
</td>
</tr>
<tr>
<td>
<p>RESOURCE_SYNCH_ON_TIME</p>
</td>
<td>
<p>The bus driver configures the host controller to synchronize the beginning of the isochronous transaction to the CYCLE_TIME specified in the StartTime member of the request's IRB. See REQUEST_ISOCH_LISTEN or REQUEST_ISOCH_TALK.</p>
</td>
</tr>
<tr>
<td>
<p>RESOURCE_USE_PACKET_BASED</p>
</td>
<td>
<p>Used to switch to packet-based transfer, rather than the default. The default is stream-based transfer, unless the host controller only supports packet-based DMA.</p>
</td>
</tr>
<tr>
<td>
<p>RESOURCE_USE_MULTICHANNEL</p>
</td>
<td>
<p>The driver owning this resource listens on multiple channels. </p>
</td>
</tr>
<tr>
<td>
<p>RESOURCE_VARIABLE_ISOCH_PAYLOAD</p>
</td>
<td>
<p>The driver owning this resource transfers frames of variable size. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field nChannel

<dd>
<p>Specifies the isochronous channel for all transactions involving the resource handle allocated by this request.</p>
</dd>

### -field nMaxBytesPerFrame

<dd>
<p>Specifies the expected maximum isochronous frame size while transmitting and receiving on the channel.</p>
</dd>

### -field nNumberOfBuffers

<dd>
<p>Specifies one more than the maximum expected number of buffers that are attached to the resource handle at any given time. </p>
</dd>

### -field nMaxBufferSize

<dd>
<p>Specifies the maximum size of the buffers that are attached to the resource handle.</p>
</dd>

### -field nQuadletsToStrip

<dd>
<p>Specifies the number of quadlets to strip from the beginning of every packet in an incoming isochronous stream. This parameter is ignored unless the device driver sets the  RESOURCE_STRIP_ADDITIONAL_QUADLETS flag in <b>u.IsochAllocateResources.fulFlags</b>.</p>
</dd>

### -field hResource

<dd>
<p>Specifies a handle to the resource.</p>
</dd>

### -field ChannelMask

<dd>
<p>Specifies a set of isochronous channels, if RESOURCE_USE_MULTICHANNEL is set, that are used for all transactions involving the resource handle allocated by this request.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>