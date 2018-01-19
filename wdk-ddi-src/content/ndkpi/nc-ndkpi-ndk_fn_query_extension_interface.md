---
UID : NC:ndkpi.NDK_FN_QUERY_EXTENSION_INTERFACE
title : NDK_FN_QUERY_EXTENSION_INTERFACE
author : windows-driver-content
description : The NdkQqueryExtensionInterface (NDK_FN_QUERY_EXTENSION_INTERFACE) function gets information about an NDK extension interface.
old-location : netvista\ndk_fn_query_extension_interface.htm
old-project : netvista
ms.assetid : 439C990E-6978-4D0F-8453-6EB2FED1DB77
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ndkpi.h
req.include-header : Ndkpi.h
req.target-type : Windows
req.target-min-winverclnt : None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NdkQqueryExtensionInterface
req.alt-loc : ndkpi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <=DISPATCH_LEVEL
req.typenames : NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
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



`*ExtensionInterfaceID`



`ExtensionInterfaceVersion`

The requested version (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>) of the extension interface.

`*pExtensionInterface`




## Return Value

The <i>NdkQqueryExtensionInterface</i> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation completed successfully.
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>The function is not supported.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

## Remarks

Each NDK object contains an <i>NdkQqueryExtensionInterface</i> (<i>NDK_FN_QUERY_EXTENSION_INTERFACE</i>) function pointer in its object type-specific function dispatch table.  <i>NdkQqueryExtensionInterface</i> queries extended interfaces that are supported by the object type. There are currently no standard extended interfaces defined. An extension interface is identified by a GUID and represented as a pointer to a function dispatch table.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndkpi.h (include Ndkpi.h) |
| **Library** |  |
| **IRQL** | <=DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_adapter_dispatch.md">NDK_ADAPTER_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_connector_dispatch.md">NDK_CONNECTOR_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_cq_dispatch.md">NDK_CQ_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_extension_interface.md">NDK_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_query_extension_interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_object_header.md">NDK_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_QUERY_EXTENSION_INTERFACE callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>