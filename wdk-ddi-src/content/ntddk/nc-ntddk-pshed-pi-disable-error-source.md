---
UID: NC.ntddk.PSHED_PI_DISABLE_ERROR_SOURCE
title: PSHED_PI_DISABLE_ERROR_SOURCE
author: windows-driver-content
description: A PSHED plug-in's DisableErrorSource callback function disables an error source.
old-location: whea\disableerrorsource.htm
old-project: whea
ms.assetid: 062927db-9581-447a-820b-82687710ea8d
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
req.alt-api: DisableErrorSource
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

# PSHED_PI_DISABLE_ERROR_SOURCE callback



## -description
<p>A PSHED plug-in's <i>DisableErrorSource</i> callback function disables an error source.</p>


## -prototype

````
PSHED_PI_DISABLE_ERROR_SOURCE DisableErrorSource;

NTSTATUS DisableErrorSource(
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
<p>A pointer to a <a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that describes the error source that is being disabled.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>DisableErrorSource</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The error source was successfully disabled.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The PSHED plug-in does not support disabling the specified error source.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error source control sets the <b>Callbacks.SetErrorSourceInfo</b>, <b>Callbacks.EnableErrorSource</b>, and <b>Callbacks.DisableErrorSource</b> members of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-set-error-source-info.md">SetErrorSourceInfo</a>, <a href="..\ntddk\nc-ntddk-pshed-pi-enable-error-source.md">EnableErrorSource</a>, and <i>DisableErrorSource</i> callback functions when the plug-in calls the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorSourceControl</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to disable an error source in response to an error source disable request by a WHEA management application. If a PSHED plug-in is registered to participate in error source control, the PSHED calls the PSHED plug-in's <i>DisableErrorSource</i> callback function to give the PSHED plug-in an opportunity to disable the error source. If the <i>DisableErrorSource</i> callback function returns STATUS_NOT_SUPPORTED, the PSHED will disable the error source. Otherwise, the PSHED will just return the return value that is returned by the <i>DisableErrorSource</i> callback function.</p>

<p>If the PSHED plug-in successfully disables the error source, the PSHED will update the WHEA_ERROR_SOURCE_DESCRIPTOR structure on behalf of the PSHED plug-in after the call to the PSHED plug-in's <i>DisableErrorSource</i> callback function returns. A PSHED plug-in's <i>DisableErrorSource</i> callback function should not modify the error source descriptor.</p>

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
<a href="..\ntddk\nc-ntddk-pshed-pi-enable-error-source.md">EnableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-set-error-source-info.md">SetErrorSourceInfo</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_DISABLE_ERROR_SOURCE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
