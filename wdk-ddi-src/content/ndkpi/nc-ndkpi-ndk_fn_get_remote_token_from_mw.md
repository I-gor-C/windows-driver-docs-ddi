---
UID: NC:ndkpi.NDK_FN_GET_REMOTE_TOKEN_FROM_MW
title: NDK_FN_GET_REMOTE_TOKEN_FROM_MW
author: windows-driver-content
description: The NdkGetRemoteTokenFromMw (NDK_FN_GET_REMOTE_TOKEN_FROM_MW) function gets a memory token from a remote NDK memory window (MW).
old-location: netvista\ndk_fn_get_remote_token_from_mw.htm
old-project: netvista
ms.assetid: 893B53DA-B858-4E21-9DD9-D244702ACF46
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NDK_FN_GET_REMOTE_TOKEN_FROM_MW, NdkGetRemoteTokenFromMw, NdkGetRemoteTokenFromMw callback function [Network Drivers Starting with Windows Vista], ndkpi/NdkGetRemoteTokenFromMw, netvista.ndk_fn_get_remote_token_from_mw
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
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
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ndkpi.h
api_name:
-	NdkGetRemoteTokenFromMw
product: Windows
targetos: Windows
req.typenames: NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
---


# NDK_FN_GET_REMOTE_TOKEN_FROM_MW callback function
The <i>NdkGetRemoteTokenFromMw</i> (<i>NDK_FN_GET_REMOTE_TOKEN_FROM_MW</i>) function gets a memory token from a remote NDK memory window (MW).

## Syntax

```
NDK_FN_GET_REMOTE_TOKEN_FROM_MW NdkFnGetRemoteTokenFromMw;

UINT32 NdkFnGetRemoteTokenFromMw(
  NDK_MW *pNdkMw
)
{...}
```

## Parameters

`*pNdkMw`

A pointer to an NDK memory window (MW) object (<a href="..\ndkpi\ns-ndkpi-_ndk_mw.md">NDK_MW</a>).


## Return Value

The 
     <i>NdkGetRemoteTokenFromMw</i> function returns a remote memory region token.

## Remarks

After an <i>NdkBind</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_bind.md">NDK_FN_BIND</a>) call returns control to the caller, <i>NdkGetRemoteTokenFromMw</i> can be called to retrieve the remote token.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. Windows Server 2012 |
| **Target Platform** | Windows |
| **Header** | ndkpi.h (include Ndkpi.h) |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="..\ndkpi\nc-ndkpi-ndk_fn_bind.md">NDK_FN_BIND</a>



<a href="..\ndkpi\ns-ndkpi-_ndk_mw.md">NDK_MW</a>