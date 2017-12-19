---
UID: NS.IDDCX.IDDCX_OPM_REQUESTED_INFORMATION~R1
title: IDDCX_OPM_REQUESTED_INFORMATION
author: windows-driver-content
description: Gives the information requested from the OPM.
old-location: display\iddcx_opm_requested_information.htm
old-project: display
ms.assetid: 0e8c49b2-1c36-432b-aba9-bc6a739ee04d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IDDCX_OPM_REQUESTED_INFORMATION,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_OPM_REQUESTED_INFORMATION
req.alt-loc: iddcx.h
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

# IDDCX_OPM_REQUESTED_INFORMATION structure



## -description

                 Gives the information requested from the OPM.
             



## -syntax

````
typedef struct IDDCX_OPM_REQUESTED_INFORMATION {
  UINT                      Size;
  OPM_REQUESTED_INFORMATION RequestedInformation;
} IDDCX_OPM_REQUESTED_INFORMATION, *IDDCX_OPM_REQUESTED_INFORMATION;
````


## -struct-fields

### -field Size

Total size of the structure.
                 


### -field RequestedInformation

The information that was requested.
                 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>