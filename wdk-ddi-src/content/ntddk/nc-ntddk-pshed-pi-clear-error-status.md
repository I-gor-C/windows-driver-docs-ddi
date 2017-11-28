---
UID: NC.ntddk.PSHED_PI_CLEAR_ERROR_STATUS
title: PSHED_PI_CLEAR_ERROR_STATUS
author: windows-driver-content
description: A PSHED plug-in's ClearErrorStatus callback function clears any platform-specific error status registers for a corrected hardware error condition.
old-location: whea\clearerrorstatus.htm
old-project: whea
ms.assetid: 8b29edf3-be7f-4a8d-af96-2b1e985ba061
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
req.alt-api: ClearErrorStatus
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
req.irql: <= HIGH_LEVEL (See Remarks section)
req.iface: 
---

# PSHED_PI_CLEAR_ERROR_STATUS callback



## -description
<p>A PSHED plug-in's <i>ClearErrorStatus</i> callback function clears any platform-specific error status registers for a corrected hardware error condition.</p>


## -prototype

````
PSHED_PI_CLEAR_ERROR_STATUS ClearErrorStatus;

NTSTATUS ClearErrorStatus(
  _Inout_opt_ PVOID                         PluginContext,
  _In_        PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource,
  _In_        ULONG                         BufferLength,
  _In_        PWHEA_ERROR_RECORD            ErrorRecord
)
{ ... }
````


## -parameters
<dl>

### -param <i>PluginContext</i> [in, out, optional]

<dd>
<p>A pointer to the context area that was specified in the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure when the PSHED plug-in called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>
</dd>

### -param <i>ErrorSource</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that describes the error source that reported the hardware error.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by the <i>ErrorRecord</i> parameter.</p>
</dd>

### -param <i>ErrorRecord</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a> structure that describes an error record. The error record describes the corrected hardware error condition for which the platform-specific error status registers are being cleared.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>ClearErrorStatus</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The platform-specific error status registers for the corrected hardware error condition were successfully cleared.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The PSHED plug-in does not support the specified error source.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error information retrieval sets the <b>Callbacks.RetrieveErrorInfo</b>, <b>Callbacks.FinalizeErrorRecord</b>, and <b>Callbacks.ClearErrorStatus</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-retrieve-error-info.md">RetrieveErrorInfo</a>, <a href="..\ntddk\nc-ntddk-pshed-pi-finalize-error-record.md">FinalizeErrorRecord</a>, and <i>ClearErrorStatus</i> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorInfoRetrieval</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>For corrected hardware error conditions, the Windows kernel calls into the PSHED to clear the error source's error status registers as the final step of processing the error. If a PSHED plug-in is registered to participate in error information retrieval, the PSHED calls the PSHED plug-in's <i>ClearErrorStatus</i> callback function so that the PSHED plug-in can clear any additional platform-specific error status registers.</p>

<p>The PSHED calls a PSHED plug-in's <i>ClearErrorStatus</i> callback function at IRQL &lt;= HIGH_LEVEL. The exact IRQL at which this callback function is called depends on the specific type of hardware error that occurred.</p>

<p>A PSHED plug-in that participates in error information retrieval sets the <b>Callbacks.RetrieveErrorInfo</b>, <b>Callbacks.FinalizeErrorRecord</b>, and <b>Callbacks.ClearErrorStatus</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-retrieve-error-info.md">RetrieveErrorInfo</a>, <a href="..\ntddk\nc-ntddk-pshed-pi-finalize-error-record.md">FinalizeErrorRecord</a>, and <i>ClearErrorStatus</i> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorInfoRetrieval</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>For corrected hardware error conditions, the Windows kernel calls into the PSHED to clear the error source's error status registers as the final step of processing the error. If a PSHED plug-in is registered to participate in error information retrieval, the PSHED calls the PSHED plug-in's <i>ClearErrorStatus</i> callback function so that the PSHED plug-in can clear any additional platform-specific error status registers.</p>

<p>The PSHED calls a PSHED plug-in's <i>ClearErrorStatus</i> callback function at IRQL &lt;= HIGH_LEVEL. The exact IRQL at which this callback function is called depends on the specific type of hardware error that occurred.</p>

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
<p>&lt;= HIGH_LEVEL (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-finalize-error-record.md">FinalizeErrorRecord</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-retrieve-error-info.md">RetrieveErrorInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_CLEAR_ERROR_STATUS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
