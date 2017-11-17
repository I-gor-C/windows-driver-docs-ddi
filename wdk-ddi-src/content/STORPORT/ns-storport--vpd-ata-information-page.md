---
UID: NS.storport._VPD_ATA_INFORMATION_PAGE
title: VPD_ATA_INFORMATION_PAGE
author: windows-driver-content
description: 
ms.assetid: bf691623-3014-40d7-b9e8-f1271e197599
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: VPD_ATA_INFORMATION_PAGE, VPD_ATA_INFORMATION_PAGE, *PVPD_ATA_INFORMATION_PAGE
req.header: storport.h
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

# VPD_ATA_INFORMATION_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 5 DeviceType			
 	
### -field UCHAR  : 3 DeviceTypeQualifier			
 	
### -field UCHAR PageCode			
 	
### -field UCHAR [2] PageLength			
 	
### -field UCHAR [4] Reserved0			
 	
### -field UCHAR [8] VendorId			
 	
### -field UCHAR [16] ProductId			
 	
### -field UCHAR [4] ProductRevisionLevel			
 	
### -field UCHAR [20] DeviceSignature			
 	
### -field UCHAR CommandCode			
 	
### -field UCHAR [3] Reserved1			
 	
### -field UCHAR [512] IdentifyDeviceData			
 	
## -remarks

## -see-also