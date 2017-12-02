---
UID: NC.ntddk.PSHED_PI_GET_ALL_ERROR_SOURCES
title: PSHED_PI_GET_ALL_ERROR_SOURCES
author: windows-driver-content
description: A PSHED plug-in's GetAllErrorSources callback function returns a list of error source descriptor structures that represents all of the error sources that are implemented by the hardware platform.
old-location: whea\getallerrorsources.htm
old-project: whea
ms.assetid: e9c97f88-aa13-4a3e-9236-c09703d17e4b
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
req.alt-api: GetAllErrorSources
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

# PSHED_PI_GET_ALL_ERROR_SOURCES callback



## -description
<p>A PSHED plug-in's <i>GetAllErrorSources</i> callback function returns a list of error source descriptor structures that represents all of the error sources that are implemented by the hardware platform.</p>


## -prototype

````
PSHED_PI_GET_ALL_ERROR_SOURCES GetAllErrorSources;

NTSTATUS GetAllErrorSources(
  _Inout_opt_ PVOID                         PluginContext,
  _Inout_     PULONG                        Count,
  _Inout_     PWHEA_ERROR_SOURCE_DESCRIPTOR *ErrorSources,
  _Inout_     PULONG                        Length
)
{ ... }
````


## -parameters
<dl>

### -param PluginContext [in, out, optional]

<dd>
<p>A pointer to the context area that was specified in the <b>Context</b> member of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure when the PSHED plug-in called the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>
</dd>

### -param Count [in, out]

<dd>
<p>A pointer to a ULONG-typed variable. When the <i>GetAllErrorSources</i> callback function is called, this variable contains the number of error source descriptor structures that are contained in the buffer pointed to by the <i>ErrorSources</i> parameter as provided by the PSHED. If the <i>GetAllErrorSources</i> callback function changes the number of error source descriptor structures that are in the buffer, it must set this variable to the new number of error source descriptor structures before it returns.</p>
</dd>

### -param ErrorSources [in, out]

<dd>
<p>A pointer to a buffer that receives an array of <a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structures that represents all of the error sources that are implemented by the hardware platform. When the <i>GetAllErrorSources</i> callback function is called, this buffer contains an initial list of error source descriptor structures that is provided by the PSHED. The PSHED plug-in can make changes to the list so that it accurately represents all of the error sources that are implemented by the hardware platform.</p>
</dd>

### -param Length [in, out]

<dd>
<p>A pointer to a ULONG-typed variable that contains the size, in bytes, of the buffer pointed to by the <i>ErrorSources</i> parameter. If the size is too small to contain the modified list of error source descriptor structures, the <i>GetAllErrorSources</i> callback function sets this variable to the buffer size that is required to contain the list and returns STATUS_BUFFER_TOO_SMALL.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>GetAllErrorSources</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The modified list of error source descriptor structures was successfully returned in the buffer pointed to by the <i>ErrorSources</i> parameter.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The size of the buffer pointed to by the <i>ErrorSources</i> parameter is too small to contain the list of error source descriptor structures.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error source discovery sets the <b>Callbacks.GetAllErrorSources </b>member of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>GetAllErrorSources</i> callback function when the plug-in calls the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFADiscovery</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>When the operating system starts, the Windows kernel calls into the PSHED to retrieve the list of error source descriptor structures that represents all of the error sources that are implemented by the hardware platform. The PSHED creates an initial list of error source descriptor structures. If a PSHED plug-in is registered to participate in error source discovery, the PSHED calls the PSHED plug-in's <i>GetAllErrorSources</i> callback function. The PSHED plug-in can make any combination of the following changes to the list of error source descriptor structures so that it accurately represents all of the error sources that are implemented by the hardware platform.</p>

<p>Modify the contents of one or more of the error source descriptor structures.</p>

<p>Remove one or more of the error source descriptor structures from the list.</p>

<p>Add one or more new error source descriptor structures to the list.</p>

<p>If the PSHED plug-in must add one or more new error source descriptor structures to the list and the size of the buffer is too small to include the additional structures, the PSHED plug-in's <i>GetAllErrorSources</i> callback function must set the variable pointed to by the <i>Length </i>parameter to the buffer size that is required to contain the list with the additional structures and return STATUS_BUFFER_TOO_SMALL. In this situation, the PSHED will allocate a larger buffer, copy the list of error source descriptor structures into the new buffer, and call the PSHED plug-in's <i>GetAllErrorSources</i> callback function a second time.</p>

<p>A PSHED plug-in that participates in error source discovery can also implement an optional <a href="..\ntddk\nc-ntddk-pshed-pi-get-error-source-info.md">GetErrorSourceInfo</a> callback function. In this situation, the PSHED plug-in also sets the <b>Callbacks.GetErrorSourceInfo </b>member of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>GetErrorSourceInfo</i> callback function when it calls the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>

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
<a href="..\ntddk\nc-ntddk-pshed-pi-get-error-source-info.md">GetErrorSourceInfo</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_GET_ALL_ERROR_SOURCES callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
