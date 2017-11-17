---
UID: NS.hubbusif._USB_BUS_INTERFACE_HUB_V6
title: USB_BUS_INTERFACE_HUB_V6
author: windows-driver-content
description: 
ms.assetid: 3e113f5b-89ed-435e-b187-997e3334de1c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_BUS_INTERFACE_HUB_V6, USB_BUS_INTERFACE_HUB_V6, *PUSB_BUS_INTERFACE_HUB_V6
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

# USB_BUS_INTERFACE_HUB_V6 structure

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
 	
## -remarks

## -see-also