---
UID: NF.rxce.RxCeQueryAdapterStatus
title: RxCeQueryAdapterStatus
author: windows-driver-content
description: RxCeQueryAdapterStatus returns the ADAPTER_STATUS structure for a given transport in a caller-allocated buffer.
old-location: ifsk\rxcequeryadapterstatus.htm
ms.assetid: ebe9bec3-6c38-48d8-b9af-03aadbc09d98
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: rxce.h
req.include-header: Rxce.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeQueryAdapterStatus
req.alt-loc: rxce.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: RxCeQueryAdapterStatus
req.iface: 
req.product: Windows 10 or later.
---

# RxCeQueryAdapterStatus function



## -description
<p><b>RxCeQueryAdapterStatus</b> returns the ADAPTER_STATUS structure for a given transport in a caller-allocated buffer.</p>


## -syntax

````
NTSTATUS RxCeQueryAdapterStatus(
   PRXCE_TRANSPORT        pTransport,
   struct _ADAPTER_STATUS *pAdapterStatus
);
````


## -parameters
<dl>

### -param <i>pTransport</i> 

<dd>
<p>A pointer to the RDBSS transport that is associated with an adapter.</p>
</dd>

### -param <i>pAdapterStatus</i> 

<dd>
<p>On input, this parameter contains a pointer to caller-allocated buffer to hold the adapter status. On output when this call is successful, the buffer contains the adapter status associated with the specified RDBSS transport.</p>
</dd>
</dl>

## -returns
<p><b>RxCeQueryAdapterStatus</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_ADDRESS_NOT_ASSOCIATED</b></dt>
</dl><p>An adapter address is not associated with the RDBSS transport. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>pTransport</i> parameter passed to this routine was invalid. </p>

<p> </p>

## -remarks
<p><b>RxCeQueryAdapterStatus</b> returns an ADAPTER_STATUS structure for a given transport. This routine is most commonly used to get the NetBIOS name of the adapter. </p>

<p><b>RxCeQueryAdapterStatus</b> calls <b>TdiBuildQueryInformation</b> with a TDI_QUERY_ADAPTER_STATUS query. </p>

<p><b>RxCeQueryAdapterStatus</b> returns an ADAPTER_STATUS structure for a given transport. This routine is most commonly used to get the NetBIOS name of the adapter. </p>

<p><b>RxCeQueryAdapterStatus</b> calls <b>TdiBuildQueryInformation</b> with a TDI_QUERY_ADAPTER_STATUS query. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxce.h (include Rxce.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=138885">ADAPTER_STATUS</a></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553461">RxCeQueryInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553474">RxCeQueryTransportInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeQueryAdapterStatus function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
