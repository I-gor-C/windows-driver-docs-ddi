---
UID: NC.wsk.PFN_WSK_RECEIVE_EVENT
title: PFN_WSK_RECEIVE_EVENT
author: windows-driver-content
description: The WskReceiveEvent event callback function notifies a WSK application that data has been received on a connection-oriented socket.
old-location: netvista\wskreceiveevent.htm
ms.assetid: 2a7a7570-ed26-48be-b27b-dc240588ecfc
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskReceiveEvent
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
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
req.iface: 
req.product: Windows 10 or later.
---

# PFN_WSK_RECEIVE_EVENT callback



## -description
<p>The 
  <i>WskReceiveEvent</i> event callback function notifies a WSK application that data has been received on a
  connection-oriented socket.</p>


## -prototype

````
PFN_WSK_RECEIVE_EVENT WskReceiveEvent;

NTSTATUS APIENTRY WskReceiveEvent(
  _In_opt_ PVOID                SocketContext,
  _In_     ULONG                Flags,
  _In_opt_ PWSK_DATA_INDICATION DataIndication,
  _In_     SIZE_T               BytesIndicated,
  _Inout_  SIZE_T               *BytesAccepted
)
{ ... }
````


## -parameters
<dl>

### -param <i>SocketContext</i> [in, optional]

<dd>
<p>A pointer to the socket context for the connection-oriented socket that has received the data. The
     WSK application provided this pointer to the WSK subsystem in one of the following ways:
     </p>
<ul>
<li>
<p>It called the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a> function to create the socket.</p>
</li>
<li>
<p>It called the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a> function to create
       the socket.</p>
</li>
<li>
<p>It called the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571109">WskAccept</a> function to accept the socket as an
       incoming connection.</p>
</li>
<li>
<p>Its 
       <a href="https://msdn.microsoft.com/672440f0-810a-4e68-82a5-d038770898c5">WskAcceptEvent</a> event callback function
       was called to accept the socket as an incoming connection.</p>
</li>
</ul>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A ULONG value that contains a bitwise OR of a combination of the following flags:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="WSK_FLAG_RELEASE_ASAP"></a><a id="wsk_flag_release_asap"></a><dl>

### -param <b>WSK_FLAG_RELEASE_ASAP</b>

</dl>
</td>
<td width="60%">
<p>The data buffers that contain the received data should not be retained by the WSK application if
       at all possible. If the WSK application retains the buffers, it should release them as soon as
       possible by calling the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571144">WskRelease</a> function.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WSK_FLAG_ENTIRE_MESSAGE"></a><a id="wsk_flag_entire_message"></a><dl>

### -param <b>WSK_FLAG_ENTIRE_MESSAGE</b>

</dl>
</td>
<td width="60%">
<p>The data buffers contain either an entire message or the final portion of a message. The
       interpretation of what constitutes an entire message is transport protocol-specific. For TCP, this
       flag indicates that the push bit was set for one or more of the TCP segments that constitute the data
       in the data buffers.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WSK_FLAG_AT_DISPATCH_LEVEL"></a><a id="wsk_flag_at_dispatch_level"></a><dl>

### -param <b>WSK_FLAG_AT_DISPATCH_LEVEL</b>

</dl>
</td>
<td width="60%">
<p>The WSK subsystem called the 
       <i>WskReceiveEvent</i> event callback function at IRQL = DISPATCH_LEVEL. If this flag is not set, the
       WSK subsystem might have called the 
       <i>WskReceiveEvent</i> event callback function at any IRQL &lt;= DISPATCH_LEVEL.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>DataIndication</i> [in, optional]

<dd>
<p>A pointer to a linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571165">WSK_DATA_INDICATION</a> structures that
     describe the received data. If this parameter is <b>NULL</b>, the socket is no longer functional and the WSK
     application must call the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> function to close the
     socket as soon as possible.</p>
</dd>

### -param <i>BytesIndicated</i> [in]

<dd>
<p>The number of bytes of received data described by the linked list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571165">WSK_DATA_INDICATION</a> structures.</p>
</dd>

### -param <i>BytesAccepted</i> [in, out]

<dd>
<p>A pointer to a SIZE_T-typed variable which receives the number of bytes of received data that is
     accepted by the WSK application. This variable needs to be set only if the WSK application accepts a
     portion of the total number of bytes of received data. If the WSK application accepts all of the
     received data, it does not have to set this variable. If the 
     <i>WskReceiveEvent</i> event callback function returns a status other than STATUS_SUCCESS, the WSK
     subsystem ignores the value of this variable.</p>
</dd>
</dl>

## -returns
<p>A WSK application's 
     <i>WskReceiveEvent</i> event callback function can return one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The WSK application accepted at least some of the received data. If the WSK application accepted
       all of the received data, the WSK subsystem can call the 
       <i>WskReceiveEvent</i> event callback function again when new data is received on the socket. However,
       if the WSK application accepted only a portion of the received data, the WSK subsystem will not call
       the 
       <i>WskReceiveEvent</i> event callback function again until after the WSK application calls the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a> function. After the WSK
       application calls the 
       <b>WskReceive</b> function, the WSK subsystem will resume calling the 
       <i>WskReceiveEvent</i> event callback function with any remaining buffered data and when new data is
       received on the socket. A WSK application can call the 
       <b>WskReceive</b> function with a zero-length buffer, which will cause the WSK subsystem to resume
       calling the 
       <i>WskReceiveEvent</i> event callback function without calling 
       <b>WskReceive</b> to receive any data from the socket.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK application accepted the data but did not retrieve all of the data contained in the
       linked list of 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571165">WSK_DATA_INDICATION</a> structures. The
       WSK application retains the linked list of WSK_DATA_INDICATION structures until all of the data has
       been retrieved. After the WSK application has retrieved all of the data it calls the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571144">WskRelease</a> function to release the linked
       list of WSK_DATA_INDICATION structures back to the WSK subsystem. The WSK subsystem can call the 
       <i>WskReceiveEvent</i> event callback function again when new data is received on the socket.</p><dl>
