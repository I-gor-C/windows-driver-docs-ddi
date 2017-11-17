---
UID: NS.usbioctl._USB_DEVICE_NODE_INFO
title: USB_DEVICE_NODE_INFO
author: windows-driver-content
description: 
ms.assetid: e077f767-ab7e-4b35-913f-595ee9c672f9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_DEVICE_NODE_INFO, USB_DEVICE_NODE_INFO, *PUSB_DEVICE_NODE_INFO
req.header: usbioctl.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# USB_DEVICE_NODE_INFO structure

## -description



## -struct-fields

### -field union __unnamed_union_0afd_4			
 	
### -field ULONG Sig			
 	
### -field ULONG LengthInBytes			
 	
### -field WCHAR [40] DeviceDescription			
 	
### -field USB_WMI_DEVICE_NODE_TYPE NodeType			
 	
### -field USB_TOPOLOGY_ADDRESS BusAddress			
 	
### -field USB_DEVICE_INFO UsbDeviceInfo			
 	
### -field USB_HUB_DEVICE_INFO HubDeviceInfo			
 	
### -field USB_COMPOSITE_DEVICE_INFO CompositeDeviceInfo			
 	
### -field USB_CONTROLLER_DEVICE_INFO ControllerDeviceInfo			
 	
### -field UCHAR [4] DeviceInformation			
 	
## -remarks

## -see-also