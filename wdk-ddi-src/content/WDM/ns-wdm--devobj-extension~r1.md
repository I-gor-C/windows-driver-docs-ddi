---
UID: NS.wdm._DEVOBJ_EXTENSION~r1
title: DEVOBJ_EXTENSION
author: windows-driver-content
description: 
ms.assetid: e54d2969-4c05-4383-bea9-5d6bbb5bcaa2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DEVOBJ_EXTENSION, DEVOBJ_EXTENSION, *PDEVOBJ_EXTENSION
req.header: wdm.h
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

# DEVOBJ_EXTENSION structure

## -description



## -struct-fields

### -field struct _DEVICE_OBJECT_POWER_EXTENSION			
 	
### -field _DEVICE_OBJECT_POWER_EXTENSION * Dope			
 	
### -field CSHORT Type			
 	
### -field USHORT Size			
 	
### -field PDEVICE_OBJECT DeviceObject			
 	
### -field ULONG PowerFlags			
 	
### -field ULONG ExtensionFlags			
 	
### -field PVOID DeviceNode			
 	
### -field PDEVICE_OBJECT AttachedTo			
 	
### -field __volatile LONG StartIoCount			
 	
### -field LONG StartIoKey			
 	
### -field ULONG StartIoFlags			
 	
### -field PVPB Vpb			
 	
### -field PVOID DependencyNode			
 	
### -field PVOID InterruptContext			
 	
### -field __volatile PVOID VerifierContext			
 	
## -remarks

## -see-also