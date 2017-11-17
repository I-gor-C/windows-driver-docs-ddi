---
UID: NS.ntddk._DEBUG_DEVICE_DESCRIPTOR
title: DEBUG_DEVICE_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 71fd8f8e-e330-4139-b459-1d37d47f251d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DEBUG_DEVICE_DESCRIPTOR, DEBUG_DEVICE_DESCRIPTOR, *PDEBUG_DEVICE_DESCRIPTOR
req.header: ntddk.h
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

# DEBUG_DEVICE_DESCRIPTOR structure

## -description



## -struct-fields

### -field union __unnamed_union_0c2a_100			
 	
### -field ULONG Bus			
 	
### -field ULONG Slot			
 	
### -field USHORT Segment			
 	
### -field USHORT VendorID			
 	
### -field USHORT DeviceID			
 	
### -field UCHAR BaseClass			
 	
### -field UCHAR SubClass			
 	
### -field UCHAR ProgIf			
 	
### -field BOOLEAN Initialized			
 	
### -field BOOLEAN Configured			
 	
### -field DEBUG_DEVICE_ADDRESS [MAXIMUM_DEBUG_BARS] BaseAddress			
 	
### -field DEBUG_MEMORY_REQUIREMENTS Memory			
 	
### -field USHORT PortType			
 	
### -field USHORT PortSubtype			
 	
### -field PVOID OemData			
 	
### -field ULONG OemDataLength			
 	
### -field KD_NAMESPACE_ENUM NameSpace			
 	
### -field PWCHAR NameSpacePath			
 	
### -field ULONG NameSpacePathLength			
 	
### -field ULONG TransportType			
 	
### -field DEBUG_TRANSPORT_DATA TransportData			
 	
### -field UCHAR  : 1 DbgHalScratchAllocated			
 	
### -field UCHAR  : 1 DbgBarsMapped			
 	
### -field UCHAR  : 1 DbgScratchAllocated			
 	
### -field UCHAR Flags			
 	
## -remarks

## -see-also