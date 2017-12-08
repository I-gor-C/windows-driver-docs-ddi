---
UID: NS.NDIS._NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO
title: _NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO
author: windows-driver-content
description: The NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO structure specifies media-specific information that is reserved for system use with native 802.11 drivers. Do not use this structure.
old-location: netvista\ndis_net_buffer_list_media_specific_info.htm
old-project: netvista
ms.assetid: cae95c4f-0af3-49de-a312-83958896006a
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO, NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO, *PNDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
---

# _NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO structure



## -description
The NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO structure specifies media-specific information that is
    reserved for system use with native 802.11 drivers. Do not use this structure.


## -syntax

````
typedef struct _NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO {
  union {
    PVOID MediaSpecificInfo;
    PVOID NativeWifiSpecificInfo;
    PVOID Value;
  };
} NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO, *PNDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO;
````


## -struct-fields

### -field MediaSpecificInfo


### -field NativeWifiSpecificInfo


### -field Value


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>