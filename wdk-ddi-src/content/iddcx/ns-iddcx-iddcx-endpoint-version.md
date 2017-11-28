---
UID: NS.iddcx.IDDCX_ENDPOINT_VERSION
title: IDDCX_ENDPOINT_VERSION
author: windows-driver-content
description: Gives version information about the video data endpoint.
old-location: display\iddcx_endpoint_version.htm
old-project: display
ms.assetid: ad6220e3-9b6a-4a46-978b-31edfb2c8b9b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_ENDPOINT_VERSION,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_ENDPOINT_VERSION
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_ENDPOINT_VERSION structure



## -description
<p>
                 Gives version information about the video data endpoint.
             </p>


## -syntax

````
typedef struct IDDCX_ENDPOINT_VERSION {
  UINT   Size;
  UINT   MajorVer;
  UINT   MinorVer;
  UINT   Build;
  UINT64 SKU;
} IDDCX_ENDPOINT_VERSION, *IDDCX_ENDPOINT_VERSION;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field <b>MajorVer</b>

<dd>
<p>
                     The major version defined by the driver.
                 </p>
</dd>

### -field <b>MinorVer</b>

<dd>
<p>
                     The minor version defined by the driver.
                 </p>
</dd>

### -field <b>Build</b>

<dd>
<p>
                     The build number defined by the driver.
                 </p>
</dd>

### -field <b>SKU</b>

<dd>
<p>
                     The SKU type defined by the driver.
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>