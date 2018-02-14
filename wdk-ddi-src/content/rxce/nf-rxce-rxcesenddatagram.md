---
UID: NF:rxce.RxCeSendDatagram
title: RxCeSendDatagram function
author: windows-driver-content
description: RxCeSendDatagram sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.
old-location: ifsk\rxcesenddatagram.htm
old-project: ifsk
ms.assetid: 9cb714d5-92f6-481d-bc5e-5fa05b6a0938
ms.author: windowsdriverdev
ms.date: 2/7/2018
ms.keywords: RxCeSendDatagram function [Installable File System Drivers], rxce/RxCeSendDatagram, rxref_dc97dbe7-c676-4b1f-8aee-7dbc7cfbc5e3.xml, RxCeSendDatagram, ifsk.rxcesenddatagram
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: "<= APC_LEVEL"
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rxce.h
apiname:
-	RxCeSendDatagram
product: Windows
targetos: Windows
req.typenames: "*LPRILWRITEPHONEBOOKENTRYPARAMS, RILWRITEPHONEBOOKENTRYPARAMS"
req.product: Windows 10 or later.
---


# RxCeSendDatagram function
<b>RxCeSendDatagram</b> sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.

## Syntax

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

## Parameters

`hAddress`

TBD

`pConnectionInformation`

A pointer to connection information that contains the remote address.

`SendOptions`

TBD

`pMdl`

A pointer to the buffer to be sent.

`SendLength`

The length of data to be sent.

`pCompletionContext`

The context passed back to the caller during <b>SendCompletion</b> for asynchronous operations. Not that this parameter is ignored if the <i>Options</i> parameter requests a synchronous send operation.


## Return Value

<b>RxCeSendDatagram</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
The allocation of nonpaged pool memory needed by this routine failed. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
An invalid length was passed in the <i>SendLength</i> parameter based on the <i>Options</i> specified.

</td>
</tr>
</table>

## Remarks

The asynchronous and synchronous options indicated in the <i>Options</i> parameter used in <b>RxCeSendDatagram</b> distinguish between two situations. In the asynchronous case, control returns to the caller once the request has been successfully submitted to the underlying transport. The results for any given request are communicated back using the <b>SendCompletion</b> callback routine. The <i>pCompletionContext</i> parameter in <b>RxCeSendDatagram</b> is passed back in the callback routine to assist the caller in disambiguating the requests.

In the synchronous case, the request is submitted to the underlying transport and the control does not return to the caller till the request completes. Note that in the synchronous case, the <i>pCompletionContext</i> parameter is ignored and the status that is returned corresponds to the completion status of the operations.

The benefit of asynchronous and synchronous options depends on the underlying transport. In a virtual circuit environment (TCP, for example), a synchronous option implies that the control does not return until the data reaches the server. On the other hand for datagram oriented transports (UDP, for example), there is very little difference between the two options.

Note that the synchronous <i>Option</i> is disregarded for sending datagrams because the underlying transports do not block on datagram sends. 

<b>RXCE_CONNECTION_INFORMATION</b> is a typedef for a <b>TDI_CONNECTION_INFORMATION</b> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | rxce.h (include Rxce.h, Tdi.h) |
| **Library** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="..\wdm\ns-wdm-_mdl.md">MDL</a>



<a href="..\rxce\nf-rxce-rxcesend.md">RxCeSend</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565085">TDI_CONNECTION_INFORMATION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeSendDatagram function%20 RELEASE:%20(2/7/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>