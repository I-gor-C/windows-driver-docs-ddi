---
UID: NS.ntddk._WHEA_ARM_BUS_ERROR
title: WHEA_ARM_BUS_ERROR
author: windows-driver-content
description: 
ms.assetid: f40daf1c-2d1d-4eb0-aeca-dbe9b960ed5f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WHEA_ARM_BUS_ERROR, WHEA_ARM_BUS_ERROR, *PWHEA_ARM_BUS_ERROR
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

# WHEA_ARM_BUS_ERROR structure

## -description



## -struct-fields

### -field WHEA_ARM_BUS_ERROR_VALID_BITS ValidationBit			
 	
### -field UCHAR  : 2 TransactionType			
 	
### -field UCHAR  : 4 Operation			
 	
### -field UCHAR  : 3 Level			
 	
### -field UCHAR  : 1 ProcessorContextCorrupt			
 	
### -field UCHAR  : 1 Corrected			
 	
### -field UCHAR  : 1 PrecisePC			
 	
### -field UCHAR  : 1 RestartablePC			
 	
### -field UCHAR  : 2 ParticipationType			
 	
### -field UCHAR  : 1 TimeOut			
 	
### -field UCHAR  : 2 AddressSpace			
 	
### -field USHORT  : 9 MemoryAccessAttributes			
 	
### -field UCHAR  : 1 AccessMode			
 	
### -field ULONG  : 20 Reserved			
 	
## -remarks

## -see-also