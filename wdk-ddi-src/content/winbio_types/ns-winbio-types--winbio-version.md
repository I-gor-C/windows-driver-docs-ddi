---
UID: NS.winbio_types._WINBIO_VERSION
title: WINBIO_VERSION
author: windows-driver-content
description: The WINBIO_VERSION structure describes major and minor version information for a WBDI driver.
old-location: biometric\winbio_version.htm
ms.assetid: 6a89a581-0af4-4a42-be81-fb7cb1f33bdd
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
req.alt-api: WINBIO_VERSION
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
ms.keywords: WINBIO_VERSION, WINBIO_VERSION, *PWINBIO_VERSION
req.iface: 
req.product: Windows 10 or later.
---

# WINBIO_VERSION structure



## -description
<p>The WINBIO_VERSION structure describes major and minor version information for a WBDI driver.</p>


## -syntax

````
typedef struct _WINBIO_VERSION {
  DWORD MajorVersion;
  DWORD MinorVersion;
} WINBIO_VERSION, *PWINBIO_VERSION;
````


## -struct-fields
<dl>

### -field <b>MajorVersion</b>

<dd>
<p>Identifies the major version of the driver.</p>
</dd>

### -field <b>MinorVersion</b>

<dd>
<p>Identifies the minor version of the driver.</p>
</dd>
</dl>

## -remarks


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