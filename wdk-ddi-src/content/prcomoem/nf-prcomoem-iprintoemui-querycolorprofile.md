---
UID: NF.prcomoem.IPrintOemUI.QueryColorProfile
title: IPrintOemUI::QueryColorProfile
author: windows-driver-content
description: The IPrintOemUI::QueryColorProfile method allows a user interface plug-in to specify an ICC profile to use for color management.
old-location: print\iprintoemui_querycolorprofile.htm
old-project: print
ms.assetid: ce1131f9-4b9c-4f20-afc9-514ccbc7ecf7
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, QueryColorProfile, IPrintOemUI::QueryColorProfile
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
req.alt-api: IPrintOemUI.QueryColorProfile
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
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::QueryColorProfile method



## -description
<p>The <code>IPrintOemUI::QueryColorProfile</code> method allows a user interface plug-in to specify an ICC profile to use for color management.</p>


## -syntax

````
HRESULT QueryColorProfile(
   HANDLE    hPrinter,
   POEMUIOBJ poemuiobj,
   PDEVMODE  pPublicDM,
   PVOID     pOEMDM,
   ULONG     ulQueryMode,
   VOID      *pvProfileData,
   ULONG     *pcbProfileData,
   FLONG     *pflProfileData
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> 

<dd>
<p>Caller-supplied printer handle.</p>
</dd>

### -param <i>poemuiobj</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>pPublicDM</i> 

<dd>
<p>Caller-supplied pointer to a validated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</dd>

### -param <i>pOEMDM</i> 

<dd>
<p>Caller-supplied pointer to the user interface plug-in's private DEVMODEW structure members.</p>
</dd>

### -param <i>ulQueryMode</i> 

<dd>
<p>One of the following caller-supplied bit flags, indicating the type of profile to be specified.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>QCP_DEVICEPROFILE</p>
</td>
<td>
<p>The caller is requesting a device profile.</p>
</td>
</tr>
<tr>
<td>
<p>QCP_SOURCEPROFILE</p>
</td>
<td>
<p>The caller is requesting a source profile.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pvProfileData</i> 

<dd>
<p>Caller-supplied pointer to a buffer to receive profile information.</p>
</dd>

### -param <i>pcbProfileData</i> 

<dd>
<p>Caller-supplied pointer to a value representing the size, in bytes, of the buffer pointed to by <i>pvProfileData</i>.</p>
</dd>

### -param <i>pflProfileData</i> 

<dd>
<p>One of the following method-supplied bit flags, indicating the type of information the method is returning.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>QCP_PROFILEDISK</p>
</td>
<td>
<p>The method is returning the file name of an ICC profile in the buffer pointed to by <i>pvProfileData</i>.</p>
</td>
</tr>
<tr>
<td>
<p>QCP_PROFILEMEMORY</p>
</td>
<td>
<p>The method is returning profile data in the buffer pointed to by <i>pvProfileData</i>.</p>
</td>
</tr>
</table>
<p> </p>
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
<p>A user interface plug-in's <code>IPrintOemUI::QueryColorProfile</code> method performs the same types of operations as the <b>DrvQueryColorProfile</b> function that is exported by user-mode printer interface DLLs. For information about printer events and how they should be processed, see the description of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548573">DrvQueryColorProfile</a> function.</p>

<p>If you provide a user interface plug-in, the printer driver's <b>DrvQueryColorProfile</b> function calls the <code>IPrintOemUI::QueryColorProfile</code> method. The <b>DrvQueryColorProfile</b> function performs its own processing for the specified event, and then calls the <code>IPrintOemUI::QueryColorProfile</code> method to handle additional processing of the event.</p>

<p>If <code>IPrintOemUI::QueryColorProfile</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

<p>A user interface plug-in's <code>IPrintOemUI::QueryColorProfile</code> method performs the same types of operations as the <b>DrvQueryColorProfile</b> function that is exported by user-mode printer interface DLLs. For information about printer events and how they should be processed, see the description of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548573">DrvQueryColorProfile</a> function.</p>

<p>If you provide a user interface plug-in, the printer driver's <b>DrvQueryColorProfile</b> function calls the <code>IPrintOemUI::QueryColorProfile</code> method. The <b>DrvQueryColorProfile</b> function performs its own processing for the specified event, and then calls the <code>IPrintOemUI::QueryColorProfile</code> method to handle additional processing of the event.</p>

<p>If <code>IPrintOemUI::QueryColorProfile</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

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