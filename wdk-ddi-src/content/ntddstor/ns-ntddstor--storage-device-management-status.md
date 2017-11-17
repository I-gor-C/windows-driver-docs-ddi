---
UID: NS.ntddstor._STORAGE_DEVICE_MANAGEMENT_STATUS
title: STORAGE_DEVICE_MANAGEMENT_STATUS
author: windows-driver-content
description: 
ms.assetid: b74ba2ae-dd4b-479e-8714-b2c45b93cfed
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: STORAGE_DEVICE_MANAGEMENT_STATUS, STORAGE_DEVICE_MANAGEMENT_STATUS, *PSTORAGE_DEVICE_MANAGEMENT_STATUS
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

# STORAGE_DEVICE_MANAGEMENT_STATUS structure

## -description



## -struct-fields

### -field ULONG Version			
 	
### -field ULONG Size			
 	
### -field STORAGE_DISK_HEALTH_STATUS Health			
 	
### -field ULONG NumberOfOperationalStatus			
 	
### -field ULONG NumberOfAdditionalReasons			
 	
### -field STORAGE_DISK_OPERATIONAL_STATUS [STORAGE_DEVICE_MAX_OPERATIONAL_STATUS] OperationalStatus			
 	
### -field STORAGE_OPERATIONAL_REASON [ANYSIZE_ARRAY] AdditionalReasons			
 	
## -remarks

## -see-also