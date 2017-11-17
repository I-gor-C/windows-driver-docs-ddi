---
UID: NE.rilapitypes.RILSUPSERVICEDATASTATUS
title: RILSUPSERVICEDATASTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedatastatus_2.htm
ms.assetid: 9879db5b-25c1-451c-bb50-37e85cf1f5e5
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSUPSERVICEDATASTATUS
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILSUPSERVICEDATASTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILSUPSERVICEDATASTATUS { 
  RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED,
  RIL_SUPSVCDATASTATUS_TIMEOUT,
  RIL_SUPSVCDATASTATUS_ERROR,
  RIL_SUPSVCDATASTATUS_MAX
} RILSUPSERVICEDATASTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED"></a><a id="ril_supsvcdatastatus_furtherinforequired"></a><b>RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED</b>

<dd></dd>

### -field <a id="RIL_SUPSVCDATASTATUS_TIMEOUT"></a><a id="ril_supsvcdatastatus_timeout"></a><b>RIL_SUPSVCDATASTATUS_TIMEOUT</b>

<dd></dd>

### -field <a id="RIL_SUPSVCDATASTATUS_ERROR"></a><a id="ril_supsvcdatastatus_error"></a><b>RIL_SUPSVCDATASTATUS_ERROR</b>

<dd></dd>

### -field <a id="RIL_SUPSVCDATASTATUS_MAX"></a><a id="ril_supsvcdatastatus_max"></a><b>RIL_SUPSVCDATASTATUS_MAX</b>

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