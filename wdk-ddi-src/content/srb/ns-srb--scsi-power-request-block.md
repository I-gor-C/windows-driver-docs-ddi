---
UID: NS.srb._SCSI_POWER_REQUEST_BLOCK
title: SCSI_POWER_REQUEST_BLOCK
author: windows-driver-content
description: 
ms.assetid: a941e10b-3a6c-41f4-a8cb-0fd555f6eb6e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SCSI_POWER_REQUEST_BLOCK, SCSI_POWER_REQUEST_BLOCK, *PSCSI_POWER_REQUEST_BLOCK
req.header: srb.h
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

# SCSI_POWER_REQUEST_BLOCK structure

## -description



## -struct-fields

### -field struct _SCSI_REQUEST_BLOCK			
 	
### -field _SCSI_REQUEST_BLOCK * NextSrb			
 	
### -field USHORT Length			
 	
### -field UCHAR Function			
 	
### -field UCHAR SrbStatus			
 	
### -field UCHAR SrbPowerFlags			
 	
### -field UCHAR PathId			
 	
### -field UCHAR TargetId			
 	
### -field UCHAR Lun			
 	
### -field STOR_DEVICE_POWER_STATE DevicePowerState			
 	
### -field ULONG SrbFlags			
 	
### -field ULONG DataTransferLength			
 	
### -field ULONG TimeOutValue			
 	
### -field PVOID DataBuffer			
 	
### -field PVOID SenseInfoBuffer			
 	
### -field PVOID OriginalRequest			
 	
### -field PVOID SrbExtension			
 	
### -field STOR_POWER_ACTION PowerAction			
 	
### -field ULONG Reserved			
 	
### -field UCHAR [16] Reserved5			
 	
## -remarks

## -see-also