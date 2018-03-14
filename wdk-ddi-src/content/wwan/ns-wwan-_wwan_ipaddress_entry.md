---
UID: NS:wwan._WWAN_IPADDRESS_ENTRY
title: "_WWAN_IPADDRESS_ENTRY"
author: windows-driver-content
description: The WWAN_IPADDRESS_ENTRY structure represents either the IPV4 or IPV6 address of a PDP context.
old-location: netvista\wwan_ipaddress_entry.htm
old-project: netvista
ms.assetid: 85615799-5AA0-4D83-9246-73F3C7ABFFF6
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_IPADDRESS_ENTRY, PWWAN_IPADDRESS_ENTRY, PWWAN_IPADDRESS_ENTRY structure pointer [Network Drivers Starting with Windows Vista], WWAN_IPADDRESS_ENTRY, WWAN_IPADDRESS_ENTRY structure [Network Drivers Starting with Windows Vista], _WWAN_IPADDRESS_ENTRY, netvista.wwan_ipaddress_entry, wwan/PWWAN_IPADDRESS_ENTRY, wwan/WWAN_IPADDRESS_ENTRY"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8.1 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_IPADDRESS_ENTRY
product: Windows
targetos: Windows
req.typenames: WWAN_IPADDRESS_ENTRY, *PWWAN_IPADDRESS_ENTRY
req.product: Windows 10 or later.
---

# _WWAN_IPADDRESS_ENTRY structure
The WWAN_IPADDRESS_ENTRY structure represents either the IPV4 or IPV6 address of a PDP context.

## Syntax
````
typedef struct _WWAN_IPADDRESS_ENTRY {
  ULONG IsIpv6:1;
  ULONG IsReported:1;
  union {
    WWAN_IPV4_ADDRESS Ipv4;
    WWAN_IPV6_ADDRESS Ipv6;
  };
} WWAN_IPADDRESS_ENTRY, *PWWAN_IPADDRESS_ENTRY;
````

## Members


`IsIpv6`



`IsReported`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 8.1 and later versions of Windows. Available in Windows 8.1 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |