---
UID : NC:ndkpi.NDK_FN_CREATE_SRQ
title : NDK_FN_CREATE_SRQ
author : windows-driver-content
description : The NdkCreateSrq (NDK_FN_CREATE_SRQ) function creates an NDK shared receive queue (SRQ) object.
old-location : netvista\ndk_fn_create_srq.htm
old-project : netvista
ms.assetid : 83125C65-021F-4EEE-8819-B73752908DE7
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
req.alt-api : NdkCreateSrq
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


# NDK_FN_CREATE_SRQ callback function
The <i>NdkCreateSrq</i> (<i>NDK_FN_CREATE_SRQ</i>) function creates an NDK shared receive queue (SRQ) object.

## Syntax

```
NDK_FN_CREATE_SRQ NdkFnCreateSrq;

NTSTATUS NdkFnCreateSrq(
  NDK_PD *pNdkPd,
  ULONG SrqDepth,
  ULONG MaxReceiveRequestSge,
  ULONG NotifyThreshold,
  NDK_FN_SRQ_NOTIFICATION_CALLBACK SrqNotification,
  PVOID SrqNotificationContext,
  GROUP_AFFINITY *Affinity,
  NDK_FN_CREATE_COMPLETION CreateCompletion,
  PVOID RequestContext,
  NDK_SRQ **ppNdkSrq
)
{...}
```

## Parameters

`*pNdkPd`



`SrqDepth`

The maximum number of receive requests that can be outstanding over the SRQ. This value  must be less than or equal to the value in the <b>MaxSrqDepth</b> member that is specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure.

`MaxReceiveRequestSge`

The maximum number of SGEs that are supported in a single receive request. This value must be less than or equal to the value in the <b>MaxReceiveRequestSge</b> member that is specified in the NDK_ADAPTER_INFO structure.

`NotifyThreshold`

The minimum number of queued receive requests for triggering SRQ notification callbacks.

`SrqNotification`

An optional <i>NdkSrqNotificationCallback</i> function(<a href="..\ndkpi\nc-ndkpi-ndk_fn_srq_notification_callback.md">NDK_FN_SRQ_NOTIFICATION_CALLBACK</a>) which the provider calls if the  queued receive request count falls below the threshold that is specified in the  <i>NotifyThreshold</i> parameter.

`SrqNotificationContext`

A context value that the NDK provider passes back to the <i>NdkSrqNotificationCallback</i> function that is specified in the <i>SrqNotification</i> parameter.

`*Affinity`



`CreateCompletion`

A pointer to an <i>NdkCreateCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_completion.md">NDK_FN_CREATE_COMPLETION</a>) function that completes the creation of an NDK object.

`RequestContext`

A context value that the NDK provider passes back to the <i>NdkCreateCompletion</i> function that is specified in the <i>CreateCompletion</i> parameter.

`**ppNdkSrq`




## Return Value

The 
     <i>NdkCreateSrq</i> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The SRQ object was created successfully and returned with the  <i>*ppNdkSrq</i> parameter.
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl> The operation is pending and will be completed later. The provider will call the function specified in the <i>CreateCompletion</i> parameter (<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_completion.md">NDK_FN_CREATE_COMPLETION</a>) to complete the pending operation.
 
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>The request failed because the requested <i>SrqDepth</i> or <i>MaxReceiveRequestSge</i> is not within the limits that are specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The request failed due to insufficient resources. 
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

## Remarks

The <i>NdkCreateSrq</i> function creates an NDK shared receive queue (SRQ) object. If the function returns STATUS_SUCCESS, the created object is returned in the <i>ppNdkSrq</i> parameter. If <i>NdkCreateSrq</i> returns STATUS_PENDING, the created object is returned by the <i>NdkCreateCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_completion.md">NDK_FN_CREATE_COMPLETION</a>) function that is specified in the <i>CreateCompletion</i> parameter.

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
<a href="..\miniport\ns-miniport-_group_affinity.md">GROUP_AFFINITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_completion.md">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_srq_notification_callback.md">NDK_FN_SRQ_NOTIFICATION_CALLBACK</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_pd.md">NDK_PD</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_srq.md">NDK_SRQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/94993523-D0D7-441E-B95C-417800840BAC">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_CREATE_SRQ callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>