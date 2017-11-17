---
UID: NS.wdm._IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS
title: IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: c68927f9-907a-4f18-85fe-f1685563dcac
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS, 
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

# IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS structure

## -description



## -struct-fields

### -field PDEVICE_OBJECT PhysicalDeviceObject			
 	
### -field PKINTERRUPT * InterruptObject			
 	
### -field PKSERVICE_ROUTINE ServiceRoutine			
 	
### -field PVOID ServiceContext			
 	
### -field PKSPIN_LOCK SpinLock			
 	
### -field KIRQL SynchronizeIrql			
 	
### -field BOOLEAN FloatingSave			
 	
### -field BOOLEAN ShareVector			
 	
### -field ULONG Vector			
 	
### -field KIRQL Irql			
 	
### -field KINTERRUPT_MODE InterruptMode			
 	
### -field KAFFINITY ProcessorEnableMask			
 	
### -field USHORT Group			
 	
## -remarks

## -see-also