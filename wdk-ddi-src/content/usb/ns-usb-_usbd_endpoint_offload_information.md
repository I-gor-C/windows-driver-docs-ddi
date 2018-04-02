---
UID: NS:usb._USBD_ENDPOINT_OFFLOAD_INFORMATION
title: "_USBD_ENDPOINT_OFFLOAD_INFORMATION"
author: windows-driver-content
description: Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints.
old-location: buses\usbd_endpoint_offload_information.htm
old-project: usbref
ms.assetid: F2A8E966-269E-447F-9467-EB2E877FFAA2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSBD_ENDPOINT_OFFLOAD_INFORMATION, PUSBD_ENDPOINT_OFFLOAD_INFORMATION, PUSBD_ENDPOINT_OFFLOAD_INFORMATION structure pointer [Buses], USBD_ENDPOINT_OFFLOAD_INFORMATION, USBD_ENDPOINT_OFFLOAD_INFORMATION structure [Buses], _USBD_ENDPOINT_OFFLOAD_INFORMATION, buses.usbd_endpoint_offload_information, usb/PUSBD_ENDPOINT_OFFLOAD_INFORMATION, usb/USBD_ENDPOINT_OFFLOAD_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Usb.h
api_name:
-	USBD_ENDPOINT_OFFLOAD_INFORMATION
product: Windows
targetos: Windows
req.typenames: USBD_ENDPOINT_OFFLOAD_INFORMATION, *PUSBD_ENDPOINT_OFFLOAD_INFORMATION
req.product: Windows 10 or later.
---

# _USBD_ENDPOINT_OFFLOAD_INFORMATION structure
Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints.

## Syntax
```
typedef struct _USBD_ENDPOINT_OFFLOAD_INFORMATION {
  ULONG                      Size;
  USHORT                     EndpointAddress;
  ULONG                      ResourceId;
  USBD_ENDPOINT_OFFLOAD_MODE Mode;
  ULONG  : 8                 RootHubPortNumber;
  ULONG  : 20                RouteString;
  ULONG  : 4                 Speed;
  ULONG  : 8                 UsbDeviceAddress;
  ULONG  : 8                 SlotId;
  ULONG  : 1                 MultiTT;
  ULONG  : 15                Reserved0;
  PHYSICAL_ADDRESS           TransferSegmentLA;
  PVOID                      TransferSegmentVA;
  size_t                     TransferRingSize;
  ULONG                      TransferRingInitialCycleBit;
  ULONG                      MessageNumber;
  PHYSICAL_ADDRESS           EventRingSegmentLA;
  PVOID                      EventRingSegmentVA;
  size_t                     EventRingSize;
  ULONG                      EventRingInitialCycleBit;
} *PUSBD_ENDPOINT_OFFLOAD_INFORMATION, USBD_ENDPOINT_OFFLOAD_INFORMATION;
```

## Members


`Size`

The size of this structure.

`EndpointAddress`

Specifies the USB-defined endpoint address.

`ResourceId`

The resource identifier.

`Mode`

A <a href="https://msdn.microsoft.com/577B2B5E-934E-4354-B6FF-FDFE9D1144D7">USBD_ENDPOINT_OFFLOAD_MODE</a>-type value that indicates whether endpoint offloading is handled in software or the USB device or host controller.

`RootHubPortNumber`

The port number of the root hub.

`RouteString`

The route string.

`Speed`

The route string.

`UsbDeviceAddress`

The USB device address.

`SlotId`

The slot identifier.

`MultiTT`

Transaction Translator (TT) hub.

`Reserved0`

Reserved.

`TransferSegmentLA`



`TransferSegmentVA`



`TransferRingSize`



`TransferRingInitialCycleBit`



`MessageNumber`



`EventRingSegmentLA`



`EventRingSegmentVA`



`EventRingSize`



`EventRingInitialCycleBit`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | usb.h |