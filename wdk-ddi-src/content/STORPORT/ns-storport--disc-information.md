---
UID: NS.storport._DISC_INFORMATION
title: DISC_INFORMATION
author: windows-driver-content
description: 
ms.assetid: ef82c190-fbbd-433b-9089-6088c336dc00
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DISC_INFORMATION, DISC_INFORMATION, *PDISC_INFORMATION
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

# DISC_INFORMATION structure

## -description



## -struct-fields

### -field UCHAR [2] Length			
 	
### -field UCHAR  : 2 DiscStatus			
 	
### -field UCHAR  : 2 LastSessionStatus			
 	
### -field UCHAR  : 1 Erasable			
 	
### -field UCHAR  : 3 Reserved1			
 	
### -field UCHAR FirstTrackNumber			
 	
### -field UCHAR NumberOfSessionsLsb			
 	
### -field UCHAR LastSessionFirstTrackLsb			
 	
### -field UCHAR LastSessionLastTrackLsb			
 	
### -field UCHAR  : 2 MrwStatus			
 	
### -field UCHAR  : 1 MrwDirtyBit			
 	
### -field UCHAR  : 2 Reserved2			
 	
### -field UCHAR  : 1 URU			
 	
### -field UCHAR  : 1 DBC_V			
 	
### -field UCHAR  : 1 DID_V			
 	
### -field UCHAR DiscType			
 	
### -field UCHAR NumberOfSessionsMsb			
 	
### -field UCHAR LastSessionFirstTrackMsb			
 	
### -field UCHAR LastSessionLastTrackMsb			
 	
### -field UCHAR [4] DiskIdentification			
 	
### -field UCHAR [4] LastSessionLeadIn			
 	
### -field UCHAR [4] LastPossibleLeadOutStartTime			
 	
### -field UCHAR [8] DiskBarCode			
 	
### -field UCHAR Reserved4			
 	
### -field UCHAR NumberOPCEntries			
 	
### -field OPC_TABLE_ENTRY [1] OPCTable			
 	
## -remarks

## -see-also