---
UID: NS.extsfns._DEBUG_IRP_INFO
title: DEBUG_IRP_INFO
author: windows-driver-content
description: 
ms.assetid: cebd4522-1c75-4051-a81e-0f7e23f08b55
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DEBUG_IRP_INFO, DEBUG_IRP_INFO, *PDEBUG_IRP_INFO
req.header: extsfns.h
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

# DEBUG_IRP_INFO structure

## -description



## -struct-fields

### -field ULONG SizeOfStruct			
 	
### -field ULONG64 IrpAddress			
 	
### -field ULONG IoStatus			
 	
### -field ULONG StackCount			
 	
### -field ULONG CurrentLocation			
 	
### -field ULONG64 MdlAddress			
 	
### -field ULONG64 Thread			
 	
### -field ULONG64 CancelRoutine			
 	
### -field DEBUG_IRP_STACK_INFO CurrentStack			
 	
### -field DEBUG_IRP_STACK_INFO [10] Stack			
 	
## -remarks

## -see-also