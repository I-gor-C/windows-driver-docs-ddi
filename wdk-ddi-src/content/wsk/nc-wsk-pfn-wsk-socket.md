---
UID: NC.wsk.PFN_WSK_SOCKET
title: PFN_WSK_SOCKET
author: windows-driver-content
description: The WskSocket function creates a new socket and returns a pointer to the associated socket object.
old-location: netvista\wsksocket.htm
old-project: netvista
ms.assetid: fddfd724-c3ba-4908-a60f-70c4934efb49
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
req.alt-api: WskSocket
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

# PFN_WSK_SOCKET callback



## -description
<p>The 
  <b>WskSocket</b> function creates a new socket and returns a pointer to the associated socket object.</p>


## -prototype

````
NTSTATUS WSKAPI * WskSocket(
  _In_           PWSK_CLIENT          Client,
  _In_           ADDRESS_FAMILY       AddressFamily,
  _In_           USHORT               SocketType,
  _In_           ULONG                Protocol,
  _In_           ULONG                Flags,
  _In_opt_       PVOID                SocketContext,
  _In_opt_ const VOID                 *Dispatch,
  _In_opt_       PEPROCESS            OwningProcess,
  _In_opt_       PETHREAD             OwningThread,
  _In_opt_       PSECURITY_DESCRIPTOR SecurityDescriptor,
  _Inout_        PIRP                 Irp
);
````


## -parameters
<dl>

### -param <i>Client</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571155">WSK_CLIENT</a> structure that was returned through
     the 
     <i>WskProviderNpi</i> parameter of the 
     <a href="..\wsk\nf-wsk-wskcaptureprovidernpi.md">
     WskCaptureProviderNPI</a> function.</p>
</dd>

### -param <i>AddressFamily</i> [in]

<dd>
<p>The address family for the socket that is being created. For more information about supported
     address families, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -param <i>SocketType</i> [in]

<dd>
<p>The type of socket that is being created. The following socket types are supported:
     </p>
<p></p>
<dl>

### -param <a id="SOCK_STREAM"></a><a id="sock_stream"></a>SOCK_STREAM

<dd>
<p>Supports reliable connection-oriented byte stream communication.</p>
</dd>

### -param <a id="SOCK_DGRAM"></a><a id="sock_dgram"></a>SOCK_DGRAM

<dd>
<p>Supports unreliable connectionless datagram communication.</p>
</dd>

### -param <a id="SOCK_RAW"></a><a id="sock_raw"></a>SOCK_RAW

<dd>
<p>Supports raw access to the transport protocol.</p>
</dd>
</dl>
<p>For more information about the socket types that are supported for each supported address family, see
     
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -param <i>Protocol</i> [in]

<dd>
<p>The transport protocol for the socket that is being created. For more information about the
     protocols that are supported for each supported address family, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A flag that specifies the WSK 
     <a href="netvista.winsock_kernel_socket_categories">socket category</a> for the
     socket that is being created. This parameter can be one of the following flags:
     </p>
<p></p>
<dl>

### -param <a id="WSK_FLAG_BASIC_SOCKET"></a><a id="wsk_flag_basic_socket"></a>WSK_FLAG_BASIC_SOCKET

<dd>
<p>A basic socket will be created that can be used only to get and set transport stack socket
       options or to perform socket I/O control operations.</p>
</dd>

### -param <a id="WSK_FLAG_LISTEN_SOCKET"></a><a id="wsk_flag_listen_socket"></a>WSK_FLAG_LISTEN_SOCKET

<dd>
<p>A listening socket will be created that can be used to listen for incoming connections from
       remote transport addresses.</p>
</dd>

### -param <a id="WSK_FLAG_DATAGRAM_SOCKET"></a><a id="wsk_flag_datagram_socket"></a>WSK_FLAG_DATAGRAM_SOCKET

<dd>
<p>A datagram socket will be created that can be used to send and receive datagrams.</p>
</dd>

