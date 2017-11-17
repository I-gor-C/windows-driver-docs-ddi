---
UID: NS.scsi._POWER_CONDITION_PAGE
title: POWER_CONDITION_PAGE
author: windows-driver-content
description: 
ms.assetid: bd21dae5-17cc-4e93-a83a-18c6134f8ea9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: POWER_CONDITION_PAGE, POWER_CONDITION_PAGE, *PPOWER_CONDITION_PAGE
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

# POWER_CONDITION_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PSBit			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR Reserved2			
 	
### -field UCHAR  : 1 Standby			
 	
### -field UCHAR  : 1 Idle			
 	
### -field UCHAR  : 6 Reserved3			
 	
### -field UCHAR [4] IdleTimer			
 	
### -field UCHAR [4] StandbyTimer			
 	
## -remarks

## -see-also