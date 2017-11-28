---
UID: NC.wsk.PFN_WSK_RECEIVE_FROM_EVENT
title: PFN_WSK_RECEIVE_FROM_EVENT
author: windows-driver-content
description: The WskReceiveFromEvent event callback function notifies a WSK application that one or more datagrams have been received on a datagram socket.
old-location: netvista\wskreceivefromevent.htm
old-project: netvista
ms.assetid: 1cdb8a70-54fe-44a6-a16c-71cbf6a49ef2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskReceiveFromEvent
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

# PFN_WSK_RECEIVE_FROM_EVENT callback



## -description
<p>The 
  <i>WskReceiveFromEvent</i> event callback function notifies a WSK application that one or more datagrams
  have been received on a datagram socket.</p>


## -prototype

````
PFN_WSK_RECEIVE_FROM_EVENT WskReceiveFromEvent;

NTSTATUS APIENTRY WskReceiveFromEvent(
  _In_opt_ PVOID                    SocketContext,
  _In_     ULONG                    Flags,
  _In_opt_ PWSK_DATAGRAM_INDICATION DataIndication
)
{ ... }
````


## -parameters
<dl>

### -param <i>SocketContext</i> [in, optional]

<dd>
<p>A pointer to the socket context for the datagram socket that has received the datagrams. The WSK
     application provided this pointer to the WSK subsystem when it called the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a> function to create the datagram
     socket.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A ULONG value that contains a bitwise OR of a combination of the following flags:
     </p>
<p></p>
<dl>

### -param <a id="MSG_BCAST"></a><a id="msg_bcast"></a>MSG_BCAST

<dd>
<p>The datagrams were received as a link-layer broadcast or with a destination transport address
       that is a broadcast address.</p>
</dd>

### -param <a id="MSG_MCAST"></a><a id="msg_mcast"></a>MSG_MCAST

<dd>
<p>The datagrams were received with a destination transport address that is a multicast
       address.</p>
</dd>

### -param <a id="WSK_FLAG_AT_DISPATCH_LEVEL"></a><a id="wsk_flag_at_dispatch_level"></a>WSK_FLAG_AT_DISPATCH_LEVEL

<dd>
<p>The WSK subsystem called the 
       <i>WskReceiveFromEvent</i> event callback function at IRQL = DISPATCH_LEVEL. If this flag is not set,
       the WSK subsystem might have called the 
       <i>WskReceiveFromEvent</i> event callback function at any IRQL &lt;= DISPATCH_LEVEL.</p>
</dd>
</dl>
</dd>

### -param <i>DataIndication</i> [in, optional]

<dd>
<p>A pointer to a linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571164">WSK_DATAGRAM_INDICATION</a> structures
     that describe the received datagrams. If this parameter is <b>NULL</b>, the socket is no longer functional and
     the WSK application must call the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> function to close the
     socket as soon as possible.</p>
</dd>
</dl>

## -returns
<p>A WSK application's 
     <i>WskReceiveFromEvent</i> event callback function can return one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The WSK application accepted the datagrams and retrieved all of the datagrams from the linked
       list of 
       <a href="..\wsk\ns-wsk--wsk-datagram-indication.md">
       WSK_DATAGRAM_INDICATION</a> structures. The WSK subsystem can call the 
       <i>WskReceiveFromEvent</i> event callback function again when new datagrams are received on the
       socket.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK application accepted the datagrams but did not retrieve all of the datagrams from the
       linked list of 
       <a href="..\wsk\ns-wsk--wsk-datagram-indication.md">
       WSK_DATAGRAM_INDICATION</a> structures. The WSK application retains the linked list of
       WSK_DATAGRAM_INDICATION structures until all of the datagrams have been retrieved. After the WSK
       application has retrieved all of the datagrams, it calls the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571144">WskRelease</a> function to release the linked
       list of WSK_DATAGRAM_INDICATION structures back to the WSK subsystem. The WSK subsystem can call the 
       <i>WskReceiveFromEvent</i> event callback function again when new datagrams are received on the
       socket.</p><dl>
<dt><b>STATUS_DATA_NOT_ACCEPTED</b></dt>
</dl><p>The WSK application did not accept the datagrams. If a WSK application returns this status code,
       the WSK subsystem will respond differently depending on how the WSK application enabled the 
       <i>WskReceiveFromEvent</i> event callback function.
       </p>

<p>If the WSK application enabled the 
         <i>WskReceiveFromEvent</i> event callback function by using the 
         <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a> socket
         option, the WSK subsystem will have the underlying transport buffer the datagrams if possible or if
         otherwise required by the protocol. The WSK subsystem will disable the 
         <i>WskReceiveFromEvent</i> event callback function and will not call the 
         <i>WskReceiveFromEvent</i> event callback function again until after the WSK application re-enables
         this event callback function with the SO_WSK_EVENT_CALLBACK socket option. After the WSK application
         has re-enabled the 
         <i>WskReceiveFromEvent</i> event callback function, the WSK subsystem will resume calling the 
         <i>WskReceiveFromEvent</i> event callback function with any remaining buffered datagrams and when new
         datagrams are received on the socket.</p>

<p>If the WSK application enabled the 
         <i>WskReceiveFromEvent</i> event callback function by using the 
         <a href="netvista.wsk_set_static_event_callbacks">
         WSK_SET_STATIC_EVENT_CALLBACKS</a> client control operation, the WSK subsystem will not disable
         the 
         <i>WskReceiveFromEvent</i> event callback function. The WSK subsystem will continue calling the 
         <i>WskReceiveFromEvent</i> event callback function when new datagrams are received on the socket.</p>

<p> </p>

## -remarks
<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveFromEvent</i> event callback function when new datagrams are received on a datagram socket
    only if the event callback function was previously enabled with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a> socket option.
    For more information about enabling a socket's event callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If a WSK application's 
    <i>WskReceiveFromEvent</i> event callback function is enabled on a datagram socket and the application
    also has a pending call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571141">WskReceiveFrom</a> function on the same
    datagram socket, then, when datagrams arrive, the pending call to the 
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
    <i>WskReceiveFromEvent</i> event callback function on the socket.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveFromEvent</i> event callback function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A WSK application's <i>WskReceiveFromEvent</i> event callback function must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback can initiate other WSK requests (assuming that it doesn't spend too much time at DISPATCH_LEVEL), but it must not wait for their completion even when the callback is called at IRQL = PASSIVE_LEVEL.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveFromEvent</i> event callback function when new datagrams are received on a datagram socket
    only if the event callback function was previously enabled with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a> socket option.
    For more information about enabling a socket's event callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If a WSK application's 
    <i>WskReceiveFromEvent</i> event callback function is enabled on a datagram socket and the application
    also has a pending call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571141">WskReceiveFrom</a> function on the same
    datagram socket, then, when datagrams arrive, the pending call to the 
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
    <i>WskReceiveFromEvent</i> event callback function on the socket.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveFromEvent</i> event callback function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A WSK application's <i>WskReceiveFromEvent</i> event callback function must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback can initiate other WSK requests (assuming that it doesn't spend too much time at DISPATCH_LEVEL), but it must not wait for their completion even when the callback is called at IRQL = PASSIVE_LEVEL.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571127">WskControlSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571141">WskReceiveFrom</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571144">WskRelease</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571148">WskSendTo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571164">WSK_DATAGRAM_INDICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571158">WSK_CLIENT_DATAGRAM_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_RECEIVE_FROM_EVENT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
