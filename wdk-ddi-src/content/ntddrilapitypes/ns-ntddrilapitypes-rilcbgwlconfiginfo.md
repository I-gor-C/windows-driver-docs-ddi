---
UID: NS.NTDDRILAPITYPES.RILCBGWLCONFIGINFO
title: RILCBGWLCONFIGINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcbgwlconfiginfo.htm
old-project: NetVista
ms.assetid: b92f6639-bf6a-4c1b-a0a6-57e310251591
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILCBGWLCONFIGINFO, LPRILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO, *LPRILCBGWLCONFIGINFO
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
req.alt-api: RILCBGWLCONFIGINFO
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

# RILCBGWLCONFIGINFO structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILCBGWLCONFIGINFO {
  BOOL      fAccept;
  RILRANGE  rgrrBroadcastMsgID;
} RILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO;
````


## -struct-fields

### -field fAccept


### -field rgrrBroadcastMsgID


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