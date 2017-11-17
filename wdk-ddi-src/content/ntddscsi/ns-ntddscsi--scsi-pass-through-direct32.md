---
UID: NS.ntddscsi._SCSI_PASS_THROUGH_DIRECT32
title: SCSI_PASS_THROUGH_DIRECT32
author: windows-driver-content
description: 
ms.assetid: b3b1e805-2988-48e5-9ce1-50838874fb44
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SCSI_PASS_THROUGH_DIRECT32, SCSI_PASS_THROUGH_DIRECT32, *PSCSI_PASS_THROUGH_DIRECT32
req.header: ntddscsi.h
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

# SCSI_PASS_THROUGH_DIRECT32 structure

## -description



## -struct-fields

### -field USHORT Length			
 	
### -field UCHAR ScsiStatus			
 	
### -field UCHAR PathId			
 	
### -field UCHAR TargetId			
 	
### -field UCHAR Lun			
 	
### -field UCHAR CdbLength			
 	
### -field UCHAR SenseInfoLength			
 	
### -field UCHAR DataIn			
 	
### -field ULONG DataTransferLength			
 	
### -field ULONG TimeOutValue			
 	
### -field VOID *POINTER_32 DataBuffer			
 	
### -field ULONG SenseInfoOffset			
 	
### -field UCHAR [16] Cdb			
 	
## -remarks

## -see-also