---
UID: NN:prcomoem.IPrintOemDriverUni
title: IPrintOemDriverUni
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemDriverUni COM interface.
old-location: print\iprintoemdriveruni_interface.htm
old-project: print
ms.assetid: efd13e9e-ba25-4d1c-894c-a275374f5266
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemDriverUni, IPrintOemDriverUni interface [Print Devices], IPrintOemDriverUni interface [Print Devices], described, prcomoem/IPrintOemDriverUni, print.iprintoemdriveruni_interface, print_unidrv-pscript_rendering_07d60c45-4913-4cac-b65d-31737752b24f.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: prcomoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
req.lib: prcomoem.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	prcomoem.h
api_name:
-	IPrintOemDriverUni
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemDriverUni interface

This section describes the methods defined for the IPrintOemDriverUni COM interface.

## Methods

<p>The <b>IPrintOemDriverUni</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemDriverUni::DrvGetDriverSetting](nf-prcomoem-iprintoemdriveruni-drvgetdriversetting.md) | The IPrintOemDriverUni::DrvGetDriverSetting method is provided by the Unidrv driver so that rendering plug-ins can obtain the current status of printer features and other internal information. |
| [IPrintOemDriverUni::DrvGetGPDData](nf-prcomoem-iprintoemdriveruni-drvgetgpddata.md) | The IPrintOemDriverUni::DrvGetGPDData method is provided by the Unidrv driver so that rendering plug-ins can obtain data defined in a printer's GPD file. |
| [IPrintOemDriverUni::DrvGetStandardVariable](nf-prcomoem-iprintoemdriveruni-drvgetstandardvariable.md) | The IPrintOemDriverUni::DrvGetStandardVariable method is provided by the Unidrv driver so that rendering plug-ins can obtain the current value of Unidrv's standard variables. |
| [IPrintOemDriverUni::DrvUniTextOut](nf-prcomoem-iprintoemdriveruni-drvunitextout.md) | The IPrintOemDriverUni::DrvUniTextOut method is provided by the Unidrv driver so that a rendering plug-in using a device-managed drawing surface can easily output text strings. |
| [IPrintOemDriverUni::DrvWriteAbortBuf](nf-prcomoem-iprintoemdriveruni-drvwriteabortbuf.md) | The IPrintOemDriverUni::DrvWriteAbortBuf method is provided by the Unidrv driver to allow an OEM rendering plug-in to send printer clean-up code after a user terminates a print job. |
| [IPrintOemDriverUni::DrvWriteSpoolBuf](nf-prcomoem-iprintoemdriveruni-drvwritespoolbuf.md) | The IPrintOemDriverUni::DrvWriteSpoolBuf method is provided by the Unidrv driver so that a rendering plug-in can send printer data to the spooler. |
| [IPrintOemDriverUni::DrvXMoveTo](nf-prcomoem-iprintoemdriveruni-drvxmoveto.md) | The IPrintOemDriverUni::DrvXMoveTo method is provided by the Unidrv driver so that a rendering plug-in can notify the driver of cursor x-position changes. |
| [IPrintOemDriverUni::DrvYMoveTo](nf-prcomoem-iprintoemdriveruni-drvymoveto.md) | The IPrintOemDriverUni::DrvYMoveTo method is provided by the Unidrv driver so that a rendering plug-in can notify the driver of cursor y-position changes. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |