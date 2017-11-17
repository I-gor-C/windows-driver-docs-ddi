---
UID: NS.ntddstor._STORAGE_ZONED_DEVICE_DESCRIPTOR
title: STORAGE_ZONED_DEVICE_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 63b60956-2c30-400d-ab9c-dc0bb0b1c40f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: STORAGE_ZONED_DEVICE_DESCRIPTOR, STORAGE_ZONED_DEVICE_DESCRIPTOR, *PSTORAGE_ZONED_DEVICE_DESCRIPTOR
req.header: ntddstor.h
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

# STORAGE_ZONED_DEVICE_DESCRIPTOR structure

## -description



## -struct-fields

### -field union ZoneAttributes			
 	
### -field __unnamed_union_0aed_13 __unnamed_union_0aed_13			
 	
### -field __WRAPPED__ ULONG Version			
 	
### -field __WRAPPED__ ULONG Size			
 	
### -field __WRAPPED__ STORAGE_ZONED_DEVICE_TYPES DeviceType			
 	
### -field __WRAPPED__ ULONG ZoneCount			
 	
### -field __WRAPPED__ ULONG ZoneGroupCount			
 	
### -field __WRAPPED__ STORAGE_ZONE_GROUP [ANYSIZE_ARRAY] ZoneGroup			
 	
### -field ULONG MaxOpenZoneCount			
 	
### -field BOOLEAN UnrestrictedRead			
 	
### -field UCHAR [3] Reserved			
 	
### -field ULONG OptimalOpenZoneCount			
 	
### -field ULONG Reserved			
 	
## -remarks

## -see-also