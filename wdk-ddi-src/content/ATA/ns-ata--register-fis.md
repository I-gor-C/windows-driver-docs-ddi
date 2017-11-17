---
UID: NS.ata._REGISTER_FIS
title: REGISTER_FIS
author: windows-driver-content
description: 
ms.assetid: 6ac6a6fe-571c-4ec4-ac43-f7d5296d622c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: REGISTER_FIS, REGISTER_FIS, *PREGISTER_FIS
req.header: ata.h
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

# REGISTER_FIS structure

## -description



## -struct-fields

### -field UCHAR FisType			
 	
### -field UCHAR  : 7 Reserved0			
 	
### -field UCHAR  : 1 CmdReg			
 	
### -field UCHAR Command			
 	
### -field UCHAR Features			
 	
### -field UCHAR SectorNumber			
 	
### -field UCHAR CylinderLow			
 	
### -field UCHAR CylinderHigh			
 	
### -field UCHAR DeviceHead			
 	
### -field UCHAR SectorNumberExp			
 	
### -field UCHAR CylinderLowExp			
 	
### -field UCHAR CylinderHighExp			
 	
### -field UCHAR FeaturesExp			
 	
### -field UCHAR SectorCount			
 	
### -field UCHAR SectorCountExp			
 	
### -field UCHAR Reserved2			
 	
### -field UCHAR Control			
 	
### -field ULONG Reserved3			
 	
## -remarks

## -see-also