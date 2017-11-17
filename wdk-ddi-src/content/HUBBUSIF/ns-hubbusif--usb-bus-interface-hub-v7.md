---
UID: NS.hubbusif._USB_BUS_INTERFACE_HUB_V7
title: USB_BUS_INTERFACE_HUB_V7
author: windows-driver-content
description: 
ms.assetid: 7f0b5de0-605d-411d-8ad7-35ce440630c8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_BUS_INTERFACE_HUB_V7, USB_BUS_INTERFACE_HUB_V7, *PUSB_BUS_INTERFACE_HUB_V7
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

# USB_BUS_INTERFACE_HUB_V7 structure

## -description



## -struct-fields

### -field USHORT Size			
 	
### -field USHORT Version			
 	
### -field PVOID BusContext			
 	
### -field PINTERFACE_REFERENCE InterfaceReference			
 	
### -field PINTERFACE_DEREFERENCE InterfaceDereference			
 	
### -field PUSB_BUSIFFN_CREATE_USB_DEVICE_EX CreateUsbDevice			
 	
### -field PUSB_BUSIFFN_INITIALIZE_USB_DEVICE_EX InitializeUsbDevice			
 	
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
 	
### -field PUSB_BUSIFFN_IS_ROOT HubIsRoot			
 	
### -field PUSB_BUSIFFN_ACQUIRE_SEMAPHORE AcquireBusSemaphore			
 	
### -field PUSB_BUSIFFN_RELEASE_SEMAPHORE ReleaseBusSemaphore			
 	
### -field PUSB_BUSIFFN_CALC_PIPE_BANDWIDTH CaculatePipeBandwidth			
 	
### -field PUSB_BUSIFFN_SET_BUS_WAKE_MODE SetBusSystemWakeMode			
 	
### -field PUSB_BUSIFFN_SET_DEVICE_FLAG SetDeviceFlag			
 	
### -field PUSB_BUSIFFN_TEST_POINT HubTestPoint			
 	
### -field PUSB_BUSIFFN_GET_DEVICE_PERFORMANCE_INFO GetDevicePerformanceInfo			
 	
### -field PUSB_BUSIFFN_WAIT_ASYNC_POWERUP WaitAsyncPowerUp			
 	
### -field PUSB_BUSIFFN_GET_DEVICE_ADDRESS GetDeviceAddress			
 	
### -field PUSB_BUSIFFN_REF_DEVICE_HANDLE RefDeviceHandle			
 	
### -field PUSB_BUSIFFN_DEREF_DEVICE_HANDLE DerefDeviceHandle			
 	
### -field PUSB_BUSIFFN_SET_DEVICE_HANDLE_IDLE_READY_STATE SetDeviceHandleIdleReadyState			
 	
### -field PUSB_BUSIFFN_CREATE_USB_DEVICE_V7 CreateUsbDeviceV7			
 	
### -field PUSB_BUSIFFN_GET_CONTAINER_ID_FOR_PORT GetContainerIdForPort			
 	
### -field PUSB_BUSIFFN_SET_CONTAINER_ID_FOR_PORT SetContainerIdForPort			
 	
### -field PUSB_BUSIFFN_ABORT_ALL_DEVICE_PIPES AbortAllDevicePipes			
 	
### -field PUSB_BUSIFFN_SET_DEVICE_ERRATA_FLAG SetDeviceErrataFlag			
 	
## -remarks

## -see-also