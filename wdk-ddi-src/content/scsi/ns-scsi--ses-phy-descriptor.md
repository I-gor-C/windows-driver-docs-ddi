---
UID: NS.scsi._SES_PHY_DESCRIPTOR
title: SES_PHY_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 07474ed6-78bf-4bb3-98a6-7122072a6731
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SES_PHY_DESCRIPTOR, SES_PHY_DESCRIPTOR, *PSES_PHY_DESCRIPTOR
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

# SES_PHY_DESCRIPTOR structure

## -description



## -struct-fields

### -field UCHAR  : 4 Reserved1			
 	
### -field UCHAR  : 3 DeviceType			
 	
### -field UCHAR  : 1 Reserved3			
 	
### -field UCHAR Reserved4			
 	
### -field UCHAR  : 1 Reserved5			
 	
### -field UCHAR  : 1 SmpInitiatorPort			
 	
### -field UCHAR  : 1 StpInitiatorPort			
 	
### -field UCHAR  : 1 SspInitiatorPort			
 	
### -field UCHAR  : 4 Reserved6			
 	
### -field UCHAR  : 1 SataDevice			
 	
### -field UCHAR  : 1 SmpTargetPort			
 	
### -field UCHAR  : 1 StpTargetPort			
 	
### -field UCHAR  : 1 SspTargetPort			
 	
### -field UCHAR  : 3 Reserved7			
 	
### -field UCHAR  : 1 SataPortSelector			
 	
### -field UCHAR [8] AttachedSASAddress			
 	
### -field UCHAR [8] SASAddress			
 	
### -field UCHAR PhyIdentifier			
 	
### -field UCHAR [7] Reserved2			
 	
## -remarks

## -see-also