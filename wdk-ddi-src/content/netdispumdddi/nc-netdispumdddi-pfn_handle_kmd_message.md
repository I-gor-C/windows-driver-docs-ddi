---
UID : NC:netdispumdddi.PFN_HANDLE_KMD_MESSAGE
title : PFN_HANDLE_KMD_MESSAGE
author : windows-driver-content
description : Called by the operating system to handle the asynchronous kernel-mode message that the Miracast user-mode driver receives when the display miniport driver calls the DxgkCbMiracastSendMessage function.
old-location : display\handlekernelmodemessage.htm
old-project : display
ms.assetid : 9DE4F3B0-915A-4C66-85F8-AE248B8471B5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _NDK_SRQ_DISPATCH, NDK_SRQ_DISPATCH
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : netdispumdddi.h
req.include-header : Netdispumdddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : HandleKernelModeMessage
req.alt-loc : Netdispumdddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : NDK_SRQ_DISPATCH
---


# PFN_HANDLE_KMD_MESSAGE callback function
Called by the operating system to handle the asynchronous kernel-mode message that the Miracast user-mode driver receives when the display miniport driver calls the <a href="..\dispmprt\nc-dispmprt-dxgkcb_miracast_send_message.md">DxgkCbMiracastSendMessage</a> function.

## Syntax

```
PFN_HANDLE_KMD_MESSAGE PfnHandleKmdMessage;

NTSTATUS PfnHandleKmdMessage(
  PVOID pMiracastContext,
  UINT InputBufferSize,
  VOID *pInputBuffer,
  UINT OutputBufferSize,
  VOID *pOutputBuffer,
  UINT *pBytesReturned
)
{...}
```

## Parameters

`pMiracastContext`

A pointer to a context associated with a display adapter.

The operating system obtained the context when it called the Miracast user-mode driver's <a href="..\netdispumdddi\nc-netdispumdddi-pfn_create_miracast_context.md">CreateMiracastContext</a> function.

`InputBufferSize`

The size of the input buffer <i>pInputBuffer</i>, supplied by the operating system.

`*pInputBuffer`



`OutputBufferSize`

The size of the output buffer <i>pOutputBuffer</i>, supplied by the operating system.

`*pOutputBuffer`



`*pBytesReturned`




## Return Value

On success, this function returns <b>STATUS_SUCCESS</b>. Otherwise, the function returns an error code defined in the Ntstatus.h header.

## Remarks

When this function is called, it's possible that it has also been called in another thread. The driver is therefore responsible for synchronizing multiple calls to <i>HandleKernelModeMessage</i> if necessary.

The operating system guarantees that this function is not called when <a href="..\netdispumdddi\nc-netdispumdddi-pfn_create_miracast_context.md">CreateMiracastContext</a>, <a href="..\netdispumdddi\nc-netdispumdddi-pfn_destroy_miracast_context.md">DestroyMiracastContext</a>, <a href="..\netdispumdddi\nc-netdispumdddi-pfn_start_miracast_session.md">StartMiracastSession</a>, and <a href="..\netdispumdddi\nc-netdispumdddi-pfn_stop_miracast_session.md">StopMiracastSession</a> are called. All the messages that the display miniport driver sends during the startup of a Miracast connected session (<i>StartMiracastSession</i>) are blocked until the session startup process has completed. The operating system also blocks all messages that the display miniport driver sends during or after a call to stop the Miracast session (<i>StopMiracastSession</i>).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | netdispumdddi.h (include Netdispumdddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn_create_miracast_context.md">CreateMiracastContext</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn_destroy_miracast_context.md">DestroyMiracastContext</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb_miracast_send_message.md">DxgkCbMiracastSendMessage</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn_start_miracast_session.md">StartMiracastSession</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn_stop_miracast_session.md">StopMiracastSession</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_HANDLE_KMD_MESSAGE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>