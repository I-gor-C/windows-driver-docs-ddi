---
UID: NS.ntddscsi._ATA_PASS_THROUGH_DIRECT32
title: ATA_PASS_THROUGH_DIRECT32
author: windows-driver-content
description: 
ms.assetid: 592988fe-b225-43df-8f9c-f70da5e79721
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ATA_PASS_THROUGH_DIRECT32, ATA_PASS_THROUGH_DIRECT32, *PATA_PASS_THROUGH_DIRECT32
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

# ATA_PASS_THROUGH_DIRECT32 structure

## -description



## -struct-fields

### -field USHORT Length			
 	
### -field USHORT AtaFlags			
 	
### -field UCHAR PathId			
 	
### -field UCHAR TargetId			
 	
### -field UCHAR Lun			
 	
### -field UCHAR ReservedAsUchar			
 	
### -field ULONG DataTransferLength			
 	
### -field ULONG TimeOutValue			
 	
### -field ULONG ReservedAsUlong			
 	
### -field VOID *POINTER_32 DataBuffer			
 	
### -field UCHAR [8] PreviousTaskFile			
 	
### -field UCHAR [8] CurrentTaskFile			
 	
## -remarks

## -see-also