---
UID: NS.ntddnlb._QUERY_HOOK_INFO
title: QUERY_HOOK_INFO
author: windows-driver-content
description: 
ms.assetid: 914e7655-9808-4eb2-9022-87ff7e2c0928
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: QUERY_HOOK_INFO, QUERY_HOOK_INFO, *PQUERY_HOOK_INFO
req.header: ntddnlb.h
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

# QUERY_HOOK_INFO structure

## -description



## -struct-fields

### -field NLB_HOOK_API_VERSION Version			
 	
### -field const WCHAR * pAdapter			
 	
### -field IF_INDEX IFIndex			
 	
### -field ADDRESS_FAMILY AddressFamily			
 	
### -field const UCHAR * ServerIPAddress			
 	
### -field USHORT ServerPort			
 	
### -field const UCHAR * ClientIPAddress			
 	
### -field USHORT ClientPort			
 	
### -field USHORT Protocol			
 	
### -field BOOLEAN bReceiveContext			
 	
### -field ULONG Flags			
 	
### -field VOID * Reserved			
 	
### -field NLB_HOOK_IP_TUPLE NewTuple			
 	
## -remarks

## -see-also