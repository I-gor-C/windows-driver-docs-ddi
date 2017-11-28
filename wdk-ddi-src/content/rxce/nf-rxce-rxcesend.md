---
UID: NF.rxce.RxCeSend
title: RxCeSend
author: windows-driver-content
description: RxCeSend sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.
old-location: ifsk\rxcesend.htm
old-project: ifsk
ms.assetid: bf1b9c63-6fc2-4006-8f9a-d4b50d61d270
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCeSend
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxce.h
req.include-header: Rxce.h, Tdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeSend
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
req.iface: 
req.product: Windows 10 or later.
---

# RxCeSend function



## -description
<p><b>RxCeSend</b> sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.</p>


## -syntax

````
NTSTATUS RxCeSend(
  _In_ PRXCE_VC pVc,
  _In_ ULONG    SendOptions,
  _In_ PMDL     pMdl,
  _In_ ULONG    SendLength,
  _In_ PVOID    pCompletionContext
);
````


## -parameters
<dl>

### -param <i>pVc</i> [in]

<dd>
<p>A pointer to the virtual circuit along which the TSDU is to be sent.</p>
</dd>

### -param <i>SendOptions</i> [in]

<dd>
<p>The desired options for transmitting the data on this send operation by the transport. Note that this is only a request sent to the transport. The transport may only support a limited number of the options specified and ignore options not supported. The <i>SendOptions</i> parameter consists of a set of bits defined in <i>rxce.h</i>. The <i>SendOptions</i> parameter can be a combination of the following bits:</p>
<p></p>
<dl>

### -param <a id="RXCE_SEND_EXPEDITED"></a><a id="rxce_send_expedited"></a>RXCE_SEND_EXPEDITED

<dd>
<p>The given data should be sent ahead of any normal send requests the transport is currently holding queued for transmission on this endpoint-to-endpoint connection. If the transport does not support expedited transfers, it can ignore this flag. Note that RXCE_SEND_EXPEDITED is equivalent to the TDI TDI_SEND_EXPEDITED flag.</p>
</dd>

### -param <a id="RXCE_SEND_NO_RESPONSE_EXPECTED"></a><a id="rxce_send_no_response_expected"></a>RXCE_SEND_NO_RESPONSE_EXPECTED

<dd>
<p>The caller is giving a hint to the underlying transport that it does not expect a response to this send from its remote-node peer. This flag should disable piggybacking of the TSDU acknowledgment by the remote-node transport. Note that RXCE_SEND_NO_RESPONSE_EXPECTED is equivalent to the TDI_SEND_NO_RESPONSE_EXPECTED flag.</p>
</dd>

### -param <a id="RXCE_SEND_NON_BLOCKING"></a><a id="rxce_send_non_blocking"></a>RXCE_SEND_NON_BLOCKING

<dd>
<p>If the underlying transport currently has no internal buffer space available for the given data, it should just complete the IRP with STATUS_DEVICE_NOT_READY. If the transport has some buffer space available, it should copy as much data as it can from the client-supplied buffer, set the <b>IoStatus.Information</b> member to the number of bytes it copied, and complete the IRP with STATUS_SUCCESS. </p>
<p>This flag is irrelevant to transports that do not buffer sends internally. Note that RXCE_SEND_NON_BLOCKING is equivalent to the TDI_SEND_NON_BLOCKING flag.</p>
</dd>

### -param <a id="RXCE_SEND_PARTIAL"></a><a id="rxce_send_partial"></a>RXCE_SEND_PARTIAL

<dd>
<p>Signifies if an RX_MEM_DESC(MDL) is to be sent in its entirety, or if only portions of it need to be sent. This option requests that the transport allow the send operation to transmit part of the data if the transport and MDL allow this behavior.</p>
</dd>

### -param <a id="RXCE_SEND_SYNCHRONOUS"></a><a id="rxce_send_synchronous"></a>RXCE_SEND_SYNCHRONOUS

<dd>
<p>Signifies if the send operation is to transmit the data synchronously. When this option is set, the request is submitted to the underlying transport and control does not return to the caller until the request completes. Note that the <i>pCompletionContext</i> parameter is ignored when this bit is set.</p>
</dd>
</dl>
</dd>

### -param <i>pMdl</i> [in]

<dd>
<p>A pointer to the buffer to be sent.</p>
</dd>

### -param <i>SendLength</i> [in]

<dd>
<p>The length of data to be sent.</p>
</dd>

### -param <i>pCompletionContext</i> [in]

<dd>
<p>The context passed back to the caller during <b>SendCompletion</b> for asynchronous operations. Not that this parameter is ignored if the <i>SendOptions</i> parameter requests a synchronous send operation.</p>
</dd>
</dl>

## -returns
<p><b>RxCeSend</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_CONNECTION_DISCONNECTED</b></dt>
</dl><p>An invalid or disconnected virtual circuit or connection was specified</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid length was passed in the <i>SendLength</i> parameter based on the <i>SendOptions</i> specified.</p>

<p> </p>

## -remarks
<p>The <b>RxCeSend</b> routine will allocate the IRP, build the send request for the underlying transport driver, and submit the request to TDI. In the case of synchronous send operations, this routine will also the free IRP and resources allocated when the routine completes.</p>

<p>The asynchronous and synchronous options indicated in the <i>SendOptions</i> parameter used in <b>RxCeSend</b> distinguish between two situations. In the asynchronous case, control returns to the caller once the request has been successfully submitted to the underlying transport. The results for any given request are communicated back using the <b>SendCompletion</b> callback routine. The <i>pCompletionContext</i> parameter in <b>RxCeSend</b> is passed back in the callback routine to assist the caller in disambiguating the requests.</p>

<p>In the synchronous case, the request is submitted to the underlying transport and the control does not return to the caller till the request completes. Note that in the synchronous case, the <i>pCompletionContext</i> parameter is ignored and the status that is returned corresponds to the completion status of the operations.</p>

<p>The benefit of asynchronous and synchronous options depends on the underlying transport. In a virtual circuit environment (TCP, for example), a synchronous option implies that the control does not return until the data reaches the server. On the other hand for datagram oriented transports (UDP, for example), there is very little difference between the two options.</p>

<p>The <b>RxCeSend</b> routine will allocate the IRP, build the send request for the underlying transport driver, and submit the request to TDI. In the case of synchronous send operations, this routine will also the free IRP and resources allocated when the routine completes.</p>

<p>The asynchronous and synchronous options indicated in the <i>SendOptions</i> parameter used in <b>RxCeSend</b> distinguish between two situations. In the asynchronous case, control returns to the caller once the request has been successfully submitted to the underlying transport. The results for any given request are communicated back using the <b>SendCompletion</b> callback routine. The <i>pCompletionContext</i> parameter in <b>RxCeSend</b> is passed back in the callback routine to assist the caller in disambiguating the requests.</p>

<p>In the synchronous case, the request is submitted to the underlying transport and the control does not return to the caller till the request completes. Note that in the synchronous case, the <i>pCompletionContext</i> parameter is ignored and the status that is returned corresponds to the completion status of the operations.</p>

<p>The benefit of asynchronous and synchronous options depends on the underlying transport. In a virtual circuit environment (TCP, for example), a synchronous option implies that the control does not return until the data reaches the server. On the other hand for datagram oriented transports (UDP, for example), there is very little difference between the two options.</p>

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
<dt>Rxce.h (include Rxce.h or Tdi.h)</dt>
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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553482">RxCeSendDatagram</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeSend function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
