---
UID: NE.rilapitypes.RILSENDMSGOPTIONS
title: RILSENDMSGOPTIONS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsendmsgoptions_2.htm
old-project: netvista
ms.assetid: 84d13b43-06c4-4454-9853-80b1fe65d29d
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
req.alt-api: RILSENDMSGOPTIONS
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

# RILSENDMSGOPTIONS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILSENDMSGOPTIONS { 
  RIL_SENDOPT_PERSISTLINK,
  RIL_SENDOPT_IMS
} RILSENDMSGOPTIONS;
````


## -enum-fields
<dl>

### -field <a id="RIL_SENDOPT_PERSISTLINK"></a><a id="ril_sendopt_persistlink"></a><b>RIL_SENDOPT_PERSISTLINK</b>

<dd></dd>

### -field <a id="RIL_SENDOPT_IMS"></a><a id="ril_sendopt_ims"></a><b>RIL_SENDOPT_IMS</b>

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