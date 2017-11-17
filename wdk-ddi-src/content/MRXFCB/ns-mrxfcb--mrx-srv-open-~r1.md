---
UID: NS.mrxfcb._MRX_SRV_OPEN_~r1
title: MRX_SRV_OPEN_
author: windows-driver-content
description: 
ms.assetid: e275b903-6b7b-4e2a-aca5-42bd3ff3566d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MRX_SRV_OPEN_, MRX_SRV_OPEN, *PMRX_SRV_OPEN
req.header: mrxfcb.h
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

# MRX_SRV_OPEN_ structure

## -description



## -struct-fields

### -field PMRX_FCB pFcb			
 	
### -field PMRX_V_NET_ROOT pVNetRoot			
 	
### -field PVOID Context			
 	
### -field PVOID Context2			
 	
### -field PMRXSHADOW_SRV_OPEN ShadowContext			
 	
### -field ULONG Flags			
 	
### -field PUNICODE_STRING pAlreadyPrefixedName			
 	
### -field CLONG UncleanFobxCount			
 	
### -field CLONG OpenCount			
 	
### -field PVOID Key			
 	
### -field ACCESS_MASK DesiredAccess			
 	
### -field ULONG ShareAccess			
 	
### -field ULONG CreateOptions			
 	
### -field ULONG BufferingFlags			
 	
### -field ULONG ulFileSizeVersion			
 	
### -field LIST_ENTRY SrvOpenQLinks			
 	
## -remarks

## -see-also