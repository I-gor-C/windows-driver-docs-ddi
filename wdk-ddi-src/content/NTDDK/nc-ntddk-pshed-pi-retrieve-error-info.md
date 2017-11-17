---
UID: NC.ntddk.PSHED_PI_RETRIEVE_ERROR_INFO
title: PSHED_PI_RETRIEVE_ERROR_INFO
author: windows-driver-content
description: A PSHED plug-in's RetrieveErrorInfo callback function retrieves platform-specific error information about a hardware error that has occurred.
old-location: whea\retrieveerrorinfo.htm
ms.assetid: 4d299057-a1cc-4b53-8ab4-031672181e74
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RetrieveErrorInfo
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
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
req.iface: 
---

# PSHED_PI_RETRIEVE_ERROR_INFO callback



## -description
<p>A PSHED plug-in's <i>RetrieveErrorInfo</i> callback function retrieves platform-specific error information about a hardware error that has occurred.</p>


## -prototype

````
PSHED_PI_RETRIEVE_ERROR_INFO RetrieveErrorInfo;

NTSTATUS RetrieveErrorInfo(
  _Inout_opt_ PVOID                         PluginContext,
  _In_        PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource,
  _In_        ULONGLONG                     BufferLength,
  _Inout_     PWHEA_ERROR_PACKET            Packet
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
<p>The size, in bytes, of the buffer pointed to by the <i>Packet</i> parameter.</p>
</dd>

### -param <i>Packet</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure that describes the hardware error packet for the hardware error.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>RetrieveErrorInfo</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The hardware error packet was successfully updated with any platform-specific error information.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The size of the buffer pointed to by the <i>Packet </i>parameter as specified by the <i>BufferLength </i>parameter is too small to contain the hardware error packet if it is updated with the platform-specific error information.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The PSHED plug-in does not support the specified error source.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error information retrieval sets the <b>Callbacks.RetrieveErrorInfo</b>, <b>Callbacks.FinalizeErrorRecord</b>, and <b>Callbacks.ClearErrorStatus</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>RetrieveErrorInfo</i>, <a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a>, and <a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorInfoRetrieval</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>Each low-level hardware error handler (LLHEH) calls into the PSHED to retrieve any platform-specific error information about a hardware error that has occurred. If a PSHED plug-in is registered to participate in error information retrieval, the PSHED calls the PSHED plug-in's <i>RetrieveErrorInfo</i> callback function so that it can update the hardware error packet with any platform-specific error information. The PSHED plug-in can modify the existing contents of the hardware error packet as well as add supplementary information to the hardware error packet. Supplementary information is added to a hardware error packet beginning at the offset specified by the <b>RawDataOffset</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.</p>

<p>A PSHED plug-in must ensure that it does not add supplementary information beyond the end of the hardware error packet. The amount of memory that an LLHEH allocates for a buffer to contain a particular hardware error packet is calculated from the <b>MaxRawDataLength</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that describes the error source. If a PSHED plug-in requires additional buffer space to contain the supplementary information, it must participate in error source discovery and increase the value in the <b>MaxRawDataLength</b> member of the <b>WHEA_ERROR_SOURCE_DESCRIPTOR</b> structure for each error source as appropriate to account for any supplemental information.</p>

<p>For most error sources, the PSHED plug-in's <i>RetrieveErrorInfo</i> callback function is called at a high IRQL. In such a situation, the PSHED plug-in's <i>RetrieveErrorInfo</i> callback function must only perform operations and make calls to other functions that are permitted at a high IRQL.</p>

<p>An important task of a PSHED plug-in's <i>RetrieveErrorInfo</i> callback function is to ensure that the severity of the error condition as specified by the <b>ErrorSeverity</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> is appropriate. For example, if the severity level of the error condition is reported as <b>WheaErrSevFatal </b>by the LLHEH but the PSHED plug-in supports a recovery mechanism for the particular error condition that was reported, the PSHED plug-in can change the severity level to <b>WheaErrSevRecoverable </b>so that the operating system will attempt recovery from the error. Similarly, if the severity level of the error condition is reported as <b>WheaErrSevRecoverable </b>by the LLHEH but the PSHED plug-in recognizes that attempting recovery of the particular error condition that was reported would only cause further problems, the PSHED plug-in can change the severity level to <b>WheaErrSevFatal </b>so that the operating system will not attempt recovery from the error.</p>

<p>The PSHED calls a PSHED plug-in's <i>RetrieveErrorInfo</i> callback function at IRQL &lt;= HIGH_LEVEL. The exact IRQL at which this callback function is called depends on the specific type of hardware error that occurred.</p>

<p>A PSHED plug-in that participates in error information retrieval sets the <b>Callbacks.RetrieveErrorInfo</b>, <b>Callbacks.FinalizeErrorRecord</b>, and <b>Callbacks.ClearErrorStatus</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>RetrieveErrorInfo</i>, <a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a>, and <a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorInfoRetrieval</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>Each low-level hardware error handler (LLHEH) calls into the PSHED to retrieve any platform-specific error information about a hardware error that has occurred. If a PSHED plug-in is registered to participate in error information retrieval, the PSHED calls the PSHED plug-in's <i>RetrieveErrorInfo</i> callback function so that it can update the hardware error packet with any platform-specific error information. The PSHED plug-in can modify the existing contents of the hardware error packet as well as add supplementary information to the hardware error packet. Supplementary information is added to a hardware error packet beginning at the offset specified by the <b>RawDataOffset</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.</p>

<p>A PSHED plug-in must ensure that it does not add supplementary information beyond the end of the hardware error packet. The amount of memory that an LLHEH allocates for a buffer to contain a particular hardware error packet is calculated from the <b>MaxRawDataLength</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that describes the error source. If a PSHED plug-in requires additional buffer space to contain the supplementary information, it must participate in error source discovery and increase the value in the <b>MaxRawDataLength</b> member of the <b>WHEA_ERROR_SOURCE_DESCRIPTOR</b> structure for each error source as appropriate to account for any supplemental information.</p>

<p>For most error sources, the PSHED plug-in's <i>RetrieveErrorInfo</i> callback function is called at a high IRQL. In such a situation, the PSHED plug-in's <i>RetrieveErrorInfo</i> callback function must only perform operations and make calls to other functions that are permitted at a high IRQL.</p>

<p>An important task of a PSHED plug-in's <i>RetrieveErrorInfo</i> callback function is to ensure that the severity of the error condition as specified by the <b>ErrorSeverity</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> is appropriate. For example, if the severity level of the error condition is reported as <b>WheaErrSevFatal </b>by the LLHEH but the PSHED plug-in supports a recovery mechanism for the particular error condition that was reported, the PSHED plug-in can change the severity level to <b>WheaErrSevRecoverable </b>so that the operating system will attempt recovery from the error. Similarly, if the severity level of the error condition is reported as <b>WheaErrSevRecoverable </b>by the LLHEH but the PSHED plug-in recognizes that attempting recovery of the particular error condition that was reported would only cause further problems, the PSHED plug-in can change the severity level to <b>WheaErrSevFatal </b>so that the operating system will not attempt recovery from the error.</p>

<p>The PSHED calls a PSHED plug-in's <i>RetrieveErrorInfo</i> callback function at IRQL &lt;= HIGH_LEVEL. The exact IRQL at which this callback function is called depends on the specific type of hardware error that occurred.</p>

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
<a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_RETRIEVE_ERROR_INFO callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
