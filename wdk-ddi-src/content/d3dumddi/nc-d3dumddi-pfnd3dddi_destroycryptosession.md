---
UID: NC:d3dumddi.PFND3DDDI_DESTROYCRYPTOSESSION
title: PFND3DDDI_DESTROYCRYPTOSESSION
author: windows-driver-content
description: The DestroyCryptoSession function releases resources for the encryption session that the CreateCryptoSession function creates.
old-location: display\destroycryptosession.htm
old-project: display
ms.assetid: 4035ef73-e1a2-49e4-808d-c40c980393a4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DestroyCryptoSession, DestroyCryptoSession callback function [Display Devices], PFND3DDDI_DESTROYCRYPTOSESSION, UserModeDisplayDriver_Functions_c1fa988d-a8b7-4538-94cd-d364873f4216.xml, d3dumddi/DestroyCryptoSession, display.destroycryptosession
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: DestroyCryptoSession is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3dumddi.h
api_name:
-	DestroyCryptoSession
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DESTROYCRYPTOSESSION callback function
The <b>DestroyCryptoSession</b> function releases resources for the encryption session that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function creates.

## Syntax

```
PFND3DDDI_DESTROYCRYPTOSESSION Pfnd3dddiDestroycryptosession;

HRESULT Pfnd3dddiDestroycryptosession(
  HANDLE hDevice,
  CONST D3DDDIARG_DESTROYCRYPTOSESSION *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>DestroyCryptoSession</b> returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The encryption session is successfully destroyed. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451632">DestroyCryptoSession</a> could not allocate the required memory for it to complete.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | DestroyCryptoSession is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543028">D3DDDIARG_DESTROYCRYPTOSESSION</a>