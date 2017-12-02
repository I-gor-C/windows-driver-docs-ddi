---
UID: NE.ehstorioctl._PDO_STATE
title: PDO_STATE
author: windows-driver-content
description: This enumeration describes the states of Physical Device Objects (PDOs).
old-location: storage\pdo_state.htm
old-project: storage
ms.assetid: 006e2cef-4e49-4819-bfce-d9bf5983643e
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
req.alt-api: PDO_STATE
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

# PDO_STATE enumeration



## -description
<p>This enumeration describes the states of Physical Device Objects (PDOs).</p>


## -syntax

````
typedef enum _PDO_STATE { 
  PDO_STATE_UNDEFINED    = 0,
  PDO_STATE_STARTED      = 1,
  PDO_STATE_NOT_STARTED  = 2
} PDO_STATE;
````


## -enum-fields
<dl>

### -field PDO_STATE_UNDEFINED

<dd>
<p>This value indicates that the PDO state is undefined.</p>
</dd>

### -field PDO_STATE_STARTED

<dd>
<p>This value indicates that the PDO is started.</p>
</dd>

### -field PDO_STATE_NOT_STARTED

<dd>
<p>This value indicates that the PDO is not started.</p>
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
<dt>EhStorIoctl.h (include EhStorIoctl.h)</dt>
</dl>
</td>
</tr>
</table>