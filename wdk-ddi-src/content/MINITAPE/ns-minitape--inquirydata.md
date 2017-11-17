---
UID: NS.minitape._INQUIRYDATA
title: INQUIRYDATA
author: windows-driver-content
description: 
ms.assetid: a9c4ef0b-4dc3-4b94-a861-fc0f1f09a541
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: INQUIRYDATA, INQUIRYDATA, *PINQUIRYDATA
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

# INQUIRYDATA structure

## -description



## -struct-fields

### -field UCHAR  : 5 DeviceType			
 	
### -field UCHAR  : 3 DeviceTypeQualifier			
 	
### -field UCHAR  : 7 DeviceTypeModifier			
 	
### -field UCHAR  : 1 RemovableMedia			
 	
### -field UCHAR Versions			
 	
### -field UCHAR  : 4 ResponseDataFormat			
 	
### -field UCHAR  : 1 HiSupport			
 	
### -field UCHAR  : 1 NormACA			
 	
### -field UCHAR  : 1 ReservedBit			
 	
### -field UCHAR  : 1 AERC			
 	
### -field UCHAR AdditionalLength			
 	
### -field UCHAR [2] Reserved			
 	
### -field UCHAR  : 1 SoftReset			
 	
### -field UCHAR  : 1 CommandQueue			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 1 LinkedCommands			
 	
### -field UCHAR  : 1 Synchronous			
 	
### -field UCHAR  : 1 Wide16Bit			
 	
### -field UCHAR  : 1 Wide32Bit			
 	
### -field UCHAR  : 1 RelativeAddressing			
 	
### -field UCHAR [8] VendorId			
 	
### -field UCHAR [16] ProductId			
 	
### -field UCHAR [4] ProductRevisionLevel			
 	
### -field UCHAR [20] VendorSpecific			
 	
### -field UCHAR [2] Reserved3			
 	
### -field VERSION_DESCRIPTOR [8] VersionDescriptors			
 	
### -field UCHAR [30] Reserved4			
 	
## -remarks

## -see-also