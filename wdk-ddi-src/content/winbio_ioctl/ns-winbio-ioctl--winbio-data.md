---
UID: NS.winbio_ioctl._WINBIO_DATA
title: WINBIO_DATA
author: windows-driver-content
description: The WINBIO_DATA structure specifies data in IOCTL payloads.
old-location: biometric\winbio_data.htm
ms.assetid: 00dc716c-621f-4312-bf53-6bc3ab492faa
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: biometric
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_DATA
req.alt-loc: winbio_ioctl.h
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
ms.keywords: WINBIO_DATA, WINBIO_DATA, *PWINBIO_DATA
req.iface: 
req.product: Windows 10 or later.
---

# WINBIO_DATA structure



## -description
<p>The WINBIO_DATA structure specifies data in IOCTL payloads.</p>


## -syntax

````
typedef struct _WINBIO_DATA {
  DWORD Size;
  BYTE  Data[1];
} WINBIO_DATA, *PWINBIO_DATA;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of the payload.</p>
</dd>

### -field <b>Data</b>

<dd>
<p>Specifies an array that contains the payload. Frequently this member contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536459">WINBIO_BIR</a>.</p>
</dd>
</dl>

## -remarks
<p>The WINBIO_DATA structure associates a length, in bytes, with an arbitrary block of contiguous memory.</p>

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
<dt>Winbio_ioctl.h</dt>
</dl>
</td>
</tr>
</table>