---
UID: NS.hubbusif._USB_BUS_INTERFACE_HUB_V3
title: USB_BUS_INTERFACE_HUB_V3
author: windows-driver-content
description: 
ms.assetid: 85a4f71e-f342-4d49-a2c1-e1965f945b37
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_BUS_INTERFACE_HUB_V3, USB_BUS_INTERFACE_HUB_V3, *PUSB_BUS_INTERFACE_HUB_V3
req.header: hubbusif.h
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

# USB_BUS_INTERFACE_HUB_V3 structure

## -description



## -struct-fields

### -field USHORT Size			
 	
### -field USHORT Version			
 	
### -field PVOID BusContext			
 	
### -field PINTERFACE_REFERENCE InterfaceReference			
 	
### -field PINTERFACE_DEREFERENCE InterfaceDereference			
 	
### -field PUSB_BUSIFFN_CREATE_USB_DEVICE CreateUsbDevice			
 	
### -field PUSB_BUSIFFN_INITIALIZE_USB_DEVICE InitializeUsbDevice			
 	
### -field PUSB_BUSIFFN_GET_USB_DESCRIPTORS GetUsbDescriptors			
 	
### -field PUSB_BUSIFFN_REMOVE_USB_DEVICE RemoveUsbDevice			
 	
### -field PUSB_BUSIFFN_RESTORE_DEVICE RestoreUsbDevice			
 	
### -field PUSB_BUSIFFN_GET_POTRTHACK_FLAGS GetPortHackFlags			
 	
### -field PUSB_BUSIFFN_GET_DEVICE_INFORMATION QueryDeviceInformation			
 	
### -field PUSB_BUSIFFN_GET_CONTROLLER_INFORMATION GetControllerInformation			
 	
### -field PUSB_BUSIFFN_CONTROLLER_SELECTIVE_SUSPEND ControllerSelectiveSuspend			
 	
### -field PUSB_BUSIFFN_GET_EXTENDED_HUB_INFO GetExtendedHubInformation			
 	
### -field PUSB_BUSIFFN_GET_ROOTHUB_SYM_NAME GetRootHubSymbolicName			
 	
### -field PUSB_BUSIFFN_GET_DEVICE_BUSCONTEXT GetDeviceBusContext			
 	
### -field PUSB_BUSIFFN_INITIALIZE_20HUB Initialize20Hub			
 	
### -field PUSB_BUSIFFN_ROOTHUB_INIT_NOTIFY RootHubInitNotification			
 	
## -remarks

## -see-also