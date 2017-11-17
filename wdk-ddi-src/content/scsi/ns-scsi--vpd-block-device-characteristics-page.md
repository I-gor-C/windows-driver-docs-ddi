---
UID: NS.scsi._VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE
title: VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE
author: windows-driver-content
description: 
ms.assetid: 0856bec3-04d7-4ce1-a0bd-a9df0b6eaea2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE, VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE, *PVPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE
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

# VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 5 DeviceType			
 	
### -field UCHAR  : 3 DeviceTypeQualifier			
 	
### -field UCHAR PageCode			
 	
### -field UCHAR Reserved0			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR MediumRotationRateMsb			
 	
### -field UCHAR MediumRotationRateLsb			
 	
### -field UCHAR MediumProductType			
 	
### -field UCHAR  : 4 NominalFormFactor			
 	
### -field UCHAR  : 2 WACEREQ			
 	
### -field UCHAR  : 2 WABEREQ			
 	
### -field UCHAR  : 1 VBULS			
 	
### -field UCHAR  : 1 FUAB			
 	
### -field UCHAR  : 1 BOCS			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 2 ZONED			
 	
### -field UCHAR  : 2 Reserved2			
 	
### -field UCHAR [3] Reserved3			
 	
### -field UCHAR [4] DepopulationTime			
 	
### -field UCHAR [48] Reserved4			
 	
## -remarks

## -see-also