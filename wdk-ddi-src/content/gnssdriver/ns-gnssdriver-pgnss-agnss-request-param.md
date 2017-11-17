---
UID: NS.gnssdriver.PGNSS_AGNSS_REQUEST_PARAM
title: PGNSS_AGNSS_REQUEST_PARAM
author: windows-driver-content
description: This structure defines AGNSS request parameters.
old-location: sensors\gnss_agnss_request_param.htm
ms.assetid: 67A1DAEF-13D3-4D47-B10C-0CA30C8EB22F
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
req.alt-api: GNSS_AGNSS_REQUEST_PARAM
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
ms.keywords: PGNSS_AGNSS_REQUEST_PARAM, GNSS_AGNSS_REQUEST_PARAM, *PGNSS_AGNSS_REQUEST_PARAM
req.iface: 
---

# PGNSS_AGNSS_REQUEST_PARAM structure



## -description
<p>This structure defines AGNSS request parameters.</p>


## -syntax

````
typedef struct {
  ULONG                   Size;
  ULONG                   Version;
  GNSS_AGNSS_REQUEST_TYPE RequestType;
  ULONG                   BlobFormat;
} GNSS_AGNSS_REQUEST_PARAM, *PGNSS_AGNSS_REQUEST_PARAM;
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

### -field <b>RequestType</b>

<dd>
<p>Specifies the type of the request (for example, time injection, blob injection).</p>
</dd>

### -field <b>BlobFormat</b>

<dd>
<p>If the RequestType is GNSS_AGNSS_BlobInjection, this contains the required  blob format.</p>
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