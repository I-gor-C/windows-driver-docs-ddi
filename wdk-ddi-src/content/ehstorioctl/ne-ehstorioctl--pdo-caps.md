---
UID: NE.ehstorioctl._PDO_CAPS
title: PDO_CAPS
author: windows-driver-content
description: This enumeration describes the capabilities of Physical Device Objects (PDOs).
old-location: storage\pdo_caps.htm
old-project: storage
ms.assetid: 78b6f3c7-bb42-4e93-8128-28b6f8e11dda
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SET_BAND_SECURITY_PARAMETERS, SET_BAND_SECURITY_PARAMETERS, *PSET_BAND_SECURITY_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ehstorioctl.h
req.include-header: EhStorIoctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PDO_CAPS
req.alt-loc: EhStorIoctl.h
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

# PDO_CAPS enumeration



## -description
<p>This enumeration describes the capabilities of Physical Device Objects (PDOs).</p>


## -syntax

````
typedef enum _PDO_CAPS { 
  PDO_CAPABILITY_UNDEFINED     = 0,
  PDO_CAPABILITY_INC512_SET    = 1,
  PDO_CAPABILITY_INC512_CLEAR  = 2
} PDO_CAPS;
````


## -enum-fields
<dl>

### -field <a id="PDO_CAPABILITY_UNDEFINED"></a><a id="pdo_capability_undefined"></a><b>PDO_CAPABILITY_UNDEFINED</b>

<dd>
<p>Command data block size granularity is undefined.</p>
</dd>

### -field <a id="PDO_CAPABILITY_INC512_SET"></a><a id="pdo_capability_inc512_set"></a><b>PDO_CAPABILITY_INC512_SET</b>

<dd>
<p>Command data block size granularity of 512 bytes is supported.</p>
</dd>

### -field <a id="PDO_CAPABILITY_INC512_CLEAR"></a><a id="pdo_capability_inc512_clear"></a><b>PDO_CAPABILITY_INC512_CLEAR</b>

<dd>
<p>Command data block size granularity of 1 byte is supported.</p>
</dd>
</dl>

## -remarks
<p>A silo must support either PDO_CAPABILITY_INC512_SET or PDO_CAPABILITY_INC512_CLEAR. It may also indicate that both values are supported by returning a logical OR of these two bits.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>EhStorIoctl.h (include EhStorIoctl.h)</dt>
</dl>
</td>
</tr>
</table>