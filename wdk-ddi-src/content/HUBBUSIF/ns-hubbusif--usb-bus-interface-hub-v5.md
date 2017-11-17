---
UID: NS.hubbusif._USB_BUS_INTERFACE_HUB_V5
title: USB_BUS_INTERFACE_HUB_V5
author: windows-driver-content
description: 
ms.assetid: e270710e-227c-4685-9d29-86b41470808a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_BUS_INTERFACE_HUB_V5, USB_BUS_INTERFACE_HUB_V5, *PUSB_BUS_INTERFACE_HUB_V5
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

# USB_BUS_INTERFACE_HUB_V5 structure

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
 	
### -field PUSB_BUSIFFN_FLUSH_TRANSFERS FlushTransfers			
 	
### -field PUSB_BUSIFFN_SET_DEVHANDLE_DATA SetDeviceHandleData			
 	
## -remarks

## -see-also