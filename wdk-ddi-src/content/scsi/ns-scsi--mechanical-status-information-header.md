---
UID: NS.scsi._MECHANICAL_STATUS_INFORMATION_HEADER
title: MECHANICAL_STATUS_INFORMATION_HEADER
author: windows-driver-content
description: 
ms.assetid: 9f99841d-bbac-41c5-bebf-8969bfed165c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MECHANICAL_STATUS_INFORMATION_HEADER, MECHANICAL_STATUS_INFORMATION_HEADER, *PMECHANICAL_STATUS_INFORMATION_HEADER
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

# MECHANICAL_STATUS_INFORMATION_HEADER structure

## -description



## -struct-fields

### -field UCHAR  : 5 CurrentSlot			
 	
### -field UCHAR  : 2 ChangerState			
 	
### -field UCHAR  : 1 Fault			
 	
### -field UCHAR  : 5 Reserved			
 	
### -field UCHAR  : 3 MechanismState			
 	
### -field UCHAR [3] CurrentLogicalBlockAddress			
 	
### -field UCHAR NumberAvailableSlots			
 	
### -field UCHAR [2] SlotTableLength			
 	
## -remarks

## -see-also