### -param <a id="WSK_FLAG_CONNECTION_SOCKET"></a><a id="wsk_flag_connection_socket"></a>WSK_FLAG_CONNECTION_SOCKET

<dd>
<p>A connection-oriented socket will be created that can be used to send and receive network data
       over a connection.</p>
</dd>

### -param <a id="WSK_FLAG_STREAM_SOCKET"></a><a id="wsk_flag_stream_socket"></a>WSK_FLAG_STREAM_SOCKET

<dd>
<p>A stream socket will be created that can either be used to listen for incoming connections from remote transport addresses, or send and receive network data over a connection.</p>
</dd>
</dl>
<p>If a WSK application does not specify any of the preceding flags, 
     <b>WskSocket</b> creates a basic socket.</p>
</dd>

### -param <i>SocketContext</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied context for the socket that is being created. The WSK subsystem
     passes this pointer to the socket's event callback functions. The context information is opaque to the
     WSK subsystem and must be stored in non-paged memory. If the WSK application will not be enabling any
     event callback functions on the new socket, it should set this pointer to <b>NULL</b>. For a basic socket, this
     pointer should always be <b>NULL</b>.</p>
</dd>

### -param <i>Dispatch</i> [in, optional]

<dd>
<p>A pointer to a constant client dispatch structure. This structure is a dispatch table that
     contains pointers to the event callback functions for the new socket. Depending on the WSK 
     <a href="netvista.winsock_kernel_socket_categories">socket category</a> of the socket
     (as specified by the 
     <i>Flags</i> parameter), this parameter is a pointer to one of the following structures.
     </p>
<table>
<tr>
<th>Flag</th>
<th>Dispatch table structure</th>
</tr>
<tr>
<td>
<p>WSK_FLAG_LISTEN_SOCKET</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571162">WSK_CLIENT_LISTEN_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>WSK_FLAG_DATAGRAM_SOCKET</p>
</td>
<td>
<p>
<a href="..\wsk\ns-wsk--wsk-client-datagram-dispatch.md">
         WSK_CLIENT_DATAGRAM_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>WSK_FLAG_CONNECTION_SOCKET</p>
</td>
<td>
<p>
<a href="..\wsk\ns-wsk--wsk-client-connection-dispatch.md">
         WSK_CLIENT_CONNECTION_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>WSK_FLAG_STREAM_SOCKET</p>
</td>
<td>
<p>
<a href="..\wsk\ns-wsk--wsk-client-stream-dispatch.md">WSK_CLIENT_STREAM_DISPATCH</a>
</p>
</td>
</tr>
</table>
<p> </p>
<p>If the WSK application will not be enabling all of the event callback functions for the new socket,
     it should set the pointers in the dispatch table to <b>NULL</b> for those event callback functions that it does
     not enable. If the WSK application will not be enabling any event callback functions on the new socket,
     it should set the 
     <i>Dispatch</i> pointer to <b>NULL</b>. For a basic socket, this pointer should always be <b>NULL</b>.</p>
</dd>

### -param <i>OwningProcess</i> [in, optional]

<dd>
<p>A pointer to the process from which the WSK subsystem will retrieve the security context to use
     when it binds the socket. The WSK subsystem uses the security context to determine whether the local
     transport address can be shared if that address is already in use. To specify the current process, a WSK
     application sets this pointer to <b>NULL</b>.</p>
</dd>

### -param <i>OwningThread</i> [in, optional]

<dd>
<p>A pointer to a specific thread from which the WSK subsystem will retrieve the security context to
     use when it binds the socket. The WSK subsystem uses the security context to determine whether the local
     transport address can be shared if that address is already in use. If a WSK application does not need to
     specify a specific thread, it sets this pointer to <b>NULL</b>.</p>
</dd>

### -param <i>SecurityDescriptor</i> [in, optional]

