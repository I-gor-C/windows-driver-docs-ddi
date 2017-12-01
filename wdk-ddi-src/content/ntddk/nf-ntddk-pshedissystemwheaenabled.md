---
UID: NF.ntddk.PshedIsSystemWheaEnabled
title: PshedIsSystemWheaEnabled
author: windows-driver-content
description: The PshedIsSystemWheaEnabled function returns a Boolean value that indicates whether the system is WHEA-enabled.
old-location: whea\pshedissystemwheaenabled.htm
old-project: whea
ms.assetid: d9935605-dc5f-4987-8a5b-b2c2b358dbbf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PshedIsSystemWheaEnabled
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
req.alt-api: PshedIsSystemWheaEnabled
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
req.irql: Any
req.iface: 
---

# PshedIsSystemWheaEnabled function



## -description
<p>The <b>PshedIsSystemWheaEnabled</b> function returns a Boolean value that indicates whether the system is WHEA-enabled.</p>


## -syntax

````
BOOLEAN PshedIsSystemWheaEnabled(void);
````


## -parameters


## -returns
<p>A Boolean value that indicates whether the system is WHEA-enabled.</p>

<p>A Boolean value that indicates whether the system is WHEA-enabled.</p>

<p>A Boolean value that indicates whether the system is WHEA-enabled.</p>

## -remarks
<p>A PSHED plug-in can call the <b>PshedIsSystemWheaEnabled</b> function before it calls the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to verify that the system is WHEA-enabled.</p>

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
<p>Any</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PshedIsSystemWheaEnabled function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
