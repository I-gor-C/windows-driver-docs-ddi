---
UID: NS:wwan._WWAN_AUTH_SIM_RESPONSE
title: "_WWAN_AUTH_SIM_RESPONSE"
author: windows-driver-content
description: The WWAN_AUTH_SIM_RESPONSE structure represents a response to a SIM authentication challenge.
old-location: netvista\wwan_auth_sim_response.htm
old-project: netvista
ms.assetid: C259CA95-D119-47EB-A32D-9C9E284B6CD4
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_AUTH_SIM_RESPONSE, PWWAN_AUTH_SIM_RESPONSE, PWWAN_AUTH_SIM_RESPONSE structure pointer [Network Drivers Starting with Windows Vista], WWAN_AUTH_SIM_RESPONSE, WWAN_AUTH_SIM_RESPONSE structure [Network Drivers Starting with Windows Vista], _WWAN_AUTH_SIM_RESPONSE, netvista.wwan_auth_sim_response, wwan/PWWAN_AUTH_SIM_RESPONSE, wwan/WWAN_AUTH_SIM_RESPONSE"
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
-	WWAN_AUTH_SIM_RESPONSE
product: Windows
targetos: Windows
req.typenames: WWAN_AUTH_SIM_RESPONSE, *PWWAN_AUTH_SIM_RESPONSE
req.product: Windows 10 or later.
---

# _WWAN_AUTH_SIM_RESPONSE structure
The WWAN_AUTH_SIM_RESPONSE structure represents a response to a SIM authentication challenge.

## Syntax
````
typedef struct _WWAN_AUTH_SIM_RESPONSE {
  BYTE  Sres1[WWAN_AUTH_SRES_LEN];
  BYTE  Kc1[WWAN_AUTH_KC_LEN];
  BYTE  Sres2[WWAN_AUTH_SRES_LEN];
  BYTE  Kc2[WWAN_AUTH_KC_LEN];
  BYTE  Sres3[WWAN_AUTH_SRES_LEN];
  BYTE  Kc3[WWAN_AUTH_KC_LEN];
  ULONG n;
} WWAN_AUTH_SIM_RESPONSE, *PWWAN_AUTH_SIM_RESPONSE;
````

## Members


`Sres1`



`Kc1`



`Sres2`



`Kc2`



`Sres3`



`Kc3`



`n`

The number of responses.

## Remarks
The <b>n</b> member can be either <b>2</b> or <b>3</b>, according to RFC 4186. If it is set to <b>2</b>, use the <b>Sres1</b>/<b>Kc1</b> and <b>Sres2</b>/<b>Kc2</b> members. If it is set to <b>3</b>,use <b>Sres1</b>/<b>Kc1</b>, <b>Sres2</b>/<b>Kc2</b>, and <b>Sres3</b>/<b>Kc3</b> members.

The <a href="..\wwan\ns-wwan-_wwan_auth_response.md">WWAN_AUTH_RESPONSE</a> structure uses this structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with  Windows 8. Supported starting with  Windows 8. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_auth_response.md">WWAN_AUTH_RESPONSE</a>