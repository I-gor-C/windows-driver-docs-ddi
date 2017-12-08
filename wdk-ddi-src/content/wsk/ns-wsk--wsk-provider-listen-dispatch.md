---
UID: NS.wsk._WSK_PROVIDER_LISTEN_DISPATCH
title: WSK_PROVIDER_LISTEN_DISPATCH
author: windows-driver-content
description: The WSK_PROVIDER_LISTEN_DISPATCH structure specifies the WSK subsystem's table of functions for a listening socket.
old-location: netvista\wsk_provider_listen_dispatch.htm
old-project: netvista
ms.assetid: 56df7cb9-9ae7-4249-9583-a9259e604238
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WSK_PROVIDER_LISTEN_DISPATCH, WSK_PROVIDER_LISTEN_DISPATCH, *PWSK_PROVIDER_LISTEN_DISPATCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_PROVIDER_LISTEN_DISPATCH
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

# WSK_PROVIDER_LISTEN_DISPATCH structure



## -description
<p>The WSK_PROVIDER_LISTEN_DISPATCH structure specifies the WSK subsystem's table of functions for a
  listening socket.</p>


## -syntax

````
typedef struct _WSK_PROVIDER_LISTEN_DISPATCH {
  WSK_PROVIDER_BASIC_DISPATCH Basic;
  PFN_WSK_BIND                WskBind;
  PFN_WSK_ACCEPT              WskAccept;
  PFN_WSK_INSPECT_COMPLETE    WskInspectComplete;
  PFN_WSK_GET_LOCAL_ADDRESS   WskGetLocalAddress;
} WSK_PROVIDER_LISTEN_DISPATCH, *PWSK_PROVIDER_LISTEN_DISPATCH;
````


## -struct-fields
<dl>

### -field Basic

<dd>
<p>The members of the 
     <a href="..\wsk\ns-wsk--wsk-provider-basic-dispatch.md">
     WSK_PROVIDER_BASIC_DISPATCH</a> structure are included as members of the WSK_PROVIDER_LISTEN_DISPATCH
     structure.</p>
</dd>

### -field WskBind

<dd>
<p>A pointer to the WSK subsystem's 
     <a href="..\wsk\nc-wsk-pfn-wsk-bind.md">WskBind</a> function for the socket.</p>
</dd>

### -field WskAccept

<dd>
<p>A pointer to the WSK subsystem's 
     <a href="..\wsk\nc-wsk-pfn-wsk-accept.md">WskAccept</a> function for the socket.</p>
</dd>

### -field WskInspectComplete

<dd>
<p>A pointer to the WSK subsystem's 
     <a href="..\wsk\nc-wsk-pfn-wsk-inspect-complete.md">WskInspectComplete</a> function for the
     socket.</p>
</dd>

### -field WskGetLocalAddress

<dd>
<p>A pointer to the WSK subsystem's 
     <a href="..\wsk\nc-wsk-pfn-wsk-get-local-address.md">WskGetLocalAddress</a> function for the
     socket.</p>
</dd>
</dl>

## -remarks
<p>The member list of the WSK_PROVIDER_LISTEN_DISPATCH structure includes an unnamed 
    <a href="..\wsk\ns-wsk--wsk-provider-basic-dispatch.md">
    WSK_PROVIDER_BASIC_DISPATCH</a> structure. The compiler that is included with the WDK supports a
    Microsoft-specific extension to the C language that allows unnamed structures within structure
    declarations. The result is that the structure members of the WSK_PROVIDER_BASIC_DISPATCH structure are
    included in the WSK_PROVIDER_LISTEN_DISPATCH structure as if they were native members of the
    WSK_PROVIDER_LISTEN_DISPATCH structure.</p>

<p>A WSK application receives a pointer to a WSK_PROVIDER_LISTEN_DISPATCH structure when the WSK
    application calls the 
    <a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a> function to create a listening socket.
    The pointer is contained in the 
    <b>Dispatch</b> member of the 
    <a href="..\wsk\ns-wsk--wsk-socket.md">WSK_SOCKET</a> structure that is received from the
    WSK subsystem.</p>

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
<a href="..\wsk\nc-wsk-pfn-wsk-accept.md">WskAccept</a>
</dt>
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
<a href="..\wsk\nc-wsk-pfn-wsk-inspect-complete.md">WskInspectComplete</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-client-listen-dispatch.md">WSK_CLIENT_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-basic-dispatch.md">WSK_PROVIDER_BASIC_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-socket.md">WSK_SOCKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_PROVIDER_LISTEN_DISPATCH structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