<dt><b>STATUS_DATA_NOT_ACCEPTED</b></dt>
</dl><p>The WSK application did not accept the data. In this situation, the WSK subsystem will have the
       underlying transport buffer the data if possible or if otherwise required by the protocol. The WSK
       subsystem will not call the 
       <i>WskReceiveEvent</i> event callback function again until after the WSK application calls the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a> function. After the WSK
       application calls the 
       <b>WskReceive</b> function, the WSK subsystem will resume calling the 
       <i>WskReceiveEvent</i> event callback function with any remaining buffered data and when new data is
       received on the socket. A WSK application can call the 
       <b>WskReceive</b> function with a zero-length buffer, which will cause the WSK subsystem to resume
       calling the 
       <i>WskReceiveEvent</i> event callback function without calling 
       <b>WskReceive</b> to receive any data from the socket.</p>

<p> </p>

## -remarks
<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveEvent</i> event callback function when new data is received on a connection-oriented socket
    only if the event callback function was previously enabled with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a> socket option.
    For more information about enabling a socket's event callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If a WSK application's 
    <i>WskReceiveEvent</i> event callback function is enabled on a connection-oriented socket and the
    application also has a pending call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a> function on the same
    connection-oriented socket, then, when data arrives, the pending call to the 
    <b>WskReceive</b> function will take precedence over the 
    <i>WskReceiveEvent</i> event callback function. The WSK subsystem calls the application's 
    <i>WskReceiveEvent</i> event callback function only if there are no IRPs queued from pending calls to the 
    <b>WskReceive</b> function. However, a WSK application should not assume that the WSK subsystem will not
    call the application's 
    <i>WskReceiveEvent</i> event callback function for a connection-oriented socket that has a pending call to
    the 
    <b>WskReceive</b> function. Race conditions exist where the WSK subsystem could still call the WSK
    application's 
    <i>WskReceiveEvent</i> event callback function for the socket. The only way for a WSK application to
    ensure that the WSK subsystem will not call the application's 
    <i>WskReceiveEvent</i> event callback function for a connection-oriented socket is to disable the
    application's 
    <i>WskReceiveEvent</i> event callback function on the socket.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveEvent</i> event callback function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A WSK application's <i>WskReceiveEvent</i> event callback function must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback can initiate other WSK requests (assuming that it doesn't spend too much time at DISPATCH_LEVEL), but it must not wait for their completion even when the callback is called at IRQL = PASSIVE_LEVEL.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveEvent</i> event callback function when new data is received on a connection-oriented socket
    only if the event callback function was previously enabled with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a> socket option.
    For more information about enabling a socket's event callback functions, see 
    <a href="netvista.enabling_and_disabling_event_callback_functions">Enabling and
    Disabling Event Callback Functions</a>.</p>

<p>If a WSK application's 
    <i>WskReceiveEvent</i> event callback function is enabled on a connection-oriented socket and the
    application also has a pending call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a> function on the same
    connection-oriented socket, then, when data arrives, the pending call to the 
    <b>WskReceive</b> function will take precedence over the 
    <i>WskReceiveEvent</i> event callback function. The WSK subsystem calls the application's 
    <i>WskReceiveEvent</i> event callback function only if there are no IRPs queued from pending calls to the 
    <b>WskReceive</b> function. However, a WSK application should not assume that the WSK subsystem will not
    call the application's 
    <i>WskReceiveEvent</i> event callback function for a connection-oriented socket that has a pending call to
    the 
    <b>WskReceive</b> function. Race conditions exist where the WSK subsystem could still call the WSK
    application's 
    <i>WskReceiveEvent</i> event callback function for the socket. The only way for a WSK application to
    ensure that the WSK subsystem will not call the application's 
    <i>WskReceiveEvent</i> event callback function for a connection-oriented socket is to disable the
    application's 
    <i>WskReceiveEvent</i> event callback function on the socket.</p>

<p>The WSK subsystem calls a WSK application's 
    <i>WskReceiveEvent</i> event callback function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A WSK application's <i>WskReceiveEvent</i> event callback function must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback can initiate other WSK requests (assuming that it doesn't spend too much time at DISPATCH_LEVEL), but it must not wait for their completion even when the callback is called at IRQL = PASSIVE_LEVEL.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571109">WskAccept</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571144">WskRelease</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571146">WskSend</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/672440f0-810a-4e68-82a5-d038770898c5">WskAcceptEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571165">WSK_DATA_INDICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/960eee8a-2950-4baf-b32d-be13b3d65951">
   WSK_CLIENT_CONNECTION_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_RECEIVE_EVENT callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
