---
UID: NE.rilapitypes.RILSERVICESETTINGSSTATUS
title: RILSERVICESETTINGSSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilservicesettingsstatus_2.htm
old-project: netvista
ms.assetid: 4d193398-752f-4aef-8ae6-59c9afabd79a
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
req.alt-api: RILSERVICESETTINGSSTATUS
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

# RILSERVICESETTINGSSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILSERVICESETTINGSSTATUS { 
  RIL_SVCSTAT_DISABLED,
  RIL_SVCSTAT_ENABLED,
  RIL_SVCSTAT_DEFAULT,
  RIL_SVCSTAT_MAX
} RILSERVICESETTINGSSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_SVCSTAT_DISABLED"></a><a id="ril_svcstat_disabled"></a><b>RIL_SVCSTAT_DISABLED</b>

<dd></dd>

### -field <a id="RIL_SVCSTAT_ENABLED"></a><a id="ril_svcstat_enabled"></a><b>RIL_SVCSTAT_ENABLED</b>

<dd></dd>

### -field <a id="RIL_SVCSTAT_DEFAULT"></a><a id="ril_svcstat_default"></a><b>RIL_SVCSTAT_DEFAULT</b>

<dd></dd>

### -field <a id="RIL_SVCSTAT_MAX"></a><a id="ril_svcstat_max"></a><b>RIL_SVCSTAT_MAX</b>

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