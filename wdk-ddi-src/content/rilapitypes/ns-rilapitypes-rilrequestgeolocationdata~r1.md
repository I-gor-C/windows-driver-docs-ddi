---
UID: NS.RILAPITYPES.RILREQUESTGEOLOCATIONDATA~R1
title: RILREQUESTGEOLOCATIONDATA
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrequestgeolocationdata_2.htm
old-project: NetVista
ms.assetid: 2d447c49-08ac-43c2-9f70-557494e82cfc
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILREQUESTGEOLOCATIONDATA, RILREQUESTGEOLOCATIONDATA, *LPRILREQUESTGEOLOCATIONDATA
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
req.alt-api: RILREQUESTGEOLOCATIONDATA
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

# RILREQUESTGEOLOCATIONDATA structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILREQUESTGEOLOCATIONDATA {
  DWORD                          cbSize;
  DWORD                          dwParams;
  DWORD                          dwExecutor;
  RILGEOLOCATIONTYPEMASK         dwLocationInformationMask;
  RILGEOLOCATIONREQUESTACCURACY  dwLocationRequestAccuracy;
  RILGEOLOCATIONREQUESTINFO      rrRequestInformation;
} RILREQUESTGEOLOCATIONDATA, RILREQUESTGEOLOCATIONDATA;
````


## -struct-fields

### -field cbSize


### -field dwParams


### -field dwExecutor


### -field dwLocationInformationMask


### -field dwLocationRequestAccuracy


### -field rrRequestInformation


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