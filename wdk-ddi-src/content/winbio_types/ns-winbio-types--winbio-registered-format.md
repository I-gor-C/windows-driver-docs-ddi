---
UID: NS.winbio_types._WINBIO_REGISTERED_FORMAT
title: WINBIO_REGISTERED_FORMAT
author: windows-driver-content
description: The WINBIO_REGISTERED_FORMAT structure specifies a biometric data format.
old-location: biometric\winbio_registered_format.htm
ms.assetid: 70591143-f429-4a6e-8f2a-cc1082f40f6e
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: biometric
req.header: winbio_types.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_REGISTERED_FORMAT
req.alt-loc: winbio_types.h
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
ms.keywords: WINBIO_REGISTERED_FORMAT, WINBIO_REGISTERED_FORMAT, *PWINBIO_REGISTERED_FORMAT
req.iface: 
req.product: Windows 10 or later.
---

# WINBIO_REGISTERED_FORMAT structure



## -description
<p>The WINBIO_REGISTERED_FORMAT structure specifies a biometric data format.</p>


## -syntax

````
typedef struct _WINBIO_REGISTERED_FORMAT {
  USHORT Owner;
  USHORT Type;
} WINBIO_REGISTERED_FORMAT, *PWINBIO_REGISTERED_FORMAT;
````


## -struct-fields
<dl>

### -field <b>Owner</b>

<dd>
<p>Specifies format owner.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>Specifies format type.</p>
</dd>
</dl>

## -remarks
<p>For Windows, the format owner is defined as follows:</p>

<p>The Type for the standard Windows fingerprint format is:</p>

<p>WBDI drivers for fingerprint sensors must support the Owner and Type for the Windows fingerprint data format. The Windows Biometric Service (WBS) verifies that a sensor minimally supports the Windows fingerprint raw data format.  Windows defines this standard raw data format to allow ISVs to write engine adapters that can take input from any sensor.  Each engine should have a capability to support at least this format, but it can specify a different format as a preferred raw format.</p>

<p>No format owner or type are defined as follows:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winbio_types.h</dt>
</dl>
</td>
</tr>
</table>