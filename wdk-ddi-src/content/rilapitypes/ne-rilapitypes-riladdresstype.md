---
UID: NE.rilapitypes.RILADDRESSTYPE
title: RILADDRESSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riladdresstype_2.htm
old-project: netvista
ms.assetid: de21f647-9372-4572-bf45-581361032911
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILADDRESSTYPE
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILADDRESSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILADDRESSTYPE { 
  RIL_ADDRTYPE_INTERNATIONAL,
  RIL_ADDRTYPE_NATIONAL,
  RIL_ADDRTYPE_NETWKSPECIFIC,
  RIL_ADDRTYPE_SUBSCRIBER,
  RIL_ADDRTYPE_ALPHANUM,
  RIL_ADDRTYPE_ABBREV,
  RIL_ADDRTYPE_IP,
  RIL_ADDRTYPE_EMAIL,
  RIL_ADDRTYPE_URI,
  RIL_ADDRTYPE_MAX
} RILADDRESSTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_ADDRTYPE_INTERNATIONAL"></a><a id="ril_addrtype_international"></a><b>RIL_ADDRTYPE_INTERNATIONAL</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_NATIONAL"></a><a id="ril_addrtype_national"></a><b>RIL_ADDRTYPE_NATIONAL</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_NETWKSPECIFIC"></a><a id="ril_addrtype_netwkspecific"></a><b>RIL_ADDRTYPE_NETWKSPECIFIC</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_SUBSCRIBER"></a><a id="ril_addrtype_subscriber"></a><b>RIL_ADDRTYPE_SUBSCRIBER</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_ALPHANUM"></a><a id="ril_addrtype_alphanum"></a><b>RIL_ADDRTYPE_ALPHANUM</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_ABBREV"></a><a id="ril_addrtype_abbrev"></a><b>RIL_ADDRTYPE_ABBREV</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_IP"></a><a id="ril_addrtype_ip"></a><b>RIL_ADDRTYPE_IP</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_EMAIL"></a><a id="ril_addrtype_email"></a><b>RIL_ADDRTYPE_EMAIL</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_URI"></a><a id="ril_addrtype_uri"></a><b>RIL_ADDRTYPE_URI</b>

<dd></dd>

### -field <a id="RIL_ADDRTYPE_MAX"></a><a id="ril_addrtype_max"></a><b>RIL_ADDRTYPE_MAX</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>