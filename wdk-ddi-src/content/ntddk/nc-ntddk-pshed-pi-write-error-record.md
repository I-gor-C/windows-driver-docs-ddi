---
UID: NC.ntddk.PSHED_PI_WRITE_ERROR_RECORD
title: PSHED_PI_WRITE_ERROR_RECORD
author: windows-driver-content
description: A PSHED plug-in's WriteErrorRecord callback function writes an error record to the system's persistent data storage.
old-location: whea\writeerrorrecord.htm
old-project: whea
ms.assetid: 4800a0f9-29ee-4631-aee8-5a4924a08f55
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
req.alt-api: WriteErrorRecord
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

# PSHED_PI_WRITE_ERROR_RECORD callback



## -description
<p>A PSHED plug-in's <i>WriteErrorRecord </i>callback function writes an error record to the system's persistent data storage.</p>


## -prototype

````
PSHED_PI_WRITE_ERROR_RECORD WriteErrorRecord;

NTSTATUS WriteErrorRecord(
  _Inout_opt_ PVOID              PluginContext,
  _In_        ULONG              Flags,
  _In_        ULONG              RecordLength,
  _In_        PWHEA_ERROR_RECORD ErrorRecord
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
<p>A bit-wise OR'ed combination of flags that affect the write operation. A possible flag is:</p>
<p></p>
<dl>

### -param <a id="WHEA_WRITE_FLAG_DUMMY"></a><a id="whea_write_flag_dummy"></a>WHEA_WRITE_FLAG_DUMMY

<dd>
<p>The write operation is a dummy write operation. No data is to be written to the system's persistent data storage.</p>
</dd>
</dl>
</dd>

### -param <i>RecordLength</i> [in]

<dd>
<p>The size, in bytes, of the error record pointed to by the <i>ErrorRecord</i> parameter.</p>
</dd>

### -param <i>ErrorRecord</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a> structure that describes the error record that is being written to the system's persistent data storage.</p>
</dd>
</dl>

## -returns
<p>A PSHED plug-in's <i>WriteErrorRecord</i> callback function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The error record was successfully written to the system's persistent data storage.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A PSHED plug-in that participates in error record persistence sets the <b>Callbacks.WriteErrorRecord</b>, <b>Callbacks.ReadErrorRecord </b>and <b>Callbacks.ClearErrorRecord </b>members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>WriteErrorRecord</i>, <a href="..\ntddk\nc-ntddk-pshed-pi-read-error-record.md">ReadErrorRecord</a>, and <a href="..\ntddk\nc-ntddk-pshed-pi-clear-error-record.md">ClearErrorRecord</a> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorRecordPersistence</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to write an error record to the system's persistent data storage whenever a fatal or otherwise unrecoverable error condition exists so that the error record is preserved while the system is restarted. If a PSHED plug-in is registered to participate in error record persistence, the PSHED calls the PSHED plug-in's <i>WriteErrorRecord</i> callback function to perform the write operation. The mechanism that is used to write the error record to the system's persistent data storage is platform-specific.</p>

<p>The PSHED calls a PSHED plug-in's <i>WriteErrorRecord</i> callback function at IRQL &lt;= HIGH_LEVEL. The exact IRQL at which this callback function is called depends on the specific type of hardware error that occurred.</p>

<p>A PSHED plug-in that participates in error record persistence sets the <b>Callbacks.WriteErrorRecord</b>, <b>Callbacks.ReadErrorRecord </b>and <b>Callbacks.ClearErrorRecord </b>members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure to point to its <i>WriteErrorRecord</i>, <a href="..\ntddk\nc-ntddk-pshed-pi-read-error-record.md">ReadErrorRecord</a>, and <a href="..\ntddk\nc-ntddk-pshed-pi-clear-error-record.md">ClearErrorRecord</a> callback functions when the plug-in calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to register itself with the PSHED. The PSHED plug-in must also set the <b>PshedFAErrorRecordPersistence</b> flag in the <b>FunctionalAreaMask</b> member of the WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure.</p>

<p>The Windows kernel calls into the PSHED to write an error record to the system's persistent data storage whenever a fatal or otherwise unrecoverable error condition exists so that the error record is preserved while the system is restarted. If a PSHED plug-in is registered to participate in error record persistence, the PSHED calls the PSHED plug-in's <i>WriteErrorRecord</i> callback function to perform the write operation. The mechanism that is used to write the error record to the system's persistent data storage is platform-specific.</p>

<p>The PSHED calls a PSHED plug-in's <i>WriteErrorRecord</i> callback function at IRQL &lt;= HIGH_LEVEL. The exact IRQL at which this callback function is called depends on the specific type of hardware error that occurred.</p>

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
<a href="..\ntddk\nc-ntddk-pshed-pi-clear-error-record.md">ClearErrorRecord</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-read-error-record.md">ReadErrorRecord</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PSHED_PI_WRITE_ERROR_RECORD callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
