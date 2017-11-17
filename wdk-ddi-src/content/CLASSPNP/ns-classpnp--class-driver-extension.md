---
UID: NS.classpnp._CLASS_DRIVER_EXTENSION
title: CLASS_DRIVER_EXTENSION
author: windows-driver-content
description: 
ms.assetid: ec29bd66-b54c-4fc0-a474-ffe5e9a287ee
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CLASS_DRIVER_EXTENSION, CLASS_DRIVER_EXTENSION, *PCLASS_DRIVER_EXTENSION
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

# CLASS_DRIVER_EXTENSION structure

## -description



## -struct-fields

### -field UNICODE_STRING RegistryPath			
 	
### -field CLASS_INIT_DATA InitData			
 	
### -field ULONG DeviceCount			
 	
### -field PCLASS_QUERY_WMI_REGINFO_EX ClassFdoQueryWmiRegInfoEx			
 	
### -field PCLASS_QUERY_WMI_REGINFO_EX ClassPdoQueryWmiRegInfoEx			
 	
### -field REGHANDLE EtwHandle			
 	
### -field PDRIVER_DISPATCH [IRP_MJ_MAXIMUM_FUNCTION + 1] DeviceMajorFunctionTable			
 	
### -field PDRIVER_DISPATCH [IRP_MJ_MAXIMUM_FUNCTION + 1] MpDeviceMajorFunctionTable			
 	
### -field PCLASS_INTERPRET_SENSE_INFO2 InterpretSenseInfo			
 	
### -field PCLASS_WORKING_SET WorkingSet			
 	
### -field ULONG SrbSupport			
 	
## -remarks

## -see-also