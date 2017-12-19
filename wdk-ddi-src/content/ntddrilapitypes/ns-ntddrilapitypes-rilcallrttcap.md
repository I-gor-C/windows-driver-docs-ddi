---
UID: NS.NTDDRILAPITYPES.RILCALLRTTCAP
title: RILCALLRTTCAP
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallrttcap.htm
old-project: NetVista
ms.assetid: 7cb8618b-93da-4b6d-8f03-fb42a8d28fd0
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILCALLRTTCAP, RILCALLRTTCAP, *LPRILCALLRTTCAP, LPRILCALLRTTCAP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLRTTCAP
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
---

# RILCALLRTTCAP structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILCALLRTTCAP {
  RILCALLRTTMODE  dwLocalRTTCap;
  RILCALLRTTMODE  dwPeerRTTCap;
} RILCALLRTTCAP, RILCALLRTTCAP;
````


## -struct-fields

### -field dwLocalRTTCap


### -field dwPeerRTTCap


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>