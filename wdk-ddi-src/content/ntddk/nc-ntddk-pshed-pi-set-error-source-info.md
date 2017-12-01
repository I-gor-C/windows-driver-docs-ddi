---
UID: NC.ntddk.PSHED_PI_SET_ERROR_SOURCE_INFO
title: PSHED_PI_SET_ERROR_SOURCE_INFO
author: windows-driver-content
description: A PSHED plug-in's SetErrorSourceInfo callback function configures an error source.
old-location: whea\seterrorsourceinfo.htm
old-project: whea
ms.assetid: 0b9cd546-d4ad-4e0e-92cb-7994c7327977
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetErrorSourceInfo
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# PSHED_PI_SET_ERROR_SOURCE_INFO callback



## -description
<p>A PSHED plug-in's <i>SetErrorSourceInfo</i> callback function configures an error source.</p>


## -prototype

````
PSHED_PI_SET_ERROR_SOURCE_INFO SetErrorSourceInfo;

NTSTATUS SetErrorSourceInfo(
  _Inout_opt_ PVOID                         PluginContext,
  _In_        PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource
)
{ ... }
````


## -parameters
<dl>

### -param <i>PluginContext</i> [in, out, optional]

<dd>
<p>A pointer to the context area that was specified in the <b>Context</b> member of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure when the PSHED plug-in called the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>
</dd>

### -param <i>ErrorSource</i> [in]

<dd>
<p>A pointer to a <a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that describes the error source that is being configured.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>SetErrorSourceInfo</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The error source was successfully configured.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The PSHED plug-in does not support configuration of the specified error source.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error source control sets the <b>Callbacks.SetErrorSourceInfo</b>, <b>Callbacks.EnableErrorSource</b>, and <b>Callbacks.DisableErrorSource</b> members of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>SetErrorSourceInfo</i>, <a href="..\ntddk\nc-ntddk-pshed-pi-enable-error-source.md">EnableErrorSource</a>, and <a href="..\ntddk\nc-ntddk-pshed-pi-disable-error-source.md">DisableErrorSource</a> callback functions when the plug-in calls the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorSourceControl</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to configure an error source in response to an error source configuration request by a WHEA management application. If a PSHED plug-in is registered to participate in error source control, the PSHED calls the PSHED plug-in's <i>SetErrorSourceInfo</i> callback function to give the PSHED plug-in an opportunity to perform the error source configuration operation. The error source configuration data is included in the <a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that is pointed to by the <i>ErrorSource</i> parameter.</p>

<p>If the PSHED plug-in does not support configuration of the specified error source, the <i>SetErrorSourceInfo</i> callback function returns STATUS_NOT_SUPPORTED. In this situation, the PSHED performs the requested error source configuration operation.</p>

<p>If the PSHED plug-in's supports configuration of the specified error source, the <i>SetErrorSourceInfo</i> callback function should save the error source's configuration data in the registry, in the system's BIOS tables, or in some other form of nonvolatile data storage that is available to the error source. The specific form of nonvolatile data storage that is used by an error source for storing the error source's configuration data is implementation-specific. The <i>SetErrorSourceInfo</i> callback function should apply the configuration data to the error source in such a way that the configuration changes become effective the next time that the system is restarted. When the system is restarted, the PSHED plug-in should report the new error source configuration data for the error source to the operating system during error source discovery.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-disable-error-source.md">DisableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-enable-error-source.md">EnableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_SET_ERROR_SOURCE_INFO callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
