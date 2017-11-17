---
UID: NS.gnssdriver.PGNSS_ERRORINFO
title: PGNSS_ERRORINFO
author: windows-driver-content
description: This structure contains error information.
old-location: sensors\gnss_errorinfo.htm
ms.assetid: 754CD1DD-88E6-4E02-8E24-1939222FE326
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_ERRORINFO
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: PGNSS_ERRORINFO, GNSS_ERRORINFO, *PGNSS_ERRORINFO
req.iface: 
---

# PGNSS_ERRORINFO structure



## -description
<p>This structure contains error information.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  ULONG ErrorCode;
  BOOL  IsRecoverable;
  WCHAR ErrorDescription[256];
  BYTE  Unused[512];
} GNSS_ERRORINFO, *PGNSS_ERRORINFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>ErrorCode</b>

<dd>
<p>Win32 Error Code associated with the event.</p>
<p>The IHV can pick the error that is most similar to what needs to be reported (for example, E_OUTOFMEMORY). The IHV can also use FACILITY_ITF to create custom errors. For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=525284">Codes in FACILITY_ITF</a>.
</p>
</dd>

### -field <b>IsRecoverable</b>

<dd>
<p>If FALSE, the GNSS adapter needs to reset it’s state with the GNSS driver.</p>
</dd>

### -field <b>ErrorDescription[256]</b>

<dd>
<p>Clear-text description of the error (not-localized) that is used for diagnostic purpose only.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>