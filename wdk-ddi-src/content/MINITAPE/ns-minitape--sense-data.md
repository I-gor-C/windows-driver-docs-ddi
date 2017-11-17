---
UID: NS.minitape._SENSE_DATA
title: SENSE_DATA
author: windows-driver-content
description: 
ms.assetid: ef1e527b-acfe-42ff-b75b-d20a4b4ba86f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SENSE_DATA, SENSE_DATA, *PSENSE_DATA
req.header: minitape.h
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

# SENSE_DATA structure

## -description



## -struct-fields

### -field UCHAR  : 7 ErrorCode			
 	
### -field UCHAR  : 1 Valid			
 	
### -field UCHAR SegmentNumber			
 	
### -field UCHAR  : 4 SenseKey			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 IncorrectLength			
 	
### -field UCHAR  : 1 EndOfMedia			
 	
### -field UCHAR  : 1 FileMark			
 	
### -field UCHAR [4] Information			
 	
### -field UCHAR AdditionalSenseLength			
 	
### -field UCHAR [4] CommandSpecificInformation			
 	
### -field UCHAR AdditionalSenseCode			
 	
### -field UCHAR AdditionalSenseCodeQualifier			
 	
### -field UCHAR FieldReplaceableUnitCode			
 	
### -field UCHAR [3] SenseKeySpecific			
 	
## -remarks

## -see-also