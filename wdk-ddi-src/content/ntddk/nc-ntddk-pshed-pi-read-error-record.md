---
UID: NC.ntddk.PSHED_PI_READ_ERROR_RECORD
title: PSHED_PI_READ_ERROR_RECORD
author: windows-driver-content
description: A PSHED plug-in's ReadErrorRecord callback function reads an error record from the system's persistent data storage.
old-location: whea\readerrorrecord.htm
old-project: whea
ms.assetid: 2fcbdfe3-bcce-4e5b-a16b-501612975e82
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
req.alt-api: ReadErrorRecord
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

# PSHED_PI_READ_ERROR_RECORD callback



## -description
<p>A PSHED plug-in's <i>ReadErrorRecord </i>callback function reads an error record from the system's persistent data storage.</p>


## -prototype

````
PSHED_PI_READ_ERROR_RECORD ReadErrorRecord;

NTSTATUS ReadErrorRecord(
  _Inout_opt_ PVOID              PluginContext,
  _In_        ULONG              Flags,
  _In_        ULONGLONG          ErrorRecordId,
  _Out_       PULONGLONG         NextErrorRecordId,
  _Inout_     PULONG             RecordLength,
  _Out_       PWHEA_ERROR_RECORD ErrorRecord
)
{ ... }
````


## -parameters
<dl>

### -param <i>PluginContext</i> [in, out, optional]

<dd>
<p>A pointer to the context area that was specified in the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure when the PSHED plug-in called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bit-wise OR'ed combination of flags that affect the read operation. No flags are currently defined.</p>
</dd>

### -param <i>ErrorRecordId</i> [in]

<dd>
<p>The identifier of the error record to be read from the system's persistent data storage. If there is not an error record stored in the system's persistent data storage that matches this identifier, the <i>ReadErrorRecord</i> callback function must return STATUS_OBJECT_NOT_FOUND.</p>
</dd>

### -param <i>NextErrorRecordId</i> [out]

<dd>
<p>A pointer to a ULONGLONG-typed variable that receives the identifier of the next error record that is stored in the system's persistent data storage. If there are no other error records stored in the system's persistent data storage, the identifier for the error record that is currently being read should be returned in this parameter.</p>
</dd>

### -param <i>RecordLength</i> [in, out]

<dd>
<p>A pointer to a ULONG-typed variable that contains the size, in bytes, of the buffer pointed to by the <i>ErrorRecord</i> parameter. If the size of the buffer is large enough to contain the error record that is being read, the <i>ReadErrorRecord</i> callback function sets this variable to the size, in bytes, of the error record that is returned in the buffer. However, if the size of the buffer is too small to contain the error record that is being read, the <i>ReadErrorRecord</i> callback function sets this variable to the size, in bytes, that is required to contain the error record. In this situation the <i>ReadErrorRecord</i> callback function must return STATUS_BUFFER_TOO_SMALL.</p>
</dd>

### -param <i>ErrorRecord</i> [out]

<dd>
<p>A pointer to a buffer that receives the error record that is read from the system's persistent data storage.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>ReadErrorRecord</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The error record was successfully read from the system's persistent data storage.</p><dl>
<dt><b>STATUS_OBJECT_NOT_FOUND</b></dt>
</dl><p>There is no error record in the system's persistent data storage that matches the identifier specified in the <i>ErrorRecordId</i> parameter.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The size of the buffer is too small to contain the error record that is being read.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error record persistence sets the <b>Callbacks.WriteErrorRecord</b>, <b>Callbacks.ReadErrorRecord </b>and <b>Callbacks.ClearErrorRecord </b>members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-write-error-record.md">WriteErrorRecord</a>, <i>ReadErrorRecord,</i> and <a href="..\ntddk\nc-ntddk-pshed-pi-clear-error-record.md">ClearErrorRecord</a> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorRecordPersistence</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to read an error record from the system's persistent data storage after the system is restarted following a fatal or otherwise unrecoverable error condition. If a PSHED plug-in is registered to participate in error record persistence, the PSHED calls the PSHED plug-in's <i>ReadErrorRecord</i> callback function to perform the read operation. The mechanism that is used to read the error record from the system's persistent data storage is platform-specific.</p>

<p>A PSHED plug-in that participates in error record persistence sets the <b>Callbacks.WriteErrorRecord</b>, <b>Callbacks.ReadErrorRecord </b>and <b>Callbacks.ClearErrorRecord </b>members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <a href="..\ntddk\nc-ntddk-pshed-pi-write-error-record.md">WriteErrorRecord</a>, <i>ReadErrorRecord,</i> and <a href="..\ntddk\nc-ntddk-pshed-pi-clear-error-record.md">ClearErrorRecord</a> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorRecordPersistence</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to read an error record from the system's persistent data storage after the system is restarted following a fatal or otherwise unrecoverable error condition. If a PSHED plug-in is registered to participate in error record persistence, the PSHED calls the PSHED plug-in's <i>ReadErrorRecord</i> callback function to perform the read operation. The mechanism that is used to read the error record from the system's persistent data storage is platform-specific.</p>

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
<a href="..\ntddk\nc-ntddk-pshed-pi-clear-error-record.md">ClearErrorRecord</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-write-error-record.md">WriteErrorRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_READ_ERROR_RECORD callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
