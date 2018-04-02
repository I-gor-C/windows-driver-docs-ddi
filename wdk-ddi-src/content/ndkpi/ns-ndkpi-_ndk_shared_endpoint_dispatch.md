---
UID: NS:ndkpi._NDK_SHARED_ENDPOINT_DISPATCH
title: "_NDK_SHARED_ENDPOINT_DISPATCH"
author: windows-driver-content
description: The NDK_SHARED_ENDPOINT_DISPATCH structure specifies dispatch function entry points for the NDK shared endpoint object.
old-location: netvista\ndk_shared_endpoint_dispatch.htm
old-project: netvista
ms.assetid: A0AFCF2B-E1A9-478C-8B03-D7C873F83369
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDK_SHARED_ENDPOINT_DISPATCH, NDK_SHARED_ENDPOINT_DISPATCH structure [Network Drivers Starting with Windows Vista], _NDK_SHARED_ENDPOINT_DISPATCH, ndkpi/NDK_SHARED_ENDPOINT_DISPATCH, netvista.ndk_shared_endpoint_dispatch
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
-	HeaderDef
api_location:
-	ndkpi.h
api_name:
-	NDK_SHARED_ENDPOINT_DISPATCH
product: Windows
targetos: Windows
req.typenames: NDK_SHARED_ENDPOINT_DISPATCH
---

# _NDK_SHARED_ENDPOINT_DISPATCH structure
The <b>NDK_SHARED_ENDPOINT_DISPATCH</b> structure specifies dispatch function entry points for the NDK shared endpoint object.

## Syntax
```
typedef struct _NDK_SHARED_ENDPOINT_DISPATCH {
  NDK_FN_CLOSE_OBJECT                      NdkCloseSharedEndpoint;
  NDK_FN_QUERY_EXTENSION_INTERFACE         NdkQueryExtension;
  NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS NdkGetLocalAddress;
} NDK_SHARED_ENDPOINT_DISPATCH;
```

## Members


`NdkCloseSharedEndpoint`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a> dispatch function.

`NdkQueryExtension`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.

`NdkGetLocalAddress`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439899">NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS</a> dispatch function.

## Remarks
The <b>NDK_SHARED_ENDPOINT_DISPATCH</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. None supported,Supported in NDIS 6.30 and later. |
| **Header** | ndkpi.h (include Ndkpi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439899">NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>