---
UID: NS.wsk._WSK_CLIENT_DISPATCH
title: WSK_CLIENT_DISPATCH
author: windows-driver-content
description: The WSK_CLIENT_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for events that are not specific to a particular socket.
old-location: netvista\wsk_client_dispatch.htm
old-project: netvista
ms.assetid: 6a6116b0-2070-4b46-8359-3c84529cd1c5
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WSK_CLIENT_DISPATCH, WSK_CLIENT_DISPATCH, *PWSK_CLIENT_DISPATCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_CLIENT_DISPATCH
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

# WSK_CLIENT_DISPATCH structure



## -description
<p>The WSK_CLIENT_DISPATCH structure specifies a WSK application's dispatch table of event callback
  functions for events that are not specific to a particular socket.</p>


## -syntax

````
typedef struct _WSK_CLIENT_DISPATCH {
  USHORT               Version;
  USHORT               Reserved;
  PFN_WSK_CLIENT_EVENT WskClientEvent;
} WSK_CLIENT_DISPATCH, *PWSK_CLIENT_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the WSK 
     <a href="netvista.network_programming_interface">Network Programming Interface
     (NPI)</a> that the WSK application would like to use.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. WSK applications must set this member to zero.</p>
</dd>

### -field <b>WskClientEvent</b>

<dd>
<p>A pointer to the WSK application's 
     <a href="..\wsk\nc-wsk-pfn-wsk-client-event.md">WskClientEvent</a> event callback function. If
     a WSK application does not implement a 
     <i>WskClientEvent</i> event callback function, this member must be set to <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>When a WSK application calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a> function, it provides a pointer to
    an initialized WSK_CLIENT_DISPATCH structure by means of the 
    <b>Dispatch</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571163">WSK_CLIENT_NPI</a> structure pointed to by the 
    <i>WskClientNpi</i> parameter.</p>

<p>The major and minor version numbers that are contained within the 
    <b>Version</b> member are encoded by using the MAKE_WSK_VERSION macro:</p>

<p>The major and minor version numbers can be extracted from the 
    <b>Version</b> member by using the WSK_MAJOR_VERSION and WSK_MINOR_VERSION macros:</p>

<p>For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.</p>

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
<a href="..\wsk\nc-wsk-pfn-wsk-client-event.md">WskClientEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571163">WSK_CLIENT_NPI</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571175">WSK_PROVIDER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571177">WSK_PROVIDER_NPI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_CLIENT_DISPATCH structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
