---
UID: NC.ntddk.PSHED_PI_INJECT_ERROR
title: PSHED_PI_INJECT_ERROR
author: windows-driver-content
description: A PSHED plug-in's InjectError callback function injects an error into the hardware platform.
old-location: whea\injecterror.htm
old-project: whea
ms.assetid: efd2658b-875e-4589-9ba0-42232e070b91
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
req.alt-api: InjectError
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

# PSHED_PI_INJECT_ERROR callback



## -description
<p>A PSHED plug-in's <i>InjectError </i>callback function injects an error into the hardware platform.</p>


## -prototype

````
PSHED_PI_INJECT_ERROR InjectError;

NTSTATUS InjectError(
  _Inout_opt_ PVOID     PluginContext,
  _In_        ULONGLONG ErrorType,
  _In_        ULONGLONG Parameter1,
  _In_        ULONGLONG Parameter2,
  _In_        ULONGLONG Parameter3,
  _In_        ULONGLONG Parameter4
)
{ ... }
````


## -parameters
<dl>

### -param PluginContext [in, out, optional]

<dd>
<p>A pointer to the context area that was specified in the <b>Context</b> member of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure when the PSHED plug-in called the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>
</dd>

### -param ErrorType [in]

<dd>
<p>The type of error to be injected into the hardware platform. Possible values are:</p>
<p></p>
<dl>

### -param INJECT_ERRTYPE_PROCESSOR_CORRECTABLE

<dd>
<p>A correctable processor error.</p>
</dd>

### -param INJECT_ERRTYPE_PROCESSOR_UNCORRECTABLENONFATAL

<dd>
<p>An uncorrectable nonfatal processor error.</p>
</dd>

### -param INJECT_ERRTYPE_PROCESSOR_UNCORRECTABLEFATAL

<dd>
<p>An uncorrectable fatal processor error.</p>
</dd>

### -param INJECT_ERRTYPE_MEMORY_CORRECTABLE

<dd>
<p>A correctable memory error.</p>
</dd>

### -param INJECT_ERRTYPE_MEMORY_UNCORRECTABLENONFATAL

<dd>
<p>An uncorrectable nonfatal memory error.</p>
</dd>

### -param INJECT_ERRTYPE_MEMORY_UNCORRECTABLEFATAL

<dd>
<p>An uncorrectable fatal memory error.</p>
</dd>

### -param INJECT_ERRTYPE_PCIEXPRESS_CORRECTABLE

<dd>
<p>A correctable PCI Express error.</p>
</dd>

### -param INJECT_ERRTYPE_PCIEXPRESS_UNCORRECTABLENONFATAL

<dd>
<p>An uncorrectable nonfatal PCI Express error.</p>
</dd>

### -param INJECT_ERRTYPE_PCIEXPRESS_UNCORRECTABLEFATAL

<dd>
<p>An uncorrectable fatal PCI Express error.</p>
</dd>

### -param INJECT_ERRTYPE_PLATFORM_CORRECTABLE

<dd>
<p>A correctable platform error.</p>
</dd>

### -param INJECT_ERRTYPE_PLATFORM_UNCORRECTABLENONFATAL

<dd>
<p>An uncorrectable nonfatal platform error.</p>
</dd>

### -param INJECT_ERRTYPE_PLATFORM_UNCORRECTABLEFATAL

<dd>
<p>An uncorrectable fatal platform error.</p>
</dd>
</dl>
</dd>

### -param Parameter1 [in]

<dd>
<p>A generic parameter that contains additional data that is passed by the WHEA management application that is injecting the error.</p>
</dd>

### -param Parameter2 [in]

<dd>
<p>A generic parameter that contains additional data that is passed by the WHEA management application that is injecting the error.</p>
</dd>

### -param Parameter3 [in]

<dd>
<p>A generic parameter that contains additional data that is passed by the WHEA management application that is injecting the error.</p>
</dd>

### -param Parameter4 [in]

<dd>
<p>A generic parameter that contains additional data that is passed by the WHEA management application that is injecting the error.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>InjectError</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The error was successfully injected into the hardware platform.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error injection sets the <b>Callbacks.GetInjectionCapabilities </b>and <b>Callbacks.InjectError </b>members of the <a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-get-injection-capabilities.md">GetInjectionCapabilities</a> and <i>InjectError</i> callback functions when the plug-in calls the <a href="..\ntddk\nf-ntddk-pshedregisterplugin.md">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorInjection</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>When a WHEA management application makes a request to inject a hardware error, the Windows kernel calls into the PSHED to inject the error into the hardware platform. If a PSHED plug-in is registered to participate in error injection, the PSHED calls the PSHED plug-in's <i>InjectError </i>callback function to perform the error injection operation.</p>

<p>The WHEA management application that is injecting the error can pass additional error-specific data to the PSHED plug-in's <i>InjectError </i>callback function by using parameters <i>Parameter1</i> through <i>Parameter4</i>. For example, on Itanium-based systems, some of the error injection operations require an accompanying address. In this situation, the WHEA management application can pass the address to the PSHED plug-in's <i>InjectError </i>callback function using one of these parameters.</p>

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
<a href="..\ntddk\nc-ntddk-pshed-pi-get-injection-capabilities.md">GetInjectionCapabilities</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-pshed-plugin-registration-packet.md">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_INJECT_ERROR callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
