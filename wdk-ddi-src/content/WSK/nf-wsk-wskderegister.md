---
UID: NF.wsk.WskDeregister
title: WskDeregister
author: windows-driver-content
description: The WskDeregister function unregisters a WSK application's registration instance that was previously created by WskRegister.
old-location: netvista\wskderegister.htm
ms.assetid: b2ff3d7b-319d-4256-a574-cb32595fd02f
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskDeregister
req.alt-loc: Netio.lib,Netio.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Netio.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WskDeregister
req.iface: 
req.product: Windows 10 or later.
---

# WskDeregister function



## -description
<p>The 
  <b>WskDeregister</b> function unregisters a WSK application's registration instance that was previously
  created by 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a>.</p>


## -syntax

````
VOID WskDeregister(
  _In_ PWSK_REGISTRATION WskRegistration
);
````


## -parameters
<dl>

### -param <i>WskRegistration</i> [in]

<dd>
<p>A pointer to the memory location initialized by 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a> that identifies a WSK
     application's registration instance.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For each call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a> that returns a success code, there
    must be exactly one corresponding 
    <b>WskDeregister</b> call that uses the same 
    <i>WskRegistration</i> parameter that was passed to 
    <b>WskRegister</b>.</p>

<p><b>WskDeregister</b> will wait to return until all of the following have completed:</p>

<p>All captured instances of the provider NPI are released.</p>

<p>Any outstanding calls to functions pointed to by 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571175">WSK_PROVIDER_DISPATCH</a> members have
      returned.</p>

<p>All sockets are closed.</p>

<p>For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.</p>

<p>For each call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a> that returns a success code, there
    must be exactly one corresponding 
    <b>WskDeregister</b> call that uses the same 
    <i>WskRegistration</i> parameter that was passed to 
    <b>WskRegister</b>.</p>

<p><b>WskDeregister</b> will wait to return until all of the following have completed:</p>

<p>All captured instances of the provider NPI are released.</p>

<p>Any outstanding calls to functions pointed to by 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571175">WSK_PROVIDER_DISPATCH</a> members have
      returned.</p>

<p>All sockets are closed.</p>

<p>For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Netio.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571178">WSK_REGISTRATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WskDeregister function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
