---
UID: NF.prcomoem.IPrintOemDriverUI.DrvUpgradeRegistrySetting
title: IPrintOemDriverUI::DrvUpgradeRegistrySetting
author: windows-driver-content
description: The IPrintOemDriverUI::DrvUpdateRegistrySetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can update device settings stored in the registry.
old-location: print\iprintoemdriverui_drvupgraderegistrysetting.htm
old-project: print
ms.assetid: 9249dd75-7d90-414a-b6b5-4be0fc4f3170
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverUI, DrvUpgradeRegistrySetting, IPrintOemDriverUI::DrvUpgradeRegistrySetting
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemDriverUI.DrvUpgradeRegistrySetting
req.alt-loc: prcomoem.h
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
req.iface: IPrintOemDriverUI
req.product: Windows 10 or later.
---

# IPrintOemDriverUI::DrvUpgradeRegistrySetting method



## -description
<p>The <code>IPrintOemDriverUI::DrvUpdateRegistrySetting</code> method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can update device settings stored in the registry.</p>


## -syntax

````
HRESULT DrvUpgradeRegistrySetting(
   HANDLE hPrinter,
   PCSTR  pFeature,
   PCSTR  pOption
);
````


## -parameters
<dl>

### -param hPrinter 

<dd>
<p>Caller-supplied printer handle.</p>
</dd>

### -param pFeature 

<dd>
<p>Caller-supplied pointer to a string identifying a printer feature name contained in the printer's <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>GPD</i></a> or <a href="wdkgloss.p#wdkgloss.postscript_printer_description__ppd_#wdkgloss.postscript_printer_description__ppd_"><i>PPD</i></a> file.</p>
</dd>

### -param pOption 

<dd>
<p>Caller-supplied pointer to a string identifying an option name, associated with the specified feature, contained in the printer's GPD or PPD file.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>The <code>IPrintOemDriverUI::DrvUpdateRegistrySetting</code> method is meant to be called from a user interface plug-in's <a href="print.iprintoemui_upgradeprinter">IPrintOemUI::UpgradePrinter</a> method, when it is necessary to update registry settings that were stored in private registry keys for an earlier version of the driver, but are now contained in a GPD or PPD file.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>