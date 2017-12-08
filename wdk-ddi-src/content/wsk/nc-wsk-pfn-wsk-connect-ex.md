---
UID: NC.wsk.PFN_WSK_CONNECT_EX
title: PFN_WSK_CONNECT_EX
author: windows-driver-content
description: The WskConnectEx function connects a connection-oriented or stream socket to a remote transport address.WskConnectEx is similar to WskConnect except that it can also optionally send a buffer of data during or after connection synchronization.
old-location: netvista\wskconnectex.htm
old-project: netvista
ms.assetid: 1BC518E9-747C-4406-8A2A-40A3BCB0A3AA
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskConnectEx
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

# PFN_WSK_CONNECT_EX callback



## -description
<p>The 
  <b>WskConnectEx</b> function connects a connection-oriented or stream socket to a remote transport address.</p>
<p><b>WskConnectEx</b> is similar to <a href="..\wsk\nc-wsk-pfn-wsk-connect.md">WskConnect</a>
  except that it can also optionally send a buffer of data during or after connection synchronization.</p>


## -prototype

````
NTSTATUS WINAPI WskConnectEx(
  _In_       PWSK_SOCKET Socket,
  _In_       PSOCKADDR   RemoteAddress,
  _In_opt_   PWSK_BUF    Buffer,
  _Reserved_ ULONG       Flags,
  _Inout_    PIRP        Irp
);
````


## -parameters
<dl>

### -param Socket [in]

<dd>
<p>A pointer to a 
     <a href="..\wsk\ns-wsk--wsk-socket.md">WSK_SOCKET</a> structure that specifies the socket
     object for the socket that is being connected to a remote transport address.</p>
</dd>

### -param RemoteAddress [in]

<dd>
<p>A pointer to a structure that specifies the remote transport address to which to connect the
     socket. This pointer must be a pointer to the specific <a href="netvista.sockaddr">SOCKADDR</a> structure type that corresponds to the
     address family that the WSK application specified when it created the socket.</p>
</dd>

### -param Buffer [in, optional]

<dd>
<p>A pointer to a <a href="..\wsk\ns-wsk--wsk-buf.md">WSK_BUF</a> structure, which contains the data to send during or after connection synchronization. The maximum allowed size in bytes is 65,535.</p>
</dd>

### -param Flags 

<dd>
<p>This parameter is reserved for system use. A WSK application must set this parameter to
     zero. </p>
</dd>

### -param Irp [in, out]

<dd>
<p>A pointer to a caller-allocated IRP that the WSK subsystem uses to complete the connect operation
     asynchronously. For more information about using IRPs with WSK functions, see 
     <a href="netvista.using_irps_with_winsock_kernel_functions">Using IRPs with Winsock
     Kernel Functions</a>.</p>
</dd>
</dl>

## -returns
<p><b>WskConnectEx</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The socket was successfully connected to the remote transport address. The IRP will be completed
       with success status.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK subsystem could not connect the socket immediately. The WSK subsystem will complete the
       IRP after it has connected the socket to the remote transport address. The status of the connect
       operation will be returned in the 
       <b>IoStatus.Status</b> field of the IRP.</p><dl>
<dt><b>STATUS_FILE_FORCED_CLOSED</b></dt>
</dl><p>The socket is no longer functional. The IRP will be completed with failure status. The WSK
       application must call the 
       <a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a> function to close the
       socket as soon as possible.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The WSK application attempted to pass a flag in to the <i>Flags</i> parameter (as no valid flags are currently defined for <b>WskConnectEx</b>, this is not allowed).</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The WSK application attempted to pass in a buffer larger than 65,535 bytes to the <i>Buffer</i> parameter.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. The IRP will be completed with failure status.</p>

<p> </p>

## -remarks
<p>A WSK application can create, bind, and connect a connection-oriented socket in a single function call
    by calling the 
    <a href="..\wsk\nc-wsk-pfn-wsk-socket-connect.md">WskSocketConnect</a> function rather than
    calling the 
    <a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a> function, the 
    <a href="..\wsk\nc-wsk-pfn-wsk-bind.md">WskBind</a> function, and then the 
    <b>WskConnectEx</b> function. We recommend calling the 
    <b>WskSocketConnect</b> function unless the WSK application needs to set a socket option or issue an I/O
    control operation before binding or connecting the socket.</p>

<p>A WSK application can call the 
    <b>WskConnectEx</b> function only on a connection-oriented or stream socket that the application previously bound to a
    local transport address by calling the 
    <a href="..\wsk\nc-wsk-pfn-wsk-bind.md">WskBind</a> function.</p>

<p>For stream sockets, once <b>WskConnectEx</b> is successfully called on a stream socket, the socket is committed to a connection-oriented flow and may no longer call listening socket functions.</p>

<p>If the <i>Buffer</i> parameter is used, the caller can free the MDL in its <a href="..\wsk\ns-wsk--wsk-buf.md">WSK_BUF</a> structure as soon as the connect request is complete.</p>

<p>Before calling <b>WskConnectEx</b> with a provided send buffer, if the WSK application sets the <b>TCP_FASTOPEN</b> option on a WSK socket via the <a href="..\wsk\nc-wsk-pfn-wsk-control-socket.md">WskControlSocket</a> function the system will optionally send some or all of the data in a SYN packet. For more information, see the <b>TCP Fastopen</b> option in <a href="winsock.ipproto_tcp_socket_options">IPPROTO_TCP Socket Options</a>.</p>

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
<p>Windows 10, version 1703</p>
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
<a href="..\wsk\nc-wsk-pfn-wsk-bind.md">WskBind</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-control-socket.md">WskControlSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-disconnect.md">WskDisconnect</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-socket-connect.md">WskSocketConnect</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-disconnect-event.md">WskDisconnectEvent</a>
</dt>
<dt>
<a href="netvista.sockaddr">SOCKADDR</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-connection-dispatch.md">
   WSK_PROVIDER_CONNECTION_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-stream-dispatch.md">
   WSK_PROVIDER_STREAM_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-socket.md">WSK_SOCKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_CONNECT_EX callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
