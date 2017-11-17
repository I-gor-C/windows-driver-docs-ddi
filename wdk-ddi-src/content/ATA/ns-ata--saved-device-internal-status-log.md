---
UID: NS.ata._SAVED_DEVICE_INTERNAL_STATUS_LOG
title: SAVED_DEVICE_INTERNAL_STATUS_LOG
author: windows-driver-content
description: 
ms.assetid: 6e187be0-3083-4855-80da-f5043c2d02f3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SAVED_DEVICE_INTERNAL_STATUS_LOG, SAVED_DEVICE_INTERNAL_STATUS_LOG, *PSAVED_DEVICE_INTERNAL_STATUS_LOG
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

# SAVED_DEVICE_INTERNAL_STATUS_LOG structure

## -description



## -struct-fields

### -field UCHAR LogAddress			
 	
### -field UCHAR [3] Reserved0			
 	
### -field ULONG OrganizationID			
 	
### -field USHORT Area1LastLogPage			
 	
### -field USHORT Area2LastLogPage			
 	
### -field USHORT Area3LastLogPage			
 	
### -field UCHAR [368] Reserved2			
 	
### -field UCHAR SavedDataAvailable			
 	
### -field UCHAR GenerationNumber			
 	
### -field UCHAR [128] ReasonIdentifier			
 	
## -remarks

## -see-also