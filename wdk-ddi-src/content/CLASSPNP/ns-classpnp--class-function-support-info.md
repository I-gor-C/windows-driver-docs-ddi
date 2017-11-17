---
UID: NS.classpnp._CLASS_FUNCTION_SUPPORT_INFO
title: CLASS_FUNCTION_SUPPORT_INFO
author: windows-driver-content
description: 
ms.assetid: 5fb45908-ae62-4b14-9d97-fe8df536ff3f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CLASS_FUNCTION_SUPPORT_INFO, CLASS_FUNCTION_SUPPORT_INFO, *PCLASS_FUNCTION_SUPPORT_INFO
req.header: classpnp.h
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

# CLASS_FUNCTION_SUPPORT_INFO structure

## -description



## -struct-fields

### -field struct ValidInquiryPages			
 	
### -field __unnamed_struct_0b7c_11 __unnamed_struct_0b7c_11			
 	
### -field struct LowerLayerSupport			
 	
### -field __unnamed_struct_0b7c_12 __unnamed_struct_0b7c_12			
 	
### -field struct IdlePower			
 	
### -field __unnamed_struct_0b7c_13 __unnamed_struct_0b7c_13			
 	
### -field KSPIN_LOCK SyncLock			
 	
### -field ULONG GenerationCount			
 	
### -field ULONG ChangeRequestCount			
 	
### -field BOOLEAN RegAccessAlignmentQueryNotSupported			
 	
### -field BOOLEAN AsynchronousNotificationSupported			
 	
### -field BOOLEAN UseModeSense10			
 	
### -field UCHAR Reserved			
 	
### -field UCHAR [2] Reserved			
 	
### -field CLASS_VPD_B0_DATA BlockLimitsData			
 	
### -field CLASS_VPD_B1_DATA DeviceCharacteristicsData			
 	
### -field CLASS_VPD_B2_DATA LBProvisioningData			
 	
### -field CLASS_READ_CAPACITY16_DATA ReadCapacity16Data			
 	
### -field CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS BlockDeviceRODLimitsData			
 	
### -field CLASS_FUNCTION_SUPPORT HwFirmwareGetInfoSupport			
 	
### -field PSTORAGE_HW_FIRMWARE_INFO HwFirmwareInfo			
 	
## -remarks

## -see-also