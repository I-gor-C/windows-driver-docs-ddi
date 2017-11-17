---
UID: NS.ntdddisk._DISK_SNAPSHOT_INFO
title: DISK_SNAPSHOT_INFO
author: windows-driver-content
description: 
ms.assetid: 9e4ff028-3ee7-4e23-9f79-79e47e6f6ba7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DISK_SNAPSHOT_INFO, DISK_SNAPSHOT_INFO, *PDISK_SNAPSHOT_INFO
req.header: ntdddisk.h
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

# DISK_SNAPSHOT_INFO structure

## -description



## -struct-fields

### -field ULONG Version			
 	
### -field DISK_SNAPSHOT_STATE State			
 	
### -field GUID SnapshotSetId			
 	
### -field GUID SnapshotId			
 	
### -field GUID LunId			
 	
### -field LARGE_INTEGER CreationTimeStamp			
 	
### -field ULONG ImportCount			
 	
### -field ULONG Flags			
 	
### -field ULONG AdditionalDataSize			
 	
### -field UCHAR [ANYSIZE_ARRAY] AdditionalData			
 	
## -remarks

## -see-also