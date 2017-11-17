---
UID: NS.minitape._SCSI_WMI_REQUEST_BLOCK
title: SCSI_WMI_REQUEST_BLOCK
author: windows-driver-content
description: 
ms.assetid: 06a66b2e-10e7-43e7-a3f3-3e952822b01f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SCSI_WMI_REQUEST_BLOCK, SCSI_WMI_REQUEST_BLOCK, *PSCSI_WMI_REQUEST_BLOCK
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

# SCSI_WMI_REQUEST_BLOCK structure

## -description



## -struct-fields

### -field USHORT Length			
 	
### -field UCHAR Function			
 	
### -field UCHAR SrbStatus			
 	
### -field UCHAR WMISubFunction			
 	
### -field UCHAR PathId			
 	
### -field UCHAR TargetId			
 	
### -field UCHAR Lun			
 	
### -field UCHAR Reserved1			
 	
### -field UCHAR WMIFlags			
 	
### -field UCHAR [2] Reserved2			
 	
### -field ULONG SrbFlags			
 	
### -field ULONG DataTransferLength			
 	
### -field ULONG TimeOutValue			
 	
### -field PVOID DataBuffer			
 	
### -field PVOID DataPath			
 	
### -field PVOID Reserved3			
 	
### -field PVOID OriginalRequest			
 	
### -field PVOID SrbExtension			
 	
### -field ULONG Reserved4			
 	
### -field ULONG Reserved6			
 	
### -field UCHAR [16] Reserved5			
 	
## -remarks

## -see-also