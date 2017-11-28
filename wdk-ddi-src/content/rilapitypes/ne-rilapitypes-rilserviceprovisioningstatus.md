---
UID: NE.rilapitypes.RILSERVICEPROVISIONINGSTATUS
title: RILSERVICEPROVISIONINGSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilserviceprovisioningstatus_2.htm
old-project: netvista
ms.assetid: 044d89f7-6167-4e85-b4b4-d706a1499480
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
req.alt-api: RILSERVICEPROVISIONINGSTATUS
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

# RILSERVICEPROVISIONINGSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILSERVICEPROVISIONINGSTATUS { 
  RIL_SVCPROV_NOTPROVISIONED,
  RIL_SVCPROV_PROVISIONED,
  RIL_SVCPROV_TEMPMODERESTRICTED,
  RIL_SVCPROV_TEMPMODEALLOWED,
  RIL_SVCPROV_MAX
} RILSERVICEPROVISIONINGSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_SVCPROV_NOTPROVISIONED"></a><a id="ril_svcprov_notprovisioned"></a><b>RIL_SVCPROV_NOTPROVISIONED</b>

<dd></dd>

### -field <a id="RIL_SVCPROV_PROVISIONED"></a><a id="ril_svcprov_provisioned"></a><b>RIL_SVCPROV_PROVISIONED</b>

<dd></dd>

### -field <a id="RIL_SVCPROV_TEMPMODERESTRICTED"></a><a id="ril_svcprov_tempmoderestricted"></a><b>RIL_SVCPROV_TEMPMODERESTRICTED</b>

<dd></dd>

### -field <a id="RIL_SVCPROV_TEMPMODEALLOWED"></a><a id="ril_svcprov_tempmodeallowed"></a><b>RIL_SVCPROV_TEMPMODEALLOWED</b>

<dd></dd>

### -field <a id="RIL_SVCPROV_MAX"></a><a id="ril_svcprov_max"></a><b>RIL_SVCPROV_MAX</b>

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