---
UID: NS.usb._USBD_ENDPOINT_OFFLOAD_INFORMATION
title: USBD_ENDPOINT_OFFLOAD_INFORMATION
author: windows-driver-content
description: Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints.
old-location: buses\usbd_endpoint_offload_information.htm
ms.assetid: F2A8E966-269E-447F-9467-EB2E877FFAA2
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_ENDPOINT_OFFLOAD_INFORMATION
req.alt-loc: Usb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: USBD_ENDPOINT_OFFLOAD_INFORMATION, USBD_ENDPOINT_OFFLOAD_INFORMATION, *PUSBD_ENDPOINT_OFFLOAD_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# USBD_ENDPOINT_OFFLOAD_INFORMATION structure



## -description
<p>Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints.</p>


## -syntax

````
typedef struct _USBD_ENDPOINT_OFFLOAD_INFORMATION {
  ULONG                       Size;
  USHORT                      EndpointAddress;
  ULONG                       ResourceId;
  USBD_ENDPOINT_OFFLOAD_MODE  Mode;
  ULONG                       RootHubPortNumber  :8;
  ULONG                       RouteString  :20;
  ULONG                       Speed  :4;
  ULONG                       UsbDeviceAddress  :8;
  ULONG                       SlotId  :8;
  ULONG                       MultiTT  :1;
  ULONG                       Reserved0  :15;
  TransferSegmentLA           PHYSICAL_ADDRESS;
  TransferSegmentVA           PVOID;
  TransferRingSize            size_t;
  TransferRingInitialCycleBit ULONG;
  MessageNumber               ULONG;
  EventRingSegmentLA          PHYSICAL_ADDRESS;
  EventRingSegmentVA          PVOID;
  EventRingSize               size_t;
  EventRingInitialCycleBit    ULONG;
} USBD_ENDPOINT_OFFLOAD_INFORMATION, *PUSBD_ENDPOINT_OFFLOAD_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>EndpointAddress</b>

<dd>
<p>Specifies the USB-defined endpoint address. </p>
</dd>

### -field <b>ResourceId</b>

<dd>
<p>The resource identifier.</p>
</dd>

### -field <b>Mode</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/577B2B5E-934E-4354-B6FF-FDFE9D1144D7">USBD_ENDPOINT_OFFLOAD_MODE</a>-type value that indicates whether endpoint offloading is handled in software or the USB device or host controller.</p>
</dd>

### -field <b>RootHubPortNumber</b>

<dd>
<p>The port number of the root hub.</p>
</dd>

### -field <b>RouteString</b>

<dd>
<p>The route string.</p>
</dd>

### -field <b>Speed</b>

<dd>
<p>The route string.</p>
</dd>

### -field <b>UsbDeviceAddress</b>

<dd>
<p>The USB device address.</p>
</dd>

### -field <b>SlotId</b>

<dd>
<p>The slot identifier.</p>
</dd>

### -field <b>MultiTT</b>

<dd>
<p>Transaction Translator (TT) hub. </p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>PHYSICAL_ADDRESS</b>

<dd>
<p>The logical address of the current segment of the transfer data.</p>
</dd>

### -field <b>PVOID</b>

<dd>
<p>The virtual address of the current segment of the transfer data.</p>
</dd>

### -field <b>size_t</b>

<dd>
<p>The size of the requested data.</p>
</dd>

### -field <b>ULONG</b>

<dd>
<p>The cycle state of the transfer.</p>
</dd>

### -field <b>ULONG</b>

<dd>
<p>Reserved message for endpoint offload mode.
</p>
</dd>

### -field <b>PHYSICAL_ADDRESS</b>

<dd>
<p>The logical address of the current segment of the transfer data.</p>
</dd>

### -field <b>PVOID</b>

<dd>
<p>The virtual address of the current segment of the transfer data.</p>
</dd>

### -field <b>size_t</b>

<dd>
<p>The size of the requested data.</p>
</dd>

### -field <b>ULONG</b>

<dd>
<p>The cycle state of the transfer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usb.h</dt>
</dl>
</td>
</tr>
</table>