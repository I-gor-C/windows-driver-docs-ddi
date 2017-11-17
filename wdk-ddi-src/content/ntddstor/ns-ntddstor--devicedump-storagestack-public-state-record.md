---
UID: NS.ntddstor._DEVICEDUMP_STORAGESTACK_PUBLIC_STATE_RECORD
title: DEVICEDUMP_STORAGESTACK_PUBLIC_STATE_RECORD
author: windows-driver-content
description: 
ms.assetid: 5bc35ec8-4ae6-4ff9-baba-35157b90c0c3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DEVICEDUMP_STORAGESTACK_PUBLIC_STATE_RECORD, DEVICEDUMP_STORAGESTACK_PUBLIC_STATE_RECORD, *PDEVICEDUMP_STORAGESTACK_PUBLIC_STATE_RECORD
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

# DEVICEDUMP_STORAGESTACK_PUBLIC_STATE_RECORD structure

## -description



## -struct-fields

### -field union StackSpecific			
 	
### -field __unnamed_union_0aed_26 __unnamed_union_0aed_26			
 	
### -field UCHAR [CDB_SIZE] Cdb			
 	
### -field UCHAR [TELEMETRY_COMMAND_SIZE] Command			
 	
### -field ULONGLONG StartTime			
 	
### -field ULONGLONG EndTime			
 	
### -field ULONG OperationStatus			
 	
### -field ULONG OperationError			
 	
### -field ULONG dwReserved			
 	
### -field ULONG dwAtaPortSpecific			
 	
### -field ULONG SrbTag			
 	
## -remarks

## -see-also