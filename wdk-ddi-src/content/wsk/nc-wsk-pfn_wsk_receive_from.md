---
UID : NC:wsk.PFN_WSK_RECEIVE_FROM
title : PFN_WSK_RECEIVE_FROM
author : windows-driver-content
description : The WskReceiveFrom function receives a datagram and any associated control information from a remote transport address.
old-location : netvista\wskreceivefrom.htm
old-project : netvista
ms.assetid : 769fea0d-e35a-4385-8027-f1518c25b637
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO, WPP_TRIAGE_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wsk.h
req.include-header : Wsk.h
req.target-type : Universal
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WskReceiveFrom
req.alt-loc : wsk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : "*PWPP_TRIAGE_INFO, WPP_TRIAGE_INFO"
req.product : Windows 10 or later.
---


# PFN_WSK_RECEIVE_FROM callback function
The 
  <b>WskReceiveFrom</b> function receives a datagram and any associated control information from a remote
  transport address.

## Syntax

```
PFN_WSK_RECEIVE_FROM PfnWskReceiveFrom;

NTSTATUS PfnWskReceiveFrom(
  PWSK_SOCKET Socket,
  PWSK_BUF Buffer,
  ULONG Flags,
  PSOCKADDR RemoteAddress,
  PULONG ControlLength,
  PCMSGHDR ControlInfo,
  PULONG ControlFlags,
  PIRP Irp
)
{...}
```

## Parameters

`Socket`

A pointer to a 
     <a href="..\wsk\ns-wsk-_wsk_socket.md">WSK_SOCKET</a> structure that specifies the socket
     object for the datagram socket from which to receive the datagram.

`Buffer`

A pointer to an initialized 
     <a href="..\wsk\ns-wsk-_wsk_buf.md">WSK_BUF</a> structure that describes the data buffer
     that receives the datagram from the socket.

`Flags`

This parameter is reserved for system use. A WSK application must set this parameter to
     zero.

`RemoteAddress`

A pointer to a caller-allocated buffer that receives the remote transport address from which the
     received datagram originated. The buffer must be located in non-paged memory. The buffer must also be
     large enough to contain the specific SOCKADDR structure type that corresponds to the address family that
     the WSK application specified when it created the datagram socket. This pointer is optional and can be
     <b>NULL</b>.

`ControlLength`



`ControlInfo`

A pointer to a caller-allocated buffer that receives the control information that is associated
     with the received datagram. The control information data that is associated with a datagram is made up
     of one or more control data objects, each of which begins with a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544964">CMSGHDR</a> structure. If there is no control
     information present for the received datagram, the contents of the buffer are undefined. This pointer is
     optional and can be <b>NULL</b>. If the 
     <i>ControlInfoLength</i> parameter is <b>NULL</b>, the 
     <i>ControlInfo</i> parameter should be <b>NULL</b>.

`ControlFlags`

A pointer to a ULONG-typed variable that receives the bitwise OR of a combination of the following
     flags:

`Irp`

A pointer to a caller-allocated IRP that the WSK subsystem uses to complete the receive operation
     asynchronously. For more information about using IRPs with WSK functions, see 
     <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/using-irps-with-winsock-kernel-functions">Using IRPs with Winsock
     Kernel Functions</a>.


## Return Value

<b>WskReceiveFrom</b> returns one of the following NTSTATUS codes:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>Data was successfully received from the socket. The IRP will be completed with success status.
       The 
       <b>IoStatus.Information</b> field of the IRP contains the number of bytes that were received.
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl>The WSK subsystem could not receive the datagram from the socket immediately. The WSK subsystem
       will complete the IRP after it has received the datagram from the socket. The status of the receive
       operation will be returned in the 
       <b>IoStatus.Status</b> field of the IRP. If the operation succeeds, the 
       <b>IoStatus.Information</b> field of the IRP will contain the number of bytes that were
       received.
<dl>
<dt><b>STATUS_FILE_FORCED_CLOSED</b></dt>
</dl>The socket is no longer functional. The IRP will be completed with failure status. The WSK
       application must call the 
       <a href="..\wsk\nc-wsk-pfn_wsk_close_socket.md">WskCloseSocket</a> function to close the
       socket as soon as possible.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred. The IRP will be completed with failure status.

## Remarks

If the WSK application has set a fixed remote transport address for the datagram socket, datagrams
    that are received from any other remote transport address will be discarded by the WSK subsystem. For
    more information about setting the remote transport address for a datagram socket, see 
    <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/sio-wsk-set-remote-address">SIO_WSK_SET_REMOTE_ADDRESS</a>.

If a WSK application's 
    <a href="..\wsk\nc-wsk-pfn_wsk_receive_from_event.md">WskReceiveFromEvent</a> event callback
    function is enabled on a datagram socket and the application also has a pending call to the 
    <b>WskReceiveFrom</b> function on the same datagram socket, then, when datagrams arrive, the pending call
    to the 
    <b>WskReceiveFrom</b> function will take precedence over the 
    <i>WskReceiveFromEvent</i> event callback function. The WSK subsystem calls the application's 
    <i>WskReceiveFromEvent</i> event callback function only if there are no IRPs queued from pending calls to
    the 
    <b>WskReceiveFrom</b> function. However, a WSK application should not assume that the WSK subsystem will
    not call the application's 
    <i>WskReceiveFromEvent</i> event callback function for a datagram socket that has a pending call to the 
    <b>WskReceiveFrom</b> function. Race conditions exist where the WSK subsystem could still call the WSK
    application's 
    <i>WskReceiveFromEvent</i> event callback function for the socket. The only way for a WSK application to
    ensure that the WSK subsystem will not call the application's 
    <i>WskReceiveFromEvent</i> event callback function on a datagram socket is to disable the application's 
    <i>WskReceiveFromEvent</i> event callback function on the socket.

If the 
    <b>WskReceiveFrom</b> function returns STATUS_PENDING, the MDL chain that is described in the 
    <a href="..\wsk\ns-wsk-_wsk_buf.md">WSK_BUF</a> structure that is pointed to by the 
    <i>Buffer</i> parameter must remain locked in memory until the IRP is completed. In addition, the variable
    that is pointed to by the 
    <i>ControlInfoLength</i> parameter, the buffer that is pointed to by the 
    <i>ControlInfo</i> parameter, and the variable that is pointed to by the 
    <i>ControlFlags</i> parameter must also remain valid until the IRP is completed. If the WSK application
    allocated these buffers or variables with one of the 
    <b>ExAllocate<i>Xxx</i></b> functions, it cannot free the memory with the corresponding 
    <b>ExFree<i>Xxx</i></b> function until after the IRP is completed. If the WSK application allocated these buffers or
    variables on the stack, it cannot return from the function that calls the 
    <b>WskReceiveFrom</b> function until after the IRP is completed.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wsk.h (include Wsk.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\wsk\nc-wsk-pfn_wsk_close_socket.md">WskCloseSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn_wsk_control_socket.md">WskControlSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn_wsk_send_to.md">WskSendTo</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn_wsk_receive_from_event.md">WskReceiveFromEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544964">CMSGHDR</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/sio-wsk-set-remote-address">SIO_WSK_SET_REMOTE_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570822">SOCKADDR</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk-_wsk_buf.md">WSK_BUF</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk-_wsk_provider_datagram_dispatch.md">
   WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk-_wsk_socket.md">WSK_SOCKET</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_RECEIVE_FROM callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>