---
UID: NS.ntddk._WHEA_GENERIC_ERROR
title: WHEA_GENERIC_ERROR
author: windows-driver-content
description: The WHEA_GENERIC_ERROR structure describes error status data for a generic error source.
old-location: whea\whea_generic_error.htm
old-project: whea
ms.assetid: 7d624645-0199-4376-b84a-83d7da3ba981
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_GENERIC_ERROR, WHEA_GENERIC_ERROR, *PWHEA_GENERIC_ERROR
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
req.alt-api: WHEA_GENERIC_ERROR
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

# WHEA_GENERIC_ERROR structure



## -description
<p>The WHEA_GENERIC_ERROR structure describes error status data for a generic error source.</p>


## -syntax

````
typedef struct _WHEA_GENERIC_ERROR {
  WHEA_GENERIC_ERROR_BLOCKSTATUS BlockStatus;
  ULONG                          RawDataOffset;
  ULONG                          RawDataLength;
  ULONG                          DataLength;
  WHEA_ERROR_SEVERITY            ErrorSeverity;
  UCHAR                          Data[1];
} WHEA_GENERIC_ERROR, *PWHEA_GENERIC_ERROR;
````


## -struct-fields
<dl>

### -field <b>BlockStatus</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-generic-error-blockstatus.md">WHEA_GENERIC_ERROR_BLOCKSTATUS</a> union that indicates what kind of error data is reported in the generic error status block.</p>
</dd>

### -field <b>RawDataOffset</b>

<dd>
<p>The offset, in bytes, from the beginning of the WHEA_GENERIC_ERROR structure to the beginning of the raw error data.</p>
</dd>

### -field <b>RawDataLength</b>

<dd>
<p>The length, in bytes, of the raw error data that is located at the offset specified in the <b>RawDataOffset</b> member.</p>
</dd>

### -field <b>DataLength</b>

<dd>
<p>The size, in bytes, of the error data contained in the <b>Data</b> member.</p>
</dd>

### -field <b>ErrorSeverity</b>

<dd>
<p>A <a href="..\ntddk\ne-ntddk--whea-error-severity.md">WHEA_ERROR_SEVERITY</a>-typed value that indicates the severity of the error condition.</p>
</dd>

### -field <b>Data</b>

<dd>
<p>A variable-sized buffer that contains the error data from the generic error source. This buffer contains the generic error status block followed by the raw error data.</p>
</dd>
</dl>

## -remarks
<p>A generic error source is described by a <a href="..\ntddk\ns-ntddk--whea-generic-error-descriptor.md">WHEA_GENERIC_ERROR_DESCRIPTOR</a> structure. The <b>ErrStatusAddress</b> member of the WHEA_GENERIC_ERROR_DESCRIPTOR structure points to a register that contains the physical address of a WHEA_GENERIC_ERROR structure in firmware reserved memory. This WHEA_GENERIC_ERROR structure contains the error status data for the generic error source.</p>

<p>A WHEA_GENERIC_ERROR structure is included in the <b>RawData</b> member of a <a href="whea.whea_error_packet">WHEA_ERROR_PACKET</a> structure whenever the <b>RawDataFormat </b>member of the WHEA_ERROR_PACKET structure contains <b>WheaRawDataFormatGeneric</b>.</p>

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
<a href="..\ntddk\ne-ntddk--whea-error-severity.md">WHEA_ERROR_SEVERITY</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-generic-error-blockstatus.md">WHEA_GENERIC_ERROR_BLOCKSTATUS</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-generic-error-descriptor.md">WHEA_GENERIC_ERROR_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_GENERIC_ERROR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
