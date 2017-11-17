---
UID: NS.minitape._SCSI_PNP_REQUEST_BLOCK
title: SCSI_PNP_REQUEST_BLOCK
author: windows-driver-content
description: 
ms.assetid: 2a97c7f3-d138-43ba-92b0-38607ae4125d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SCSI_PNP_REQUEST_BLOCK, SCSI_PNP_REQUEST_BLOCK, *PSCSI_PNP_REQUEST_BLOCK
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

# SCSI_PNP_REQUEST_BLOCK structure

## -description



## -struct-fields

### -field struct _SCSI_REQUEST_BLOCK			
 	
### -field _SCSI_REQUEST_BLOCK * NextSrb			
 	
### -field USHORT Length			
 	
### -field UCHAR Function			
 	
### -field UCHAR SrbStatus			
 	
### -field UCHAR PnPSubFunction			
 	
### -field UCHAR PathId			
 	
### -field UCHAR TargetId			
 	
### -field UCHAR Lun			
 	
### -field STOR_PNP_ACTION PnPAction			
 	
### -field ULONG SrbFlags			
 	
### -field ULONG DataTransferLength			
 	
### -field ULONG TimeOutValue			
 	
### -field PVOID DataBuffer			
 	
### -field PVOID SenseInfoBuffer			
 	
### -field PVOID OriginalRequest			
 	
### -field PVOID SrbExtension			
 	
### -field ULONG SrbPnPFlags			
 	
### -field ULONG Reserved			
 	
### -field UCHAR [16] Reserved4			
 	
## -remarks

## -see-also