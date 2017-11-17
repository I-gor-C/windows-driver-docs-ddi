---
UID: NS.dsm._DSM_INIT_DATA
title: DSM_INIT_DATA
author: windows-driver-content
description: 
ms.assetid: 619d4e43-0677-4e93-874f-f6acc047c0b2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DSM_INIT_DATA, DSM_INIT_DATA, *PDSM_INIT_DATA
req.header: dsm.h
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

# DSM_INIT_DATA structure

## -description



## -struct-fields

### -field union __unnamed_union_0bd3_5			
 	
### -field ULONG InitDataSize			
 	
### -field DSM_INQUIRE_DRIVER DsmInquireDriver			
 	
### -field DSM_COMPARE_DEVICES DsmCompareDevices			
 	
### -field DSM_DEVICE_SERIAL_NUMBER DsmDeviceSerialNumber			
 	
### -field DSM_GET_CONTROLLER_INFO DsmGetControllerInfo			
 	
### -field DSM_SET_DEVICE_INFO DsmSetDeviceInfo			
 	
### -field DSM_IS_PATH_ACTIVE DsmIsPathActive			
 	
### -field DSM_PATH_VERIFY DsmPathVerify			
 	
### -field DSM_INVALIDATE_PATH DsmInvalidatePath			
 	
### -field DSM_MOVE_DEVICE DsmMoveDevice			
 	
### -field DSM_REMOVE_PENDING DsmRemovePending			
 	
### -field DSM_REMOVE_DEVICE DsmRemoveDevice			
 	
### -field DSM_REMOVE_PATH DsmRemovePath			
 	
### -field DSM_SRB_DEVICE_CONTROL DsmSrbDeviceControl			
 	
### -field DSM_LB_GET_PATH DsmLBGetPath			
 	
### -field DSM_UNLOAD DsmUnload			
 	
### -field DSM_SET_COMPLETION DsmSetCompletion			
 	
### -field DSM_CATEGORIZE_REQUEST DsmCategorizeRequest			
 	
### -field DSM_BROADCAST_SRB DsmBroadcastSrb			
 	
### -field DSM_WMILIB_CONTEXT DsmWmiInfo			
 	
### -field PVOID DsmContext			
 	
### -field PDRIVER_OBJECT DriverObject			
 	
### -field UNICODE_STRING DisplayName			
 	
### -field ULONG Reserved			
 	
### -field DSM_TYPE DsmType			
 	
### -field DSM_VERSION_INFO DsmVersion			
 	
### -field DSM_WMILIB_CONTEXT DsmWmiGlobalInfo			
 	
### -field DSM_ADDRESS_TYPE_SUPPORTED DsmIsAddressTypeSupported			
 	
### -field DSM_DEVICE_NOT_USED DsmDeviceNotUsed			
 	
### -field DSM_INTERPRET_ERROR DsmInterpretError			
 	
### -field DSM_INTERPRET_ERROR_EX DsmInterpretErrorEx			
 	
## -remarks

## -see-also