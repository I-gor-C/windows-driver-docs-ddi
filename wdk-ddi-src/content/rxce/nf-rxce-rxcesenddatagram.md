---
UID: NF.rxce.RxCeSendDatagram
title: RxCeSendDatagram
author: windows-driver-content
description: RxCeSendDatagram sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.
old-location: ifsk\rxcesenddatagram.htm
old-project: ifsk
ms.assetid: 9cb714d5-92f6-481d-bc5e-5fa05b6a0938
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCeSendDatagram
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
req.alt-api: RxCeSendDatagram
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

# RxCeSendDatagram function



## -description
<p><b>RxCeSendDatagram</b> sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.</p>


## -syntax

````
NTSTATUS RxCeSendDatagram(
  _In_ PRXCE_TRANSPORT              pTransport,
  _In_ PRXCE_ADDRESS                pAddress,
  _In_ PRXCE_CONNECTION_INFORMATION pConnectionInformation,
  _In_ ULONG                        Options,
  _In_ PMDL                         pMdl,
  _In_ ULONG                        SendLength,
  _In_ PVOID                        pCompletionContext
);
````


## -parameters
<dl>

### -param <i>pTransport</i> [in]

<dd>
<p>A pointer to the transport along which the TSDU is to be sent.</p>
</dd>

### -param <i>pAddress</i> [in]

<dd>
<p>A pointer to the local transport address.</p>
</dd>

### -param <i>pConnectionInformation</i> [in]

<dd>
<p>A pointer to connection information that contains the remote address.</p>
</dd>

### -param <i>Options</i> [in]

<dd>
<p>The desired options for transmitting the data on this send operation by the transport. Note that this is only a request sent to the transport. The transport may only support a limited number of the options specified and ignore options not supported. The <i>Options</i> parameter consists of set of bits defined in <i>rxce.h</i>. The <i>Options</i> parameter can be a combination of the following bits:</p>
<p></p>
<dl>

### -param <a id="RXCE_SEND_PARTIAL"></a><a id="rxce_send_partial"></a>RXCE_SEND_PARTIAL

<dd>
<p>Signifies if an RX_MEM_DESC(MDL) is to be sent in its entirety, or if only portions of it need to be sent. This option requests that the transport allow the send operation to transmit part of the data if the transport and MDL allow this behavior.</p>
</dd>

### -param <a id="RXCE_SEND_SYNCHRONOUS"></a><a id="rxce_send_synchronous"></a>RXCE_SEND_SYNCHRONOUS

<dd>
<p>Signifies if the send operation is to transmit the data synchronously. When this option is set, the request is submitted to the underlying transport and control does not return to the caller until the request completes. Note that the <i>pCompletionContext</i> parameter is ignored when this bit is set.</p>
<p>Note that the RXCE_SEND_SYNCHRONOUS option is disregarded for sending datagrams because the underlying transports do not block on datagram sends.</p>
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
<p>The context passed back to the caller during <b>SendCompletion</b> for asynchronous operations. Not that this parameter is ignored if the <i>Options</i> parameter requests a synchronous send operation.</p>
</dd>
</dl>

## -returns
<p><b>RxCeSendDatagram</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid length was passed in the <i>SendLength</i> parameter based on the <i>Options</i> specified.</p>

<p> </p>

## -remarks
<p>The asynchronous and synchronous options indicated in the <i>Options</i> parameter used in <b>RxCeSendDatagram</b> distinguish between two situations. In the asynchronous case, control returns to the caller once the request has been successfully submitted to the underlying transport. The results for any given request are communicated back using the <b>SendCompletion</b> callback routine. The <i>pCompletionContext</i> parameter in <b>RxCeSendDatagram</b> is passed back in the callback routine to assist the caller in disambiguating the requests.</p>

<p>In the synchronous case, the request is submitted to the underlying transport and the control does not return to the caller till the request completes. Note that in the synchronous case, the <i>pCompletionContext</i> parameter is ignored and the status that is returned corresponds to the completion status of the operations.</p>

<p>The benefit of asynchronous and synchronous options depends on the underlying transport. In a virtual circuit environment (TCP, for example), a synchronous option implies that the control does not return until the data reaches the server. On the other hand for datagram oriented transports (UDP, for example), there is very little difference between the two options.</p>

<p>Note that the synchronous <i>Option</i> is disregarded for sending datagrams because the underlying transports do not block on datagram sends. </p>

<p><b>RXCE_CONNECTION_INFORMATION</b> is a typedef for a <b>TDI_CONNECTION_INFORMATION</b> structure. </p>

<p>The asynchronous and synchronous options indicated in the <i>Options</i> parameter used in <b>RxCeSendDatagram</b> distinguish between two situations. In the asynchronous case, control returns to the caller once the request has been successfully submitted to the underlying transport. The results for any given request are communicated back using the <b>SendCompletion</b> callback routine. The <i>pCompletionContext</i> parameter in <b>RxCeSendDatagram</b> is passed back in the callback routine to assist the caller in disambiguating the requests.</p>

<p>In the synchronous case, the request is submitted to the underlying transport and the control does not return to the caller till the request completes. Note that in the synchronous case, the <i>pCompletionContext</i> parameter is ignored and the status that is returned corresponds to the completion status of the operations.</p>

<p>The benefit of asynchronous and synchronous options depends on the underlying transport. In a virtual circuit environment (TCP, for example), a synchronous option implies that the control does not return until the data reaches the server. On the other hand for datagram oriented transports (UDP, for example), there is very little difference between the two options.</p>

<p>Note that the synchronous <i>Option</i> is disregarded for sending datagrams because the underlying transports do not block on datagram sends. </p>

<p><b>RXCE_CONNECTION_INFORMATION</b> is a typedef for a <b>TDI_CONNECTION_INFORMATION</b> structure. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553479">RxCeSend</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565085">TDI_CONNECTION_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeSendDatagram function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
