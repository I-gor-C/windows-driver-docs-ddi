---
UID: NS.ntddk._WHEA_PSHED_PLUGIN_REGISTRATION_PACKET
title: WHEA_PSHED_PLUGIN_REGISTRATION_PACKET
author: windows-driver-content
description: The WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure describes the data required for registering a PSHED plug-in with the PSHED.
old-location: whea\whea_pshed_plugin_registration_packet.htm
old-project: whea
ms.assetid: 9dafa65f-26f6-42a6-a125-013c61a66ccc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_PSHED_PLUGIN_REGISTRATION_PACKET,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_PSHED_PLUGIN_REGISTRATION_PACKET
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure



## -description
<p>The WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure describes the data required for registering a PSHED plug-in with the PSHED.</p>


## -syntax

````
typedef struct _WHEA_PSHED_PLUGIN_REGISTRATION_PACKET {
  ULONG                       Length;
  ULONG                       Version;
  PVOID                       Context;
  ULONG                       FunctionalAreaMask;
  ULONG                       Reserved;
  WHEA_PSHED_PLUGIN_CALLBACKS Callbacks;
} WHEA_PSHED_PLUGIN_REGISTRATION_PACKET, *PWHEA_PSHED_PLUGIN_REGISTRATION_PACKET;
````


## -struct-fields
<dl>

### -field Length

<dd>
<p>The size, in bytes, of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>
</dd>

### -field Version

<dd>
<p>The version of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure. PSHED plug-ins must set this member to WHEA_PLUGIN_REGISTRATION_PACKET_VERSION.</p>
</dd>

### -field Context

<dd>
<p>A PSHED plug-in-supplied context area that is passed to the PSHED plug-in's callback functions.</p>
</dd>

### -field FunctionalAreaMask

<dd>
<p>A bit-wise OR'ed combination of flags that specifies the functional areas in which the PSHED plug-in participates. Possible flags are:</p>
<p></p>
<dl>

### -field PshedFADiscovery

<dd>
<p>The PSHED plug-in participates in error source discovery.</p>
</dd>

### -field PshedFAErrorSourceControl

<dd>
<p>The PSHED plug-in participates in error source control.</p>
</dd>

### -field PshedFAErrorRecordPersistence

<dd>
<p>The PSHED plug-in participates in error record persistence.</p>
</dd>

### -field PshedFAErrorInfoRetrieval

<dd>
<p>The PSHED plug-in participates in error information retrieval.</p>
</dd>

### -field PshedFAErrorRecovery

<dd>
<p>The PSHED plug-in participates in error recovery.</p>
</dd>

### -field PshedFAErrorInjection

<dd>
<p>The PSHED plug-in participates in error injection.</p>
</dd>
</dl>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use. PSHED plug-ins should set this member to zero.</p>
</dd>

### -field Callbacks

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-callbacks.md">WHEA_PSHED_PLUGIN_CALLBACKS</a> structure that describes the callback functions for the PSHED plug-in.</p>
</dd>
</dl>

## -remarks
<p>A PSHED plug-in passes an initialized WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure to the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function when it registers itself with the PSHED.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-pshed-plugin-callbacks.md">WHEA_PSHED_PLUGIN_CALLBACKS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
