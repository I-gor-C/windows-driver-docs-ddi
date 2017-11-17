---
UID: NS.1394._NODE_DEVICE_EXTENSION
title: NODE_DEVICE_EXTENSION
author: windows-driver-content
description: 
ms.assetid: 797491ec-4736-4a93-a8e0-cb588075ebc7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NODE_DEVICE_EXTENSION, NODE_DEVICE_EXTENSION, *PNODE_DEVICE_EXTENSION
req.header: 1394.h
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

# NODE_DEVICE_EXTENSION structure

## -description



## -struct-fields

### -field ULONG Tag			
 	
### -field BOOLEAN bConfigurationInformationValid			
 	
### -field PCONFIG_ROM ConfigRom			
 	
### -field ULONG UnitDirectoryLength			
 	
### -field PVOID UnitDirectory			
 	
### -field IO_ADDRESS UnitDirectoryLocation			
 	
### -field ULONG UnitDependentDirectoryLength			
 	
### -field PVOID UnitDependentDirectory			
 	
### -field IO_ADDRESS UnitDependentDirectoryLocation			
 	
### -field ULONG VendorLeafLength			
 	
### -field PTEXTUAL_LEAF VendorLeaf			
 	
### -field ULONG ModelLeafLength			
 	
### -field PTEXTUAL_LEAF ModelLeaf			
 	
### -field NODE_ADDRESS NodeAddress			
 	
### -field UCHAR Speed			
 	
### -field UCHAR Priority			
 	
### -field PIRP Irp			
 	
### -field PDEVICE_OBJECT DeviceObject			
 	
### -field PDEVICE_OBJECT PortDeviceObject			
 	
### -field PVOID DeviceInformation			
 	
### -field PBUS_BUS_RESET_NOTIFICATION ResetRoutine			
 	
### -field PVOID ResetContext			
 	
## -remarks

## -see-also