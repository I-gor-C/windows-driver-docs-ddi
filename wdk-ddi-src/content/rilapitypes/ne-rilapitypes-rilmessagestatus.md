---
UID: NE.rilapitypes.RILMESSAGESTATUS
title: RILMESSAGESTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessagestatus_2.htm
old-project: netvista
ms.assetid: 30ae1eff-447c-4f6f-8f6c-cd8bc657d32d
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
req.alt-api: RILMESSAGESTATUS
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

# RILMESSAGESTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMESSAGESTATUS { 
  RIL_MSGSTATUS_RECUNREAD,
  RIL_MSGSTATUS_RECREAD,
  RIL_MSGSTATUS_STOUNSENT,
  RIL_MSGSTATUS_STOSENT,
  RIL_MSGSTATUS_MAX
} RILMESSAGESTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGSTATUS_RECUNREAD"></a><a id="ril_msgstatus_recunread"></a><b>RIL_MSGSTATUS_RECUNREAD</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUS_RECREAD"></a><a id="ril_msgstatus_recread"></a><b>RIL_MSGSTATUS_RECREAD</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUS_STOUNSENT"></a><a id="ril_msgstatus_stounsent"></a><b>RIL_MSGSTATUS_STOUNSENT</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUS_STOSENT"></a><a id="ril_msgstatus_stosent"></a><b>RIL_MSGSTATUS_STOSENT</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUS_MAX"></a><a id="ril_msgstatus_max"></a><b>RIL_MSGSTATUS_MAX</b>

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