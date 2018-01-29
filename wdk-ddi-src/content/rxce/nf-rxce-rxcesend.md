---
UID : NF:rxce.RxCeSend
title : RxCeSend function
author : windows-driver-content
description : RxCeSend sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.
old-location : ifsk\rxcesend.htm
old-project : ifsk
ms.assetid : bf1b9c63-6fc2-4006-8f9a-d4b50d61d270
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : rxce/RxCeSend, rxref_07c5b21c-253c-4032-a5e8-61c4e71450fb.xml, RxCeSend, RxCeSend function [Installable File System Drivers], ifsk.rxcesend
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : rxce.h
req.include-header : Rxce.h, Tdi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : <= APC_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*LPRILWRITEPHONEBOOKENTRYPARAMS, RILWRITEPHONEBOOKENTRYPARAMS"
req.product : Windows 10 or later.
---


# RxCeSend function
<b>RxCeSend</b> sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.

## Syntax

````
NTSTATUS RxCeSend(
  _In_ PRXCE_VC pVc,
  _In_ ULONG    SendOptions,
  _In_ PMDL     pMdl,
  _In_ ULONG    SendLength,
  _In_ PVOID    pCompletionContext
);
````

## Parameters

`pVc`

A pointer to the virtual circuit along which the TSDU is to be sent.

`SendOptions`

The desired options for transmitting the data on this send operation by the transport. Note that this is only a request sent to the transport. The transport may only support a limited number of the options specified and ignore options not supported. The <i>SendOptions</i> parameter consists of a set of bits defined in <i>rxce.h</i>. The <i>SendOptions</i> parameter can be a combination of the following bits:

`pMdl`

A pointer to the buffer to be sent.

`SendLength`

The length of data to be sent.

`pCompletionContext`

The context passed back to the caller during <b>SendCompletion</b> for asynchronous operations. Not that this parameter is ignored if the <i>SendOptions</i> parameter requests a synchronous send operation.


## Return Value

<b>RxCeSend</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: 
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_CONNECTION_DISCONNECTED</b></dt>
</dl>
</td>
<td width="60%">
An invalid or disconnected virtual circuit or connection was specified

</td>
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
An invalid length was passed in the <i>SendLength</i> parameter based on the <i>SendOptions</i> specified.

</td>
</tr>
</table>

## Remarks

The <b>RxCeSend</b> routine will allocate the IRP, build the send request for the underlying transport driver, and submit the request to TDI. In the case of synchronous send operations, this routine will also the free IRP and resources allocated when the routine completes.

The asynchronous and synchronous options indicated in the <i>SendOptions</i> parameter used in <b>RxCeSend</b> distinguish between two situations. In the asynchronous case, control returns to the caller once the request has been successfully submitted to the underlying transport. The results for any given request are communicated back using the <b>SendCompletion</b> callback routine. The <i>pCompletionContext</i> parameter in <b>RxCeSend</b> is passed back in the callback routine to assist the caller in disambiguating the requests.

In the synchronous case, the request is submitted to the underlying transport and the control does not return to the caller till the request completes. Note that in the synchronous case, the <i>pCompletionContext</i> parameter is ignored and the status that is returned corresponds to the completion status of the operations.

The benefit of asynchronous and synchronous options depends on the underlying transport. In a virtual circuit environment (TCP, for example), a synchronous option implies that the control does not return until the data reaches the server. On the other hand for datagram oriented transports (UDP, for example), there is very little difference between the two options.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rxce.h (include Rxce.h, Tdi.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\wdm\ns-wdm-_mdl.md">MDL</a>

<a href="..\rxce\nf-rxce-rxcesenddatagram.md">RxCeSendDatagram</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeSend function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>