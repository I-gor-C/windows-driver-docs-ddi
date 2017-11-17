---
UID: NS.wsk._WSK_CLIENT_LISTEN_DISPATCH
title: WSK_CLIENT_LISTEN_DISPATCH
author: windows-driver-content
description: The WSK_CLIENT_LISTEN_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a listening socket.
old-location: netvista\wsk_client_listen_dispatch.htm
ms.assetid: aaef10f5-2933-4e16-aca6-2277b52fb174
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
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
req.alt-api: WSK_CLIENT_LISTEN_DISPATCH
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
ms.keywords: WSK_CLIENT_LISTEN_DISPATCH, WSK_CLIENT_LISTEN_DISPATCH, *PWSK_CLIENT_LISTEN_DISPATCH
req.iface: 
req.product: Windows 10 or later.
---

# WSK_CLIENT_LISTEN_DISPATCH structure



## -description
<p>The WSK_CLIENT_LISTEN_DISPATCH structure specifies a WSK application's dispatch table of event
  callback functions for a listening socket.</p>


## -syntax

````
typedef struct _WSK_CLIENT_LISTEN_DISPATCH {
  PFN_WSK_ACCEPT_EVENT  WskAcceptEvent;
  PFN_WSK_INSPECT_EVENT WskInspectEvent;
  PFN_WSK_ABORT_EVENT   WskAbortEvent;
} WSK_CLIENT_LISTEN_DISPATCH, *PWSK_CLIENT_LISTEN_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>WskAcceptEvent</b>

<dd>
<p>A pointer to the WSK application's 
     <a href="https://msdn.microsoft.com/672440f0-810a-4e68-82a5-d038770898c5">WskAcceptEvent</a> event callback function for
     the socket. If the WSK application does not enable the 
     <i>WskAcceptEvent</i> event callback function for the socket, this pointer can be <b>NULL</b>.</p>
</dd>

### -field <b>WskInspectEvent</b>

<dd>
<p>A pointer to the WSK application's 
     <a href="https://msdn.microsoft.com/40f184ac-4ef3-485a-a529-71c1f2716427">WskInspectEvent</a> event callback function
     for the socket. If the WSK application does not enable conditional accept mode for the socket, this
     pointer can be <b>NULL</b>.</p>
</dd>

### -field <b>WskAbortEvent</b>

<dd>
<p>A pointer to the WSK application's 
     <a href="https://msdn.microsoft.com/50e0ef5d-0577-4b5c-b541-fc78079a953c">WskAbortEvent</a> event callback function for
     the socket. If the WSK application does not enable conditional accept mode for the socket, this pointer
     can be <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>A WSK application passes a pointer to a WSK_CLIENT_LISTEN_DISPATCH structure to the WSK subsystem when
    the WSK application calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a> function to create a listening
    socket.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/50e0ef5d-0577-4b5c-b541-fc78079a953c">WskAbortEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/672440f0-810a-4e68-82a5-d038770898c5">WskAcceptEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/40f184ac-4ef3-485a-a529-71c1f2716427">WskInspectEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571176">WSK_PROVIDER_LISTEN_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_CLIENT_LISTEN_DISPATCH structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
