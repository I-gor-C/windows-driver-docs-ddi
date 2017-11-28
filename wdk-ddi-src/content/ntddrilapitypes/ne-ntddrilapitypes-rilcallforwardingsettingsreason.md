---
UID: NE.ntddrilapitypes.RILCALLFORWARDINGSETTINGSREASON
title: RILCALLFORWARDINGSETTINGSREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallforwardingsettingsreason.htm
old-project: netvista
ms.assetid: d1c39f60-15fb-450d-b879-fb5d236fcf45
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
req.alt-api: RILCALLFORWARDINGSETTINGSREASON
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

# RILCALLFORWARDINGSETTINGSREASON enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLFORWARDINGSETTINGSREASON { 
  RIL_FWDREASON_MOBILEBUSY,
  RIL_FWDREASON_NOREPLY,
  RIL_FWDREASON_UNREACHABLE,
  RIL_FWDREASON_ALLFORWARDING,
  RIL_FWDREASON_ALLCONDITIONAL,
  RIL_FWDREASON_MAX
} RILCALLFORWARDINGSETTINGSREASON;
````


## -enum-fields
<dl>

### -field <a id="RIL_FWDREASON_MOBILEBUSY"></a><a id="ril_fwdreason_mobilebusy"></a><b>RIL_FWDREASON_MOBILEBUSY</b>

<dd></dd>

### -field <a id="RIL_FWDREASON_NOREPLY"></a><a id="ril_fwdreason_noreply"></a><b>RIL_FWDREASON_NOREPLY</b>

<dd></dd>

### -field <a id="RIL_FWDREASON_UNREACHABLE"></a><a id="ril_fwdreason_unreachable"></a><b>RIL_FWDREASON_UNREACHABLE</b>

<dd></dd>

### -field <a id="RIL_FWDREASON_ALLFORWARDING"></a><a id="ril_fwdreason_allforwarding"></a><b>RIL_FWDREASON_ALLFORWARDING</b>

<dd></dd>

### -field <a id="RIL_FWDREASON_ALLCONDITIONAL"></a><a id="ril_fwdreason_allconditional"></a><b>RIL_FWDREASON_ALLCONDITIONAL</b>

<dd></dd>

### -field <a id="RIL_FWDREASON_MAX"></a><a id="ril_fwdreason_max"></a><b>RIL_FWDREASON_MAX</b>

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