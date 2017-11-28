---
UID: NC.wsk.PFN_WSK_GET_LOCAL_ADDRESS
title: PFN_WSK_GET_LOCAL_ADDRESS
author: windows-driver-content
description: The WskGetLocalAddress function retrieves the local transport address of a socket.
old-location: netvista\wskgetlocaladdress.htm
old-project: netvista
ms.assetid: 13cd4199-63f8-49f3-a12f-86e1d367b4aa
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
req.alt-api: WskGetLocalAddress
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

# PFN_WSK_GET_LOCAL_ADDRESS callback



## -description
<p>The 
  <b>WskGetLocalAddress</b> function retrieves the local transport address of a socket.</p>


## -prototype

````
NTSTATUS WSKAPI * WskGetLocalAddress(
  _In_    PWSK_SOCKET Socket,
  _Out_   PSOCKADDR   LocalAddress,
  _Inout_ PIRP        Irp
);
````


## -parameters
<dl>

### -param <i>Socket</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a> structure that specifies the socket
     object for the socket that is being queried.</p>
</dd>

### -param <i>LocalAddress</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that receives the local transport address for the socket.
     The buffer must be located in non-paged memory. The buffer must also be large enough to contain the
     specific SOCKADDR structure type that corresponds to the address family that the WSK application
     specified when it created the socket.
     </p>
<p>For a connection-oriented socket that the WSK application accepted on a listening socket, the address
     family is the same as the address family that the WSK application specified when it created the
     listening socket.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to a caller-allocated IRP that the WSK subsystem uses to complete the retrieve operation
     asynchronously. For more information about using IRPs with WSK functions, see 
     <a href="netvista.using_irps_with_winsock_kernel_functions">Using IRPs with Winsock
     Kernel Functions</a>.</p>
</dd>
</dl>

## -returns
<p><b>WskGetLocalAddress</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The local transport address for the socket was successfully retrieved. The IRP will be completed
       with success status.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK subsystem could not retrieve the local transport address for the socket immediately. The
       WSK subsystem will complete the IRP after it has retrieved the local transport address for the socket.
       The status of the retrieve operation will be returned in the 
       <b>IoStatus.Status</b> field of the IRP.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The socket is not bound to a local transport address. The IRP will be completed with failure
       status.</p><dl>
<dt><b>STATUS_FILE_FORCED_CLOSED</b></dt>
</dl><p>The socket is no longer functional. The IRP will be completed with failure status. The WSK
       application must call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> function to close the
       socket as soon as possible.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. The IRP will be completed with failure status.</p>

<p> </p>

## -remarks
<p>A WSK application can call the 
    <b>WskGetLocalAddress</b> function only on a socket that has been bound to a local transport address.</p>

<p>A listening, datagram, or stream socket is bound to a local transport address when the WSK application
    calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571121">WskBind</a> function.</p>

<p>A connection-oriented socket is bound to a local transport address in one of the following ways:</p>

<p>The WSK application calls the 
      <b>WskBind</b> function.</p>

<p>The WSK application creates, binds, and connects the socket by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a> function.</p>

<p>The WSK subsystem binds the socket when the WSK application accepts an incoming connection request
      on a listening socket.</p>

<p>The 
    <b>WskGetLocalAddress</b> function is particularly useful for determining the specific local transport
    address that was assigned to a socket by the transport protocol when the socket was bound to the local
    wildcard address. For a connection-oriented socket that was bound to the local wildcard address, the
    local transport address might not be assigned to the socket by the transport protocol until the socket is
    connected to a remote transport address. The step where the local transport address is assigned to the
    socket is transport protocol-dependent. For TCP, the port number is assigned when a connection-oriented
    socket is bound, but the IP address is not assigned until the socket is connected.</p>

<p>If the 
    <b>WskGetLocalAddress</b> function returns STATUS_PENDING, the buffer that is pointed to by the 
    <i>LocalAddress</i> parameter must remain valid until the IRP is completed. If the WSK application
    allocated the buffer with one of the 
    <b>ExAllocate<i>Xxx</i></b> functions, it cannot free the memory with the corresponding 
    <b>ExFree<i>Xxx</i></b> function until after the IRP is completed. If the WSK application allocated the buffer on the
    stack, it cannot return from the function that calls the 
    <b>WskGetLocalAddress</b> function until after the IRP is completed.</p>

<p>A WSK application can call the 
    <b>WskGetLocalAddress</b> function only on a socket that has been bound to a local transport address.</p>

<p>A listening, datagram, or stream socket is bound to a local transport address when the WSK application
    calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571121">WskBind</a> function.</p>

<p>A connection-oriented socket is bound to a local transport address in one of the following ways:</p>

<p>The WSK application calls the 
      <b>WskBind</b> function.</p>

<p>The WSK application creates, binds, and connects the socket by calling the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a> function.</p>

<p>The WSK subsystem binds the socket when the WSK application accepts an incoming connection request
      on a listening socket.</p>

<p>The 
    <b>WskGetLocalAddress</b> function is particularly useful for determining the specific local transport
    address that was assigned to a socket by the transport protocol when the socket was bound to the local
    wildcard address. For a connection-oriented socket that was bound to the local wildcard address, the
    local transport address might not be assigned to the socket by the transport protocol until the socket is
    connected to a remote transport address. The step where the local transport address is assigned to the
    socket is transport protocol-dependent. For TCP, the port number is assigned when a connection-oriented
    socket is bound, but the IP address is not assigned until the socket is connected.</p>

<p>If the 
    <b>WskGetLocalAddress</b> function returns STATUS_PENDING, the buffer that is pointed to by the 
    <i>LocalAddress</i> parameter must remain valid until the IRP is completed. If the WSK application
    allocated the buffer with one of the 
    <b>ExAllocate<i>Xxx</i></b> functions, it cannot free the memory with the corresponding 
    <b>ExFree<i>Xxx</i></b> function until after the IRP is completed. If the WSK application allocated the buffer on the
    stack, it cannot return from the function that calls the 
    <b>WskGetLocalAddress</b> function until after the IRP is completed.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571109">WskAccept</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571121">WskBind</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571125">WskConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571135">WskGetRemoteAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-accept-event.md">WskAcceptEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570822">SOCKADDR</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-connection-dispatch.md">
   WSK_PROVIDER_CONNECTION_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-datagram-dispatch.md">
   WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571176">WSK_PROVIDER_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-stream-dispatch.md">WSK_PROVIDER_STREAM_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_GET_LOCAL_ADDRESS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
