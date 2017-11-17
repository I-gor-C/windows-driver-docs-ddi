---
UID: NS.ndis._NDIS_REQUEST
title: NDIS_REQUEST
author: windows-driver-content
description: 
ms.assetid: d9225b13-236e-49f0-a547-f11fc8e360b2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_REQUEST, NDIS_REQUEST, *PNDIS_REQUEST
req.header: ndis.h
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

# NDIS_REQUEST structure

## -description



## -struct-fields

### -field union DATA			
 	
### -field _DATA _DATA			
 	
### -field union __unnamed_union_0c0c_13			
 	
### -field UCHAR [4 * sizeof(PVOID)] MacReserved			
 	
### -field NDIS_REQUEST_TYPE RequestType			
 	
### -field UCHAR [9 * sizeof(PVOID)] NdisReserved			
 	
### -field UCHAR [2 * sizeof(PVOID)] MiniportReserved			
 	
### -field NDIS_OID Oid			
 	
### -field PVOID InformationBuffer			
 	
### -field UINT InformationBufferLength			
 	
### -field UINT BytesWritten			
 	
### -field UINT BytesNeeded			
 	
### -field NDIS_OID Oid			
 	
### -field PVOID InformationBuffer			
 	
### -field UINT InformationBufferLength			
 	
### -field UINT BytesRead			
 	
### -field UINT BytesNeeded			
 	
### -field UCHAR [2 * sizeof(PVOID)] CallMgrReserved			
 	
### -field UCHAR [2 * sizeof(PVOID)] ProtocolReserved			
 	
## -remarks

## -see-also