---
UID: NS.ntddk._WHEA_GENERIC_ERROR_BLOCKSTATUS
title: WHEA_GENERIC_ERROR_BLOCKSTATUS
author: windows-driver-content
description: The WHEA_GENERIC_ERROR_BLOCKSTATUS union indicates what kind of error data is reported in a generic error status block.
old-location: whea\whea_generic_error_blockstatus.htm
ms.assetid: 38c8422d-7307-4acd-81f0-931d2e128cb9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_GENERIC_ERROR_BLOCKSTATUS
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
ms.keywords: WHEA_GENERIC_ERROR_BLOCKSTATUS, WHEA_GENERIC_ERROR_BLOCKSTATUS, *PWHEA_GENERIC_ERROR_BLOCKSTATUS
req.iface: 
---

# WHEA_GENERIC_ERROR_BLOCKSTATUS structure



## -description
<p>The WHEA_GENERIC_ERROR_BLOCKSTATUS union indicates what kind of error data is reported in a generic error status block.</p>


## -syntax

````
typedef union _WHEA_GENERIC_ERROR_BLOCKSTATUS {
  struct {
    ULONG UncorrectableError  :1;
    ULONG CorrectableError  :1;
    ULONG MultipleUncorrectableErrors  :1;
    ULONG MultipleCorrectableErrors  :1;
    ULONG ErrorDataEntryCount  :10;
    ULONG Reserved  :18;
  };
  ULONG  AsULONG;
} WHEA_GENERIC_ERROR_BLOCKSTATUS, *PWHEA_GENERIC_ERROR_BLOCKSTATUS;
````


## -struct-fields
<dl>

### -field <b>UncorrectableError</b>

<dd>
<p>The generic error status block is reporting uncorrectable error data.</p>
</dd>

### -field <b>CorrectableError</b>

<dd>
<p>The generic error status block is reporting correctable error data.</p>
</dd>

### -field <b>MultipleUncorrectableErrors</b>

<dd>
<p>The generic error status block is reporting multiple uncorrectable errors.</p>
</dd>

### -field <b>MultipleCorrectableErrors</b>

<dd>
<p>The generic error status block is reporting multiple correctable errors.</p>
</dd>

### -field <b>ErrorDataEntryCount</b>

<dd>
<p>The number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560529">WHEA_GENERIC_ERROR_DATA_ENTRY</a> structures that are contained in the generic error status block.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>AsULONG</b>

<dd>
<p>A ULONG representation of the contents of the WHEA_GENERIC_ERROR_BLOCKSTATUS union.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_GENERIC_ERROR_BLOCKSTATUS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560524">WHEA_GENERIC_ERROR</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560524">WHEA_GENERIC_ERROR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560529">WHEA_GENERIC_ERROR_DATA_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_GENERIC_ERROR_BLOCKSTATUS union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
