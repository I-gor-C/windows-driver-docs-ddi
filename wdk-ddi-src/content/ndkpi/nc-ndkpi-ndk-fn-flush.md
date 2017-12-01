---
UID: NC.ndkpi.NDK_FN_FLUSH
title: NDK_FN_FLUSH
author: windows-driver-content
description: The NdkFlush (NDK_FN_FLUSH) function initiates cancelling of the receive and the initiator queue requests that are currently pending on an NDK queue pair (QP) object.
old-location: netvista\ndk_fn_flush.htm
old-project: netvista
ms.assetid: 8C5F62DD-36CB-4EBC-9113-BB5BF19C0D45
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
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
req.alt-api: NdkFlush
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# NDK_FN_FLUSH callback



## -description
<p>The <i>NdkFlush</i> (<i>NDK_FN_FLUSH</i>) function initiates cancelling of the receive and the initiator queue requests that are currently pending on an NDK queue pair (QP) object.</p>


## -prototype

````
NDK_FN_FLUSH NdkFlush;

VOID NdkFlush(
  _In_ NDK_QP *pNdkQp
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkQp</i> [in]

<dd>
<p>A pointer to an NDK queue pair (QP) object (<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>).</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>NdkFlush</i> cancels the receive and the initiator queue requests that are currently pending on a QP. The flushed requests have STATUS_CANCELLED as completion status.</p>

<p>If the  NDK consumer wants to verify that all of the requests are flushed after issuing <i>NdkFlush</i>, the consumer must empty the CQ until it sees completions for all requests that were queued prior to calling <i>NdkFlush</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_FLUSH callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
