---
UID: NS.minitape._SRBEX_DATA_SCSI_CDB_VAR
title: SRBEX_DATA_SCSI_CDB_VAR
author: windows-driver-content
description: 
ms.assetid: d79c382b-156d-403a-9b0c-b44aafb99509
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SRBEX_DATA_SCSI_CDB_VAR, SRBEX_DATA_SCSI_CDB_VAR, *PSRBEX_DATA_SCSI_CDB_VAR
req.header: minitape.h
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

# SRBEX_DATA_SCSI_CDB_VAR structure

## -description



## -struct-fields

### -field SRBEXDATATYPE Type			
 	
### -field ULONG Length			
 	
### -field UCHAR ScsiStatus			
 	
### -field UCHAR SenseInfoBufferLength			
 	
### -field UCHAR [2] Reserved			
 	
### -field ULONG CdbLength			
 	
### -field ULONG [2] Reserved1			
 	
### -field PVOID POINTER_ALIGN SenseInfoBuffer			
 	
### -field UCHAR POINTER_ALIGN [ANYSIZE_ARRAY] Cdb			
 	
## -remarks

## -see-also