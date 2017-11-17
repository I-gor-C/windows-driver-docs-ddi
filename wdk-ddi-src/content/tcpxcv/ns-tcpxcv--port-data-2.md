---
UID: NS.tcpxcv._PORT_DATA_2
title: PORT_DATA_2
author: windows-driver-content
description: 
ms.assetid: 2a404371-5e4a-45c1-b57b-84d3ce1e879f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PORT_DATA_2, PORT_DATA_2, *PPORT_DATA_2
req.header: tcpxcv.h
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

# PORT_DATA_2 structure

## -description



## -struct-fields

### -field WCHAR [MAX_PORTNAME_LEN] sztPortName			
 	
### -field DWORD dwVersion			
 	
### -field DWORD dwProtocol			
 	
### -field DWORD cbSize			
 	
### -field DWORD dwReserved			
 	
### -field WCHAR [MAX_NETWORKNAME2_LEN] sztHostAddress			
 	
### -field WCHAR [MAX_SNMP_COMMUNITY_STR_LEN] sztSNMPCommunity			
 	
### -field DWORD dwDoubleSpool			
 	
### -field WCHAR [MAX_QUEUENAME_LEN] sztQueue			
 	
### -field BYTE [514] Reserved			
 	
### -field DWORD dwPortNumber			
 	
### -field DWORD dwSNMPEnabled			
 	
### -field DWORD dwSNMPDevIndex			
 	
### -field DWORD dwPortMonitorMibIndex			
 	
## -remarks

## -see-also