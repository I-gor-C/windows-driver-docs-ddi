---
UID: NS.wdm._IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS
title: IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 72880fa2-ead0-4296-849e-9031706f7923
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS, 
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

# IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS structure

## -description



## -struct-fields

### -field union ConnectionContext			
 	
### -field __unnamed_union_0cb3_164 __unnamed_union_0cb3_164			
 	
### -field PDEVICE_OBJECT PhysicalDeviceObject			
 	
### -field PKMESSAGE_SERVICE_ROUTINE MessageServiceRoutine			
 	
### -field PVOID ServiceContext			
 	
### -field PKSPIN_LOCK SpinLock			
 	
### -field KIRQL SynchronizeIrql			
 	
### -field BOOLEAN FloatingSave			
 	
### -field PKSERVICE_ROUTINE FallBackServiceRoutine			
 	
### -field PVOID * Generic			
 	
### -field PIO_INTERRUPT_MESSAGE_INFO * InterruptMessageTable			
 	
### -field PKINTERRUPT * InterruptObject			
 	
## -remarks

## -see-also