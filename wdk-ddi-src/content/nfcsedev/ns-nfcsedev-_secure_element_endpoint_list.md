---
UID: NS.NFCSEDEV._SECURE_ELEMENT_ENDPOINT_LIST
title: _SECURE_ELEMENT_ENDPOINT_LIST
author: windows-driver-content
description: The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS.
old-location: nfpdrivers\_secure_element_endpoint_list.htm
old-project: nfpdrivers
ms.assetid: 0F69EE38-C124-47A6-B3CA-31F089657894
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _SECURE_ELEMENT_ENDPOINT_LIST, *PSECURE_ELEMENT_ENDPOINT_LIST, PSECURE_ELEMENT_ENDPOINT_LIST, SECURE_ELEMENT_ENDPOINT_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# _SECURE_ELEMENT_ENDPOINT_LIST structure



## -description
The output parameter for <a href="..\nfcsedev\ni-nfcsedev-ioctl_nfcse_enum_endpoints.md">IOCTL_NFCSE_ENUM_ENDPOINTS</a>.



## -syntax

````
typedef struct _SECURE_ELEMENT_ENDPOINT_LIST {
  DWORD                                                            NumberOfEndpoints;
  _Field_size_(NumberOfEndpoints)
    SECURE_ELEMENT_ENDPOINT_INFO EndpointList[ANYSIZE_ARRAY];
} SECURE_ELEMENT_ENDPOINT_LIST, *P_SECURE_ELEMENT_ENDPOINT_LIST;
````


## -struct-fields

### -field NumberOfEndpoints

The number of enumerated endpoints on the NFC controller.


### -field EndpointList[ANYSIZE_ARRAY]

An array of <a href="nfpdrivers._secure_element_endpoint_info">SECURE_ELEMENT_ENDPOINT_INFO</a> structures.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>