---
UID: NE.rilapitypes.RILMSGCDMAMSGPRIVACY
title: RILMSGCDMAMSGPRIVACY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgprivacy_2.htm
old-project: netvista
ms.assetid: 1a143103-a952-410c-a143-153685f022dd
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
req.alt-api: RILMSGCDMAMSGPRIVACY
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

# RILMSGCDMAMSGPRIVACY enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGCDMAMSGPRIVACY { 
  RIL_MSGPRIVACYCLASS_RESTRICTED,
  RIL_MSGPRIVACYCLASS_CONFIDENTIAL,
  RIL_MSGPRIVACYCLASS_SECRET,
  RIL_MSGPRIVACYCLASS_MAX
} RILMSGCDMAMSGPRIVACY;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGPRIVACYCLASS_RESTRICTED"></a><a id="ril_msgprivacyclass_restricted"></a><b>RIL_MSGPRIVACYCLASS_RESTRICTED</b>

<dd></dd>

### -field <a id="RIL_MSGPRIVACYCLASS_CONFIDENTIAL"></a><a id="ril_msgprivacyclass_confidential"></a><b>RIL_MSGPRIVACYCLASS_CONFIDENTIAL</b>

<dd></dd>

### -field <a id="RIL_MSGPRIVACYCLASS_SECRET"></a><a id="ril_msgprivacyclass_secret"></a><b>RIL_MSGPRIVACYCLASS_SECRET</b>

<dd></dd>

### -field <a id="RIL_MSGPRIVACYCLASS_MAX"></a><a id="ril_msgprivacyclass_max"></a><b>RIL_MSGPRIVACYCLASS_MAX</b>

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