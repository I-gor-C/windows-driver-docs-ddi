---
UID: NF.d3dkmthk.D3DKMTCreateProtectedSession
title: D3DKMTCreateProtectedSession function
author: windows-driver-content
description: Used to create a protected session.
old-location: display\d3dkmtcreateprotectedsession.htm
old-project: display
ms.assetid: f6967f07-564b-4730-9950-4703b541165b
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3DKMTCreateProtectedSession
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTCreateProtectedSession
req.alt-loc: d3dkmthk.h
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

# D3DKMTCreateProtectedSession function



## -description

			
            Used to create a protected session.



## -syntax

````
NTSTATUS  D3DKMTCreateProtectedSession(
  _Inout_ D3DKMT_CREATEPROTECTEDSESSION  D3dkmt_createprotectedsession
);
````


## -parameters

### -param D3dkmt_createprotectedsession [in, out]

Holds information to create a protected session.


## -returns

Returns STATUS_SUCCESS if completed successfully.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">


</td>
</tr>
</table>