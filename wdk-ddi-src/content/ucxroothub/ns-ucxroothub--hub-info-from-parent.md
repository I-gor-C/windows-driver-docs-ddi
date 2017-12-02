---
UID: NS.ucxroothub._HUB_INFO_FROM_PARENT
title: HUB_INFO_FROM_PARENT
author: windows-driver-content
description: Describes information about a hub from its parent device.
old-location: buses\_hub_info_from_parent.htm
old-project: usbref
ms.assetid: 6259CC70-A54B-4A44-B38B-D24C296C8EA0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HUB_INFO_FROM_PARENT, HUB_INFO_FROM_PARENT, *PHUB_INFO_FROM_PARENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HUB_INFO_FROM_PARENT
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# HUB_INFO_FROM_PARENT structure



## -description
<p>Describes information about a hub from its parent device. </p>


## -syntax

````
typedef struct _HUB_INFO_FROM_PARENT {
  PDEVICE_OBJECT                              IoTarget;
  USB_DEVICE_DESCRIPTOR                       DeviceDescriptor;
  USHORT                                      U1ExitLatency;
  USHORT                                      U2ExitLatency;
  USHORT                                      ExitLatencyOfSlowestLinkForU1;
  UCHAR                                       DepthOfSlowestLinkForU1;
  USHORT                                      ExitLatencyOfSlowestLinkForU2;
  UCHAR                                       DepthOfSlowestLinkForU2;
  USHORT                                      HostInitiatedU1ExitLatency;
  USHORT                                      HostInitiatedU2ExitLatency;
  UCHAR                                       TotalHubDepth;
  USHORT                                      TotalTPPropogationDelay;
  PARENT_HUB_FLAGS                            HubFlags;
  PUSB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED SublinkSpeedAttr;
  ULONG                                       SublinkSpeedAttrCount;
} HUB_INFO_FROM_PARENT, *P_HUB_INFO_FROM_PARENT;
````


## -struct-fields
<dl>

### -field IoTarget

<dd>
<p>A pointer to the WDM device object of the parent that represents the I/O target.</p>
</dd>

### -field DeviceDescriptor

<dd>
<p>A <a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a> structure that contains the device descriptor.</p>
</dd>

### -field U1ExitLatency

<dd>
<p>The time to transition from the U1 state. </p>
</dd>

### -field U2ExitLatency

<dd>
<p>The time to transition from the U2 state. </p>
</dd>

### -field ExitLatencyOfSlowestLinkForU1

<dd>
<p>The exit latency for the slowest link for U1 transition.</p>
</dd>

### -field DepthOfSlowestLinkForU1

<dd>
<p>The depth of the hub based on which the latency
        for the slowest link is calculated for a U1 transition.</p>
</dd>

### -field ExitLatencyOfSlowestLinkForU2

<dd>
<p>The exit latency for the slowest link for U2 transition.</p>
</dd>

### -field DepthOfSlowestLinkForU2

<dd>
<p>The depth of the hub based on which the latency
        for the slowest link is calculated for a U2 transition.</p>
</dd>

### -field HostInitiatedU1ExitLatency

<dd>
<p>Host-initiated exit latency to transition from the U1 state. </p>
</dd>

### -field HostInitiatedU2ExitLatency

<dd>
<p>Host-initiated exit latency to transition from the U2 state. </p>
</dd>

### -field TotalHubDepth

<dd>
<p>Total hub depth.</p>
</dd>

### -field TotalTPPropogationDelay

<dd>
<p>The total TP propagation delay.</p>
</dd>

### -field HubFlags

<dd>
<p>A bitwise-OR of <a href="..\ucxroothub\ns-ucxroothub--parent-hub-flags.md">PARENT_HUB_FLAGS</a> flags.</p>
</dd>

### -field SublinkSpeedAttr

<dd>
<p>A pointer to a <b>USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED</b> structure that describes the USB 3.1capability's sublink speed attributes. For structure declaration, see Usbspec.h</p>
</dd>

### -field SublinkSpeedAttrCount

<dd>
<p>The count of sublink speed attributes.</p>
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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>