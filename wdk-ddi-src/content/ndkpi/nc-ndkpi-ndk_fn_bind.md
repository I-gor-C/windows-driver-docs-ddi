---
UID : NC:ndkpi.NDK_FN_BIND
title : NDK_FN_BIND
author : windows-driver-content
description : The NdkBind (NDK_FN_BIND) function binds a memory window to a specific sub-region of a memory region (MR).
old-location : netvista\ndk_fn_bind.htm
old-project : netvista
ms.assetid : F363C538-A5D7-4A08-B7CD-CA7D7346AC10
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
req.alt-api : NdkBind
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


# NDK_FN_BIND callback function
The <i>NdkBind</i> (<i>NDK_FN_BIND</i>) function binds a memory window to a specific sub-region of a memory region (MR).

## Syntax

```
NDK_FN_BIND NdkFnBind;

NTSTATUS NdkFnBind(
  NDK_QP *pNdkQp,
  PVOID RequestContext,
  NDK_MR *pMr,
  NDK_MW *pMw,
  PVOID VirtualAddress,
  SIZE_T Length,
  ULONG Flags
)
{...}
```

## Parameters

`*pNdkQp`



`RequestContext`

A context value to return in the <b>RequestContext</b> member of the <a href="..\ndkpi\ns-ndkpi-_ndk_result.md">NDK_RESULT</a> structure for this request.

`*pMr`



`*pMw`



`VirtualAddress`

A virtual address that must be greater than or equal to the virtual address of the MDL for the MR and less than the virtual address of the MDL for the MR plus the value in the <i>Length</i> parameter.

Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a> macro to obtain the virtual address of the MDL for the MR.

`Length`

The length of the MR to bind to the MW.

`Flags`

A bitwise OR of flags which specifies the operations that are allowed. The following flags are supported:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Return Value

The 
     <i>NdkBind</i> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The request was posted successfully. A completion entry will be queued to the CQ when the work request is completed.
<dl>
<dt><b>STATUS_CONNECTION_INVALID</b></dt>
</dl>The queue pair (QP) is not connected.

<dl>
<dt><b>STATUS_ACCESS_VIOLATION</b></dt>
</dl>The memory region does not allow the type of access requested for the memory window. The NDK_OP_FLAG_ALLOW_WRITE  flag requires a memory region that was registered with the NDK_MR_FLAG_ALLOW_LOCAL_WRITE flag.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

## Remarks

<i>NdkBind</i> binds a memory window (MW) to a specific sub-region of a memory region (MR).

The address in the <i>VirtualAddress</i> parameter must be an address within the virtually contiguous region that is described by the MDL chain that was specified during memory registration. The address must be treated by the provider as an index into the memory region. The address must not be used by the provider as a valid virtual address for reading or writing buffer contents.

After this call returns, the remote token will be available with the <i>NdkGetRemotetokenFromMw</i> function (<a href="..\ndkpi\nc-ndkpi-ndk_fn_get_remote_token_from_mw.md">NDK_FN_GET_REMOTE_TOKEN_FROM_MW</a>).

This function does not support a zero-based virtual address.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_get_remote_token_from_mw.md">NDK_FN_GET_REMOTE_TOKEN_FROM_MW</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_mr.md">NDK_MR</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_mw.md">NDK_MW</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_qp.md">NDK_QP</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_result.md">NDK_RESULT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/DA2D0FCA-D84B-4599-A560-8F87A0918D99">NDKPI Deferred Processing Scheme</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2BF6F253-FCB4-4A61-9A67-81092F3C44E4">NDKPI Work Request Posting Requirements</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_BIND callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>