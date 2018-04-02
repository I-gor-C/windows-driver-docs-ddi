---
UID: NS:ndkpi._NDK_LISTENER_DISPATCH
title: "_NDK_LISTENER_DISPATCH"
author: windows-driver-content
description: The NDK_LISTENER_DISPATCH structure specifies dispatch function entry points for the NDK listener object.
old-location: netvista\ndk_listener_dispatch.htm
old-project: netvista
ms.assetid: CF44B920-428A-4CD0-94BF-15F80189D9C3
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDK_LISTENER_DISPATCH, NDK_LISTENER_DISPATCH structure [Network Drivers Starting with Windows Vista], PNDK_LISTENER_DISPATCH, PNDK_LISTENER_DISPATCH structure pointer [Network Drivers Starting with Windows Vista], _NDK_LISTENER_DISPATCH, ndkpi/NDK_LISTENER_DISPATCH, ndkpi/PNDK_LISTENER_DISPATCH, netvista.ndk_listener_dispatch
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
-	NDK_LISTENER_DISPATCH
product: Windows
targetos: Windows
req.typenames: NDK_LISTENER_DISPATCH
---

# _NDK_LISTENER_DISPATCH structure
The <b>NDK_LISTENER_DISPATCH</b> structure specifies dispatch function entry points for the NDK listener object.

## Syntax
```
typedef struct _NDK_LISTENER_DISPATCH {
  NDK_FN_CLOSE_OBJECT               NdkCloseListener;
  NDK_FN_QUERY_EXTENSION_INTERFACE  NdkQueryExtension;
  NDK_FN_LISTEN                     NdkListen;
  NDK_FN_GET_LISTENER_LOCAL_ADDRESS NdkGetLocalAddress;
  NDK_FN_CONTROL_CONNECT_EVENTS     NdkControlConnectEvents;
} NDK_LISTENER_DISPATCH;
```

## Members


`NdkCloseListener`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a> dispatch function.

`NdkQueryExtension`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.

`NdkListen`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439902">NDK_FN_LISTEN</a> dispatch function.

`NdkGetLocalAddress`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439892">NDK_FN_GET_LISTENER_LOCAL_ADDRESS</a> dispatch function.

`NdkControlConnectEvents`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439869">NDK_FN_CONTROL_CONNECT_EVENTS</a> dispatch function.

## Remarks
The <b>NDK_LISTENER_DISPATCH</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. None supported,Supported in NDIS 6.30 and later. |
| **Header** | ndkpi.h (include Ndkpi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439869">NDK_FN_CONTROL_CONNECT_EVENTS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439892">NDK_FN_GET_LISTENER_LOCAL_ADDRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439902">NDK_FN_LISTEN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>