---
UID: NS.minitape._STORAGE_REQUEST_BLOCK
title: STORAGE_REQUEST_BLOCK
author: windows-driver-content
description: 
ms.assetid: 899bd1d4-cded-47c1-aa58-1c90ede81a21
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: STORAGE_REQUEST_BLOCK, STORAGE_REQUEST_BLOCK, *PSTORAGE_REQUEST_BLOCK
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

# STORAGE_REQUEST_BLOCK structure

## -description



## -struct-fields

### -field struct _STORAGE_REQUEST_BLOCK			
 	
### -field _STORAGE_REQUEST_BLOCK POINTER_ALIGN * NextSrb			
 	
### -field USHORT Length			
 	
### -field UCHAR Function			
 	
### -field UCHAR SrbStatus			
 	
### -field UCHAR [4] ReservedUchar			
 	
### -field ULONG Signature			
 	
### -field ULONG Version			
 	
### -field ULONG SrbLength			
 	
### -field ULONG SrbFunction			
 	
### -field ULONG SrbFlags			
 	
### -field ULONG ReservedUlong			
 	
### -field ULONG RequestTag			
 	
### -field USHORT RequestPriority			
 	
### -field USHORT RequestAttribute			
 	
### -field ULONG TimeOutValue			
 	
### -field ULONG SystemStatus			
 	
### -field ULONG ZeroGuard1			
 	
### -field ULONG AddressOffset			
 	
### -field ULONG NumSrbExData			
 	
### -field ULONG DataTransferLength			
 	
### -field PVOID POINTER_ALIGN DataBuffer			
 	
### -field PVOID POINTER_ALIGN ZeroGuard2			
 	
### -field PVOID POINTER_ALIGN OriginalRequest			
 	
### -field PVOID POINTER_ALIGN ClassContext			
 	
### -field PVOID POINTER_ALIGN PortContext			
 	
### -field PVOID POINTER_ALIGN MiniportContext			
 	
### -field ULONG [ANYSIZE_ARRAY] SrbExDataOffset			
 	
## -remarks

## -see-also