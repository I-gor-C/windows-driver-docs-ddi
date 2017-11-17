---
UID: NS.storport._DISK_INFORMATION
title: DISK_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 23711476-f047-4feb-a01e-684154c29571
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DISK_INFORMATION, DISK_INFORMATION, *PDISK_INFORMATION
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

# DISK_INFORMATION structure

## -description



## -struct-fields

### -field UCHAR [2] Length			
 	
### -field UCHAR  : 2 DiskStatus			
 	
### -field UCHAR  : 2 LastSessionStatus			
 	
### -field UCHAR  : 1 Erasable			
 	
### -field UCHAR  : 3 Reserved1			
 	
### -field UCHAR FirstTrackNumber			
 	
### -field UCHAR NumberOfSessions			
 	
### -field UCHAR LastSessionFirstTrack			
 	
### -field UCHAR LastSessionLastTrack			
 	
### -field UCHAR  : 5 Reserved2			
 	
### -field UCHAR  : 1 GEN			
 	
### -field UCHAR  : 1 DBC_V			
 	
### -field UCHAR  : 1 DID_V			
 	
### -field UCHAR DiskType			
 	
### -field UCHAR [3] Reserved3			
 	
### -field UCHAR [4] DiskIdentification			
 	
### -field UCHAR [4] LastSessionLeadIn			
 	
### -field UCHAR [4] LastPossibleStartTime			
 	
### -field UCHAR [8] DiskBarCode			
 	
### -field UCHAR Reserved4			
 	
### -field UCHAR NumberOPCEntries			
 	
### -field OPC_TABLE_ENTRY [0] OPCTable			
 	
## -remarks

## -see-also