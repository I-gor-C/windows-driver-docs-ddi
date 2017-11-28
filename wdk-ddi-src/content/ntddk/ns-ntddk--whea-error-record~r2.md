---
UID: NS.ntddk._WHEA_ERROR_RECORD~r2
title: WHEA_ERROR_RECORD
author: windows-driver-content
description: The WHEA_ERROR_RECORD structure describes an error record that contains error information about a hardware error condition that occurred.
old-location: whea\whea_error_record.htm
old-project: whea
ms.assetid: 29ed998c-d833-496f-a728-0eef2cd49ae6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_ERROR_RECORD, WHEA_ERROR_RECORD, *PWHEA_ERROR_RECORD
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
req.alt-api: WHEA_ERROR_RECORD
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

# WHEA_ERROR_RECORD structure



## -description
<p>The WHEA_ERROR_RECORD structure describes an <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a> that contains error information about a hardware error condition that occurred.</p>


## -syntax

````
typedef struct _WHEA_ERROR_RECORD {
  WHEA_ERROR_RECORD_HEADER             Header;
  WHEA_ERROR_RECORD_SECTION_DESCRIPTOR SectionDescriptor[ANYSIZE_ARRAY];
} WHEA_ERROR_RECORD, *PWHEA_ERROR_RECORD;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a> structure that describes general information about the hardware error condition.</p>
</dd>

### -field <b>SectionDescriptor</b>

<dd>
<p>A variable sized array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structures that describe each of the sections of error information that are contained in the error record. The number of structures in the array is specified by the <b>Header.SectionCount</b> member of the WHEA_ERROR_RECORD structure.</p>
</dd>
</dl>

## -remarks
<p>When a hardware error occurs, WHEA creates an <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a> to store the error information associated with the hardware error condition. Each error record is described by a WHEA_ERROR_RECORD structure. The Windows kernel includes the error record with the Event Tracing for Windows (ETW) hardware error event that it raises in response to the error so that the error record is saved in the system event log.</p>

<p>The format of the error records that are used by WHEA are based on the <i>Common Platform Error Record</i> as described in Appendix N of version 2.2 of the <a href="http://go.microsoft.com/fwlink/p/?linkid=69484">Unified Extensible Firmware Interface (UEFI) Specification</a>.</p>

<p>A user-mode application can retrieve the error record from the hardware error event for analysis. For more information about how to develop an application to retrieve error records from hardware error events, see <a href="NULL">WHEA Hardware Error Event Processing Applications</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_RECORD structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
