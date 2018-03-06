---
UID: NN:prcomoem.IPrintOemDriverPS
title: IPrintOemDriverPS
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemDriverPS COM Interface.
old-location: print\iprintoemdriverps_interface.htm
old-project: print
ms.assetid: 39f791e6-aae3-46f6-8195-c165761d0df5
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemDriverPS, IPrintOemDriverPS interface [Print Devices], IPrintOemDriverPS interface [Print Devices], described, prcomoem/IPrintOemDriverPS, print.iprintoemdriverps_interface, print_unidrv-pscript_rendering_a44b8943-0472-41da-9e5b-2f82d34e1f9a.xml
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
-	IPrintOemDriverPS
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemDriverPS interface

This section describes the methods defined for the IPrintOemDriverPS COM Interface.

## Methods

<p>The <b>IPrintOemDriverPS</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemDriverPS::DrvGetDriverSetting](nf-prcomoem-iprintoemdriverps-drvgetdriversetting.md) | The IPrintOemDriverPS::DrvGetDriverSetting method is provided by the Pscript5 driver so that rendering plug-ins can obtain the current status of printer features and other internal information. |
| [IPrintOemDriverPS::DrvWriteSpoolBuf](nf-prcomoem-iprintoemdriverps-drvwritespoolbuf.md) | The IPrintOemDriverPS::DrvWriteSpoolBuf method is provided by the Pscript5 driver so that rendering plug-ins can send printer data to the spooler. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |