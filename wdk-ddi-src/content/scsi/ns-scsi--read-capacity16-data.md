---
UID: NS.scsi._READ_CAPACITY16_DATA
title: READ_CAPACITY16_DATA
author: windows-driver-content
description: 
ms.assetid: eb3ac119-e033-4ea4-9a8c-4451ef7ec4f1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: READ_CAPACITY16_DATA, READ_CAPACITY16_DATA, *PREAD_CAPACITY16_DATA
req.header: scsi.h
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

# READ_CAPACITY16_DATA structure

## -description



## -struct-fields

### -field LARGE_INTEGER LogicalBlockAddress			
 	
### -field ULONG BytesPerBlock			
 	
### -field UCHAR  : 1 ProtectionEnable			
 	
### -field UCHAR  : 3 ProtectionType			
 	
### -field UCHAR  : 2 RcBasis			
 	
### -field UCHAR  : 2 Reserved			
 	
### -field UCHAR  : 4 LogicalPerPhysicalExponent			
 	
### -field UCHAR  : 4 ProtectionInfoExponent			
 	
### -field UCHAR  : 6 LowestAlignedBlock_MSB			
 	
### -field UCHAR  : 1 LBPRZ			
 	
### -field UCHAR  : 1 LBPME			
 	
### -field UCHAR LowestAlignedBlock_LSB			
 	
### -field UCHAR [16] Reserved3			
 	
## -remarks

## -see-also