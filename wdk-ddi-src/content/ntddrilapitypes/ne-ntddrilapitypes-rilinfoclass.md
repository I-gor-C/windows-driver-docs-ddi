---
UID: NE.ntddrilapitypes.RILINFOCLASS
title: RILINFOCLASS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilinfoclass.htm
old-project: netvista
ms.assetid: 2e4bd8bd-ce7e-4eb4-ac0d-68fb8890eb26
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILINFOCLASS
req.alt-loc: ntddrilapitypes.h
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

# RILINFOCLASS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILINFOCLASS { 
  RIL_INFOCLASS_VOICE,
  RIL_INFOCLASS_DATA,
  RIL_INFOCLASS_FAX,
  RIL_INFOCLASS_SMS,
  RIL_INFOCLASS_DATACIRCUITSYNC,
  RIL_INFOCLASS_DATACIRCUITASYNC,
  RIL_INFOCLASS_PACKETACCESS,
  RIL_INFOCLASS_PADACCESS,
  RIL_INFOCLASS_ALL
} RILINFOCLASS;
````


## -enum-fields
<dl>

### -field <a id="RIL_INFOCLASS_VOICE"></a><a id="ril_infoclass_voice"></a><b>RIL_INFOCLASS_VOICE</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_DATA"></a><a id="ril_infoclass_data"></a><b>RIL_INFOCLASS_DATA</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_FAX"></a><a id="ril_infoclass_fax"></a><b>RIL_INFOCLASS_FAX</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_SMS"></a><a id="ril_infoclass_sms"></a><b>RIL_INFOCLASS_SMS</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_DATACIRCUITSYNC"></a><a id="ril_infoclass_datacircuitsync"></a><b>RIL_INFOCLASS_DATACIRCUITSYNC</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_DATACIRCUITASYNC"></a><a id="ril_infoclass_datacircuitasync"></a><b>RIL_INFOCLASS_DATACIRCUITASYNC</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_PACKETACCESS"></a><a id="ril_infoclass_packetaccess"></a><b>RIL_INFOCLASS_PACKETACCESS</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_PADACCESS"></a><a id="ril_infoclass_padaccess"></a><b>RIL_INFOCLASS_PADACCESS</b>

<dd></dd>

### -field <a id="RIL_INFOCLASS_ALL"></a><a id="ril_infoclass_all"></a><b>RIL_INFOCLASS_ALL</b>

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>