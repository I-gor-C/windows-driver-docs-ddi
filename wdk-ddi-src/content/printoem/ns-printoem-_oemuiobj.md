---
UID: NS.PRINTOEM._OEMUIOBJ
title: _OEMUIOBJ
author: windows-driver-content
description: The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins.
old-location: print\oemuiobj.htm
old-project: print
ms.assetid: ba9252ec-3aef-4e8c-a335-bde33686beae
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: _OEMUIOBJ, OEMUIOBJ, *POEMUIOBJ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OEMUIOBJ
req.alt-loc: printoem.h
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

# _OEMUIOBJ structure



## -description
The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins.



## -syntax

````
typedef struct _OEMUIOBJ {
  DWORD       cbSize;
  POEMUIPROCS pOemUIProcs;
} OEMUIOBJ, *POEMUIOBJ;
````


## -struct-fields

### -field cbSize

Size of the OEMUIOBJ structure.


### -field pOemUIProcs

Pointer to a an <a href="print.oemuiprocs">OEMUIPROCS</a> structure, which is a private, internal structure.


## -remarks
User interface plug-ins do not need to reference an OEMUIOBJ structure's members. Plug-ins receive a pointer to this structure as input to their <a href="print.iprintoemui_devicecapabilities">IPrintOemUI::DeviceCapabilities</a>, <a href="print.iprintoemui_devqueryprintex">IPrintOemUI::DevQueryPrintEx</a> and <a href="print.iprintoemui_querycolorprofile">IPrintOemUI::QueryColorProfile</a> methods. Additionally, the OEMCUIPPARAM structure contains an OEMUIOBJ structure pointer. Plug-ins must supply the received pointer when calling <a href="print.iprintoemdriverui_drvgetdriversetting">IPrintOemDriverUI::DrvGetDriverSetting</a> or <a href="print.iprintoemdriverui_drvupdateuisetting">IPrintOemDriverUI::DrvUpdateUISetting</a>.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>