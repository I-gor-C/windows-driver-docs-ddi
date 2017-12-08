---
UID: NE.ntddk._WHEA_ERROR_SEVERITY
title: WHEA_ERROR_SEVERITY
author: windows-driver-content
description: The WHEA_ERROR_SEVERITY enumeration defines the possible severity levels of a hardware error condition.
old-location: whea\whea_error_severity.htm
old-project: whea
ms.assetid: 3b056910-dc33-4608-bb7d-a3f13bc546ca
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_ERROR_SEVERITY
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
req.irql: 
req.iface: 
---

# WHEA_ERROR_SEVERITY enumeration



## -description
<p>The WHEA_ERROR_SEVERITY enumeration defines the possible severity levels of a hardware error condition.</p>


## -syntax

````
typedef enum _WHEA_ERROR_SEVERITY { 
  WheaErrSevRecoverable    = 0,
  WheaErrSevFatal          = 1,
  WheaErrSevCorrected      = 2,
  WheaErrSevInformational  = 3
} WHEA_ERROR_SEVERITY, *PWHEA_ERROR_SEVERITY;
````


## -enum-fields
<dl>

### -field WheaErrSevRecoverable

<dd>
<p>The error has not been corrected but might be recoverable.</p>
</dd>

### -field WheaErrSevFatal

<dd>
<p>The error has not been corrected and is fatal.</p>
</dd>

### -field WheaErrSevCorrected

<dd>
<p>The error has been corrected by the hardware or firmware.</p>
</dd>

### -field WheaErrSevInformational

<dd>
<p>An error has not occurred.</p>
<div class="alert"><b>Note</b>  In versions of the WDK that were released prior to Windows 7, this value was named <b>WheaErrSevNone</b>.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The <a href="whea.whea_error_packet">WHEA_ERROR_PACKET</a>, <a href="..\ntddk\ns-ntddk--whea-error-record-header.md">WHEA_ERROR_RECORD_HEADER</a>, <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>, and <a href="..\ntddk\ns-ntddk--whea-generic-error.md">WHEA_GENERIC_ERROR</a> structures each contain a member of type WHEA_ERROR_SEVERITY that specifies the severity of the error that is described by the structure.</p>

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
<a href="whea.whea_error_packet">WHEA_ERROR_PACKET</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-error-record-header.md">WHEA_ERROR_RECORD_HEADER</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-generic-error.md">WHEA_GENERIC_ERROR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_SEVERITY enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
