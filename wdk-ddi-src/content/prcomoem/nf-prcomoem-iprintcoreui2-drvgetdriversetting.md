---
UID: NF.prcomoem.IPrintCoreUI2.DrvGetDriverSetting
title: IPrintCoreUI2::DrvGetDriverSetting
author: windows-driver-content
description: The IPrintCoreUI2::DrvGetDriverSetting method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can obtain the current status of printer features and other internal information.
old-location: print\iprintcoreui2_drvgetdriversetting.htm
old-project: print
ms.assetid: 501ff6f1-c5f1-4ad7-be96-a95ba3e34622
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, DrvGetDriverSetting, IPrintCoreUI2::DrvGetDriverSetting
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
req.alt-api: IPrintCoreUI2.DrvGetDriverSetting
req.alt-loc: Prcomoem.h
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
req.iface: IPrintCoreUI2
req.product: Windows 10 or later.
---

# IPrintCoreUI2::DrvGetDriverSetting method



## -description
<p>The <code>IPrintCoreUI2::DrvGetDriverSetting</code> method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can obtain the current status of printer features and other internal information.</p>


## -syntax

````
STDMETHOD DrvGetDriverSetting(
   PVOID  pci ,
   PCSTR  Feature,
   PVOID  pOutput,
   DWORD  cbSize,
   PDWORD pcbNeeded ,
   PDWORD pdwOptionsReturned 
);
````


## -parameters
<dl>

### -param <i>pci </i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure. </p>
</dd>

### -param <i>Feature</i> 

<dd>
<p>Caller-supplied value identifying the printer feature for which option settings are returned. This can be either a string pointer or a constant, as described in the following Remarks section.</p>
</dd>

### -param <i>pOutput</i> 

<dd>
<p>Caller-supplied pointer to a buffer to receive the specified information. </p>
</dd>

### -param <i>cbSize</i> 

<dd>
<p>Caller-supplied size, in bytes, of the buffer pointed to by <i>pOutput</i>.</p>
</dd>

### -param <i>pcbNeeded </i> 

<dd>
<p>Caller-supplied pointer to a location to receive the minimum buffer size required to contain the requested information. </p>
</dd>

### -param <i>pdwOptionsReturned </i> 

<dd>
<p>Caller-supplied pointer to a location to receive the number of option strings placed in <i>pOutput</i>.</p>
</dd>
</dl>

## -returns
<p>This method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>This method is inherited from the <a href="NULL">IPrintOemDriverUI COM Interface</a>, and can be called only by Windows XP and later Pscript5 UI plug-ins that do not fully replace the core driver's standard UI pages, and is supported during the UI plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines. When this method is supported, it has the same behavior as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553114">IPrintOemDriverUI::DrvGetDriverSetting</a>. When it is not supported, this method should return E_NOTIMPL.</p>

<p>This method is inherited from the <a href="NULL">IPrintOemDriverUI COM Interface</a>, and can be called only by Windows XP and later Pscript5 UI plug-ins that do not fully replace the core driver's standard UI pages, and is supported during the UI plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines. When this method is supported, it has the same behavior as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553114">IPrintOemDriverUI::DrvGetDriverSetting</a>. When it is not supported, this method should return E_NOTIMPL.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553114">IPrintOemDriverUI::DrvGetDriverSetting</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::DrvGetDriverSetting method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
