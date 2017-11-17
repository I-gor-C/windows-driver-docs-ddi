---
UID: NS.nfcsedev._SECURE_ELEMENT_ENDPOINT_LIST
title: SECURE_ELEMENT_ENDPOINT_LIST
author: windows-driver-content
description: The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS.
old-location: nfpdrivers\_secure_element_endpoint_list.htm
ms.assetid: 0F69EE38-C124-47A6-B3CA-31F089657894
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: nfpdrivers
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_ENDPOINT_LIST
req.alt-loc: nfcsedev.h
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
ms.keywords: SECURE_ELEMENT_ENDPOINT_LIST, SECURE_ELEMENT_ENDPOINT_LIST, *PSECURE_ELEMENT_ENDPOINT_LIST
req.iface: 
---

# SECURE_ELEMENT_ENDPOINT_LIST structure



## -description
<p>The output parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/dn905506">IOCTL_NFCSE_ENUM_ENDPOINTS</a>.</p>


## -syntax

````
typedef struct _SECURE_ELEMENT_ENDPOINT_LIST {
  DWORD                                                            NumberOfEndpoints;
  _Field_size_(NumberOfEndpoints)
    SECURE_ELEMENT_ENDPOINT_INFO EndpointList[ANYSIZE_ARRAY];
} SECURE_ELEMENT_ENDPOINT_LIST, *P_SECURE_ELEMENT_ENDPOINT_LIST;
````


## -struct-fields
<dl>

### -field <b>NumberOfEndpoints</b>

<dd>
<p>The number of enumerated endpoints on the NFC controller.</p>
</dd>

### -field <b>EndpointList[ANYSIZE_ARRAY]</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/dn905621">SECURE_ELEMENT_ENDPOINT_INFO</a> structures.</p>
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
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>