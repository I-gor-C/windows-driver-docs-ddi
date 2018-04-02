---
UID: NS:wwan._WWAN_AUTH_AKAP_CHALLENGE
title: "_WWAN_AUTH_AKAP_CHALLENGE"
author: windows-driver-content
description: The WWAN_AUTH_AKAP_CHALLENGE structure represents an authentication challenge using the AKA' method.
old-location: netvista\wwan_auth_akap_challenge.htm
old-project: netvista
ms.assetid: 0C1862D6-1252-4CF7-926A-C4647D545255
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_AUTH_AKAP_CHALLENGE, PWWAN_AUTH_AKAP_CHALLENGE, PWWAN_AUTH_AKAP_CHALLENGE structure pointer [Network Drivers Starting with Windows Vista], WWAN_AUTH_AKAP_CHALLENGE, WWAN_AUTH_AKAP_CHALLENGE structure [Network Drivers Starting with Windows Vista], _WWAN_AUTH_AKAP_CHALLENGE, netvista.wwan_auth_akap_challenge, wwan/PWWAN_AUTH_AKAP_CHALLENGE, wwan/WWAN_AUTH_AKAP_CHALLENGE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
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
-	WWAN_AUTH_AKAP_CHALLENGE
product: Windows
targetos: Windows
req.typenames: WWAN_AUTH_AKAP_CHALLENGE, *PWWAN_AUTH_AKAP_CHALLENGE
req.product: Windows 10 or later.
---

# _WWAN_AUTH_AKAP_CHALLENGE structure
The WWAN_AUTH_AKAP_CHALLENGE structure represents an authentication challenge using the AKA' method.

## Syntax
```
typedef struct _WWAN_AUTH_AKAP_CHALLENGE {
  BYTE  Rand[WWAN_AUTH_RAND_LEN];
  BYTE  Autn[WWAN_AUTH_AUTN_LEN];
  BYTE  NetworkName[WWAN_AUTH_NETWORK_NAME_MAX_LEN];
  ULONG NetworkNameLength;
} WWAN_AUTH_AKAP_CHALLENGE, *PWWAN_AUTH_AKAP_CHALLENGE;
```

## Members


`Rand`



`Autn`



`NetworkName`



`NetworkNameLength`

The length, in bytes, of the access network  returned in <b>NetworkName</b>.

## Remarks
The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464127">WWAN_AUTH_CHALLENGE</a> structure uses this structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with  Windows 8. Supported starting with  Windows 8. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh464127">WWAN_AUTH_CHALLENGE</a>