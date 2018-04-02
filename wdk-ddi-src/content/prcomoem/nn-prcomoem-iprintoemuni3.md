---
UID: NN:prcomoem.IPrintOemUni3
title: IPrintOemUni3
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemUni3 COM interface.
old-location: print\iprintoemuni3_interface.htm
old-project: print
ms.assetid: cf5705fb-8420-4eec-99d4-d56f192da581
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemUni3, IPrintOemUni3 interface [Print Devices], IPrintOemUni3 interface [Print Devices], described, prcomoem/IPrintOemUni3, print.iprintoemuni3_interface, print_unidrv-pscript_rendering_631f975d-1d52-4db8-8e90-71cdb99f4ef1.xml
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
req.lib: 
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
-	IPrintOemUni3
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemUni3 interface

This section describes the methods defined for the <b>IPrintOemUni3</b> COM interface.

The <b>IPrintOemUni3</b> COM interface includes its own methods as well as those that belong to <a href="https://msdn.microsoft.com/097366a0-2ded-435c-9b63-2b736b716032">IPrintOemUni</a> COM interface and the <a href="https://msdn.microsoft.com/789ca699-89b3-41d3-9167-812f1a9eb3bc">IPrintOemUni2</a> COM interface.

The <b>IPrintOemUni3</b> COM interface is available in Windows Vista and later.

## Methods

<p>The <b>IPrintOemUni3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemUni3::DownloadPattern](nf-prcomoem-iprintoemuni3-downloadpattern.md) | The IPrintOemUni3::DownloadPattern method downloads a pattern to a printer. |
| [IPrintOemUni3::GetImplementedMethod](nf-prcomoem-iprintoemuni3-getimplementedmethod.md) | The IPrintOemUni3::GetImplementedMethod method is used by Unidrv to determine which IPrintOemUni interface methods a rendering plug-in has implemented. |
| [IPrintOemUni3::GetPDEVAdjustment](nf-prcomoem-iprintoemuni3-getpdevadjustment.md) | The IPrintOemUni3::GetPDEVAdjustment method enables a plug-in to override specific PDEV settings. |
| [IPrintOemUni3::SetBandSize](nf-prcomoem-iprintoemuni3-setbandsize.md) | The IPrintOemUni3::SetBandSize method can be used with Unidrv-supported printers to specify the desired band size on the printed output. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |