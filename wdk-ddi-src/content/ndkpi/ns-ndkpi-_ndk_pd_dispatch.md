---
UID: NS:ndkpi._NDK_PD_DISPATCH
title: "_NDK_PD_DISPATCH"
author: windows-driver-content
description: The NDK_PD_DISPATCH structure specifies dispatch function entry points for the NDK protection domain (PD) object.
old-location: netvista\ndk_pd_dispatch.htm
old-project: netvista
ms.assetid: 3BAD6CF9-8DCD-470F-9C2E-C7C9C0B29ADA
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDK_PD_DISPATCH, NDK_PD_DISPATCH structure [Network Drivers Starting with Windows Vista], _NDK_PD_DISPATCH, ndkpi/NDK_PD_DISPATCH, netvista.ndk_pd_dispatch
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
-	NDK_PD_DISPATCH
product: Windows
targetos: Windows
req.typenames: NDK_PD_DISPATCH
---

# _NDK_PD_DISPATCH structure
The <b>NDK_PD_DISPATCH</b> structure specifies dispatch function entry points for the NDK protection domain (PD) object.

## Syntax
```
typedef struct _NDK_PD_DISPATCH {
  NDK_FN_CLOSE_OBJECT                       NdkClosePd;
  NDK_FN_QUERY_EXTENSION_INTERFACE          NdkQueryExtension;
  NDK_FN_CREATE_MR                          NdkCreateMr;
  NDK_FN_CREATE_MW                          NdkCreateMw;
  NDK_FN_CREATE_SRQ                         NdkCreateSrq;
  NDK_FN_CREATE_QP                          NdkCreateQp;
  NDK_FN_CREATE_QP_WITH_SRQ                 NdkCreateQpWithSrq;
  NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN NdkGetPrivilegedMemoryRegionToken;
} NDK_PD_DISPATCH;
```

## Members


`NdkClosePd`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a> dispatch function.

`NdkQueryExtension`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.

`NdkCreateMr`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439875">NDK_FN_CREATE_MR</a> dispatch function.

`NdkCreateMw`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439876">NDK_FN_CREATE_MW</a> dispatch function.

`NdkCreateSrq`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439883">NDK_FN_CREATE_SRQ</a> dispatch function.

`NdkCreateQp`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439878">NDK_FN_CREATE_QP</a> dispatch function.

`NdkCreateQpWithSrq`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439880">NDK_FN_CREATE_QP_WITH_SRQ</a> dispatch function.

`NdkGetPrivilegedMemoryRegionToken`

The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439896">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a> dispatch function.

## Remarks
The <b>NDK_PD_DISPATCH</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. None supported,Supported in NDIS 6.30 and later. |
| **Header** | ndkpi.h (include Ndkpi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439875">NDK_FN_CREATE_MR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439876">NDK_FN_CREATE_MW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439878">NDK_FN_CREATE_QP</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439880">NDK_FN_CREATE_QP_WITH_SRQ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439883">NDK_FN_CREATE_SRQ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439896">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>