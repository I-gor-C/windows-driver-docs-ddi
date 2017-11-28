---
UID: NC.wsk.PFN_WSK_SEND_TO
title: PFN_WSK_SEND_TO
author: windows-driver-content
description: The WskSendTo function sends datagram data to a remote transport address.
old-location: netvista\wsksendto.htm
old-project: netvista
ms.assetid: 34257ef2-947a-463a-b234-04fbaffa9344
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskSendTo
req.alt-loc: wsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PFN_WSK_SEND_TO callback



## -description
<p>The 
  <b>WskSendTo</b> function sends datagram data to a remote transport address.</p>


## -prototype

````
NTSTATUS WSKAPI * WskSendTo(
  _In_       PWSK_SOCKET Socket,
  _In_       PWSK_BUF    Buffer,
  _Reserved_ ULONG       Flags,
  _In_opt_   PSOCKADDR   RemoteAddress,
  _In_       ULONG       ControlInfoLength,
  _In_opt_   PCMSGHDR    ControlInfo,
  _Inout_    PIRP        Irp
);
````


## -parameters
<dl>

### -param <i>Socket</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a> structure that specifies the socket
     object for the datagram socket over which to send the datagram.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to an initialized 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571153">WSK_BUF</a> structure that describes the data buffer
     that contains the datagram that is being sent over the socket.</p>
</dd>

### -param <i>Flags</i> 

<dd>
<p>This parameter is reserved for system use. A WSK application must set this parameter to
     zero.</p>
</dd>

### -param <i>RemoteAddress</i> [in, optional]

<dd>
<p>A pointer to a structure that specifies the remote transport address to which to send the
     datagram. This pointer must be a pointer to the specific SOCKADDR structure type that corresponds to the
     address family that the WSK application specified when it created the socket.
     </p>
<p>If the WSK application has set either a fixed remote transport address or a fixed destination
     transport address for the datagram socket, this pointer is optional and may be <b>NULL</b>. If <b>NULL</b>, the
     datagram is sent to the fixed remote transport address or the fixed destination transport address. If
     non-<b>NULL</b>, the datagram is sent to the specified remote transport address.</p>
<p>For more information about setting a fixed remote transport address for a datagram socket, see 
     <a href="netvista.sio_wsk_set_remote_address">
     SIO_WSK_SET_REMOTE_ADDRESS</a>.</p>
<p>For more information about setting a fixed destination transport address for a datagram socket, see 
     <a href="netvista.sio_wsk_set_sendto_address">
     SIO_WSK_SET_SENDTO_ADDRESS</a>.</p>
</dd>

### -param <i>ControlInfoLength</i> [in]

<dd>
<p>The number of bytes of data in the buffer that is pointed to by the 
     <i>ControlInfo</i> parameter. If there is no control information associated with the datagram, the 
     <i>ControlInfoLength</i> parameter must be zero.</p>
</dd>

### -param <i>ControlInfo</i> [in, optional]

<dd>
<p>A pointer to a buffer that contains control information that is associated with the datagram that
     is being sent. The control information data consists of one or more control data objects, each of which
     begins with a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544964">CMSGHDR</a> structure. If there is no control
     information that is associated with the datagram, this parameter should be <b>NULL</b>.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to a caller-allocated IRP that the WSK subsystem uses to complete the send operation
     asynchronously. For more information about using IRPs with WSK functions, see 
     <a href="netvista.using_irps_with_winsock_kernel_functions">Using IRPs with Winsock
     Kernel Functions</a>.</p>
</dd>
</dl>

## -returns
<p><b>WskSendTo</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The datagram was successfully sent over the socket. The IRP will be completed with success
       status. The 
       <b>IoStatus.Information</b> field of the IRP contains the number of bytes that were sent.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK subsystem could not send the datagram over the socket immediately. The WSK subsystem
       will complete the IRP after it has sent the datagram over the socket. The status of the send operation
       will be returned in the 
       <b>IoStatus.Status</b> field of the IRP. If the operation succeeds, the 
       <b>IoStatus.Information</b> field of the IRP will contain the number of bytes that were sent.</p><dl>
<dt><b>STATUS_FILE_FORCED_CLOSED</b></dt>
</dl><p>The socket is no longer functional. The IRP will be completed with failure status. The WSK
       application must call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> function to close the
       socket as soon as possible.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. The IRP will be completed with failure status.</p>

<p> </p>

## -remarks
<p>If the 
    <b>WskSendTo</b> function returns STATUS_PENDING, the MDL chain that is described in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571153">WSK_BUF</a> structure that is pointed to by the 
    <i>Buffer</i> parameter must remain locked in memory until the IRP is completed. In addition, the buffer
    that is pointed to by the 
    <i>ControlInfo</i> parameter must also remain valid until the IRP is completed. If the WSK application
    allocated the MDL chain or the control information buffer with one of the 
    <b>ExAllocate<i>Xxx</i></b> functions, it cannot free the memory with the corresponding 
    <b>ExFree<i>Xxx</i></b> function until after the IRP is completed. If the WSK application allocated the MDL chain or
    the control information buffer on the stack, it cannot return from the function that calls the 
    <b>WskSendTo</b> function until after the IRP is completed.</p>

<p>The WSK subsystem does not perform any buffering of data when it sends datagrams over a socket.
    Therefore, a call to the 
    <b>WskSendTo</b> function will not be completed by the WSK subsystem until all of the data has actually
    been sent.</p>

<p>If the 
    <b>WskSendTo</b> function returns STATUS_PENDING, the MDL chain that is described in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571153">WSK_BUF</a> structure that is pointed to by the 
    <i>Buffer</i> parameter must remain locked in memory until the IRP is completed. In addition, the buffer
    that is pointed to by the 
    <i>ControlInfo</i> parameter must also remain valid until the IRP is completed. If the WSK application
    allocated the MDL chain or the control information buffer with one of the 
    <b>ExAllocate<i>Xxx</i></b> functions, it cannot free the memory with the corresponding 
    <b>ExFree<i>Xxx</i></b> function until after the IRP is completed. If the WSK application allocated the MDL chain or
    the control information buffer on the stack, it cannot return from the function that calls the 
    <b>WskSendTo</b> function until after the IRP is completed.</p>

<p>The WSK subsystem does not perform any buffering of data when it sends datagrams over a socket.
    Therefore, a call to the 
    <b>WskSendTo</b> function will not be completed by the WSK subsystem until all of the data has actually
    been sent.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571127">WskControlSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571141">WskReceiveFrom</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-receive-from-event.md">WskReceiveFromEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544964">CMSGHDR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570822">SOCKADDR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571153">WSK_BUF</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-datagram-dispatch.md">
   WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_SEND_TO callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
