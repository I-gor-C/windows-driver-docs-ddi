---
UID: NN:prcomoem.IPrintOemPS
title: IPrintOemPS
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemPS COM interface.
old-location: print\iprintoemps_interface.htm
old-project: print
ms.assetid: 14c545b7-8080-424f-9164-f97ef8a1acc2
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemPS, IPrintOemPS interface [Print Devices], IPrintOemPS interface [Print Devices], described, prcomoem/IPrintOemPS, print.iprintoemps_interface, print_unidrv-pscript_rendering_f48d01c9-e49f-40b6-90ab-6904f0081305.xml
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
-	IPrintOemPS
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemPS interface

This section describes the methods defined for the <b>IPrintOemPS</b> COM interface.

## Methods

<p>The <b>IPrintOemPS</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemPS::Command](nf-prcomoem-iprintoemps-command.md) | The IPrintOemPS::Command method is used by rendering plug-ins for the Microsoft PostScript printer driver, in order to insert PostScript commands into the print job's data stream. |
| [IPrintOemPS::DevMode](nf-prcomoem-iprintoemps-devmode.md) | The IPrintOemPS::DevMode method, provided by rendering plug-ins for Pscript5, performs operations on private DEVMODEW members. |
| [IPrintOemPS::DisableDriver](nf-prcomoem-iprintoemps-disabledriver.md) | The IPrintOemPS::DisableDriver method allows a rendering plug-in for Pscript to free resources that were allocated by the plug-in's IPrintOemPS::EnableDriver method. |
| [IPrintOemPS::DisablePDEV](nf-prcomoem-iprintoemps-disablepdev.md) | The IPrintOemPS::DisablePDEV method allows a rendering plug-in for Pscript5 to delete the private PDEV structure that was allocated by its IPrintOemPS::EnablePDEV method. |
| [IPrintOemPS::EnableDriver](nf-prcomoem-iprintoemps-enabledriver.md) | The IPrintOemPS::EnableDriver method allows a rendering plug-in for Pscript to hook out some graphics DDI functions. |
| [IPrintOemPS::EnablePDEV](nf-prcomoem-iprintoemps-enablepdev.md) | The IPrintOemPS::EnablePDEV method allows a rendering plug-in for Pscript5 to create its own PDEV structure. |
| [IPrintOemPS::GetInfo](nf-prcomoem-iprintoemps-getinfo.md) | A rendering plug-in's IPrintOemPS::GetInfo method returns identification information. |
| [IPrintOemPS::PublishDriverInterface](nf-prcomoem-iprintoemps-publishdriverinterface.md) | The IPrintOemPS::PublishDriverInterface method allows a rendering plug-in for Pscript5 to obtain the Pscript5 driver's IPrintCorePS2, IPrintOemDriverPS, or IPrintCoreHelperPS interface. |
| [IPrintOemPS::ResetPDEV](nf-prcomoem-iprintoemps-resetpdev.md) | The IPrintOemPS::ResetPDEV method allows a rendering plug-in for Pscript5 to reset its PDEV structure. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |