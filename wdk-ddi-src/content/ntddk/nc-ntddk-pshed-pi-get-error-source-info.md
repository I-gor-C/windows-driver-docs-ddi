---
UID: NC.ntddk.PSHED_PI_GET_ERROR_SOURCE_INFO
title: PSHED_PI_GET_ERROR_SOURCE_INFO
author: windows-driver-content
description: A PSHED plug-in's GetErrorSourceInfo callback function returns an error source descriptor structure that represents a particular error source that is implemented by the hardware platform.
old-location: whea\geterrorsourceinfo.htm
old-project: whea
ms.assetid: 8ede391a-acda-4540-a8bb-1b232695d632
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
req.alt-api: GetErrorSourceInfo
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

# PSHED_PI_GET_ERROR_SOURCE_INFO callback



## -description
<p>A PSHED plug-in's <i>GetErrorSourceInfo</i> callback function returns an error source descriptor structure that represents a particular error source that is implemented by the hardware platform.</p>


## -prototype

````
PSHED_PI_GET_ERROR_SOURCE_INFO GetErrorSourceInfo;

NTSTATUS GetErrorSourceInfo(
  _Inout_opt_ PVOID                         PluginContext,
  _Inout_     PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource
)
{ ... }
````


## -parameters
<dl>

### -param <i>PluginContext</i> [in, out, optional]

<dd>
<p>A pointer to the context area that was specified in the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure when the PSHED plug-in called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>
</dd>

### -param <i>ErrorSource</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that represents a particular error source that is implemented by the hardware platform.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>GetErrorSourceInfo</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The error source information was successfully updated.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error source discovery sets the <b>Callbacks.GetAllErrorSources </b>member and, optionally, the <b>Callbacks.GetErrorSourceInfo </b>member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-get-all-error-sources.md">GetAllErrorSources</a> and <i>GetErrorSourceInfo</i> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFADiscovery</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to obtain additional details about a particular error source. This occurs when a new error source is added to the system by a bus driver. For example, when the PCI driver discovers a PCI Express (PCIe) device that is capable of reporting PCIe errors, it reports the error source to the operating system.</p>

<p>If a PSHED plug-in is registered to participate in error source discovery and it has implemented a <i>GetErrorSourceInfo</i> callback function, after the PSHED has updated the error source descriptor structure with the information that it has collected about the error source, the PSHED calls the PSHED plug-in's <i>GetErrorSourceInfo</i> callback function so that the PSHED plug-in can provide additional details about the error source. The <i>GetErrorSourceInfo</i> callback function updates the contents of the error source descriptor structure so that it accurately represents the error source as it is implemented by the hardware platform.</p>

<p>A PSHED plug-in that participates in error source discovery sets the <b>Callbacks.GetAllErrorSources </b>member and, optionally, the <b>Callbacks.GetErrorSourceInfo </b>member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-get-all-error-sources.md">GetAllErrorSources</a> and <i>GetErrorSourceInfo</i> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFADiscovery</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to obtain additional details about a particular error source. This occurs when a new error source is added to the system by a bus driver. For example, when the PCI driver discovers a PCI Express (PCIe) device that is capable of reporting PCIe errors, it reports the error source to the operating system.</p>

<p>If a PSHED plug-in is registered to participate in error source discovery and it has implemented a <i>GetErrorSourceInfo</i> callback function, after the PSHED has updated the error source descriptor structure with the information that it has collected about the error source, the PSHED calls the PSHED plug-in's <i>GetErrorSourceInfo</i> callback function so that the PSHED plug-in can provide additional details about the error source. The <i>GetErrorSourceInfo</i> callback function updates the contents of the error source descriptor structure so that it accurately represents the error source as it is implemented by the hardware platform.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-get-all-error-sources.md">GetAllErrorSources</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_GET_ERROR_SOURCE_INFO callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
