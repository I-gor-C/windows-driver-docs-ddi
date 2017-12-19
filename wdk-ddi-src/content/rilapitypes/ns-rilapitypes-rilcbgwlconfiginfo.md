---
UID: NS.RILAPITYPES.RILCBGWLCONFIGINFO
title: RILCBGWLCONFIGINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcbgwlconfiginfo_2.htm
old-project: NetVista
ms.assetid: 5939b967-bbc7-42e3-af90-a1c20698a934
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO, *LPRILCBGWLCONFIGINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCBGWLCONFIGINFO
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
req.product: Windows 10 or later.
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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>