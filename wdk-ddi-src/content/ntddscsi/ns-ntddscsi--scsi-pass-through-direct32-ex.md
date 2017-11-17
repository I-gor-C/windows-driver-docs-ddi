---
UID: NS.ntddscsi._SCSI_PASS_THROUGH_DIRECT32_EX
title: SCSI_PASS_THROUGH_DIRECT32_EX
author: windows-driver-content
description: 
ms.assetid: 3a8d390f-90ba-48ae-86e6-a91cfe399b8a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SCSI_PASS_THROUGH_DIRECT32_EX, SCSI_PASS_THROUGH_DIRECT32_EX, *PSCSI_PASS_THROUGH_DIRECT32_EX
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

# SCSI_PASS_THROUGH_DIRECT32_EX structure

## -description



## -struct-fields

### -field ULONG Version			
 	
### -field ULONG Length			
 	
### -field ULONG CdbLength			
 	
### -field ULONG StorAddressLength			
 	
### -field UCHAR ScsiStatus			
 	
### -field UCHAR SenseInfoLength			
 	
### -field UCHAR DataDirection			
 	
### -field UCHAR Reserved			
 	
### -field ULONG TimeOutValue			
 	
### -field ULONG StorAddressOffset			
 	
### -field ULONG SenseInfoOffset			
 	
### -field ULONG DataOutTransferLength			
 	
### -field ULONG DataInTransferLength			
 	
### -field VOID *POINTER_32 DataOutBuffer			
 	
### -field VOID *POINTER_32 DataInBuffer			
 	
### -field UCHAR [ANYSIZE_ARRAY] Cdb			
 	
## -remarks

## -see-also