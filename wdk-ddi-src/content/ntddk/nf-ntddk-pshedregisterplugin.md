---
UID: NF.ntddk.PshedRegisterPlugin
title: PshedRegisterPlugin
author: windows-driver-content
description: The PshedRegisterPlugin function registers a PSHED plug-in with the PSHED.
old-location: whea\pshedregisterplugin.htm
old-project: whea
ms.assetid: 8ad93312-932c-417c-8198-9ba515e3d55d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PshedRegisterPlugin
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PshedRegisterPlugin
req.alt-loc: Pshed.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Pshed.lib
req.dll: Pshed.dll
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# PshedRegisterPlugin function



## -description
<p>The <b>PshedRegisterPlugin</b> function registers a PSHED plug-in with the PSHED.</p>


## -syntax

````
NTSTATUS PshedRegisterPlugin(
  _Inout_ PWHEA_PSHED_PLUGIN_REGISTRATION_PACKET Packet
);
````


## -parameters
<dl>

### -param <i>Packet</i> [in, out]

<dd>
<p>A pointer to an initialized  <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure that describes the PSHED plug-in's registration information.</p>
</dd>
</dl>

## -returns
<p><b>PshedRegisterPlugin</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The PSHED plug-in was successfully registered.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The data in the supplied registration packet is invalid.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in calls the <b>PshedRegisterPlugin</b> function to register itself with the PSHED. A PSHED plug-in typically calls this function from within either its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function or its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> function.</p>

<p>A PSHED plug-in calls the <b>PshedRegisterPlugin</b> function to register itself with the PSHED. A PSHED plug-in typically calls this function from within either its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function or its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> function.</p>

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
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Pshed.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Pshed.dll</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PshedRegisterPlugin function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
