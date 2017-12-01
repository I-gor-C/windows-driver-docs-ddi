---
UID: NC.wsk.PFN_WSK_DISCONNECT_EVENT
title: PFN_WSK_DISCONNECT_EVENT
author: windows-driver-content
description: The WskDisconnectEvent event callback function notifies a WSK application that a connection on a connection-oriented socket has been disconnected by the remote application.
old-location: netvista\wskdisconnectevent.htm
old-project: netvista
ms.assetid: bf12d7b3-080e-46d9-b276-76d42068e7c6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskDisconnectEvent
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

# PFN_WSK_DISCONNECT_EVENT callback



## -description
<p>The 
  <i>WskDisconnectEvent</i> event callback function notifies a WSK application that a connection on a
  connection-oriented socket has been disconnected by the remote application.</p>


## -prototype

````
PFN_WSK_DISCONNECT_EVENT WskDisconnectEvent;

NTSTATUS APIENTRY WskDisconnectEvent(
  _In_opt_ PVOID SocketContext,
  _In_     ULONG Flags
)
{ ... }
````


## -parameters
<dl>

### -param <i>SocketContext</i> [in, optional]

<dd>
<p>A pointer to the socket context for the connection-oriented socket that has been disconnected. The
     WSK application provided this pointer to the WSK subsystem in one of the following ways:
     </p>
<ul>
<li>
<p>It called the 
       <a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a> function to create the socket.</p>
</li>
<li>
<p>It called the 
       <a href="..\wsk\nc-wsk-pfn-wsk-socket-connect.md">WskSocketConnect</a> function to create
       the socket.</p>
</li>
<li>
<p>It called the 
       <a href="..\wsk\nc-wsk-pfn-wsk-accept.md">WskAccept</a> function to accept the socket as an
       incoming connection.</p>
</li>
<li>
<p>Its 
       <a href="..\wsk\nc-wsk-pfn-wsk-accept-event.md">WskAcceptEvent</a> event callback function
       was called to accept the socket as an incoming connection.</p>
</li>
</ul>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A ULONG value that contains a bitwise OR of a combination of the following flags:
     </p>
<p></p>
<dl>

### -param <a id="WSK_FLAG_ABORTIVE"></a><a id="wsk_flag_abortive"></a>WSK_FLAG_ABORTIVE

<dd>
<p>The remote application performed an abortive disconnect of the socket. If this flag is not set,
       the remote application performed a graceful disconnect of the socket.</p>
</dd>

### -param <a id="WSK_FLAG_AT_DISPATCH_LEVEL"></a><a id="wsk_flag_at_dispatch_level"></a>WSK_FLAG_AT_DISPATCH_LEVEL

<dd>
<p>The WSK subsystem called the 
       <i>WskDisconnectEvent</i> event callback function at IRQL = DISPATCH_LEVEL. If this flag is not set,
       the WSK subsystem might have called the 
       <i>WskDisconnectEvent</i> event callback function at any IRQL &lt;= DISPATCH_LEVEL.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>A WSK application's 
     <i>WskDisconnectEvent</i> event callback function must always return STATUS_SUCCESS.</p>

## -remarks
<p>The WSK subsystem calls a WSK application's 
    <i>WskDisconnectEvent</i> event callback function when a connection-oriented socket is disconnected by the
    remote application only if the event callback function was previously enabled with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a> socket option.
    For more information about enabling a socket's event callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If the remote application performed a graceful disconnect of the socket, no further data will be
    received from the socket. However, the WSK application can still send data to the socket until the socket
    is either completely closed by the remote application or the WSK application calls the 
    <a href="..\wsk\nc-wsk-pfn-wsk-disconnect.md">WskDisconnect</a> function or the 
    <a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a> function on the socket.</p>

<p>If the remote application performed an abortive disconnect of the socket, no further data will be
    received from the socket and no further data can be sent to the socket.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskDisconnectEvent</i> event callback function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A WSK application's <i>WskDisconnectEvent</i> event callback function must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback can initiate other WSK requests (assuming that it doesn't spend too much time at DISPATCH_LEVEL), but it must not wait for their completion even when the callback is called at IRQL = PASSIVE_LEVEL.</p>

## -requirements
<table>
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
<a href="..\wsk\nc-wsk-pfn-wsk-accept.md">WskAccept</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-connect.md">WskConnect</a>
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
<a href="..\wsk\nc-wsk-pfn-wsk-accept-event.md">WskAcceptEvent</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-client-connection-dispatch.md">
   WSK_CLIENT_CONNECTION_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_DISCONNECT_EVENT callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
