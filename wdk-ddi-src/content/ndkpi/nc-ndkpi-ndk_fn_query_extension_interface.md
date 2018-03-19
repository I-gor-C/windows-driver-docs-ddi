---
UID: NC:ndkpi.NDK_FN_QUERY_EXTENSION_INTERFACE
title: NDK_FN_QUERY_EXTENSION_INTERFACE
author: windows-driver-content
description: The NdkQqueryExtensionInterface (NDK_FN_QUERY_EXTENSION_INTERFACE) function gets information about an NDK extension interface.
old-location: netvista\ndk_fn_query_extension_interface.htm
old-project: netvista
ms.assetid: 439C990E-6978-4D0F-8453-6EB2FED1DB77
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NDK_FN_QUERY_EXTENSION_INTERFACE, NdkQqueryExtensionInterface, NdkQqueryExtensionInterface callback function [Network Drivers Starting with Windows Vista], ndkpi/NdkQqueryExtensionInterface, netvista.ndk_fn_query_extension_interface
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
-	NdkQqueryExtensionInterface
product: Windows
targetos: Windows
req.typenames: NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
---


# NDK_FN_QUERY_EXTENSION_INTERFACE callback function
The <i>NdkQqueryExtensionInterface</i> (<i>NDK_FN_QUERY_EXTENSION_INTERFACE</i>) function gets information about an NDK extension interface.

## Syntax

```
NDK_FN_QUERY_EXTENSION_INTERFACE NdkFnQueryExtensionInterface;

NTSTATUS NdkFnQueryExtensionInterface(
  NDK_OBJECT_HEADER *pNdkObject,
  GUID *ExtensionInterfaceID,
  NDK_VERSION ExtensionInterfaceVersion,
  NDK_EXTENSION_INTERFACE *pExtensionInterface
)
{...}
```

## Parameters

`*pNdkObject`

A pointer to the object header (<a href="..\ndkpi\ns-ndkpi-_ndk_object_header.md">NDK_OBJECT_HEADER</a>) for the object being queried.

`*ExtensionInterfaceID`

A pointer to the GUID that identifies the extension interface.

`ExtensionInterfaceVersion`

The requested version (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>) of the extension interface.

`*pExtensionInterface`

A pointer to an   <a href="..\ndkpi\ns-ndkpi-_ndk_extension_interface.md">NDK_EXTENSION_INTERFACE</a> structure that the provider  initialized if the function returns STATUS_SUCCESS.


## Return Value

The <i>NdkQqueryExtensionInterface</i> function returns one of the following NTSTATUS codes.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The operation completed successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>
</td>
<td width="60%">
The function is not supported.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>Other status codes</b></dt>
</dl>
</td>
<td width="60%">
An error occurred. 

</td>
</tr>
</table>

## Remarks

Each NDK object contains an <i>NdkQqueryExtensionInterface</i> (<i>NDK_FN_QUERY_EXTENSION_INTERFACE</i>) function pointer in its object type-specific function dispatch table.  <i>NdkQqueryExtensionInterface</i> queries extended interfaces that are supported by the object type. There are currently no standard extended interfaces defined. An extension interface is identified by a GUID and represented as a pointer to a function dispatch table.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. Windows Server 2012 |
| **Target Platform** | Windows |
| **Header** | ndkpi.h (include Ndkpi.h) |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="..\ndkpi\ns-ndkpi-_ndk_connector_dispatch.md">NDK_CONNECTOR_DISPATCH</a>



<a href="..\ndkpi\ns-ndkpi-_ndk_adapter_dispatch.md">NDK_ADAPTER_DISPATCH</a>



<a href="..\ndkpi\ns-ndkpi-_ndk_extension_interface.md">NDK_EXTENSION_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>



<a href="..\ndkpi\nc-ndkpi-ndk_fn_query_extension_interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>



<a href="..\ndkpi\ns-ndkpi-_ndk_object_header.md">NDK_OBJECT_HEADER</a>



<a href="..\ndkpi\ns-ndkpi-_ndk_cq_dispatch.md">NDK_CQ_DISPATCH</a>