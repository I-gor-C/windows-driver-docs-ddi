---
UID: NS.NTDDRILAPITYPES.RILUICCAPPPERSOCHECKSTATUS
title: RILUICCAPPPERSOCHECKSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccapppersocheckstatus.htm
old-project: NetVista
ms.assetid: 6438f692-75b0-4a41-a2f9-68b0fe3f23cf
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILUICCAPPPERSOCHECKSTATUS, *LPRILUICCAPPPERSOCHECKSTATUS, LPRILUICCAPPPERSOCHECKSTATUS, RILUICCAPPPERSOCHECKSTATUS
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
req.alt-api: RILUICCAPPPERSOCHECKSTATUS
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

# RILUICCAPPPERSOCHECKSTATUS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILUICCAPPPERSOCHECKSTATUS {
  DWORD                            cbSize;
  DWORD                            dwParams;
  HUICCAPP                         hUiccApp;
  DWORD                            dwPersoFeature;
  RILUICCAPPPERSOCHECKSTATUSSTATE  dwPersoCheckState;
} RILUICCAPPPERSOCHECKSTATUS, RILUICCAPPPERSOCHECKSTATUS;
````


## -struct-fields

### -field cbSize


### -field dwParams


### -field hUiccApp


### -field dwPersoFeature


### -field dwPersoCheckState


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