<dd>
<p>A pointer to a SECURITY_DESCRIPTOR structure that specifies the security descriptor to apply to
     the socket that is being created. The security descriptor controls the sharing of the local transport
     address to which the socket is bound. If a WSK application specifies a non-<b>NULL</b> pointer, it must specify
     a pointer to a cached copy of a security descriptor that was obtained by calling the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571126">WskControlClient</a> function with the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571154">WSK_CACHE_SD</a> control code. To specify a
     default security descriptor that does not allow sharing of the local transport address, a WSK
     application sets 
     <i>SecurityDescriptor</i> to <b>NULL</b>.
     </p>
<p>For more information about the SECURITY_DESCRIPTOR structure, see the reference page for
     SECURITY_DESCRIPTOR in the Microsoft Windows SDK documentation.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to a caller-allocated IRP that the WSK subsystem uses to complete the creation of the
     new socket asynchronously. For more information about using IRPs with WSK functions, see 
     <a href="netvista.using_irps_with_winsock_kernel_functions">Using IRPs with Winsock
     Kernel Functions</a>.</p>
</dd>
</dl>

## -returns
<p><b>WskSocket</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The new socket was successfully created. The IRP will be completed with success status.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK subsystem could not create the socket immediately. The WSK subsystem will complete the
       IRP after it has created the new socket. The status of the socket creation will be returned in the 
       <b>IoStatus.Status</b> field of the IRP.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. The IRP will be completed with failure status.</p>

<p> </p>

## -remarks
<p>If the IRP is completed with success status, the 
    <b>IoStatus.Information</b> field of the IRP contains a pointer to a socket object structure (
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a>) for the new socket.</p>

<p>A WSK application can obtain a list of available transport protocols by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571126">WskControlClient</a> function with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571195">WSK_TRANSPORT_LIST_QUERY</a> control
    code. 
    <b>WskControlClient</b> returns a list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571193">WSK_TRANSPORT</a> structures that contains all of
    the valid combinations of the 
    <i>AddressFamily</i>, 
    <i>SocketType</i>, and 
    <i>Protocol</i> parameters.</p>

<p>When a WSK application successfully creates a new socket, all of the event callback functions on the
    new socket are disabled by default. For more information about enabling any of the new socket's event
    callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If a WSK application specifies a non-<b>NULL</b> pointer for the 
    <i>SecurityDescriptor</i> parameter, it must not release the cached security descriptor until after the
    IRP is completed.</p>

<p>The WSK subsystem allocates the memory for the socket object structure (WSK_SOCKET) for the new socket
    on behalf of the WSK application. The WSK subsystem deallocates this memory when the socket is
    closed.</p>

<p>If the IRP is completed with success status, the 
    <b>IoStatus.Information</b> field of the IRP contains a pointer to a socket object structure (
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a>) for the new socket.</p>

<p>A WSK application can obtain a list of available transport protocols by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571126">WskControlClient</a> function with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571195">WSK_TRANSPORT_LIST_QUERY</a> control
    code. 
    <b>WskControlClient</b> returns a list of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571193">WSK_TRANSPORT</a> structures that contains all of
    the valid combinations of the 
    <i>AddressFamily</i>, 
    <i>SocketType</i>, and 
    <i>Protocol</i> parameters.</p>

<p>When a WSK application successfully creates a new socket, all of the event callback functions on the
    new socket are disabled by default. For more information about enabling any of the new socket's event
    callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If a WSK application specifies a non-<b>NULL</b> pointer for the 
    <i>SecurityDescriptor</i> parameter, it must not release the cached security descriptor until after the
    IRP is completed.</p>

<p>The WSK subsystem allocates the memory for the socket object structure (WSK_SOCKET) for the new socket
    on behalf of the WSK application. The WSK subsystem deallocates this memory when the socket is
    closed.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571122">WskCaptureProviderNPI</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571126">WskControlClient</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571155">WSK_CLIENT</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-client-connection-dispatch.md">
   WSK_CLIENT_CONNECTION_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571158">WSK_CLIENT_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571162">WSK_CLIENT_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-client-stream-dispatch.md">WSK_CLIENT_STREAM_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571175">WSK_PROVIDER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571177">WSK_PROVIDER_NPI</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_SOCKET callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
